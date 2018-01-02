# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mysql.items import MysqlItem


class SinacrawlSpider(CrawlSpider):
    name = 'sinaCrawl'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    # http://news.sina.com.cn/o/2018-01-01/doc-ifyqchnr8167263.shtml
    # http://news.sina.com.cn/c/nd/2018-01-01/doc-ifyqcwaq6663506.shtml
    rules = (
        Rule(LinkExtractor(allow=r'.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MysqlItem()
        i['title'] = response.xpath('/html/head/title/text()').extract()
        i['keywd'] = response.xpath('/html/head/meta[4]/@content').extract()
        return i
