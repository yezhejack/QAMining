#coding:utf-8
import os
from SubPreprocess import *
from ltpprocess import *
from prefixspan import *
import json

if __name__=='__main__':

    #pre-process subtitles
    #path='/Users/JackYip/Workspace/QA_Mining/Subtitles/'
    #result=CleanSubFiles(path)
    #f=open('/Users/JackYip/Workspace/QA_Mining/subtitle.dat','w')
    #for line in result:
    #    f.write(line)
    #f.close()

    #tag on the good question-answer pairs
    print '***************************************'
    print 'tag on good question-answer pairs'
    sen_db=[]
    sen_db_tomine=[]
    tagged_sen=[]
    key_file=open(current_path+'ltp.key','r')
    key=key_file.readline()
    key_file.close()
    input_file=open(current_path+'GoodQA.dat','r')
    sentence=input_file.readline()
    while sentence!='':
        sen_db.append(sentence)
        tagged_sen.append(tagsentence(sentence,key,['pos','relate'],'local'))
        print tagged_sen[-1]
        sentence=input_file.readline()
    input_file.close()
    print tagged_sen

    #mine pattern from good question-answer pairs
    print '***************************************'
    print 'Begin to mine patterns'
    patterns=[]
    for (pat,index) in prefixspan(tagged_sen,5):
        if len(pat)>=3:
            patterns.append(pat)
    print patterns

    #tag on the subtitles to mine
    print '***************************************'
    print 'tag on the subtitles to mine'
    tagged_sen_tomine=[]
    key_file=open(current_path+'ltp.key','r')
    key=key_file.readline()
    key_file.close()
    input_file=open(current_path+'subtitle.dat','r')
    sentence=input_file.readline()
    while sentence!='':
        sen_db_tomine.append(sentence)
        tagged_sen_tomine.append(tagsentence(sentence,key,['pos','relate'],'local'))
        print tagged_sen_tomine[-1]
        sentence=input_file.readline()
    input_file.close()
    print tagged_sen_tomine

    mine_result=[]
    for i in range(len(tagged_sen_tomine)):
        for sen2 in patterns:
            sen1=tagged_sen_tomine[i]
            if ismatched(sen1,sen2)==True:
                print sen_db_tomine[i]
                print sen1
                print sen2
                mine_result.append(sen_db_tomine[i])
                break
