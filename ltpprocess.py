#coding:utf-8
#this code provide the interface to use ltp-cloud platform from SCIR
import urllib2
import json
current_path='/Users/JackYip/Workspace/QA_Mining/'
#return json
def tagsentence(text,api_key):
    url_get_base = "http://api.ltp-cloud.com/analysis/?"
    text=text.strip()
    print text
    api_key=api_key.strip()
    format = 'json'
    pattern = 'all'
    result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
    content = result.read().strip()
    return content
