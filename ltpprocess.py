#coding:utf-8
#this code provide the interface to use ltp-cloud platform from SCIR
import urllib2,urllib
import json
import xml.etree.ElementTree as ET

current_path='/Users/JackYip/Workspace/QA_Mining/'
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
                print content
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

