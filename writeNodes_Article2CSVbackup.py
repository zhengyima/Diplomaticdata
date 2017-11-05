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


writer = csv.writer(file('b_dataallarticlenodes.csv', 'wb'))  # or datanodes-articles
writer.writerow(['name', ':LABEL'])


pid = int(pid)
step  = int(csize/20)
print step
start = 0+step*pid
end = start +step
print "start:"+str(start)
print "end:"+str(end)
cursor.batch_size(1000)
article = cursor[1000000]
print article

for articles in cursor:

    cnt += 1
    if cnt<start:
        continue
    print "in"
    dict = {}
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
    for i in dict:
        writer.writerow([i, 'Person',cnt])
  #  if(cnt>100):
        #break
    if cnt % 3000 == 0:
        print cnt/3000

