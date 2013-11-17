#!/usr/bin/env python
###Author By DengLei
###Email is 244979152@qq.com
import multiprocessing
import sys,os,time
import MultiRunCounter
import logger
cur_dir = os.path.dirname(os.path.abspath(__file__))
track_num = MultiRunCounter.AddNumber()
script = 'python %s/Hardware_Single_Sftp.py' %cur_dir

host_list = sys.argv[1].split()
run_user = sys.argv[2]
option= sys.argv[3]
file_name1 = sys.argv[4]
file_name2 = sys.argv[5]
# batch run process
result = []
def run(host):
    cmd = '''%s %s %s '%s' %s %s -t %s''' % (script,host,run_user, option,file_name1,file_name2,track_num)
    os.system(cmd)

if len(host_list) < 50:
    thread_num = len(host_list)
else:
    thread_num = 30
pool = multiprocessing.Pool(processes=thread_num)

for ip in host_list:
    result.append(pool.apply_async(run,(ip,)) )
pool = multiprocessing.Pool(processes=thread_num)
if option == '-s':
    log_msg = "send %s to %s " % (file_name1,file_name2)
    logger.RecordLogSummary('CREATE','BatchSendFile',track_num,run_user,log_msg,len(host_list),'/tmp/opt_%s.log' %track_num)
elif option == '-g':
    log_msg = "get file %s from %s" % (file_name1,file_name2)
    logger.RecordLogSummary('CREATE','BatchGetFile',track_num,run_user,log_msg,len(host_list),'/tmp/opt_%s.log' %track_num)
pool.close()
pool.join()


for res in result:
    res.get()

