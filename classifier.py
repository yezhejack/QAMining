#coding:utf-8

# this code is using the classifier to determine which two sentences are a dialogue
# the default postitive input is data/patterns
# the default negative input is data/Answer_patterns.dat
# this code will use libsvm https://www.csie.ntu.edu.tw/~cjlin/libsvm/

import os
import argparse
import json

if __name__=="__main__":
    current_path=os.getcwd()
    #parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument('--pos_input',help='the name of input file in ./data/,default=tagged_GoodQA.dat',default='tagged_GoodQA.dat')
    parser.add_argument('--neg_input',help='the name of output file in ./data/,default=tagged_GoodQA_Answer.dat',default='tagged_GoodQA_Answer.dat')
    args=parser.parse_args()
    
    # read positive input
    f=open(current_path+'/data/'+args.pos_input,'r')
    tmp_str=f.readline()
    pos_patterns=json.loads(tmp_str)
    f.close()
    
    # read negative input
    f=open(current_path+'/data/'+args.neg_input,'r')
    tmp_str=f.readline()
    neg_patterns=json.loads(tmp_str)
    f.close()

    # turn the data into vectors and output the result into tmp_libsvm.dat
    f=open(current_path+'/data/tmp_libsvm_train.dat','w')
    tag_index_dict={}
    counter=0
    for pat in pos_patterns:
        sen="1"
        l=[]
        for tag in pat:
            if tag in tag_index_dict:
                l.append(tag_index_dict[tag])
            else:
                counter+=1
                tag_index_dict[tag]=counter
                l.append(counter)
        l.sort()
        pre_index=0
        same_index_counter=0
        for index in l:
            if pre_index==0:
                pre_index=index
                same_index_counter+=1
            elif pre_index==index:
                same_index_counter+=1
            elif pre_index!=index:
                sen=sen+" "+str(pre_index)+":"+str(same_index_counter)
                pre_index=index
                same_index_counter=1
        # output the last group tag
        sen=sen+" "+str(pre_index)+":"+str(same_index_counter)+'\n'
        f.write(sen)

    for pat in neg_patterns:
        sen="-1"
        l=[]
        for tag in pat:
            if tag in tag_index_dict:
                l.append(tag_index_dict[tag])
            else:
                counter+=1
                tag_index_dict[tag]=counter
                l.append(counter)
        l.sort()
        pre_index=0
        same_index_counter=0
        for index in l:
            if pre_index==0:
                pre_index=index
                same_index_counter+=1
            elif pre_index==index:
                same_index_counter+=1
            elif pre_index!=index:
                sen=sen+" "+str(pre_index)+":"+str(same_index_counter)
                pre_index=index
                same_index_counter=1
        # output the last group tag
        sen=sen+" "+str(pre_index)+":"+str(same_index_counter)+'\n'
        f.write(sen)
    f.close()

    os.system("svm-train data/tmp_libsvm.dat")
    
    # turn the test data into vectors
    f=open(current_path+'/data/tagdatapos.dat','r')
    end_line_num=int(f.readline())
    f.close()

    #read tagged sentences
    f=open(current_path+'/data/tagged_subtitle.dat','r')
    tmp_str=f.readline()
    tagged_sen_db=json.loads(tmp_str)
    f.close()

    f=open(current_path+'/data/QA_subtitle.txt','r')
    pos_list=[]
    line=f.readline()
    while line!="":
        pos_list.append(int(line))
        line=f.readline()
        line=f.readline()
        line=f.readline()
    f.close()
    
    f=open(current_path+'/data/tmp_libsvm_test.dat','w')
    for i in range(0,end_line_num):
        if i+1 in pos_list:
            sen="1"
        else:
            sen="-1"
        l=[]
        for tag in tagged_sen_db[i]:
            if tag in tag_index_dict:
                l.append(tag_index_dict[tag])
        l.sort()
        pre_index=0
        same_index_counter=0
        for index in l:
            if pre_index==0:
                pre_index=index
                same_index_counter+=1
            elif pre_index==index:
                same_index_counter+=1
            elif pre_index!=index:
                sen=sen+" "+str(pre_index)+":"+str(same_index_counter)
                pre_index=index
                same_index_counter=1
        # output the last group tag
        sen=sen+" "+str(pre_index)+":"+str(same_index_counter)+'\n'
        f.write(sen)
    f.close()

    os.system('svm-predict data/tmp_libsvm_test.dat data/tmp_libsvm.dat.model data/libsvm.result')

    













