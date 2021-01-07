#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import json
import sys
# 为了避免发送中文消息报错，使用utf8方式编码
reload(sys)
sys.setdefaultencoding('utf8')

def sendmsg(sub,mes):
    # 微信公众号上应用的CropID和Secret
    CropID = 'xx'
    Secret = 'xxx'
    # 获取access_token
    GURL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (CropID, Secret)
    result = urllib2.urlopen(GURL).read()
    dict_result = json.loads(result)
    Gtoken = dict_result['access_token']
    # 生成通过post请求发送消息的url
    PURL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Gtoken
    messages = mes
    subject = sub
    t = subject + '\n' + messages
    #企业号中的应用id
    AppID=xxx
    #部门成员id，微信接收者
    UserID='xxx'
    #部门id，定义可接收消息的成员范围
    PartyID='xxxxx'
    #生成post请求信息
    post_data = {}
    msg_content = {}
    msg_content['content'] = t
    post_data['touser'] = UserID
    post_data['toparty'] = PartyID
    post_data['msgtype'] = 'text'
    post_data['agentid'] = AppID
    post_data['text'] = msg_content
    post_data['safe'] = '0'
    #由于字典格式不能被识别，需要转换成json然后在作post请求
    #注：如果要发送的消息内容有中文的话，第三个参数一定要设为False
    json_post_data = json.dumps(post_data,False,False)
    #通过urllib2.urlopen()方法发送post请求
    req = urllib2.Request(PURL,json_post_data)
    request_post = urllib2.urlopen(req)
    #read()方法查看请求的返回结果
    print request_post.read()
