### Mining Question-Answer pairs from texts and subtitles ###
the prefixspan.py is modified from https://github.com/chuanconggao/PrefixSpan-py by putting it in a module called prefixspan
#### directory and file explain ####
main.py                                               the main body of the system
prefixspan.py                                         prefixspan module
SubPreprocess.py                                      process the subtitles
GoodQA.txt                                            origin good question-answer pairs
GoodQA.dat                                            tide version of GoodQA.txt without blank line
subtitles.dat                                         the file produced from subtitles preprocess procedure
/Subtitles                                            put the srt format subtitles
