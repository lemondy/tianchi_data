#!/bin/usr/env python
# -*- coding:utf-8 -*-#

import os

#统计每条微博中 URL 的个数
trainpath = r'G:\tianchi\weibo\predict\predictuser'
urloutputpath = r'G:\tianchi\weibo\predict\feature\url'

def countURL():
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            readfile = open(trainpath+'\\'+filename,'r')
            outfile = open(urloutputpath+'\\'+filename,'ab')
            
            for line in readfile:
                line_split = line.split('\t')
                count = 0
                
                count += line_split[3].count('http://')
                count += line_split[3].count('https://')
                outfile.write(line_split[0]+'\t'+line_split[2]+'\t'+str(count)+'\n')
                print 'user',line_split[0],'count url',count
            outfile.close()
            readfile.close()


countURL()
