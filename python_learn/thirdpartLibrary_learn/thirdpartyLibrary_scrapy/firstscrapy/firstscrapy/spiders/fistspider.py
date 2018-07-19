# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: fistspider.py
@time: 2018/7/11 11:06
@desc:
'''
import  sys,os
project_dir=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0,project_dir)

import scrapy
import firstscrapy.items
class FistScrapy(scrapy.Spider):
    name='first_scrapy'
    # def start_requests(self):
    #     urls=['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']
    #     for url in urls:
    #         yield scrapy.Request(url,callback=self.parse)

    start_urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/2/']

    def parse(self, response):
        item=firstscrapy.items.FirstscrapyItem()
        print(response.xpath)
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

