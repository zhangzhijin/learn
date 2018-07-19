# encoding: utf-8
'''
@author: zzj
@license: (C) Copyright 2008-2030
@contact: zzj_work@sina.cn
@software: python
@file: myre.py
@time: 2018/7/16 11:21
@desc:
'''

import re
# a = re.findall("[^a-z]", "你好a匹配吗")   #反取，匹配出除字母外的字符
# print(a)  #以列表形式返回匹配到的字符串



# a = re.findall("你好*", "这个字符串是否你好好好好")   #需要字符串里完全符合，你好，就匹配，（规则里的*元字符）前面的一个字符可以是0或多个原本字符
# print(a)  #以列表形式返回匹配到的字符串

# a = re.findall("匹配+", "匹配规则这个字符串是否匹配规则则则则则")   #需要字符串里完全符合，匹配规则，就匹配，（规则里的+元字符）前面的一个字符可以是1个或多个原本字符
# print(a)  #以列表形式返回匹配到的字符串
#

# a = re.findall("你好?", "你今年你好好")   #需要字符串里完全符合，你好，就匹配，（规则里的?元字符）前面的一个字符可以是0个或1个原本字符
# print(a)  #以列表形式返回匹配到的字符串
# #['你', '你好']

# a = re.findall("匹配规则{3}", "匹配规这个字符串是否匹配规则则则")   #{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次
# print(a)  #以列表形式返回匹配到的字符串

# a = re.findall("[^a-z]", "你好abc你好ddd代码订单 ")   #反取，匹配出除字母外的字符
# print(a)  #以列表形式返回匹配到的字符串

pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.findall('12twothree34four')        # 查找头部，没有匹配
print(m)