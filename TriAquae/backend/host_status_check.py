#!/usr/bin/env python
#Author: Alex Li
import os,time,sys

if '-s' in sys.argv:
	check_interval = sys.argv[sys.argv.index('-s') +1]
	print check_interval
else:	
	check_interval = 20


cur_dir = os.path.dirname(os.path.abspath(__file__))
script ="time python %s/muti_ping3.py" % cur_dir

while True:
	print '---------start checking.....--------'
	os.system(script)
	print "+++++++sleep %s seconds+++++++++" %(check_interval)
	time.sleep(int(check_interval))
