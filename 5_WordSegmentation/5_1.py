#!usr/bin/env python
#coding:utf-8

import xlrd
import os


def read_text(text_path): #读取需处理的文本
	with open(text_path,'r') as f:
		text=f.read()
	return list(text)

def read_wordlist(excel_path,colnum): #读取词表
	file = xlrd.open_workbook(excel_path)
	sheet = file.sheets()[0] 
	wordlist =list(sheet.col_values(colnum))[1:]
	return wordlist


def split(text,MaxLen,wordlist): #最大逆向分词算法（MaxLen是规定匹配长度即最大匹配长度，本测试中取MaxLen=6）
	result_list=[] #存放分词结果 
	w=[] #存放截取的词语
	text_length = len(text) #文本总长度
	while text_length>0:
		split_length = min(text_length, MaxLen) #实际截取长度（文本长度>=6时，取6，否则取文本自身长度为截取长度）
		for i in range(split_length, 0, -1):
			w = text[text_length - i: text_length] #截取text_length-i到text_length-1索引的词进行匹配
			w="".join(w) #连接截取的元素
			if w in wordlist:
				result_list.append(w)
				text_length = text_length - i
				break
			elif i == 1:
				result_list.append(w)
				text_length = text_length - 1
	result_list.reverse() #把逆向分词结果结果以文本原始顺序输出
	result="/".join(str(w) for w in result_list)
	return result

def write_result(result_path,result): #将结果写入txt文件
	f=open(result_path,'w')
	f.write(result)
	f.close()

def multi_file(path): #遍历文件夹中所有文件并获取文件名
	for rootpath,dirname,filename in os.walk(path):
		return filename

def main():
	wordlist=read_wordlist(r'/Users/jiangruiyin/Desktop/任务5-20180228-蒋睿吟/词表/words.xlsx',1)+read_wordlist(r'/Users/jiangruiyin/Desktop/任务5-20180228-蒋睿吟/词表/stopwords.xlsx',1)
	text_path=r'/Users/jiangruiyin/Desktop/任务5-20180228-蒋睿吟/分词文本/'
	filesname=multi_file(text_path)	
	for filename in filesname:
		text=read_text(text_path+filename)
		result=split(text,6,wordlist)
		result_path=r'/Users/jiangruiyin/Desktop/任务5-20180228-蒋睿吟/分词结果/'+filename
		write_result(result_path,result)


if __name__=="__main__":
    main()

