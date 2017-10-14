#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship

test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="db2"
)

#test_graph.delete_all()
conn = MongoClient('127.0.0.1', 27017)
db = conn.Diplomaticdata
db.authenticate("Diplomaticer", "77777")
posts = db.EventNews

cursor =  posts.find({})
cnt = 0

for articles in cursor:
    #es = []
    if len(articles['paragraphs'])>0:
        for paragraph in articles['paragraphs']:
            if len(paragraph['sentences'])>0:
                for sentence in paragraph['sentences']:
                    if len(sentence['entities'])>0:
                        for e in sentence['entities']:
                            if(e['type'] == "Person"):
                                test_graph.run("MERGE (n:Person{name:{a}})",a=e['entity'])
    cnt += 1
    print cnt
