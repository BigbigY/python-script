#!/usr/bin/python
import os
import time
os.chdir('/project/')
source_list = ['/project/app','/project/rqb','/project/rqt']
target_dir = '/backup/'
today = time.strftime('%Y%m%d')
if not os.path.exists(target_dir + today):
    os.mkdir(target_dir + today)
    print "Successful created directory",target_dir + today
for source in source_list:
    target = target_dir + today + os.sep + source[9:] + '.tar.gz'
    tar_command = "tar zcvf %s %s" % (target, source[9:])
    
    if os.system(tar_command) == 0:
        print 'Successful backup to',target
        time.sleep(3)
    else:
        print 'Backup FALLED'