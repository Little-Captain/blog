Title: Lean Python(Chapter 3)
Date: 2017-09-21 21:26:45
Category: Lean Python
Tag: Python

> Program Structure

做决定
=====

## if 语句

<!--more-->

```python
if test:
    statement1 # 如果条件为真, 这三条语句都将执行
    statement2
    statement3
# if else
if test:
    DoThis()
else:
    DoThat()
# if elif else
if test1:
    DoThis()
elif test2:
    DoThat()
else:
    DoOther()
```

* 同一语句中的 `if` `elif` `else` 的缩进必须保持一致

## pass 语句

* pass 语句就是什么都不做

```python
if test1:
    DoThis()
elif test2:
    DoThat()
# else 不是严格必须, 但是加上, 通过使用 pass 语句, 表明这时什么都不做, 语义更明确
else:
    pass
```

## 常见的测试条件

* 比较

```python
var1 > var2
```

* 序列的成员所属关系

```python
var in seq
var not in seq
```

* 序列长度

```python
len(x)>0
```

* 布尔值

```python
fileopen # fileopen == True ?
```

* 变量是否有值

```python
var # not None (or zero or '')
```

* 校验

```python
var.isalpha() # alphanumeric ?
```

* 计算结果比较

```python
(price * quantity) > 100.0 # cost > 100?
```

* 逻辑操作符: `and` `or` `not` 可以用来连接条件构成复合条件

* 嵌套的条件表达式, 通过缩进区分层级

```python
if age>19:
    if carValue>10000:
        if gotConvictions:
            rejectInsuranceApplication()
```

循环和迭代
=========

## for 循环 

* 迭代一个集合中的每个元素

```python
theTeam=['Julia','Jane','Tom','Dick','Harry']
for person in theTeam:
    print('%s is in the team' % person)
# for 循环的通用格式为 for var in seq:
```

```python
range(10) # [0, 1, 2, ... , 9]
range(1, 10) # [1, 2, ... , 9], 不包括 10
range(1, 20, 3) # 1 开始, 20 结束(不包括), 3 为步长

# 不想遍历序列, 只是想执行指定的代码指定的次数
for i in range(3):
```

## while 循环 

* 重复执行循环直到测试失败

```python
n = 4
while n > 0:
    print(n)
    n -= 1
```

## break 语句 

* 终止循环, 执行循环后的语句

```python
while True:
    command=input('Enter command:')
    if command=='exit':
        break
    else:
        print(command)
print('bye')
```

## continue 语句

* 跳过本次循环的后续代码, 直接进行下次循环

```python
while True:
    command=input('Enter command:')
    if len(command)==0:
        continue
    elif command=='exit':
        print('Goodbye')
        break
    else:
        print(command)
print('bye')
```

## List Comprehensions (列表推导式、列表解析)

```python
# 普通方法
squares=[]
for i in range(1,11):
    squares.append(i*i)
# 列表推导式
squares=[i*i for i in range(1,11)]
# 具体语法
[expr for element in iterable if condition]
# if 语句用于从 iterable 中选择元素
# 例子
evens = [i for i in range(1,100) if not i % 2]
trulines = [l for l in lines if l.find('True')>-1]
```

使用函数
=======

## 函数是什么

* 一个函数是一个代码片段

```python
# 关键字 def 用于定义一个新函数
def lenDictList(seq):
    if type(seq) not in [list,dict]:
        return -1
    nelems = 0
    for elem in seq:
        nelems += 1
    return nelems

# 调用实例
l = [1,2,3,4,5]
d = {1:'one',2:'two',3:'three'}
lenDictList(l)
lenDictList(d)
lenDictList(34)
```

## 返回值

```python
return
return True
return False
return r1, r2, r3
return dict(a = v1, b = v2)
```

## 调用函数

```python
# 左边变量的个数必须和右边函数的返回值个数匹配
count = len(seq)
max, min, average = analyse(numlist)
fee = calculateFee(hours, rate, taxfactor)
```

## 调用时给参数指定名字

* 指定名字的参数必须全部位于未指定名字的参数之后
* 自定名字的参数是关键字参数, 没有指定名字的参数是位置参数. `关键字参数`必须位于`位置参数`之`后`

```python
def fn(a, b, c=1.0):
    return a*b*c
fn(1,2,3)
fn(1,2)
fn(1,b=2)
fn(a=1,b=2,c=3)
fn(1,b=2,3) # 错误!!! positional argument follows keyword argument
```

## 变量作用域

```python
sharedvar = "I'm sharable"
def first():
    print(sharedvar)
    firstvar = 'Not shared'
    return
def second():
    print(sharedvar)
    print(firstvar) # error
    return
```


