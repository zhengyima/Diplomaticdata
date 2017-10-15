# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

from py2neo import Graph,Node,Relationship

from django.core   import serializers

import json

test_graph = Graph(
    "http://127.0.0.1:7474",
    username="neo4j",
    password="123456"
)

 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def near(request):
    return render(request,'near.html')

def find_near(request):
    a = request.GET['pname']
    data = test_graph.data("MATCH (a:Person) RETURN a LIMIT 4")
    return HttpResponse(json.dumps(data),content_type="application/json")