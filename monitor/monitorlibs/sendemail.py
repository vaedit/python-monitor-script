#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮件函数
def smail(sub,body):
    tolist = ["xx@qq.com", "xx@qq.com"]
    cc = ["xx@qq.com", "xx@163.com"]
    sender = '管理员 <worktest2020@163.com>'
    subject = sub
    smtpserver = 'smtp.163.com'
    username = 'xx@163.com'
    password = 'xxx'
    messages = body

    msg = MIMEText(messages, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(tolist)
    msg['Cc'] = ','.join(cc)
    try:
        s = smtplib.SMTP()
        s.connect(smtpserver, '25')
        s.login(username, password)
        s.sendmail(sender, tolist+cc, msg.as_string())
        s.quit()
        print '邮件发送成功'
    except Exception as e:
        print '邮件发送失败：%s' %e
