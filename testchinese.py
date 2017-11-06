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

dict = {}
dict['我'] = 'i'
print dict['我']