#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os

#统计一条微博是否 @ 别人和 @ 的个数

trainpath = r'G:\tianchi\weibo\predict\predictuser'
isAtpath = r'G:\tianchi\weibo\predict\feature\isat'


#只需处理 12 月份的微博
def isAtOther():
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            readfile = open(trainpath+'\\'+filename,'r')
            outfile = open(isAtpath+'\\'+filename,'ab')
            for line in readfile:
                line_split = line.split('\t')
                
                if line_split[3].find('@') != -1:
                    outfile.write(line_split[0]+'\t'+line_split[2]+'\t'+str('1')+'\n')
                    print 'find @',line_split[3]
                else:
                    outfile.write(line_split[0]+'\t'+line_split[2]+'\t'+str('0')+'\n')
            readfile.close()
            outfile.close()
                        

isAtOther()
