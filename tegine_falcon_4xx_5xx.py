#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import requests
import time
import json

merit = {}
up_merit = {}
payload = []
endpoint = socket.gethostname()
step = 60
counterType = "GAUGE"
furl = "http://127.0.0.1:1988/v1/push"

def LenNum(): 
    len_num = os.popen("curl http://127.0.0.1/us|grep bbtree.com|wc -l")
    len_num = int(len_num.next())
    return len_num

def ChangeMerit():
    lena = os.popen("curl http://127.0.0.1/us|grep 'bbtree.com'")
    for i in range(0,len_num): 
        i = lena.next()
        i =  i.split(',')
        merit[i[0]] = i[1:] 

def TmpData():            
    with open('/tmp/curl_tmp.txt','w') as f:  # 写文件
        for merit_k in merit.keys():  
            f.write("%s,%s,%s,%s\n"%(merit_k,merit[merit_k][3],merit[merit_k][6],merit[merit_k][7]))
def ReadDic():
    with open('/tmp/curl_tmp.txt') as f:  # 转换字典
        for l in f.xreadlines():  
            l = l.split(',')
            up_merit[l[0]] = l[1],l[2],l[3]
len_num = LenNum()
ChangeMerit()
ReadDic()

for merit_k in merit.keys(): # 两个字典的K一样，因此做一次循环
    if float(merit[merit_k][3]) < 100.0:
        continue
    tag = "domain=%s"%merit_k 
    
    req_total_sum,http_4xx_sum,http_5xx_sum = float(merit[merit_k][3]) - float(up_merit[merit_k][0]),float(merit[merit_k][6]) - float(up_merit[merit_k][1]),float(merit[merit_k][7]) - float(up_merit[merit_k][2])

    http_4xx_percent = http_4xx_sum*100.0#/req_total_sum # 开始计算4xx百分比
    http_5xx_percent = http_5xx_sum*100.0#/req_total_sum # 开始计算5xx百分比
    if http_4xx_percent == 0.0:
        http_4xx_percent = 0.0
    else:
        http_4xx_percent = http_4xx_percent/req_total_sum
    if http_5xx_percent == 0.0:
        http_5xx_percent = 0.0
    else:
        http_5xx_percent = http_5xx_percent/req_total_sum

    payload.append({"metric":"ngx_http_5xx_percent","endpoint":endpoint,"timestamp":int(time.time()),"step":step,"value":http_5xx_percent,"counterType":counterType,"tags":tag})
    payload.append({"metric":"ngx_http_4xx_percent","endpoint":endpoint,"timestamp":int(time.time()),"step":step,"value":http_4xx_percent,"counterType":counterType,"tags":tag})
    payload.append({"metric":"ngx_http_total","endpoint":endpoint,"timestamp":int(time.time()),"step":step,"value":req_total_sum,"counterType":counterType,"tags":tag})
    payload.append({"metric":"ngx_http_5xx_sum","endpoint":endpoint,"timestamp":int(time.time()),"step":step,"value":http_5xx_sum,"counterType":counterType,"tags":tag})
    payload.append({"metric":"ngx_http_4xx_sum","endpoint":endpoint,"timestamp":int(time.time()),"step":step,"value":http_4xx_sum,"counterType":counterType,"tags":tag})

r = requests.post(furl, data=json.dumps(payload))
TmpData() # 存1分钟前数据
