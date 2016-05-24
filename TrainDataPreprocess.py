#coding:utf-8

# this code is used for clean the train data
import argparse
import os
def CleanSubtitle(input,output):
    
if __name__=="__main__":
    current_path=os.getcwd()  
    #arguments parser
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",help="the path of train data file,default=data/GoodQA_Answer.txt",default="data/GoodQA_Answer.txt")
    parser.add_argument("--output",help="the output file",default="data/GoodQA_Answer.dat")
    args=parser.parse_args()
    
    input_file=open(args.input,'r')
    output_file=open(args.output,'w')
    line=input_file.readline()
    while line!="":
    	line=line.strip()
        if len(line)>0:
        	output_file.write(line+'\n')
    	line=input_file.readline()
    input_file.close()    
    output_file.close()
