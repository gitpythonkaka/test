#!/usr/bin/env python 

import thread
from time import sleep, ctime

def thread0():
    print '1 : start @ ', ctime()
    sleep(4)
    print '1 : end   @ ', ctime()

def thread1():
    print '2 : start @ ', ctime()
    sleep(4)
    print '2 : end   @ ', ctime()

def main():
    print 'starting at:', ctime()
    thread.start_new_thread(thread0, ())
    thread.start_new_thread(thread1, ())
    sleep(6)
    print 'all DONE at: ', ctime()

if __name__ == '__main__':
    main()



