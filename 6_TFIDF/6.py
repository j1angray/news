#!usr/bin/env python


import xlrd
import os
import math


def read_text(text_path): #读取文本
	with open(text_path,'r') as f: 
		text=f.read()
	return text

def read_wordlist(excel_path,colnum): #读取词表
	file = xlrd.open_workbook(excel_path)
	sheet = file.sheets()[0] 
	wordlist =list(sheet.col_values(colnum))[1:]
	return wordlist

def count_keyword(keylist,wordlist): #去除停用词后的词频统计
	dic={}
	for key in keylist.split('/'):
		if key not in wordlist:
			if key in dic:
				dic[key]+=1
			else:
				dic[key]=1
	return dic

def tf_value(keydic): #计算词频  
	max_fre=max(keydic.values())
	for key in keydic:
		keydic[key]=keydic[key]/max_fre# 词频标准化:词频=某个词在文章中出现次数/该文出现次数最多次的出现次数
	return keydic

def build_corpuslist(dic): #获得语料库元素
	word_list=[]
	for key in dic:
		word_list.append(key) 
	return word_list


def tfidf_value(keydic,corpus_list):#计算TF-IDF值
	tfidf_dic={}
	count_text=len(corpus_list)
	for key in keydic:
		tfidf_dic.setdefault(key,0)
		for word_list in corpus_list:
			if key in word_list:
				tfidf_dic[key]+=1
	for key in tfidf_dic:
		tfidf_dic[key]=math.log(count_text/(tfidf_dic[key]+1))#计算逆文档频率,逆文档频率=ln(语料库文章总数/(包含该词的文档数+1))
		tfidf_dic[key]*=keydic[key]
	return tfidf_dic


def multi_file(path): #遍历文件夹中所有文件并获取文件名
	for rootpath,dirname,filename in os.walk(path):
		return filename

def write_result(result_path,dic): #将结果写入txt文件
	f = open(result_path,'w') 
	for sort in sorted(dic.items(),key=lambda j:j[1],reverse=1): #降序排序
		for item in sort:
			f.write(str(item)+'\t')
		f.write('\n')	
	f.close()

def main():
	corpus_list=[]
	text_path=r'/Users/jiangruiyin/Desktop/任务6-20180312-蒋睿吟/分词结果/'
	filesname=multi_file(text_path)	
	for filename in filesname:
		keylist=read_text(text_path+filename)	
		wordlist=read_wordlist(r'/Users/jiangruiyin/Desktop/任务6-20180312-蒋睿吟/stopwords.xlsx',1)
		keydic=count_keyword(keylist,wordlist)
		tf_value(keydic)
		corpus_list.append(keydic)#构建语料库
		tfidf_dic=tfidf_value(keydic,corpus_list)
		result_path=r'/Users/jiangruiyin/Desktop/任务6-20180312-蒋睿吟/tfidf/'+filename
		write_result(result_path,tfidf_dic)

if __name__ == '__main__':
	main()
