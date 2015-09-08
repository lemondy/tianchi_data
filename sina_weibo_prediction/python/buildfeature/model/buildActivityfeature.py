#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os,datetimeSub

#构造用户的活跃度  n/time

trainpath = r'G:\tianchi\weibo\train\user-train-big'
baseactivitypath = r'G:\tianchi\weibo\train\baseactivity.txt'
activitypath = r'G:\tianchi\weibo\feature\activity'

#统计 20140701--20141130 时间段所发微博总数
def buildBaseActivity():
    outbaseactivity  = open(baseactivitypath,'ab')
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            readfile = open(trainpath+'\\'+filename,'r')
            activitycount = 0
            for line in readfile:
                line_split = line.split('\t')
                if line_split[2] < '2014-12-01':
                    activitycount += 1
                else:
                    break
            readfile.close()
            outbaseactivity.write(line_split[0]+'\t'+str(activitycount)+'\n')
            if activitycount > 1200:
                print 'activity user',line_split[0]
    

#buildBaseActivity()

#构造 12 微博活跃度
def buildActivity():
    activity = dict()
    for user in open(baseactivitypath,'r'):
        content = user.split('\t')
        activity[content[0]] = content[1]

    #print 'len(activity)',len(activity)
    starttime = '2014-07-01'

    
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            readfile = open(trainpath+'\\'+filename,'r')
            outfile = open(activitypath+'\\'+filename,'ab')
            count = 0
            for line in readfile:
                line_split = line.split('\t')
                if line_split[2] > '2014-11-30':
                    count += 1
                    endtime = line_split[2]
                    acti = float(int(activity[line_split[0]])+count)/float(datetimeSub.daysdiff(endtime,starttime))
                    outfile.write(line_split[0]+'\t'+line_split[2]+'\t'+str(acti)+'\n')
            outfile.close()
            readfile.close()
                    


buildActivity()
