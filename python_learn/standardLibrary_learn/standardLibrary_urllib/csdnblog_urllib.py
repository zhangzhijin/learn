# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: csdnblog_urllib.py
@time: 2018/7/16 15:23
@desc:
'''
import urllib.request
import  re

headers=("User-Agent"," Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299")
url='https://blog.csdn.net'
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data=opener.open(url).read().decode('utf-8')
f=open("D:\\zzj\\11_programfile\\learn\\file\\csdn\\csdn.net.html","w",encoding='utf-8')
f.write(data)
f.close()
pat='<li class="clearfix"[\s\S.]*?</dl>[\s\S]*?</div>[\s\S]*?</li>'
like_title=re.compile(pat).findall(data,re.S)
listlen=len(like_title)
print(listlen)

for i in range(0,listlen):

    content=like_title[i]
    link_pat1='<h2>[\s\S.]*?<a href=".*?"'
    link1=re.compile(link_pat1).findall(content)
    link_pat='https.*?[\d]+'
    link = re.compile(link_pat).findall(link1[0])
    print(link[0])

    print('---------------------地'+str(i)+'个元素-------------')


