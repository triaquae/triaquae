from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple 
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from django.contrib.sites.models import Site as djangosite

import admin_ip

import logging.config, logging, logging.handlers

#self module
import models
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.ERROR)
logger = logging.getLogger(__name__)

#admin.site.unregister(djangouser)
#admin.site.unregister(djangogroup)
#admin.site.unregister(djangosite)



class RemoteUserAdminForm(forms.ModelForm):
    class Meta:
        model = models.RemoteUser
    triaquaeusers = forms.ModelMultipleChoiceField(
        queryset=models.TriaquaeUser.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name= ('Triaquae User'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(RemoteUserAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['triaquaeusers'].initial = self.instance.triaquaeuser_set.all()

    def save(self, commit=True):
        remoteuser = super(RemoteUserAdminForm, self).save(commit=False)  
        if commit:
            remoteuser.save()
        if remoteuser.pk:
            remoteuser.triaquaeuser_set = self.cleaned_data['triaquaeusers']
            self.save_m2m()
        return remoteuser


class RemoteUserAdmin(admin.ModelAdmin):
    form = RemoteUserAdminForm
    

class TriaquaeUserAdminForm(forms.ModelForm):
    class Meta:
        model = models.TriaquaeUser
    

class TriaquaeUserAdmin(admin.ModelAdmin):
    #form = TriaquaeUserAdminForm
    list_display = ('user', 'email')
    list_editable = ('email',)
    filter_horizontal = ('group','remoteuser', 'ip',)

