#!/usr/bin/env python

import platform
# import subprocess
import os,sys,re,time
# import fileinput
import random_pass
import tri_config
sys.path.append(tri_config.Working_dir)
config_file = 'tri_config.py'

def Usage():
    print
    print '''\033[;32mUsage: %s 
    init        initialization TriAquae to Dev Model
    \033[0m''' % sys.argv[0]
    sys.exit()

try:
    if len(sys.argv[0]) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        Usage()
except IndexError:
    Usage()

''' check system release version '''
sys_info = platform.platform().lower()
if "ubuntu" in sys_info:
    sys_version = "ubuntu"
elif "redhat" in sys_info or "centos" in sys_info:
    sys_version = "redhat"
else:
    print '\033[;31mOnly tested RedHat,Centos and Ubuntu\033[0m'
    sys.exit()



def setup_init():
    Working_dir = os.path.abspath('..')
    # Working_dir = tri_config.Working_dir
    if len(tri_config.MySQL_Pass) == 0:
        import_db = "mysql -u'%s' <TriAquae.sql" % tri_config.MySQL_User
    else:
        import_db = "mysql -u'%s' -p'%s' <TriAquae.sql" % (tri_config.MySQL_User,tri_config.MySQL_Pass)
    #print import_db
    if os.system(import_db) == 0:
        asset_collect_user = tri_config.Asset_collect_user
        asset_user_password = random_pass.main()

        ''' modify asset management script username and password by DengLei '''
        f = open('tri_config.py','r')
        content = f.read()
        line1 = re.sub("Asset_collect_user.*","Asset_collect_user = '%s'" % asset_collect_user,content)
        line2 = re.sub("Asset_user_password.*","Asset_user_password = '%s'" % asset_user_password,line1)
        f = open('tri_config.py','w')
        f.write(line2)
        f.flush()
        f.close()

        f = open('Tri_Scrwer.py','r')
        content = f.read()
        line1 = re.sub("triaquae_user=.*","triaquae_user='%s'" % asset_collect_user,content)
        line2 = re.sub("old_passwd=.*","old_passwd='%s'" % asset_user_password,line1)
        f = open('Tri_Scrwer.py','w')
        f.write(line2)
        f.flush()
        f.close()



        ''' Create tri_connector user '''
        tri_connector_username = tri_config.Tri_connector_username
        tri_connector_password = tri_config.Tri_connector_password
        tri_connector_scripts = tri_config.Tri_connector_baoleiuser
        if os.system('id %s >/dev/null 2>&1' % tri_connector_username) != 0:
            if sys_version == "ubuntu":
                os.system('useradd -r -m -s /bin/bash %s' % (tri_connector_username))
                os.system('echo %s:%s |chpasswd' % (tri_connector_username,tri_connector_password))
                #configure .profile
                f = open('/home/%s/.profile' % tri_connector_username,'a')
                f.write('python %s\nlogout\n' % tri_connector_scripts)
                f.flush()
                f.close()
            elif sys_version == "redhat":
                os.system('useradd %s' % (tri_connector_username))
                os.system('echo %s |passwd %s --stdin >/dev/null 2>&1' % (tri_connector_password,tri_connector_username))
                #configure .profile
                f = open('/home/%s/.bash_profile' % tri_connector_username,'a')
                f.write('python %s\nlogout\n' % tri_connector_scripts)
                f.flush()
                f.close()

        ''' Create all related dirs '''
        os.system('python tri_config.py --initial')

        ''' Timing to perform asset management to collect '''
        if sys_version == "ubuntu":
            cron_path = "/var/spool/cron/crontabs/root"
        elif sys_version == "redhat":
            cron_path = "/var/spool/cron/root"
        cmd = '''
        \n# TriAquae Automatically collect hardware information
        \n00 00 * * * /usr/bin/python %s/TriAquae/backend/Hardware_Multiprocess_Run_Collect_And_write.py\n''' % Working_dir
        f = open(cron_path,'a')
        f.write(cmd)
        f.close()

        print "\033[33;1mInitComplete!\033[0m"

    else:
        print '\033[;31mPlease fix above database configuration error and rerun this step!\033[0m'
        sys.exit(1)


''' Determine the user steps '''
# if sys.argv[1] == "build":
#     try:
#         sys.argv[2]
#     except IndexError:
#         print '\n\033[;31mError: You must specify where to install this program\033[0m\n'
#         sys.exit()

#     if sys.argv[2].startswith('--prefix='):
#         Ins_Dir = sys.argv[2].split('=')[1]
#         if len(Ins_Dir) == 0:
#             Ins_Dir = os.path.abspath('..')
#         setup_build(Ins_Dir)
#     else:
#         Usage()

# elif sys.argv[1] == "init":
#     setup_init()
# else:
#     Usage()

if sys.argv[1] == "init":
    setup_init()
else:
    Usage()

