# encoding=utf-8

from pymongo import *
import json

predir = "/home/zhang/news_data_2017_02_01/"
client = MongoClient("localhost", 27017)
db = client.news_db
news = db.news_collection
file = open(predir+"news_tech_finance.json", 'r')
error_count = 0
right_count = 0

# print news.count()
s1 = u"本文为头条号作者发布，不代表今日头条立场。".encode("utf-8")
s2 = u"本文为头条号作者原创，未经授权，不得转载。".encode("utf-8")
for json_string in file:
    parsed_json = json.loads(json_string)
    try:
        news_ctg = parsed_json['category'].encode("utf-8").split('_')[2]
        news_title = parsed_json['title'].encode("utf-8")
        news_content = parsed_json['content'].encode("utf-8")
        news_url = parsed_json['url'].encode("utf-8")

        s = news_content.split(s1)[0]
        s = s.split(s2)[0]

        # print news_ctg
        # print news_title
        # print s
        # print news_url

        if news.find({"news_url": news_url}).count() < 1:
            one_news = {"news_ctg": news_ctg, "news_title": news_title,
                        "news_content": s, "news_url": news_url}
            news.insert(one_news)
            right_count += 1
    except:
        error_count += 1

print error_count
print right_count
