#!/usr/bin/env python 
#Author: Alex Li
import os,sys
import time,datetime
import subprocess
from subprocess import Popen
#------------
###################-------------------------------
import db_connector
import get_user_ip_list,mailer
ip_list = db_connector.IP.objects.filter(status_monitor_on='True')
ping_status_dic = {}
ping_error_list = []
recover_list = []

p = [] # ip -> process
#for i in ip_list:
for i in ip_list:
	#ip = "10.98.33.%s" % i
	ip = i.ip
	if len(db_connector.ServerStatus.objects.filter(host = ip)) ==0:
		insert_status_item = db_connector.ServerStatus.objects.create(host = ip, hostname = i.hostname,host_uptime=time.strftime('%Y_%m_%d %H:%M:%S'), last_check=time.strftime('%Y_%m_%d %H:%M:%S'))
		insert_status_item.save()
	p.append((ip, Popen(['ping', '-c', '3', ip], stdout=subprocess.PIPE)))

while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None: # ping finished
            p.remove((ip, proc)) # this makes it O(n**2)
            #ping_status_dic[ip] = proc.communicate() # add result to dic
	    #print proc.returncode
	    if proc.returncode != 0: #error 
		ping_error_list.append(ip)
	    else:
                ping_status_dic[ip] = proc.communicate() # add result to dic
		

for ip,result in ping_status_dic.items():
	status = result[0].split('received,')[1].split('%')[0].strip()
	if 'rtt' in result[0]: # normal
		rtt = result[0].split('\n')[-2]
		#print ip,status,rtt
		ok_ip = db_connector.ServerStatus.objects.get(host=ip)
		ok_ip.ping_status = rtt
		ok_ip.host_status = 'UP'
		if ok_ip.attempt_count != 0:
			recover_list.append(ok_ip.host)
			ok_ip.attempt_count = 0
		ok_ip.up_count += 1
		if ok_ip.up_count == 0:
			ok_ip.availability = 0
		elif ok_ip.breakdown_count == 0 and ok_ip.up_count != 0:
			ok_ip.availability = 100

		else:
			ok_ip.availability =  float(ok_ip.up_count) / float((ok_ip.up_count  + ok_ip.breakdown_count)) * 100
		ok_ip.last_check = time.strftime('%Y_%m_%d %H:%M:%S') 
		ok_ip.save()
	elif 'error' in status:   #unreachable
		
		print ip,'err',status.split()[-1]

	else:   # 
		print ip,'---->packet loss',status

#--------------------------- 
# ping doesn't work ,use nc to scan port 

#for ip in ping_error_list:
#	print ip,'error'

#print "\033[32;1m Ok: %s , unreachable:%s\033[0m" %(len(ping_status_dic),len(ping_error_list))


T = []
Port_status_dic = {}

if len(ping_error_list) > 0:
	for i in ping_error_list:
		ip = "%s" % i
		port = str(db_connector.IP.objects.get(ip= ip).port)
        	T.append((ip, Popen(['nc', '-w', '1', ip, port ], stdout=subprocess.PIPE)))
	
	while T:
		for i, (ip,proc) in enumerate(T[:]):
			if proc.poll() is not None:
				T.remove((ip,proc))
				if proc.returncode == 0:
					Port_status_dic[ip] = 'YES'
				else:
					Port_status_dic[ip] = 'NO'
	#time.sleep(.04)

	if Port_status_dic:
		for err_ip,port_status in Port_status_dic.items():
			ip = db_connector.ServerStatus.objects.get(host= err_ip)
			msg= "Ping doesn't work. Telnet port:22 Reachable: %s" % port_status
			ip.ping_status = msg
			if port_status == 'NO':
				ip.host_status = 'DOWN'
				ip.attempt_count +=  1
				ip.breakdown_count += 1
				#ip.availability = ip.up_count /( ip.up_count + ip.breakdown_count) * 100
			else:
				ip.host_status = 'UP'
                		if ip.attempt_count != 0:
                        		recover_list.append(ip.host)
					ip.attempt_count = 0
				ip.up_count +=1
			if ip.up_count == 0:
				ip.availability = 0
			elif ip.breakdown_count == 0 and ip.up_count != 0:
				ip.availability = 100
			else:		
				ip.availability = float(ip.up_count) /float(( ip.up_count + ip.breakdown_count)) * 100
			ip.last_check = time.strftime('%Y_%m_%d %H:%M:%S') 
			print ip.last_check	
			ip.save()
				
#for ip in ping_error_list:
#       print ip,'error'

down_servers = Port_status_dic.values().count('NO')
print "\033[32;1m%s---- Ok: %s , unreachable:%s\033[0m" %(time.strftime('%Y_%m_%d %H:%M:%S'),len(ping_status_dic), down_servers)

down_ip_list =[]

#not sending email again after exceeds the alert limit!
for ip_addr in Port_status_dic.keys():
	alert_limit = db_connector.IP.objects.get(ip=ip_addr).alert_limit
	down_count =  db_connector.ServerStatus.objects.get(host=ip_addr).attempt_count
	if alert_limit >=  down_count:down_ip_list.append(ip_addr)	

alert_server_dic = {'DOWN': down_ip_list, 'RECOVERED': recover_list}


mail_alert_down_dic = {}
mail_alert_recover_dic  = {}

#Add down and recovered IP list to above 2 dics
for user,user_ip_list in get_user_ip_list.can_access_dic.items():
	mail_alert_down_dic[user] = []
	mail_alert_recover_dic[user]  = []
	for ip in alert_server_dic['DOWN']:
			
		if ip in user_ip_list:
			mail_alert_down_dic[user].append(ip) 
		else:pass #print 'not belong to ',ip,user

	for ip in alert_server_dic['RECOVERED']:
               if ip in user_ip_list:
			mail_alert_recover_dic[user].append(ip)
			print ip

def mail_alert(alert_dic,subject):
	for email,ip_list in alert_dic.items():
		email_list = [email]
		if len(ip_list) !=0:
		
			print 'send email to ',email,ip_list
			if mailer.send_mail(email, '%s %s'%(subject,",".join(ip_list)) , ", ".join(ip_list) ):
	        		print "Mail sent success!"
    			else:
        			print "Mail sent failed!" 



if len(down_ip_list) != 0:
	mail_alert(mail_alert_down_dic,"Alert:Servers down!!!")
if len(recover_list) !=0:
	mail_alert(mail_alert_recover_dic,"Notice:Servers recoverd!!!")

print 'these server have recovered!', recover_list
