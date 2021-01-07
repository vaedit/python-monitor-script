#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil,time,writelog,sendwechat,sendding,sendemail,checkip
def run():
    ip = checkip.ipaddress()
    while True:
        firsttraffic = psutil.net_io_counters(pernic=True)
        time.sleep(15)
        secondtraffic = psutil.net_io_counters(pernic=True)
        for key in firsttraffic:
            if key == 'lo':
                continue
            netrecv = (secondtraffic[key].bytes_recv - firsttraffic[key].bytes_recv)/1024/1024/15
            netsent = (secondtraffic[key].bytes_sent - firsttraffic[key].bytes_sent)/1024/1024/15
            netrecv_speed = str(round(netrecv,2))
         #   netrecv_speed = 11
            netsent_speed = str(round(netsent,2))
            if float(netrecv_speed) > 10 or float(netsent_speed) > 10:
                body = "IP地址: " + ip + "\n" + "告警内容: 流量异常！ " + '\n' + '接收流量: ' + str(netrecv_speed) + '/s' + "\n" + '发送流量: ' + netsent_speed + '/s'
    #            sendemail.smail('网卡流量告警',body)
                sendwechat.sendmsg('流量告警', body)
        time.sleep(180)
