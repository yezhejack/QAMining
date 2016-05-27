#coding:utf-8
if __name__=="__main__":
    template="{\n    python pattern_mine.py --input tagged_dialogues_positive_simple_5.dat --output patterns_%s.dat --method PrefixSpan --ispercent --minsup 0.%s\n    python classifier.py --pos_input tagged_dialogues_positive_simple_5.dat --neg_input tagged_dialogues_negative_simple_5.dat --pat_input patterns_%s.dat --test_input tagged_subtitle_2.dat --method 1\n}&"
    f=open("work2.sh","w")
    for i in range(1,6):
        per=str(1036-2*i)
        cmd=template % (per,per,per)
        f.write(cmd+"\n")
    f.close()
