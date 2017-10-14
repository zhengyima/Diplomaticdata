#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship

test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="123456"
)
#test_graph.delete_all()

conn = MongoClient('127.0.0.1', 27017)
db = conn.Diplomaticdata
db.authenticate("Diplomaticer", "77777")
posts = db.EventNews

cursor =  posts.find({})
cnt = 0


for articles in cursor:
    es = []
    if len(articles['paragraphs'])>0:
        for paragraph in articles['paragraphs']:
            if len(paragraph['sentences'])>0:
                for sentence in paragraph['sentences']:
                    if len(sentence['entities'])>0:
                        for e in sentence['entities']:
                            #find_node_1 = test_graph.find_one('Person', 'name', e['entity'])
                            find_node_1 = test_graph.data("MATCH (s) WHERE ID(s) = {a} RETURN s",a=cnt)
                            #print find_node_1[0]
                           # if(e.type == "Person"):
                             #   cypher.execute("MERGE (n:Person{name:{a}})",a=e['entity'])
                            #query = neo4j.CypherQuery(graph_db, "CREATE (a) RETURN a")
                            '''
                            if find_node_1 == None:
                                find_node_1 = Node("Entity", name=e['entity'])
                                test_graph.create(find_node_1)
                                if len(es)>0:
                                    for node in es:
                                        #find_r = test_graph.match_one(start_node=find_node_1,end_node=node)
                                        #if find_r
                                        rel = test_graph.match_one(start_node=find_node_1,
                                                                                 end_node=node,
                                                                                 bidirectional=True)
                                        if(rel == None):
                                            rel = Relationship(find_node_1, 'CALL', node , value=1)
                                            test_graph.create(rel)
                                        else:
                                            rel['value'] += 1
                                            test_graph.push(rel)
                                es.append(find_node_1)
                            '''
    print cnt
    cnt += 1
'''
cursor = posts.find({"paragraphs.sentences.entities.entity": "中国"})
#cursor = posts.find({})
cnt = 0
for i in cursor:
    cnt = cnt + 1
    if(cnt == 1):
        cursor1 = i.find({"paragraphs.sentences.entities.entity": "中国"})
        break
for i in cursor1:
    print i
'''
#print(cursor.count())

'''
for post in cursor:
    print(post)
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))
'''

