# Mining dialogues from texts and subtitles #

## Introduction ##

The version after `0.0.1` may not provide support of online ltp-cloud because of its lack of speed.And I will give up the prefixspan from others open source except SPMF.

## ChangeLog ##

* `Version 0.0.1` only use simple strategy to match patterns
* `Version 0.0.2` using machine learning methods to imporve the performance. 
* `Version 0.1.1` add multiple process method to train svm classifier

## Dependencies ##
* openpyxl
* chardet
* xml
* ltp

## Miner ##

1. put the .srt files in data/produce
2. run ltp in ```127.0.0.1:12345/ltp```
3. ```python Miner.py```
4. the result is in data/dialogues.txt

## directory and file explain ##

* __auto_experiment.py__
  * test automatically with simple startegy.
* __classifier.py__
  * using the `libsvm` to determine a sentences pair whether is a dialogue
* __evaluation.py__
  * evaluate the mine performance.
* __extract_keywords.py__
  * get the top-k keywords in the training data
* __find_dialogue.py__
  * provide interface to find the dialogue matched a pattern
* __ltpprocess.py__
  * provide interface to call ltp in local method.
* __main.py__
  * the main body of the system
* __pattern_mine.py__
  * pattern_mine module
  * This module contains a lot of other mine modules, such as SPFM. 
* __SubPreprocess.py__
  * process the subtitles
  * It has some unformal method.
* __tagdata.py__
  * it's helpful tool to tag the data for training or evaluation
* __ReadXunFei.py__
  * generate dialogue from the XunFei xlsx database into plain text

* _/data_ :contains the data used in the project the 
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
	* __tagged_dialogues_positive_simple.dat__
	  * json format
	  * first is sentence database
	  * second line is tagged dialogues database
	* __dialogues_positive_simple.txt__
	  * it's a simple version for dialogues come from 1500.xlsx
	* __dialogues_test.txt__
	  * dialuges come from subtitle for test
	  * list every two close lines as a candidate dialogues

## How to use ##
This code doesn't provide a very universial way to call every part of `QA_Mining`. This code is designed for experiments. To save the time, you can 

### Setting LTP ###

#### using cloud service of HIT-LTP ####
Create a file named 'ltp.key' that containes key of ltp-cloud. Then put is in the `./data`.

#### using local HIT-LTP server ####
It's recommended to use ltp comes from HIT-SCIR instead of ltp-cloud. So we need to set up a ltp server in a local network.

```
https://github.com/HIT-SCIR/ltp
```

Version 3.0.0 has the memory leak problem.

Start Command

```
./bin/ltp_server --threads 4
```
The default url is `127.0.0.1:12345/ltp`

### Example:simple strategy ###
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
The most accurate help documentation is in 'python xxxx.py -h'

#### Faster experiment tool ####
Instead of running main.py, we can call the python script one by one to mine dialogue. It's a good way to take our time to adjust model and some modules. Every module provide input and output file configurations. For example, we can run the ltpprocess.py only once to tag the sentence for the same sentence data. We store the result in the disk, so we can test many ways to mine sequence patterns without extra running of ltpprocess.py.

### Example:using machine learning method ###
1. Prodcue tagged file using ltpprocess. I produce a few modes to change a sentence into a sequence.
  
  ```
  python ltpprocess.py --input dialogues_positive_simple.txt --output tagged_dialogues_positive_simple_5.dat --tag_type 5
  python ltpprocess.py --input dialogues_negative_simple.txt --output tagged_dialogues_negative_simple_5.dat --tag_type 5
  python ltpprocess.py --input subtitle.dat --output tagged_subtitle_2.dat --tag_type 2
  ```
  These codes will produce three tagged files. `tagged_dialogues_positive_simple_5.dat` and `tagged_dialogues_negative_simple_5.dat` are for training. `tagged_subtitle_2.dat` is for test.

2. Mine patterns

  ```
  python pattern_mine.py --input tagged_dialogues_positive_simple_5.dat --output patterns_1044.dat --method PrefixSpan --ispercent --minsup 0.1044
  ```
3. Train classifier and test
  
  ```
  python classifier.py --pos_input tagged_dialogues_positive_simple_5.dat --neg_input tagged_dialogues_negative_simple_5.dat --pat_input patterns_1044.dat --test_input tagged_subtitle_2.dat --
    method 1
  ```
  It's very important tha the `pat_input` should be matched with the `output` of `pattern_mine.py`.

4. Using multiple process to find good parameters
  
  As we see, there are a lot of parameters to be decided. So we have to run the code many times to see which group of parameters is better.
  
  You can create a `.sh` file in root of the project. For example I want to compare many results which come from different value of minsup. So I can fork a process for a value. It's simple.

## Details ##

### main.py ###
main.py provides the whole procedure to mine dialogues.


### tagdata.py ###
It will help me to tag the data by hand and it can be recover from last place. I mainly use it to provide test data. 

parameters 

* `--input` The file name of subtitle.
* `--output` The file name of result file contained the dialogues that are mined from `--input` by hand.
* `--new` A flag to tell code whether to start a new tag task. Because this code supports continuing the last task.
* `--position`The file contains the last task status. Only 

### ltpprocess.py ###
It provides the tool to process sentence or dialogues.

It has three tag type:

1. Only keep the ltp tag

2. Keep the keywords saved in `./data/keywords.txt`. Tag a dialogues every time. When tagging the first sentence it will add `1` to every tag and when tagging the second sentence it will add `2` to every tag. BEFOR EVERY DIALOGUE IT SHOULD EXIST A NUMBER OCCPUYED A LINE.

3. It is used for tagging a subtitile file. It assume every two close lines as a dialogues. And then tag them. For example,there are 1000 lines in a subtitle, it will produce 999 dialuges.

### ReadXunFei.py ###
This module's name is weird. But its main goal is to construct positive cases and negative cases.

It doesn't provide choice for input file name. Two input files are needed. 

1. `./data/subtitle.dat`:every line is sentence in the order of time come from subtitile
2. `./data/1500.xlsx`:specific data

There are three output files:

1. `./data/dialogues_positive.txt`:every three line is a positive dialogues: `index` `first sentence``seconde sentence`
2. `./data/dialogues_negative.txt`like last term, but the cases are negative.
3. `./data/seg_sen_db.dat`.Two lines. The first line contains positive cases and the second line contains negative cases. After load, it is a list. list->list->word. It's the result of segment


### extract_keywords.py ###
It has hard code problem. You should have a file located in `./data/seg_sen_db.dat`. It contains two lines.Every line is a json format string.The first line contains positive cases and the second line contains negative cases. After load, it is a list. list->list->word. 

This module will extract top-k useful word to help classifier to identify dialogues.

### pattern_mine.py ###
It provide three ways to mine patterns.

1. prefixspan
2. multiple minsup prefixspan
3. maximial sequential pattern

### find_dialogue.py ###
This module will using the patterns found by `pattern_mine.py` to match the dialogues. It only cover the first sentence of a dialogue.

### classifier.py ###
This module uses machine learning methods to detect the dialogues.It has two methods:

1. directly input the tagged_sentence without keywords to train a svm
2. combine patterns to train a svm

### Miner.py ###
It's a dialogues miner base on simple strategy.

## usage ##

#### old usage ####
minsup can be the absolute format or the percentage format. For example, if you want to mine the patterns have a minimal support value 20.

```
python pattern_mine.py --minsup 20 --method prefixspan_old
```
If you want it to be 20%.

```
python pattern_mine.py --minsup 20 --ispercent --method prefixspan_old
```

You can replace the `prefixspan_old` with `PrefixSpan`. It will use `SPMF` and provide faster speed.

The value of minisup can be float. But if there is no 'ispercent' followed, the float value will be cut into an integer value.

#### recommended usage ####
```
python pattern_mine.py --input tagged_dialogues_positive_simple.dat --method MaxSP --minsup 0.05
```

```
python classifier.py --pos_input tagged_dialogues_positive_simple.dat --neg_input tagged_dialogues_negative.dat --method 1 --test_input tagged_dialogues_test.dat
```

The parameter of `--minsup` should be adjusted to produce a proper quantity of patterns.


### something about data/ ###
* Answer_patterns.dat comes from tagged\_GoodQA\_Answer.dat
* .dat means the mid-step input and output
* .txt means the input and output of the whols system
* .tmp means the temporary file which will be deleted after the tasks
* tagged_*.dat is output of ltpprocess.py  