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

pid = sys.argv[1]
pid = int(pid)

nodesi2n = []  #key:id value:name
nodesn2i = {}  #key:name value:id
csv_reader = csv.reader(open('nodes2.csv'))
for row in csv_reader:
    #node = [];
    #node.append(cnt-1)
    #node.append(row[0])
    nodesi2n.append(row[1])
    nodesn2i[row[1]+"^^^"+row[3]] = cnt -1
    #print row[0]
    cnt += 1


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
rdict = {}
numofPerson = cnt - 1 #人的个数
numofRel = 0
rs = []
keyys = []
writer = csv.writer(file('b_rsp'+str(pid)+'.csv', 'wb'))
for i in range(pid*(cnt-1)/30,(pid+1)*(cnt-1)/30): #第一个人到倒数第二个人
    article_id = nodes_articles[i][2]
    j = i+1
    while j <= cnt-1 and nodes_articles[j][2] == article_id :
        #rdict[nodes_articles[i][0]+"&"+nodes_articles[j][0]] = numofRel
        #keyys.append(nodes_articles[i][0]+"&"+nodes_articles[j][0]) #!
        numofRel += 1
        #print nodesn2i[nodes_articles[i][0]]
        #print nodesn2i[nodes_articles[j][0]]
        row = [nodesn2i[nodes_articles[i][0] + "^^^" + str(int(nodes_articles[i][2])-1) ],1,nodesn2i[nodes_articles[j][0] + "^^^" + str(int(nodes_articles[j][2])-1)],"CALL"]
        writer.writerow(row)
        #rs.append(row)
        j += 1
    print i
    #print cnt-1

'''
writer = csv.writer(file('rs.csv', 'wb'))
writer.writerow([':START_ID','value',':END_ID',':TYPE'])
for i in rs:
    writer.writerow(i)
'''











