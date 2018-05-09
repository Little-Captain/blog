Title: PyQt(Chapter 05)
Date: 2017-10-09 11:41:54
Category: PyQt
Tags: PyQt, Python

> Classes

类
===

* 类是数据和操作的模板
* 通过类可以创建实例(对象)

```python
# 多个父类用逗号隔开
class classname[(base-classes)]:
    statement(s)
```

## 类对象的属性

* 类属性, 不需要实例对象, 使用类名引用

```python
class rect:
    l = 8
print(rect.l)
```

```python
class rect(object):
    pass
rect.l = 10
print(rect.l)
```

### 内建的类属性

* 一个类隐式的设置了一些类属性, 我们称之为内建类属性

```python
__name__ # 类名
__bases__ # 一个 tuple 指示 base classes
__dict__ # 通过 key/value 存储类的自定义属性. rect.__dict__['l'] = 8
__doc__ # 类的文档字符串
__module__ # 定义类的模块名
```

```python
class rect:
    l=8
    b=5
print("Length is %d, Breadth is %d" % (rect.l, rect.b))
print("Class name is ", rect.__name__, " and Base class is ",rect.__bases__)
print("Attributes of this class are ", rect.__dict__)
```

* 如果你没有指定一个`基类`, 默认`object`

## 类中定义函数

```python
class classname(base-classes):
    class variable(s)
    def method 1(self):
        instance variable(s)
        statement(s)
    [def method n(self):
        instance variable(s)
        statement(s)]
```

* 一个类可以拥有两种类型的数据成员: 类属性和实例属性

```python
# 实例方法中访问类属性
# 访问类属性, 必须使用类名前缀
class rect:
    l = 8
    b = 5
    def area(self):
        print(rect.l * rect.b)
```

## 实例

```python
class rect:
    l = 8
    b = 5
    # 你需要显示的指定 self 参数
    # 然而, 调用时你不需要传入该参数
    def rectarea(self):
        return rect.l * rect.b
r = rect() # 创建实例对象
print("Area of rectangle is ", r.rectarea())
```

### \_\_init\_\_() 方法

* `__init__()` 方法是创建一个实例后第一个被执行的方法, 且自动执行
* 它就像 C++ 和 Java 语言中用于执行初始化操作的构造器
* 实例被构造后, 才调用 `__init__()` 方法
* 定义 `__init__` 方法时, 如果有父类, 你必须显示的调用父类的 `__init__` 方法
* `__init__` 方法, 不要返回任何值, 不然会抛出 TypeError 异常

```python
class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def rectarea(self):
        return self.l * self.b
r = rect()
print("Area of rectangle is ", r.rectarea())
```

* 给 `__init__` 方法传参

```python
class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def rectarea(self):
        return self.l * self.b
r = rect(5, 8)
print('Area of rectangle is ', r.rectarea())
```

* 给 `__init__` 方法定义`默认值参数`

```python
class rect:
    def __init__(self,x=8, y=5):
        self.l = x
        self.b = y
    def rectarea(self):
        return self.l * self.b
r = rect()
s = rect(10,20)
print("Area of rectangle is ", r.rectarea())
print("Area of rectangle is ", s.rectarea())
```

* 实例的字符串描述: 实例的 `__str__` 方法被 `str()`函数和 `print` 语句调用

```python
class rect:
    def __init__(self, x,y):
        self.l = x
        self.b = y
    def __str__(self):
        return 'Length is %d, Breadth is %d' % (self.l, self.b)
    def rectarea(self):
        return self.l * self.b
r = rect(5, 8)
print(r)
print("Area of rectangle is ", r.rectarea())
```

## 类方法

* 类方法没有 `self` 参数, 接收一个 `class` 作为它的第一个参数, 称之为 `cls`
* 类方法通过`类对象`直接调用, 而不是`实例对象`
* 一个类方法通过使用 `@classmethod` 装饰器来定义.
* `装饰器`提供了一个方便的`方法`用于在`函数和类`中来`插入和修改代码`

```python
# 语法
@classmethod
def f(cls, parm1, parm2, . . .):
    body of the method
```

```python
class book:
    price = 100
    @classmethod
    def display(cls):
        print(cls.price)
    def show(self, x):
        self.price = x
        print(self.price)

b = book()
c = book()
book.display()
b.display()
b.show(200)
c.show(300)
```

## 静态方法

* 一个可代替的类方法实现
* 静态方法通过对普通函数使用 `@staticmethod` 装饰器创建
* 类方法和静态方法的不同点: 静态方法没有 `cls` 参数; 类方法会被继承, 静态方法却不会
* 静态方法可以通过类对象和实例对象调用

```python
@staticmethod
def name (parm. . .):
    body of the method
```

```python
class rect:
    @staticmethod
    def disp_message():
        l = 50
        print ("Length is ", l)
# 通过 类对象 调用
rect.disp_message()
r = rect()
# 通过 实例对象 调用
r.disp_message()
```

* `类方法`和`静态方法`都可以通过`类对象`和`实例对象`调用
* `实例方法`只能通过`实例对象`调用

```python
class product:
    count = 0
    def __init__(self, name):
        self.name=name
        product.count += 1
    @staticmethod
    def prodstatcount():
        return product.count
    @classmethod
    def prodclasscount(cls):
        print('Class info: ', cls)
        print('Class method - The product count is: ', cls.count)
p1 = product('Camera')
p2 = product('Cell')
print('Static method - The product count is: ',\
      product.prodstatcount(), p1.prodstatcount())
product.prodclasscount()
p2.prodclasscount()
```

垃圾回收
=======

```python
class rect:
    n = 0
    def __init__(self, x, y):
        rect.n += 1
        self.l = x 
        self.b = y
    def __del__(self):
        rect.n -= 1
        print(self.__class__.__name__, 'destroyed')
    def rectarea(self):
        print ('Area of rectangle is', self.l * self.b)
    def noOfObjects(self):
        print ('Number of objects are:', rect.n)

r=rect(3,5)
r.rectarea()
s=rect(5,8)
s.rectarea()
r.noOfObjects()
```

继承
===

* 子类继承了父类所有的属性和方法, 所以可以节省时间和精力

## 继承的分类

### 单继承

* 如果父类也有 `__init__` 方法, 子类的 `__init__` 方法必须调用

```python
class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def rectarea(self):
        return self.l * self.b
class triangle(rect):
    def __init__(self):
        # 调用父类的初始化方法
        rect.__init__(self)
        self.x = 17
        self.y = 13
    def trigarea(self):
        return 1/2 * self.x * self.y

r=triangle()
# 如果通过多态去调用父类的方法, 涉及到父类的属性, 父类的 __init__ 方法必须在子类的__init__ 方法中调用
print("Area of rectangle is ", r.rectarea())
print("Area of triangle is ", r.trigarea())
```

#### 访问控制指示符

* 用于标识类成员的可见性
* `public` : 类的外部和内部同样访问
* `private` : 类的外部不能访问, 一个 `private` 成员通过使用 `__` (双下划线)前缀定义, 并且不能以下划线结束
* 类外部访问 private 成员, 使用 `_类名`+`private成员名`

```python
# 访问 public 成员
class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def rectarea(self):
        return self.l * self.b
r = rect(5, 8)
print("Area of rectangle is ", r.rectarea())
print("Area of rectangle is ", r.l * r.b)
# 访问 private 成员
class rect:
    def __init__(self, x,y):
        self.__l = x
        self.__b = y
    def rectarea(self):
        return self.__l * self.__b
r=rect(5,8)
print ("Area of rectangle is ", r.rectarea())
# 类外部访问 private 成员, 使用 _类名+private成员
print ("Area of rectangle is ", r._rect__l * r._rect__b)
print ("Area of rectangle is ", r.__l* r.__b) # 抛出错误
```

* 一个子类可以访问父类的 `public` 成员变量和方法

#### 重写(override)

* 子类重写父类的方法, 先走子类的方法

```python
class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def area(self):
        return self.l * self.b
class triangle(rect):
    def __init__(self):
        rect.__init__(self)
        self.x = 17
        self.y = 13
    def area(self):
        return 1/2 * self.x * self.y
r=triangle()
print ("Area of triangle is ", r.area())
```

* 在子类中访问父类的方法

```python
class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def area(self):
        print("Area of rectangle is ", self.l * self.b)
class triangle(rect):
    def __init__(self):
        rect.__init__(self)
        self.x = 17
        self.y = 13
    def area(self):
        # 使用 类名 调用父类中方法
        rect.area(self)
        print("Area of triangle is ", 1/2 * self.x * self.y)
r = triangle()
r.area()
```

### 多层继承

* C 继承自 B, B 继承自 A, 这就是多层继承
* C 可以访问 B 中的 public 成员, B 可以访问 A 中的 public 成员
* 父类中的 public 成员在子类中也是 public 成员

```python
class worker:
    ...
class officer(worker):
    ...
class manager(officer):
    ...
```

```python
class worker:
    def __init__(self, c, n, s):
        self.code = c
        self.name = n
        self.salary = s
    def showworker(self):
        print("Code is ", self.code)
        print("Name is ", self.name)
        print("Salary is ", self.salary)
class officer(worker):
    def __init__(self, c, n, s):
        worker.__init__(self, c, n, s)
        self.hra = s * 60 / 100
    def showofficer(self):
        worker.showworker(self)
        print("HRA - House Rent Allowance is ", self.hra)
class manager(officer):
    def __init__(self, c, n, s):
        officer.__init__(self, c, n, s)
        self.da = s * 98 / 100
    def showmanager(self):
        officer.showofficer(self)
        print ("DA - Dearness Allowance is ", self.da)
w = worker(101, 'John' , 2000)
o = officer(102, 'David', 4000)
m = manager(103, 'Ben' , 5000)
print ("Information of worker is ")
w.showworker()
print ("\nInformation of officer is ")
o.showofficer()
print ("\nInformation of manager is ")
m.showmanager()
```

```python
class student:
    def __init__(self, r, n):
        self.roll = r
        self.name = n
    def showstudent(self):
        print("Roll : ", self.roll)
        print("Name is ", self.name)
class science(student):
    def __init__(self, r, n, p, c):
        student.__init__(self, r, n)
        self.physics = p
        self.chemistry = c
    def showscience(self):
        student.showstudent(self)
        print("Physics marks : ", self.physics)
        print("Chemistry marks : ", self.chemistry)
class arts(student):
    def __init__(self, r,n,h,g):
        student.__init__(self,r,n)
        self.history = h
        self.geography=g
    def showarts(self):
        student.showstudent(self)
        print("History marks : ", self.history)
        print("Geography marks : ", self.geography)
s = science(101, 'David', 65, 75)
a = arts(102, 'Ben', 70, 60)
print("Information of science student is ")
s.showscience()
print("\nInformation of arts student is ")
a.showarts()
```

### 多继承

* C 同时继承自 A 和 B, C 可以访问 A 和 B 中所有的 public 成员

```python
class worker:
    ...
class officer:
    ...
class manager(worker, officer):
    ...
```

```python
class student:
    def __init__(self, r, n):
        self.roll = r
        self.name = n
    def showstudent(self):
        print("Roll : ", self.roll)
        print("Name is ", self.name)
class science:
    def __init__(self, p, c):
        self.physics = p
        self.chemistry = c
    def showscience(self):
        print("Physics marks : ", self.physics)
        print("Chemistry marks : ", self.chemistry)
class results(student, science):
    def __init__(self, r, n, p, c):
        student.__init__(self, r, n)
        science.__init__(self, p, c)
        self.total = self.physics + self.chemistry
        self.percentage = self.total / 200 * 100
    def showresults(self):
        student.showstudent(self)
        science.showscience(self)
        print("Total marks : ", self.total)
        print("Percentage marks : ", self.percentage)
s = results(101, 'David', 65, 75)
print("Result of student is ")
s.showresults()
```

* `多继承`可能会产生`混乱`

#### 父类中存在名字和签名相同的方法

* 写在前面的类的方法将会被调用
* 如果我们都需要, 那我们就要`重写`父类方法后, 进行`主动调用`

```python
class rect:
    def __init__(self):
        self.l = 8
        self.b = 5
    def area(self):
        return self.l * self.b
class triangle:
    def __init__(self):
        self.x = 17
        self.y = 13
    def area(self):
        return 1/2 * self.x * self.y
class both(rect, triangle):
    pass
r = both()
print("Area of rectangle is ", r.area()) # 这里会调用 rect 的 area 方法
print(r.l, r.b, r.x, r.y); # 会抛出异常, 找不到 x 属性, 初步推断, triangle 的 __init__ 方法没有调用, 不提供子列的 __init__ 方法, 默认的 __init__ 方法会调用第一个父类的 __init__ 方法进行初始化
```

运算符重载
========

## + : \_\_add\_\_

```python
class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def __str__(self):
        return 'Length is %d, Breadth is %d' % (self.l, self.b)
    def __add__(self, other):
        return rect(self.l + other.l, self.b + other.b)
    def rectarea(self):
        return self.l * self.b
r1 = rect(5, 8)
r2 = rect(10, 20)
r3 = r1 + r2 # 通过实例 r1 调用其 __add__ 方法, r2 作为参数传入
print(r3)
print("Area of rectangle is ", r3.rectarea())
```

## == : \_\_eq\_\_

```python
class rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def __str__(self):
        return 'Length is %d, Breadth is %d' % (self.l, self.b)
    def __eq__(self, other):
        return ((self.l == other.l) and (self.b == other.b))
    def rectarea(self):
        return self.l * self.b
r1 = rect(5,8)
r2 = rect(10,20)
if r1 == r2: # 通过实例 r1 调用其 __eq__ 方法, r2 作为参数传入
    print('The two instances are equal')
else:
    print('The two instances are not equal')

r2 = rect(5,8)
if r1 == r2:
    print('The two instances are equal')
else:
    print('The two instances are not equal')
```

多态性
=====

* 相同名称和签名的方法在不同的类中执行不同的任务
* 你在不知道具体类的情况下, 通过多态调用对应的方法(不知道这个方法所属的具体类)

```python
class book:
    def __init__(self, x):
        self.price = x
class stockist(book):
    def __init__(self, x):
        book.__init__(self, x)
    def commission(self):
        self.comm = self.price * 5 / 100
        print("Commission of Stockist is %.2f" % self.comm)
class distributor(book):
    def __init__(self, x):
        book.__init__(self, x)
    def commission(self):
        self.comm = self.price * 8 / 100
        print("Commission of Distributor is %.2f" % self.comm)
class retailer(book):
    def __init__(self,x):
        book.__init__(self,x)
    def commission(self):
        self.comm = self.price * 10 / 100
        print("Commission of Retailer is %.2f" % self.comm)
r = stockist(100)
s = distributor(100)
t = retailer(100)
prncomm = [r, s, t]
for c in prncomm:
    c.commission()
```

Properties(属性)
===

* 用于管理实例变量, 提供 getter 和 setter

```python
class product(object):
    def __init__(self, name):
        self._name = name
    def set_name(self, name):
        print ('Setting product name: %s' % name)
        self._name = name
    def get_name(self):
        return self._name
    def del_name(self):
        del self._name
    # 属性声明
    name = property(get_name, set_name)
p = product('Camera')
print('Getting product name ', p.name)
p.name = 'Cell'
print('Getting product name ', p.name)
```

descriptor
==========

* `descriptor` 是 一个 `properties` 的超集
* `descriptor` 是 `类族`, 用来方便我们管理实例对象的实例变量

```python
# 常用方法
__set__() # 获得对象的实例变量值
__get__() # 设置对象的实例变量值
__delete__() # 删除对象的某个实例变量
```

```python
# descriptor 的语法
class Descriptor:
    def __get__(self, instance, owner):
        ...
    def __set__(self, instance, value):
        ...
    def __delete__(self, instance):
        ...
```

* 无数据的 descriptor: 针对`对象`只实现 `__get__` 方法
* 有数据的 descriptor: 针对`对象`同时实现 `__delete__` `__set__` `__get__`

```python
class product:
    def __init__(self, name, x = 5):
        self.name = name
        self.price = x
    def __set__(self, obj, value):
        print ('Setting attribute' , self.name, obj, value)
        self.price = value
    def __get__(self, obj, objtype):
        print ('Getting attribute',self.name, obj, objtype)
        return self.price
class cart:
    p = product('butter', 7)
k = cart()
print(k.p)
k.p = 10
print(k.p)
```

\_\_setattr\_\_ 、 \_\_getattr\_\_ 、 \_\_delattr\_\_
==================================

* 在给实例变量赋值时, `__setattr__` 方法会被调用

```python
def __setattr__(self, name, value):
    self.name = value
# 上面的赋值会导致无穷的递归调用 __setattr__ 方法
# 应该使用 __dict__ 字典来给赋值, 实现如下
def __setattr__(self, name, value):
    # 这里可以进行类型检查
    self.__dict__[name] = value
```

* `__getattr__` 方法使用字符串对象获取实例变量, 当属性搜索失败时, 会被调用, 比如当你访问一个未定义的属性. 这个方法应该要么返回实例变量值, 要么抛出属性访问错误异常

```python
def __getattr__(self, name):
    return self.name
```

* 当对一个实例的属性使用 `del` 时, `__delattr__` 方法会被调用

```python
def __delattr__(self, name):
    del self.name
```

```python
class product:
    # 类属性
    price = 25
    def __init__(self, name):
        self.name = name
    def __setattr__(self, name, value):
        print(name, '+')
        self.__dict__[name] = value
    def __getattr__(self, name):
        print(name, '-')
        return self.name
p = product('Camera')
print(p.price)
print(p.name)
p.price = 15
p.name = "Cell"
print(p.name)
print(p.price)
```

