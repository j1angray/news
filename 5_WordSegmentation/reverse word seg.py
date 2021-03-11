#!usr/bin/env python
#coding:utf-8

import xlrd

def read_text(text_path): #读取需处理的文本
	with open(text_path,encoding='gbk') as f: #来源文本的编码模式为gbk
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
		split_length = min(text_length, MaxLen) #实际截取长度（文本长度>=MaxLen时，取MaxLen，否则取文本自身长度为截取长度）
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


def main():
	wordlist=read_wordlist(u'/Users/jiangruiyin/Desktop//book.xls',1)
	text_path=u'/Users/jiangruiyin/Desktop/待分词语料.txt'
	text=read_text(text_path)
	result=split(text,5,wordlist)
	result_path=u'/Users/jiangruiyin/Desktop/逆向分词结果.txt'
	write_result(result_path,result)


if __name__=="__main__":
    main()

