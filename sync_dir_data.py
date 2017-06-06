#!/usr/bin/env python
#-*- coding:utf-8 -*- 
import os
import shutil
import linecache

s_dir = [
"classRuleSync",
"dataSync",
"dynamicSync",
"schoolMailSync",
"openRegistrationData",
"schoolNewsSync",
"syncCardAndDevice"
]

#s_dir = ["classRuleSync"]

p_dir = [
"tuxing_7133",
"tuxing_7090",
"tuxing_7091",
"tuxing_7092",
"tuxing_7093",
"tuxing_7094",
"tuxing_7095",
"tuxing_7096",
"tuxing_7097",
"tuxing_7098"
]

s_url = '/datassd/tuxing_s'
d_url = '/datassd/tuxing'

#num_a = 0
#num_b = 5
#num_b = int(raw_input('You want number:'))

# 原有文件数量
a1 = int(os.popen('find %s/ -name *.json -type f|wc -l'%s_url).read().strip())

# mkdir dir
def Mkdir():
#    os.makedirs('%s/deleteLog'%d_url)
#    os.makedirs('%s/syncLog'%d_url)
#    os.makedirs('%s/yncCardAndDeviceLog'%d_url)
    for a in s_dir:
        for b in p_dir:
            os.makedirs('%s/%s/%s/'%(d_url,b,a))
    print "-->mkdir directory template ok" 
    
# clear file
def Clear():
    for a in p_dir:
        for b in s_dir:
            cmd = "rm -rf %s/%s/%s/* "% (d_url,a,b)
            os.system('%s'%cmd)
    print '-->clear directory ok'
    
    #shutil.rmtree(d_url)

# mv/copy file
def Mvfile():
    num_a = 0
    num_b = int(raw_input('You want number:'))
    print 'start move file...'    
    for s_d in s_dir:
        with open('/datassd/data.txt','w') as f:
            a = os.popen('find %s/%s/ -name *.json -type f'%(s_url,s_d)).read()
            f.write(a)
            f.close()
        data_n = 1
        while data_n > 0:
            for tomcat_dir in p_dir:
                cache = linecache.getlines('/datassd/data.txt')[num_a:num_b]
                for line in cache:
                    print line.replace("\n","")
                    shutil.move(line.replace("\n",""),'%s/%s/%s/'%(d_url,tomcat_dir,s_d))
                    #shutil.copy(line.replace("\n",""),'%s/%s/%s/'%(d_url,tomcat_dir,s_d))
                os.system('sed -i "1,%sd" /datassd/data.txt'%num_b)
                linecache.clearcache()
            data_n = os.path.getsize('/datassd/data.txt')

# check file
def Check():
    a2 = int(os.popen('find %s/ -name *.json -type f|wc -l'%s_url).read().strip())
    b2 = int(os.popen('find %s/ -name *.json -type f|wc -l'%d_url).read().strip())
    if a2 == 0 and a1 == b2:
        print '-->%s 剩余: %s,原有: %s 已迁移: %s'%(s_url,a2,a1,a1)
        print '-->%s 现有文件: %s'%(d_url,b2)
        print '-->迁移完成'
    else:
        print '-->原数据未迁移完'

#Mkdir()

Clear()
Mvfile()
Check()
