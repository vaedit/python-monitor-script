#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib,urllib2
import json

def send_msg(mobile,item_name):
    """
     钉钉机器人API接口地址:
     https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1
     :param mobile:
     :param itemName:
     :return:
    """
    access_token = "钉钉机器人API接口toekn"
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + access_token
    data = {
        "msgtype": "text",
        "text": {
            "content": item_name
        },
        "at": {
            "atMobiles": [
                mobile
            ],
            "isAtAll": "false"
        }
    }
    # 设置编码格式
    json_data = json.dumps(data).encode(encoding='utf-8')
    header_encoding = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
    req = urllib2.Request(url=url, data=json_data, headers=header_encoding)
    res = urllib2.urlopen(req)
