from django.db import models
from django.db.models import Model
from revisable_head.models import Revisable

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
class Poster(SocialModel):
    """
    An individual "account" on a tracked network
    """
    external_id = models.IntegerField()
    display_pic = models.ImageField(upload_to="dp/")
    display_name = models.CharField(max_length=255)


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
