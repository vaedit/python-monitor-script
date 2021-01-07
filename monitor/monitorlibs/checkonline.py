#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil,sendwechat,sendding,checkip,writelog,time,getconfig

def run():
    ip = checkip.ipaddress()
    users = eval(getconfig.getkey('global','users'))
    while True:
        usernames = psutil.users()
        for i in usernames:
            name = i.name
            if name not in users:
                body = "IP地址: " + ip + "\n" + "告警内容: " + '\n' + '非法用户登录' + "\n" + '具体用户名::' + name
                sendwechat.sendmsg('非法用户登录',body)
        time.sleep(180)
