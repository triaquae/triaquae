#!/usr/bin/env python
import sys
import random
import string
def usage():
    print "Usage: ./randompasswd.py num [num in (1-1024)]"
    exit(1)
def randomPassword(num):
    passwd = ''
    seed = string.letters + string.digits
    for i in xrange(num):
        passwd += seed[random.randrange(1,len(seed))]
    return passwd
def main():
    #print randomPassword(20)
    return randomPassword(6)
if __name__ == '__main__':
    main()
