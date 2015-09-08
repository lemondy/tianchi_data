#!/bin/usr/env python
# -*- coding:utf-8 -*-#
import os,jieba
from JaccardSimilarity import *

interestpath = r'G:\tianchi\weibo\predict\feature\interest'


trainpath = r'G:\tianchi\weibo\predict\feature\fenci'
predictpath = r'G:\tianchi\weibo\predict\predictuser'

def loadHistoryInterest(path):
    
    interests = dict()
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            userfile = open(trainpath+"\\"+filename,'r')
            name = filename.split('.')
            #不能使用 set 类型，会去重
            interestset = []
            for line in userfile:
                line = line.strip()
                line_split = line.split(',')
                for i in line_split:
                    interestset.append(i)
            interests[name[0]] = interestset
            #save memory
            userfile.close()
        interestset = []
    return interests


#Jaccard similarity
def buildInterest():

    #load the user's history data
    interests = loadHistoryInterest(trainpath)
    
    print 'len(interests)',len(interests)

    stopkey = [line.strip() for line in open(r'G:\tianchi\weibo\train\stopkey.txt','r')]
    
    #output user interest
    for root,dirnames,filenames in os.walk(predictpath):
        for filename in filenames:
            predictfile = open(predictpath+'\\'+filename,'r')
            outfile = open(interestpath+'\\'+filename,'ab')
            name = filename.split('.')

            for weibo_content in predictfile:
                weibo = weibo_content.split('\t')
                content = jieba.cut(weibo[3],cut_all=True)
                content_list = list(set(content)-set(stopkey))
                hash_interests = hashContentsList(interests[name[0]])
                hash_content = hashContentsList(content_list)
                
                intersection = calcIntersection(hash_interests,hash_content)
                unionset = calcUnionSet(hash_interests,hash_content,intersection)

                similarity = calcSimilarity(intersection,unionset)
                outfile.write(weibo[0]+'\t'+weibo[1]+'\t'+weibo[2]+'\t'+str(similarity)+'\n')
                print 'user',name[0],'similarity',similarity

            outfile.close()
            predictfile.close()
                

buildInterest() 
        
