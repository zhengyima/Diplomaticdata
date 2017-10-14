#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 统计每个人出现的个数，但被证明无法提高精度

from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#test_graph.delete_all()
conn = MongoClient('127.0.0.1', 27017)
db = conn.Diplomaticdata
db.authenticate("Diplomaticer", "77777")
posts = db.EventNews

cursor =  posts.find({})
cnt = 0


nodesi2n = []  #key:id value:name
nodesn2i = {}  #key:name value:id
csv_reader = csv.reader(open('CSV/dataallnodes.csv'))
for row in csv_reader:
    if cnt == 0:
        cnt+= 1
        continue
    if(cnt + 2 > 80788):
        break
    #node = [];
    #node.append(cnt-1)
    #node.append(row[0])
    nodesi2n.append(row[0])
    nodesn2i[row[0]] = cnt -1
    cnt += 1

print nodesi2n[1]
print nodesn2i["李国文"]
numofrows = cnt-1


cnt = 0
nodes_articles = [] #i=1~244349
csv_reader = csv.reader(open('CSV/datanodes-articles.csv'))
for row in csv_reader:
    nodes_articles.append(row)
    cnt+=1
    #print cnt
print "read complete"
#print nodes_articles[2][2]
print cnt
rdict = {}
numofPerson = cnt - 1 #人的个数
numofRel = 0
rs = []
keyys = []
writer = csv.writer(file('CSV/nodes_total_count.csv', 'wb'))
node_count = [0 for i in range(0, cnt-1)]
for i in range(1,cnt):
    node_count[nodesn2i[nodes_articles[i][0]]] += 1
    print i

cnt = 0
for i in node_count:
    row = [cnt,i]
    writer.writerow(row)
    cnt += 1
    print cnt
    if(cnt == numofrows):
        break

'''
writer = csv.writer(file('rs.csv', 'wb'))
writer.writerow([':START_ID','value',':END_ID',':TYPE'])
for i in rs:
    writer.writerow(i)
'''











