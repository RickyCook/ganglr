from ganglr.models import *

from rest_framework import serializers
from social.apps.django_app.default.models import UserSocialAuth

class PosterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poster
        fields = ('provider',
                  'external_id',
                  'user_social_auth',
                  'display_pic',
                  'display_name')

class UserSocialAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSocialAuth
        fields = ('provider',
                  'uid',
                  'extra_data')
