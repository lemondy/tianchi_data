#!/bin/usr/env python
# -*- coding: utf-8 -*-
#get every user data from the train set and predict set


trainpath = r'G:\tianchi\weibo\weibo_train_data.txt'
predictpath = r'G:\tianchi\weibo\weibo_predict_data.txt'
usertrainpath = r'G:\tianchi\weibo\train\everyuserdata'
userpredictpath = r'G:\tianchi\weibo\predict\everyuserdata'

def isExist(dataset,element):
    for i in dataset:
        if i == element:
            return True
    return False

def getEveryUserData():
    userNotInTrain = [line.strip() for line in open(r'G:\tianchi\weibo\userNotInTrain.txt','r')]
    predictUser = [line.strip() for line in open(r'G:\tianchi\weibo\predict\users.txt','r')]
    #for user in userNotInTrain:
        #print 'user',user
    #delete user who does not show in the train
    new_predictuser = []
    '''for user in predictUser:
        if isExist(userNotInTrain,user) == False:
            new_predictuser.append(user)'''
    #get two list difference
    new_predictuser = list(set(predictUser).difference(set(userNotInTrain)))
    print 'len(new_predictuser)',len(new_predictuser)

    #get train user data
    traindata = open(trainpath,'r')
    for line in traindata:
        line_split = line.split('\t')
        if line_split[0] in new_predictuser:
            userfile = open(usertrainpath+'\\'+line_split[0]+'.txt','ab')
            userfile.write(line)
    traindata.close()
    print 'trian data over'
    
    #get predict user data
    predictdata = open(predictpath,'r')
    for line in predictdata:
        line_split = line.split('\t')
        outfile = open(userpredictpath+'\\'+line_split[0]+'.txt','ab')
        outfile.write(line)
    print 'predict data over'
    predictdata.close()
    

getEveryUserData()
