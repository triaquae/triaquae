#!/usr/bin/env python
#Author: Alex Li
import sys,os
from datetime import *
#----------------Use Django Mysql model----------------
import db_connector
import tri_config
#----------------Use Paramiko to connect ssh-----------
import paramiko
import logger
import MultiRunCounter
from django.core.exceptions import ObjectDoesNotExist
try:
	if sys.argv[1] == '-h':
		print '''
usage:    runSFTP.py ip user option localfile remote_path -t track_mark --single 
-s   :    send file , e.g: ./runSFTP.py 192.168.2.13 alex -s local_filename.tgz /remoteServerPath/ -t 355
		     ./runSFTP.py 192.168.2.13 alex -s local_filename.tgz /remoteServerPath/ --single
-g   :    get file,   e.g: ./demo3_sftp.py 192.168.91.171 alex -g /remotePath/Remote_filename.tgz -t 365
		     ./demo3_sftp.py 192.168.91.171 alex -g /remotePath/Remote_filename.tgz --single

--single: run in single mode,it will create a trackmark in DB automatically.
-t track_mark: set the trackmark for this file transfer operation,usually use in multi-process mode
'''
		sys.exit()
except IndexError:
	print "invalid argument followed after the script, try -h for help."
	sys.exit()
try:
	if '-t' in sys.argv:
		track_mark_index = sys.argv.index('-t') + 1
		track_mark = int(sys.argv[track_mark_index]) 
	else:
        	add_track_mark = MultiRunCounter.AddNumber()
        	track_mark = int(add_track_mark)	
except ValueError:
	print "wrong track_mark provided after -t, expect a int type by get str"
if '--single' in sys.argv:
	multi_run = 0
else:
	multi_run = 1	

Split_line="------------- "
home = os.environ['HOME']
try:
    h=db_connector.IP.objects.get(ip = sys.argv[1])
    host= h.ip 
    port= int(h.port )
    username = sys.argv[2] 
    auth = db_connector.AuthByIpAndRemoteUser.objects.get(ip__ip=host, remoteUser__name= username)
    password = auth.password
    auth_type = auth.authtype
    option = sys.argv[3]
    pkey_file= auth.password
except ObjectDoesNotExist:
    err_msg = 'No access right to host,please make sure you have your TriAquae user bound to remote user %s and host %s' %(sys.argv[2],sys.argv[1])
    logger.RecordLog(sys.argv[1],'SftpConnection','N/A',err_msg,'Error',track_mark,sys.argv[2],multi_run)
    print err_msg
    sys.exit()
try:
	run_user = sys.argv[6]
except IndexError:
	run_user = 'TestSftpUser'

s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    t = paramiko.Transport((host,port))
    if auth_type == 'ssh-key':
		key = paramiko.RSAKey.from_private_key_file(pkey_file)
		t.connect(username=username,pkey=key)
    elif auth_type == 'ssh':
		t.connect(username=username,password=password)

except paramiko.AuthenticationException:
	msg= host,'---Authentication failed!'
	print msg
	logger.RecordLog(host,'SftpConnection','N/A',msg,'Error',track_mark,run_user,multi_run)
	sys.exit()
except paramiko.SSHException:
	msg= host,'---Unable to connect,no route to host!'
	print msg
	logger.RecordLog(host,'SftpConnection','N/A',msg,'Error',track_mark,run_user,multi_run)
	sys.exit()


sftp = paramiko.SFTPClient.from_transport(t)
remote_path = sys.argv[5] 
sftp_recv = tri_config.Tri_sftp_recv_dir 
if option == '-s': #send file
	local_file = sys.argv[4]
	filename = local_file.split('/')[-1]
	remote_file ='%s/%s' %(remote_path,filename)
	msg= '------- sending file %s to %s -------' %(local_file,host)
	print msg
	try:
		sftp.mkdir(remote_path)
	except IOError:pass
	sftp.put(local_file,remote_file)
		
	msg = host,"send file %s to remote directory successful: %s, under %s's home direcotry" % (filename,remote_path,username)
	logger.RecordLog(host,'SendFile','N/A',msg,'Success',track_mark,run_user,multi_run)
	sftp.put(local_file,remote_file)
	print 'Done!'
elif option == '-g': # get file
	remote_file = sys.argv[4]
	filename = remote_file.split('/')[-1]
	local_file = '%s/%s_%s' %(sftp_recv,host,filename)
	print '------- getting file %s from %s -------' %(remote_file,host)
	try:
		sftp.lstat(remote_file)	
		sftp.get(remote_file,local_file)
		print 'put file %s into local path: ' % local_file
		msg = "Result:",'Get file %s from remote ip %s and put it into local path: %s successful' %(remote_file,host,local_file)
		logger.RecordLog(host,'GetFile','N/A',msg,'Success',track_mark,run_user,multi_run)
		print 'Done'	
	except IOError:
		msg= 'Error:','file on remote ip %s not exist or it is a directory!' % host
		print msg
		logger.RecordLog(host,'GetFile','N/A',msg,'Error',track_mark,run_user,multi_run)

	
s.close()
