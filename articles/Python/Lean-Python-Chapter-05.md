Title: Lean Python(Chapter 05)
Date: 2017-09-22 13:53:15
Category: Python
Tags: Lean Python

> Module

导入模块
=======

* 一个`文件`就是一个`模块`, `模块名`就是`文件名`

```python
# as 使用自定义的名字引用这个模块
import modulename [as name]
# 从模块中引入指定的函数、类、变量等
from module import function1, function2...
# 从模块中引入所有的内容, 这时直接使用, 而不需要使用 . 引用
from module import *
```

* 注意 : 通常, 导入模块的需要内容和功能, 而要避免使用 `import *`

## Python 自带模块

* 查看 Python 环境 Path

```python
import sys
sys.path
```

