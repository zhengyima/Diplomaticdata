from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
# create an unique index

test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="123456"
)
print test_graph.data("MATCH (a:Person) RETURN a.name LIMIT 4")



