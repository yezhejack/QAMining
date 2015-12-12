#coding:utf-8
#this program provide the quick way to tag the good QA of the subtitles
#this program will recover from the last QA index of the output_file
#output_file example
'35\n<Qsentence>\n<Asentence>\n'
import os
import sys
import argparse
reload(sys)
sys.setdefaultencoding('utf8')

if __name__=='__main__':
    current_path=os.getcwd()
    #get arguments
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input",help="the file name of subtitile. The fils should be in data/. default=subtitle.dat",default="subtitle.dat")
    parser.add_argument("-o","--output",help="The file name of output result.default=QA_subtitle.txt",default="QA_subtitle.txt")
    parser.add_argument("-n","--new",help='Create a new file',action='store_true')
    args=parser.parse_args()

    last_index=0
    if args.new==True:
        output_file=open(current_path+'/data/'+args.output,'w')
        output_file.close()
    else:
        #recover from the output
        output_file=open(current_path+'/data/'+args.output,'r')
        sentence=output_file.readline()
        while sentence!='':
            last_index=int(sentence)
            sentence=output_file.readline()
            sentence=output_file.readline()
            sentence=output_file.readline()
        output_file.close()

    input_file=open(current_path+'/data/'+args.input,'r')
    output_file=open(current_path+'/data/'+args.output,'a')

    sen_db=[]
    sentence=input_file.readline()
    while sentence!='':
        sen_db.append(sentence)
        sentence=input_file.readline()

    for i in range(last_index+1,len(sen_db)-1):
        print '*********************************************'
        print 'No.'+str(i)
        print sen_db[i].strip()
        print sen_db[i+1].strip()
        ans=raw_input('input y or n:')
        if ans=='y':
            output_file.write(str(i)+'\n'+'Q:'+sen_db[i].strip()+'\n'+'A:'+sen_db[i+1].strip()+'\n')

    input_file.close()
    output_file.close()
