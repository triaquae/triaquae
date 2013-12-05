#!/usr/bin/env python

import os,sys,time
import logger,tri_config,tri_module
import django
triaquae_path = tri_config.Working_dir
working_dir = logger.cur_dir
status_check_script = 'host_status_check.py'
snmp_monitor_script = 'multiprocessing_snmpMonitor.py'
service_log = '%s/tri_service.log' % tri_config.Log_dir
snmp_monitor_log = '%s/tri_snmp_service.log' % tri_config.Log_dir
def status_monitor(interval):
	script = '%s/%s' %(working_dir,status_check_script)
	print "Checking service status....."
	if service_status(status_check_script) == 'Running':
		print "\033[33;1mHost Status Monitor service is already running!\033[0m" 
	else:
		print "Starting HOST Status Monitor Service...."
		cmd = 'nohup python %s -s %s >> %s 2>&1 &' % (script,interval,service_log)
		result  = os.system(cmd)
		if result == 0:
			print '\033[32;1mHost status monitor service started successfully!\n\033[0m'

def snmp_monitor():
	script = '%s/%s' %(working_dir,snmp_monitor_script)
	print "Checking snmp status....."
	if service_status(snmp_monitor_script) == 'Running':
                print "\033[33;1mTriAquae SNMP monitor service is already running!\033[0m\n" 
        else:
                print "Starting TriAquae SNMP monitor service...." 
                cmd = 'nohup python %s  >> %s 2>&1 &' % (script, snmp_monitor_log)
                result  = os.system(cmd)
                if result == 0:
                        print '\033[32;1mTriAquae SNMP monitor service started successfully!\n\033[0m'

def shellinabox():
    if service_status('shellinaboxd') == 'Running':
        print "\033[33;1mshellinaboxd service is already running!\033[0m" 
    else:
        cmd = '%s/shellinaboxd/bin/shellinaboxd -t -b -p %s --css %s/shellinaboxd/share/doc/shellinabox/white-on-black.css' % (triaquae_path,tri_config.Tri_Port,triaquae_path)
        print cmd
        if os.system(cmd) == 0:
            print '\033[32;1mshellinaboxd start success!\n\033[0m'
        else:
            print '\033[31;1mshellinaboxd start failed!\n\033[0m'
        
def wsgiserver():
    if service_status('runwsgiserver') == 'Running':
        print "\033[33;1mrunwsgiserver service is already running!\033[0m" 
    else:
        cmd = 'nohup python %s/manage.py runwsgiserver host=0.0.0.0 port=7000 staticserve=collectstatic >>%s 2>&1 &' % (triaquae_path,service_log)
        if os.system(cmd) == 0:
            print '\033[32;1mwsgi server start success!\n\033[0m'
        else:
            print '\033[31;1mwsgi server start failed!\n\033[0m'

def stop_service(service_name):
	cmd = "ps -ef| grep %s|grep -v grep |awk '{print $2}'|xargs kill -9" %(service_name)	
	
	if service_status(service_name) == 'Running':
		cmd_result = os.system(cmd)
		if cmd_result == 0:
			print '..............\n'
			time.sleep(1)
			print '\033[31;1m%s stopped! \033[0m' % service_name
		else:
			print '\033[31;1mCannot stop %s service successfully,please manually kill the pid!\033[0m' % service_name
	else:
		print 'Service is not running...,nothing to kill! '

def service_status(service_name):
	cmd = "ps -ef |grep %s|grep -v grep |awk '{print $2}'" % service_name 
	result = os.popen(cmd).read().strip()
	try:
		service_pid = result.split()[0]
		if service_pid:
			print "\033[32;1m%s monitor service is running...\033[0m" % service_name
			return "Running"
	except IndexError:
		print "\033[31;1m%s service is not running....\033[0m" % service_name
		return "Dead"
try:
	if sys.argv[1] == 'start':
		status_monitor(30)
		snmp_monitor()
		shellinabox()
		wsgiserver()
	elif sys.argv[1] == 'stop':
		stop_service(snmp_monitor_script)
		stop_service(status_check_script)
		stop_service('shellinaboxd')
		stop_service('runwsgiserver')
	elif sys.argv[1] == 'status':
		service_status(snmp_monitor_script)
		service_status(status_check_script)
		service_status('shellinaboxd')
		service_status('runwsgiserver')
except IndexError:
	
	print 'No argument detected!\nUse: stop|start|status'

