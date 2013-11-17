#!/usr/bin/env python

import tri_module
import base64
from binascii import hexlify
import getpass
import os
import select
import socket
import sys
import threading
import time
import traceback

import paramiko
import interactive
import db_connector, logger, MultiRunCounter

def Usage():
    print """
    \033[;32mUsage: python %s "hostname port username mode [passwd | rsa_key] TriAquae User" \033[0m""" % sys.argv[0]
    sys.exit()

try:
    if len(sys.argv[0]) == 1 or sys.argv[1] == "-h":
       Usage()
except IndexError:
    Usage()
    sys.exit()

django_loginuser = sys.argv[6]
hostname = sys.argv[1]
port = int(sys.argv[2])
username = sys.argv[3]
mode = sys.argv[4]
if mode == "SSH_PASSWD":
    password = sys.argv[5]
    connect_cmd = "python %s %s %s %s %s %s %s" %(sys.argv[0],hostname,port,username,mode,password,django_loginuser)
elif mode == "SSH_KEY":
    key_path = sys.argv[5]
    connect_cmd = "python %s %s %s %s %s %s %s" %(sys.argv[0],hostname,port,username,mode,key_path,django_loginuser)
else:
    Usage()


def agent_auth(transport, username):
    """
    Attempt to authenticate to the given transport using any of the private
    keys available from an SSH agent.
    """
    
    agent = paramiko.Agent()
    agent_keys = agent.get_keys()
    if len(agent_keys) == 0:
        return
        
    for key in agent_keys:
        print 'Trying ssh-agent key %s' % hexlify(key.get_fingerprint()),
        try:
            transport.auth_publickey(username, key)
            print '... success!'
            return
        except paramiko.SSHException:
            print '... nope.'


def manual_auth(username, hostname,mode):
    #print username,hostname,mode
    if mode == "SSH_PASSWD":
        pw = password
        t.auth_password(username, pw)
    elif mode == "SSH_KEY":
        key = key_path
        key = paramiko.RSAKey.from_private_key_file(key)
        t.auth_publickey(username, key)


# setup logging
#paramiko.util.log_to_file('demo.log')
#paramiko.util.log_to_file('/server/scripts/py/django/Coral/web01/logs/demo.log')


# now connect
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
except Exception as error:
    print '*** Connect failed: ' + str(error)
    #traceback.print_exc()
    ''' record login faile to opslog table'''
    track_mark = MultiRunCounter.AddNumber()
    logger.RecordLogSummary('CREATE','TriConnector',track_mark,username,connect_cmd,"1",django_loginuser,error,0,1)
    sys.exit(1)

try:
    t = paramiko.Transport(sock)
    try:
        t.start_client()
    except paramiko.SSHException:
        print '*** SSH negotiation failed.'
        sys.exit(1)

    try:
        keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    except IOError:
        try:
            keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
        except IOError:
            print '*** Unable to open host keys file'
            keys = {}

    # check server's host key -- this is important.
    key = t.get_remote_server_key()
    if not keys.has_key(hostname):
        print '*** WARNING: Unknown host key!'
    elif not keys[hostname].has_key(key.get_name()):
        print '*** WARNING: Unknown host key!'
    elif keys[hostname][key.get_name()] != key:
        print '*** WARNING: Host key has changed!!!'
        sys.exit(1)
    else:
        print '*** Host key OK.'


    # get username
    if username == '':
        default_username = getpass.getuser()
        username = raw_input('Username [%s]: ' % default_username)
        if len(username) == 0:
            username = default_username

    agent_auth(t, username)
    if not t.is_authenticated():
        #manual_auth(username, hostname)
        manual_auth(username, hostname,mode)
    if not t.is_authenticated():
        print '*** Authentication failed. :('
        t.close()
        sys.exit(1)

    chan = t.open_session()
    chan.get_pty()
    chan.invoke_shell()
    ''' record login faile to opslog table'''
    track_mark = MultiRunCounter.AddNumber()
    logger.RecordLogSummary('CREATE','TriConnector',track_mark,username,connect_cmd,"1",django_loginuser,"success",1,0)
    #print '*** Here we go!'
    print
    interactive.interactive_shell(chan,django_loginuser,hostname)
    chan.close()
    t.close()

#except Exception, e:
except (Exception, paramiko.AuthenticationException) as error:
    #print '*** Caught exception: ' + str(error.__class__) + ': ' + str(error)
    print error
    ''' record login faile to opslog table'''
    track_mark = MultiRunCounter.AddNumber()
    logger.RecordLogSummary('CREATE','TriConnector',track_mark,username,connect_cmd,"1",django_loginuser,error,0,1)

    #traceback.print_exc()
    try:
        t.close()
    except:
        pass
    sys.exit(1)


