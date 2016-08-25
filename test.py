#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import urllib2,urllib
import json
import base64
from lib.data import conf

github_url = "https://api.github.com/repos/moonsea/ecshop/contents/activity.php?ref=master"

# data={'status':'read','rating':3,'tag':'小说'}  # 根据api文档提供的参数，我们来获取一下阿北读过的书中，他标记了‘小说’这个标签的三星书籍，把这些参数值存在一个dict里

# data = urllib.urlencode(data) # 把参数进行编码

url = urllib2.Request(github_url)

response = urllib2.urlopen(url)

result = json.loads(response.read())

for key in result.keys():
	print key,':',result[key]

a = result['content']
print base64.b64decode(a)
