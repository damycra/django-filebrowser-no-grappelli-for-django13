from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    # filebrowser urls
    url(r'^browse/$', 'filebrowser.views.browse', name="fb_browse"),
    url(r'^mkdir/', 'filebrowser.views.mkdir', name="fb_mkdir"),
    url(r'^upload/', 'filebrowser.views.upload', name="fb_upload"),
    url(r'^edit/$', 'filebrowser.views.edit', name="fb_edit"),
    url(r'^rename/$', 'filebrowser.views.rename', name="fb_rename"),
    url(r'^delete/$', 'filebrowser.views.delete', name="fb_delete"),
    url(r'^versions/$', 'filebrowser.views.versions', name="fb_versions"),
    
)
