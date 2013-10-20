from ganglr.api import router as api_router

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # url(r'^$', 'ganglr.views.home', name='home'),
    # url(r'^ganglr/', include('ganglr.foo.urls')),

    url(r'^login$', 'ganglr.views.login'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1/', include(api_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
urlpatterns += staticfiles_urlpatterns()