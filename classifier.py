#coding:utf-8

# this code is using the classifier to determine which two sentences are a dialogue
# the default postitive input is data/patterns
# the default negative input is data/Answer_patterns.dat
# this code will use libsvm https://www.csie.ntu.edu.tw/~cjlin/libsvm/

import os
import argparse
import json
from find_dialogue import *

def method_0(pos_input,neg_input):
    current_path=os.getcwd()
    # read positive input
    f=open(current_path+'/data/'+pos_input,'r')
    tmp_str=f.readline()
    pos_patterns=json.loads(tmp_str)
    f.close()
    
    # read negative input
    f=open(current_path+'/data/'+neg_input,'r')
    tmp_str=f.readline()
    neg_patterns=json.loads(tmp_str)
    f.close()

    # turn the data into vectors and output the result into tmp_libsvm.dat
    f=open(current_path+'/data/libsvm_train.tmp','w')
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

    os.system("svm-train -t 0 data/libsvm_train.tmp data/libsvm_model.tmp")
    
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
    
    f=open(current_path+'/data/libsvm_test.tmp','w')
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

    os.system('svm-predict data/libsvm_test.tmp data/libsvm_model.tmp data/libsvm_result.txt')


def method_1(pos_input,neg_input,pat_input,test_input):
    current_path=os.getcwd()
    # read positive input
    f=open(current_path+'/data/'+pos_input,'r')
    tmp_str=f.readline()
    tmp_str=f.readline()
    pos_dials=json.loads(tmp_str)
    print pos_dials[0]
    f.close()
    
    # read negative input
    f=open(current_path+'/data/'+neg_input,'r')
    tmp_str=f.readline()
    tmp_str=f.readline()
    neg_dials=json.loads(tmp_str)
    print neg_dials[0]
    f.close()

    #read patterns from disk
    f=open(current_path+'/data/'+pat_input,'r')
    tmp_str=f.readline()
    patterns=json.loads(tmp_str)
    f.close()

    f=open(current_path+'/data/libsvm_train.tmp','w')
    for dial in pos_dials:
        sen="1"
        for i in range(1,len(patterns)+1):
            if ismatched(dial,patterns[i-1])==True:
                sen=sen+" "+str(i)+":1";
        sen=sen+'\n'
        f.write(sen)
    
    for dial in pos_dials:
        sen="-1"
        for i in range(1,len(patterns)+1):
            if ismatched(dial,patterns[i-1])==True:
                sen=sen+" "+str(i)+":1";
        sen=sen+'\n'
        f.write(sen)
    f.close()

    # construct test file
    # turn the test data into vectors
    f=open(current_path+'/data/tagdatapos.dat','r')
    end_line_num=int(f.readline())
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

    #sentence database and tagged dialogues database from disk
    f=open(current_path+'/data/'+test_input)
    sen_db=json.loads(f.readline())
    tagged_dial_db=json.loads(f.readline())
    f.close()

    f=open(current_path+'/data/libsvm_test.tmp','w')
    for i in range(0,end_line_num):
        if i+1 in pos_list:
            sen="1"
        else:
            sen="-1"
        
        for j in range(1,len(patterns)+1):
            if ismatched(tagged_dial_db[i],patterns[j-1])==True:
                sen=sen+" "+str(j)+":1";
        sen=sen+'\n'
        f.write(sen)
    f.close()

    os.system("svm-train -t 0 data/libsvm_train.tmp data/libsvm_model.tmp")
    os.system('svm-predict data/libsvm_test.tmp data/libsvm_model.tmp data/libsvm_result.txt')

if __name__=="__main__":
    
    #parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument('--pos_input',help='the name of input file in ./data/,default=tagged_GoodQA.dat',default='tagged_GoodQA.dat')
    parser.add_argument('--neg_input',help='the name of output file in ./data/,default=tagged_GoodQA_Answer.dat',default='tagged_GoodQA_Answer.dat')
    parser.add_argument('--pat_input',help="the name of pattern file in ./data/,default=patterns.dat",default="patterns.dat")
    parser.add_argument('--test_input',help="the name of test file in ./data/,default=tagged_dialogues_test.dat",default="tagged_dialogues_test.dat")
    parser.add_argument('--method',help='the method name of libsvm\n0-detect the question of dialogues\n1-using pattern to predict',default='0')
    args=parser.parse_args()
    
    if args.method=="0":
        method_0(args.pos_input,args.neg_input)
    elif args.method=="1":
        method_1(args.pos_input,args.neg_input,args.pat_input,args.test_input)

    













