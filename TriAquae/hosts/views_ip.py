# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.template import loader, Context, RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from django.template import Context
import datetime
import re, traceback
import logging


import models

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)
logger = logging.getLogger(__name__)

# buf format
# ip \t hostname \t idc \t protocol type \t port \t operating system
@csrf_protect
def load_batch_ip(request):
    if 'buf' in request.POST:
        buf = request.POST['buf']
        list_buf = buf.splitlines()
        list_buf = [l for l in list_buf if not re.match('#', l)]
        num = 0

        for l in list_buf:
            try:
                (ip, hostname, idc, port, os) = l.split()[:5]
                #(ip, hostname, idc, port, os) = re.split('\s+', l)[:6]
                idc = models.Idc.objects.get(name=idc)
                models.IP(ip=ip, hostname=hostname, idc=idc, port =port, os=os).save()
                num += 1
            except:
                logger.error('%s' % traceback.format_exc())
        messages.info(request, 'load %s ips, filter %s lines' % (num, len(list_buf) - num))
        return  HttpResponseRedirect('/admin/hosts/ip/')
    elif 'buf' in request.GET:
        logger.error(request.GET)
        messages.info(request, 'load 0 ips for http get ')
    return  HttpResponseRedirect('/admin/hosts/ip/')

@csrf_protect
def load_batch_ip_form(request):
    batch_title = 'load batch ip'
    batch_comment = '\n#'.join(('', 
        'Input your authorization for ip & remoteuser here. ',
        'Example',
	'Format: ip \t hostname \t IDC \t  port \t operating system. ',
        '        192.168.1.1 \t test1 \t BJ \t 22 \t linux',
        '        192.168.1.2 \t test2 \t SH  \t 22 \t linux'))
    batch_context = {'batch_action':'/admin/hosts/load_batch_ip/', 'batch_comment':batch_comment, 'batch_title':batch_title}
    return render(request, 'load_batch_form.html', batch_context)
