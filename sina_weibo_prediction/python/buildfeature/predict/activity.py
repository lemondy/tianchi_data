#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os
import datetimeSub

baseactivitypath = r'G:\tianchi\weibo\predict\baseactivity.txt'
predictpath = r'G:\tianchi\weibo\predict\predictuser'
trainpath = r'G:\tianchi\weibo\train\user-train-big'
activitypath = r'G:\tianchi\weibo\predict\feature\activity'

def buildBaseActivity():
    outbaseactivity  = open(baseactivitypath,'ab')
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            readfile = open(trainpath+'\\'+filename,'r')
            name = filename.split('.')
            activitycount = 0
            lines = readfile.readlines()
            activitycount = len(lines)
            readfile.close()
            outbaseactivity.write(name[0]+'\t'+str(activitycount)+'\n')
            if activitycount > 1200:
                print 'activity user',name[0]
    
#buildBaseActivity()


def buildActivity():
    activity = dict()
    for user in open(baseactivitypath,'r'):
        content = user.split('\t')
        activity[content[0]] = content[1]

    #print 'len(activity)',len(activity)
    starttime = '2014-07-01'

    
    for root,dirnames,filenames in os.walk(predictpath):
        for filename in filenames:
            readfile = open(predictpath+'\\'+filename,'r')
            outfile = open(activitypath+'\\'+filename,'ab')
            count = 0
            for line in readfile:
                line_split = line.split('\t')
                
                count += 1
                endtime = line_split[2]
                acti = float(int(activity[line_split[0]])+count)/float(datetimeSub.daysdiff(endtime,starttime))
                outfile.write(line_split[0]+'\t'+line_split[2]+'\t'+str(acti)+'\n')
            outfile.close()
            readfile.close()
                    


buildActivity()

