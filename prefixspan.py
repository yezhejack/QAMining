#coding:utf-8
#! /usr/bin/env python

from collections import defaultdict
import argparse
import json
import os

#an example of db
#db= [
#    ['a','b','c','d','e'],
#    ['b','b','b','d','e'],
#    ['c','b','c','c','a'],
#    ['b','b','b','c','c'],
#]

def prefixspan(db,minsup):
    results = []

    def mine_rec(patt, mdb):
        def localOccurs(mdb):
            occurs = defaultdict(list)

            for (i, stoppos) in mdb:
                seq = db[i]
                for j in xrange(stoppos, len(seq)):
                    l = occurs[seq[j]]
                    if len(l) == 0 or l[-1][0] != i:
                        l.append((i, j + 1))

            return occurs

        for (c, newmdb) in localOccurs(mdb).items():
            newsup = len(newmdb)

            if newsup >= minsup:
                newpatt = patt + [c]

                results.append((newpatt, [i for (i, stoppos) in newmdb]))
                mine_rec(newpatt, newmdb)

    mine_rec([], [(i, 0) for i in xrange(len(db))])
    return results



def mine_patterns(input,output,minsup,minlen):
    tmp_str=''
    current_path=os.getcwd()
    f=open(current_path+'/data/'+input,'r')
    tmp_str=f.readline()
    sen_db=json.loads(tmp_str)
    tmp_str=f.readline()
    tagged_sen_db=json.loads(tmp_str)
    f.close()

    patterns=[]
    for (pat,index) in prefixspan(tagged_sen_db,minsup):
        if len(pat)>=minlen:
            patterns.append(pat)
    print 'There are '+str(len(patterns))+' have been found.'
    f=open(current_path+'/data/'+output,'w')
    f.write(json.dumps(patterns))
    f.close()

if __name__=='__main__':
    #parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",help="the input file name,default=tagged_GoodQA.dat",default='tagged_GoodQA.dat')
    parser.add_argument("--output",help="the output file name ,default=patterns.dat",default='patterns.dat')
    parser.add_argument("--minsup",type=int,help="the minimal support for mining,default=3",default=3)
    parser.add_argument("--minlen",type=int,help="the minimal length for mining patterns,default=0",default=0)
    args=parser.parse_args()

    mine_patterns(args.input,args.output,args.minsup,args.minlen)
