Title: Lean Python(Chapter 2)
Date: 2017-09-19 18:42:46
Category: Python

> Everything is Object

<!--more-->

对象类型
=======

```python
# 使用 type 查看对象类型
type(23)
```

> 类型有 : int str list class function file bool(True、False) NoneType(None) long

工厂方法
=======

```python
int(4.0)
str(4)
list(1, 2, 3, 4)
tuple(1, 2, 3, 4)
dict(one = 1, two = 2)
```

数
==

```python
12345678901234567890
1 / 7.0
x = 1E20
int(x/7.0)
```

算数操作
======

```python
2 + 3
2.0 + 3
3 - 2
3.0 - 2
3 * 2
3 * 2.0
3.0 * 2.0
3 / 2 # 除法总是产生浮点数
-6 / 2
15 % 4 # int 3
4 ** 3
-4 ** 3
4 ** -3
```

转换函数
======

```python
int(1.234)
int(-1.234)
long(1.234)
long(-1.234)
long('1234')
long('1.234')
long(float('1.234'))
float(4)
float('4.321')
```

布尔值
=====

```python
# 非零即真
bool('any text') # True
bool('') # False
bool([]) # False
```

随机数
=====

```python
import random
# 产生 [a, b] 间的 int 数
random.randint(a,b)
# 产生 [0.0 1.0] 间的浮点数
random.random()
```

序列 : 字符串、列表、元组
=====================

* 一组字符的序列
* 一组值的序列
* 一组值的序列, 和列表很相似, 但是元组内的实体不可改变

## 存取

* 可以从前遍历序列, 也可从后遍历序列

```python
# 从前
x[0]
...
x[n-1]
# 从后
x[-1]
...
x[-n]
```

## 成员关系

```python
'a' in 'track'              # True
9 in [1,2,3,4,5,6]          # False
'x' not in 'next'           # False
'red' not in ['tan','pink'] # True
```

## 连接操作 : +

```python
sequence1 + sequence2
'mr' + 'joe' + 'soap'
```

```python
# join() 函数在处理字符串和元组的连接时比较高效, 推荐使用
'-'.join(('a','b','c','d'))
```

## 元素和切片

* slice 访问格式 `[startindex:endindex]`, 包括 `startindex` 的元素, 而不包括 `endindex` 的元素
* `[:endindex]` 从 `0` 开始
* `[startindex:]` 到 `末尾` 结束

```python
mylist = ['a', 'b', 'c', 'd', 'e', 'f']
mylist[0] # 'a'
mylist[1:3] # ['b', 'c']
```

```python
mylist = [1, 2, 3, ['a', 'b', 'c'], 5]
# 使用多重索引访问嵌套的序列
mylist[3][1] # 'b'
```

## 序列内建函数

```python
mylist = [4, 5, 6, 7, 1, 2, 3]
len(mylist)
max(mylist)
min(mylist)
```

## 字符串

* 字符串不可变

```python
mystr = 'Paddington Station'
mystr=mystr.upper()
```

* 赋值, 字符串成对使用 `'` 或 `"` 来包裹. 你可以在一对中使用另一对

```python
text = 'Paul said, "Hello World!"'
print(text)
```

* 访问子串

```python
text='Paul said, "Hi"'
text[:4]
text[-4:]
text[5:9]
text[0:4] + text[12:14]
```

* 字符串比较

```python
'mcr'>'liv'
'X'>'t'
```

* 子串搜索

```python
'a' in 'the task' # True
'as' in 'the task' # True
```

* 特殊字符和转义符

```python
\0 # Null character
\t # Horizontal tab
\n # Newline character
\' # Single quote
\" # Double quote
\\ # Backslash
```

* 包裹多行 `"""`

```python
multiline="""Line1
Line 2
Line 3"""
```

* 字符串的格式化

```python
# % 操作符提供了字符串格式化功能, 结构如下
formatstring % (arguments to format)
# formatstring 包含 %标记的占位符
%c # 单字符或只有一个字符的字符串
%s # 字符串
%d # 整数
%f # 浮点数
%% # 百分号
```

```python
ntoys = 4
myname='Fred'
'%s has %d toys' % (myname,ntoys)
# 'Fred has 4 toys'
```

* 字符串函数

```python
# 字符串函数都返回一个新字符串, 因为字符串不可变
find() # 查找文本
isalpha() # 判断是否是字母
isdigit() # 判断是否是数字
join() # 连接
upper() # 转换为大写
lower() # 转换为小写
split() # 将字符串分离为 list
replace() # 替换字符
rstrip() # 移除右边的空白字符
lstrip() # 移除左边的空白字符
strip() # 移除左右两边的空白字符
```

## 列表

* 创建

```python
mylist = []
names=['Tom','Dick','Harry']
mixedlist = [1,2,3,'four'] # 混合
elist = [1,2,3,[4,5,6]] # 嵌套
names[1] # 'Dick'
elist[3][1] # 5
# 如果访问不存在的 index, 会产生一个 list index 越界错误
```

* 修改

```python
mylist = []
# append 追加
mylist.append('Tom')
mylist.append('Dick')
mylist.append('Harry')
# 改变值
mylist[1]='Bill'
# 删除
del mylist[1] # # ['Tom','Harry']
```

* 获取索引

```python
mylist=['Tom','Dick','Harry']
mylist.index('Dick') # 1
mylist.index('Henry') # 不存在, 抛出错误
```

* 序列操作和相关函数

> len、max、min、sum、sorted、reversed

## 元组

* 不可变, 这是和列表相比最大的区别

* 创建

```python
mynumbers = (1,2,3,4,5,6,7)
months=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
mixed = ('a',123,'some text',[1,2,3,'testing'])
```

* 访问

```python
mynumbers[3]
months[3:6]
mixed[2]+' '+mixed[3][3]
# 访问一个不存在的 index, 同样会抛出 index 越界的错误
```

* 序列操作和相关函数

> len、max、min、sum、sorted、reversed

## 字典

* 创建

```python
wdays={ 'M':'Monday', 'T':'Tuesday', 'W':'Wednesday', 'Th':'Thursday', 'F':'Friday', 'Sa':'Saturday', 'Su':'Sunday' }
wdays['M']
wdays['W']
wdays['Su']
newdict = {} # 空字典
```

* 修改

```python
newdict = {}
# 添加
newdict['1st'] = 'first entry'
newdict['2nd'] = 'second entry'
# 修改
newdict['1st'] = 'new value'
# 删除
del newdict['2nd']
# 长度
len(newdict)
```

* 操作, 特殊的有用操作

```python
# 判断 key 是否存在
'Sa' in wdays
# 通过 keys 创建 List
wdays.keys()
# 通过 values 创建一个可递归的 List
wdays.values()
# 查找 values, 没找到使用默认值
wdays.get('X','Not a day')
```


