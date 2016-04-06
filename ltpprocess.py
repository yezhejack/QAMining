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
def tagsentence(text,api_key,attri,mode):
    if mode=='remote':
        url_get_base = "http://api.ltp-cloud.com/analysis/?"
        text=text.strip()
        print text
        api_key=api_key.strip()
        format = 'json'
        pattern = 'all'
        result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
        content = result.read().strip()
        content_json=json.loads(content)[0][0]
        seq=[]
        for sen_json in content_json:
            seq_word=[]
            for i in range(len(attri)):
                if i==0:
                    seq_word=sen_json[attri[i]]
                else:
                    seq_word=seq_word+'-'+sen_json[attri[i]]
            seq.append(seq_word)
        return seq

    if mode=='local':
        text=text.strip()
        print text
        uri_base = "http://127.0.0.1:12345/ltp"
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
            seq_word=[]
            for i in range(len(attri)):
                if i==0:
                    seq_word=word.attrib[attri[i]]
                else:
                    seq_word=seq_word+'-'+word.attrib[attri[i]]
            seq.append(seq_word)
        return seq
    return []

# This function is used to tag a sentence and remain the keywords, add the 
# flag to each tag
# For example: <1-我-r-SBV> it means it's the first sentence of a dialogues,
# and the content of this word is '我' 
# Return list
# attri:a list of 'pos' 'id' 'relate' 'ne'
# mode: 'local' stands for calling the ltp_server of local host
#      'remote' stands for calling the ltp_cloud
# flag '1':the first sentence of a dialogue '2': the second sentence of it
def tagsentence_keywords(text,api_key,attri,mode,flag):

    # read keywords from keywords.txt
    f=open('data/keywords.txt','r')
    keywords=[]
    line=f.readline()
    while line!="":
        line=line.strip()
        keywords.append(line)
        line=f.readline()
    f.close()

    if mode=='remote':
        url_get_base = "http://api.ltp-cloud.com/analysis/?"
        text=text.strip()
        print text
        api_key=api_key.strip()
        format = 'json'
        pattern = 'all'
        result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
        content = result.read().strip()
        content_json=json.loads(content)[0][0]
        seq=[]
        for sen_json in content_json:
            seq_word=flag+'-'
            if sen_json['cont'] in keywords:
                seq_word=seq_word+sen_json['cont']+'-'
            for i in range(len(attri)):
                if i==0:
                    seq_word=seq_word+sen_json[attri[i]]
                else:
                    seq_word=seq_word+'-'+sen_json[attri[i]]
            seq.append(seq_word)
        return seq

    if mode=='local':
        text=text.strip()
        print text
        uri_base = "http://127.0.0.1:12345/ltp"
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
            seq_word=flag+'-'
            if word.attrib['cont'] in keywords:
                seq_word=seq_word+word.attrib['cont']+'-'
            for i in range(len(attri)):
                if i==0:
                    seq_word=word.attrib[attri[i]]
                else:
                    seq_word=seq_word+'-'+word.attrib[attri[i]]
            seq.append(seq_word)
        return seq
    return []

#provide file io for tagging sentence
#the inputfile must be in the data/
#the outputfile will be in the data/
#when the tag_type==2, users have to make sure the odd number line is first sentence
# type 2 is used to tag conversations
def tagger(input,output,tags,mode,keypath,maxlen,tag_type):
    current_path=os.getcwd()

    key=''
    if mode=='remote':
        key_file=open(current_path+'/data/'+keypath,'r')
        key=key_file.readline()
        key_file.close()

    sen_db=[]
    tagged_sen_db=[]
    input_file=open(current_path+'/data/'+input,'r')
    sentence=input_file.readline()

    if tag_type==1:
        while sentence!='':
            if len(sentence)<=maxlen:
                sen_db.append(sentence)
                tagged_sen_db.append(tagsentence(sentence,key,tags,mode))
                print tagged_sen_db[-1]
            sentence=input_file.readline()
    
    elif tag_type==2:
        while sentence!='':
            sen_db.append(sentence)
            tagged_sen_db.append(tagsentence_keywords(sentence,key,tags,mode))
            print tagged_sen_db[-1]
            
            sentence=input_file.readline()

    input_file.close()
    print tagged_sen_db

    output_file=open(current_path+'/data/'+output,'w')
    output_file.write(json.dumps(sen_db)+'\n')
    output_file.write(json.dumps(tagged_sen_db))
    output_file.close()

def segment_sentence(text,api_key,mode):
    if mode=='remote':
        url_get_base = "http://api.ltp-cloud.com/analysis/?"
        text=text.strip()
        print text
        api_key=api_key.strip()
        format = 'json'
        pattern = 'all'
        result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
        content = result.read().strip()
        content_json=json.loads(content)[0][0]
        seq=[]
        for sen_json in content_json:
            seq.append(sen_json['cont'])
        return seq

    if mode=='local':
        text=text.strip()
        uri_base = "http://127.0.0.1:12345/ltp"
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
    return []
if __name__=="__main__":
    #parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',help='the name of input file in ./data/,default=ltpprocess_input.dat',default='ltpprocess_input.dat')
    parser.add_argument('--output',help='the name of output file in ./data/,default=ltpprocess_output.dat',default='ltpprocess_output.dat')
    parser.add_argument('--tags',nargs='+',help='the tags,default=[pos,relate]',default=['pos','relate'])
    parser.add_argument('--mode',help='the mode of ltp_server,default=local',default='local')
    parser.add_argument('--keypath',help='the key file of ltp_cloud,default=ltp.key',default='ltp.key')
    parser.add_argument('--maxlen',type=int,help='the max length of sentence,default=0 means no limit',default=99999)
    parser.add_argument('--tag_type',type=int,help='the type of tag,1:no keywords  2: with keywords and flag',default=1)
    args=parser.parse_args()

    tagger(args.input,args.output,args.tags,args.mode,args.keypath,args.maxlen,args.tag_type)
