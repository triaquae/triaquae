from django.db import models
from django import forms
from datetime import datetime

#from django.contrib.auth.models import (User, BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import User
# Create your models here.


class Devinfo(models.Model):
    Triaquae_Hostname = models.CharField("Triaquae_Hostname", max_length=50, default='Null')
    System_Hostname = models.CharField("System_Hostname", max_length=50, default='Null')
    System_Ip = models.CharField("System_Ip", max_length=64, default='Null')
    Device_Type = models.CharField("Device_type", max_length=64, default='Null')
    Device_Model = models.CharField("Device_model", max_length=64, default='Null')
    System_Kernel = models.CharField("System_Kernel", max_length=256, default='Null')
    System_Version = models.CharField("System_Version", max_length=64, default='Null')
    System_Mac = models.CharField("System_Mac", max_length=256, default='Null')
    Physical_Memory = models.CharField("Physical_Memory", max_length=64, default='Null')
    System_Swap = models.CharField("System_Swap", max_length=64, default='Null')
    Memory_Slots_Number = models.CharField("Memory_Slots_Number", max_length=30, default='Null')
    Memory_Slots_All = models.CharField("Memory_Slots_All", max_length=2000, default='Null')
    Logical_Cpu_Cores = models.CharField("Logical_Cpu_Cores", max_length=64, default='Null')
    Physical_Cpu_Cores = models.CharField("Physical_Cpu_Cores", max_length=64, default='Null')
    Physical_Cpu_Model = models.CharField("Physical_Cpu_Model", max_length=64, default='Null')
    Physical_Cpu_MHz = models.CharField("Physical_Cpu_MHz", max_length=256, default='Null')
    Hard_Disk = models.CharField("Hard_Disk", max_length=64, default='Null')
    Ethernet_Interface = models.CharField("Ethernet_Interface", max_length=364, default='Null')
    System_Hostid = models.CharField("System_Hostid", max_length=30, default='Null')
    Device_Sn = models.CharField("Device_Sn", max_length=164, default='Null')
    Asset_Number = models.CharField("Asset_Number", max_length=164, default="Null")
    Note1 = models.CharField("Note1", max_length=256, default='Null')
    Note2 = models.CharField("Note2", max_length=256, default='Null')
    Note3 = models.CharField("Note3", max_length=256, default='Null')
    Check_Time = models.DateTimeField("Check_Time", auto_now=True)

    def __unicode__(self):
        return "%s" % (self.System_Hostname)

class Check_Devinfo(models.Model):
    Triaquae_Hostname = models.CharField("Triaquae_Hostname", max_length=50)
    Change_Type = models.CharField("Change_Type", max_length=64)
    Old_Value = models.CharField("Old_Value", max_length=64)
    New_Value = models.CharField("New_Value", max_length=64, default='Null')
    Change_Time = models.DateTimeField("Change_Time", auto_now=True)

    def __unicode__(self):
        return "%s" % (self.System_Hostname)

class DevForm(forms.ModelForm):
    System_Hostname = forms.CharField(max_length=50)
    System_Ip = forms.CharField(max_length=64)
    Device_Type = forms.CharField(max_length=64)
    Device_Model = forms.CharField(max_length=64)
    System_Kernel = forms.CharField(max_length=256)
    System_Version = forms.CharField(max_length=64)
    System_Mac = forms.CharField(max_length=640)
    Physical_Memory = forms.CharField(max_length=64)
    System_Swap = forms.CharField(max_length=64)
    Memory_Slots_Number = forms.CharField(max_length=3)
    Memory_Slots_All = forms.CharField(max_length=256)
    Logical_Cpu_Cores = forms.CharField(max_length=64)
    Physical_Cpu_Cores = forms.CharField(max_length=64)
    Physical_Cpu_Model = forms.CharField(max_length=64)
    Physical_Cpu_MHz = forms.CharField(max_length=256)
    Hard_Disk = forms.CharField(max_length=64)
    Ethernet_Interface = forms.CharField(max_length=64)
    Device_Sn = forms.CharField(max_length=64)
    Asset_Number = forms.CharField(max_length=64)
    System_Hostid = forms.CharField(64)
    Note1 = forms.CharField(max_length=256)
    Note2 = forms.CharField(max_length=256)
    Note3 = forms.CharField(max_length=256)
    Check_Time = forms.DateTimeField()


class Idc(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.name

class IP(models.Model):
    hostname=models.CharField(max_length=50, unique=True)
    ip = models.IPAddressField(unique=True)
    idc = models.ForeignKey(Idc, null=True, blank=True)
    group = models.ManyToManyField(Group, null=True, blank=True)
    port = models.IntegerField(default='22')
    os = models.CharField(max_length=20, default='linux', verbose_name='Operating System')

    #snmp related
    alert_limit = models.IntegerField(default=5)
    snmp_alert_limit = models.IntegerField(default=5)
    asset_collection = models.BooleanField(default=True,verbose_name='enable asset collection')
    status_monitor_on = models.BooleanField(default=True)
    snmp_on = models.BooleanField(default=True)
    snmp_version = models.CharField(max_length=10,default='2c')
    snmp_community_name = models.CharField(max_length=50,default='public')
    snmp_security_level = models.CharField(max_length=50,default='auth')
    snmp_auth_protocol = models.CharField(max_length=50,default='MD5')
    snmp_user = models.CharField(max_length=50,default='triaquae_snmp')
    snmp_pass = models.CharField(max_length=50,default='my_pass')

    system_load_warning = models.IntegerField(default=0,blank=True,verbose_name="load >")
    system_load_critical = models.IntegerField(default=0,blank=True)
    cpu_idle_warning = models.IntegerField(default=0,blank=True, verbose_name = "cpuIdle% < ")
    cpu_idle_critical= models.IntegerField(default=0,blank=True)
    mem_usage_warning = models.IntegerField(default=0,blank=True, verbose_name="memoryUsage% >")
    mem_usage_critical = models.IntegerField(default=0,blank=True)
    def __unicode__(self):
        return self.ip

class RemoteUser(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __unicode__(self):
        return self.name

class TriaquaeUser(models.Model):
    user = models.ForeignKey(User, null=True)
    email = models.EmailField()
    remoteuser = models.ManyToManyField(RemoteUser, null=True, blank=True)
    group = models.ManyToManyField(Group, null=True, blank=True)
    ip = models.ManyToManyField(IP, null=True, blank=True)
    def __unicode__(self):
        return '%s' % self.user

class AuthByIpAndRemoteUser(models.Model):
    password = models.CharField(max_length=1024,verbose_name="Password or SSH_KEY")
    AUTH_CHOICES = (('ssh-password', 'ssh-password'),('ssh-key', 'ssh-key'))
    authtype = models.CharField(max_length=100, choices=AUTH_CHOICES)
    ip = models.ForeignKey(IP, null=True, blank=True)
    remoteUser = models.ForeignKey(RemoteUser, null=True, blank=True)
    def __unicode__(self):
        return '%s\t%s' % (self.ip, self.remoteUser)
    #save throw exception
    class Meta:
        unique_together = (('ip','remoteUser'),)



class ServerStatus(models.Model):
    host = models.IPAddressField(primary_key=True)
    hostname = models.CharField(max_length=100)
    host_status = models.CharField(max_length=10,default='Unkown')
    ping_status = models.CharField(max_length=100,default='Unkown')
    last_check = models.CharField(max_length=100,default='N/A')
    host_uptime = models.CharField(max_length=50,default='Unkown')
    attempt_count = models.IntegerField(default=0)
    breakdown_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    snmp_alert_count = models.IntegerField(default=0)
    availability = models.CharField(max_length=20,default=0)
    def __unicode__(self):
        return self.host

class OpsLog(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True,blank=True)
    log_type = models.CharField(max_length=50)
    tri_user = models.CharField(max_length=30)
    run_user = models.CharField(max_length=30)
    cmd = models.TextField()
    total_task = models.IntegerField()
    success_num = models.IntegerField()
    failed_num = models.IntegerField()
    track_mark = models.IntegerField(unique=True)
    note = models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.cmd

class OpsLogTemp(models.Model):
        date = models.DateTimeField(auto_now_add=True)
        user = models.CharField(max_length=30)
        ip = models.IPAddressField()
        event_type = models.CharField(max_length=50)
        cmd = models.TextField()
        event_log = models.TextField()
        result = models.CharField(max_length=30,default='unknown')
        track_mark = models.IntegerField(blank=True)
        note = models.CharField(max_length=100,blank=True)
        def __unicode__(self):
            return self.ip
class QuickLink(models.Model):
	link_name = models.CharField(max_length=50)
	url = models.URLField()
	COLOR_CHOICES = (('btn-danger', 'red'),('btn-warning', 'yellow'),('btn-success','green'), ('btn-primary','dark-blue'),('btn-info','blue'))
        color = models.CharField(max_length=100, choices=COLOR_CHOICES)
