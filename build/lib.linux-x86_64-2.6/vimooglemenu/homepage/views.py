from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import RequestContext



def homepageview(request):
  return(render_to_response( 'vimooglemenu.haml',{'webpage':'webpage'} ,context_instance = RequestContext(request)  ))