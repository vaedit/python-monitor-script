#!/usr/bin/env python
# -*- coding:utf-8 -*-
#from multiprocessing import Pool,current_process
import os,sys,time,urllib2
from monitorlibs import checktraffic,checkcpu,checkdisk,checkmem,checkonline,checkdiskio
from monitorlibs import sendemail,sendwechat,checkip,writelog,getconfig
import psutil,Queue,platform
from threading import Thread,current_thread
ip = checkip.ipaddress()
monitorjobQ=Queue.Queue(0)
NUM_WORKERS=5

class monitorthread(Thread):
    def __init__(self,monitorputin):
        Thread.__init__(self)
        self.monitorqueue = monitorputin
    def monitorprocess(self,job):
        job.run()
    def run(self):
        while True:
            if self.monitorqueue.qsize() > 0:
                try:
                    monitorjob = self.monitorqueue.get_nowait()
                    self.monitorprocess(monitorjob)
                except Queue.Empty:
                    queue_size = 0
            else:
                break

def funzioneDemo():
    # 这是具体业务函数示例
    WhiteList = getconfig.getkey('global', "WhiteList")
#    print WhiteList
    if "disk" not in WhiteList:
        monitorjobQ.put(checkdisk)
    if "traffic" not in WhiteList:
        monitorjobQ.put(checktraffic)
    if "cpu" not in WhiteList:
        monitorjobQ.put(checkcpu)
    if "mem" not in WhiteList:
        monitorjobQ.put(checkmem)
    if "checkonline" not in WhiteList:
        monitorjobQ.put(checkonline)
    if "diskio" not in WhiteList:
        monitorjobQ.put(checkdiskio)
    for x in range(NUM_WORKERS):
        monitorthread(monitorjobQ).start()

def createDaemon():
    # fork进程
    try:
        if os.fork() > 0: os._exit(0)
    except OSError, error:
        print 'fork #1 failed: %d (%s)' % (error.errno, error.strerror)
        os._exit(1)
    os.chdir('/root/monitor/')
    os.setsid()
    os.umask(0)
    try:
        pid = os.fork()
        if pid > 0:
            fpid = open('/var/run/monitor.pid','w')
            fpid.write(str(pid))
            fpid.close()
            os._exit(0)
    except OSError, error:
        print 'fork #2 failed: %d (%s)' % (error.errno, error.strerror)
        os._exit(1)
    # 重定向标准IO
    sys.stdout.flush()
    sys.stderr.flush()
    si = file("/dev/null", 'r')
    so = file("/dev/null", 'a+')
    se = file("/dev/null", 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
    # 在子进程中执行代码
    funzioneDemo() # function demo
if __name__ == '__main__':
    if platform.system() == "Linux":
        createDaemon()
    else:
        os._exit(0)
