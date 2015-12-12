#coding:utf-8
import os
from SubPreprocess import *
from ltpprocess import *
from prefixspan import *
import json
import argparse
current_path=''
if __name__=='__main__':
    current_path=os.getcwd()
    #arguments parser
    parser=argparse.ArgumentParser()
    parser.add_argument("-m","--mode",help="\'local\' for the local ltp_server, \'remote\' for the ltp_cloud",default='remote')
    parser.add_argument("--workingpath",help="the path of data: ltp.key GoodQA.dat subtitle.dat,default = current path",default=current_path+'/data')
    parser.add_argument("--keypath",help="the path of key file default = current_path/ltp.key",default=current_path+'/data/ltp.key')
    parser.add_argument("--goodqapath",help="the path of Good QA file, default = current_path/GoodQA.dat",default=current_path+'/data/GoodQA.dat')
    parser.add_argument("--tominepath",help="the path of file to mine, default = current_path/subtitle.dat",default=current_path+'/data/subtitle.dat')
    parser.add_argument("--minsup",type=float,help="the minimal support of the patterns, default=3",default=3)
    parser.add_argument("--ispercent",help="indict the minsup value is percentage",action='store_true')
    parser.add_argument("--minlen",type=int,help="the minimal length of any pattern, default=3",default=3)
    parser.add_argument("--outputpath",help="the path of file to store final result,default=data/dialogues.txt",default="data/dialogues.txt")
    args=parser.parse_args()

    #pre-process subtitles
    #path='/Users/JackYip/Workspace/QA_Mining/data/Subtitles/'
    #result=CleanSubFiles(path)
    #f=open('/Users/JackYip/Workspace/QA_Mining/data/subtitle.dat','w')
    #for line in result:
    #    f.write(line)
    #f.close()

    #tag on the good question-answer pairs
    print '***************************************'
    print 'tag on good question-answer pairs'
    sen_db=[]
    sen_db_tomine=[]
    tagged_sen=[]
    key=''
    if args.mode=='remote':
        key_file=open(args.keypath,'r')
        key=key_file.readline()
        key_file.close()
    input_file=open(args.goodqapath,'r')
    sentence=input_file.readline()
    while sentence!='':
        sen_db.append(sentence)
        tagged_sen.append(tagsentence(sentence,key,['pos','relate'],args.mode))
        print tagged_sen[-1]
        sentence=input_file.readline()
    input_file.close()
    print tagged_sen

    #mine pattern from good question-answer pairs
    print '***************************************'
    print 'Begin to mine patterns'
    #get the absolute minsup
    absolute_minsup=1
    if args.ispercent==True:
        absolute_minsup=int(args.minsup*len(sen_db)/100)
    else:
        absolute_minsup=int(args.minsup)

    #check minimal support value
    if absolute_minsup<=0 or absolute_minsup>len(sen_db):
        print '[Error]The minsup is out of legal range!'
        exit()

    patterns=[]
    for (pat,index) in prefixspan(tagged_sen,absolute_minsup):
        if len(pat)>=args.minlen:
            patterns.append(pat)
    print patterns

    #tag on the subtitles to mine
    print '***************************************'
    print 'tag on the subtitles to mine'
    tagged_sen_tomine=[]
    if args.mode=='remote':
        key_file=open(args.keypath,'r')
        key=key_file.readline()
        key_file.close()
    input_file=open(args.tominepath,'r')
    sentence=input_file.readline()
    while sentence!='':
        sen_db_tomine.append(sentence)
        tagged_sen_tomine.append(tagsentence(sentence,key,['pos','relate'],args.mode))
        print tagged_sen_tomine[-1]
        sentence=input_file.readline()
    input_file.close()
    print tagged_sen_tomine

    mine_result=[]
    result_file=open(args.outputpath,'w')
    for i in range(len(tagged_sen_tomine)):
        for sen2 in patterns:
            sen1=tagged_sen_tomine[i]
            if ismatched(sen1,sen2)==True:
                print sen_db_tomine[i]
                if i+1<len(tagged_sen_tomine):
                    result_file.write(sen_db_tomine[i])
                    result_file.write(sen_db_tomine[i+1])
                    result_file.write('***********************************************\n')
                print sen1
                print sen2
                mine_result.append(sen_db_tomine[i])
                break
    result_file.close()
