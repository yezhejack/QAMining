#coding:utf-8
#! /usr/bin/env python
# this code is for checking tagged file
import json
import argparse
if __name__=="__main__":
	#parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input",help="the input file name,default=tagged_GoodQA.dat",default='tagged_GoodQA.dat')
    args=parser.parse_args()

    f=open(args.input,'r')
    line=f.readline()
    db=json.loads(line)
    line=f.readline()
    tagged_db=json.loads(line)
    f.close()

    for i in range(len(db)):
    	print '[index=%d]' % (i)
    	print db[i]
    	seq=""
    	for x in tagged_db[i]:
    		seq+="["+x+"]"
    	print seq

    print 'db length= %d' % (len(db))
    print 'tagged_db length= %d' % (len(tagged_db))
