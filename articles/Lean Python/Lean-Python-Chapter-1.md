Title: Lean Python(Chapter 1)
Date: 2017-09-19 12:40:08
Category: Lean Python
Tag: Python

> Foundation

解释器
=====

## 交互模式

* dir : 列出一个对象的所有属性

```python
dir(print)
```

<!--more-->

* help : 查看内建关键字和方法的帮助文档

```python
help(open)
```

## 命令行模式

* 通过在命令行中加载 python 程序执行

```python
python myprogram.py
```

注释、代码块、缩进
===============

* 使用 `#` 进行注释
* 使用相同的`缩进`区分代码块
* `:` 用在 if、elif、else、while、for、函数定义中, 区分首行和下面的具体代码块, 具体代码块需要缩进
* 使用 `\` 连接多行代码

变量
====

* 赋值

```python
var = expression
var1, var2, var3 = expression
a = b = c = 1
```

* 关键字

> and class elif finally if lambda print while as assert break continue def del else except exec for from global import in is not or pass raise return try with yield

* 内建名字

> True False all any dir eval float format max min open print round set tuple type None abs chr dict exit file input int next object quit range str sum vars zip

* 特殊标识符

```python
# 形式
_xxx
__xxx__
__xxx
```

* 例如: \_\_name\_\_ 代表模块名

模块
===

* 导入模块

```python
import mymodule
```

典型的程序结构
===========

```python
# 自定 python 的位置
#!/usr/local/bin/python3.6
# 引入模块, 说明模块功能
from datetime import datetime
# 创建全局变量
now = datetime.now();
# 首先定义类, 其他引入这个模块的代码可以使用
class bookClass(object):
    "Book object"
    def __init__(self, title):
        self.title = title
        return
# 然后定义函数, 通过 module.function() 调用
def testbook():
    "testing testing..."
    title = "How to test Py"
    book = bookClass(title)
    print("Tested the book")
# 如果模块运行, 这儿的代码将被执行
if __name__ == '__main__':
    testBook()
```


