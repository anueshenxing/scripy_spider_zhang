# encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time


class TouTiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ["toutiao.com"]
    start_urls = [
        'http://toutiao.com/articles_news_society/p1'
    ]
    base_url = 'http://toutiao.com'
    # maxpage = 501;#允许爬的最大的页数
    maxpage = 500  # 允许爬的最大的页数
    category = ['articles_news_entertainment', 'articles_news_car']
                # 'articles_news_health', 'articles_news_food']
                # 'articles_news_tech', 'articles_news_finance',
                # 'articles_news_military', 'articles_news_travel',
                # 'articles_news_sports', 'articles_news_edu', 'articles_news_society']

    # 请求每一个分类,按页数来
    def parse(self, response):

        for ctg in self.category:

            for page in range(1, self.maxpage):
                url = self.base_url + '/' + ctg + '/p' + str(page)
                request = scrapy.Request(url, self.parseNewsHref)
                request.meta['ctg'] = ctg
                yield request

    # 解析每页新闻列表的地址

    def parseNewsHref(self, response):
        urls = response.xpath("//div[@class='info']//a/@href").extract()
        ctg = response.meta['ctg']
        for url in urls:
            news_url = self.base_url + url
            request = scrapy.Request(news_url, self.parseNews)
            request.meta['ctg'] = ctg
            yield request

        # 解析具体新闻内容

    def parseNews(self, response):
        #articles = response.xpath("//div[@id='pagelet-article']")
        item = NewsSpiderItem()
        title = response.xpath("//h1[@class='article-title']/text()").extract()[0]
        ctg = response.meta['ctg']
        # tm = response.xpath("//span[@class='time']/text()").extract()
        content = response.xpath("//div[@class='article-content']//p/text()").extract()
        print title
        # if len(title) != 0 and len(tm) != 0 and len(content) != 0:
        if len(title) != 0:
            item['title'] = title
            item['category'] = ctg
            # item['time'] = int(time.mktime(time.strptime(tm, '%Y-%m-%d %H:%M')))
            item['url'] = response.url
            cc = ''
            if len(content) != 0:
                for c in content:
                    cc = cc + c + '\n'
                item['content'] = cc
            yield item

    # def printC(self, text):
    #     for t in text:
    #         print t.encode('utf-8')
