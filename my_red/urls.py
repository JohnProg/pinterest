from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    	                {'document_root' : settings.MEDIA_ROOT, }),
                        #
                        url(r'^', include('apps.myuser.urls')),
                        # url(r'^post/', include('apps.post.urls')),
)