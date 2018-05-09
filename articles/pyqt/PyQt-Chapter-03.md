Title: PyQt(Chapter 03)
Date: 2017-09-27 10:15:21
Category: PyQt
Tags: PyQt, Python

Sequence
========

* 有序
* 通过索引定位
* 切片操作取出子 sequence
* String、Tuple(至少含有两个元素, (1) 为 int 1) 不可变(创建后, 元素不可变), List 可变
* `+` `*` `[]` 是所有 sequence 通用的操作符
* `+` 连接
* `*` 重复序列, 产生新的序列
* `[]` 取出指定的元素和子 sequence

```python
# +
[1, 1] + [1, 2] # [1, 1, 1, 2]
(1, 2) + (1, 2) # [1, 2, 1, 2]
'12' + '12' # '1212'
# *
[1, 2] * 3 # [1, 2, 1, 2, 1, 2]
(1, 2) * 3 # (1, 2, 1, 2, 1, 2)
'12' * 3 # '121212'
# []
[1, 2, 3, 4][1:3] # [2, 3]
(1, 2, 3, 4)[1:3] # (2, 3)
'12312312'[1:3] # '23'
```

字符串
=====

* `'` `"` `'''` `"""`
* 字符串以 `\0` 结束

* 不可变
* 当你对字符串执行一个操作时, 将创建一个新字符串

```python
k = 'Hello World!'
k = "Hello World!"
k = '''
Hello World!
It\' s hot today
Let\'s party '''
```

## 函数与方法的区别

* 函数是模块中的方法, 通过名字直接调用
* 方法与对象关联, 被对象调用

## 字符串常用函数和方法

```python
# 常用字符串方法和函数
str()
max()
min()
len()
sorted()
reversed()
capitalize()
lower()
upper()
swapcase()
title()
join(sequence)
ljust(width)
rjust(width)
center(width)
lstrip()
rstrip()
strip()
isalnum()
isalpha()
isdigit()
islower()
istitle()
isupper()
```

```python
s = input("Enter a string: ")
n = len(s)
print("The first character of", s, "is", s[0])
print("The entered string will appear character wise as:")
for i in range(0,n):
    print(s[i])
print("The entered string will appear character wise as:")
for i in s:
    print (i)
print("String with its characters sorted is", sorted(s))
print("String in reverse form is", "".join(reversed(s)))
```

```python
# 查找子字符串的方法
count(s, [start], [end]) #  查找 s 出现的次数
find(s, [start], [end]) # 查找 s 出现的第一个 index, 没有返回 -1
index(s, [start], [end]) # 查找 s 出现的第一个 index, 没有抛出错误
rfind(s, [start], [end]) # 查找 s 出现的最后一个 index, 没有返回 -1
rindex(s, [start], [end]) # 查找 s 出现的最后一个 index, 没有抛出错误
```

```python
# 匹配特定的字符串前缀或后缀
# suffix 可以是一个 字符串 or 字符串构成的tuple
startswith(suffix, [start], [end]) # 返回 True or False
endswith(suffix, [start], [end])
```

```python
# 切割字符串 or 替换字符串
partition(separator)
'aLb'.partition('L') # ('a', 'L', 'b')
'aLb'.partition(':') # ('aLb', '', '')
split(separator,[n]) # n 表示切分几次
splitlines(boolean)  # 通过行分隔符切割字符串
expandtabs([tabsize]) # 将 tab 展开为 空格
replace(sl, s2, [n]) # 将 s1 替换为 s2 n 次, n 没有指定, 替换所有
```

数组
===

* 一维数组
* 二维数组

```python
m1 = [ [1, 2], [3, 4], [5, 6], [7, 8] ]
m2 = [ [9, 8], [7, 6], [5, 4], [3, 2] ]
m3 = [ 2*[0] for i in range(4) ]
print("Addition of two matrices is")
for i in range(4):
    for j in range(2):
        m3[i][j] = m1[i][j] + m2[i][j]
for row in m3:
    print (row)
```

List
====

```python
months = ['January', 'February', 'March', \
          'April', 'May', 'June', 'July', \
          'August', 'September', 'October', \
          'November', 'December']
index = 0
for i in months:
    print(index + 1, i)
    index += 1
n = int(input("Enter a value between 1 and 12: "))
if 1 <= n <= 12:
    print ("The month is", months[n - 1])
else:
    print ("Value is out of the range")
```

## 切片操作(slicing)

```python
# 基本语法
list[start_index:end_index] # 包含 start_index(默认0) , 不包含 end_index(默认至结束)
tmplist = ['John', 'Kelly', 10, 'Caroline', 15, 'Steve', 'Katheline']
tmplist[0:3]
tmplist[2:4]
tmplist[-4]
tmplist[-4:-2]
tmplist[-5:5]
tmplist[:3]
tmplist[3:]
tmplist[:-3]
tmplist[-3:]
```

* `list` 相关方法

```python
append(object)
insert(index, object) # 将 object 插入 index 前, index 超出范围, 小于就在前追加, 大于就在后追加
pop(index) # 默认 -1, 最后一个元素. 移除并返回. 对空 list 操作将抛出异常
del list[n] # 删除 list 的 n
remove(value) # 移除, 如果 value 不再 list 中, 将抛出异常
reverse() # 反转 list
extend(list) # 将 list 的元素添加到原始 list 中
count(value) # 统计 value 在 list 中出现的次数
index(value) # 获取 value 在 list 中 index, 不存在将抛出异常
```

Tuple
=====

* 不可变
* 可存储任何数据类型

```python
names = ('John', 'Kelly', 'Caroline', 'Steve', 'Katheline')
n = input("Enter the name to search: ")
if n in names:
    print("The name", n, "is present in the tuple")
else:
    print("The name", n, "does not exist in the tuple")
countries = ('U.S.', 'U.K', 'India')
names += countries
print("The tuples are concatenated. The concatenated tuple is", names)
```

Dictionary
==========

* 可变

```python
d = {key1 : value1, key2 : value2 }
```

## 常用方法和函数

```python
clear()
pop(key, [default]) # key 对应的值不存在, 返回 default 指定的默认值
update(new, [key=value...]) # 合并两个字典, 已存在的 key 更新
copy()
get(key, [default]) # 如果 key 不存在, 默认值也没有提供, 就抛出一个异常
items() # 返回 tuple 组成的 序列 (key, value)
keys() # 返回 key 组成的 序列
values() # 返回 value 组成的 序列
```

```python
student1 = {'John' : 60, 'Kelly' : 70, 'Caroline' : 80}
student2 = dict([('David', 90), ('John',55)])
print('The items in dictionary student1 are:', student1.items())
print('The keys in student1 dictionary are:', student1.keys())
print('The values in student1 dictionary are:', student1.values())
student1.update(student2)
print('The items in dictionary student1 after merging with student2 dictionary are:', student1.items())
n = input('Enter name whose marks you want to see: ')
if n in student1: # key
    print('The marks of', n , 'are' , student1.get(n))
else:
    print('Sorry the name', n, 'does not exist in student1 dictionary')
```

Set
===

## 并(|)

```python
S1 = set([3,5,6,10,11,100])
S2 = set([1,3,5,6,11,15])
S1 | S2 # set([1,3,5,6,10,11,15,100])
```

## 交(&)

```python
S1 & S2 # set([3, 5, 6, 11])
```

## 差(-)

```python
S1 - S2 # set([10, 100])
```

## 集合的常用方法和函数

```python
len()
max()
min()
sum()
any() # 只要集合中有一个值为 True 就返回 True
all() # 集合中所有的值都为 True 才返回 True
sorted() # 将集合中元素排序后, 以 list 输出
clear() 
pop() # 移除集合中任意的一个元素, 如果集合为空, 将抛出异常
add(item)
remove(item)/discard(item) # 移除指定的元素, 如果不存在, 就抛出异常
update(set) # 将指定的 set 合并到原集合中
```

