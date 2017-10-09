from py2neo import Graph,Node,Relationship
test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="77777"
)
test_graph.delete_all()
test_node_1 = Node("Person",name = "test_node_1")
test_node_2 = Node("Person",name = "test_node_2")
test_graph.create(test_node_1)
test_graph.create(test_node_2)

node_1_call_node_2 = Relationship(test_node_1,'CALL',test_node_2)
node_1_call_node_2['count'] = 1
node_2_call_node_1 = Relationship(test_node_2,'CALL',test_node_1)
node_2_call_node_1['count'] = 2
test_graph.create(node_1_call_node_2)
test_graph.create(node_2_call_node_1)
node_1_call_node_2['count']+=1
test_graph.push(node_1_call_node_2)

#find_code_1 = test_graph.find_one(
#  label="Person",
#  property_key="name",
#  property_value="test_node_1"
#)
find_code_1 = test_graph.find_one('Person', 'name', 'test_node_1')
print find_code_1;
if find_code_1 == test_node_1:
    print "right"
else:
    print "not right"
