#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.son import SON

conn = MongoClient('127.0.0.1', 27017)
db = conn.admin
db.authenticate("root", "77777")
db.inventory.insert_many([
    {"item": "journal",
     "qty": 25,
     "tags": ["blank", "red"],
     "dim_cm": [14, 21]},
    {"item": "notebook",
     "qty": 50,
     "tags": ["red", "blank"],
     "dim_cm": [14, 21]},
    {"item": "paper",
     "qty": 100,
     "tags": ["red", "blank", "plain"],
     "dim_cm": [14, 21]},
    {"item": "planner",
     "qty": 75,
     "tags": ["blank", "red"],
     "dim_cm": [22.85, 30]},
    {"item": "postcard",
     "qty": 45,
     "tags": ["blue"],
     "dim_cm": [10, 15.25]}])
cursor = db.inventory.find({"tags": ["red", "blank"]})
for i in cursor:
    print i
print "------------"

cursor = db.inventory.find({"tags": {"$all": ["red", "blank"]}})
for i in cursor:
    print i
print "------------"