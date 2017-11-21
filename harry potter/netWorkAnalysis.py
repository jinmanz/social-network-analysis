#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:51:15 2017

@author: zjm
"""

import codecs
from nltk.tokenize import word_tokenize
from collections import defaultdict

person_counter = defaultdict(int)  
person_per_line = []
relationships = {}


namelist = ['Harry', 'Hermione', 'Ron','Sirius','Cho','Colin','Argus','Morfin','Luna','Draco','James','Lily','Fred','George','Ginny','Molly','Oliver','Dumbledore','Voldemort','Peeves','Percy','Snape']


file_object = codecs.open('HP3.txt','r','utf-8')

for line in file_object:
    poss = word_tokenize(line)
    person_per_line.append([])
    for w in poss:
        if w not in namelist:
            continue
        person_per_line[-1].append(w)
        
        if person_counter.get(w) is None: #Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值None
       # if w not in person_counter.keys():
            relationships[w] = {}
        person_counter[w] +=1

# 统计人物关系 
print "start to process edges"
#遍历每一段，笛卡尔积形式统计人物关系
for p in person_per_line:
    for name1 in p:
        for name2 in p:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] +=1

# 输出
with codecs.open("node.csv","a+","utf-8") as f:
    f.write("Id,Label,Weight\r\n")
    for name, times in person_counter.items():
        f.write(name+","+name+","+str(times)+"\r\n")
        
with codecs.open("edge.csv","a+","utf-8") as f:
    f.write("Source,Target,Weight\r\n")
    for name, edges in relationships.items():
        for v,w in edges.items():
            #if w >3:
            f.write(name+","+ v + "," + str(w) + "\r\n")
                











#reference: http://blog.csdn.net/qq_32400847/article/details/60467433
#https://github.com/maoqyhz/TextCharactervVisualization/blob/master/TextCharactervVisualization/CharacterRelationship/relationship_view.py
#http://www.cnblogs.com/Sinte-Beuve/p/7679392.html
#https://medium.com/zareen-farooqui/harry-potter-text-analysis-4d89ffe59d5b
