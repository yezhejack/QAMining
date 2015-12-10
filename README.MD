### Mining Question-Answer pairs from texts and subtitles ###
the prefixspan.py is modified from https://github.com/chuanconggao/PrefixSpan-py by putting it in a module called prefixspan

#### directory and file explain ####
* main.py                                               the main body of the system
* prefixspan.py                                         prefixspan module
* SubPreprocess.py                                      process the subtitles
* subtitles.dat                                         the file produced from subtitles preprocess procedure
* ltpprocess.py                                         provide interface to call ltp-cloud
* find_dialogue.py                                      provide interface to find the dialogue matched a pattern
* /data                                                 contains the data used in the project
    * GoodQA.dat                                        the good question-answer pairs
    * ltp.key                                           contains the remote ltp-cloud key
    * /Subtitles                                        put the srt format subtitles

#### create a file named 'ltp.key' that containes key of ltp-cloud ####

#### hardcode problem ####
1. ltp mode
2. minsup
3. patterns minimal length
4. url

#### set local ltp server ####
It's recommended to use ltp comes from HIT-SCIR instead of ltp-cloud. So we need to set up a ltp server in a local network.

#### main.py ####
main.py provides the whole procedure to mine dialogues.

#### faster experiment ####
Instead of running main.py, we can call the python script one by one to mine dialogue. It's a good way to take our time to adjust model and some modules. Every module provide input and output file configurations. For example, we can run the ltpprocess.py only once to tag the sentence for the same sentence data. We store the result in the disk, so we can test many ways to mine sequence patterns without extra running of ltpprocess.py.
