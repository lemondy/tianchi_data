#!/usr/bin/env python
#-*- encoding:utf-8 -*-

product_N_input_file = open('..\\..\\data\\gen\\item_feature_two_week.txt','r')
product_N_input = product_N_input_file.readlines()
product_N_input_file.close()

product_R_input_file = open('..\\..\\data\\gen\\item_store_feature_two_week.txt','r')
product_R_input=product_R_input_file.readlines()
product_R_input_file.close()
#输出到文件中，保存的是商品在四周内总销量
product_amount = open('..\\..\\data\\gen\\product_amount_two.txt','a')
#初步使用去年两周的数据来作为接下来两周的仓库数量
#全国的数据
product_N_dict = {}
product_R_dict = {}

#全国
for product in product_N_input:
	product_item = product.split(',')
	#item_id, qty_alipay
	if product_N_dict.has_key((product_item[1],'all')):
		product_N_dict[(product_item[1],'all')] += int(product_item[29])
	else:
		product_N_dict[(product_item[1],'all')] = int(product_item[29])

#product_amount.write(str(product_N_dict))
items_N = map(lambda x:str(x[0][0])+","+str(x[0][1])+","+str(x[1])+'\n',product_N_dict.items())
def compare(a,b):
	a=a[:-1].split(",")
	a=int(a[0])
	b=b[:-1].split(",")
	b=int(b[0])
	return a-b
items_N=sorted(items_N,cmp=compare)
for item in items_N:
	product_amount.write(item)
print 'product_amount_N', reduce(lambda x,y:x+y, product_N_dict.values())
#分区
for product in product_R_input:
	product_item = product.split(',')
	#item_id, qty_alipay_njhs 非聚划算的件数
	if product_R_dict.has_key((product_item[1],product_item[2])):
		product_R_dict[(product_item[1],product_item[2])] += int(product_item[30])
	else:
		product_R_dict[(product_item[1],product_item[2])] = int(product_item[30])

items_R = map(lambda x:str(x[0][0])+","+str(x[0][1])+","+str(x[1])+'\n',product_R_dict.items())
items_R = sorted(items_R,cmp=compare)
print 'product_amount_R', reduce(lambda x,y:x+y, product_R_dict.values())
for item in items_R:
	product_amount.write(item)

