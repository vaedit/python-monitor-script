#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil,sendemail,checkip,time,sendwechat,getconfig
def run():
    ip = checkip.ipaddress()
    cputhreshold = getconfig.getkey('global','cputhreshold')
    while True:
        cpuuseage = psutil.cpu_percent(interval=3)
        cpuuseagepre = str(round(cpuuseage,2))
        if cpuuseage > int(cputhreshold):
            body = "IP地址: " + ip + "\n" + "告警内容: " + '\n' + 'cpu使用率已超过80' + "\n" + '具体使用率::' + cpuuseagepre + '%'
#            sendemail.smail('cpu负载告警', body)
            sendwechat.sendmsg('负载告警', body)
        time.sleep(180)
