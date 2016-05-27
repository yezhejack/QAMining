#coding:utf-8
#! /usr/bin/env python

from collections import defaultdict
import argparse
import json
import os



def mine_patterns(input,output,method,minsup,ispercent,minlen):
    # This function will produce a temporary file to contain the transfered sequence
    # .eg only contains number(>=1)
    pid=str(os.getpid())
    tmp_ifile_name='/tmp/spmf_input_%s' % (pid) # used for spmf input
    tmp_ofile_name='/tmp/spmf_output_%s' % (pid) # used for spmf output

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

    # change the absolute value of minsup into percent
    percent_minsup=float(minsup)
    absolute_minsup=0 # to eliminate the bias of this change
    if ispercent==False:
        absolute_minsup=int(minsup)
        percent_minsup=float(minsup)/float(len(tagged_sen_db))


    # call the spmf using command-line
    print '[Start] call spmf'
    os.system('java -jar spmf.jar run %s %s %s %s' %(method,tmp_ifile_name,tmp_ofile_name,str(percent_minsup)))
    print '[Finish] call spmf'

    # convert the number sequence back to the tag sequence
    try:
        patterns=[]
        f=open(tmp_ofile_name,'r')
        line=f.readline()
        while line!="":
            seq=[]
            line_split=line.split(' ')
            if (len(line_split)-2)/2>=minlen:
                for word in line_split:
                    if word=='' or word=="#SUP:":
                        break
                    else:
                        index=int(word)
                        if index!=-1:
                            seq.append(num_tag_list[index])
                #if seq[0].split('-')[0]=="1" and seq[-1].split('-')[0]=="2":
                #    patterns.append(seq)
                print len(line_split)
                print seq
                patterns.append(seq)
            line=f.readline()
        f.close()
    except BaseException as e :
        print e
        print '[Wrong] someting is WRONG!!!!'
        f.close()

    for pat in patterns:
        print pat
    print percent_minsup
    # write the sequence to the output
    print '[Done]There are '+str(len(patterns))+' patterns have been found.'
    f=open(current_path+'/data/'+output,'w')
    f.write(json.dumps(patterns))
    f.close()

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



def prefixspan_old(input,output,minsup,ispercent,minlen):
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
    for pat in patterns:
        print pat
    print '[Done]There are '+str(len(patterns))+' patterns have been found.'
    f=open(current_path+'/data/'+output,'w')
    f.write(json.dumps(patterns))
    f.close()

if __name__=='__main__':
    #parse the arguments
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",help="the input file name,default=tagged_GoodQA_Question.dat",default='tagged_GoodQA_Question.dat')
    parser.add_argument("--output",help="the output file name ,default=patterns.dat",default='patterns.dat')
    parser.add_argument("--method",type=str,help="method for mining sequence pattern, PrefixSpan, MaxSP, prefixspan_old",default='PrefixSpan')
    parser.add_argument("--minsup",help="the minimal support for mining,default=3",default="5%")
    parser.add_argument("--ispercent",help="indict the minsup value is percentage",action='store_true')
    parser.add_argument("--minlen",type=int,help="the minimal length for mining patterns,default=0",default=0)
    args=parser.parse_args()

    if args.method=='PrefixSpan':
        mine_patterns(args.input,args.output,args.method,args.minsup,args.ispercent,args.minlen)
    elif args.method=='MaxSP':
        mine_patterns(args.input,args.output,args.method,args.minsup,args.ispercent,args.minlen)
    elif args.method=='prefixspan_old':
        prefixspan_old(args.input,args.output,args.minsup,args.ispercent,args.minlen)
