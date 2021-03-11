#!usr/bin/env python
#coding:utf-8

import xlrd
import time

def open_excel_data(file_name,sheet_name,colnum): 
	file = xlrd.open_workbook(file_name)
	sheet = file.sheet_by_name(sheet_name) 
	data =list(sheet.col_values(colnum)) 
	return data

def set_datalist(data): 
	datalist = []
	for i in data :
		datalist.extend(i.split('/'))
	datalist = set(datalist)
	return datalist


def form_datalist(data): 
	formated_datalist=[]
	for i in data:
		formated_datalist.append(i.split('/'))
	return formated_datalist


def create_matrix(datalist): 
	length = len(datalist)+1 
	matrix = [[0 for col in range(length)] for row in range(length)]
	col=1
	row=1
	for row_1 in datalist:
		matrix[0][col] = row_1 
		col += 1
		if col == length:
			break 
	for col_1 in datalist:
		matrix[row][0] = col_1 
		row += 1
		if row == length:
			break 
	return matrix


def count_setmatrix(matrix,formated_datalist): 
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix)):
			if matrix[row][0] == matrix[0][col]:
				matrix[row][col] = str(0)
			else:
				count = 0
				for i in formated_datalist:
					if matrix[row][0] in i and matrix[0][col] in i:
						count += 1
					else:
						continue
				matrix[row][col] = str(count)
	return matrix


def output_txt(txt_path,matrix): 
	with open(txt_path,'w') as f :
		for row in range(0,len(matrix)):   
			for col in range(0,len(matrix)):
				if row == 0 and col == 0:
					f.write('\t')
				else:
 					f.write(str(matrix[row][col]) + '\t') 
			f.write('\n')


def main():
	begin=time.clock()
	data=open_excel_data(r'/Users/jiangruiyin/Desktop/任务4-20180228-蒋睿吟/材料1.xlsx',u'2012paper',2)	
	wordlist=set_datalist(data)
	formated_wordlist=form_datalist(data)
	init_matrix=create_matrix(wordlist)
	txt_path=r'/Users/jiangruiyin/Desktop/任务4-20180228-蒋睿吟/关键词贡献矩阵.txt'
	matrix=count_setmatrix(init_matrix,formated_wordlist)
	output_txt(txt_path,matrix)
	end=time.clock()
	print('程序运行耗时%s秒'%(end-begin)) #打印出程序运行的耗时

if __name__=="__main__":
	main()

 