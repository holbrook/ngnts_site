from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView


from rest_framework import routers

from ngnts_site.ngnts import views
from ngnts_site.ngnts import serializers


router = routers.DefaultRouter()
router.register(r'users', serializers.UserViewSet)
router.register(r'bizservices', views.BizServiceViewSet)




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^ngnts', include('ngnts_site.ngnts.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
