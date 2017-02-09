# encoding=utf-8

from pymongo import *

client = MongoClient("localhost", 27017)
db = client.news_db
news = db.news_collection

ctgs = ['society', 'edu', 'sports', 'travel', 'military', 'finance',
        'tech', 'food', 'health', 'car', 'entertainment']

for ctg in ctgs:
    count = news.find({"news_ctg": ctg}).count()
    print ctg + ":" + str(count)
