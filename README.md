# scripy_spider_zhang

##运行爬虫
cd news_spider
scray crawl toutiao

## 数据及注意事项
  - 抓取的新闻为utf-8格式的，并不是乱码
  - 按需要修改xpath解析方式
  - 默认参数可以抓取到13万条左右的数据，
   	- title.json(不含新闻内容)
   	- news.json(含新闻内容)，可以在setting.py中修改默认写入选项
   	- `news2db.py` 可以将json文件写入`sqlite3`数据库
  - 所有的数据配置均可以在tool/Global.py中修改
