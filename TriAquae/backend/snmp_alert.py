#!/usr/bin/env python

import os,json
import get_user_ip_list,mailer,db_connector,tri_config
f= file(tri_config.Snmp_temp_log)
performance_dic = {}
mail_dic = {'SNMP_ERROR':[] , 'RECOVER_LIST':[] }
snmp_monitor_list = []
for i in f.readlines():
    try:
        line = i.strip().split('|')
        host = line[0].strip()
        if line[1].strip() == 'OK':
            performance_dic[host] =  json.loads(line[2])
        else:
            mail_dic['SNMP_ERROR'].append(host)
        snmp_monitor_list.append(host)    
    except IndexError:continue



for h,dic in performance_dic.items():
    mail_dic[h] = [] #create an empty snmp data list for each host
    server = db_connector.IP.objects.get(ip=h)
    
    if server.cpu_idle_critical != 0 and int(dic['CpuIdle']) - server.cpu_idle_critical <= 0:
        mail_dic[h].append('Critical: Value of CpuIdle is %s,exceeds the limit %s' %(int(dic['CpuIdle']), server.cpu_idle_critical))
    elif server.cpu_idle_warning != 0 and int(dic['CpuIdle'])  - server.cpu_idle_warning <= 0: 
        mail_dic[h].append('Warning: Value of CpuIdle is %s,exceeds the limit %s' %(int(dic['CpuIdle']), server.cpu_idle_warning))
    else: 
        pass #print h,'not hitting the CpuIdle alert line yet!'
    
    
    if server.system_load_critical !=0 and float(dic['SystemLoad']) - server.system_load_critical >=0:
        mail_dic[h].append('Critical: Value of System Load is %s,exceeds the limit %s' %(float(dic['SystemLoad']), server.system_load_critical))
    elif server.system_load_warning != 0 and float(dic['SystemLoad']) - server.system_load_warning >=0:
        mail_dic[h].append('Warning: Value of System Load is %s,exceeds the limit %s' %(float(dic['SystemLoad']),server.system_load_warning))
    else:
        pass #print h,'not hitting the SYSTEM LOAD alert line yet!'
   
    if server.mem_usage_critical != 0 and float(dic['MemUsage']) - server.mem_usage_critical  >= 0:
        mail_dic[h].append('Critical: Value of Memusage is %s,exceeds the limit %s' %(float(dic['MemUsage']),server.mem_usage_critical))
    elif server.mem_usage_warning != 0 and float(dic['MemUsage']) - server.mem_usage_warning >=0:
        mail_dic[h].append('Warning: Value of Memusage is %s,exceeds the limit %s' %(float(dic['MemUsage']),server.mem_usage_warning))
    else:
        pass #print h,'not hitting the MEM alert line yet!'
    if len(mail_dic[h]) == 0: del mail_dic[h] #delete this item from dic if this host has nothing to alert 

#reset the alerting counter for recovered ip list
for i in snmp_monitor_list:
    if i not in mail_dic.keys() and i not in mail_dic['SNMP_ERROR']: # means snmp data not crossing any limit line
        print '\033[32;1mSNMP status is ok\033[0m',i
        ok_ip = db_connector.ServerStatus.objects.get(host=i)
        if ok_ip.snmp_alert_count == 0:pass  #snmp status is up before
        else:  #snmp last status was down, now it's recovered
            ok_ip.snmp_alert_count = 0 
            ok_ip.save()
            print '\033[32;1mServer performance status back to normal!\033[0m',ok_ip.hostname
	    mail_dic['RECOVER_LIST'].append(ok_ip.hostname)
    
    else: #if i  in mail_dic['SNMP_ERROR']:
        snmp_alerting_ip = db_connector.ServerStatus.objects.get(host=i)
        #print snmp_alerting_ip.snmp_alert_count
	snmp_alerting_ip.snmp_alert_count += 1
        snmp_alerting_ip.save()

#Match the alerting list with relative person
mail_alert_dic = {}
for u,ip_list in  get_user_ip_list.can_access_dic.items(): 
   mail_alert_dic[u] = [] 
   for h,data in mail_dic.items():
      if h != 'SNMP_ERROR' and h != 'RECOVER_LIST':
		if db_connector.ServerStatus.objects.get(host=h).snmp_alert_count > db_connector.IP.objects.get(ip=h).snmp_alert_limit:pass # crossed max alert limit
		else:
		   if h in ip_list:
			mail_alert_dic[u].append({h:data})
      elif h == 'RECOVER_LIST':
		for recover_host in data:
			mail_alert_dic[u].append({recover_host:'Host performance recovered from crossing the limit or breaking down!'}) 
      else:
           for ip in ip_list:
             if db_connector.ServerStatus.objects.get(host=ip).snmp_alert_count > db_connector.IP.objects.get(ip=ip).snmp_alert_limit:pass # 'crossed max alert limit!' 
             else:
                if ip in data:
                    mail_alert_dic[u].append( {ip:'SNMP Error la'} )

for mail_address,data in mail_alert_dic.items():
  if len(data) !=0:
    print "\033[32;1m Send email to %s\033[0m" % mail_address
    mail_content = []
    for i in data:
        for ip_addr,alert_data in i.items():
              mail_content.append("%s\t%s\n" %(ip_addr,alert_data))


    print 'Mail CoNTENT:::',' '.join(mail_content)
    
    if mailer.send_mail(mail_address, "TriAuqae:Performance Alert" , " ".join(mail_content) ):
        print "Mail sent success!"
    else:
        print "Mail sent failed!" 
