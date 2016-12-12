#!/usr/bin/env python
# -*-coding:utf-8-*-
# Filename: monitorSQL.py
# Author:   yy520it@gmail.com
# This is a real-time monitoring logs, the script for the specified keyword alarm
import pymysql
import sys
import urllib
import urllib2
import time
 
 
#短信接口
URL = 'SMS interface url'
def sendsms(mobile,content):
        content = '[%s] %s' % (time.strftime('%Y%m%d %H:%M:%S'),content)
        data = {'m':mobile,'c':content}
        body = urllib.urlencode(data)
        request = urllib2.Request(URL,body)
        urldata = urllib2.urlopen(request)
 
#打开数据库
db = pymysql.connect('192.168.1.1','username','password','DBname',charset='utf8')
 
#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
 
sql = "Input to sql"
try:
    #获取SQL语句
    cursor.execute(sql)
    #获取所有记录列表
    results = cursor.fetchall()
    len_num = len(results)   #结果条数
    if len_num > 0:
        #设置报警人手机
        sendsms(15066666666,'SQL执行结果为%s条'%len_num)
    else:
        pass
except:
    print 'Error:unable to fecth data'
 
db.close()