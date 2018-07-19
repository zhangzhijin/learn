# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: start.py
@time: 2018/7/18 15:25
@desc:
'''
import  scrapy
import scrapy.crawler
from csdnscrapy.spiders import csdnspider

process=scrapy.crawler.CrawlerProcess()
process.crawl(csdnspider.CsdnSpider)
process.start()


import  scrapy.crawler
runner=scrapy.crawler.CrawlerRunner()
runner.crawl(csdnspider.CsdnSpider)
runner.join()