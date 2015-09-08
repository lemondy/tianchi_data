#!/bin/usr/env python
# -*- coding:utf-8 -*-#
from shutil import copy
import os

trainpath = r'G:\tianchi\weibo\train\user-train-big'
predictpath = r'G:\tianchi\weibo\predict\everyuserdata'
outpath = r'G:\tianchi\weibo\predict\predictuser'

def getPredictUser():
    predictuser = set()
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            name = filename.split('.')
            predictuser.add(name[0])
    print 'trainpath over'
    
    for root,dirnames,filenames in os.walk(predictpath):
        for filename in filenames:
            name = filename.split('.')
            if name[0] in predictuser:
                copy(predictpath+'\\'+filename,outpath+'\\'+filename)
                print 'copy user',name[0]


getPredictUser()

    
    


    
    
