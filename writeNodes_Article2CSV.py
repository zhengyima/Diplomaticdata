#!/usr/bin/env python
# -*- coding:utf-8 -*-
# write all the person that appears in every articles with article id , if they appear not once , we will show every
# article they appear in .
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

csize = cursor.count()
pid = sys.argv[1]


writer = csv.writer(file('b_dataallarticlenodes'+pid+'.csv', 'wb'))  # or datanodes-articles
writer.writerow(['name', ':LABEL'])

pid = int(pid)
step  = int(csize/20)
start = 0+step*pid
end = start +step
print "start:"+str(start)
print "end:"+str(end)

start1 = 17952154+(3556217/20)*pid
end1 = start1 + (3556217/20)

dict = {}
#cursor.skip(start)
print "skip"
print start1
print end1
ss1 = str(start1)
ss1 = "00000000"+ss1
ss2 = str(end1)
ss2 = "00000000"+ss2

cursor = posts.find({"_id":{"$gte":ss1,"$lt":ss2}},{"paragraphs.sentences.entities": 1})
cursor.batch_size(10000)
print cursor.count()

cnt = (3556217/20)*pid
for articles in cursor:
    #print "in"
    cnt += 1
    dict = {}
    print cnt
    #es = []
    if len(articles['paragraphs'])>0:
        for paragraph in articles['paragraphs']:
            if len(paragraph['sentences'])>0:
                for sentence in paragraph['sentences']:
                    if len(sentence['entities'])>0:
                        for e in sentence['entities']:
                            if(e['type'] == "Person"):
                               # writer.writerow([e['entity'], 'Person'])
                                dict[e['entity']] = cnt;
    for j in dict:
        writer.writerow([j, 'Person',cnt])
  #  if(cnt>100):
        #break
    if cnt % 3000 == 0:
        print cnt/3000

