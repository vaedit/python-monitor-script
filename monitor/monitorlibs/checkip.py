#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2,urllib,json,re,ConfigParser

def ipaddress():
    config = ConfigParser.ConfigParser()
    config.read('/root/monitor/config/config.txt')
    try:
        ip = config.get('global','ip')
        return ip
    except:
        url = 'http://myip.ipip.net'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        header={"User-Agent": user_agent}
        request = urllib2.Request(url,headers=header)
        responese = urllib2.urlopen(request)
        res = responese.read()
        result = re.search(r'(\d{1,3}\.){3}\d{1,3}',res)
        config.set("global",'ip',result.group())
        config.write(open('/root/monitor/config/config.txt','w'))
        return result.group()
