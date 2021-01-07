#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil,sendemail,checkip,time,sendwechat,getconfig
def run():
    ip = checkip.ipaddress()
    memthreshold=getconfig.key('global','memthreshold')
    while True:
        meminfo = psutil.virtual_memory()
        memusagepre = meminfo.percent
 #       print memusagepre
        memfreeM = meminfo.free/1024/1024
        memfreeG = meminfo.free/1024/1024/1024
        if memusagepre > int(memthreshold):
            body = "IP地址: " + ip + "\n" + "告警内容: " + '\n'  + '内存使用已达： ' + str(memusagepre) + "%" + "\n" + '剩余空间' + str(memfreeM) + "M" + "(" + str(memfreeG) + "G)"
          #  sendemail.smail('内存告警', body)
            sendwechat.sendmsg('内存告警', body)
        time.sleep(180)
