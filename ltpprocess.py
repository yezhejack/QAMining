#coding:utf-8
#this code provide the interface to use ltp-cloud platform from SCIR
import urllib2
import json
current_path='/Users/JackYip/Workspace/QA_Mining/'
#return json
def tagsentence(text,api_key):
    url_get_base = "http://api.ltp-cloud.com/analysis/?"
    text=text.strip()
    api_key=api_key.strip()
    print text
    print api_key
    format = 'json'
    pattern = 'all'
    result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
    content = result.read().strip()
    return content

if __name__=='__main__':
    key_file=open(current_path+'ltp.key','r')
    key=key_file.readline()
    key_file.close()

    input_file=open(current_path+'GoodQA.dat','r')
    sentence=input_file.readline()
    print sentence
    print key
    result=json.loads(tagsentence(sentence,key))[0][0]
    seq=[]
    for i in range(len(result)):
        s=result[i]
        seq.append(s['pos']+'-'+s['relate'])
    print result
    print seq
    input_file.close()

