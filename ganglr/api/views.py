"""
API endpoints
"""

from ganglr.models import *
from ganglr.api.serializers import *

from rest_framework import viewsets

class PosterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allow viewing of posters
    """
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
