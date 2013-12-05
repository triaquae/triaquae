#!/usr/bin/env python
#Author: Alex Li
import multiprocessing
import sys,os,time
import db_connector,logger,MultiRunCounter
#----------------Use Django Mysql model----------------

cur_dir = os.path.dirname(os.path.abspath(__file__))
script = 'python %s/run_command4.py' % cur_dir




try:
	if sys.argv[1] == '-h':
		print '''\n\033[32;1mUsage: python multiprocessing_runCMD.py track_num 'ip_list' cmd run_user\033[0m
Example: python multiprocessing_runCMD.py 34 '192.168.2.13 202.106.0.23 10.0.0.2' 'df -h' alex \n
--auto : auto add the track_mark
	./multiprocessing_runCMD2.py --auto '192.168.91.171 192.168.10.43 192.168.10.160 192.168.91.171' 'df -h' alex'''
		sys.exit()
except IndexError:
	print "argument error,try -h for help"
	sys.exit()
try:
	if sys.argv[1] == "--auto":
		track_num = MultiRunCounter.AddNumber()
	else:	
		track_num = sys.argv[1]
except IndexError:
	print "argument error,try -h for help"
	sys.exit()

if __name__ == "__main__":
	run_user = sys.argv[4] 
	raw_ip_list = sys.argv[2].split()
	remove_duplicate_ip = set(raw_ip_list)
	ip_list = list(remove_duplicate_ip)
	cmd= sys.argv[3]

	# batch run process
	logger.RecordLogSummary('CREATE','BatchRunCommand',track_num,run_user,cmd,len(ip_list),'/tmp/opt_%s.log' %track_num)
	
	result = []
	def run(host):
		task = '''%s %s '%s' %s %s''' % (script,host,cmd,run_user,track_num)
		os.system(task)

	if len(ip_list) < 50:
		thread_num = len(ip_list)
	else:
		thread_num = 30
	pool = multiprocessing.Pool(processes=thread_num)

	for ip in ip_list:
		result.append(pool.apply_async(run,(ip,)) )
	#time.sleep(5)
	#pool.terminate()

	pool.close()
	pool.join()


	for res in result:
		res.get(timeout=5)
