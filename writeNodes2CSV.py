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
conn = MongoClient('183.174.228.2', 38018)
db = conn.cnnews2017
#db.authenticate("Diplomaticer", "77777")
posts = db.cnnews_index

cursor =  posts.find({},{"paragraphs.sentences.entities":1})
cnt = 0
cursor.batch_size(1000)



csize = cursor.count()
pid = sys.argv[1]


writer = csv.writer(file('b_dataallnodes'+pid+'.csv', 'wb'))
writer.writerow(['id:ID','name', ':LABEL'])

pid = int(pid)
step  = int(csize/20)
start = 0+step*pid
end = start +step
print "start:"+str(start)
print "end:"+str(end)

dict = {}
cursor.skip(start)
print "skip"
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
    print cnt
    #print articles['_id']
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


