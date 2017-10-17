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
'''
dat =  test_graph.data("Match (n:Person{name: '习近平'})-[r:CALL]-(end:Person) where r.value > 10 return r.value,n.name,end.name "
                      "order by r.value desc limit 25")
for i in dat:
    print i['n.name']
'''
a = '习近平'
data = test_graph.data("Match (n:Person{name: {str}})-[r:CALL]-(end:Person) where r.value > 10 return r.value, "
                       "n.name,end.name order by r.value desc limit 25", str=a)
tdata = data
cnt = 0
'''
for i in data:
    iname = i['end.name']
    # inode = test_graph.node(i['end.id'])
    ccnt = 0
    for j in data:
        jname = j['end.name']
        if iname == jname:
            continue
        # jnode = test_graph.node(j['end.id'])
        # find_r = test_graph.match_one(start_node=inode,end_node=jnode,bidirectional=True);
        find_r = test_graph.data("Match (n:Person{name: {i}})-[r:CALL]-(end:Person{name:{j}}) return r.value", i=iname
                                 , j=jname)
        if find_r:
            data.append({"r.value": find_r[0]['r.value'], "n.name": iname, "end.name": jname})
        print iname + '________' + jname
    cnt += 1
    print cnt
'''

''' 一种方法：
nodes = []
for i in range(0,len(data)):
    node = test_graph.node(data[i]['id(end)'])
    nodes.append(node)
for i in range(0,len(data)):
    iname = data[i]['end.name']
    cnt = 0
    inode = nodes[i]
    for j in range(0,len(data)):
        jname = data[j]['end.name']
        if iname == jname:
            continue
        jnode = nodes[j]
        find_r = test_graph.match_one(start_node=inode,end_node=jnode,rel_type='CALL',bidirectional=True);

        #find_r = test_graph.data("Match (n:Person{name: {i}})-[r:CALL]-(end:Person{name:{j}}) return r.value", i=iname
        #                         , j=jname)
        #if find_r:
        #    data.append({"r.value": find_r[0]['r.value'], "n.name": iname, "end.name": jname})
        #print iname + '________' + jname
    cnt += 1
    print cnt
    
'''
'''
cnt = 0
for i in range(0,len(data)):
    hisdata = test_graph.data("Match (n:Person{name: {str}})-[r:CALL]-(end:Person) where r.value > 2 return r.value, "
                           "n.name,end.name", str=data[i]['end.name'])
    print len(hisdata)
    
    for j in range(0,len(hisdata)):
        for k in range(0,len(data)):
            if hisdata[j]['end.name'] == data[i]['end.name']:
            cnt += 1
            data.append(hisdata[j])


print cnt

'''
'''打算采用的方法
hisdatas = []
for i in range(0,len(data)):
    hisdata = test_graph.data("Match (n:Person{name: {str}})-[r:CALL]-(end:Person) where r.value > 2 return r.value, "
                           "n.name,end.name", str=data[i]['end.name'])
    hisdatas.append(hisdata)

cnt = 0
for i in range(0,len(data)):
    for j in range(0,len(hisdatas)):
        for k in range(0,len(hisdatas[j])):
            if(data[i]['end.name']==hisdatas[j][k]['end.name']):
                if(hisdatas[j][k] in data):
                    continue
                else:
                    data.append({'r.value':hisdatas[j][k]['r.value'],'n.name':hisdatas[j][k]['end.name'],
                                            'end.name':hisdatas[j][k]['n.name']})
                    #cnt += 1
#print cnt
'''
'''
data = test_graph.run("Match(p1:Person{name:'习近平'}),(p2:Person{name:'桑巴'}),p=allshortestpaths((p1)-[*..10]-(p2)) return p");
nodes_total = []
rels_total = []
for datai in data:
    nodes = datai['p'].nodes()
    rels = datai['p'].relationships()
    #print rel
    #print nodes
    #print rels
    for i in range(0,len(nodes)):
        if nodes[i]['name'] not in nodes_total:
            nodes_total.append(nodes[i]['name'])
        if i<len(nodes)-1:
            rels_total.append({"start_node":nodes[i]['name'],"end_node":nodes[i]['name'],"val":rels[i]['value']})
'''
fperson = '习近平'
tperson = '桑巴'
data = test_graph.run("Match(p1:Person{name:{fp}}),(p2:Person{name:{tp}}),p=allshortestpaths((p1)-[*..10]-(p2)) "                                    "return p",fp=fperson,tp=tperson);
nodes_total = []
rels_total = []
#all_nodes_total = []
paths = []
cnt = 0
for datai in data:
    nodes = datai['p'].nodes()
    rels = datai['p'].relationships()
    # print rel
    # print nodes
    # print rels
    this_path = []
    this_path_val = 0
    this_path_values = []
    for i in range(0, len(nodes)):
        #all_nodes_total.append(nodes[i]['name'])
        if nodes[i]['name'] not in nodes_total:
            nodes_total.append(nodes[i]['name'])
        if i < len(nodes) - 1:
            rels_total.append(
                {"start_node": nodes[i]['name'], "end_node": nodes[i+1]['name'], "val": rels[i]['value']})
            this_path.append(
                {"start_node": nodes[i]['name'], "end_node": nodes[i + 1]['name'], "val": rels[i]['value']})
            this_path_val += rels[i]['value']
            this_path_values.append(rels[i]['value'])
    paths.append({'path':this_path,'val':np.sum(this_path_values)})

paths.sort(cmp=f2)




