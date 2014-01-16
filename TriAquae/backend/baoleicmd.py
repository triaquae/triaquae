#!/usr/bin/env python

import os, sys, time, datetime, readline, socket
from baoleidb import DBQuery
import tri_config

# tab completion
readline.parse_and_bind('tab: complete')
# history file
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')

username = sys.argv[1]

head = '''\33[32;1m
                                                        TriConn by TriAquae
________________________________________________________________________________\033[0m
'''

tail = '''\33[32;1m
                                                        TriConn by TriAquae
________________________________________________________________________________\033[0m
'''

class TriConn:
    def __init__(self):
        # definition Type(self.GroupList, self.GroupList, self.UserList)
        self.GroupList = {}
        self.IPList = {}
        self.UserList = {}
        self.summary = []          # save remote_ip and remote_user

    def Help(self):
        print '''\033[32;1m
            ID            Description
            f   fast      fast login
            s   search    search keyword. "q" is quit. "p" is previous.
            b   back      back menu.
            v   view log  view to the last log.
            h   help      parameter description.
            q   quit      exit TriConn.
        \033[0m'''

    def ViewLog(self, lines):
        print '\033[32;1mview log: %s lines\033[0m' % lines
        #with open('/usr/local/TriAquae/TriAquae/logs/audit_2013_12_14_admin.log', 'r+') as f:
        try:
            #with open('%s/TriAquae/logs/audit_%s_%s.log' % (tri_config.Working_dir, time.strftime('%Y_%m_%d'), username),'r+') as f:
            #    for num, i in enumerate(f.readlines()):
            #        print num + 1, i,
            #        if num + 1 == line:
            #            break
            daytime = time.strftime('%Y_%m_%d')
            for num, line in enumerate(reversed(open('%s/TriAquae/logs/audit_%s_%s.log' % (tri_config.Working_dir, daytime, username)).readlines())):
                print num + 1, line,
                if num + 1 == lines:
                    break
        except IOError:
            print '\033[31;1mToday do not produce a log\033[0m'

        #self.InputKey()

    def Connection(self, remote_ip, remote_user):
        try:
            valid_ip = 'ok'
            socket.inet_aton(remote_ip)
            conn = DBQuery().Summary(remote_ip, remote_user, username)
            #print conn
            os.system(conn)
        except:
            valid_ip = 'no'
            print '\033[31;1mInput is not a valid address or address does not exist\033[0m'

        print 'valid_ip', valid_ip,'------------'


    def FastLogin(self):
        data = map(str, DBQuery().AuthIP())
        ip_user = [v.replace('\t', ' ') for v in data]
        
        # raw_input tab 
        def complete(text, state):
            for i in ip_user:
                if i.startswith(text):
                    if not state:
                        return i
                    else:
                        state -= 1
        readline.parse_and_bind("tab: complete")
        readline.set_completer(complete)

        while True:
            ip_user = raw_input('Please input ip and user > ').strip().split()
            if 'q' in ip_user:
                self.Main()
            elif len(ip_user) == 2:
                remote_ip, remote_user = ip_user[0], ip_user[1]
                self.Connection(remote_ip, remote_user)
                break
            else: 
                continue

    #def Search(self, Type, search):
    #    # search keyword. Type(self.GroupList, self.GroupList, self.UserList) search(user search input key)

    #    key = 0
    #    print head
    #    print '\033[35;1m id  group\033[0m'
    #    print
    #    for k, v in Type:
    #        if search in v.lower():
    #            print '\033[32;1m %s. %s\033[0m' % (k, v)
    #            key += 1
    #    else:
    #        if key == 0:
    #            print '\033[31;1m %s Not found\033[0m' % search
    #    print tail 

    def Search(self):
        # search keyword. Type(self.GroupList, self.IPList , self.UserList) search(user search input key)

        data = DBQuery().DisHostIp('all')
        remote_list = {}

        while True:
            search = raw_input('Please input the key words [ q ] > ').strip()
            if search == 'q': self.Main()
            elif len(search) == 0: continue
            else: break

        key = 0
        print head
        print '\033[35;1m id  search result\033[0m'
        print
        for i in data:
            if search in i['hostname'].lower() or search in i['ip'].lower():
                key += 1
                print '\033[32;1m  %s. %s \033[36;1m[%s]\033[0m \033[0m' % (key, i['hostname'], i['ip'])
                remote_list[key] = i['ip']
            else:
                pass
        if key == 0:
            print '\033[31;1m %s Not found\033[0m' % search
            self.Search()
        print tail 

        while True:
            try:
                choose = raw_input('Please input id [ q | p ] > ').strip()
                if choose == 'q':
                    self.Main()
                if choose == 'p':
                    self.Search()
                elif len(choose) == 0:
                    continue
                elif int(choose) in remote_list.keys():
                    #print remote_list[int(choose)],'=========='
                    self.summary.append(remote_list[int(choose)])
                    self.ChooseRemoteUser(remote_list[int(choose)])
                else:
                    print '\033[31;1m Please input a valid id number\033[0m'
                    continue
            except ValueError:
                print '\033[31;1m Please input id number \033[0m'


    def Display(self, title, Type, dbquery, group='None'):
        # Display all info
        id = 0

        print head
        for n in self.summary:
            print "\033[35;1m%s\033[0m =>" % n,
        print 
        print 
        print '\033[32;1m id  %s\033[0m' % title
        print

        data = map(str, dbquery)
        num = DBQuery().ReturnIPNum()
        #print 'data : ', data
        #print 'num : ', num
        IpList = DBQuery().DisHostIp(group)
        for i in data:
	    id += 1
            if title == 'group':
                # Show the IP number
                print '\033[32;1m  %s. %s \033[36;1m[%s]\033[0m \033[0m' % (id , i, num[id - 1])
            elif title == 'ip':
                # display hostname and ip
                try:
                    print '\033[32;1m  %s. %s \033[36;1m[%s]\033[0m \033[0m' % (id , IpList[id - 1]['hostname'], IpList[id - 1]['ip'])
                except IndexError:
                    pass
            else:
                print '\033[32;1m  %s. %s \033[0m' % (id , i)

            Type[id] = str(i)
        print tail


    def InputKey(self, Type, next_page):
        # judge user input Type(self.GroupList, self.GroupList, self.UserList)

        while True:
            #input = raw_input('Please choose items [ id | f | s | b | v | h | q ]: ').strip()
            input = raw_input('[help | search | fast | back | quit] #: ').strip()
            #print 'input : ', input
            #print 'Type : ', map(str, Type.keys())
            #print 'self.summary : ', self.summary
            if input in map(str, Type.keys()):   # gain user input id
                element = Type[int(input)]
                self.summary.append(element)  # summary list
                #print 'element : ', element
                next_page(element)               # skip next page
            elif len(input) == 0:
                continue
            elif input == 'f' or input == 'fast':                   # fast login.
                self.FastLogin()
            elif input == 's' or input == 'search':                   # search keyword.
                #search = raw_input('Please input the key words > ').strip()
                self.Search()
                #self.Search()
            elif input == 'b' or input == 'back':                   # backend menu
                self.Main()
            elif input[0] == 'v':                   # view the last log
                try:
                    lines = int(input.split()[1])
                    self.ViewLog(lines)
                except IndexError:
                    self.ViewLog(lines=10)
                except ValueError:
                    pass
            elif input == 'h' or input == 'help':                   # display help
                self.Help()
            elif input == 'q':                   # quit TriConn
                print '\n\033[31;1mInput "quit" TriConn Exit\033[0m'
            elif input == 'quit':
                sys.exit(0)

    def Summary(self, remote_user):
        #print self.summary,'|||||||||||'
        #print self.summary[0],'|||||||||||'
        #print self.summary[1],'|||||||||||'
        try:
            print 'summmar : ',self.summary
            remote_ip = self.summary[0]
            remote_user = self.summary[1]
            self.Connection(remote_ip, remote_user)
        except:
            print '\033[31;1m%s\033[0m permissions deny.' % remote_ip
        

    def ChooseRemoteUser(self, ip):
        # Show the IP of users
        self.Display('user', self.UserList, DBQuery().DisRemotUser(ip))
        self.InputKey(self.UserList, self.Summary)


    def ChooseRemoteIP(self, group):
        # The IP under the display group.
        self.summary = []
        self.Display('ip', self.IPList, DBQuery().DisIP(group), group)
        self.InputKey(self.IPList, self.ChooseRemoteUser)


    def Main(self):
        # Display all groups.
        #print self.GroupList, self.IPList, self.UserList
        self.summary = []
        self.Display('group', self.GroupList, DBQuery().DisGroup())   # Query the database, display menu
        self.InputKey(self.GroupList, self.ChooseRemoteIP)            # Determine the user to enter the keywords, (self.GroupList is Type | self.ChooseRemoteIP is next page function) 


    
if __name__ == '__main__':
    while True:
        try:
            TriConn().Main()
        except KeyboardInterrupt:
            print '\n\033[31;1mInput "quit" TriConn Exit\033[0m'
            continue
        #print '\n\033[31;1mTriAquae TriConn Exit\033[0m'
#if __name__ == '__main__':
#    try:
#        TriConn().Main()
#    except KeyboardInterrupt:
#        while True:
#            print '........'
#            TriConn().Main()
#        #print '\n\033[31;1mTriAquae TriConn Exit\033[0m'
