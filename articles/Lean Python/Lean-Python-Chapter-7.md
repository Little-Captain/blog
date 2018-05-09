Title: Lean Python(Chapter 7)
Date: 2017-09-23 15:39:49
Category: Python

> Exception and Error Handling

<!-- more -->

异常和错误的处理
=============

```python
print('Input two numbers. the first will be divided by the second')

afirst = input('first number:')
first=float(afirst)
asecond = input('second number:')
second = float(asecond)

quotient = first / second
print('Quotient first/second = ',quotient)
```

```python
print('Input two numbers. the first will be divided by the second')

afirst = input('first number:')
asecond = input('second number:')

try:
    first=float(afirst)
    second = float(asecond)
    quotient = first / second
    print('Quotient 1st/2nd = ', quotient)
except Exception as diag:
    print(diag.__class__.__name__, ':', diag)
```

* Exception 是一个针对异常的顶层类, 所以它可以捕获所有的错误


