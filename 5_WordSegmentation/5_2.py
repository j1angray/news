#!usr/bin/env python


import xlrd
import os


def read_text(text_path): #读取需处理的文本
	with open(text_path,'r') as f: 
		text=f.read()
	return text

def count_keyword(keylist): #词频统计
	dic={}
	for key in keylist.split('/'):
		if key in dic:
			dic[key]+=1
		else:
			dic[key]=1
	return dic

def write_result(result_path,keydic): #将结果写入txt文件
	f = open(result_path,'w') 
	for sort in sorted(keydic.items(),key=lambda j:j[1],reverse=1): #降序排序
		for item in sort:
			f.write(str(item)+'\t')
		f.write('\n')	
	f.close()

def multi_file(path): #遍历文件夹中所有文件并获取文件名
	for rootpath,dirname,filename in os.walk(path):
		return filename

def main():
	text_path=r'/Users/jiangruiyin/Desktop/任务5-20180228-蒋睿吟/分词结果/'
	filesname=multi_file(text_path)	
	for filename in filesname:
		keylist=read_text(text_path+filename)	
		keydic=count_keyword(keylist)
		result_path=r'/Users/jiangruiyin/Desktop/任务5-20180228-蒋睿吟/词频统计/'+filename
		write_result(result_path,keydic)

if __name__ == '__main__':
	main()
