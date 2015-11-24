#coding:utf-8
import os
from SubPreprocess import *

path='/Users/JackYip/Workspace/QA_Mining/Subtitles/'
result=CleanSubFiles(path)
f=open('/Users/JackYip/Workspace/QA_Mining/subtitle.dat','w')
for line in result:
    f.write(line)
f.close()

