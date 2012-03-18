from django.conf.urls.defaults import *

##admin module disabled
##Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()


#urlpatterns = patterns('django.views.static', 
#    url(r'^js/(?P<path>.*)$',       'serve', {'document_root': '/home/picturep/sites/djangovimooglemenu/vimooglemenu/static/js/'    ,  'show_indexes': True} ),
#    url(r'^css/(?P<path>.*)$',      'serve', {'document_root': '/home/picturep/sites/djangovimooglemenu/vimooglemenu/static/css/'   ,  'show_indexes': True} ),
#    url(r'^images/(?P<path>.*)$',   'serve', {'document_root': '/home/picturep/sites/djangovimooglemenu/vimooglemenu/static/images/',  'show_indexes': True} ),
#    url(r'^js/(?P<path>.*)$',       'serve', {'document_root': '/home/user/python/djangovimooglemenu/vimooglemenu/homepage/static/js/'    ,  'show_indexes': True} ),
#    url(r'^css/(?P<path>.*)$',      'serve', {'document_root': '/home/user/python/djangovimooglemenu/vimooglemenu/homepage/static/css/'   ,  'show_indexes': True} ),
#    url(r'^images/(?P<path>.*)$',   'serve', {'document_root': '/home/user/python/djangovimooglemenu/vimooglemenu/homepage/static/images/',  'show_indexes': True} ),
#    url(r'^js/(?P<path>.*)$',       'serve', {'document_root': settings.CSS_ROOT} ),
#    url(r'^css/(?P<path>.*)$',      'serve', {'document_root': settings.JS_ROOT} ),
#    url(r'^images/(?P<path>.*)$',   'serve', {'document_root': settings.IMAGES_ROOT} ),
#)


#from django.conf import settings
#if settings.DEBUG:
#    urlpatterns += patterns('django.views.static',
#        url(r'^media/(?P<path>.*)$','serve', {'document_root': settings.MEDIA_ROOT,}  ),
#   )
## this assumes MEDIA_URL has a value of '/media/'.


#urlpatterns += patterns('',
urlpatterns   = patterns('',

#   #admin module disabled
#   #Uncomment the admin/doc line below and add 'django.contrib.admindocs' to INSTALLED_APPS to enable admin documentation:
#   (r'^admin/doc/', include('django.contrib.admindocs.urls')),
#   #Uncomment the next line to enable the admin:
#   (r'^admin/', include(admin.site.urls)),
    
    (r'', include('homepage.urls')),
)




