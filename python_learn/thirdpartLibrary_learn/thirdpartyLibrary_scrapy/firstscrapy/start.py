# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: start.py
@time: 2018/7/13 17:41
@desc:
'''
from scrapy import cmdline
cmdline.execute("scrapy crawl csdnblogspider -t csdnblogspider.txt".split())