#!/usr/bin/env python
# -*-coding:utf-8-*-
# Filename: monitorLog.py
# Author:   yy520it@gmail.com
# This is a real-time monitoring logs, the script for the specified keyword alarm

import subprocess
import sys
import urllib
import urllib2
import os
import signal
import time

#短信接口
def sendsms(mobile,content):
        URL = 'SMS interface url'
        content = '[%s] %s' % (time.strftime('%Y%m%d %H:%M:%S'),content)
        data = {'m':mobile,'c':content}
        body = urllib.urlencode(data)
        request = urllib2.Request(URL,body)
        urldata = urllib2.urlopen(request)


#日志文件目录和名称
logFile = '/usr/local/tomcat8/logs/name.log' 
 

def monitorLog(logFile):
    print '监控的日志文件 是%s' % logFile
    popen = subprocess.Popen('tail -f ' + logFile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = popen.pid
    print('Popen.pid:' + str(pid))

    while True:
        line = popen.stdout.readline().strip()

        # 判断内容是否为空,避免在重启tomcat，杀掉日志
        if len(line) == 0:
            print 'tail进程死掉'
            popen.kill()
            print '杀掉进程,重新执行程序'
            break
		# 发送报警人
        if 'org.hibernate.exception.LockTimeoutException' in line:
            print('发现异常报警')
            sendsms(15066666666,'级别:严重 LockTimeoutException错误')


        # 当前时间
        thistime = time.strftime('%H:%M')
        if thistime == '23:59':
            popen.kill()
            sys.exit('清空僵尸进程')

    print '等待180秒'
    time.sleep(180)
    monitorLog(logFile)
 
if __name__ == '__main__':
    monitorLog(logFile)