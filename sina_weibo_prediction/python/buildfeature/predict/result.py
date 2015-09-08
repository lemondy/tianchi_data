#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os

#将预测的结果进行整合
togetherpath = r'G:\tianchi\weibo\predict\result\putAllTogether'
forwardpath = r'G:\tianchi\weibo\predict\result\forward'
commentpath = r'G:\tianchi\weibo\predict\result\comment'
likepath = r'G:\tianchi\weibo\predict\result\like'

def readPredictValue(path):
    mDict = dict()
    for root,dirnames,filenames in os.walk(path):
        
        
        for filename in filenames:
            readfile = open(path+'\\'+filename,'r')
            name = filename.split('.')
            #标识是否为第一行
            first = 0
            predictlist = []
            for line in readfile:
                line = line.strip()
                line_split = line.split(',')
                if first == 0:
                    first = 1
                else:
                   # print line_split[1]
                    predictlist.append(line_split[1])
            mDict[name[0]] = predictlist
            readfile.close()
    return mDict

                    
def putPredictTogether(path):
    
    forwardDict = readPredictValue(forwardpath)
    print 'forward load over'
    commentDict = readPredictValue(commentpath)
    print 'comment load over'
    likeDict = readPredictValue(likepath)
    print 'like load over'

    print 'data load over'
    
    
    forwardkeys = forwardDict.keys()
    commentkeys = commentDict.keys()
    likekeys = likeDict.keys()

    print len(forwardkeys),len(commentkeys),len(likekeys)
    
    intersect = list(set(forwardkeys).intersection(set(commentkeys)))
    intersect2 = list(set(intersect).intersection(set(likekeys)))
    print 'len(intersect2)',len(intersect2)
    '''
    for user in forwardkeys:
        if(user in commentkeys) and (user in likekeys):
            forwardlist = forwardDict[user]
            commentlist = commentDict[user]
            likelist = likeDict[user]
            

            outfile = open(path+'\\'+user+'.txt','ab')
            for i in range(0,len(forwardlist)):
                forward = float(forwardlist[i])
                comment = float(commentlist[i])
                like = float(likelist[i])

                outfile.write(str(abs(int(forward)))+','+str(abs(int(comment)))+','+str(abs(int(like)))+'\n')
            outfile.close()
            '''

putPredictTogether(togetherpath)

        

            

    
