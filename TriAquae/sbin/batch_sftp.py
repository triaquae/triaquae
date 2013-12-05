#!/usr/bin/env python
#Author: Alex Li
import multiprocessing
import sys,os,time
import db_connector,logger,MultiRunCounter
#----------------Use Django Mysql model----------------
cur_dir = os.path.dirname(os.path.abspath(__file__))

run_user = "MultiSftpTestUser"
track_num = MultiRunCounter.AddNumber()
script = 'python  %s/demo3_sftp.py' % cur_dir
try:
        if sys.argv[1] == '-h':
                print '''\n\033[32;1mUsage: python multiprocessing_sftp.py track_num run_user -s/-g local_file remote_path 'ip_list'\033[0m
-s: python multiprocessing_sftp.py 34 alex -s /tmp/local_file.tgz /remotePath/ '192.168.2.13 202.106.0.23 10.0.0.2'
    ./multiprocessing_sftp.py --auto  alex -s /tmp/local_file.tgz /remotePath/ '192.168.91.171 192.168.10.43 192.168.10.160'\n
-g: python multiprocessing_sftp.py 34 alex -g /remotePath/test_file.tgz  '192.168.2.13 202.106.0.23 10.0.0.2' 
    python multiprocessing_sftp.py --auto alex -g /remotePath/test_file.tgz  '192.168.2.13 202.106.0.23 10.0.0.2' 

--auto: auto add the track_mark 
'''
                sys.exit()
except IndexError:
        print "Argument error,try -h for help"
        sys.exit()
try:
        if sys.argv[1] == "--auto":
                track_num = MultiRunCounter.AddNumber()
        else:
                track_num = sys.argv[1]
except IndexError:
        print "argument error,try -h for help"
        sys.exit()


run_user = sys.argv[2]
option = sys.argv[3] # use '-s' or '-g'

if option == '-s':
	local_file = sys.argv[4]
	remote_path = sys.argv[5]
	raw_ip_list = sys.argv[6].split()
elif option == '-g':
	remote_file = sys.argv[4]
	raw_ip_list = sys.argv[5].split()
remove_duplicate_ip = set(raw_ip_list)
ip_list = list(remove_duplicate_ip)


def compress(source_file):
	compressed_file = "%s.tgz" % source_file
	cmd = "tar cvzf %s %s" %(compressed_file,source_file)
	os.system(cmd)
	file_size = os.stat(compressed_file).st_size
	return compressed_file,file_size


# batch run process
result = []

def run(host,option):
	if option == 'send':
		cmd = '''%s %s %s '%s' %s %s -t %s''' % (script,host,run_user,'-s',local_file,remote_path,track_num)
	elif option == 'get':
		cmd = '''%s %s %s '%s' %s -t %s''' % (script,host,run_user,'-g',remote_file,track_num)
	os.system(cmd)

if len(ip_list) < 50:
	thread_num = len(ip_list)
else:
	thread_num = 50
pool = multiprocessing.Pool(processes=thread_num)
if option == '-s':
	log_msg = "send %s to remote path %s " % (local_file,remote_path)
	logger.RecordLogSummary('CREATE','BatchSendFile',track_num,run_user,log_msg,len(ip_list),'/tmp/opt_%s.log' %track_num)
	for ip in ip_list:
		result.append(pool.apply_async(run,(ip,'send')) )
elif option == '-g':
	log_msg = "get file %s from remote servers" % remote_file
        logger.RecordLogSummary('CREATE','BatchGetFile',track_num,run_user,log_msg,len(ip_list),'/tmp/opt_%s.log' %track_num)

        for ip in ip_list:
                result.append(pool.apply_async(run,(ip,'get')) )
#time.sleep(5)
#pool.terminate()

pool.close()
pool.join()


for res in result:
	res.get(timeout=5)
