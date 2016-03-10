#coding:utf-8
import argparse
import os

def evaluate(eval_file,standard_file,tagdatapos_file):
    current_path=os.getcwd()

    t=open(current_path+'/data/'+tagdatapos_file)
    sen=t.readline()
    last_index=int(sen)
    t.close()

    s=open(current_path+'/data/'+standard_file,'r')
    standard_index_list=[]
    sen=s.readline()
    while sen!='':
        standard_index_list.append(int(sen))
        sen=s.readline()
        sen=s.readline()
        sen=s.readline()
    s.close()

    e=open(current_path+'/data/'+eval_file,'r')
    eval_index_list=[]
    sen=e.readline()
    while sen!='':
        if int(sen)>last_index:
            break
        eval_index_list.append(int(sen))
        sen=e.readline()
        sen=e.readline()
        sen=e.readline()
        sen=e.readline()
    e.close()

    #precision
    precision=0.0
    for e_index in eval_index_list:
        if e_index in standard_index_list:
            precision+=1.0
    
    if len(eval_index_list)==0:
        precision==0.0
    else:
        precision=precision/len(eval_index_list)

    #recall
    recall=0.0
    for s_index in standard_index_list:
        if s_index in eval_index_list:
            recall+=1.0

    if len(standard_index_list)==0:
        recall=0.0
    else:
        recall=recall/len(standard_index_list)

    minimal_precision=(float)(len(standard_index_list))/last_index
    print 'minimal_precision='+str(minimal_precision)
    print 'precision='+str(precision)
    print 'recall='+str(recall)

    return minimal_precision,precision,recall

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-e','--eval_file',help="the file to be evaluated,defalut=dialogues.txt ",default="dialogues.txt")
    parser.add_argument('-s','--standard_file',help='the standard file,dfault=QA_subtitle.txt',default='QA_subtitle.txt')
    parser.add_argument('-p','--tagdatapos_file',help='the position file contains last index of tagged subtitile,default=tagdatapos.dat',default='tagdatapos.dat')
    args=parser.parse_args()

    evaluate(args.eval_file,args.standard_file,args.tagdatapos_file)
