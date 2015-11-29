### Mining Question-Answer pairs from texts and subtitles ###
the prefixspan.py is modified from https://github.com/chuanconggao/PrefixSpan-py by putting it in a module called prefixspan
#### directory and file explain ####
* main.py                                               the main body of the system
* prefixspan.py                                         prefixspan module
* SubPreprocess.py                                      process the subtitles
* GoodQA.txt                                            origin good question-answer pairs
* GoodQA.dat                                            tide version of GoodQA.txt without blank line
* subtitles.dat                                         the file produced from subtitles preprocess procedure
* /Subtitles                                            put the srt format subtitles
* ltpprocess.py                                         provide interface to call ltp-cloud
#### create a file named 'ltp.key' that containes key of ltp-cloud ####
#### hardcode problem ####
1. ltp mode
2. minsup
3. patterns minimal length
4. url
