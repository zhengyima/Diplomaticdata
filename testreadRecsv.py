#!/usr/bin/env python
# -*- coding:utf-8 -*-

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
csv_reader = csv.reader(open('dataallnodes.csv'))
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


cnt = 0
nodes_articles = [] #i=1~244349
csv_reader = csv.reader(open('datanodes-articles.csv'))
for row in csv_reader:
    nodes_articles.append(row)
    cnt+=1
    #print cnt
print "read complete"
#print nodes_articles[2][2]

rdict = {}
numofPerson = cnt - 1 #人的个数
numofRel = 0
rs = []
keyys = []
for i in range(1,cnt-1): #第一个人到倒数第二个人
    article_id = nodes_articles[i][2]
    j = i+1
    while nodes_articles[j][2]==article_id and j<=cnt:
        tmp1 = tmp2 = 0
        if nodes_articles[i][0]+"&"+nodes_articles[j][0] in keyys:
            tmp1 = 1
        if nodes_articles[j][0]+"&"+nodes_articles[i][0] in keyys:
            tmp2 = 1
        if tmp1 == 0 and tmp2 == 0:
            rdict[nodes_articles[i][0]+"&"+nodes_articles[j][0]] = numofRel
            keyys.append(nodes_articles[i][0]+"&"+nodes_articles[j][0]) #!
            numofRel += 1
            row = [nodes_articles[i][0],1,nodes_articles[j][0],"CALL"]
            rs.append(row)
        elif tmp1 ==1 and tmp2 == 0:
            rs[rdict[nodes_articles[i][0]+"&"+nodes_articles[j][0]]][1] += 1
        elif tmp1 ==0 and tmp2 == 1:
            rs[rdict[nodes_articles[j][0] + "&" + nodes_articles[i][0]]][1] += 1
        else:
            print "error"
            exit(-1)
        j += 1
    print i


writer = csv.writer(file('rs.csv', 'wb'))
writer.writerow([':START_ID','value',':END_ID',':TYPE'])
for i in rs:
    writer.writerow(i)












