#!/usr/bin/env python
#Author: Alex Li

import os,sys
import time,datetime,json
import tri_config
date =time.strftime('%Y_%m_%d %H\:%M\:%S')
snmp_oid_list = {
		#'SystemVersion': '.1.3.6.1.2.1.1.1.0',
		#'RunningProcessNum' : '.1.3.6.1.2.1.25.4.2.1.2|wc -l',
		#'EthernetName' : '1.3.6.1.2.1.31.1.1.1.1.2',
		#'MainIpAddress': ".1.3.6.1.2.1.4.20|grep IpAddress|grep -v '127.0.0.1'",
		#'TotalRAM' : '.1.3.6.1.2.1.25.2.2', # in KB
		#'TotalSWAP': '.1.3.6.1.4.1.2021.4.3.0', # in KB
		#'TotalSharedMEM': '.1.3.6.1.4.1C.2021.4.15.0',  # in KB
		#'TotalDiskSize' : '.1.3.6.1.4.1.2021.9.1.6.1', #in KB\
		#'UsedSpace' : '.1.3.6.1.4.1.2021.9.1.9.1', # in percentage
		#'PartitionName' : '.1.3.6.1.4.1.2021.9.1.3.1', #string
		'StorageTable' : '''hrStorageTable|awk -F'::' '{print $2 ,"None"}' ''' , # return RAM and Disk info
		'MemTable':  '''.1.3.6.1.4.1.2021.4 |awk -F'::' '{print $2 ,"None"}' ''',
		#'1MinLoad' : '.1.3.6.1.4.1.2021.10.1.3.1', 
		#'5MinLoad' : '.1.3.6.1.4.1.2021.10.1.3.2',
		#'15MinLoad' : '.1.3.6.1.4.1.2021.10.1.3.3', 
		'Load' : ".1.3.6.1.4.1.2021.10|grep laLoad.[0-9]|awk -F: '{print $4}'|xargs echo 'load='",
		'CpuIdle' : '.1.3.6.1.4.1.2021.11', # in percentage
		'CpuUsage': '''.1.3.6.1.4.1.2021.11|grep Cpu |awk -F'::' '{print $2}' ''',	
		'IfDescr' : "ifDescr |awk -F'::' '{print $2}'",
		'IfIn'	: "ifInOctets |awk -F'::' '{print $2}' ",
		'IfOut' : "ifOutOctets |awk -F'::' '{print $2}'",
	}
	
try:
  err_msg = '''\033[31;1mError:wrong argument,please check!!!\033[0m
usage: ./snmp_monitory.py -v 2c -c public -h 192.168.2.33\n
	./snmp_monitor.py -v 3 -u my_uername -l auth -a MD5 -A my_password -h 192.168.3.42\n
	'''
  if sys.argv[1] == '-h' or len(sys.argv) == 0:
	print err_msg
	sys.exit()
  if '-v'  and '-h' in sys.argv:
	snmp_version =  sys.argv[sys.argv.index('-v') + 1]
	if snmp_version == '2c':
		community_name = sys.argv[sys.argv.index('-c') + 1]
	elif snmp_version == '3':
		snmp_user = sys.argv[sys.argv.index('-u') + 1]
		snmp_auth = sys.argv[sys.argv.index('-l') + 1]
		snmp_MD5 = sys.argv[sys.argv.index('-a') + 1]
		snmp_pass = sys.argv[sys.argv.index('-A') + 1]
	
	ip_addr = sys.argv[sys.argv.index('-h') + 1]
  else:
	print err_msg	
	sys.exit()
except IndexError:
	print err_msg
	sys.exit()
except ValueError:
        print err_msg
        sys.exit() 
snmp_data = {'Mem_list' : [],'Ip_speed' : []}
Mem_list = []
Cpu_usage = []

performance_dic = {}


def insert_to_db(IP_ADDR, SNMP_STATUS, SNMP_DATA ):
	cmd = '''echo %s '|' %s '|' '%s' >> %s''' %(IP_ADDR, SNMP_STATUS, json.dumps(SNMP_DATA),tri_config.Snmp_temp_log)
	os.system(cmd)
	pass
def test_snmp():
	if snmp_version == '2c':
		cmd = "snmpwalk -v %s -c %s %s .1.3.6.1.4.1.2021.10" %  (snmp_version, community_name, ip_addr)
		#cmd = "snmpwalk -v %s -c %s %s system" %  (snmp_version, community_name, ip_addr)
	if snmp_version == '3':
		cmd = "snmpwalk -v %s -u %s -l %s -a %s -A %s %s .1.3.6.1.4.1.2021.10" %(snmp_version, snmp_user, snmp_auth, snmp_MD5, snmp_pass, ip_addr)
	cmd_result = os.system(cmd)
	if cmd_result != 0:
		err_msg = "Could not connect to SNMP,please check the network or snmp configuration!"
		insert_to_db(ip_addr, 'Timeout', err_msg)
		print err_msg 
		sys.exit()
#Test snmp before run bulk snmp commands
test_snmp()

#run bulk snmp commands to gather system performance data
for name,oid in snmp_oid_list.items():
        if snmp_version == '2c':
                cmd = "snmpwalk -v %s -c %s %s %s" %  (snmp_version, community_name, ip_addr,oid)
        if snmp_version == '3':
                cmd = "snmpwalk -v %s -u %s -l %s -a %s -A %s %s %s" %(snmp_version, snmp_user, snmp_auth, snmp_MD5, snmp_pass, ip_addr, oid)
	cmd_result = os.popen(cmd).read()
	if name == 'StorageTable' or name == 'MemTable':
		snmp_data['Mem_list'].append(cmd_result.split('\n'))
		continue
	if name == 'CpuUsage':
		snmp_data[name] = cmd_result
		continue
	if name == 'IfDescr' or name == 'IfIn' or name == 'IfOut':
		snmp_data['Ip_speed'].append(cmd_result.split('\n'))
                continue		
	result = cmd_result.strip('\n').split('=')
	snmp_data[name] = result[1:]


STEP = 2
HEARTBEAT = 600 
Period_1h = 'now-1h'
Period_1d = "now-1d"
PIC_DIR = tri_config.RRDTOOL_png_dir 
RRD_DIR = tri_config.RRDTOOL_rrd_file_dir
def draw_graph(rrdfile_name,DS,ip,addtional=0):
	if DS == 'CpuUsage':
		os.system('''rrdtool graph %s/%s_%s_%s.png \\
		--start now-1h --title "CPU Usage" \\
		--vertical-label "Idle in percentage" \\
		--height 200 --width 600 \\
		--slope-mode --alt-autoscale \\
		DEF:value1=%s:cpu_idle:MAX  \\
		DEF:value2=%s:cpu_system:MAX \\
		DEF:value3=%s:cpu_user:MAX \\
		AREA:value1#00ff00:"cpu_idle %s" \\
		AREA:value2#0000ff:"cpu_system %s" \\
		AREA:value3#E04000:"cpu_user %s"\\
		COMMENT:"Last update %s" ''' % (PIC_DIR,ip,DS,Period_1h, rrdfile_name, rrdfile_name, rrdfile_name,cpu_idle,cpu_system,cpu_user, date)  )
                os.system('''rrdtool graph %s/%s_%s_%s.png \\
                --start now-1d --title "CPU Usage" \\
                --vertical-label "Idle in percentage" \\
                --height 200 --width 600 \\
                --slope-mode --alt-autoscale \\
                DEF:value1=%s:cpu_idle:MAX  \\
                DEF:value2=%s:cpu_system:MAX \\
                DEF:value3=%s:cpu_user:MAX \\
                AREA:value1#00ff00:"cpu_idle %s" \\
                AREA:value2#0000ff:"cpu_system %s" \\
                AREA:value3#E04000:"cpu_user %s"\\
                 COMMENT:"Last update %s" ''' % (PIC_DIR,ip,DS,Period_1d, rrdfile_name, rrdfile_name, rrdfile_name,cpu_idle,cpu_system,cpu_user, date)  )
        

	if DS == 'Ip_speed':
		eth_name = addtional
		print eth_name
		os.system('''rrdtool graph %s/%s_%s_%s.png \\
		--start now-1h --title "%s speed " \\
		--vertical-label "kb" \\
		--height 200 --width 600 \\
		--slope-mode --alt-autoscale 	\\
		DEF:value1=%s:in:MAX \\
		DEF:value2=%s:out:MAX \\
		AREA:value1#f007:"in_speed %sBit" \\
		AREA:value2#0f05:"out_speed %sBit" \\
		COMMENT:"Last update %s" \\
		''' %(PIC_DIR,ip,eth_name,Period_1h,eth_name,rrdfile_name,rrdfile_name,in_speed,out_speed ,date ))
                os.system('''rrdtool graph %s/%s_%s_%s.png \\
                --start now-1d --title "%s speed " \\
                --vertical-label "kb" \\
                --height 200 --width 600 \\
                --slope-mode --alt-autoscale    \\
                DEF:value1=%s:in:MAX \\
                DEF:value2=%s:out:MAX \\
                AREA:value1#f007:"in_speed %sBit" \\
                AREA:value2#0f05:"out_speed %sBit" \\
                COMMENT:"Last update %s" \\
                ''' %(PIC_DIR,ip,eth_name,Period_1d,eth_name,rrdfile_name,rrdfile_name,in_speed,out_speed ,date ))
	if DS == 'Load':
		os.system('''rrdtool graph %s/%s_%s_%s.png \\
		--start now-1h --title "System Load Average" \\
		--vertical-label "LOAD AVERAGE" \\
		--height 200 --width 600 \\
		--slope-mode --alt-autoscale \\
 		DEF:value1=%s:Load_1:MAX \\
		DEF:value2=%s:Load_5:MAX \\
		DEF:value3=%s:Load_15:MAX \\
		AREA:value1#00ff00:"1min %s"  \\
		LINE2:value2#0000ff:"5min %s" \\
		LINE3:value3#E04000:"15min %s" \\
		COMMENT:"Last update %s"  ''' % (PIC_DIR,ip,DS,Period_1h,rrdfile_name,rrdfile_name,rrdfile_name,load_1,load_5,load_15,date )  )
                os.system('''rrdtool graph %s/%s_%s_%s.png \\
                --start now-1d --title "System Load Average" \\
                --vertical-label "LOAD AVERAGE" \\
                --height 200 --width 600 \\
                --slope-mode --alt-autoscale \\
                DEF:value1=%s:Load_1:MAX \\
                DEF:value2=%s:Load_5:MAX \\
                DEF:value3=%s:Load_15:MAX \\
                AREA:value1#00ff00:"1min %s"  \\
                LINE2:value2#0000ff:"5min %s" \\
                LINE3:value3#E04000:"15min %s" \\
                COMMENT:"Last update %s"  ''' % (PIC_DIR,ip,DS,Period_1d,rrdfile_name,rrdfile_name,rrdfile_name,load_1,load_5,load_15,date )  )
	if DS == 'Mem_list':
		os.system('''rrdtool graph %s/%s_%s_%s.png \\
		--start now-1h --title "Memory usage" \\
		--vertical-label "MEMORY(MB)"	\\
		--height 200 --width 600 \\
		--slope-mode --alt-autoscale \\
		DEF:value1=%s:RAM_used:MAX  \\
		DEF:value2=%s:Cached:MAX \\
		DEF:value3=%s:SWAP_used:MAX \\
		AREA:value1#00ff00:"RAM_used %sM" \\
		AREA:value2#006600:"Cached %sM"\\
		LINE3:value3#E04000:"SWAP_used %sM"\\
		COMMENT:"      " \\
		COMMENT:"Last update %s" \\
		COMMENT:"Total_RAM %sM" \\
		COMMENT:"Total_SWAP %sM" \\
		''' % (PIC_DIR,ip,DS,Period_1h,rrdfile_name,rrdfile_name,rrdfile_name,MEM_used,Cached_MEM,SWAP_used, date,Total_RAM,Total_SWAP  ))
                os.system('''rrdtool graph %s/%s_%s_%s.png \\
                --start now-1d --title "Memory usage" \\
                --vertical-label "MEMORY(MB)"   \\
                --height 200 --width 600 \\
                --slope-mode --alt-autoscale \\
                DEF:value1=%s:RAM_used:MAX  \\
                DEF:value2=%s:Cached:MAX \\
                DEF:value3=%s:SWAP_used:MAX \\
                AREA:value1#00ff00:"RAM_used %sM" \\
                AREA:value2#006600:"Cached %sM"\\
                LINE3:value3#E04000:"SWAP_used %sM"\\
                COMMENT:"      " \\
                COMMENT:"Last update %s" \\
                COMMENT:"Total_RAM %sM" \\
                COMMENT:"Total_SWAP %sM" \\
                ''' % (PIC_DIR,ip,DS,Period_1d,rrdfile_name,rrdfile_name,rrdfile_name,MEM_used,Cached_MEM,SWAP_used, date,Total_RAM,Total_SWAP  ))
for name,data in  snmp_data.items():
	rrdfile = '%s/%s_%s.rrd' % (RRD_DIR,ip_addr,name)
	
	if  name == 'CpuIdle':
		cpu_idle = data[0].split()[1]
		print cpu_idle
		try:
			os.lstat(rrdfile)
		except OSError:
			os.system('''rrdtool create %s --step 50  DS:%s:GAUGE:%s:0:100  RRA:MAX:0.5:1:2880 ''' % (rrdfile,name,HEARTBEAT) ) 
		os.system("rrdtool update %s --template %s  N:%d" % (rrdfile,name,int(cpu_idle) )) 
		draw_graph(rrdfile,name,ip_addr)
	elif name == 'CpuUsage':
		cpu_dic = {}
		info_list =  data.split('\n')
		for i in info_list:
			if len(i) == 0:break
			cpu_dic[i.split()[0]] = i.split()[3]
		cpu_idle = cpu_dic['ssCpuIdle.0']
		cpu_system = cpu_dic['ssCpuSystem.0']
		cpu_user = cpu_dic['ssCpuUser.0']
		performance_dic['CpuIdle'] = cpu_idle
		print 'CpuUsage:',cpu_idle,cpu_system,cpu_user
		try:
                        os.lstat(rrdfile)
                except OSError:
                        os.system('''rrdtool create %s --step 50 \\
			DS:cpu_idle:GAUGE:%s:0:100 \\
			DS:cpu_system:GAUGE:%s:0:100 \\
			DS:cpu_user:GAUGE:%s:0:100 \\
			RRA:MAX:0.5:1:2880 ''' % (rrdfile,HEARTBEAT,HEARTBEAT,HEARTBEAT) )

                os.system("rrdtool update %s --template 'cpu_idle:cpu_system:cpu_user'  N:%s:%s:%s" % (rrdfile,int(cpu_idle), cpu_system, cpu_user ))
		draw_graph(rrdfile,name,ip_addr)
	elif name == 'Load':
		print data
		load_1 = data[0].split()[0]
		load_5 = data[0].split()[1]
		load_15 = data[0].split()[2]
		performance_dic['SystemLoad'] = load_1
		print 'Load:',load_1, load_5, load_15
		try:
                        os.lstat(rrdfile)
                except OSError:
                        os.system('''rrdtool create %s --step 50  DS:Load_1:GAUGE:%s:0:100  DS:Load_5:GAUGE:%s:0:100 DS:Load_15:GAUGE:%s:0:100  RRA:MAX:0.5:1:2880 ''' % (rrdfile,HEARTBEAT,HEARTBEAT,HEARTBEAT) )
                os.system("rrdtool update %s --template 'Load_1:Load_5:Load_15'  N:%s:%s:%s" % (rrdfile,load_1,load_5,load_15 ))
                draw_graph(rrdfile,name,ip_addr)
	elif name == 'Mem_list':
		info_dic = {}
		for i in data:
		  for item in i:
			if len(item) ==0:break
			key = item.split()[0]
			value = item.split()[3]	
			info_dic[key] = value
		
		if info_dic is None:
		#if info_dic is not None:
			print info_dic
			Total_RAM = int(info_dic['hrStorageSize.1']) / 1024
			Total_SWAP = int(info_dic['hrStorageSize.10']) / 1024
			Cached_MEM = int(info_dic['hrStorageSize.7']) / 1024
			Free_SWAP = int(info_dic['memAvailSwap.0']) / 1024
			Free_MEM = int(info_dic['memAvailReal.0']) /1024
			Buffer_MEM = int(info_dic['memBuffer.0']) /1024
			MEM_used = Total_RAM - Free_MEM
			SWAP_used = Total_SWAP - Free_SWAP
			performance_dic['MemUsage'] = float(Total_RAM - Cached_MEM - Free_MEM) / Total_RAM * 100 
			#SWAP_used = 520
			print "Memory:", MEM_used,SWAP_used,Cached_MEM
			try:
				os.lstat(rrdfile)
			except OSError:
				os.system('''rrdtool create %s --step 50 \\
				DS:RAM_used:GAUGE:%s:U:U \\
				DS:Cached:GAUGE:%s:U:U \\
				DS:SWAP_used:GAUGE:%s:U:U \\
				RRA:MAX:0.5:1:300	\\
				''' % (rrdfile,HEARTBEAT,HEARTBEAT,HEARTBEAT)  )
			os.system('''rrdtool update %s --template 'RAM_used:Cached:SWAP_used' N:%s:%s:%s \\
			''' % (rrdfile ,MEM_used,Cached_MEM, SWAP_used ))
			draw_graph(rrdfile,name,ip_addr)
	elif name == 'Ip_speed':
		ip_speed_dic = {}
		
		for i in data:
			for item in i:
				if len(item) ==0:break
				ip_speed_dic[item.split()[0]] = item.split()[3]
		for obj_name,value in ip_speed_dic.items():
	
			if obj_name.startswith('ifDescr'):
				ethernet_name = ip_speed_dic[obj_name] 
				in_speed = int(ip_speed_dic['ifInOctets.%s' % obj_name[-1]]) / 8 /1000
				out_speed = int(ip_speed_dic['ifOutOctets.%s' % obj_name[-1]]) /8 /1000
				print "Network:", ethernet_name,in_speed,out_speed

				rrd_file = '%s/%s_%s.rrd' % (RRD_DIR,ip_addr,ethernet_name)
				try:
                                	os.lstat(rrd_file)
                        	except OSError:
					os.system('''rrdtool create %s --step 50 \\
					DS:in:GAUGE:%s:U:U \\
					DS:out:GAUGE:%s:U:U \\
					RRA:MAX:0.5:1:300 \\
					''' %(rrd_file,HEARTBEAT,HEARTBEAT ) )
				os.system('''rrdtool update %s --template 'in:out' N:%s:%s ''' %(rrd_file, in_speed, out_speed) )
				draw_graph(rrd_file,name,ip_addr, ethernet_name)
	else :
		pass

insert_to_db(ip_addr,'OK', performance_dic)
