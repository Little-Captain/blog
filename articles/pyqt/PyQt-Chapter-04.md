Title: PyQt(Chapter 04)
Date: 2017-10-07 13:29:34
Category: PyQt
Tags: PyQt, Python

函数
===

* 在 Python 中, `函数`别当做`对象`

## 函数的定义

```python
def function-name(parameters):
    statements(s)
```

## 返回语句

* 返回语句是可选的, 如果没有, 函数返回 None

## 默认参数值

```python
def sum(x, y = 10):
    return x + y
print(sum(10))
print(sum(5, 8))
```

## 关键字参数

```python
def volume(l, b=5, h=10):
    print('l is', l, 'and b is', b, 'and h is', h, 'and volume is', l*b*h)
volume(2, 4)
volume(3, h=6)
volume(h=7, l=2)
```

## 本地和全局变量

* 本地变量在函数内定义, 在函数内访问
* 全局变量在函数内外都可以访问
* 如果在函数外访问本地变量, 将抛出一个错误

### 全局变量

* 如果某个函数需要全局变量, 在函数的第一条语句应该是这样的

```python
global identifiers # 多个以逗号隔开
```

* 使用 `global` 定义全局变量
* 如果本地变量没有初始化, 一个 UnboundLocalError 异常将会被抛出

```python
def compute():
    global x
    print ("Value of x in compute function is", x)
    x += 5
    return None
def dispvalue():
    global x
    print ("Value of x in dispvalue function is", x)
    x -= 2
    return None
x = 0
compute()
dispvalue()
compute()
```

### 本地变量

```python
def compute(x):
    x += 5
    print("Value of x in function is", x)
    return None
x = 10
compute(x)
print ("Value of x is still", x)
```

## Lambda 函数

* 一个 lambda 函数只能包含一条语句

```python
filter(function, sequence)
map(function, sequence)
reduce(function, sequence)
```

## 函数的属性

* 函数是对象, 所以有属性

```python
# 函数属性
functionname.__doc__ # 函数文档字符串, 函数体的第一行字符串
functionname.__name__ # 函数名
functionname.__module__ # 函数所属模块名
functionname.__defaults__ # 一个 tuple, 代表分配给默认参数的默认参数值
functionname.__code__ # 实际的代码对象
functionname.__dict__ # 代表函数属性的本地命名空间
# 你可以 set 和 get 属于你自己的函数属性
```

### 文档字符串

* 函数体的第一个逻辑行代表函数的文档字符串
* 要显示文档字符串使用 `__doc__` 属性
* `函数`、`类`、`模块`都有文档字符串

```python
def rect(l, b):
    '''Computes the area of rectangle
Values for length and breadth are passed to the function for computation'''
    print('Area of rectangle is', l*b)
rect(5, 8)
print(rect.__doc__)
```

递归
===

* 一个函数, 自己调用自己
* 实现递归调用, 结束条件必须明确

```python
def addseq(x):
    if x == 1: return 1
    else: return x + addseq(x-1)
print('The sum of first 10 sequence numbers is', addseq(10))
```

迭代器
=====

* 迭代器用于循环遍历一个集合中的数据
* iter() 函数创建一个迭代器对象
* 一旦获取到了一个迭代器对象, 就可以通过迭代器对象的 next() 方法遍历这个对象

```python
# iter 调用对象的 __iter__ 方法获取一个迭代器对象
iter(object)
```

## generator

* 另一个中创建迭代器的方法, 使用 `generator`
* generator 是一个创建迭代器的函数
* 对于一个函数要变成 `generator`, 必须在返回语句中使用 `yield` 关键字
* 同理, `generator` 函数使用 `yield` 关键字来获取一个容器对象的下一个值
* `yield` 语句仅仅在定义 `generator` 函数时使用, 且仅仅在 `generator` 函数体内使用
* 当调用一个 `generator` 函数时, 它返回一个称为 `generator iterator` 的迭代器

```python
def fruits(seq):
    for fruit in seq:
        yield '%s' % fruit

f = fruits(['Apple', 'Orange', 'Mango', 'Banana' ])
print('The list of fruits is:' )
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
f = fruits(['Apple', 'Orange', 'Mango', 'Banana' ])
print('The list of fruits is:' )
for x in f:
    print (x)
```

## generator expression

* `generator expression` : 创建迭代器对象, 通过圆括号包裹
* `generator expression` 像是匿名函数, 通常由`至少一个 for 语句`和`零个或多个 if 语句`组成

```python
def squarenum(x):
    return x * x
iteratorobj = (squarenum(x) for x in range(6))
print('The squares of first five sequence numbers')
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
```

模块
===

* 一个模块就是一个针对特定任务的一些函数、变量组成的一个文件
* 一个模块只要被导入, 可以在任何地方重用
* 模块的文件名必须以`.py`为后缀名

```python
# 导入模块的多种方式
# 方式一: 全部导入, 不重命名
import calendar
calendar.prcal()
# 方式二: 指定导入, 不需要模块名前缀
from calendar import prcal
prcal()
# 方式三: 指定全部导入, 不需要模块名前缀
from calendar import *
prcal()
# 方式四: 全部导入, 重命名
import calendar as cal
cal.prcal()
```

## Math 模块

* Math 模块包含一些三角函数、常量、还有其他很多很多的函数

```python
math.pi
math.e
ceil(x)
floor(x)
```

### dir() 函数

* 查看模块中所有 `identifier`, 包括函数、类、变量

```python
# 不传参, 就使用当前模块
dir(模块名)
```

命令行参数
========

* `sys.argv` 命令行参数存储的变量, 它是个 list, 长度至少是1, 0索引位置指示的是运行的程序名
* 传入命令行参数时, 使用`空格`分隔

```python
import sys
print('There are %d arguments' % len(sys.argv))
print('The command line arguments are:' )
print(sys.argv)
for i in sys.argv:
    print(i)
    print('Path of the Python is' , sys.path)
```





