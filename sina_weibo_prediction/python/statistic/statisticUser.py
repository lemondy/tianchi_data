#!/bin/usr/env python
#this file statistic how many users in the train set and predict set

trainpath = r'G:\tianchi\weibo\weibo_train_data.txt'
predictpath = r'G:\tianchi\weibo\weibo_predict_data.txt'

trainoutpath = r'G:\tianchi\weibo\train\users.txt'
predictoutpath = r'G:\tianchi\weibo\predict\users.txt'

userNotInTrainpath = r'G:\tianchi\weibo\userNotInTrain.txt'

def statisticUser(trainpath,predictpath):
    trainfile = open(trainpath,'r')
    predictfile = open(predictpath,'r')
    trainout = open(trainoutpath,'ab')
    predictout = open(predictoutpath,'ab')
    out = open(userNotInTrain,'ab')
    trainusers = set()
    predictusers = set()
    
    print 'begin'
    #get the train user
    for line in trainfile:
        line_split = line.split('\t')
        if line_split[0] not in trainusers:
            trainusers.add(line_split[0])
    
    #get predict user
    for line in predictfile:
        line_split = line.split('\t')
        if line_split[0] not in predictusers:
            predictusers.add(line_split[0])
    
    
    for user in trainusers:
        trainout.write(user+'\n')
    print 'train user write over'
    
    for user in predictusers:
        predictout.write(user+'\n')
    print 'predict user write over'
   

#statisticUser(trainpath,predictpath)

def statUserNotInTrain():
    trainuser = [line.strip() for line in open(r'G:\tianchi\weibo\train\users.txt','r')]
    predictuser = [line.strip() for line in open(r'G:\tianchi\weibo\predict\users.txt','r')]

    userNotInTrain = list(set(predictuser).difference(set(trainuser)))
    out = open(userNotInTrainpath,'ab')
    for user in userNotInTrain:
        out.write(user+'\n')

statUserNotInTrain()
