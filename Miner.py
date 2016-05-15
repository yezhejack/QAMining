# coding:utf-8
# the formal miner for dialogues v0.1.0 
from SubPreprocess import *
from ltpprocess import *
from find_dialogue import *

if __name__=="__main__":
    # extract pure text from srt
    output_file=open("data/subtitle_test.txt","w")
    result=ReadSubFiles("data/produce")
    for sen in result[:-2]:
    	output_file.write(sen.strip()+'\n')
    output_file.write(result[-1].strip())
    output_file.close()

    # parse the sentences
    tagger("subtitle_test.txt","tagged_subtitle_test.dat",['pos','relate'],"http://127.0.0.1:12345/ltp",99999,1)

    # find dialogues
    find("tagged_subtitle_test.dat","patterns.dat","dialogues.txt","1")