Title: PyQt(Chapter 06)
Date: 2017-10-10 18:38:53
Category: PyQt
Tags: PyQt, Python

> File Handling

* 文件是数据对象序列的容器, 被描述为字节序列
* 文件处理是读写文件的技术

* 文件分类
  * 文本文件: 容易理解, 但是不易更新
  * 二进制文件: 优化了处理速度. 通过 offset 写入数据, 通过 seek() 方法访问特定的数据
  * Pickled files: 用于存储对象. 为了优化性能, 将对象存储为二进制格式

* 处理文件三步走:
  * 打开文件
  * 执行文件操作(读、写、更新)
  * 关闭文件

打开文件
=======

```python
# file_name 文件名
# mode 打开文件的目的
open(file_name, mode) # 返回 file handler 对象
f = open('xyz.txt', 'w')
```

* mode

```python
r  # 打开 for 读, 默认, 文件必须存在
w  # 创建一个文件用于写入. 如果文件已存在, 文件的原始内容将被覆盖(覆盖相当于完全擦除后, 再写入)
a  # 打开文件追加, 如果文件不存在, 就创建新文件
r+ # 打开 for 读写, 文件必须存在
w+ # 创建一个文件用于读写. 如果文件已存在, 文件的原始内容将被覆盖
a+ # 打开文件追加和读取, 如果文件不存在, 就创建新文件
```

文件操作
=======

* open

> open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
> Open file and return a stream.  Raise IOError upon failure.
> 
> file is either a text or byte string giving the name (and the path
> if the file isn't in the current working directory) of the file to
> be opened or an integer file descriptor of the file to be
> wrapped. (If a file descriptor is given, it is closed when the
> returned I/O object is closed, unless closefd is set to False.)
> 
> mode is an optional string that specifies the mode in which the file
> is opened. It defaults to 'r' which means open for reading in text
> mode.  Other common values are 'w' for writing (truncating the file if
> it already exists), 'x' for creating and writing to a new file, and
> 'a' for appending (which on some Unix systems, means that all writes
> append to the end of the file regardless of the current seek position).
> In text mode, if encoding is not specified the encoding used is platform
> dependent: locale.getpreferredencoding(False) is called to get the
> current locale encoding. (For reading and writing raw bytes use binary
> mode and leave encoding unspecified.) The available modes are:
> 
> ========= ===============================================================
> Character Meaning
> --------- ---------------------------------------------------------------
> 'r'       open for reading (default)
> 'w'       open for writing, truncating the file first
> 'x'       create a new file and open it for writing
> 'a'       open for writing, appending to the end of the file if it exists
> 'b'       binary mode
> 't'       text mode (default)
> '+'       open a disk file for updating (reading and writing)
> 'U'       universal newline mode (deprecated)
> ========= ===============================================================
> 
> The default mode is 'rt' (open for reading text). For binary random
> access, the mode 'w+b' opens and truncates the file to 0 bytes, while
> 'r+b' opens the file without truncation. The 'x' mode implies 'w' and
> raises an `FileExistsError` if the file already exists.
> 
> Python distinguishes between files opened in binary and text modes,
> even when the underlying operating system doesn't. Files opened in
> binary mode (appending 'b' to the mode argument) return contents as
> bytes objects without any decoding. In text mode (the default, or when
> 't' is appended to the mode argument), the contents of the file are
> returned as strings, the bytes having been first decoded using a
> platform-dependent encoding or using the specified encoding if given.
> 
> 'U' mode is deprecated and will raise an exception in future versions
> of Python.  It has no effect in Python 3.  Use newline to control
> universal newlines mode.
> 
> buffering is an optional integer used to set the buffering policy.
> Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
> line buffering (only usable in text mode), and an integer > 1 to indicate
> the size of a fixed-size chunk buffer.  When no buffering argument is
> given, the default buffering policy works as follows:
> 
> * Binary files are buffered in fixed-size chunks; the size of the buffer
> is chosen using a heuristic trying to determine the underlying device's
> "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
> On many systems, the buffer will typically be 4096 or 8192 bytes long.
> 
> * "Interactive" text files (files for which isatty() returns True)
> use line buffering.  Other text files use the policy described above
> for binary files.
> 
> encoding is the name of the encoding used to decode or encode the
> file. This should only be used in text mode. The default encoding is
> platform dependent, but any encoding supported by Python can be
> passed.  See the codecs module for the list of supported encodings.
> 
> errors is an optional string that specifies how encoding errors are to
> be handled---this argument should not be used in binary mode. Pass
> 'strict' to raise a ValueError exception if there is an encoding error
> (the default of None has the same effect), or pass 'ignore' to ignore
> errors. (Note that ignoring encoding errors can lead to data loss.)
> See the documentation for codecs.register or run 'help(codecs.Codec)'
> for a list of the permitted encoding error strings.
> 
> newline controls how universal newlines works (it only applies to text
> mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
> follows:
> 
> * On input, if newline is None, universal newlines mode is
> enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
> these are translated into '\n' before being returned to the
> caller. If it is '', universal newline mode is enabled, but line
> endings are returned to the caller untranslated. If it has any of
> the other legal values, input lines are only terminated by the given
> string, and the line ending is returned to the caller untranslated.
> 
> * On output, if newline is None, any '\n' characters written are
> translated to the system default line separator, os.linesep. If
> newline is '' or '\n', no translation takes place. If newline is any
> of the other legal values, any '\n' characters written are translated
> to the given string.
> 
> If closefd is False, the underlying file descriptor will be kept open
> when the file is closed. This does not work when a file name is given
> and must be True in that case.
> 
> A custom opener can be used by passing a callable as *opener*. The
> underlying file descriptor for the file object is then obtained by
> calling *opener* with (*file*, *flags*). *opener* must return an open
> file descriptor (passing os.open as *opener* results in functionality
> similar to passing None).
> 
> open() returns a file object whose type depends on the mode, and
> through which the standard file operations such as reading and writing
> are performed. When open() is used to open a file in a text mode ('w',
> 'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
> a file in a binary mode, the returned class varies: in read binary
> mode, it returns a BufferedReader; in write binary and append binary
> modes, it returns a BufferedWriter, and in read/write mode, it returns
> a BufferedRandom.
> 
> It is also possible to use a string or bytearray as a file for both
> reading and writing. For strings StringIO can be used like a file
> opened in a text mode, and for bytes a BytesIO can be used like a file
> opened in a binary mode.

* close

> close(self, /)
> Flush and close the IO object.
> This method has no effect if the file is already closed.

* read

> read(self, size=-1, /)
> Read at most n characters from stream.
> Read from underlying buffer until we have n characters or we hit EOF.
> If n is negative or omitted, read until EOF.

* readline

> readline(self, size=-1, /)
> Read until newline or EOF.
> 
> Returns an empty string if EOF is hit immediately.

* readlines

> readlines(self, hint=-1, /)
> Return a list of lines from the stream.  
> 
> hint can be specified to control the number of lines read: no more
> lines will be read if the total size (in bytes/characters) of all
> lines so far exceeds hint.

* flush

> flush(self, /)
> Flush write buffers, if applicable.
> This is not implemented for read-only and non-blocking streams.

* write

> write(self, text, /)
> Write string to stream.
> 
> Returns the number of characters written (which is always equal to
> the length of the string).

* writelines

> writelines(self, lines, /)

* seek

> seek(self, cookie, whence=0, /)
> Change stream position.
> 
> Change the stream position to the given byte offset. The offset is
> interpreted relative to the position indicated by whence.  Values
> for whence are:
> 
> * 0 -- start of stream (the default); offset should be zero or positive
> * 1 -- current stream position; offset may be negative
> * 2 -- end of stream; offset is usually negative
>     
> Return the new absolute position.

* tell

> tell(self, /)
> Return current stream position.
  
```python
matter = '''Python is a great language
Easy to understand and learn
Supports Object Oriented Programming
Also used in web development '''
f = open('aboutbook.txt', 'w')
print(type(f))
f.write(matter)
f.close()
f = open('aboutbook.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print (line)
f.close()
```

> A blank line carries a newline character `\n` and is considered a string of length `1`.

## 文件信息

* 通过文件对象(file handler)获取

* fileno

> fileno(self, /)
> Returns underlying file descriptor if one exists.
> 
> OSError is raised if the IO object does not use a file descriptor.

* isatty

> isatty(self, /)
> Return whether this is an 'interactive' stream.
> 
> Return False if it can't be determined.

* closed : 测试文件是否关闭了

* mode : 文件模式

* name : 文件名

```python
f = open("aboutbook.txt", "r")
print("Name of the file:", f.name)
print("Closed?", f.closed)
print("Opening mode:", f.mode)
print("File number descriptor is:", f.fileno())
f.close()
```

## 读取文件

```python
f = open('aboutbook.txt', 'r')
lines = f.read()
print(lines)
f.close()
```

```python
import sys
try:
    f = open('aboutbook.txt', 'r')
    lines = f.read()
except IOError:
    print('File aboutbook.txt does not exist')
    sys.exit(1)
f.close()
print (lines)
```

* `stdin` `stdout` `stderr` 标准输入输出流对象, 使用它们可以更好的控制流

## 向文件中追加内容

```python
import sys
matter2 = ''' Its very hot today
Lets have a Cold drink '''
f = open('aboutbook.txt', 'a' )
f.write("\n%s" % matter2)
f.close()
f = open('aboutbook.txt', 'r')
lines = f.readlines()
f.close()
print('The contents in the file are:')
for line in lines:
    sys.stdout.write(line)
```

## 复制文件

```python
f = open('aboutbook.txt', 'r')
lines = f.read()
f.close()
g = open('copyaboutbook.txt', 'w' )
g.write(lines)
g.close()
print('The copy of the file is made')
g = open('copyaboutbook.txt', 'r' )
lines = g.read()
print(lines)
g.close()
```

## 从文件中删除内容

```python
import sys
f = open('aboutbook.txt', 'r' )
lines = f.readlines()
print('Original content of the file:')
for line in lines:
    sys.stdout.write(line)
f.close()
del lines[1:3]
f = open('aboutbook.txt', 'w' )
f.writelines(lines)
f.close()
print('\nThe content of the file after deleting second and third line:')
f = open('aboutbook.txt', 'r' )
lines = f.read()
print (lines)
f.close()
```

## 更新文件的内容

```python
import sys
f = open('aboutbook.txt', 'r')
lines = f.readlines()
print('Original content of the file:')
for line in lines:
    sys.stdout.write(line)
f.close()
n = int(input("\n\nEnter the line number to change: "))
if n <=len(lines):
    r = input("Enter the new content: ")
    lines[n-1] = r + "\n"
    f = open('aboutbook.txt', 'w' )
    f.writelines(lines)
    f.close()
    print('The content of the file after updating line' , n)
    f = open('aboutbook.txt', 'r' )
    lines = f.read()
    print (lines)
    f.close()
else:
    print ("The line number", n, "is not found in the file" )
```

## 从文件的任意位置读入内容

```python
f = open('aboutbook.txt', 'r')
line = f.readline()
print('A line from file is:', line)
f.seek(5)
line = f.readline()
print('The line from character 6 till end of line is:', line)
print('The pointer is at location', f.tell())
f.seek(11)
line = f.read(15)
print('The fifteen characters starting at location 12 are as:', line)
```

## 访问文件中指定的内容

```python
import linecache
line = linecache.getline('aboutbook.txt', 3)
print('The content of the third line is:', line)
```

```python
f = open('numbers.txt', 'w' )
n = int(input('How many numbers? ' ))
print('Enter', n, 'numbers' )
for i in range(0,n):
    m = input()
    f.write("%s\n" % m)
f.close()
f = open('numbers.txt')
lines = f.readlines()
f.close()
print('The numbers stored in the file are')
for line in lines:
    print(int(line))
print('The numbers in the file multiplied by 2')
for line in lines:
    print (int(line) * 2)
```

## 创建二进制文件

```python
str = 'Hello World!'
f = open("filebinary.bin", "wb")
f.write(str.encode('utf-8'))
f.close()
f = open("filebinary.bin","rb" )
fcontent=f.read()
f.close()
print('The content in the file is:')
print(fcontent.decode('utf-8'))
```

## 序列化(Pickling)

* Pickling : 一个将结构化数据转换为数据流的过程
* 通过 `Pickling`, 可以将 `list` `tuple` `function` `class` 通过使用 `ASCII` 字符存储在文件中
* `序列化`的数据格式被标准化了, 所以与序列化相对的有`反序列化`
* `序列化` : 存储数据; `反序列化` : 恢复数据
* 常用模块 `pickle` `cPickle`, 它们功能一样, `cPickle` 是 C 实现, 所以性能更好

```python
import pickle
class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def rectarea(self):
        # 这样返回的是一个 tuple
        return "Area of rectangle is", self.l * self.b
r = rect(5, 8)
f = open('studentinfo.bin', 'wb')
pickle.dump(r, f)
f.close()
del r
f = open('studentinfo.bin','rb')
storedobj = pickle.load(f)
print(type(storedobj))
print(storedobj.rectarea())
```

```python
import pickle
class user:
    def __init__(self, x, y, z):
        self.id = x
        self.name = y
        self.emailadd = z
    def dispuser(self):
        print('User ID:', self.id)
        print('User Name:', self.name)
        print('Email Address:', self.emailadd)
f = open('UsersInfo.bin', 'wb')
n = int(input('How many users? '))
print('Enter', n, 'numbers')
for i in range(0, n):
    u = input('User ID: ')
    n = input('User Name: ')
    e = input('Email Address: ')
    usrobj = user(u, n, e)
    pickle.dump(usrobj,f)
f.close()
print('\nInformation of the users is:')
f = open('UsersInfo.bin', 'rb')
while True:
    try:
        # 从 f 中 load 对象, load 方法是 一个接一个 的 load 对象的
        usrobj = pickle.load(f)
    except EOFError:
        # 文件结束异常捕获
        break
    else:
        # 使用 load 的对象
        usrobj.dispuser()
f.close()
```

异常处理
=======

* 异常处理的两种形式
  * try/except : 至少要有一个 `except` 语句与 `try` 语句配对
  * try/finally : 不管异常出现与否, `finally` 语句总是被执行. 

## try/except

```python
try:
    statement(s)
except SomeException: # except 的数量无限制, 每一个 except 表达式就是一个异常处理器(exception handler)
    code for handling exception 
[else:
    statement(s)]
```

* try/except 的处理过程
  * 执行 try 代码块
  * 如果 try 代码块没有抛出异常, except 代码块被忽略
  * 如果 try 代码块抛出了异常, 就会通过 except 来匹配对应的异常, 当匹配到了, 就执行 except 代码块
  * 如果 except 没有匹配到, Python 会在 try 代码块的外部继续寻找 `exception handler`. 如果还是没有找到, 就使用 Python 内建的异常处理器
  * else 语句只有在 try 代码块执行成功(没有抛出异常)时, 才执行. 
  * try 代码块可以嵌套

* 常见异常

```python
AssertionError # 断言失败异常
AttributeError # 属性没有找到异常
EOFError # 读取文件超出文件结束符异常
FloatingPointError # 浮点操作失败异常
IOError # I/O 操作失败异常
IndexError # index 超出 range
KeyError # mapping 的 key 不存在
OSError # 操作系统调用失败
OverflowError # 值太大, 不能表示. 移除异常
TypeError # 对参数应用了不适当的类型
ValueError # 使用了不适当的参数值
ZeroDivisionError # 除零异常 ( / %)
```

## try/finally

* 异常出现后, 后续代码就会停止执行并退出程序
* 无论异常出现与否, 一些确定的都需要被执行, 包括释放内存、关闭文件, 这时就可以使用 finally 代码块
* try/finally 的处理过程
  * 执行 try 代码块
  * 如果 try 代码块没有抛出异常, finally 代码块被执行
  * 如果 try 代码块中执行到退出语句(return、break、continue), finally 代码块在退出前被执行
  * 如果 try 代码块中出现了异常, 先执行 finally 代码块, 然后再抛出异常


```python
import sys
try:
    f = open('aboutbook.txt', 'r')
    try:
        lines = f.read()
    finally:
        f.close()
except IOError:
    print('File aboutbook.txt does not exist')
    sys.exit(1)
print(lines)
```

## 抛出异常

* 可以在 try/except 中使用 `raise` 语句抛出确定的异常

```python
try:
    if condition:
        raise customException, statement for customException 
except customException, e:
    statements for customException
```

```python
class myException(Exception):
    def __init__(self, quantity):
        Exception.__init__(self)
        self.quantity = quantity
try:
    s = int(input('Enter quantity '))
    if s <= 0:
        raise myException(s)
except EOFError:
    print('You pressed EOF ')
except myException as ex:
    print('myException:The quantity entered is %d, it must be some positive value'\
          % ex.quantity)
else:
    print ('No exception raised.')
```

## 使用断言

* 当断言失败时, 会抛出 `AssertionError` 异常

```python
n = int(input('Enter a positive value: '))
assert(n >= 0), "Entered value is not a positive value"
```

