 #coding:utf-8
#this code provide the interface to use ltp-cloud platform from SCIR
#and provide independent script for calling ltp
import urllib2,urllib
import json
import xml.etree.ElementTree as ET
import argparse
import os
import json

#return list
#attri:a list of 'pos' 'id' 'relate' 'ne'
#mode: 'local' stands for calling the ltp_server of local host
#      'remote' stands for calling the ltp_cloud
def tagsentence(text,uri_base,attri):
    text=text.strip()
    data = {'s': text,'x': 'n','t': 'all'}
    flag=False
    while flag==False:
        try:
            request = urllib2.Request(uri_base)
            params = urllib.urlencode(data)
            response = urllib2.urlopen(request, params)
            content = response.read().strip()
            tree=ET.fromstring(content)
            flag=True
        except BaseException:
            flag=False
    seq=[]

    for word in tree.iter('word'):
        seq_word=""
        for i in range(len(attri)):
            if i==0:
                seq_word=word.attrib[attri[i]]
            else:
                seq_word=seq_word+'-'+word.attrib[attri[i]]
        seq.append(seq_word)
    return seq

def tagsentence_number(text,uri_base,attri,sen_flag):
    text=text.strip()
    data = {'s': text,'x': 'n','t': 'all'}
    flag=False
    while flag==False:
        try:
            request = urllib2.Request(uri_base)
            params = urllib.urlencode(data)
            response = urllib2.urlopen(request, params)
            content = response.read().strip()
            tree=ET.fromstring(content)
            flag=True
        except BaseException:
            flag=False
    seq=[]
    for word in tree.iter('word'):
        seq_word=sen_flag
        for i in range(len(attri)):
                seq_word=seq_word+'-'+word.attrib[attri[i]]
        seq.append(seq_word)
    return seq

# This function is used to tag a sentence and remain the keywords, add the 
# flag to each tag
# For example: <1-我-r-SBV> it means it's the first sentence of a dialogues,
# and the content of this word is '我' 
# Return list
# attri:a list of 'pos' 'id' 'relate' 'ne'
# mode: 'local' stands for calling the ltp_server of local host
#      'remote' stands for calling the ltp_cloud
# flag '1':the first sentence of a dialogue '2': the second sentence of it
def tagsentence_keywords(text,uri_base,attri,sen_flag):
    # read keywords from keywords.txt
    f=open('data/keywords.txt','r')
    keywords=[]
    line=f.readline()
    while line!="":
        line=line.strip()
        keywords.append(line.decode('utf8'))
        line=f.readline()
    f.close()

    text=text.strip()
    data = {'s': text,'x': 'n','t': 'all'}
    flag=False
    while flag==False:
        try:
            request = urllib2.Request(uri_base)
            params = urllib.urlencode(data)
            response = urllib2.urlopen(request, params)
            content = response.read().strip()
            tree=ET.fromstring(content)
            flag=True
        except BaseException:
            flag=False
    seq=[]
    for word in tree.iter('word'):
        seq_word=sen_flag+'-'
        if word.attrib['cont'] in keywords:
            seq_word=seq_word+word.attrib['cont']+'-'
        for i in range(len(attri)):
            if i==0:
                seq_word=seq_word+word.attrib[attri[i]]
            else:
                seq_word=seq_word+'-'+word.attrib[attri[i]]
        seq.append(seq_word)
    return seq


#provide file io for tagging sentence
#the inputfile must be in the data/
#the outputfile will be in the data/
#when the tag_type==2, users have to make sure the odd number line is first sentence
# type 2 is used to tag conversations
def tagger(input,output,tags,uri_base,maxlen,tag_type):
    current_path=os.getcwd()
    sen_db=[]
    tagged_sen_db=[]
    tagged_dia_db=[]
    input_file=open(current_path+'/data/'+input,'r')
    sentence=input_file.readline().strip()
    # tag question with pos
    if tag_type==1:
        while sentence!='':
            if len(sentence)<=maxlen:
                sen_db.append(sentence)
                tagged_sen_db.append(tagsentence(sentence,uri_base,tags))
                print tagged_sen_db[-1]
            sentence=input_file.readline().strip()
        print tagged_sen_db
        output_file=open(current_path+'/data/'+output,'w')
        output_file.write(json.dumps(sen_db)+'\n')
        output_file.write(json.dumps(tagged_sen_db))
        output_file.close()

    # tag dialogues with number ,keywords and pos
    elif tag_type==2:
        sen_db.append(sentence)
        sentence=input_file.readline().strip()
        dia_db=[]
        while sentence!='':
            sen_db.append(sentence)
            tagged_dia=tagsentence_keywords(sen_db[-2],uri_base,tags,"1")
            tagged_dia=tagged_dia+tagsentence_keywords(sen_db[-1],uri_base,tags,"2")
            dia_db.append(sen_db[-2]+'\n'+sen_db[-1])
            tagged_dia_db.append(tagged_dia)
            print sen_db[-2]
            print sen_db[-1]
            print tagged_dia
            sentence=input_file.readline().strip()     
        output_file=open(current_path+'/data/'+output,'w')
        output_file.write(json.dumps(dia_db)+'\n')
        output_file.write(json.dumps(tagged_dia_db))
        output_file.close()

    # tag dialogues with number,pos
    elif tag_type==3:
        sen_db.append(sentence)
        sentence=input_file.readline().strip()
        dia_db=[]
        while sentence!='':
            sen_db.append(sentence)
            tagged_dia=tagsentence_number(sen_db[-2],uri_base,tags,"1")
            tagged_dia=tagged_dia+tagsentence_number(sen_db[-1],uri_base,tags,"2")
            dia_db.append(sen_db[-2]+'\n'+sen_db[-1])
            tagged_dia_db.append(tagged_dia)
            print sen_db[-2]
            print sen_db[-1]
            print tagged_dia
            sentence=input_file.readline().strip()        
        output_file=open(current_path+'/data/'+output,'w')
        output_file.write(json.dumps(dia_db)+'\n')
        output_file.write(json.dumps(tagged_dia_db))
        output_file.close()

    # tag dialogues pos
    elif tag_type==4:
        sen_db.append(sentence)
        sentence=input_file.readline().strip()
        dia_db=[]
        while sentence!='':
            sen_db.append(sentence)
            tagged_dia=tagsentence(sen_db[-2],uri_base,tags)
            tagged_dia=tagged_dia+tagsentence(sen_db[-1],uri_base,tags)
            dia_db.append(sen_db[-2]+'\n'+sen_db[-1])
            tagged_dia_db.append(tagged_dia)
            print sen_db[-2]
            print sen_db[-1]
            print tagged_dia
            sentence=input_file.readline().strip()        
        output_file=open(current_path+'/data/'+output,'w')
        output_file.write(json.dumps(dia_db)+'\n')
        output_file.write(json.dumps(tagged_dia_db))
        output_file.close()

    # a case contains three lines with keywords,number and pos
    elif tag_type==5: 
        dia_db=[]
        while sentence!='':
            while sentence !='' and sentence.isdigit()==False :
                sentence=input_file.readline().strip()
            if sentence=='':
                break
            tagged_dia=[]
            sentence=input_file.readline().strip()
            sen_db.append(sentence)
            tagged_dia=tagged_dia+tagsentence_keywords(sentence,uri_base,tags,"1")
            sentence=input_file.readline().strip()
            sen_db.append(sentence)
            tagged_dia=tagged_dia+tagsentence_keywords(sentence,uri_base,tags,"2")
            tagged_dia_db.append(tagged_dia)
            dia_db.append(sen_db[-2]+'\n'+sen_db[-1])
            print dia_db[-1]
            print tagged_dia_db[-1]
            sentence=input_file.readline().strip()
        output_file=open(current_path+'/data/'+output,'w')
        output_file.write(json.dumps(dia_db)+'\n')
        output_file.write(json.dumps(tagged_dia_db))
        output_file.close()
    
    # a case contains three lines with number and pos
    elif tag_type==6: 
        dia_db=[]
        while sentence!='':
            while sentence !='' and sentence.isdigit()==False :
                sentence=input_file.readline().strip()
            if sentence=='':
                break
            tagged_dia=[]
            sentence=input_file.readline().strip()
            sen_db.append(sentence)
            tagged_dia=tagged_dia+tagsentence_number(sentence,uri_base,tags,"1")
            sentence=input_file.readline().strip()
            sen_db.append(sentence)
            tagged_dia=tagged_dia+tagsentence_number(sentence,uri_base,tags,"2")
            tagged_dia_db.append(tagged_dia)
            dia_db.append(sen_db[-2]+'\n'+sen_db[-1])
            print dia_db[-1]
            print tagged_dia_db[-1]
            sentence=input_file.readline().strip()
        output_file=open(current_path+'/data/'+output,'w')
        output_file.write(json.dumps(dia_db)+'\n')
        output_file.write(json.dumps(tagged_dia_db))
        output_file.close()

    # a case contains three lines with pos
    elif tag_type==7:
        dia_db=[]
        while sentence!='':
            while sentence !='' and sentence.isdigit()==False :
                sentence=input_file.readline().strip()
            if sentence=='':
                break
            print sentence
            tagged_dia=[]
            sentence=input_file.readline().strip()
            sen_db.append(sentence)
            tagged_dia=tagged_dia+tagsentence(sentence,uri_base,tags)
            sentence=input_file.readline().strip()
            sen_db.append(sentence)
            tagged_dia=tagged_dia+tagsentence(sentence,uri_base,tags)
            tagged_dia_db.append(tagged_dia)
            dia_db.append(sen_db[-2]+'\n'+sen_db[-1])
            print dia_db[-1]
            print tagged_dia_db[-1]
            sentence=input_file.readline().strip()
        output_file=open(current_path+'/data/'+output,'w')
        output_file.write(json.dumps(dia_db)+'\n')
        output_file.write(json.dumps(tagged_dia_db))
        output_file.close()
    input_file.close()
    
def segment_sentence(text,uri_base):
    text=text.strip()
    data = {'s': text,'x': 'n','t': 'all'}
    flag=False
    while flag==False:
        try:
            request = urllib2.Request(uri_base)
            params = urllib.urlencode(data)
            response = urllib2.urlopen(request, params)
            content = response.read().strip()
            tree=ET.fromstring(content)
            flag=True
        except BaseException:
            flag=False
    seq=[]
    for word in tree.iter('word'):
        seq.append(word.attrib['cont'])
    return seq


if __name__=="__main__":
    #parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',help='the name of input file in ./data/,default=ltpprocess_input.dat',default='ltpprocess_input.dat')
    parser.add_argument('--output',help='the name of output file in ./data/,default=ltpprocess_output.dat',default='ltpprocess_output.dat')
    parser.add_argument('--tags',nargs='+',help='the tags,default=[pos,relate]',default=['pos','relate'])
    parser.add_argument('--uri_base',help='the uri of ltp server request',default="http://127.0.0.1:12345/ltp")
    parser.add_argument('--maxlen',type=int,help='the max length of sentence,default=0 means no limit',default=99999)
    parser.add_argument('--tag_type',type=int,help='the type of tag.[1]question pos. [2]dialogues pos flag keywords. [3]dialogues pos number. [4]dialogues pos. [5]format2 dialogues pos flag keywords. [6]format2 dialogues pos flag. [7]format2 dialogues pos.',default=1)
    args=parser.parse_args()

    tagger(args.input,args.output,args.tags,args.uri_base,args.maxlen,args.tag_type)
