# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb')

    def process_item(self, item, spider):
        # print(item['title'])
        # print(item['keywd'])
        title = item['title'][0]
        keywd = item['keywd'][0]
        sql = "insert into mytb(title,keywd) values (' " + title + " ','" + keywd + "')"
        # print(sql)
        self.conn.query(sql)
        return item

    def process_close(self, spider):
        self.conn.close()
