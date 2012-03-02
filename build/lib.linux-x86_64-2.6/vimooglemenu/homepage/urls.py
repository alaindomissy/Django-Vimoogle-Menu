from django.conf.urls.defaults import *

from vimooglemenu.homepage import views

urlpatterns = patterns('',
                       #url(r'^$',
                       #    contact_form,
                       #   name='contact_form'),
                           
                       url(r'',
                           views.homepageview,
                           name='homepageview'
                           ),
                       )
                       #r'^\?P(*)$',           '^?P(<webpage>*)/'
                 
