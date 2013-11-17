from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple 
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from django.contrib.sites.models import Site as djangosite
from django.shortcuts import render
import admin_ip

import logging.config, logging, logging.handlers

#self module
import models
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)
logger = logging.getLogger(__name__)


class AuthByIpAndRemoteUserForm(forms.ModelForm):
    def custom_method(self):
        print 'hello world'
        
class AuthByIpAndRemoteUserAdmin(admin.ModelAdmin):
    search_fields = ['ip__ip']
    fields = ('ip', 'remoteUser', 'authtype', 'password')
    list_display = ('ip', 'remoteUser', 'authtype', 'password')
    list_editable = ('remoteUser', 'authtype', 'password')
    actions = ('load_from_csv',)
    form = AuthByIpAndRemoteUserForm
    def load_from_csv(self, request, queryset):
        return render(request, 'load_auth_ip_remoteuser_form.html')
    
