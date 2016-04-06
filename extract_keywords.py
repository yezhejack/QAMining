#coding:utf-8
from ltpprocess import *
import json

if __name__=="__main__":
    pos_sen_db=[]
    neg_sen_db=[]
    f=open('data/seg_sen_db.dat','r')
    line=f.readline()
    pos_sen_db=json.loads(line)
    line=f.readline()
    neg_sen_db=json.loads(line)

    print '[Finished] reading seg sen db'
    '''
    pos_file=open('data/dialogues_positive.txt','r')
    neg_file=open('data/dialogues_negative.txt','r')
    line=pos_file.readline()
    print line
    while line!="":
        line=pos_file.readline()
        pos_sen_db.append(segment_sentence(line,"","local"))
        line=pos_file.readline()
        pos_sen_db.append(segment_sentence(line,"","local"))
        line=pos_file.readline()
        print line
    
    line=neg_file.readline()
    print line
    while line!="":
        line=neg_file.readline()
        neg_sen_db.append(segment_sentence(line,"","local"))
        line=neg_file.readline()
        neg_sen_db.append(segment_sentence(line,"","local"))
        line=neg_file.readline()
        print line
    pos_file.close()
    neg_file.close()
    '''

    pos_word_count_dict={}
    pos_total_word=0
    for sen in pos_sen_db:
        for word in sen:
            if word in pos_word_count_dict:
                pos_word_count_dict[word]+=1
            else:
                pos_word_count_dict[word]=1
            pos_total_word+=1

    neg_word_count_dict={}
    neg_total_word=0
    for sen in neg_sen_db:
        for word in sen:
            if word in neg_word_count_dict:
                neg_word_count_dict[word]+=1
            else:
                neg_word_count_dict[word]=1
            neg_total_word+=1

    word_EI_list=[]
    for word in pos_word_count_dict:
        A=pos_word_count_dict[word]
        C=pos_total_word-A
        if word in neg_word_count_dict:
            B=neg_word_count_dict[word]
        else:
            B=0
        word_EI_list.append({'word':word,'EI':float(A)*A/((A+B)*(A+C))})

    # sort
    sorted_word_list=sorted(word_EI_list,key=lambda word:-word['EI'])
    # word_EI_list.sort(lambda a,b:b['EI']-a['EI'])
    print sorted_word_list
    f=open('data/keywords.txt','w')
    for i in range(0,200):
        print str(i)
        print sorted_word_list[i]['word']+':'+str(sorted_word_list[i]['EI'])
        f.write(sorted_word_list[i]['word'].encode('utf8')+'\n')
    f.close()