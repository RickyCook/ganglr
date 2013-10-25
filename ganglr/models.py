from django.conf import settings
from django.db import models
from django.db.models import Model
from jsonpath_rw import jsonpath, parse as jsonpath_expr
from social.apps.django_app.default.models import UserSocialAuth
from social.pipeline.user import user_details as social_user_details
from social.utils import setting_name

import urllib

UID_LENGTH = getattr(settings, setting_name('UID_LENGTH'), 255)

class SocialModel(Model):
    """
    Abstract base for all social models
    """

    class Meta:
        abstract = True

    external_id = models.CharField(max_length=UID_LENGTH)
    first_seen = models.DateTimeField(auto_now_add=True)
    access_via = models.ForeignKey(UserSocialAuth, null=True)

    raw_data_mapping = None

    def __init__(self, facebook_data=None, *args, **kwargs):
        merged_kwargs = self.raw_to_kwargs(facebook_data).update(kwargs)
        super(SocialModel, self).__init__(*args, **merged_kwargs)

    def raw_to_kwargs(self, data):
        """
        Convert raw data retrieved from Facebook and convert it to kwargs
        suitable for setting fields in this model
        """

        if not self.raw_data_mapping:
            raise NotImplementedError("Must set raw_data_mapping in child class")

        if not data:
            return {}

        kwargs = {}

        for attr, path in data.iteritems():
            val = path.find(data)
            if len(val) == 1:
                kwargs[attr] = val[0]
            elif len(val) > 1:
                kwangs[attr] = val

        return kwargs

    def set_data(self, **kwargs):
        """
        Set data by kwargs, like happens in __init__
        """

        for field, val in kwargs.iteritems():
            setattr(self, field, val)

    def refresh_from_raw(self, data):
        """
        Refresh this model's data based on raw data retrieved from facebook
        """

        self.set_data(self.raw_to_kwargs(data))

    def graph_api(self):
        """
        Retrieve a GraphAPI relevant to this object
        """
        return GraphAPI(self.access_via.tokens)

#
# People
#
def social_new_poster(strategy, details, response, user=None, *args, **kwargs):
    print "CREATE NEW POSTER FOR %s" % kwargs['uid']
    social_user_details(strategy, details, response, user, *args, **kwargs)
    poster, _ = Poster.objects.get_or_create(
        external_id=kwargs['uid'],
    )
    poster.user_social_auth = kwargs['social']
    poster.display_name = details['fullname']
    poster.save()


class Poster(SocialModel):
    """
    An individual "account" on a tracked network
    """

    user_social_auth = models.ForeignKey(
        UserSocialAuth,
        null=True,
        related_name='poster_associations_set')

    display_pic = models.ImageField(upload_to="dp/", null=True)
    display_name = models.CharField(max_length=255)

    raw_data_mapping = {
        'external_id': jsonpath_expr('id'),
        'display_name': jsonpath_expr('name'),
    }

    def internal_auth_lookup(self):
        """
        Do a lookup for auths in the DB that match the provider/external id of
        this object (which has a chance of being out of sync)
        """
        return UserSocialAuth.objects.filter(uid=self.external_id)

    def internal_auth_reassociate(self):
        """
        Look up and associate with the first matched auth matching provider/
        external id of this object
        """
        try:
            self.user_social_auth = self.internal_auth_lookup()[0]
        except IndexError:
            return False

    def graph_api(self):
        if self.user_social_auth:
            return GraphAPI(self.user_social_auth.tokens)

        return super(Poster, self).graph_api()

    # TODO make this all generic
    def refresh_home(self):
        api = self.graph_api()
        feed = api.get('me/home')
        for post_data in feed['data']:
            try:
                post = Post.objects.get(external_id=post_data['id'])
            except DoesNotExist:
                post = Post(
                    facebook_data=post_data,
                    access_via=self.user_social_auth,
                )


#
# Content
#
class Post(SocialModel):
    """
    Any form of wall post, tweet, comment, etc
    """

    poster = models.ForeignKey(Poster)
    parent = models.ForeignKey('self')

    content_text = models.TextField()

    raw_data_mapping = {
        'external_id': jsonpath_expr('id'),
        'content_text': jsonpath_expr('message'),
    }


class PostMedia(Model):
    """
    Abstract base class for media that is attached to posts
    """

    class Meta:
        abstract = True

    post = models.ForeignKey(Post)


class PostImage(PostMedia):
    """
    Images attached to posts
    """

    content = models.ImageField(upload_to="post/")
    original = models.URLField()


class PostLink(PostMedia):
    """
    Links attached to posts
    """

    content = models.URLField()
