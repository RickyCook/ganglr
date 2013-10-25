"""
API endpoints
"""

from ganglr.models import *
from ganglr.api.serializers import *

from rest_framework import viewsets
from rest_framework.decorators import link
from social.apps.django_app.default.models import UserSocialAuth

class PostersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allow viewing of posters
    """
    model = Poster
    serializer_class = PosterSerializer

class UserSocialAuthsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allow viewing of social auths
    """
    queryset = UserSocialAuth.objects.all()
    serializer_class = UserSocialAuthSerializer