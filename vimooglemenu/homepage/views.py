from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import RequestContext



def homepageview(request,pagename):
  return(render_to_response( 'vimooglemenu.haml',{'pagename':pagename} ,context_instance = RequestContext(request)  ))