# -*- coding: utf-8 -*-
import scrapy

'''
微博电影评论爬虫
'''
class WeibomovieSpider(scrapy.Spider):
    name = "weibomovie"
    allowed_domains = ["weibo.com"]
    start_urls = ['http://weibo.com/']

    def parse(self, response):
        pass

    def parse1(self):
        return 0