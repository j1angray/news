#!usr/bin/env python


import xlrd
import os
import random

def read_text(text_path): #读取文本
	with open(text_path,'r') as f: 
		text=f.read()
	return text

def read_wordlist(excel_path,colnum): #读取词表
	file = xlrd.open_workbook(excel_path)
	sheet = file.sheets()[0] 
	wordlist =list(sheet.col_values(colnum))[1:]
	return wordlist

def random_sentence(text): #将语料以句子为单位划分，并随机打乱
	sentence_list=[]
	for sen in text.split('。/'):
		sentence_list.append(sen+'。/')
	random.shuffle(sentence_list) #随机打乱
	return sentence_list

def sep_sentence(sentence_list,percent): #按照9:1的比例分为训练语料与测试语料	
	prop=int(percent*len(sentence_list))
	train_text=[]
	text_text=[]
	for train_index in range(prop):
		train_text.append(sentence_list[train_index]+'\n')
	for test_index in range(train_index,len(sentence_list)):
		text_text.append(sentence_list[test_index]+'\n')
	return (train_text,text_text)


def mark_word(text): #将语料按规则进行标注以转化形式
	wordlist=[]
	marklist=[]
	for word in text.split('/'):
		if word != '\n':
			wordlist.append(word.strip())
	for elem in wordlist:
		if elem=='。':
				marklist.append(elem+'\t'+'BE'+'\n\n')
		elif len(elem)==1:
			marklist.append(elem+'\t'+'BE'+'\n')	
		elif len(elem)>1: #我这里为什么写“else:”在train_text.txt测试时就提示“string index out of range”而test_text.txt测试顺利？⚆_⚆
			n=len(elem)
			marklist.append(elem[0]+'\t'+'B'+'\n')
			marklist.append(elem[n-1]+'\t'+'E'+'\n')
			for i in range(1,n-1):
				marklist.append(elem[i]+'\t'+'M'+'\n')		
	return marklist


def write_result(result_path,text): #将结果写入txt文件
	f=open(result_path,'w')
	for elem in text:
		f.write(elem)
	f.close()


def multi_file(path): #遍历文件夹中所有文件并获取文件名
	for rootpath,dirname,filename in os.walk(path):
		return filename

def main():
	text=read_text(r'/Users/jiangruiyin/Desktop/任务7-20180316-蒋睿吟/1.txt')
	senlist=random_sentence(text)
	(train_text,test_text)=sep_sentence(senlist,0.9)
	write_result(r'/Users/jiangruiyin/Desktop/任务7-20180316-蒋睿吟/train_text.txt',train_text)
	write_result(r'/Users/jiangruiyin/Desktop/任务7-20180316-蒋睿吟/test_text.txt',test_text)
	test=read_text(r'/Users/jiangruiyin/Desktop/任务7-20180316-蒋睿吟/test_text.txt')
	train=read_text(r'/Users/jiangruiyin/Desktop/任务7-20180316-蒋睿吟/train_text.txt')
	marktest=mark_word(test)
	marktrain=mark_word(train)
	write_result(r'/Users/jiangruiyin/Desktop/任务7-20180316-蒋睿吟/test.txt',marktest)
	write_result(r'/Users/jiangruiyin/Desktop/任务7-20180316-蒋睿吟/train.txt',marktrain)

if __name__ == '__main__':
	main()
