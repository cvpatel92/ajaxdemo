from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
import socket


def main(request):
   return render_to_response('ajaxexample.html', context_instance=RequestContext(request))

def ajax(request):
   if request.POST.has_key('client_response'):
        x = request.POST['client_response']                  
        y = socket.gethostbyname(x)  
        print y                         
        response_dict = {}                                          
        response_dict.update({'server_response': y })                                                                   
        return HttpResponse(json.dumps(response_dict), content_type='application/javascript') 
   else:
        return render_to_response('ajaxexample.html', context_instance=RequestContext(request))