#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os,random



activitypath = r'G:\tianchi\weibo\feature\activity'
interestpath = r'G:\tianchi\weibo\feature\interest'
isAtpath = r'G:\tianchi\weibo\feature\isAt'
countAtpath = r'G:\tianchi\weibo\feature\countAt'
urlpath = r'G:\tianchi\weibo\feature\url'

outpath = r'G:\tianchi\weibo\feature\putTogether'

def readActivity(path):
    activities = dict()
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            readfile = open(path+'\\'+filename,'r')
            name = filename.split('.')
            activity = []
            for line in readfile:
                line=line.strip()
                line_split = line.split('\t')
                activity.append(line_split[2])

            activities[name[0]] = activity
            readfile.close()
    return activities


def readInterest(path):
    interests = dict()

    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            readfile = open(path+'\\'+filename,'r')
            name = filename.split('.')
            interest = []
            for line in readfile:
                line=line.strip()
                line_split = line.split('\t')    
                interest.append(line_split[3])

            interests[name[0]] = interest
            readfile.close()
    return interests


def readIsAt(path):
    isAt = dict()
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            readfile = open(path+'\\'+filename,'r')
            name = filename.split('.')

            temp = []
            for line in readfile:
                line=line.strip()
                line_split = line.split('\t')
                temp.append(line_split[2])
            isAt[name[0]] = temp
            readfile.close()
    return isAt


def readCountAt(path):
    countAt = dict()

    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            readfile = open(path+'\\'+filename,'r')
            name = filename.split('.')

            temp = []
            for line in readfile:
                line=line.strip()
                line_split = line.split('\t')
                temp.append(line_split[2])
            countAt[name[0]] = temp
            readfile.close()
    return countAt

def readUrl(path):
    urls = dict()

    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            readfile = open(path+'\\'+filename,'r')
            name = filename.split('.')

            urllist = []
            for line in readfile:
                line=line.strip()
                line_split=line.split('\t')
                urllist.append(line_split[2])
            urls[name[0]] = urllist
            readfile.close()
    return urls
    
#将构造的特征进行整合
def integrateFeature():
    activityDict = readActivity(activitypath)
    print 'activity load over'
    interestDict = readInterest(interestpath)
    print 'interest load over'
    isAtDict = readIsAt(isAtpath)
    print 'isat load over'
    countAtDict = readCountAt(countAtpath)
    print 'countat load over'
    urlDict = readUrl(urlpath)
    print 'url load over'

    keys = activityDict.keys()
    print 'len(keys)',len(keys),'len(activityDict)',len(activityDict)
    
    for i in range(0,len(activityDict)):
        outfile = open(outpath+'\\'+keys[i]+'.txt','ab')
        activity = activityDict[keys[i]]
        interest = interestDict[keys[i]]
        isAt = isAtDict[keys[i]]
        countAt = countAtDict[keys[i]]
        url = urlDict[keys[i]]
        #outfile.write('activity'+'\t'+'interest'+'\t'+'isat'+'\t'+'countat'+'\t'+'url'+'\n')
        for j in range(0,len(activity)):
            if isAt[j] == '0':
                isAt[j] = str(random.random() / float(100.0))
            if countAt[j] == '0':
                countAt[j] = str(random.random()/ float(100.0))
            if url[j] == '0':
                url[j] = str(random.random() / float(100.0))
            if isAt[j] == '1':
                isAt[j] = str(random.random())
            if countAt[j] == '1':
                countAt[j] = str(random.random())
            if url[j] == '1':
                url[j] = str(random.random())
            outfile.write(activity[j]+'\t'+interest[j]+'\t'+isAt[j]+'\t'+countAt[j]+'\t'+url[j]+'\n')
        outfile.close()
        print 'user',keys[i],'out over'


integrateFeature()

trainpath = r'G:\tianchi\weibo\train\user-train-big'
finalpath = r'G:\tianchi\weibo\feature\final'

#将特征与评论转发赞组合在一起
def constructTrainset():
    users = dict()
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            readfile = open(trainpath+'\\'+filename,'r')
            name = filename.split('.')

            numberlist = []
            for line in readfile:
                line = line.strip()
                line_split = line.split('\t')
                numberlist.append(line_split[3]+','+line_split[4]+','+line_split[5])

            users[name[0]] = numberlist
            readfile.close()
    print 'number read over'
    
    for root,dirnames,filenames in os.walk(outpath):
        for filename in filenames:
            readfile = open(outpath+'\\'+filename,'r')
            
            name = filename.split('.')
            outfile = open(finalpath+'\\'+name[0]+'.csv','ab')
            numberlist = users[name[0]]

            lines = readfile.readlines()
            outfile.write('activity'+','+'interest'+','+'isat'+','+'countat'+','+'url'+','+'forward'+','+'comment'+','+'like'+'\n')
            for i in range(0,len(lines)):
                print 'i',i
                line = lines[i].strip().replace('\t',',')+','+numberlist[i]+'\n'
                outfile.write(line)
            
            print 'write user',name[0]
            readfile.close()
    
constructTrainset()
