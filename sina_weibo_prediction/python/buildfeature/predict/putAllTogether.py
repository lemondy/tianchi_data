#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os,random



activitypath = r'G:\tianchi\weibo\predict\feature\activity'
interestpath = r'G:\tianchi\weibo\predict\feature\interest'
isAtpath = r'G:\tianchi\weibo\predict\feature\isat'
countAtpath = r'G:\tianchi\weibo\predict\feature\countat'
urlpath = r'G:\tianchi\weibo\predict\feature\url'
predictpath = r'G:\tianchi\weibo\predict\predictuser'

outpath = r'G:\tianchi\weibo\predict\feature\putTogether'

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

def readID(path):
    weiboID = dict()
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            readfile = open(path+'\\'+filename,'r')
            name = filename.split('.')

            idlist = []
            for line in readfile:
                line = line.strip()
                line_split = line.split('\t')
                idlist.append(line_split[1]+','+line_split[2])
            weiboID[name[0]] = idlist
            readfile.close()
    return weiboID

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
    weiboIDdict = readID(predictpath)
    print 'id load over'

    keys = activityDict.keys()
    print 'len(keys)',len(keys),'len(activityDict)',len(activityDict)
    
    for i in range(0,len(activityDict)):
        outfile = open(outpath+'\\'+keys[i]+'.csv','ab')
        activity = activityDict[keys[i]]
        interest = interestDict[keys[i]]
        isAt = isAtDict[keys[i]]
        countAt = countAtDict[keys[i]]
        url = urlDict[keys[i]]
        weiboId = weiboIDdict[keys[i]]
        outfile.write('uid'+','+'mid'+','+'pubtime'+','+'activity'+','+'interest'+','+'isat'+','+'countat'+','+'url'+'\n')
        for j in range(0,len(activity)):
            if isAt[j] == '0':
                isAt[j] = str(random.random() / float(100.0))
            if countAt[j] == '0':
                countAt[j] = str(random.random()/ float(100.0))
            if url[j] == '0':
                url[j] = str(random.random() / float(100.0))
            if isAt[j] == '1':
                isAt[j] = str(random.random())
            #if int(countAt[j]) == 1:
             #   countAt[j] = str(random.random())
            if url[j] == '1':
                url[j] = str(random.random())
            outfile.write(keys[i]+','+weiboId[j]+','+activity[j]+','+interest[j]+','+isAt[j]+','+countAt[j]+','+url[j]+'\n')
        outfile.close()
        print 'user',keys[i],'out over'


integrateFeature()





