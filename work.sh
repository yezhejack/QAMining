{
    python pattern_mine.py --input tagged_dialogues_positive_simple_5.dat --method PrefixSpan --ispercent --minsup 0.1044 >/dev/null 2>&1
    python classifier.py --pos_input tagged_dialogues_positive_simple_5.dat --neg_input tagged_dialogues_negative_simple_5.dat --test_input tagged_subtitle_2.dat --method 1 >>1044.txt 2>&1
}&
{
    python pattern_mine.py --input tagged_dialogues_positive_simple_5.dat --method PrefixSpan --ispercent --minsup 0.1044 >/dev/null 2>&1
    python classifier.py --pos_input tagged_dialogues_positive_simple_5.dat --neg_input tagged_dialogues_negative_simple_5.dat --test_input tagged_subtitle_2.dat --method 1 >>1044.txt 2>&1
}&
