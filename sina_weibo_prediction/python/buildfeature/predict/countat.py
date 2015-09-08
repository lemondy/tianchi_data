#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os

trainpath = r'G:\tianchi\weibo\predict\predictuser'

countAtpath = r'G:\tianchi\weibo\predict\feature\countat'

def countAt():
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            readfile = open(trainpath+'\\'+filename,'r')
            outfile = open(countAtpath+'\\'+filename,'ab')

            for line in readfile:
                line_split = line.split('\t')
                
                outfile.write(line_split[0]+'\t'+line_split[2]+'\t'+str(line_split[3].count('@'))+'\n')
                print 'write user',line_split[0],'count @',str(line_split[3].count('@'))
            readfile.close()
            outfile.close()

countAt()
