#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 将所有关系（包括重复的）写入csv文件，以供之后使用cpp进行处理

from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

csv_reader = csv.reader(open('nodes2.csv'))
writer = csv.writer(file('chenhong.csv', 'wb'))
chenhongs  = []
for row in csv_reader:
    if(row[1] == "陈红"):
        #writer.writerow(row)
        #persons = row[4]
        #locations = row[5]
        #organizations = row[6]
        features = row[4] + row[5] + row[6]
        #writer.writerow([row[0],row[1],row[3],features])
        chenhongs.append([row[0],row[1],row[3],features])

f_t = {}      #f_t['li']=1
t_f  = [[]]
numoftype = 0


print "get"
for item in chenhongs:
    features = item[3].split()
    if len(features) == 0:
        item.append(0)
        continue
    isold = 0
    for myfeature in features:
        if f_t.has_key(myfeature):
            isold = f_t[myfeature]
            break
    if  isold:
        for myfeature in features:
            f_t[myfeature] = isold
        item.append(isold)
        #item.append(len(features))
    else :
        numoftype += 1
        for myfeature in features:
            f_t[myfeature] = numoftype
            #print myfeature
        item.append(numoftype)
        #item.append(len(features))
for chenhong in chenhongs:
    writer.writerow(chenhong)


test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="77777"
)
data = test_graph.data("Match (n:Person{name: {str}})-[r:CALL]-(end:Person)"
                       " return r.value,end.name,end.id ", str="陈红")
cnt = 0
for dataitem in data:
    #dataitem['end.name'].decode('utf-8')
    #print dataitem['end.name'].encode('utf-8')
    #print dataitem['end.name'].encode('utf-8')

    if f_t.has_key(dataitem['end.name'].encode('utf-8')):
        #print "haskey!"
        data1 = test_graph.data("Match (n:Person{name:{str0},tid:{str1}}) return n",str0="陈红",
                                str1=f_t[dataitem['end.name'].encode('utf-8')])
        if len(data1) == 0:
            create = test_graph.run("Create (n:Person{name:{str0},tid:{str1}}) ",
                                    str0 = "陈红",str1=f_t[dataitem['end.name'].encode('utf-8')])
        createrel = test_graph.run("Match (a:Person{name:{str0},tid:{str1}}),(b:Person{name:{str2}})"
                                   "create (a)-[r:CALL{value:{val}}]->(b) return r",str0="陈红",str1=
        f_t[dataitem['end.name'].encode('utf-8')],str2=dataitem['end.name'],val=dataitem['r.value'])
    cnt += 1
    print cnt

















