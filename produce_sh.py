#coding:utf-8
if __name__=="__main__":
    num_groups=12
    num_tasks_of_group=4
    template="\n    python pattern_mine.py --input tagged_dialogues_positive_simple_5.dat --output patterns_%s.dat --method PrefixSpan --ispercent --minsup 0.%s\n    python classifier.py --pos_input tagged_dialogues_positive_simple_5.dat --neg_input tagged_dialogues_negative_simple_5.dat --pat_input patterns_%s.dat --test_input tagged_subtitle_2.dat --method 1\n"
    param=900
    f=open("work.sh","w")
    for i in range(0,num_groups):
        f.write("{")
        for j in range(0,num_tasks_of_group):
            per="0"+str(param)
            param+=2
            cmd=template % (per,per,per)
            f.write(cmd)
        f.write("}&\n")
    f.close()
