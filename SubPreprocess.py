#coding:utf-8
#Read subtitles with '.srt' . And change the format of the file and 
#leave the subtitle only with the content in a new file
#Date:2015.11.22
#By YE Zhe
import os.path


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
            result=result.encode('UTF-8')
    return result