# -*- coding: utf-8 -*-
import scrapy


class WeibomovieSpider(scrapy.Spider):
    name = "weibomovie"
    allowed_domains = ["weibo.com"]
    start_urls = ['http://weibo.com/']

    def parse(self, response):
        pass
