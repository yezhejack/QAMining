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



def mine_patterns(input,output,minsup,ispercent,minlen):
    tmp_str=''
    current_path=os.getcwd()
    f=open(current_path+'/data/'+input,'r')
    tmp_str=f.readline()
    sen_db=json.loads(tmp_str)
    tmp_str=f.readline()
    tagged_sen_db=json.loads(tmp_str)
    f.close()

    #get the absolute minsup
    absolute_minsup=1
    if ispercent==True:
        absolute_minsup=int(minsup*len(sen_db)/100)
    else:
        absolute_minsup=int(minsup)

    #check minimal support value
    if absolute_minsup<=0 or absolute_minsup>len(sen_db):
        print '[Error]The minsup is out of legal range!'
        return

    #begin mine    
    patterns=[]
    for (pat,index) in prefixspan(tagged_sen_db,absolute_minsup):
        if len(pat)>=minlen:
            patterns.append(pat)
    print '[Done]There are '+str(len(patterns))+' patterns have been found.'
    f=open(current_path+'/data/'+output,'w')
    f.write(json.dumps(patterns))
    f.close()

# Status: Pending
# Reason: Take too long time to run
def mine_patterns_multiple_minsup(input,output,alpha):    
    # read tagged sentences
    tmp_str=''
    current_path=os.getcwd()
    f=open(current_path+'/data/'+input,'r')
    tmp_str=f.readline()
    sen_db=json.loads(tmp_str)
    tmp_str=f.readline()
    tagged_sen_db=json.loads(tmp_str)
    f.close()

    # calculate tags frequency
    counter={}
    tag_sen_dict={} # key is tag, value is sen index list
    for i in xrange(len(tagged_sen_db)):
        tagged_sen=tagged_sen_db[i]
        for tag in tagged_sen:
            
            if tag in counter:
                counter[tag]+=1
            else:
                counter[tag]=1

            if tag in tag_sen_dict:
                tag_sen_dict[tag].append(i)
            else:
                tag_sen_dict[tag]=[]

    # test output
    print 'Tags Frequency'
    print counter
    print 'tag_sen_dict'
    print tag_sen_dict

    # seperate the tag by frequency
    tag_group={} #the map for store groups by frequency: key is frequency, value is tag
    for (key,value) in counter.iteritems():
        if value in tag_group:
            tag_group[value].append(key)
        else:
            tag_group[value]=[key]

    # test output
    print 'Tags Group'
    print tag_group

    patterns=[]
    # mine the pattern by group
    for (value,tag_list) in tag_group.iteritems():
        print str(value)+str(tag_list) 

        minsup=alpha*value
        print 'minsup='+str(minsup)
        
        # construct the group
        w_index=[]
        w=[]
        for tag in tag_list:
            # get the index of sentence about the tag
            sen_index_list=tag_sen_dict[tag]
            for index in sen_index_list:
                if index not in w_index:
                    w_index.append(index)
                    w.append(tagged_sen_db[index])
        
        print '[Finished]Construct the Group.'
        print 'There are '+str(len(w))+' sentences. '
        
        prefixspan_result=prefixspan(w,minsup)
        print 'There are '+str(len(prefixspan_result))+' patterns have been found.'

        for (pat,index) in prefixspan_result:
            # check the pat relations with w
            is_related=False
            for pat_tag in pat:
                if pat_tag in tag_list:
                    is_related=True
                    break

            if is_related==True:
                if pat not in patterns:
                    patterns.append(pat)

        print 'Until now, there are '+str(len(patterns))+' patterns have been found.'
        print '[Finished] PrefixSpan'
                    
    print '[Done]There are '+str(len(patterns))+' patterns have been found.'
    f=open(current_path+'/data/'+output,'w')
    f.write(json.dumps(patterns))
    f.close()

# Mining Frequent Maximal Sequential Patterns Using the MaxSP Algorithm
def MaxSP(input,output,minsup,minlen):
    # This function will produce a temporary file to contain the transfered sequence 
    # .eg only contains number(>=1)
    
    tmp_ifile_name='tmp_input.txt' # used for spmf input
    tmp_ofile_name='tmp_output.txt' # used for spmf output

    # Convert the data train into the SPMF format
    # read tagged sentences
    tmp_str=''
    current_path=os.getcwd()
    f=open(current_path+'/data/'+input,'r')
    tmp_str=f.readline()
    sen_db=json.loads(tmp_str)
    tmp_str=f.readline()
    tagged_sen_db=json.loads(tmp_str)
    f.close()

    num_seq_file=open(tmp_ifile_name,'w')
    tag_num_dict={}
    num_tag_list=[""]
    counter=0
    for i in xrange(len(tagged_sen_db)):
        tmp_str=""
        tagged_sen=tagged_sen_db[i]
        for tag in tagged_sen:
            if tag in tag_num_dict:
                tmp_str=tmp_str+tag_num_dict[tag]+" -1 "
            else:
                counter+=1
                tag_num_dict[tag]=str(counter)
                num_tag_list.append(tag)
                tmp_str=tmp_str+tag_num_dict[tag]+" -1 "
        tmp_str=tmp_str+"-2\n"
        num_seq_file.write(tmp_str)
        print tmp_str
    num_seq_file.close()

    # call the spmf using command-line
    print '[Start] call spmf'
    os.system('java -jar spmf.jar run MaxSP %s %s %s' %(tmp_ifile_name,tmp_ofile_name,str(minsup)))
    print '[Finish] call spmf'

    # convert the number sequence back to the tag sequence
    try:
        patterns=[]
        f=open(tmp_ofile_name,'r')
        line=f.readline()
        while line!="":
            seq=[]
            line_split=line.split(' ')
            for word in line_split:
                if word=='':
                    break
                else:
                    index=int(word)
                    if index!=-1:
                        seq.append(num_tag_list[index])
            #if seq[0].split('-')[0]=="1" and seq[-1].split('-')[0]=="2":
            #    patterns.append(seq)
            patterns.append(seq)
            line=f.readline()
        f.close()
    except:
        print '[Wrong] someting is WRONG!!!!'
        f.close()

    # write the sequence to the output
    print '[Done]There are '+str(len(patterns))+' patterns have been found.'
    f=open(current_path+'/data/'+output,'w')
    f.write(json.dumps(patterns))
    f.close()

if __name__=='__main__':
    #parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",help="the input file name,default=tagged_GoodQA.dat",default='tagged_GoodQA.dat')
    parser.add_argument("--output",help="the output file name ,default=patterns.dat",default='patterns.dat')
    parser.add_argument("--method",type=str,help="method for mining sequence pattern, prefixspan, MaxSP, multiple_prefixspan",default='prefixspan')
    parser.add_argument("--minsup",type=float,help="the minimal support for mining,default=3",default=3)
    parser.add_argument("--ispercent",help="indict the minsup value is percentage",action='store_true')
    parser.add_argument("--minlen",type=int,help="the minimal length for mining patterns,default=0",default=0)
    parser.add_argument("--alpha",type=float,help="the parameter for multipleminsup mode",default=0.1)
    args=parser.parse_args()
    
    if args.method=='prefixspan':
        mine_patterns(args.input,args.output,args.minsup,args.ispercent,args.minlen)
        exit()
    if args.method=='multiple_prefixspan':
        mine_patterns_multiple_minsup(args.input,args.output,args.alpha)
        exit()
    if args.method=='MaxSP':
        MaxSP(args.input,args.output,args.minsup,args.minlen)
        exit()