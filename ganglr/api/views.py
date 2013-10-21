"""
API endpoints
"""

from ganglr.models import *
from ganglr.api.serializers import *

from rest_framework import viewsets
from social.apps.django_app.default.models import UserSocialAuth

class PostersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allow viewing of posters
    """
    queryset = Poster.latest.all()
    serializer_class = PosterSerializer

class UserSocialAuthsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allow viewing of social auths
    """
    queryset = UserSocialAuth.objects.all()
    serializer_class = UserSocialAuthSerializer