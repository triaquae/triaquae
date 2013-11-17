#!/usr/bin/env python
#Author: Alex Li
import sys,os,time
#----------------Use Django Mysql model----------------

import db_connector
#----------------Use Paramiko to connect ssh-----------

import paramiko
import logger,MultiRunCounter
#print sys.argv
from django.core.exceptions import ObjectDoesNotExist

Split_line="------------- "
try:
	if sys.argv[1] == '-h':
		print '''
usage	:	runCmd.py ip	'command' remote_user  track_mark
		./runCmd.py 192.168.2.14 'df -h' alex 34
--single: 	run in single mode,it means you don't need to care about the trackmark stuff,use it when only have one IP to run, this will automatically create a new trackmark in DB
		./runCmd.py 192.168.91.171 df alex --single
		'''
		sys.exit()
except IndexError:
	print "argument error,try -h for help" 
	sys.exit()
try:
	track_mark = sys.argv[4]
	if track_mark == '--single':
		track_mark = MultiRunCounter.AddNumber()
except IndexError:
	track_mark = MultiRunCounter.AddNumber()

try:
	run_user = sys.argv[3]
except IndexError:
	run_user = "Tester_single"

if  sys.argv[-1] == '--single':
	multi_run = 0 
else:
	multi_run = 1

cmd = sys.argv[2]
def cmd_excute():
	try:
		h=db_connector.IP.objects.get(ip = sys.argv[1])
		host= h.ip 
		port= int(h.port )
		username = run_user 
		auth = db_connector.AuthByIpAndRemoteUser.objects.get(ip__ip=host, remoteUser__name= username)
		password = auth.password
		auth_type = auth.authtype
		print password, auth_type
		pkey_file= auth.password 
	except ObjectDoesNotExist:
	    err_msg = 'No access right to host,please make sure you have your TriAquae user bound to remote user %s and host %s' %(run_user,sys.argv[1])
	    logger.RecordLog(sys.argv[1],'CommandExcution',cmd,err_msg,'Error',track_mark,run_user,multi_run)
	    print err_msg
	    sys.exit()

	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())


	try:
		if auth_type == 'ssh-key':
			#pkey_file = '/home/alex/.ssh/id_rsa'
			key = paramiko.RSAKey.from_private_key_file(pkey_file)
			s.connect(host,port,username,pkey=key,timeout=5)
			stdin,stdout,stderr = s.exec_command(cmd)

			result = stdout.read(),stderr.read()
			logger.RecordLog(host,'CommandExcution',cmd,result,'Success',track_mark,run_user,multi_run)
			print Split_line,h.ip,Split_line,'\n',
			for line in result:
				print line,
		elif auth_type == 'ssh':
			s.connect(host,port,username,password,timeout=5)
			stdin,stdout,stderr = s.exec_command(cmd)
			result = stdout.read(),stderr.read()
			logger.RecordLog(host,'CommandExcution',cmd,result,'Success',track_mark,run_user,multi_run)
			print Split_line,h.ip,Split_line,'\n',stdout.read()
			if stderr.read():print 'error happend!',stderr.read()
			for line in result:
				print line,
	except paramiko.AuthenticationException:
		result = "%s ---Authentication failed!\n" %host
		print result
		logger.RecordLog(host,'CommandExcution',cmd,result,'Error',track_mark,run_user,multi_run)
	'''except :
		result = "%s ---timeout or configration error, please manually check the connection!\n" %host
		print result
		logger.RecordLog(host,'CommandExcution',cmd,result,'Error',track_mark,run_user,multi_run)
	'''
	s.close()

if __name__ == '__main__':
	while True:
	  try:
		check_pause = os.popen("cat %s/cmd_pause.txt|grep %s" % (logger.cur_dir,track_mark)).read().strip().split()
		print check_pause
		if check_pause[1] == 'pause':
			time.sleep(1)
			pass
		else:
			cmd_excute()
			break

	  except IndexError:
		cmd_excute()
		break
