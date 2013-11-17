#!/usr/bin/env python

import platform
import subprocess
import os,sys,re,time
import fileinput
import random_pass
import tri_config
sys.path.append(tri_config.Working_dir)
config_file = 'tri_config.py'

def Usage():
    print
    print '''\033[;32mUsage: %s 
    build --prefix=dir  Check and prepare the pre-installation environment 
    install             install software
    init		initialization TriAquae
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


#  setup_build function
#    a. call checking env script (write --prefix into tri_config.py Working_dir)
#    b. install triweb

def setup_build(Ins_Dir):
    print '\033[32;1mStart to check pre-installation environment...................................\n\033[0m'
    ''' install path write into tri_config Working_dir '''
    Working_dir = tri_config.Working_dir
    f = open(config_file,'r')
    content = f.read()
    f.close()
    new_content = re.sub("Working_dir =.*","Working_dir = '%s'" % Ins_Dir,content)
    f = open(config_file,'w')
    f.write(new_content)
    f.flush()
    f.close()

    """
    print '\033[33;1mInstalling TriWeb......\n\033[0m'
    if os.system('/bin/bash triweb_ins.sh %s/TriWeb' % Ins_Dir) == 0:
        print '\033[33;1mInstalling TriWeb done.\n\033[0m'
    else:
        print '\033[31;1mInstalling TriWeb failed.,Please check the reason for failure\n\033[0m'


    print '\033[33;1mInstalling rrdtool......\n\033[0m'
    if os.system('/bin/bash rrdtool_ins.sh %s/rrdtool' % Ins_Dir) == 0:
        print '\033[33;1mInstalling rrdtool done.\n\033[0m'
        print "\nIf no error printed out , you can run '\033[32;40;1mpython setup.py install\033[0m' to install the program \n"
    else:
        print '\033[31;1mInstalling rrdtool failed.,Please check the reason for failure\n\033[0m'
    """
    print "\nIf no error printed out , you can run '\033[32;40;1mpython setup.py install\033[0m' to install the program \n"

#  setup_install function
#    a. According "tri_config" to "Working_dir" parameter of file will copy the installation package to install path

def setup_install():
    Working_dir = tri_config.Working_dir
    if not os.path.exists(Working_dir):
        os.makedirs(Working_dir)       
    #FileCopy='cp -rp bin conf INSTALL.txt include logs modules scripts %s' % Working_dir
    FileCopy='cd ../ && cp -rp manage.py  shellinaboxd  TriAquae  TriSFTP %s' % Working_dir

    os.system(FileCopy)

    time.sleep(3)
    print '\n\033[32;1mInstall Complete\033[0m\n'
    print "\033[33;1m*Please configure your tri_config.py file!\033[0m"
    print "After configured tri_config.py ,you can run '\033[32;40;1mpython setup.py init\033[0m' to complete the initialization!\n"


#  setup_init function
#    a. exec manage.py syncdb (Write to the database table structure)
#    b. create "Tri_connector_username" and "Asset_collect_user" user. use random password into tri_config.py and Hardware_Check_Client_Script.py
#    c. Initialize OpsLog and IP table. OpsLog(track_mark) and IP(localhost info)

def setup_init():
    Working_dir = tri_config.Working_dir
    MySQL_Name = tri_config.MySQL_Name
    MySQL_User = tri_config.MySQL_User
    MySQL_Pass = tri_config.MySQL_Pass
    Tri_IP = tri_config.Tri_IP
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
        #for line in fileinput.input('Tri_Scrwer.py',inplace=1):
        #    content = line.replace("triaquae_user='triaquae'","triaquae_user='%s'" % asset_collect_user).replace("old_passwd='123456'","old_passwd='%s'" % asset_user_password)
        #    print content,

        ''' Copy the modified files '''
        time.sleep(2)
        import shutil
        src1 = "tri_config.py"
        dst1 = "%s/TriAquae/backend/tri_config.py" % Working_dir
        shutil.copyfile(src1, dst1)
        src2 = "Tri_Scrwer.py"
        dst2 = "%s/TriAquae/backend/Tri_Scrwer.py" % Working_dir
        shutil.copyfile(src2, dst2)


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
if sys.argv[1] == "build":
    try:
        sys.argv[2]
    except IndexError:
        print '\n\033[;31mError: You must specify where to install this program\033[0m\n'
        sys.exit()

    if sys.argv[2].startswith('--prefix='):
        Ins_Dir = sys.argv[2].split('=')[1]
        if len(Ins_Dir) == 0:
            Ins_Dir = "/usr/local/TriAquae"
        setup_build(Ins_Dir)
    else:
        Usage()

elif sys.argv[1] == "install":
    setup_install()
elif sys.argv[1] == "init":
    setup_init()
else:
    Usage()

