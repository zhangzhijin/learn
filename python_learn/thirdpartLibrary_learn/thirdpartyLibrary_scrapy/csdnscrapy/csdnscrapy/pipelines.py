# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import json
class CsdnscrapyPipeline(object):
    def __init__(self):
        self.file = open('csdnblog.json', 'w',encoding='utf-8')

    def open_spider(self, spider):
        pass;
    def process_item(self, item, spider):
        json_str=json.dumps(dict(item),ensure_ascii=False)+ "\n";
        # content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print(json_str)
        self.file.write(json_str,)

        return item

    def close_spider(self, spider):
        self.file.close();
