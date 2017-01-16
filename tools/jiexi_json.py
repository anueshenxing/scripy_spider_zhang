# encoding=utf-8

from pymongo import *
from xml.dom.minidom import Document

client = MongoClient("localhost", 27017)
db = client.news_db
news = db.news_collection_1

doc = Document()
root = doc.createElement("root")
doc.appendChild(root)
count = 0

# file = open("../storedata/news.json", 'r')
# output = open("../storedata/news.txt", 'a')
# a = 0
# b = 0
# for json_string in file:
for one_news in news.find():
    # print json_string
    # try:
    #     parsed_json = json.loads(json_string)
    #     news_ctg = parsed_json['category'].encode("utf-8").split('_')[2]
    #     print news_ctg
    #     news_title = parsed_json['title'].encode("utf-8")
    #     print news_title
    #     news_content = parsed_json['content'].encode("utf-8")
    #     print news_content
    # except:
    #     b += 1

    # output.write(title)
    # Collection = doc.createElement("Collection")
    # root.appendChild(Collection)

    data = doc.createElement("data")
    root.appendChild(data)

    title = doc.createElement("title")
    data.appendChild(title)
    titleName = doc.createTextNode(one_news["news_title"])
    title.appendChild(titleName)

    category = doc.createElement("category")
    data.appendChild(category)
    categoryName = doc.createTextNode(one_news["news_ctg"])
    category.appendChild(categoryName)

    # subCategory = doc.createElement("subCategory")
    # data.appendChild(subCategory)
    # subCategoryName = doc.createTextNode(u"环境保护")
    # subCategory.appendChild(subCategoryName)

    content = doc.createElement("content")
    data.appendChild(content)
    detailContent = doc.createTextNode(one_news["news_content"])
    content.appendChild(detailContent)

filename = "../storedata/news.xml"
f = open(filename, "a")
f.write(doc.toprettyxml(indent="  "))
f.close()
