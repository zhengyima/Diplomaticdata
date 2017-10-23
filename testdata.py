#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
from json import dumps
# create an unique index
import numpy as np

def f2(a,b):
    return a['val']-b['val']
test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="123456"
)
a = '丁磊'
maxn = request.GET['maxnear']

data = test_graph.data("Match (n:Person{name: {str}})-[r:CALL]-(end:Person) where r.value > 1 return r.value, "
                       "n.name,end.name order by r.value desc limit " + maxn, str=a)
# tdata = []
# for i in range(0,maxn):
#    tdata[i] = data[i]

# data = tdata
'''
for i in data:
    iname = i['end.name']
    #inode = test_graph.node(i['end.id'])
    for j in data:
        jname = j['end.name']
        if iname==jname:
            continue
        #jnode = test_graph.node(j['end.id'])
        #find_r = test_graph.match_one(start_node=inode,end_node=jnode,bidirectional=True);
        find_r = test_graph.data("Match (n:Person{name: {i}})-[r:CALL]-(end:Person{name:{j}}) return r.value",i=iname
                                 ,j=jname)
        if find_r:
            data.append({"r.value":find_r[0]['r.value'],"n.name":iname,"end.name":jname})
'''
'''

for i in range(0, len(data)):
    hisdata = test_graph.data(
        "Match (n:Person{name: {str}})-[r:CALL]-(end:Person) where r.value > 10 return r.value, "
        "n.name,end.name order by r.value desc limit 25", str=data[i]['end.name'])
    for j in range(0, len(hisdata)):
        if hisdata[j]['end.name'] == data[i]['end.name']:
            data.append(hisdata[j])
'''
hisdatas = []
for i in range(0, len(data)):
    hisdata = test_graph.data(
        "Match (n:Person{name: {str}})-[r:CALL]-(end:Person) where r.value > 100 return r.value, "
        "n.name,end.name", str=data[i]['end.name'])
    hisdatas.append(hisdata)

cnt = 0
for i in range(0, len(data)):
    for j in range(0, len(hisdatas)):
        for k in range(0, len(hisdatas[j])):
            if (data[i]['end.name'] == hisdatas[j][k]['end.name']):
                if (hisdatas[j][k] in data):
                    continue
                else:
                    data.append({'r.value': hisdatas[j][k]['r.value'], 'n.name': hisdatas[j][k]['end.name'],
                                 'end.name': hisdatas[j][k]['n.name']})
                    # cnt += 1
# print cnt

