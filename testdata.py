#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
# create an unique index

test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="123456"
)
dat =  test_graph.data("Match (n:Person{name: '习近平'})-[r:CALL]-(end:Person) where r.value > 10 return r.value,n.name,end.name "
                      "order by r.value desc limit 25")
for i in dat:
    print i



