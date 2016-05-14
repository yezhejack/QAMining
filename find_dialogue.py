#coding:utf-8
import os
import json
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#to check the sequence is matched or not
#this function will check that if sen1 containes a pattern, sen2
#PS:the order of pattern won't be ignored
def ismatched(sen1,sen2):
    i=0
    for tag2 in sen2:
        flag=False
        while i<len(sen1):
            tag1=sen1[i]
            i+=1
            if tag1==tag2:
                flag=True
                break
        if flag==False:
            return False
    return True

def find(tagged_sen_file,patterns_file,output,mode):
    current_path=os.getcwd()
    sen_db_tomine=[]
    tagged_sen_tomine=[]
    patterns=[]

    #read sentences and tagged sentences
    f=open(current_path+'/data/'+tagged_sen_file,'r')
    tmp_str=f.readline()
    sen_db_tomine=json.loads(tmp_str)
    tmp_str=f.readline()
    tagged_sen_tomine=json.loads(tmp_str)
    f.close()

    #read patterns from disk
    f=open(current_path+'/data/'+patterns_file,'r')
    tmp_str=f.readline()
    patterns=json.loads(tmp_str)
    f.close()

    mine_result=[]
    result_file=open(current_path+'/data/'+output,'w')
    for i in range(len(tagged_sen_tomine)):
        for sen2 in patterns:
            sen1=tagged_sen_tomine[i]
            if ismatched(sen1,sen2)==True:
                print sen_db_tomine[i].strip()
                if i+1<len(tagged_sen_tomine):
                    result_file.write(str(i)+'\n')
                    result_file.write(sen_db_tomine[i].strip()+'\n')
                    if mode=="1":
                        result_file.write(sen_db_tomine[i+1].strip()+'\n')
                    result_file.write('***********************************************\n')
                print sen1
                print sen2
                mine_result.append(sen_db_tomine[i])
                break
    result_file.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-t","--tagged_sen_file",help="the file contains tagged sentence,default=tagged_subtitle.dat",default='tagged_subtitle.dat')
    parser.add_argument("-p","--patterns_file",help="the file contains patterns,default=patterns.dat",default="patterns.dat")
    parser.add_argument("-o","--output",help="output file,default=dialogues.txt",default="dialogues.txt")
    parser.add_argument("-m","--mode",help="it indicate this program is for [1]question or [2]dialogues,default=1",default="1")
    args=parser.parse_args()

    find(args.tagged_sen_file,args.patterns_file,args.output,args.mode)
