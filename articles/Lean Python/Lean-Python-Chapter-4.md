Title: Lean Python(Chapter 4)
Date: 2017-09-21 23:39:04
Category: Lean Python

> Input and Output

显示输出
=======

```python
# 格式
print(arg1,arg2,arg3...,sep=' ',end='\n')
```

<!--more-->

* 使用格式输出

```python
print('%d plus %d makes %d' % (3, 7, 10))
```

* 抑制最后的空行输出

```python
print('one...','two...','three',end='')
```

获取用户输入
==========

```python
yourName=input('Enter your name: ')
```

* 接收的输入都是字符串, 所以要用户输入数字等需要自行解析

```python
count = input('Enter a number: ')
if len(count) > 0:
    if count.isdigit():
        count = int(count)
        print(count++)
```

读写文件
======

## 打开文件

```python
fileobj = open(filename, mode)
```

* mode

| 打开模式 | 文件存在 | 文件不存在 |
|:-:|:-:|:-:|
| 'r' | 打开, 只读 | 不存在文件或目录, 报错 |
| 'w' | 打开, 写入(覆盖) | 创建, 写入 |
| 'a' | 打开, 写入(追加) | 创建, 写入 |

```python
fname = 'myfile.txt'
fp = open(fname, 'r')
fp = open(fname, 'w')
fp = open(fname, 'a')
```

## 关闭文件

* 一旦你完成文件操作, 就应该关闭文件
* 文件的 open 和 close 操作, 总是成对使用

```python
import os
fp = open(fname,'w') 
# do something
fp.close()
```

## 读取文件

* read() 以`字符串`的形式`读取`文件的`全部内容`
* 可以将读取的内容以`换行符`('\n')进行`分隔`

```python
fp = open(fname, 'r')
text = fp.read()
lines = text.split('\n')
fp.close()
```

* readlines() 返回一个 list , list 的元素就是每行的字符串

```python
fp = open(fname, 'r')
lines = fp.readlines() # 每行包含换行符'\n'
fp.close()
```

```python
fp = open(fname, 'r')
# 去掉了右边的空白字符
lines = [line.rstrip() for line in fp.readlines()]
fp.close()
```

* 使用文件对象自带的迭代器逐行读取文件内容

```python
fp = open(fname,'r')
for eachLine in fp:
    print(eachLine, end = '')
fp.close()
```

## 写入文件

* 标准写入函数 write()
* write() 函数, 不主动添加任何换行符

```python
fp.write(textline)
```

```python
fp = open('text.txt','w')
while True:
    text = input('Enter text (end with blank):')
    if len(text)==0:
        break
    else:
        fp.write(text+'\n')
fp.close()
```

```python
lines=['line 1','line 2','line 3','line 4']
# write all lines with no '\n'
fp.writelines(lines)
# writes all line with '\n'
fp.writelines([line+'\n' for line in lines])
```

* 注意 : write() 和 writelines() 函数都不会在字符串末尾添加换行符(\n), 你必须自己添加

## 访问文件系统

* os 模块中的一些常用函数

```python
import os
# remove a file (deleteme.txt) from disk
os.unlink('deleteme.txt')
# rename file on disk (from file.txt to newname.txt)
os.rename('file.txt','newname.txt')
# change current/working directory
os.chdir(newdirectory)
# create list of files in a directory
filelist = os.listdir(dirname)
# obtain current directory
curdir = os.getcwd()
# create a directory
os.mkdir(dirname)
# remove a directory (requires it to be empty)
os.rmdir(dirname)
# in the following examples, we need to use
# the os.path module
#
# does the file/directory exist?
exists = os.path.exists(path)
# does path name exist and(且) is it a file?
isfile = os.path.isfile(filepathname)
# does path name exist and(且) is it is directory?
isdir = os.path.isdir(filepath)
```

命令行参数
========

```python
python mycopy.py thisfile.txt thatfile.txt
```

* 如何捕获命令行参数

```python
import sys
nargs=len(sys.argv) # sys.argv is List
print('%d argument(s)' % (nargs))
n=0
for a in sys.argv:
    print('  arg %d is %s' % (n, a))
    n+=1
```

* 注意 : `第一参数`总是`程序的名字`


