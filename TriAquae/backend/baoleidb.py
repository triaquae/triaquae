#!/usr/bin/env python

import sys
import db_connector
from TriAquae.hosts.models import Group, IP, AuthByIpAndRemoteUser

remote_ip = '192.168.2.2'
remote_user = 'coral'
baoleihost_file = "/usr/local/TriAquae/TriAquae/backend/baoleihost.py"
login_user = 'admin'

def DisGroup():
    group = Group.objects.all()
    return group

def DisIP(group_name):
    ip = IP.objects.filter(group__name=group_name) 
    return ip
    #print ip

def DisRemotUser(remote_ip, remote_user):
    remote_user = AuthByIpAndRemoteUser.objects.get(ip__ip=remote_ip, remoteUser__name=remote_user)
    return remote_user

def RemoteIP():
    remote_login_server = AuthByIpAndRemoteUser.objects.get(ip__ip=remote_ip, remoteUser__name=remote_user)
    #print remote_login_server.authtype, remote_login_server.password,'==============='
    protocol_type = remote_login_server.authtype
    password = remote_login_server.password
    key_path = remote_login_server.password
    port = IP.objects.get(ip=remote_ip).port
    if protocol_type == "ssh":
            protocol = "SSH_PASSWD"
            cmd = "python %s %s %s %s %s %s %s\n" % (baoleihost_file,remote_ip,port,remote_user,protocol,password,login_user)
    elif protocol_type == "ssh-key":
            protocol = "SSH_KEY"
            cmd = "python %s %s %s %s %s %s %s\n" % (baoleihost_file,remote_ip,port,remote_user,protocol,key_path,login_user)
    print cmd

if __name__ == "__main__":
    pass
    #DisGroup()
    DisIP('BJ')
    #DisRemotUser(remote_ip, remote_user)
