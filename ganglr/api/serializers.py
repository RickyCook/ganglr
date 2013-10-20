from ganglr.models import *

from rest_framework import serializers

class PosterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poster
        fields = ('external_id', 'display_pic', 'display_name')
