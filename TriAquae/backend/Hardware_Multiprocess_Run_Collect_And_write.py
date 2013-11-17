#!/usr/bin/env python
###Author By DengLei
###Email is 244979152@qq.com
import multiprocessing
import sys,os,time
import MultiRunCounter
import db_connector
import tri_config
import shutil
cur_dir = os.path.dirname(os.path.abspath(__file__))
sftp_script = 'python %s/Hardware_Multiprocess_Sftp.py' %cur_dir
ip = db_connector.IP.objects.filter(asset_collection=1)
ip_list = ''
for i in range(len(ip)):
    ip_list = ip_list + str(ip[i]) + ' '
run_user=tri_config.Asset_collect_user
Hardware_Collect_Script_Name='Hardware_Collect_Script.py'
###send file to remote machine
option='-s'
file1='%s/%s' %(cur_dir,Hardware_Collect_Script_Name)
file2='/tmp/%s' %Hardware_Collect_Script_Name
task = '''%s '%s' %s %s %s %s''' % (sftp_script,ip_list,run_user,option,file1,file2)
print "\033[1;32;40m%s\033[0m" %'send file to remote machine!'
os.system(task)
###run remote hardware collect python script
cmd_script='python %s/multiprocessing_runCMD2.py' %cur_dir
option='--auto'
command='sudo python /tmp/%s' %Hardware_Collect_Script_Name
task = '''%s %s '%s' '%s' %s''' % (cmd_script,option,ip_list,command,run_user)
print "\033[1;32;40m%s\033[0m" %'run remote hardware collect python script'
os.system(task)
###get file from remote machine
option='-g'
Hardware_Output_Name='triaquae_asset_collection.temp'
recieve_dir=tri_config.Asset_collection_dir
file1='/tmp/%s' %Hardware_Output_Name
file2='%s/%s' %(recieve_dir,Hardware_Output_Name)
task = '''%s '%s' %s %s %s %s''' % (sftp_script,ip_list,run_user,option,file1,file2)
print "\033[1;32;40m%s\033[0m" %'get file from remote machine'
os.system(task)
###wirte collect hardware information to mysql
write_script='python %s/Hardware_Write_Mysql.py' %cur_dir
task = '''%s''' % (write_script)
print "\033[1;32;40m%s\033[0m" %'wirte collect hardware information to mysql'
os.system(task)
###copy hardware information to backup and plus date
backup_dir=tri_config.Asset_collection_backup_dir
for i in os.listdir(recieve_dir):
    if i.endswith('@@triaquae_asset_collection.temp'):
        old_file=recieve_dir+os.sep+i
	new_file=backup_dir+os.sep+i+'-'+time.strftime('%Y%m%d')
        shutil.move(old_file,new_file)
print "\033[1;32;40m%s\033[0m" %'copy hardware information to backup and plus date'
