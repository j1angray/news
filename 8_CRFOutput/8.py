#!usr/bin/env python


def read_text(text_path): #读取文本
	with open(text_path,'r') as f: 
		text=f.readlines()
	return text

def cal_PRF(text):
	p=0
	prf_list=[]
	h=[]
	m=[]
	for i in range(len(text)):
		sen=text[i].strip()
		if sen!='': 		#注意去除output文档中的空格或空行
			prf_list.append(sen.split('\t'))
	h=[y for [x,y,z] in prf_list]
	m=[z for [x,y,z] in prf_list]
	for l in range(len(h)):
		if h[l]==m[l] and h[l]==('B'or'BE'):	#识别正确的词语个数
			p=p+1
	h_num=h.count('B')		#人工标注出的词语个数
	m_num=m.count('B')		#机器识别出的词语个数
	p_value=p/m_num
	r_value=p/h_num
	f_value=2*p_value*r_value/(p_value+r_value)
	return (p_value,r_value,f_value)

def write_result(output_path,result_path,value): #将结果写入txt文件
	fp=open(output_path,'r')
	for line in fp:
		f=open(result_path,'a')
		f.write(line)
	f.write('\n\n准确率Precision:'+str(value[0])+'\n\n召回率(Recall):'+str(value[1])+'\n\nF值(F-Measure):'+str(value[2]))
	fp.close()
	f.close()



def main():
	output_path=r'/Users/jiangruiyin/Desktop/任务8-20180322-蒋睿吟/output.txt'
	result_path=r'/Users/jiangruiyin/Desktop/任务8-20180322-蒋睿吟/result.txt'
	text=read_text(output_path)
	value=cal_PRF(text)
	write_result(output_path,result_path,value)


if __name__ == '__main__':
	main()
