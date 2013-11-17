#!usr/bin/env python
###Author By DengLei
###Email is 244979152@qq.com
import os
import sys
import re
import json
import db_connector
import tri_config
here=tri_config.Asset_collection_dir
ip = db_connector.IP.objects.filter(asset_collection=1)
hostname_list=[]
devinfo_triaquae_hostname=db_connector.Devinfo.objects.all()
devinfo_triaquae_hostname_list=[]
for i in range(len(ip)):
    open_asset_hostname=  db_connector.IP.objects.get(ip=ip[i]).hostname
    hostname_list.append(open_asset_hostname)
check_triaquae_hostname=[]
for i in os.listdir(here):
    if i.endswith('@@triaquae_asset_collection.temp'):
	receive_file=open(here+'/'+i)
	receive_json=json.load(receive_file)
	hostname=receive_json['System_Hostname']
	Triaquae_Hostname = re.split('@@',i)[0]
	check_triaquae_hostname.append(Triaquae_Hostname)
	hostname_check = db_connector.Devinfo.objects.filter(Triaquae_Hostname=Triaquae_Hostname)
	if len(receive_json['Ethernet_Interface']) >= 1:
	    Ethernet_Interface_list = []
	    for i in  receive_json['Ethernet_Interface']:
		Ethernet_Interface_list.append(i.encode('utf-8'))
	    Ethernet_Interface_list = ','.join(Ethernet_Interface_list)
	else:
	    Ethernet_Interface_list = receive_json['Ethernet_Interface']
	if len(receive_json['Memory_Slots_All']) >= 1:
	    Memory_Slots_All_list = []
	    for i in  receive_json['Memory_Slots_All']:
		Memory_Slots_All_list.append(i.encode('utf-8'))
	    Memory_Slots_All_list = ','.join(Memory_Slots_All_list)
	else:
	    Memory_Slots_All_list = receive_json['Memory_Slots_All']
	if len(receive_json['Physical_Cpu_MHz']) >= 1:
	    Physical_Cpu_MHz_list = []
	    for i in  receive_json['Physical_Cpu_MHz']:
		Physical_Cpu_MHz_list.append(i.encode('utf-8'))
	    Physical_Cpu_MHz_list = ','.join(Physical_Cpu_MHz_list)
	else:
	    Physical_Cpu_MHz_list = receive_json['Physical_Cpu_MHz']
        if len(receive_json['Device_Sn']) >= 1:
            Device_Sn_list = []
            for i in  receive_json['Device_Sn']:
                Device_Sn_list.append(i.encode('utf-8'))
            Device_Sn_list = ','.join(Device_Sn_list)
        else:
            Device_Sn_list = receive_json['Device_Sn']
	if len(receive_json['Hard_Disk']) >= 1:
	    Hard_Disk_list = []
	    for i in  receive_json['Hard_Disk']:
		Hard_Disk_list.append(i.encode('utf-8'))
	    Hard_Disk_list = ','.join(Hard_Disk_list)
	else:
	    Hard_Disk_list = receive_json['Hard_Disk']
	if len(receive_json['System_Ip']) >= 1:
	    System_Ip_list = []
	    for i in  receive_json['System_Ip']:
		System_Ip_list.append(i.encode('utf-8'))
	    System_Ip_list = ','.join(System_Ip_list)
	else:
	    System_Ip_list = receive_json['System_Ip']
	if len(receive_json['System_Mac']) >= 1:
	    System_Mac_list = []
	    for i in  receive_json['System_Mac']:
		System_Mac_list.append(i.encode('utf-8'))
	    System_Mac_list = ','.join(System_Mac_list)
	else:
	    System_Mac_list = receive_json['System_Mac']
	if  len(hostname_check) < 1:
	    if len(receive_json["Memory_Slots_All"]) > 0:
		insert_devinfo = db_connector.Devinfo(Device_Type=receive_json['Device_Type'], Device_Model=receive_json['Device_Model'], Device_Sn=Device_Sn_list,System_Kernel= receive_json['System_Kernel'], Ethernet_Interface = Ethernet_Interface_list,Memory_Slots_Number= receive_json['Memory_Slots_Number'], Memory_Slots_All=Memory_Slots_All_list, Physical_Memory=receive_json['Physical_Memory'], Logical_Cpu_Cores=receive_json['Logical_Cpu_Cores'],Physical_Cpu_Cores=receive_json['Physical_Cpu_Cores'],Physical_Cpu_Model=receive_json['Physical_Cpu_Model'],Physical_Cpu_MHz=  Physical_Cpu_MHz_list,System_Version= receive_json['System_Version'], Hard_Disk=Hard_Disk_list, System_Ip=System_Ip_list, System_Mac=System_Mac_list,System_Hostname= receive_json['System_Hostname'], Triaquae_Hostname= Triaquae_Hostname,System_Hostid= receive_json['System_Hostid'], System_Swap= receive_json['System_Swap'])
	    else:
		insert_devinfo = db_connector.Devinfo(Device_Type=receive_json['Device_Type'], Device_Model=receive_json['Device_Model'], Device_Sn=Device_Sn_list,System_Kernel= receive_json['System_Kernel'], Ethernet_Interface = Ethernet_Interface_list,Memory_Slots_Number= receive_json['Memory_Slots_Number'], Physical_Memory=receive_json['Physical_Memory'], Logical_Cpu_Cores=receive_json['Logical_Cpu_Cores'],Physical_Cpu_Cores=receive_json['Physical_Cpu_Cores'],Physical_Cpu_Model=receive_json['Physical_Cpu_Model'],Physical_Cpu_MHz=  Physical_Cpu_MHz_list,System_Version= receive_json['System_Version'], Hard_Disk=Hard_Disk_list, System_Ip=System_Ip_list, System_Mac=System_Mac_list,System_Hostname= receive_json['System_Hostname'],Triaquae_Hostname= Triaquae_Hostname,System_Hostid= receive_json['System_Hostid'], System_Swap= receive_json['System_Swap'])		
	    insert_devinfo.save()
	else:	 
	    devinfo = db_connector.Devinfo.objects.get(Triaquae_Hostname=Triaquae_Hostname)
	    Device_Type= devinfo.Device_Type
	    Device_Model= devinfo.Device_Model
	    Device_Sn= devinfo.Device_Sn
	    System_Kernel= devinfo.System_Kernel
	    Ethernet_Interface= devinfo.Ethernet_Interface
	    Memory_Slots_Number= devinfo.Memory_Slots_Number
	    Memory_Slots_All= devinfo.Memory_Slots_All
	    Physical_Memory= devinfo.Physical_Memory
	    Logical_Cpu_Cores= devinfo.Logical_Cpu_Cores
	    Physical_Cpu_Cores= devinfo.Physical_Cpu_Cores
	    Physical_Cpu_Model= devinfo.Physical_Cpu_Model
	    Physical_Cpu_MHz= devinfo.Physical_Cpu_MHz
	    System_Version= devinfo.System_Version
	    Hard_Disk= devinfo.Hard_Disk
	    System_Ip= devinfo.System_Ip
	    System_Mac= devinfo.System_Mac
	    System_Hostname= devinfo.System_Hostname
	    Triaquae_Hostname= devinfo.Triaquae_Hostname
	    System_Hostid = devinfo.System_Hostid
	    System_Swap= devinfo.System_Swap
	    db_connector.Devinfo.objects.filter(Triaquae_Hostname=Triaquae_Hostname).delete()
	    if len(receive_json["Memory_Slots_All"]) > 0:
		insert_devinfo = db_connector.Devinfo(Device_Type=receive_json['Device_Type'], Device_Model=receive_json['Device_Model'], Device_Sn=receive_json['Device_Sn'],System_Kernel= receive_json['System_Kernel'], Ethernet_Interface = Ethernet_Interface_list,Memory_Slots_Number= receive_json['Memory_Slots_Number'], Memory_Slots_All=Memory_Slots_All_list, Physical_Memory=receive_json['Physical_Memory'], Logical_Cpu_Cores=receive_json['Logical_Cpu_Cores'],Physical_Cpu_Cores=receive_json['Physical_Cpu_Cores'],Physical_Cpu_Model=receive_json['Physical_Cpu_Model'],Physical_Cpu_MHz=  Physical_Cpu_MHz_list,System_Version= receive_json['System_Version'], Hard_Disk=Hard_Disk_list, System_Ip=System_Ip_list, System_Mac=System_Mac_list,System_Hostname= receive_json['System_Hostname'], Triaquae_Hostname=Triaquae_Hostname, System_Hostid= receive_json['System_Hostid'], System_Swap= receive_json['System_Swap'])
	    else:
		insert_devinfo = db_connector.Devinfo(Device_Type=receive_json['Device_Type'], Device_Model=receive_json['Device_Model'], Device_Sn=receive_json['Device_Sn'],System_Kernel= receive_json['System_Kernel'], Ethernet_Interface = Ethernet_Interface_list,Memory_Slots_Number= receive_json['Memory_Slots_Number'], Physical_Memory=receive_json['Physical_Memory'], Logical_Cpu_Cores=receive_json['Logical_Cpu_Cores'],Physical_Cpu_Cores=receive_json['Physical_Cpu_Cores'],Physical_Cpu_Model=receive_json['Physical_Cpu_Model'],Physical_Cpu_MHz=  Physical_Cpu_MHz_list,System_Version= receive_json['System_Version'], Hard_Disk=Hard_Disk_list, System_Ip=System_Ip_list, System_Mac=System_Mac_list,System_Hostname= receive_json['System_Hostname'], Triaquae_Hostname=Triaquae_Hostname, System_Hostid= receive_json['System_Hostid'], System_Swap= receive_json['System_Swap'])		
	    insert_devinfo.save()	    
	    if Device_Type <> receive_json['Device_Type']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Device_Type', Old_Value=Device_Type, New_Value=receive_json['Device_Type'] )
		insert_check_Check_Devinfo.save()	    
	    if Device_Model <> receive_json['Device_Model']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Device_Model', Old_Value=Device_Model, New_Value=receive_json['Device_Model'] )
		insert_check_Check_Devinfo.save()
	    if Device_Sn <> receive_json['Device_Sn']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Device_Sn', Old_Value=Device_Sn, New_Value=receive_json['Device_Sn'] )
		insert_check_Check_Devinfo.save()			
	    if System_Kernel <> receive_json['System_Kernel']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='System_Kernel', Old_Value=System_Kernel, New_Value=receive_json['System_Kernel'] )
		insert_check_Check_Devinfo.save()			
	    if Ethernet_Interface.encode('utf-8') <> str(Ethernet_Interface_list):
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Ethernet_Interface', Old_Value=Ethernet_Interface, New_Value=Ethernet_Interface_list )
		insert_check_Check_Devinfo.save()		
	    if Memory_Slots_Number <> receive_json['Memory_Slots_Number']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Memory_Slots_Number', Old_Value=Memory_Slots_Number, New_Value=receive_json['Memory_Slots_Number'] )
		insert_check_Check_Devinfo.save()
	    if Memory_Slots_All.encode('utf-8') == 'Null':
		Memory_Slots_All = str([])
		if Memory_Slots_All <> str(Memory_Slots_All_list):
		    insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Memory_Slots_All',New_Value=Memory_Slots_All_list )
		    insert_check_Check_Devinfo.save()		    
	    elif Memory_Slots_All.encode('utf-8') <> str(Memory_Slots_All_list):
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Memory_Slots_All', Old_Value=Memory_Slots_All, New_Value=Memory_Slots_All_list )
		insert_check_Check_Devinfo.save()		
	    if Physical_Memory <> receive_json['Physical_Memory']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Physical_Memory', Old_Value=Physical_Memory, New_Value=receive_json['Physical_Memory'] )
		insert_check_Check_Devinfo.save()			
	    if Logical_Cpu_Cores <> receive_json['Logical_Cpu_Cores']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Logical_Cpu_Cores', Old_Value=Logical_Cpu_Cores, New_Value=receive_json['Logical_Cpu_Cores'] )
		insert_check_Check_Devinfo.save()		
	    if Physical_Cpu_Cores <> receive_json['Physical_Cpu_Cores']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Physical_Cpu_Cores', Old_Value=Physical_Cpu_Cores, New_Value=receive_json['Physical_Cpu_Cores'] )
		insert_check_Check_Devinfo.save()				
	    if Physical_Cpu_Model <> receive_json['Physical_Cpu_Model']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Physical_Cpu_Model', Old_Value=Physical_Cpu_Model, New_Value=receive_json['Physical_Cpu_Model'] )
		insert_check_Check_Devinfo.save()		
	    if Physical_Cpu_MHz.encode('utf-8') <> str(Physical_Cpu_MHz_list):
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Physical_Cpu_MHz', Old_Value=Physical_Cpu_MHz, New_Value=Physical_Cpu_MHz_list)
		insert_check_Check_Devinfo.save()		
	    if System_Version <> str(receive_json['System_Version']):
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='System_Version', Old_Value=System_Version, New_Value=receive_json['System_Version'] )
		insert_check_Check_Devinfo.save()
	    if Hard_Disk <> str(Hard_Disk_list):
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='Hard_Disk', Old_Value=Hard_Disk, New_Value=Hard_Disk_list )
		insert_check_Check_Devinfo.save()			
	    if System_Ip.encode('utf-8') <> str(System_Ip_list):
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='System_Ip', Old_Value=System_Ip, New_Value=System_Ip_list )
		insert_check_Check_Devinfo.save()		
	    if System_Mac.encode('utf-8') <> str(System_Mac_list):
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='System_Mac', Old_Value=System_Mac, New_Value=System_Mac_list)
		insert_check_Check_Devinfo.save()			
	    if System_Hostname <> receive_json['System_Hostname']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='System_Hostname', Old_Value=System_Hostname, New_Value=receive_json['System_Hostname'] )
		insert_check_Check_Devinfo.save()			
	    if System_Hostid <> receive_json['System_Hostid']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='System_Hostid', Old_Value=System_Hostid, New_Value=receive_json['System_Hostid'] )
		insert_check_Check_Devinfo.save()			
	    if System_Swap <> receive_json['System_Swap']:
		insert_check_Check_Devinfo = db_connector.Check_Devinfo(Triaquae_Hostname= Triaquae_Hostname, Change_Type='System_Swap', Old_Value=System_Swap, New_Value=receive_json['System_Swap'] )
		insert_check_Check_Devinfo.save()
for i in devinfo_triaquae_hostname:
    devinfo_triaquae_hostname_list.append(i.Triaquae_Hostname)
for i in devinfo_triaquae_hostname_list:
    if i not in hostname_list:
        db_connector.Devinfo.objects.filter(Triaquae_Hostname=i).delete()
for i in hostname_list:
    if i not in check_triaquae_hostname:
	db_connector.Devinfo.objects.filter(Triaquae_Hostname=i).delete()
        data='no data'
        insert_devinfo = db_connector.Devinfo(Device_Type=data, Device_Model=data, Device_Sn=data,System_Kernel= data, Ethernet_Interface = data,Memory_Slots_Number= data, Physical_Memory=data, Logical_Cpu_Cores=data,Physical_Cpu_Cores=data,Physical_Cpu_Model=data,Physical_Cpu_MHz=  data,System_Version= data, Hard_Disk=data, System_Ip=data, System_Mac=data,System_Hostname=data, Triaquae_Hostname=i, System_Hostid= data, System_Swap= data)
        insert_devinfo.save()
