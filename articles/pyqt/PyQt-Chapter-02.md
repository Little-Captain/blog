Title: PyQt(Chapter 02)
Date: 2017-09-25 00:54:00
Category: PyQt
Tags: PyQt, Python

> Getting Wet in Python (深入巨蟒湿地)

算数操作符
========

```python
x + y # Addition
x - y # Subtraction
x * y # Multiplication
x / y # Division
x // y # Truncating division (floor division)
x ** y # Exponentiation. Sets x to the power y
x % y # Modulo operator
–x # Unary minus
+x # Unary plus
```


## 除法操作符

* `/` : 结果总是不会被截断, 结果总是浮点数
* `//` : 不管有没有浮点操作数, 都将结果截断为整数. 但是如果一个操作数为浮点数, 结果就为浮点数

```python
b = 17
h = 13
a = 1.0 / 2.0 * b * h
print("Area of triangle is", a)
print("Base= %d, Height is %d, Area of triangle is %f" % (b, h, a))
```

```python
p = q = r = 10
a = 1.0 / 3.0 * (p + q + r)
print ("Average of three variables is", a) 
print ("Average of three variables is %.2f" % a) 
print ("Average of three variables is %d" % a)
```

```python
# __future__ 是版本新特性, 意思是下一个版本会添加, 而且这些新特性可能与当前版本不兼容
# from __future__ import division
p = q = r = 10
a = (p + q + r) / 3
print ("Average of three variables is", a)
```

## 幂运算

* `**` a ** b : a<sup>b</sup>
* pow(a, b) 与 a ** b 等价

```python
r = 3
pi = 22 / 7
v = 4 / 3 * pi * pow(r, 3)
print ("Volume of sphere is %.2f" % v)
```

```python
from math import pi
r = 3
v = 4 / 3 * pi * pow(r, 3)
print ("Volume of sphere is %.2f" % v)
```

多重赋值
=======

```python
p, q, r = 10, 20, 30
sum, avg = p + q + r, (p + q + r) / 3
```

使用转义序列
==========

```python
\a # Bell (beep) 
\b # Backspace 
\f # Form feed 
\n # Newline 
\r # Carriage return 
\t # Tab
\v # Vertical tab 
\\ # Literal backslash 
\' # Single quote 
\" # Double quote
```

```python
print('Hello World\nIt\'s hot today') 
print('Festival Discount\b\b\b\b\b\b\b\b\b Offer') 
print("Isn't it?")
print('Isn\'t it?')
print("He said: \"I am going \"")
print('\\Text enclosed in back slashes\\')
print ('Bell sound \a')
print('Name\tEmail Address\tContact Number')
```

确定数据类型
==========

* `type` 函数

```python
a = 10
b = 15.5
c = "Hello"
d = [2, 9, 4]
e = ('apple', 'mango', 'banana') 
f=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
```

八进制和十六进制
=============

```python
a = 0o25
b = 0x1af
print('Value of a in decimal is', a) 
c = 19
print('19 in octal is %o and in hex is %x' % (c, c)) 
d = oct(c) # d 是字符串
e = hex(c) # e 是字符串
print('19 in octal is', d, 'and in hex is', e)
```

获取数据
=======

* 使用 `input` 函数, 提示用户输入数据, 并从标准输入读入一行数据, 并将读入的数据以字符串返回

```python
variable = input('Message')
```

自动数据类型转换
=============

```python
a = 3
a = a + .0 # int -> float
b = 3
b = b + 0j # int -> complex
```

显示(强制)数据类型转换
===================

* 使用函数进行转换 `int` `float` `str` ...
* `转换失败`会`抛出异常`

```python
int(x=0) -> integer
int(x, base=10) -> integer # base [2 26]
```

```python
l = input("Enter length: ")
b = input("Enter width: ") 
a = int(l) * int(b)
print("Area of rectangle is", a)
```

```python
from math import pi
r = int(input("Enter radius: "))
a = pi * r * r
print("Area of the circle is", a)
print("Area of the circle is %.2f" % a)
```

位运算
=====

* 位运算只能应用于 `int` `long`

```python
x << y # x 左移 y 位
x >> y # x 右移 y 位
x & y # x 和 y 按位与
x | y # x 和 y 按位或
x ^ y # x 和 y 按位异或
~x # x 按位取反
```

```python
a = 10 # 1010
b = 7  # 0111
c = a & b
d = a ^ b
e = a | b
print('The result of 10 and 7 operation is', c)
print('The result of 10 exclusive or 7 operation is' , d) 
print ('The result of 10 or 7 operation is', e)
g = a << 2
print('Left shifting - Multiplying 10 by 4 becomes:' , g) 
h = a >> 1
print('Right shifting - Dividing 10 by 2 becomes:', h)
```

复数
====

```python
a = 3 + 1.2j
a.real # 3.0
a.imag # 1.2
```

```python
a = 3.0 + 1.2j
b = -2.0 - 9.0j
print('The two complex numbers are', a, 'and', b)
c = a + b
print('The addition of two complex numbers is:', c)
print('The addition of two real numbers is:', a.real + b.real)
print('The addition of two imaginary number is:', a.imag + b.imag)
```

选择结构
=======

```python
if (logical expression): 
    statement(s)
else: # else 语句是可选的
    statement(s)
```

```python
# 比较运算符
< # Less than
> # Greater than
<= # Less than or equal to
>= # Greater than or equal to
== # Equal to
!= # Not equal to  
```


```python
if (logical expression):
    statement(s)
elif (logical expression 1):
    statement(s)
[elif (logical expression n):
    statement(s)]
else:
    statement(s)
```

逻辑运算符
========

```python
and # 逻辑与
or  # 逻辑或
not # 逻辑非
```

比较链
=====

```python
x <= y and y <= z
# 等价于
x <= y <= z
```

循环
===

## while

```python
while expression:
    statement1
    statement2
    statement3
```

## break and continue

```python
k = 1
while 1:
    print(k)
    k += 1
    if k > 10:
        break
```

```python
k = 1
while k <= 10:
    if k == 7:
        k += 1
        continue
    print(k)
    k += 1
```

## pass

* 表示`空的语句块`, 什么也不做
* 表示代码占位符, 这部分代码你可能在随后扩展程序功能时添加

```python
k = 1
while k <= 10:
    if k == 7:
        pass
    else:
        print(k)
    k += 1
```

## range()函数

* 参数必须是整数
* 生成和返回一个整数的序列
* 如果所给参数, 不能产生序列, 就会返回一个空序列

```python
# [0 x)
range(x)
# [x, y)
range(x, y)
# [x, y) step 可以小于 0, step 不能为 0
range(x, y, step)
```

## for

* 通过一个`序列`(list、tuple、string、dictionary)进行`迭代`
* Python容器包含: 集合(set)、序列(sequence)

```python
for iterating_var in sequence:
    statement1
    statement2
    statement3
```

## 成员操作符

* `in` `not in` 判断序列中是否存在某个值

```python
for i in (7, 3, 8, 1, 4):
    print(i)
```

## choice() 函数

* 从一个序列中随机获取一个值

```python
# choice(sequence)
from random import choice
k = choice(range(1, 10))
print("Random number is", k)
```

```python
print(1)
for i in range(2, 101):
    x = 1
    for j in range(2, i):
        n = i % j
        if n == 0:
            x = 0
            break
    if x == 1:
        print(i)
```

