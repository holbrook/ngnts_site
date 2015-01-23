from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers

from ngnts_site.ngnts import views
from ngnts_site.ngnts import serializers
from .views import *



router = routers.DefaultRouter()
router.register(r'bizservices', views.BizServiceViewSet,base_name='abc')



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index_view),
)
