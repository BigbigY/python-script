#!/usr/bin/python3
# -*-coding:utf-8-*-
# Filename: �����ļ��ؼ���С����.py
# Author:   yy520it@gmail.com
# This is a small program to find the key word

import sys
filename = input('��������Ҫ������·�����ĵ�����:')
if len(filename) == 0:
    sys.exit('����Ϊ��!')
while True:
  mubiao = input('��������Ҫ�����Ĺؼ���:')
  if mubiao == 'exit':
      sys.exit('��ӭʹ������ϵͳ!')
  if len(mubiao) == 0:
      continue
  mubiao2 = input('������ڶ����ؼ��ʣ����԰�Enter:')
  if len(mubiao2) == 0:
      with open(filename) as f:
          Num = 0
          for line in f:
              line = line.strip('\n')
              index = line.find(mubiao)
              if index > -1:
                  Num += 1
                  print (line[:index] + ('\033[31;1m%s\033[0m' % mubiao) + line[ index + len(mubiao):])
      print ('һ���ҵ���\033[31;1m%s\033[0m;' % Num)
  if mubiao == 'exit':
      sys.exit('��ӭʹ������ϵͳ!')
  else:
      print ('����2���ؼ���')
      with  open(filename) as f:
          Num = 0
          for line in f:
              line = line.strip('\n')
              index = line.find(mubiao)
              index2 = line.find(mubiao2)
              if index > -1 and index2 > -1:
                  Num += 1
                  print (line[:index] + ('\033[31;1m%s\033[0m' % mubiao) + line[index:index2] + ('\033[31;1m%s\033[0m' % mubiao2) + line[ index2 + len(mubiao2):] )
      print ('һ���ҵ���\033[31;1m%s\033[0m;' % Num)