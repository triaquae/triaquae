#!/usr/bin/env python
###Author By DengLei
###Email is 244979152@qq.com
import subprocess
import platform
import json
import os
#from collections import namedtuple
msg=platform.platform()
if 'Window' in msg:
    print 'hardware script not support win'
Device_Type=((subprocess.Popen("/usr/sbin/dmidecode -t 1|grep Manufacturer|cut -d ':' -f2|cut -d ' ' -f2",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
Device_Model=((subprocess.Popen("/usr/sbin/dmidecode -t 1|grep 'Product Name'|cut -d : -f2",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
Device_Sn=((subprocess.Popen("/usr/sbin/dmidecode -t 1|grep 'Serial Number'|cut -d : -f2",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
System_Kernel=((subprocess.Popen("/bin/uname -a",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
Ethernet_Interface=(subprocess.Popen("lspci|grep 'Ethernet'",shell=True,stdout=subprocess.PIPE)).stdout.readlines()
if len(Ethernet_Interface)>1:
        Ethernet_Interface_New=[]
        for i in range(len(Ethernet_Interface)):
		Ethernet_Interface_New.append(Ethernet_Interface[i].strip('\n'))
else:
    Ethernet_Interface_New = Ethernet_Interface
Memory_Slots_Number=((subprocess.Popen("/usr/sbin/dmidecode |grep -A16 'Memory Device$'|grep 'Size'|wc -l",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
Memory_Slots_All=(subprocess.Popen("/usr/sbin/dmidecode |grep -A16 'Memory Device$'|grep 'Size'",shell=True,stdout=subprocess.PIPE).stdout.readlines())
if len(Memory_Slots_All)>= 1:
	Memory_Slots_All_New=[]
        for i in range(len(Memory_Slots_All)):
                Memory_Slots_All_New.append(Memory_Slots_All[i].strip('\n'))
else:
    Memory_Slots_All_New = Memory_Slots_All
Physical_Memory=((subprocess.Popen("""cat /proc/meminfo |grep MemTotal |awk '{print $2/1024, "MB"}'""", shell=True,stdout=subprocess.PIPE).stdout.readline().strip('\n') ))
Logical_Cpu_Cores=((subprocess.Popen("grep -c 'model name' /proc/cpuinfo",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
Physical_Cpu_Cores=((subprocess.Popen("cat /proc/cpuinfo |grep 'physical id'|uniq -c|wc -l",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
Physical_Cpu_Model=((subprocess.Popen("cat /proc/cpuinfo |grep 'model name' |head -n 1|cut -d : -f2",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
Physical_Cpu_MHz=(subprocess.Popen("grep 'cpu MHz' /proc/cpuinfo| awk -F ':' '{print $2}'|cut -d ' ' -f2",shell=True,stdout=subprocess.PIPE)).stdout.readlines()
if len(Physical_Cpu_MHz)>= 1:
        Physical_Cpu_MHz_New=[]
        for i in range(len(Physical_Cpu_MHz)):
                Physical_Cpu_MHz_New.append(Physical_Cpu_MHz[i].strip('\n'))
else:
    Physical_Cpu_MHz_New = Physical_Cpu_MHz
System_Version=platform.platform()
Hard_Disk=(subprocess.Popen("parted -l | grep Disk | grep -v mapper ",shell=True,stdout=subprocess.PIPE)).stdout.readlines()
if len(Hard_Disk)>= 1:
        Hard_Disk_New=[]
        for i in range(len(Hard_Disk)):
                Hard_Disk_New.append(Hard_Disk[i].strip('\n'))
else:
    Hard_Disk_New = Hard_Disk
System_Networ_Card=(subprocess.Popen("/sbin/ifconfig|grep HWaddr|awk '{print $1}'",shell=True,stdout=subprocess.PIPE)).stdout.readlines()
System_Ip=(subprocess.Popen("/sbin/ifconfig|grep 'inet addr:'|grep -Ev '127.0.0.1|169'|cut -d: -f2|awk '{print $1}'",shell=True,stdout=subprocess.PIPE)).stdout.readlines()
if len(System_Networ_Card) == len(System_Ip):
    System_Ip_New=[]
    for i in range(len(System_Networ_Card)):
	System_Ip_New.append('%s:%s'%(System_Networ_Card[i].strip('\n'),System_Ip[i].strip('\n')))
else:
    System_Ip_New = System_Ip
System_Mac=(subprocess.Popen("/sbin/ifconfig -a|grep 'HWaddr'|grep -v usb0|awk '{print $NF}'",shell=True,stdout=subprocess.PIPE)).stdout.readlines()
if len(System_Networ_Card) == len(System_Mac):
	System_Mac_New=[]    
	for i in range(len(System_Networ_Card)):
	    System_Mac_New.append('%s:%s'%(System_Networ_Card[i].strip('\n'),System_Mac[i].strip('\n')))
else:
    System_Mac_New = System_Mac
System_Hostname= platform.node()
System_Hostid= ((subprocess.Popen("/usr/bin/hostid",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
System_Swap= ((subprocess.Popen("free -m|grep Swap|awk '{print $2}'",shell=True,stdout=subprocess.PIPE)).stdout.readline()).strip('\n')
write_here = '/tmp'
write_file = file('%s/triaquae_asset_collection.temp'%(write_here), 'w')
send = json.dumps({'Device_Type': Device_Type, 'Device_Model': Device_Model, 'Device_Sn': Device_Sn, 'System_Kernel': System_Kernel, 'Ethernet_Interface': Ethernet_Interface_New, "Memory_Slots_Number": Memory_Slots_Number, 'Memory_Slots_All': Memory_Slots_All_New ,'Physical_Memory': Physical_Memory, 'Logical_Cpu_Cores': Logical_Cpu_Cores, 'Physical_Cpu_Cores': Physical_Cpu_Cores, 'Physical_Cpu_Model': Physical_Cpu_Model, 'Physical_Cpu_MHz': Physical_Cpu_MHz_New, 'System_Version': System_Version, 'Hard_Disk': Hard_Disk_New, 'System_Ip': System_Ip_New, 'System_Mac': System_Mac_New, 'System_Hostname': System_Hostname, 'System_Hostid': System_Hostid, 'System_Swap': System_Swap})
write_file.write(send)
write_file.close()
