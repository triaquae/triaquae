#!/usr/bin/env python
#Author: Alex Li
import sys,os,time
import tri_config,tri_module
sys.path.append(tri_config.Working_dir)
os.environ['DJANGO_SETTINGS_MODULE'] ='TriAquae.settings'
#----------------Use Django Mysql model----------------
from TriAquae.hosts.models import * 
