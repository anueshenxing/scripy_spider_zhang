# encoding=utf-8
import re
import string
import jieba
from pymongo import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

client = MongoClient("localhost", 27017)
db = client.news_db
news = db.news_collection
file_name = "../storedata/yuliao.txt"
f = open(file_name, "a")
delset = string.punctuation

# s1 = u"本文为头条号作者发布，不代表今日头条立场。".encode("utf-8")
# s2 = u"你为别人拼命过吗？就像走完一条漫长的隧道。时间一直向前走，没有尽头只有路口".encode("utf-8")
# print type(s1)
a = 0
for one_news in news.find():
    # s = one_news["news_content"].encode("utf-8")
    # s = one_news["news_content"].strip(s1)
    # s = one_news["news_content"].strip(s1)
    # s = s.strip(s2)
    temp = one_news["news_content"].decode("utf-8")
    # print one_news["news_ctg"] + ": " + one_news["news_title"]
    s = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！：)《》「」，。？;；、，~@#￥%“”……&*（）]+".decode("utf8"), "".decode("utf8"),temp)
    a += 1
    # print str(a) + ":---" + s + one_news["news_title"].encode("utf-8")
    seg_list = jieba.cut(s)
    result = " ".join(seg_list)
    print result.encode("utf-8")
    f.write(result+"\n")
