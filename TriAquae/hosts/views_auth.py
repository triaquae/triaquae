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
import logging.config, logging, logging.handlers

#from unipath import Path
import models

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)
logger = logging.getLogger(__name__)

# buf format
# ip \t hostname \t idc \t protocol type \t port \t operating system
@csrf_protect
def load_batch_auth(request):
    if 'buf' in request.POST:
        buf = request.POST['buf']
        list_buf = buf.splitlines()
        list_buf = [l for l in list_buf if l and not re.match('#', l)]
        num = 0
        for l in list_buf:
            logger.error('save %s' % l)
            try:
                (ip, remoteuser, authtype, password) = re.split('\s+', l)[:4]
                
                ip, created = models.IP.objects.get_or_create(ip=ip)
                logger.error('ip [%s] created[%s]' %(ip, created))
                remoteuser, created = models.RemoteUser.objects.get_or_create(name=remoteuser)
                logger.error('remoteuser [%s] created[%s]' %(remoteuser, created))
                obj_auth = models.AuthByIpAndRemoteUser(ip=ip, remoteUser=remoteuser, authtype=authtype, password=password)
                obj_auth.validate_unique()
                obj_auth.save()
                
                num += 1
            except:
                logger.error('%s' % traceback.format_exc())
        messages.info(request, 'load %s auths, filter %s ones' % (num, len(list_buf) - num))
        return  HttpResponseRedirect('/admin/hosts/authbyipandremoteuser/')
    elif 'buf' in request.GET:
        logger.error(request.GET)
        return HttpResponseRedirect('/admin/hosts/authbyipandremoteuser/')
        
@csrf_protect
def load_batch_auth_form(request):
    batch_title = 'load batch authorization'
    batch_comment = '\n#'.join(('', "Input your authorization for ip & remoteuser here. ",
                    'Format: ip \t remote_user \t auth_type \t password or key_file path. ', 
                    'Example: ',
                    '192.168.1.1 \t apache \t ssh-password \t pass1234Aer3 ',
                    '192.168.1.2 \t test2  \t ssh-key 	\t /root/.ssh/id_rsa'))
    batch_context = {'batch_action':'/admin/hosts/load_batch_auth/', 'batch_comment':batch_comment, 'batch_title':batch_title}
    return render(request, 'load_batch_form.html', batch_context)
