#!/usr/bin/env python
# Verify TriAquae user login

import sys,os,getpass
import tri_config,tri_module
triaquae_path = tri_config.Working_dir
triaquae_log = tri_config.Log_dir
sys.path.append(triaquae_path)
os.chdir(triaquae_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TriAquae.settings")
import TriAquae.hosts.views
from django.contrib import auth

def Usage():
    print """
    \033[;32mVerify TriAquae Account Info\033[0m"""
    sys.exit()

def user_auth():
    import baoleihead
    print
    print """\033[;34m------ Verify TriAquae Account Info ------\033[0m"""
    username = raw_input('\033[;35mTriAquae username:\033[0m ')
    password = getpass.getpass('\033[;35mTriAquae password:\033[0m ')
    #print username,password
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        if user.is_authenticated():
            login_user = user.username
        print '\033[;32mTriAquae %s,Auth Success\033[0m' % username
        exec_connector = ('python %s/TriAquae/backend/baoleicmd.py %s') % (triaquae_path, username)
        os.system(exec_connector)
        #exec_connector = ('/bin/bash %s/%s_profile') % (triaquae_log,username)
        #os.system(exec_connector)
    else:
        print '\033[;31mTriAquae %s,Auth Failed\033[0m' % username
        user_auth()

user_auth()
