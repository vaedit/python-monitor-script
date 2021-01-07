#!/usr/bin/env python
# -*- coding:utf-8 -*-
import ConfigParser,writelog,traceback

def getkey(section,feild):
    config = ConfigParser.ConfigParser()
    try:
        config.read('/root/monitor/config/config.txt')
        values = config.get(section,feild)
        return values
    except:
        errorlog = traceback.format_exc()
        writelog.logwrite(errorlog)

