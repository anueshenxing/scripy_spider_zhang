# encoding=utf-8

from pymongo import *

client = MongoClient("localhost", 27017)
db = client.news_db
news_2017 = db.news_collection_2017
news_2016 = db.news_collection
error_count = 0
right_count = 0

# print news.count()

for one in news_2016.find():
    try:
        news_ctg = one['news_ctg'].encode("utf-8")
        news_title = one['news_title'].encode("utf-8")
        news_content = one['news_content'].encode("utf-8")
        news_url = one['news_url'].encode("utf-8")

        if news_2017.find({"news_url": news_url}).count() < 1:
            one_news = {"news_ctg": news_ctg, "news_title": news_title,
                        "news_content": news_content, "news_url": news_url}
            news_2017.insert(one_news)

            right_count += 1
    except:
        error_count += 1

print error_count
print right_count
