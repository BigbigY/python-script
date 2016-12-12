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

#���Žӿ�
def sendsms(mobile,content):
        URL = 'SMS interface url'
        content = '[%s] %s' % (time.strftime('%Y%m%d %H:%M:%S'),content)
        data = {'m':mobile,'c':content}
        body = urllib.urlencode(data)
        request = urllib2.Request(URL,body)
        urldata = urllib2.urlopen(request)


#��־�ļ�Ŀ¼������
logFile = '/usr/local/tomcat8/logs/name.log' 
 

def monitorLog(logFile):
    print '��ص���־�ļ� ��%s' % logFile
    popen = subprocess.Popen('tail -f ' + logFile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = popen.pid
    print('Popen.pid:' + str(pid))

    while True:
        line = popen.stdout.readline().strip()

        # �ж������Ƿ�Ϊ��,����������tomcat��ɱ����־
        if len(line) == 0:
            print 'tail��������'
            popen.kill()
            print 'ɱ������,����ִ�г���'
            break
		# ���ͱ�����
        if 'org.hibernate.exception.LockTimeoutException' in line:
            print('�����쳣����')
            sendsms(15066666666,'����:���� LockTimeoutException����')


        # ��ǰʱ��
        thistime = time.strftime('%H:%M')
        if thistime == '23:59':
            popen.kill()
            sys.exit('��ս�ʬ����')

    print '�ȴ�180��'
    time.sleep(180)
    monitorLog(logFile)
 
if __name__ == '__main__':
    monitorLog(logFile)