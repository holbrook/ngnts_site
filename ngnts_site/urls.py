from django.conf.urls import patterns, include, url



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('ngnts_site.ngnts.urls')),

)
