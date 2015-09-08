#!/bin/usr/env python
# -*- coding:utf-8 -*-#

import os,jieba,sys
reload(sys)
sys.setdefaultencoding('utf-8')

#对历史数据和预测数据进行分词划分

#from 2014/07/01 -- 2014/11/30,只是针对历史数据相对较多的用户
fenci_0711_path = r'G:\tianchi\weibo\train\fenci-train-0711'
fenci_12_path = r'G:\tianchi\weibo\train\fenci-model-12'
trainuserpath = r'G:\tianchi\weibo\train\user-train-big'

def fenci():
    stopkey = [line.strip() for line in open(r'G:\tianchi\weibo\train\stopkey.txt','r')]
    for root,dirnames,filenames in os.walk(trainuserpath):
        print 'file numbers',len(filenames)
        for filename in filenames:
            filecontent = open(trainuserpath+'\\'+filename,'r')
            outfile1 = open(fenci_0711_path+'\\'+filename,'ab')
            outfile2 = open(fenci_12_path+'\\'+filename,'ab')
            for line in filecontent.readlines():
                line_split = line.split('\t')
                if line_split[2] < '2014-12-01':
                    fenci_list = jieba.cut(line_split[6],cut_all=True)
                    fenci_key = ','.join(list(set(fenci_list)-set(stopkey)))
                    outfile1.write(fenci_key)
                else:
                    outfile2.write(line)
            print 'file',filename,'over'
            
            fenci_list = []
            outfile1.close()
            outfile2.close()
            

fenci()
