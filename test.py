#coding:utf-8
import os
if __name__=='__main__':
    input_file=open('/Users/JackYip/Workspace/QA_Mining/GoodQA.txt','r')
    output_file=open('GoodQA.dat','w')
    line=input_file.readline()
    while line!='':
        if len(line)>1:
            output_file.write(line)
        line=input_file.readline()
    input_file.close()
    output_file.close()
