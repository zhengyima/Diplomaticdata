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

cursor =  posts.find({})
cnt = 0

for articles in cursor:
    es = []
    print cnt
    if(cnt<19646):
        cnt += 1
        continue
    if len(articles['paragraphs'])>0:
        for paragraph in articles['paragraphs']:
            if len(paragraph['sentences'])>0:
                for sentence in paragraph['sentences']:
                    if len(sentence['entities'])>0:
                        for e in sentence['entities']:
                            #print e['entity'];
                            find_node_1 = test_graph.find_one('Entity', 'name', e['entity'])
                            if find_node_1 == None:
                                find_node_1 = Node("Entity", name=e['entity'])
                                test_graph.create(find_node_1)
                                if len(es)>0:
                                    for node in es:
                                        #find_r = test_graph.match_one(start_node=find_node_1,end_node=node)
                                        #if find_r
                                        '''
                                        rel = test_graph.match_one(start_node=find_node_1,
                                                                                 end_node=node,
                                                                                 bidirectional=True)
                                        '''
                                        #if(rel == None):
                                        #print find_node_1
                                        #print node
                                        rel = test_graph.match(start_node=find_node_1, end_node=node,
                                                                     bidirectional=True)
                                        listrel = list(rel);
                                        #print len(listrel)
                                        if len(listrel) > 0:

                                            #print "******************"
                                            listrel[0]['value'] += 1
                                            #print rel[0]['value']
                                            test_graph.push(listrel[0])
                                        else:
                                            rel = Relationship(find_node_1, 'CALL', node , value=1)
                                            test_graph.create(rel)
                                es.append(find_node_1)
                            else:
                                if len(es)>0:
                                    ines = 0
                                    for node in es:
                                        if node == find_node_1:
                                            ines =1
                                            break
                                    if(ines == 1):
                                        continue
                                    for node in es:
                                        #find_r = test_graph.match_one(start_node=find_node_1,end_node=node)
                                        #if find_r
                                        '''
                                        rel = test_graph.match_one(start_node=find_node_1,
                                                                                 end_node=node,
                                                                                 bidirectional=True)
                                        '''
                                        #if(rel == None):
                                        #print find_node_1
                                        #print node
                                        rel = test_graph.match(start_node=find_node_1, end_node=node,
                                                                     bidirectional=True)
                                        listrel = list(rel);
                                        #print len(listrel)
                                        if len(listrel) > 0:

                                            #print "******************"
                                            listrel[0]['value'] += 1
                                            test_graph.push(listrel[0])
                                        else:
                                            rel = Relationship(find_node_1, 'CALL', node , value=1)
                                            test_graph.create(rel)
                                es.append(find_node_1)

    cnt += 1
    #print "--------------------------------------------------"
    #print cnt
    if(cnt % 652 == 0):
        print cnt/652
    '''
    if(cnt == 3):
        break
    '''













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

