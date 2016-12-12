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
 
 
#���Žӿ�
URL = 'SMS interface url'
def sendsms(mobile,content):
        content = '[%s] %s' % (time.strftime('%Y%m%d %H:%M:%S'),content)
        data = {'m':mobile,'c':content}
        body = urllib.urlencode(data)
        request = urllib2.Request(URL,body)
        urldata = urllib2.urlopen(request)
 
#�����ݿ�
db = pymysql.connect('192.168.1.1','username','password','DBname',charset='utf8')
 
#ʹ��cursor()��������һ���α����cursor
cursor = db.cursor()
 
sql = "Input to sql"
try:
    #��ȡSQL���
    cursor.execute(sql)
    #��ȡ���м�¼�б�
    results = cursor.fetchall()
    len_num = len(results)   #�������
    if len_num > 0:
        #���ñ������ֻ�
        sendsms(15066666666,'SQLִ�н��Ϊ%s��'%len_num)
    else:
        pass
except:
    print 'Error:unable to fecth data'
 
db.close()