#!usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

def count_keyword(keylist):
	dic={}
	for key in keylist:
		if key in dic:
			dic[key]+=1
		else:
			dic[key]=1
	return(dic)

def open_excel_keywordlist(file_name,sheet_name,colnum):
	file = xlrd.open_workbook(file_name) 
	sheet = file.sheet_by_name(sheet_name) 
	data =list(sheet.col_values(colnum)) #获取某一列的数据存入列表
	wordlist = []
	for i in data :
		wordlist.extend(i.strip().split('/')) #\i元素按照“/”分开,再追加进wordlist

	keydic=count_keyword(wordlist) #将列表中各元素存入词典
	return keydic

def output_txt(txt_name,keydic): 
	f = open(txt_name,'w') 
	for sort in sorted(keydic.items(),key=lambda j:j[1],reverse=1): #降序排序
		for item in sort:
			f.write(str(item)+'\t')
		f.write('\n')	
	f.close()

def main():
	keydic=open_excel_keywordlist(r'/Users/jiangruiyin/Desktop/材料1.xlsx',u'2012paper',2)	
	txt_name=('/Users/jiangruiyin/Desktop/关键词频次.txt')
	output_txt(txt_name,keydic)	

if __name__=="__main__":
	main()