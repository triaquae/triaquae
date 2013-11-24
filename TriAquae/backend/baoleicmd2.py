#!/usr/bin/env python

import random,time,datetime
from baoleidb import DisGroup, DisIP, DisRemotUser

ran = random.random


def GetDate():
    global currdate
    date = datetime.datetime.now()
    currdate = time.strftime('%Y-%m-%d')

def GetTime():
    global currtime
    time = datetime.datetime.now()
    currtime = time.strftime('%H:%M:%S')
