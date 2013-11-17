# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Devinfo'
        db.create_table(u'hosts_devinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Triaquae_Hostname', self.gf('django.db.models.fields.CharField')(default='Null', max_length=50)),
            ('System_Hostname', self.gf('django.db.models.fields.CharField')(default='Null', max_length=50)),
            ('System_Ip', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Device_Type', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Device_Model', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('System_Kernel', self.gf('django.db.models.fields.CharField')(default='Null', max_length=256)),
            ('System_Version', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('System_Mac', self.gf('django.db.models.fields.CharField')(default='Null', max_length=256)),
            ('Physical_Memory', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('System_Swap', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Memory_Slots_Number', self.gf('django.db.models.fields.CharField')(default='Null', max_length=30)),
            ('Memory_Slots_All', self.gf('django.db.models.fields.CharField')(default='Null', max_length=1000)),
            ('Logical_Cpu_Cores', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Physical_Cpu_Cores', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Physical_Cpu_Model', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Physical_Cpu_MHz', self.gf('django.db.models.fields.CharField')(default='Null', max_length=256)),
            ('Hard_Disk', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Ethernet_Interface', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('System_Hostid', self.gf('django.db.models.fields.CharField')(default='Null', max_length=30)),
            ('Device_Sn', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Asset_Number', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Note1', self.gf('django.db.models.fields.CharField')(default='Null', max_length=256)),
            ('Note2', self.gf('django.db.models.fields.CharField')(default='Null', max_length=256)),
            ('Note3', self.gf('django.db.models.fields.CharField')(default='Null', max_length=256)),
            ('Check_Time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'hosts', ['Devinfo'])

        # Adding model 'Check_Devinfo'
        db.create_table(u'hosts_check_devinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Triaquae_Hostname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Change_Type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('Old_Value', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('New_Value', self.gf('django.db.models.fields.CharField')(default='Null', max_length=64)),
            ('Change_Time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'hosts', ['Check_Devinfo'])

        # Adding model 'Idc'
        db.create_table(u'hosts_idc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'hosts', ['Idc'])

        # Adding model 'Group'
        db.create_table(u'hosts_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'hosts', ['Group'])

        # Adding model 'IP'
        db.create_table(u'hosts_ip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(unique=True, max_length=15)),
            ('idc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hosts.Idc'], null=True, blank=True)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default='22')),
            ('os', self.gf('django.db.models.fields.CharField')(default='linux', max_length=20)),
            ('alert_limit', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('snmp_alert_limit', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('asset_collection', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status_monitor_on', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('snmp_on', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('snmp_version', self.gf('django.db.models.fields.CharField')(default='2c', max_length=10)),
            ('snmp_community_name', self.gf('django.db.models.fields.CharField')(default='public', max_length=50)),
            ('snmp_security_level', self.gf('django.db.models.fields.CharField')(default='auth', max_length=50)),
            ('snmp_auth_protocol', self.gf('django.db.models.fields.CharField')(default='MD5', max_length=50)),
            ('snmp_user', self.gf('django.db.models.fields.CharField')(default='triaquae_snmp', max_length=50)),
            ('snmp_pass', self.gf('django.db.models.fields.CharField')(default='my_pass', max_length=50)),
            ('system_load_warning', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('system_load_critical', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('cpu_idle_warning', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('cpu_idle_critical', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('mem_usage_warning', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('mem_usage_critical', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'hosts', ['IP'])

        # Adding M2M table for field group on 'IP'
        m2m_table_name = db.shorten_name(u'hosts_ip_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ip', models.ForeignKey(orm[u'hosts.ip'], null=False)),
            ('group', models.ForeignKey(orm[u'hosts.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ip_id', 'group_id'])

        # Adding model 'RemoteUser'
        db.create_table(u'hosts_remoteuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'hosts', ['RemoteUser'])

        # Adding model 'TriaquaeUser'
        db.create_table(u'hosts_triaquaeuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'hosts', ['TriaquaeUser'])

        # Adding M2M table for field remoteuser on 'TriaquaeUser'
        m2m_table_name = db.shorten_name(u'hosts_triaquaeuser_remoteuser')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triaquaeuser', models.ForeignKey(orm[u'hosts.triaquaeuser'], null=False)),
            ('remoteuser', models.ForeignKey(orm[u'hosts.remoteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triaquaeuser_id', 'remoteuser_id'])

        # Adding M2M table for field group on 'TriaquaeUser'
        m2m_table_name = db.shorten_name(u'hosts_triaquaeuser_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triaquaeuser', models.ForeignKey(orm[u'hosts.triaquaeuser'], null=False)),
            ('group', models.ForeignKey(orm[u'hosts.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triaquaeuser_id', 'group_id'])

        # Adding M2M table for field ip on 'TriaquaeUser'
        m2m_table_name = db.shorten_name(u'hosts_triaquaeuser_ip')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triaquaeuser', models.ForeignKey(orm[u'hosts.triaquaeuser'], null=False)),
            ('ip', models.ForeignKey(orm[u'hosts.ip'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triaquaeuser_id', 'ip_id'])

        # Adding model 'AuthByIpAndRemoteUser'
        db.create_table(u'hosts_authbyipandremoteuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('authtype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hosts.IP'], null=True, blank=True)),
            ('remoteUser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hosts.RemoteUser'], null=True, blank=True)),
        ))
        db.send_create_signal(u'hosts', ['AuthByIpAndRemoteUser'])

        # Adding unique constraint on 'AuthByIpAndRemoteUser', fields ['ip', 'remoteUser']
        db.create_unique(u'hosts_authbyipandremoteuser', ['ip_id', 'remoteUser_id'])

        # Adding model 'ServerStatus'
        db.create_table(u'hosts_serverstatus', (
            ('host', self.gf('django.db.models.fields.IPAddressField')(max_length=15, primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('host_status', self.gf('django.db.models.fields.CharField')(default='Unkown', max_length=10)),
            ('ping_status', self.gf('django.db.models.fields.CharField')(default='Unkown', max_length=100)),
            ('last_check', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('host_uptime', self.gf('django.db.models.fields.CharField')(default='Unkown', max_length=50)),
            ('attempt_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('breakdown_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('snmp_alert_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('availability', self.gf('django.db.models.fields.CharField')(default=0, max_length=20)),
        ))
        db.send_create_signal(u'hosts', ['ServerStatus'])

        # Adding model 'AlertTemp'
        db.create_table(u'hosts_alerttemp', (
            ('host', self.gf('django.db.models.fields.IPAddressField')(max_length=15, primary_key=True)),
            ('snmp_status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('snmp_data', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'hosts', ['AlertTemp'])

        # Adding model 'OpsLog'
        db.create_table(u'hosts_opslog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('log_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tri_user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('run_user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cmd', self.gf('django.db.models.fields.TextField')()),
            ('total_task', self.gf('django.db.models.fields.IntegerField')()),
            ('success_num', self.gf('django.db.models.fields.IntegerField')()),
            ('failed_num', self.gf('django.db.models.fields.IntegerField')()),
            ('track_mark', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'hosts', ['OpsLog'])

        # Adding model 'OpsLogTemp'
        db.create_table(u'hosts_opslogtemp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cmd', self.gf('django.db.models.fields.TextField')()),
            ('event_log', self.gf('django.db.models.fields.TextField')()),
            ('result', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=30)),
            ('track_mark', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'hosts', ['OpsLogTemp'])


    def backwards(self, orm):
        # Removing unique constraint on 'AuthByIpAndRemoteUser', fields ['ip', 'remoteUser']
        db.delete_unique(u'hosts_authbyipandremoteuser', ['ip_id', 'remoteUser_id'])

        # Deleting model 'Devinfo'
        db.delete_table(u'hosts_devinfo')

        # Deleting model 'Check_Devinfo'
        db.delete_table(u'hosts_check_devinfo')

        # Deleting model 'Idc'
        db.delete_table(u'hosts_idc')

        # Deleting model 'Group'
        db.delete_table(u'hosts_group')

        # Deleting model 'IP'
        db.delete_table(u'hosts_ip')

        # Removing M2M table for field group on 'IP'
        db.delete_table(db.shorten_name(u'hosts_ip_group'))

        # Deleting model 'RemoteUser'
        db.delete_table(u'hosts_remoteuser')

        # Deleting model 'TriaquaeUser'
        db.delete_table(u'hosts_triaquaeuser')

        # Removing M2M table for field remoteuser on 'TriaquaeUser'
        db.delete_table(db.shorten_name(u'hosts_triaquaeuser_remoteuser'))

        # Removing M2M table for field group on 'TriaquaeUser'
        db.delete_table(db.shorten_name(u'hosts_triaquaeuser_group'))

        # Removing M2M table for field ip on 'TriaquaeUser'
        db.delete_table(db.shorten_name(u'hosts_triaquaeuser_ip'))

        # Deleting model 'AuthByIpAndRemoteUser'
        db.delete_table(u'hosts_authbyipandremoteuser')

        # Deleting model 'ServerStatus'
        db.delete_table(u'hosts_serverstatus')

        # Deleting model 'AlertTemp'
        db.delete_table(u'hosts_alerttemp')

        # Deleting model 'OpsLog'
        db.delete_table(u'hosts_opslog')

        # Deleting model 'OpsLogTemp'
        db.delete_table(u'hosts_opslogtemp')


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
            'Asset_Number': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Check_Time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'Device_Model': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Device_Sn': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Device_Type': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Ethernet_Interface': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Hard_Disk': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Logical_Cpu_Cores': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '64'}),
            'Memory_Slots_All': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '1000'}),
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
            'last_check': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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