from django.conf.urls.defaults import *

from vimooglemenu.homepage import views

urlpatterns = patterns( '',  
                        url(r'^(?P<pagename>link0.*)/$', views.homepageview, name='vmm-link0'),
                        url(r'^(?P<pagename>link1.*)/$', views.homepageview, name='vmm-link1'),
                        url(r'^(?P<pagename>link2.*)/$', views.homepageview, name='vmm-link2'),
                        url(r'^(?P<pagename>link3.*)/$', views.homepageview, name='vmm-link3'),
                        url(r'^(?P<pagename>link4.*)/$', views.homepageview, name='vmm-link4'),
                        url(r'^(?P<pagename>link5.*)/$', views.homepageview, name='vmm-link5'),
                       #url(r''         , views.homepageview,                      name='vmm-homepageview'),
                        url(r'^(?P<pagename>.*)/$', views.homepageview, name='vimooglemenu-homepageview'),
                       )
                       

                 
