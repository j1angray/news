#!usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

def open_excel(file_name,sheet_name):
	file = xlrd.open_workbook(file_name)
	sheet = file.sheet_by_name(sheet_name) 
	data =[]
	for i in range(0,sheet.nrows):
		data.append(list(sheet.row_values(i))) 
	return data


def merge(data,colnum):
	i=0
	result=[]
	for i in range(1,len(data)):
		if i<len(data)-1:
			if data[i][0] == data[i+1][0]: #此行与下一行的论文ID一致
				data[i+1][colnum] = data[i][colnum] + ';'+ data[i+1][colnum] #将两行的作者信息合并
			else:
				result.append(data[i]) #此行与下一行的论文ID不一致，把此行存入result  
		else:result.append(data[i])
	return result


def output_txt(txt_name,result):	 
	f = open(txt_name,'w') 
	for i in range(0,len(result)):
		f.write(result[i][0]+'\t'+ result[i][1]+ '\t' + result[i][2] + '\n') 
	f.close()

def main():
	data=open_excel(r'/Users/jiangruiyin/Desktop/材料2.xlsx',u'2010paper')
	result=merge(data,2)
	txt_name=('/Users/jiangruiyin/Desktop/合并结果.txt')
	output_txt(txt_name,result)	

if __name__=="__main__":
	main()
