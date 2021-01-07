#!/usr/bin/python
# -*- coding:utf-8 -*-
import psutil,sendwechat,sendding,checkip,writelog,time,getconfig
def run():
    ip = checkip.ipaddress()
    diskiothreshold=getconfig.getkey('global','diskiothreshold')
    dev = psutil.disk_io_counters(perdisk=True)
    while True:
        for key in dev:
            if key == 'sda1':
                firstcheck = psutil.disk_io_counters(perdisk=True)
                time.sleep(30)
                secondcheck = psutil.disk_io_counters(perdisk=True)
                firstcheck_read = firstcheck[key].read_count
                firstcheck_write = firstcheck[key].write_count
                secondcheck_read = secondcheck[key].read_count
                secondcheck_write = secondcheck[key].write_count
                firstio = firstcheck_read + firstcheck_write
                secondio = secondcheck_read + secondcheck_write
                iops = (secondio - firstio)/30
                if iops > int(diskiothreshold):
                    body = "IP地址: " + ip + "\n" + "告警内容: " + '\n' + "磁盘：" + "/data" + "\n" + "iops:" +  iops
                    sendwechat.sendmsg('磁盘io告警',body)
        time.sleep(180)
