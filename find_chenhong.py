#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 将所有关系（包括重复的）写入csv文件，以供之后使用cpp进行处理

from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

csv_reader = csv.reader(open('nodes2.csv'))
writer = csv.writer(file('chenhong.csv', 'wb'))
for row in csv_reader:
    if(row[1] == "陈红"):
        writer.writerow(row)
