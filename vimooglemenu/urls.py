from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



#urlpatterns = patterns('django.views.static', 
#    url(r'^js/(?P<path>.*)$',       'serve', {'document_root': '/home/picturep/sites/djangovimooglemenu/vimooglemenu/static/js/'    ,  'show_indexes': True} ),
#    url(r'^css/(?P<path>.*)$',      'serve', {'document_root': '/home/picturep/sites/djangovimooglemenu/vimooglemenu/static/css/'   ,  'show_indexes': True} ),
#    url(r'^images/(?P<path>.*)$',   'serve', {'document_root': '/home/picturep/sites/djangovimooglemenu/vimooglemenu/static/images/',  'show_indexes': True} ),
#)


#from django#.conf import settings
#if settings.DEBUG:
#    urlpatterns += patterns('django.views.static',
#        url(r'^media/(?P<path>.*)$','serve', {'document_root': settings.MEDIA_ROOT,}  ),
#   )
## this assumes MEDIA_URL has a value of '/media/'.


#urlpatterns += patterns('',
urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    
    (r'', include('homepage.urls')),
    
    
)



