#!/usr/bin/env python

import sys
import db_connector
from TriAquae.hosts.models import Group, IP, AuthByIpAndRemoteUser

#remote_ip = '192.168.2.2'
#remote_user = 'coral'
baoleihost_file = "/usr/local/TriAquae/TriAquae/backend/baoleihost.py"

class DBQuery:
    def __init__(self):
        self.num = []

    def ReturnNum(self, type, next_type):
        for i in type:
            self.num.append(len(next_type(i)))
        #return self.num
        print 'self.num', self.num,'================='
        return self.num

    def DisGroup(self):
        group = Group.objects.all()
        #number = self.ReturnNum(group, self.DisIP)
        #print 'group', number,'--------'
        #return group, self.num
        return group
    
    def DisIP(self, group_name):
        ip = IP.objects.filter(group__name = group_name) 
        #number = self.ReturnNum(ip, self.DisRemotUser)
        #print 'ip', number,'--------'
        #return ip, number
        return ip
    
    def DisRemotUser(self, remote_ip):
        remote_user = []
        for ip_user in AuthByIpAndRemoteUser.objects.filter(ip__ip = remote_ip):
            remote_user.append(str(ip_user).split()[-1])
        #for i in remote_user:
        #    self.num.append(0)
        #return remote_user, self.num
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
