from ganglr.api.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posters', PostersViewSet)
router.register(r'user_social_auths', UserSocialAuthsViewSet)
