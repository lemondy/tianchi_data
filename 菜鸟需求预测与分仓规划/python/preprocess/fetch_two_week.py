#!/usr/bin/env python
#-*- encoding:utf-8 -*-

'''
#提取去年四周的数据，前后一周：20141221--20150117
item_N_input = open('..\\..\\data\\item_feature1.csv','r').readlines()
item_R_input = open('..\\..\\data\\item_store_feature1.csv','r').readlines()

item_N_ouput = open('..\\..\\data\\gen\\item_feature_four_week.txt','w')
item_R_ouput = open('..\\..\\data\\gen\\item_store_feature_four_week.txt','w')
#全国
for product in item_N_input:
	product_item = product.split(',')
	if product_item[0] >= '20141221' and product_item[0] <= '20150117':
		item_N_ouput.write(product)
		#print 'product',product
item_N_ouput.close()

#分区
for product in item_R_input:
	product_item = product.split(',')
	if product_item[0] >= '20141221' and product_item[0] <= '20150117':
		item_R_ouput.write(product)
		#print 'product',product
item_R_ouput.close()
'''

#去年约两周的数据
item_N_input = open('..\\..\\data\\item_feature1.csv','r').readlines()
item_R_input = open('..\\..\\data\\item_store_feature1.csv','r').readlines()

item_N_ouput = open('..\\..\\data\\gen\\item_feature_two_week.txt','w')
item_R_ouput = open('..\\..\\data\\gen\\item_store_feature_two_week.txt','w')
#全国
for product in item_N_input:
	product_item = product.split(',')
	if product_item[0] >= '20141227' and product_item[0] <= '20150111':
		item_N_ouput.write(product)
		#print 'product',product
item_N_ouput.close()

#分区
for product in item_R_input:
	product_item = product.split(',')
	if product_item[0] >= '20141227' and product_item[0] <= '20150111':
		item_R_ouput.write(product)
		#print 'product',product
item_R_ouput.close()


