#!/usr/bin/env python

from multiprocessing import Process,Lock
import sys,os,time

script = sys.argv[0]
list = [1000,1200,1400,1600,1800,10000]
Proce_num_list = []

def worker(num):
    try:
        #print p.name, p.pid, os.getppid()
        if int(num) == int(list[-1]):
            print 'Check out automatically exit.'
            os.system('kill -9 %s' % os.getppid())
            #sys.exit()
        elif num in list:
            print '---------------------------------'
            Proce_num = os.popen('ps -ef|grep -v grep |grep %s |wc -l' % script).read()
            print 'The %s largest number of process: \033[;32m%s\033[0m' % (num ,Proce_num)
            #Proce_num_list += int(Proce_num)
            Proce_num_list.append(int(Proce_num))
            #Proce_num_list[num] = int(Proce_num)
            #print '---------------------------------'
            #print Proce_num_list,'============='
            #print type(Proce_num_list),'============='

        time.sleep(10)

 
    except (KeyboardInterrupt, OSError, AttributeError): 
        sys.exit()


if __name__ == "__main__":
    num = 0
    while True:
        num = num + 1
        Proce_num_list = []
        try:
            p = Process(target=worker ,args=(num,))
            #print p.name, p.pid
            p.start()
        except: 
            p.shutdown()
