# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FirstscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company=scrapy.Field();#
    address=scrapy.Field();
    position = scrapy.Field();
    workYear=scrapy.Field();
    education=scrapy.Field();
    tel=scrapy.Field();
    hr=scrapy.Field();
    desc = scrapy.Field()
    create_date=scrapy.Field()
