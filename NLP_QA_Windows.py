#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'lbbxsxlz'

#加载Jieba
import jieba
import jieba.analyse
import jieba.posseg
jieba.initialize()

#加载HanLP
from jpype import *
startJVM(getDefaultJVMPath(), "-Djava.class.path=D:\workspace\HanLP\hanlp-1.2.8-release\hanlp-1.2.8.jar;D:\workspace\HanLP\hanlp-1.2.8-release")
HanLP = JClass('com.hankcs.hanlp.HanLP')
Suggester = JClass('com.hankcs.hanlp.suggest.Suggester')
#NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
#创建文本推荐对象
suggester = Suggester()
file = open("lbb_test.txt", "rb")
print("==========文本内容========")
for line in file:
    #print(line)
    sentence = line.decode('utf-8')
    print(sentence,end = "")
    suggester.addSentence(sentence)
file.close()
print("\n")

n = 1
while(n > 0):
    str = input("please input a sentence or input quit to exit \n")
    #str = "世界上最高的山峰是哪座山？"
    if (str == "quit"):
        break
    print(40*"=")
    #print("--------分词--------")
    #print("Jieba分词 ")
    #str_list = jieba.cut(str, cut_all = False)
    #print("/" .join(str_list))
    #print("HanLP分词 ")
    #print(HanLP.segment(str))
    print("--------分词与词性标注--------")
    print("Jieba分词与词性标注 ")
    words = jieba.posseg.cut(str)
    print("[", end = "")
    for word, flag in words:
        print("%s/%s, " % (word, flag) , end = "")
    print("]")
    print("HanLP分词与词性标注 ")
    print(HanLP.segment(str))
    #str_list = HanLP.segment(str)
    #for a in str_list:
    #    print(a)
    #print(NLPTokenizer.segment(str))
    print("--------关键词抽取--------")
    print("Jieba关键词抽取 ")
    #for x, w in jieba.analyse.textrank(str, withWeight=False):
    #    print('%s%s' % (x, w))
    tags = jieba.analyse.textrank(str, withWeight=False)
    print("[", end = "")
    print(",".join(tags), end = "")
    print("]")
    #print("tf-idf ")
    #tfidf_tags = jieba.analyse.tfidf(str, withWeight=True)
    #keyword = tfidf_tags[2]
    #print(keyword)
    print("HanLP关键词抽取 ")
    keywords = HanLP.extractKeyword(str, 3)
    print(keywords)
    key = keywords[0]
    #print(key)
    print("========根据关键字找类似的句子========")
    print(suggester.suggest(key,1))
    #n = 0
shutdownJVM()

