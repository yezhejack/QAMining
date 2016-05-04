#coding:utf-8
import random

#从正例的问句中建立新的反例 104720个样例
if __name__=="__main__":
    input_file=open("data/dialogues_positive_simple.txt","r")
    output_file=open("data/dialogues_negative_simple.txt","w")
    ans_list=[]
    line=input_file.readline()
    while line!="":
        line=input_file.readline()
        line=input_file.readline().strip()
        ans_list.append(line)
        line=input_file.readline()
    index=1
    while index<104721:
        output_file.write(str(index)+'\n')
        output_file.write(ans_list[random.randint(0,len(ans_list)-1)]+'\n')
        output_file.write(ans_list[random.randint(0,len(ans_list)-1)]+'\n')
        index+=1
    input_file.close()
    output_file.close()

    input_file=open("data/dialogues_positive_simple.txt","r")
    output2_file=open("data/dialogues_negative_simple_reverse.txt","w")
    line0=input_file.readline()
    while line0!="":
        line0=line0.strip()
        output2_file.write(line0+'\n')
        line1=input_file.readline().strip()
        line2=input_file.readline().strip()
        output2_file.write(line2+'\n')
        output2_file.write(line1+'\n')
        line0=input_file.readline().strip()
    input_file.close()
    output2_file.close()