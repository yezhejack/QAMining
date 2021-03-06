#coding:utf-8
#Read subtitles with '.srt' . And change the format of the file and
#leave the subtitle only with the content in a new file
#Date:2015.11.22
#By YE Zhe
import os.path
import chardet

# Read all .srt files in 'p' directory and put all of it into list.
def ReadSubFiles(p):
    print p
    result=[]
    list_dirs=os.walk(p)
    srt_files_path=[]
    for root,dirs,files in list_dirs:
        for f in files:
            print f
            if os.path.splitext(f)[1]=='.srt':
                srt_files_path.append(os.path.join(root,f))

    for f in srt_files_path:
        print f
        input_f=open(f)
        code=chardet.detect(input_f.read())
        input_f.close()
        print code
        input_f=open(f)
        line=input_f.readline()
        while line!="":
            try:
                if code['encoding'].find('utf') ==-1 and code['encoding'].find('UTF')==-1:
                    line=line.decode(code['encoding'])
                if line.find('-->')!=-1:
                    line=input_f.readline().strip()
                    if code['encoding'].find('utf') ==-1 and code['encoding'].find('UTF')==-1:
                        line=line.decode(code['encoding'])
                    print line
                    if line!="":
                        result.append(line)
            except BaseException,e:
                print e
                print "There is something wrong with decode."
            line=input_f.readline()
        input_f.close()
        print f
    return result  

# It's better to use ReadSubFiles beacuse it can fit more coding format.
def CleanSubFiles(p):
    print p
    result=[]
    list_dirs=os.walk(p)
    srt_files_path=[]
    for root,dirs,files in list_dirs:
        for f in files:
            print f
            if os.path.splitext(f)[1]=='.srt':
                srt_files_path.append(os.path.join(root,f))

    for f in srt_files_path:
        print f
        input_f=open(f)
        line=input_f.readline()
        while line!='':
            line=ConvertToUTF8(line)
            if line.find('-->')!=-1:
                line=ConvertToUTF8(input_f.readline())
                print line
                if line!="":
                    result.append(line)
            line=input_f.readline()
        input_f.close()
    return result

def ConvertToUTF8(str):
    result=str
    if isinstance(str,unicode)==False:
        try:
            result=str.decode('gb2312')
        except BaseException,e:
            print 'not gb2312'
            result=str.decode('GBK')
        finally:
            try:
                result=result.encode('UTF-8')
            except BaseException,e:
                print e
                return ""
    return result

# in some cases, a srt file would put two sentence in a line
# this function is used to split it
# example
# input_file
# - Hello Genius   - Hello World
# output_file
# Hello Genius
# Hello World
def SplitSenInALine(input_path,output_path):
    input_file=open(input_path,'r')
    output_file=open(output_path,'w')
    tmp_str=input_file.readline()
    while tmp_str!='':
        if '-' in tmp_str:
            split_str=tmp_str.split('-')
            print tmp_str
            print split_str
            if len(split_str)>2:
                for i in range(1,len(split_str)):
                    output_file.write(split_str[i].strip()+'\n')
            else:
                output_file.write(tmp_str.strip()+'\n')
        else:
            output_file.write(tmp_str.strip()+'\n')
        tmp_str=input_file.readline()
    input_file.close()
    output_file.close()

# output the every dialogues of the subtitle
# for example 
# input
# A
# B
# C
# output
# 1
# A
# B
# 2
# B
# C
def SubToDialogues(input_path,output_path):
    input_file=open(input_path,'r')
    output_file=open(output_path,'w')
    counter=1
    first_str=input_file.readline()
    second_str=input_file.readline()
    while second_str!='':
        output_file.write(str(counter)+'\n')
        output_file.write(first_str.strip()+'\n')
        output_file.write(second_str.strip()+'\n')
        counter+=1
        first_str=second_str
        second_str=input_file.readline()
    input_file.close()
    output_file.close()

if __name__=="__main__":
    # test
    index=1;
    output_file=open('data/benben_dialogues.txt','w')
    for i in range(1,8):
        file_name="benben_dialogues_"+str(i)+".txt"
        f=open("data/"+file_name,'r')
        line=f.readline()
        while line!="":
            output_file.write(str(index)+'\n')
            line=f.readline().strip()
            output_file.write(line+'\n')
            line=f.readline().strip()
            output_file.write(line+'\n')
            line=f.readline()
            line=f.readline()
            index+=1
        f.close()
    output_file.close()