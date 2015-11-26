#coding:utf-8
import os
from SubPreprocess import *
from ltpprocess import *
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
    tagged_sen=[]
    key_file=open(current_path+'ltp.key','r')
    key=key_file.readline()
    key_file.close()

    input_file=open(current_path+'test_GoodQA.dat','r')
    sentence=input_file.readline()
    while sentence!='':
        print sentence
        print key
        result=json.loads(tagsentence(sentence,key))[0][0]
        seq=[]
        for i in range(len(result)):
            seq.append(result[i]['pos']+'-'+result[i]['relate'])
        tagged_sen.append(seq)
        sentence=input_file.readline()
    input_file.close()
    print tagged_sen


