### Mining Question-Answer pairs from texts and subtitles ###
prefixspan.py is modified from https://github.com/chuanconggao/PrefixSpan-py by putting it in a module called prefixspan

The version after `1.0.0` will not provide support of online ltp-cloud because of its lack of speed.And I will give up the prefixspan from others open source except SPMF.

#### simple version ####
this version only use simple strategy to match patterns

#### directory and file explain ####

* __auto_experiment.py__
  * test automatically
* __classifier.py__
  * using the libsvm to determine whether the dialogue
* __evaluation.py__
  * evaluate the mine result
* __extract_keywords.py__
  * get the top-k keywords in the training data
* __find_dialogue.py__
  * provide interface to find the dialogue matched a pattern
* __ltpprocess.py__
  * provide interface to call ltp-cloud
* __main.py__
  * the main body of the system
* __pattern_mine.py__
  * pattern_mine module
  * This module contains a lot of other mine modules, such as SPFM. 
* __SubPreprocess.py__
  * process the subtitles
* __tagdata.py__
  * it's helpful tool to tag the data for training or evaluation
* __xlsx\_to\_txt.py__
  * generate dialogue from the XunFei xlsx database into plain text

* _/data_ :contains the data used in the project 
	* __GoodQA_Question.dat__
	  * the questions of good question-answer pairs
	* __GoodQA_Answer.dat__
	  * the Answers of good question-answer pairs
	* __ltp.key__
	  * contains the remote ltp-cloud key
	* __/Subtitles__
	  * put the srt format subtitles
	* __subtitle.dat__
	  * the good format subtitle
	* __keywords.txt__
	  * the most useful word to detect dialogue, produced by `extract_keywords.py`
	* __patterns.dat__
	  * the default output of `pattern_mine.py`
	* __dialogues_negative.txt__
	  * the negative cases of train data
	* __dialogues_positive.txt__
	  * the positive cases of train data
	* __seg_sen_db.dat__
	  * result of segmentation of `dialogues_positive.txt` and `dialogues_negative.txt`
	  * contains two lines data: first line is positive cases and the second line is negative cases
	* __QA_subtitle.txt__
	  * the mine result of myself as the standard result
	* __tagdatapos.dat__
	  * record the tagdata procedure for `tagdata.py`
	
#### create a file named 'ltp.key' that containes key of ltp-cloud ####

#### hardcode problem ####
1. url

#### set local ltp server ####
It's recommended to use ltp comes from HIT-SCIR instead of ltp-cloud. So we need to set up a ltp server in a local network.
https://github.com/HIT-SCIR/ltp

#### main.py ####
main.py provides the whole procedure to mine dialogues.

#### faster experiment ####
Instead of running main.py, we can call the python script one by one to mine dialogue. It's a good way to take our time to adjust model and some modules. Every module provide input and output file configurations. For example, we can run the ltpprocess.py only once to tag the sentence for the same sentence data. We store the result in the disk, so we can test many ways to mine sequence patterns without extra running of ltpprocess.py.

#### a example ####
1. A plain subtitles file is needed. Every line is a sentence. It is named after 'subtitle.dat'
2. A positive example is needed. This file  is named after `GoodQA.dat` which contains the first sentences of all good Question-Answer pairs.
3. Using ltpprocess.py to tag `subtitle.dat` and `GoodQA.dat`
  ```
  python ltpprocess --input subtitle.dat  --output tagged_subtitle.dat
  python lttprocess --input GoodQA.dat    --output tagged_GoodQA.dat
  ```
  The two files, tagged_subtitle.dat and tagged_GoodQA.dat, have two lines, first line is a json string of original sentences and the second line is the tags of original sentences in same order.

4. Using pattern_mine.py to mine the sequence patterns from tagged\_GoodQA.dat
  
  ```
  python pattern_mine --minsup 30 --minlen 10 --input tagged_GoodQA.dat --output patterns.dat
  ```
5. Using find_dialogue.py to find the sentence matched with any pattern of 'patterns.dat'
  
  ```
  python find_dialogue -o dialogues_minsup30_minlen_10.txt
  ```

#### modules features ####
##### pattern_mine #####
minsup can be the absolute format or the percentage format. For example, if you want to mine the patterns have a minimal support value 20.
```
python pattern_mine.py --minsup 20
```
If you want it to be 20%.
```
python pattern_mine.py --minsup 20 --ispercent
```
The value of minisup can be float. But if there is no 'ispercent' followed, the float value will be cut into an integer value.

##### tagdata #####
It will help me to tag the data by hand and it can be recover from last place. 

#### something about data/ ####
* Answer_patterns.dat comes from tagged\_GoodQA\_Answer.dat
* .dat means the mid-step input and output
* .txt means the input and output of the whols system
* .tmp means the temporary file which will be deleted after the tasks
