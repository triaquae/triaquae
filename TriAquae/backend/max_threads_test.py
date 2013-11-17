#!/usr/bin/env python
#coding=gbk

import threading
import time, random,  sys

class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value = value = self.value + 1
        self.lock.release()
        return value

counter = Counter()
cond = threading.Condition()

class Worker(threading.Thread):

    def run(self):
        print self.getName(),  "-- created."
        cond.acquire()

        cond.wait()
        #print self.getName(), "-- task", "finished"
        cond.release()
if __name__ == '__main__':
   
        try:
            for i in range(3500):
                Worker().start() # start a worker
        except BaseException,  e:
            print "ERROR: ", type(e),  e
            time.sleep(5)
            print "maxium i=",  i
        finally:
            cond.acquire()
            cond.notifyAll()
            cond.release()
            time.sleep(3)
            print threading.currentThread().getName(),  " quit"