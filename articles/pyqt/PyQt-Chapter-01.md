Title: PyQt(Chapter 01)
Date: 2017-09-24 20:12:54
Category: PyQt
Tags: PyQt, Python

> Python and Its Features

数据类型
======

## Integers

* 32 bits
* [-2<sup>32</sup> 2<sup>32</sup>-1]

## Long Integers

* 无限精度, 受限于计算机内存

## Floating Point Numbers

* 浮点总是双精度的, 64 bits

## Boolean

* 仅取两个值: True、False

## Complex Number(复数)

* a + b * j
* a、b都是浮点数

## Strings

* Unicode 字符序列

## Lists

* 一组值的有序序列

## Tuples

* 不可变、一组值的有序序列

## Sets

* 无序的值的集合

## Dictionaries

* 无序的键值对集合

> 0b、0B: 二进制; 0o、0O: 八进制; 0x、0X: 十六进制

编程的基本元素
============

## 字面量

```python
10 # Integer literal10.50 # Floating-point literal 
10.50j #Imaginary literal 
'Hello' # String literal 
"World!" # String literal 
'''Hello World!It might rain today # Triple-quoted string literalTomorrow is Sunday'''
```

## 变量

```python
l = 10length = 10 
length_rectangle = 10.0 
k = "Hello World!"
```

```python
a = True #Booleanvariableb = [2,9,4] # List variablec = ('apple', 'mango', 'banana') # tuple variable 
# A tuple in python language refers to an ordered, immutable (non changeable) set of values of any data type.
```

## 关键字

* Python 共有 31 个关键字

```python
and class elif finally if
lambda print while as assert
break continue def del else
except exec for from global
import in is not or
pass raise return try with yield
```

注释
===

```python
# this is comment
```

代码多行支持
==========

* 物理行 : 编辑器中看见的一行
* 逻辑行 : Python 中的一个语句
* Python 中一般物理行就是逻辑行. 但可以使用 `\` 将多个物理行转换为逻辑行
* 如果括号(`(``[``{`)没有关闭, Python 也将把多个物理行转换为一个逻辑行
* Python 缩排规则仅使用在连续行的第一行, 其他行不适用

打印输出
=======

```python
# 通用语法
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# 例子
print ("Hello World!") print (10)print (l)print ("Length is ",l)
print ("Length is %d and Breadth is %d" % (l, b)) # 如果格式不匹配, 将转换为要输出的格式
```

```python
%s # Displays in string format.%d # Displays in decimal format%e # Displays in exponential format.%f # Displays in floating-point format.%o # Displays in octal (base 8) format. 
%x # Displays in hexadecimal format. 
%c # Displays ASCII code.
```

```pythonprint (10) 
print('Hello World! \
It might rain today. \
Tomorrow is Sunday.')
print('''Hello World!
It might rain today.
Tomorrow is Sunday.''')
```


