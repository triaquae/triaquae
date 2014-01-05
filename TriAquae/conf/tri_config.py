#Author: Alex Li
import os,sys

Working_dir = '/usr/local/TriAquae'
Max_batch_threads =  35
Tri_sftp_dir = '%s/TriSFTP' % Working_dir
Tri_sftp_send_dir = '%s/TriSFTP/send' % Working_dir
Tri_sftp_recv_dir = '%s/TriSFTP/recv' % Working_dir
Dangerous_cmd_list = '%s/share/dangerous_cmd.txt' % Working_dir
RRDTOOL_png_dir = '%s/TriAquae/static/img/rrdtool_png/' %  Working_dir
RRDTOOL_rrd_file_dir= '%s/rrdtool/rrd_files' % Working_dir

#TriAquae database info
MySQL_Name = 'TriAquae'   # Don't change this database name
MySQL_Host = '127.0.0.1'  # Your Mysql hostname
MySQL_Port = '3306'       # Your Mysql port
MySQL_User = 'root'       # Your Mysql username
MySQL_Pass = ''           # Your Mysql password, '' means no password.

#TriAquae Log settings
Log_dir = '%s/TriAquae/logs' % Working_dir
Snmp_temp_log = '%s/snmp_temp.log' % Log_dir

Tri_IP = '192.168.2.5'  # Change it to your own IP address
Tri_Port = '4200'      # render device
Tri_connector_username = 'tri_connector'
Tri_connector_password = 'tripass'
Tri_connector_baoleiuser = '%s/TriAquae/backend/baoleiuser.py' % Working_dir
Tri_connector_baoleihost = '%s/TriAquae/backend/baoleihost.py' % Working_dir

Asset_collection_dir = '%s/asset_collection' % Log_dir
Asset_collection_backup_dir = '%s/asset_collection_backup' % Log_dir
Ops_log_temp_purge_days = 1

SMTP_server = 'smtp.company.com'
Mail_username = 'tri_mailuser'
Mail_password = 'Motherfucker!23'

Asset_collect_user = 'triaquae'
Asset_user_password = 'dqnzbf'

dir_list = [Working_dir,Tri_sftp_dir, Log_dir,Tri_sftp_send_dir, Tri_sftp_recv_dir, Dangerous_cmd_list, RRDTOOL_rrd_file_dir,RRDTOOL_png_dir,Asset_collection_dir,Asset_collection_backup_dir]


try:
    if sys.argv[1] == '--initial':
        for d in dir_list:
            try:
            	os.makedirs(d)
            except OSError:continue
except IndexError:pass
