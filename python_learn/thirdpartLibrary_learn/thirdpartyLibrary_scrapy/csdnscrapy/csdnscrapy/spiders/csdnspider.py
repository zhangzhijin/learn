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
import  re
import csdnscrapy.items
class CsdnSpider(scrapy.Spider):
    name='csdnblogspider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'csdnscrapy.pipelines.CsdnscrapyPipeline': 1,
        }
    }
    def start_requests(self):
       urls=['https://blog.csdn.net/']
       for url in urls:
           yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        item = csdnscrapy.items.CsdnItem()
        title_list=response.xpath('//ul/li/div/div/h2/a[@href]/text()').extract()
        link_list=response.xpath('//ul/li/div/div/h2/a[@href]/@href').extract()
        for i in range(0,len(link_list)):
            item['title']=title_list[i]
            item['link']=link_list[i]

            yield item

        # item['read_cnt']
        # item['content_cn']




