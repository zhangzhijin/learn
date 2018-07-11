# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: urllib.py
@time: 2018/7/10 8:32
@desc:
'''

import urllib.request
import urllib.parse
import os
header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}
url='http://www.baidu.com'
req = urllib.request.Request(url=url,headers=header)
req.add_header("key","value")
response=urllib.request.urlopen(req)
data=response.read().decode('utf-8')

print(data)
f=open('baidu.txt','a+',encoding='utf-8')
f.write(data)
f.close;

# url='http://www.baidu.com'
# proxy_addr='11.17.171.129:8080'
# proxy=urllib.request.ProxyHandler({'http':proxy_addr})
# opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
# data=urllib.request.urlopen(url).read().decode('utf8')
# print(data)
