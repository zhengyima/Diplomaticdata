#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.son import SON
from py2neo import Graph,Node,Relationship
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

url = "http://websensor.playbigdata.com/fss3/service.svc/GetSearchResults"

querystring = {"query":"陈红 张国富","num":"5","start":"1"}

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    'upgrade-insecure-requests': "1",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'postman-token': "5549dc28-2253-f247-d5f9-1f8e87bd830f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
