# -*- coding:utf8 -*-
import urllib2
if __name__ == '__main__':
    url_get_base = "http://api.ltp-cloud.com/analysis/?"
    api_key = 'K5x1j4b1YYLdTpeogLzD2L0jEfjk1fkx0hvypgAA'
    text = '如果一个光子打向有两个狭缝的平面'
    format = 'json'
    pattern = 'all'
    result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
    content = result.read().strip()
    print content
