from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple 
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from django.contrib.sites.models import Site as djangosite

from django.shortcuts import render


import logging.config, logging, logging.handlers

#self module
import models

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)
logger = logging.getLogger(__name__)


    
class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
    ips = forms.ModelMultipleChoiceField(
        queryset=models.IP.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name= ('Ip list'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['ips'].initial = self.instance.ip_set.all()

    def save(self, commit=True):
        groupmachine = super(GroupForm, self).save(commit=False)  
        if commit:
            groupmachine.save()
        if groupmachine.pk:
            groupmachine.ip_set = self.cleaned_data['ips']
            self.save_m2m()
        return groupmachine

class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
        

class IpAdmin(admin.ModelAdmin):
    search_fields = ('ip','hostname','os')
    fields = ('hostname', 'ip', 'idc','group',  'port', 'os','status_monitor_on', 'snmp_on','asset_collection','alert_limit','snmp_alert_limit', 'snmp_version', 'snmp_security_level', 'snmp_community_name','snmp_auth_protocol', 'snmp_user', 'snmp_pass' ,'system_load_warning', 'system_load_critical', 'cpu_idle_warning', 'cpu_idle_critical', 'mem_usage_warning', 'mem_usage_critical')
    list_display = ('ip', 'hostname',  'idc',  'port', 'os')
    list_editable = ('idc',  'port', 'os')
    #radio_fields = {'idc':admin.VERTICAL}
    filter_horizontal = ('group',)
    list_filter = ('idc','os','group')
    #actions = ['add_to_groupmachine', 'add_to_cdnmachine','batch_load']
    def add_to_groupmachine(self, request, queryset):
        pass
    def add_to_cdnmachine(self, request, queryset):
        pass
    def batch_load(self, request, queryset):
        logger.error('begin batch_load ip')
        render(request, 'load_ip_batch_form.html')

class IdcAdminForm(GroupForm):
    class Meta:
        model = models.Idc
    fields=('name')
    
class IdcAdmin(admin.ModelAdmin):
    form = IdcAdminForm

