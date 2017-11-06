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

#test_graph.delete_all()
conn = MongoClient('183.174.228.2', 38018)
db = conn.cnnews2017
#db.authenticate("Diplomaticer", "77777")
posts = db.cnnews_index

cursor =  posts.find({})
cnt = 0

nodesi2n = []  #key:id value:name
nodesn2i = {}  #key:name value:id
csv_reader = csv.reader(open('bn.csv'))
for row in csv_reader:
    if cnt == 0:
        cnt+= 1
        continue
    if(cnt + 2 > 505041):
        break
    #node = [];
    #node.append(cnt-1)
    #node.append(row[0])
    nodesi2n.append(row[1])
    nodesn2i[row[1]] = cnt -1
    #print row[0]
    cnt += 1

pcnt = cnt
sysnum = int(sys.argv[1])
cnt = 0
nodes_articles = [] #i=1~244349
csv_reader = csv.reader(open('bna.csv'))
for row in csv_reader:
    nodes_articles.append(row)
    cnt+=1
    #print cnt
print "read complete"
#print nodes_articles[2][2]
print cnt

#1~cnt-1
hashmap = [0 for n in range(510000)]
print "hashmap init success"
print nodes_articles[1296812][0]
print nodesn2i[nodes_articles[1296812][0]]

for i in range(1,cnt-1): #第一个人到倒数第二个人
    #if i>5380893:python writeAllRel2CSVnew2.py 2
     #   print i
    if nodesn2i[nodes_articles[i][0]]<0 or nodesn2i[nodes_articles[i][0]]>=1*(pcnt-1)/10:
        continue
    article_id = nodes_articles[i][2]
    j = i + 1
    if(not isinstance(hashmap[nodesn2i[nodes_articles[i][0]]],dict)):
        hashmap[nodesn2i[nodes_articles[i][0]]] = {}
    while j <= cnt - 1 and nodes_articles[j][2] == article_id :
        # rdict[nodes_articles[i][0]+"&"+nodes_articles[j][0]] = numofRel
        #  keyys.append(nodes_articles[i][0]+"&"+nodes_articles[j][0]) #!
        if nodesn2i[nodes_articles[i][0]]<nodesn2i[nodes_articles[j][0]]:
            j += 1
            continue
        if hashmap[nodesn2i[nodes_articles[i][0]]].has_key(nodesn2i[nodes_articles[j][0]]):
            hashmap[nodesn2i[nodes_articles[i][0]]][nodesn2i[nodes_articles[j][0]]] += 1
        else:
            hashmap[nodesn2i[nodes_articles[i][0]]][nodesn2i[nodes_articles[j][0]]] = 1

        # print nodesn2i[nodes_articles[i][0]]
        # print nodesn2i[nodes_articles[j][0]]
        # row = [nodesn2i[nodes_articles[i][0]], 1, nodesn2i[nodes_articles[j][0]], "CALL"]
        # writer.writerow(row)
        # rs.append(row)
        j += 1
    print i

writer = csv.writer(file('b_rsout2'+str(sysnum)+'.csv', 'wb'))
cnt=  0
for item in hashmap:
    if isinstance(item,dict):
        for item_item in item:
            writer.writerow([cnt,item[item_item],item_item,'CALL'])
    cnt+=1


