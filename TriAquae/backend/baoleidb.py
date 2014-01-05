#!/usr/bin/env python

import sys
import db_connector, tri_config
from TriAquae.hosts.models import Group, IP, AuthByIpAndRemoteUser

baoleihost_file = "%s/TriAquae/backend/baoleihost.py" % tri_config.Working_dir

class DBQuery:
    def __init__(self):
        self.num = []

    def ReturnIPNum(self):
        # return ip in group number
        group = Group.objects.all()
        for i in group:
            self.num.append(len(self.DisIP(i)))
        return self.num

    def DisHostIp(self, group_name='all'):
        # return ip and hostname
        if group_name == 'all':
            ip_host = IP.objects.filter().values('ip','hostname') 
        else:
            ip_host = IP.objects.filter(group__name = group_name).values('ip','hostname')
        return ip_host
 
    def AuthIP(self):
        # fast login valid ip
        ip_user = AuthByIpAndRemoteUser.objects.all()
        return ip_user

    def DisGroup(self):
        group = Group.objects.all()
        return group
    
    def DisIP(self, group_name):
        ip = IP.objects.filter(group__name = group_name) 
        return ip
    
    def DisRemotUser(self, remote_ip):
        remote_user = []
        for ip_user in AuthByIpAndRemoteUser.objects.filter(ip__ip = remote_ip):
            remote_user.append(str(ip_user).split()[-1])
        return remote_user

    def Summary(self, remote_ip, remote_user, login_user):
        remote_login_server = AuthByIpAndRemoteUser.objects.get(ip__ip=remote_ip, remoteUser__name=remote_user)
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
        return cmd
    
if __name__ == "__main__":
    DBQuery().DisGroup()
    #DBQuery().DisIP('BJ')
    #DBQuery.DisRemotUser('127.0.0.1')
