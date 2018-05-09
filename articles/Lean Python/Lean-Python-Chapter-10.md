Title: Lean Python(Chapter 10)
Date: 2017-09-23 17:46:49
Category: Python

字符串搜索
========

* find 返回字符串出现的字符位置, 如果没有找到就返回 -1

```python
txt="The quick brown fox jumps over the lazy dog"
txt.find('jump')
txt.find('z')
txt.find('green')
```

<!-- more -->

正则表达式
========

```python
# 匹配邮箱
import re

regex = '\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s]'
text = """This is some text with x@y.z embedded e-mails
that we'll use as@example.com
some lines have no email addresses
others@have.two valid email@address.com
The re module is awonderful@thing."""
print('** Search text ***\n'+text)
print('** Regex ***\n' + regex + '\n***')

utext = text.upper()

s = re.search(regex, utext)
if s:
    print('*** At least one email found "' + s.group() + '"')

m = re.findall(regex, utext)
if m:
    for match in m:
        print('Match found', match.strip())
```

## 捕获括号

```python
# 找出 html 中的 links
import urllib.request
import re

response = urllib.request.urlopen('http://leanpy.com')
data1 = str(response.read())

regex = '<a\s[^>]*href\s*=\s*\"([^\"]*)\"[^>]*>(.*?)</a>'

pm = re.compile(regex)
matches = pm.findall(data1)

for m in matches:
    ms=''.join(('Link: "',m[0],'" Text: "',m[1],'"'))
    print(ms)
```


