#!/usr/bin/python3
# -*-coding:utf-8-*-
# Filename: 查找文件关键字小程序.py
# Author:   yy520it@gmail.com
# This is a small program to find the key word

import sys
import os

filename = input('请输入您要搜索的路径及文档名称:')
if len(filename) == 0:
    sys.exit('不能为空!')

if os.path.isfile(filename) != True:
    print("文件不存在!")
    exit(1)

while True:
  mubiao = input('请输入您要搜索的关键词:')
  if mubiao == 'exit':
      sys.exit('欢迎使用搜索系统!')
  if len(mubiao) == 0:
      continue
  mubiao2 = input('请输入第二个关键词，忽略按Enter:')
  if len(mubiao2) == 0:
      with open(filename,'r',encoding="utf-8") as f:
          Num = 0
          for line in f:
              line = line.strip('\n')
              index = line.find(mubiao)
              if index > -1:
                  Num += 1
                  print (line[:index] + ('\033[31;1m%s\033[0m' % mubiao) + line[ index + len(mubiao):])
      print ('一共找到了\033[31;1m%s\033[0m;' % Num)
  if mubiao == 'exit':
      sys.exit('欢迎使用搜索系统!')
  else:
      print ('搜索2个关键词')
      with  open(filename,'r',encoding='utf-8') as f:
          Num = 0
          for line in f:
              line = line.strip('\n')
              index = line.find(mubiao)
              index2 = line.find(mubiao2)
              if index > -1 and index2 > -1:
                  Num += 1
                  print (line[:index] + ('\033[31;1m%s\033[0m' % mubiao) + line[index:index2] + ('\033[31;1m%s\033[0m' % mubiao2) + line[ index2 + len(mubiao2):] )
      print ('一共找到了\033[31;1m%s\033[0m;' % Num)