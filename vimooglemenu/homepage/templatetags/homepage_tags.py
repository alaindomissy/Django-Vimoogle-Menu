from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navcurrent(requestpath, urls):
    #if requestpath in ( reverse(url) for url in urls.split() ):
    #    return "<li 'class'='current'   >"
    #else:
        return "<li 'class'='singlelink'>"     




        #<a 'href': '/" + pagelink + r"' >" + pagedisplay + "</a></li>
        #<a 'href':*" + pagelink + "*' >"  + pagedisplay + "</a></li>
        #pagelink, pagedisplay
        #"<li 'class'='singlelink'><a 'href':'pagelink' >pagedisplay</a></li>"     
        #% {'pagelink':pagelink  'pagedisplay':pagedisplay}
        #
        #"<li 'class'='singlelink' ><a 'href': '%s' >%s</a></li>" % )



#@register.simple_tag
#def navcurrent(request, views):
#    views = ["homepage.views." + view for view in views.split()]
#    try:
#        view = urlresolvers.resolve(request.path).url_name
#        if view in views:
#            return "<li 'class'='current'   >"
#        else:
#            return "<li 'class'='singlelink'>"
#    except urlresolvers.Resolver404:
#        return ""