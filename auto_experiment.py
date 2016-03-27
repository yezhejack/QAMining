#coding:utf-8
import argparse
from pattern_mine import *
import find_dialogue
import evaluation

def auto_experiment(MAX_minsup,MIN_minsup,sup_gap,MAX_minlen,MIN_minlen,len_gap):
    #open the file to store the results of the experiment
    output_file=open("data/evaluation_MAXminsup%d_MINminsup%d_supgap%d_MAXminlen%d_MINminlen%d_lengap%d.txt" %(MAX_minsup,MIN_minsup,sup_gap,MAX_minlen,MIN_minlen,len_gap),"w")
    
    sup=MIN_minsup
    while sup<=MAX_minsup:
        length=MIN_minlen
        while length<=MAX_minlen:
            mine_patterns("tagged_GoodQA.dat","patterns_minsup%d_minlen%d.dat" %(sup,length),sup,False,length)
            find_dialogue.find("tagged_subtitle.dat","patterns_minsup%d_minlen%d.dat" %(sup,length),"dialogues_minsup%d_minlen%d.txt" %(sup,length))
            (minimal_precision,precision,recall)=evaluation.evaluate("dialogues_minsup%d_minlen%d.txt" %(sup,length),"QA_subtitle.txt","tagdatapos.dat")
            output_file.write("\n")
            output_file.write("minsup==%d\n" %(sup))
            output_file.write("minlen==%d\n" %(length))
            output_file.write('minimal_precision='+str(minimal_precision)+'\n')
            output_file.write('precision='+str(precision)+'\n')
            output_file.write('recall='+str(recall)+'\n')
            length=length+len_gap
        
        sup=sup+sup_gap

    #close the file
    output_file.close()

if __name__=="__main__":
    #input parameters
    parser=argparse.ArgumentParser()
    parser.add_argument("--MAXminsup",type=int,help="the maximal <minimal support>",default=100)
    parser.add_argument("--MINminsup",type=int,help="the minimal <minimal support>",default=30)
    parser.add_argument("--supgap",type=int,help="the step from minimal <minimal support> toward maximal <minimal support>",default=10)
    parser.add_argument("--MAXminlen",type=int,help="the maximal <minimal length>",default=10)
    parser.add_argument("--MINminlen",type=int,help="the minimal <minimal length>",default=3)
    parser.add_argument("--lengap",type=int,help="the step from minimal <minimal length> toward maximal <minimal length> ",default=1)
    args=parser.parse_args()

    auto_experiment(args.MAXminsup,args.MINminsup,args.supgap,args.MAXminlen,args.MINminlen,args.lengap)
