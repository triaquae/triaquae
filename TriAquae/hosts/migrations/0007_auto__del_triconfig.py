# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TriConfig'
        db.delete_table(u'hosts_triconfig')


    def backwards(self, orm):
        # Adding model 'TriConfig'
        db.create_table(u'hosts_triconfig', (
            ('function', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('function_info', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'hosts', ['TriConfig'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hosts.alerttemp': {
            'Meta': {'object_name': 'AlertTemp'},
            'host': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'primary_key': 'True'}),
            'snmp_data': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'snmp_status': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'hosts.authbyipandremoteuser': {
            'Meta': {'unique_together': "(('ip', 'remoteUser'),)", 'object_name': 'AuthByIpAndRemoteUser'},
            'authtype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hosts.IP']", 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'remoteUser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hosts.RemoteUser']", 'null': 'True', 'blank': 'True'})
        },
        u'hosts.check_devinfo': {
            'Change_Time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'Change_Type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'Meta': {'object_name': 'Check_Devinfo'},
            'New_Value': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Old_Value': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'Triaquae_Hostname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'hosts.devinfo': {
            'Asset_Number': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '164'}),
            'Check_Time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'Device_Model': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Device_Sn': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '164'}),
            'Device_Type': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Ethernet_Interface': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '364'}),
            'Hard_Disk': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Logical_Cpu_Cores': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Memory_Slots_All': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '2000'}),
            'Memory_Slots_Number': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '30'}),
            'Meta': {'object_name': 'Devinfo'},
            'Note1': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '256'}),
            'Note2': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '256'}),
            'Note3': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '256'}),
            'Physical_Cpu_Cores': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Physical_Cpu_MHz': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '256'}),
            'Physical_Cpu_Model': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Physical_Memory': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'System_Hostid': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '30'}),
            'System_Hostname': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '50'}),
            'System_Ip': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'System_Kernel': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '256'}),
            'System_Mac': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '256'}),
            'System_Swap': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'System_Version': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Triaquae_Hostname': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'hosts.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'hosts.idc': {
            'Meta': {'object_name': 'Idc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'hosts.ip': {
            'Meta': {'object_name': 'IP'},
            'alert_limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'asset_collection': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cpu_idle_critical': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cpu_idle_warning': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hosts.Group']", 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hosts.Idc']", 'null': 'True', 'blank': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'}),
            'mem_usage_critical': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mem_usage_warning': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'default': "'linux'", 'max_length': '20'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': "'22'"}),
            'snmp_alert_limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'snmp_auth_protocol': ('django.db.models.fields.CharField', [], {'default': "'MD5'", 'max_length': '50'}),
            'snmp_community_name': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '50'}),
            'snmp_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'snmp_pass': ('django.db.models.fields.CharField', [], {'default': "'my_pass'", 'max_length': '50'}),
            'snmp_security_level': ('django.db.models.fields.CharField', [], {'default': "'auth'", 'max_length': '50'}),
            'snmp_user': ('django.db.models.fields.CharField', [], {'default': "'triaquae_snmp'", 'max_length': '50'}),
            'snmp_version': ('django.db.models.fields.CharField', [], {'default': "'2c'", 'max_length': '10'}),
            'status_monitor_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'system_load_critical': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'system_load_warning': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'hosts.opslog': {
            'Meta': {'object_name': 'OpsLog'},
            'cmd': ('django.db.models.fields.TextField', [], {}),
            'failed_num': ('django.db.models.fields.IntegerField', [], {}),
            'finish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'run_user': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'success_num': ('django.db.models.fields.IntegerField', [], {}),
            'total_task': ('django.db.models.fields.IntegerField', [], {}),
            'track_mark': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'tri_user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'hosts.opslogtemp': {
            'Meta': {'object_name': 'OpsLogTemp'},
            'cmd': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event_log': ('django.db.models.fields.TextField', [], {}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '30'}),
            'track_mark': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'hosts.remoteuser': {
            'Meta': {'object_name': 'RemoteUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'hosts.serverstatus': {
            'Meta': {'object_name': 'ServerStatus'},
            'attempt_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'availability': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '20'}),
            'breakdown_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'primary_key': 'True'}),
            'host_status': ('django.db.models.fields.CharField', [], {'default': "'Unkown'", 'max_length': '10'}),
            'host_uptime': ('django.db.models.fields.CharField', [], {'default': "'Unkown'", 'max_length': '50'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_check': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '100'}),
            'ping_status': ('django.db.models.fields.CharField', [], {'default': "'Unkown'", 'max_length': '100'}),
            'snmp_alert_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'up_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'hosts.triaquaeuser': {
            'Meta': {'object_name': 'TriaquaeUser'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hosts.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hosts.IP']", 'null': 'True', 'blank': 'True'}),
            'remoteuser': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hosts.RemoteUser']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        }
    }

    complete_apps = ['hosts']