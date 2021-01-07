#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil,sendemail,checkip,time,sendwechat,getconfig
def run():
    ip = checkip.ipaddress()
    diskthreshold = getconfig.getkey('global','diskthreshold')
    while True:
        devs = psutil.disk_partitions()
        # 显示硬盘信息：
       # print devs
        # 硬盘名称与挂载点，文件类型：
        for dev in devs:
    #        print('硬盘名：%s, 挂载点：%s, 文件类型：%s' % (dev.device, dev.mountpoint, dev.fstype))
            diskusage = psutil.disk_usage(dev.mountpoint).percent
            diskusage_int = str(round(diskusage,2))
            diskfree = str(psutil.disk_usage(dev.mountpoint).free/1024/1024/1024)
            if diskusage > int(diskthreshold):
                body = "IP地址: " + ip + "\n" + "告警内容: " + '\n' + "磁盘：" + dev.mountpoint + "\n" + '使用已达:: ' + diskusage_int + "\n" + '剩余空间:: ' + diskfree + 'G'
#                sendemail.smail('磁盘告警',body)
                sendwechat.sendmsg('磁盘告警',body)
        time.sleep(180)
