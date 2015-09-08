#!/bin/usr/env python
# -*- coding:utf-8 -*- #
import os
#from shutil import copy
#count users whether their forward,comments,like all are zero.

#字符串前面加一个 r 就可以让字符串不转义 '\t'
trainpath = r'G:\tianchi\weibo\train\everyuserdata'
zeroUserpath = r'G:\tianchi\weibo\train\zeroUser.txt'


def count0user(path):
    forward_sum = 0
    comment_sum = 0
    like_sum = 0
    out = open(zeroUserpath,'ab')
    #visit files under the directory
    for root,dirnames,filenames in os.walk(path):
        #traverse all files
        for filename in filenames:
            infile = open(path + '\\' + filename)
            #traverse file content
            for line in infile:
                line_split = line.split('\t')
                forward_sum =forward_sum + int(line_split[3])
                comment_sum =comment_sum + int(line_split[4])
                like_sum =like_sum + int(line_split[5])
            print 'forward',forward_sum,'comment',comment_sum,'like',like_sum

       
            if ((forward_sum == 0) and (comment_sum == 0) and (like_sum == 0)):
                out.write(line_split[0]+'\n')
                
            
            #clear counter
            forward_sum = 0
            comment_sum = 0
            like_sum = 0


count0user(trainpath)            
    
