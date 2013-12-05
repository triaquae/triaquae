#!/usr/bin/env python
#Author: Deng Lei
import os
import sys
import crypt
import subprocess
import platform
triaquae_user='triaquae'
save_dir='/tmp'
old_passwd='5jykPF'
try:
    if sys.argv[1] == '-h':
        print '''
usage   :       ./Hardware_Check_Client_Script.py  option
-y	:       if you run this check script in this option,it will auto solve problem of script found
                ./Hardware_Check_Client_Script.py  -y 
-n	:       if you run this check script in this option,it will only print found problem,no auto solve
                ./Hardware_Check_Client_Script.py  -n
                '''
        sys.exit()
except IndexError:
        print "argument error,try -h for help"
        sys.exit()
option_auto=sys.argv[1]
###check run user 
if os.getuid() == 0:
    print "\033[1;32;40m%s   %s\033[0m" %('Checking this script run user is root!','Pass')
else:
    print "\033[1;31;40m%s   %s\033[0m" %('Checking this script run user is root!','No pass')
    sys.exit(1)
###check python version
now_version=((sys.version).split()[0])[0:3]
require_version='2.6'
if now_version >= require_version:
    print "\033[1;32;40m%s   %s\033[0m" %('Checking python version is >2.6','Pass')
else:
    print "\033[1;31;40m%s   %s\033[0m" %('Checking python version is <2.6','Not pass')
###check install modules
modules=['subprocess','platform','json','crypt']
for i in modules:
    try:
        __import__(i)
    	print "\033[1;32;40m%s\033[0m" %'Checking "%s" modules   %s'%(i,'Pass')
    except Exception,e:
	print "\033[1;31;40m%s\033[0m   %s" %(e,'No pass')
	if option_auto == '-y':
	    print 'i will auto install this modules'
	    system=platform.platform()
	    for i in modules:
		cmd='/usr/bin/easy_install %s' %i
		os.system(cmd)
		if 'Window' in system:
		    print "\033[1;31;40m%s\033[0m   %s" %('hardware check environment script not support window system','No pass')
###check triaquae exist
triaquae_passwd=crypt.crypt(old_passwd,"TR")
cmd='useradd -p %s -m %s'%(triaquae_passwd,triaquae_user)
check_value=((subprocess.Popen("grep %s /etc/passwd|wc -l"%(triaquae_user),shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
if check_value == '1':
    print "\033[1;32;40m%s    %s\033[0m" %('Checking "Triaquae" user in the /etc/passwd!','Pass')
else:
    print "\033[1;31;40m%s    %s\033[0m" %('Checking "Triaquae" user not in the /etc/passwd','No pass')
    if option_auto == '-y':
        print "\033[1;32;40m%s\033[0m" %'now i will auto create this user and modify the one passwd'
        os.system(cmd)
###check triaquae user in sudoer
info='%s ALL=NOPASSWD:/usr/bin/python /tmp/Hardware_Collect_Script.py\n'%(triaquae_user)
f=open('/etc/sudoers','a+')
if info in f.readlines():
    print "\033[1;32;40m%s   %s\033[0m" %('Checking "Triaquae" user in the /etc/sudoers!','Pass')
else:
    print "\033[1;31;40m%s   %s\033[0m" %('Checking "Triaquae" user not in the /etc/sudoers!','No pass')
    if option_auto == '-y':
        print  "\033[1;32;40m%s\033[0m" %'i will input "triaquae ALL=NOPASSWD:/usr/bin/python /tmp/Hardware_Collect_Script.py" in the /etc/sudoers!'
        f.write(info)
f.close()
