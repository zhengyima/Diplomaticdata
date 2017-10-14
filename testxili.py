#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship

test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="77777"
)
#test_graph.delete_all()

conn = MongoClient('127.0.0.1', 27017)
db = conn.Diplomaticdata
db.authenticate("Diplomaticer", "77777")
posts = db.EventNews

#cursor =  posts.find({});
cnt = 0
#find_node_1 = Node("Entity", name='习近平')
#find_node_2 = Node("Entity", name='李克强')
find_node_1 = test_graph.find_one('Entity', 'name', '李克')
find_node_2 = test_graph.find_one('Entity', 'name', '习近')

rel = test_graph.match_one(start_node=find_node_1,
                           end_node=find_node_2,
                           bidirectional=True)

print rel
rel['value'] += 1
test_graph.push(rel)

