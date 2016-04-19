#!/usr/bin/env python
#-*- encoding:utf-8 -*-

product_four_week_file = open('..\\..\\data\\gen\\product_amount_two.txt','r')
product_sub_sample_file = open('..\\..\\data\\sample_submission.csv','r')

submission_result = open('..\\..\\data\\submission_result.csv','w+')
product_four_week = product_four_week_file.readlines()
product_four_week_file.close()

product_sub_sample = product_sub_sample_file.readlines()
product_sub_sample_file.close()

product_four_week_dict = {}
product_sub_sample_dict = {}

for product in product_four_week:
	product_item = product.split(',')
	product_four_week_dict[(product_item[0],product_item[1])] = product_item[2]

for product in product_sub_sample:
	product_item = product.split(',')
	product_sub_sample_dict[(product_item[0],product_item[1])] = 0

#合并示例中的和在历史中有数据的商品
for key in product_sub_sample_dict.keys():
	if product_four_week_dict.has_key(key):
		submission_result.write(key[0]+','+key[1]+','+product_four_week_dict[key])
	else:
		submission_result.write(key[0]+','+key[1]+','+str(product_sub_sample_dict[key])+'\n')




