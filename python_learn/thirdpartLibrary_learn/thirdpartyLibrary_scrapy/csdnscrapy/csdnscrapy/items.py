# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class CsdnItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field();
    read_cnt=scrapy.Field();
    content_cn=scrapy.Field();
