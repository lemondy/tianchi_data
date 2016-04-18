#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#统计所有分区仓库中的商品是否都包含在全国仓库中
#全国
productsPath_N = open('..\\..\\data\\item_feature1.csv','r')
products_N = productsPath_N.readlines()
products_N_title = products_N[0]
#print len(products_N)
#print products_N[1].split(',')
#分区
productsPath_R = open('..\\..\\data\\item_store_feature1.csv','r')
products_R = productsPath_R.readlines()
products_R_title = products_R[0]
#print len(products_R)

#读取商品ID
#全国,分区
products_N_ID = set()
products_R_ID = set()

for product in products_N[1:len(products_N)]:
	product_item_feature = product.split(',')
	products_N_ID.add(product_item_feature[1])  #item id

for product in products_R[1:len(products_R)]:
	product_item_feature = product.split(',')
	products_R_ID.add(product_item_feature[1])  #item id
print 'len(products_R_ID):',len(products_R_ID)

print 'len(products_N_ID):',len(products_N_ID)

#product_dif = products_N_ID - products_R_ID
product_dif = products_R_ID - products_N_ID
print 'difference:',product_dif

#两种情况输出均为output: set([])

#并集
product_N_R = products_N_ID | products_R_ID

#sample_submission
sample_products_file = open('..\\..\\data\\sample_submission.csv','r')
sample_products =  sample_products_file.readlines()

sample_products_ID = set()
for product in sample_products:
	product_item = product.split(",")
	sample_products_ID.add(product_item[0])
print 'sample line',len(sample_products_ID)

print 'dif2:',(product_N_R-sample_products_ID)