#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
from json import dumps
# create an unique index
import numpy as np

def f2(a,b):
    return a['val']-b['val']
test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="123456"
)
a = "习近平"

maxn = int("5")

data = test_graph.data("Match (n:Person{name: {str}})-[r:CALL]-(end:Person) where r.value > 1 return r.value, "
                    "n.name,end.name order by r.value desc limit {maxnx}",str=a,maxnx=maxn)

print data

print int("12")
