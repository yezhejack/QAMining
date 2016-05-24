#coding:utf-8
from openpyxl import load_workbook
from SubPreprocess import *
from ltpprocess import *
import json
# This is a temporary tool to convert XunFei Dialogues Database 
# 1500.xlsx to txt

if __name__=="__main__":
    uri_base="http://127.0.0.1:12345/ltp"
    wb=load_workbook(filename="data/1500.xlsx",read_only=True)
    sheet_name=wb.get_sheet_names()[0]
    print sheet_name
    ws=wb[sheet_name]
    index=1
    question=[]
    seg_question=[]
    ans=[]
    seg_ans=[]
    dialogues_index=1

    pos_sen_db=[]
    neg_sen_db=[]
    f=open('data/dialogues_positive.txt','w')
    fout=open('data/seg_sen_db.dat','w')
    for row in ws.rows:

        # jump over the first two lines
        if index>2:
            if row[0].value:
                # output
                if len(question)>0 and len(ans)>0:
                    print question
                    print ans
                    for i in range(len(question)):
                        for j in range(len(ans)):
                            q=question[i]
                            a=ans[j]
                            f.write(str(dialogues_index)+'\n')
                            f.write(q+'\n')
                            f.write(a+'\n')

                            pos_sen_db.append(seg_question[i])
                            pos_sen_db.append(seg_ans[j])
                            dialogues_index+=1
                            
                question=[]
                seg_questiono                ans=[]
                seg_ans=[]
            else:
                if row[1].value:
                    q=row[1].value.encode('utf8')
                    question.append(q)
                    seg_question.append(segment_sentence(q,uri_base))
                if row[2].value:
                    a=row[2].value.encode('utf8')
                    ans.append(a)
                    seg_ans.append(segment_sentence(q,uri_base))
        index+=1

    fout.write(json.dumps(pos_sen_db))
    f.close()

    sen_db=[]
    seg_sen_db=[]
    input_file=open('data/subtitle.dat','r')
    output_file=open('data/dialogues_negative.txt','w')
    line=input_file.readline()
    while line!="":
        sen_db.append(line.strip())
        seg_sen_db.append(segment_sentence(line.strip(),uri_base))
        line=input_file.readline()

    index=1
    for k in range(10,16):
        for i in range(len(sen_db)-k):
            output_file.write(str(index)+'\n')
            output_file.write(sen_db[i]+'\n')
            output_file.write(sen_db[i+k]+'\n')
            neg_sen_db.append(seg_sen_db[i])
            neg_sen_db.append(seg_sen_db[i+k])
            index+=1
    
    fout.write(json.dumps(neg_sen_db))
    output_file.close()
    input_file.close()
    fout.close()