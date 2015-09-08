#!/bin/usr/env python
# -*- coding:utf-8 -*-#

import os,jieba,sys
reload(sys)
sys.setdefaultencoding('utf-8')

#对历史数据和预测数据进行分词划分

#
fencipath = r'G:\tianchi\weibo\predict\feature\fenci'

trainuserpath = r'G:\tianchi\weibo\train\user-train-big'

def fenci():
    stopkey = [line.strip() for line in open(r'G:\tianchi\weibo\train\stopkey.txt','r')]
    for root,dirnames,filenames in os.walk(trainuserpath):
        print 'file numbers',len(filenames)
        for filename in filenames:
            filecontent = open(trainuserpath+'\\'+filename,'r')
            outfile = open(fencipath+'\\'+filename,'ab')
            
            for line in filecontent:
                
                line_split = line.split('\t')
                
                fenci_list = jieba.cut(line_split[6],cut_all=True)
                fenci_key = ','.join(list(set(fenci_list)-set(stopkey)))
                outfile.write(fenci_key)
            
            print 'file',filename,'over'
            
            fenci_list = []
            outfile.close()
            filecontent.close()
            

fenci()
