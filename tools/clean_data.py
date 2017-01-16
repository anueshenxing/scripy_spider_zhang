# encoding=utf-8

from pymongo import *
import json

client = MongoClient("localhost", 27017)
db = client.news_db
news = db.news_collection
file = open("../storedata/news.json", 'r')
error_count = 0
right_count = 0

# print news.count()

for json_string in file:
    parsed_json = json.loads(json_string)
    try:
        news_ctg = parsed_json['category'].encode("utf-8").split('_')[2]
        news_title = parsed_json['title'].encode("utf-8")
        news_content = parsed_json['content'].encode("utf-8")
        news_url = parsed_json['url'].encode("utf-8")

        if news.find({"news_url": news_url}).count() < 1:
            one_news = {"news_ctg": news_ctg, "news_title": news_title,
                        "news_content": news_content, "news_url": news_url}
            news.insert(one_news)
            right_count += 1
    except:
        error_count += 1

print error_count
print right_count
