from django.conf import settings
from django.db import models
from django.db.models import Model
from revisable_head.models import Revisable
from social.apps.django_app.default.models import UserSocialAuth
from social.pipeline.user import user_details as social_user_details
from social.utils import setting_name

UID_LENGTH = getattr(settings, setting_name('UID_LENGTH'), 255)

class SocialModel(Revisable, Model):
    """
    Abstract base for all social models
    """

    class Meta:
        abstract = True

    first_seen = models.DateTimeField(auto_now_add=True)


#
# People
#
def social_new_poster(strategy, details, response, user=None, *args, **kwargs):
    social_user_details(strategy, details, response, user, *args, **kwargs)
    poster, _ = Poster.objects.get_or_create(
        external_id=kwargs['uid'],
        provider=kwargs['social'].provider,
    )
    poster.user_social_auth = kwargs['social']
    poster.display_name = details['fullname']
    poster.save()


class Poster(SocialModel):
    """
    An individual "account" on a tracked network
    """

    external_id = models.CharField(max_length=UID_LENGTH)
    provider = models.CharField(max_length=32)
    user_social_auth = models.ForeignKey(UserSocialAuth, null=True)

    display_pic = models.ImageField(upload_to="dp/", null=True)
    display_name = models.CharField(max_length=255)

    def internal_auth_lookup(self):
        """
        Do a lookup for auths in the DB that match the provider/external id of
        this object (which has a chance of being out of sync)
        """
        return UserSocialAuth.objects.filter(
            uid=self.external_id,
            provider=self.provider)

    def internal_auth_reassociate(self):
        """
        Look up and associate with the first matched auth matching provider/
        external id of this object
        """
        try:
            self.user_social_auth = self.internal_auth_lookup()[0]
        except IndexError:
            return False


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
