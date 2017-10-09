#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.son import SON

conn = MongoClient('127.0.0.1', 27017)
db = conn.admin
db.authenticate("root", "77777")
'''
db.inventory.insert_many([
    {"item": "journal",
     "instock": [
         SON([("warehouse", "A"), ("qty", 5)]),
         SON([("warehouse", "C"), ("qty", 15)])]},
    {"item": "notebook",
     "instock": [
         SON([("warehouse", "C"), ("qty", 5)])]},
    {"item": "paper",
     "instock": [
         SON([("warehouse", "A"), ("qty", 60)]),
         SON([("warehouse", "B"), ("qty", 15)])]},
    {"item": "planner",
     "instock": [
         SON([("warehouse", "A"), ("qty", 40)]),
         SON([("warehouse", "B"), ("qty", 5)])]},
    {"item": "postcard",
     "instock": [
         SON([("warehouse", "B"), ("qty", 15)]),
         SON([("warehouse", "C"), ("qty", 35)])]}])
'''
cursor = db.inventory.find(
    {"instock": {"$elemMatch": {"qty": {"$gt": 10, "$lte": 20}}}})
for i in cursor:
    print i
print "-------"
cursor = db.inventory.find({"instock.qty": {"$gt": 10, "$lte": 20}})
for i in cursor:
    print i
print "-------"
cursor = db.inventory.find(
    {"instock.qty": 5, "instock.warehouse": "A"})
for i in cursor:
    print i
print "-------"
ins = db.inventory.count();
print ins
print db.inventory.instock
'''ins = db.inventory.instock
cursor = ins.find({})
for i in cursor:
    print i
'''
