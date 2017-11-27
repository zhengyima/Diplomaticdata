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
cursor.batch_size(10000)



csize = cursor.count()
pid = sys.argv[1]


writer = csv.writer(file('b_dataallnodess'+pid+'.csv', 'wb'))
writer.writerow(['id:ID','name', ':LABEL'])

pid = int(pid)
step  = int(csize/20)
start = 0+step*pid
end = start +step
print "start:"+str(start)
print "end:"+str(end)

start1 = 17952154+(3556217/20)*pid
end1 = start1 + (3556217/20)
#end1 = start1+20000

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
cnt = 0
bcnt = 0
for articles in cursor:
    #es = []

    #sid = str(i)
    #sid = "00000000"+sid
    #cursor = posts.find({"_id":sid}, {"paragraphs.sentences.entities": 1})
    #if cursor.count() == 0:
    #   continue
    dict = {}
    if len(articles['paragraphs'])>0:
        for paragraph in articles['paragraphs']:
            if len(paragraph['sentences'])>0:
                for sentence in paragraph['sentences']:
                    if len(sentence['entities'])>0:
                        for e in sentence['entities']:
                            if(e['type'] == "Person") and (not dict.has_key(e['entity'])):
                               # writer.writerow([e['entity'], 'Person'])
                               dict[e['entity']] = 1
                               person = ''
                               location = ''
                               organizition = ''
                               for ee in sentence['entities']:
                                if ee['type'] == 'Location' and location.find(ee['entity'])==-1:
                                       location += ee['entity']+' '
                                if ee['type'] == 'Organization'and organizition.find(ee['entity'])==-1:
                                        organizition += ee['entity']+' '
                                if ee['type'] == 'Person' and ee['entity'] != e['entity'] and person.find(ee['entity'])==-1:
                                    person+=ee['entity']+' '
                               writer.writerow([bcnt, e['entity'], 'Person',cnt,person,location,organizition])
                               bcnt += 1

    cnt += 1
    #print cnt
    #print articles['_id']
  #  if(cnt>100):
        #break
    print cnt
    if cnt % 3000 == 0:
        print cnt/3000



'''
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
'''


