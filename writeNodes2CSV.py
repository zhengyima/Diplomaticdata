#!/usr/bin/env python
# -*- coding:utf-8 -*-
# write all Person in mongodb to a csv file

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

writer = csv.writer(file('dataallnodes2.csv', 'wb'))
writer.writerow(['id:ID','name', ':LABEL'])

dict = {}
for articles in cursor:
    #es = []
    if len(articles['paragraphs'])>0:
        for paragraph in articles['paragraphs']:
            if len(paragraph['sentences'])>0:
                for sentence in paragraph['sentences']:
                    if len(sentence['entities'])>0:
                        for e in sentence['entities']:
                            if(e['type'] == "Person"):
                               # writer.writerow([e['entity'], 'Person'])
                                dict[e['entity']] = 1
    cnt += 1
  #  if(cnt>100):
        #break
    if cnt % 3000 == 0:
        print cnt/3000

cnt = 0
for i in dict:
    cnt += 1
print cnt

cnt  = 0
for i in dict:
    writer.writerow([cnt,i, 'Person'])
    cnt += 1
    if cnt % 1000 == 0:
        print cnt/1000


