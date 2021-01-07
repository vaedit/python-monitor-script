#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,time
def logwrite(logbody):
    logtext=logbody
    if not os.path.exists("/root/monitor/logs"):
        os.mkdir('/root/monitor/logs')
    now_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
    logtext_body = now_time + logtext + '\n'
    file = open("/root/monitor/logs/"+now_time+'.txt',"a")
    file.write(logtext_body)
    file.close()
