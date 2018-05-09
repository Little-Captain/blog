Title: Lean Python(Chapter 06)
Date: 2017-09-23 14:25:36
Category: Python
Tags: Lean Python

> Object Orientation

创建对象
======

## 类的定义

* 类是对象的模板

```python
from datetime import datetime

class person(object):
    "Person Class"
    def __init__(self, name, age, parent = None):
        self.name =name
        self.age = age
        self.created = datetime.today()
        self.parent = parent
        self.children = []
        print('Created', self.name, 'age', self.age)
    
    def setName(self, name):
        self.name = name
        print('Updated name', self.name)
        
    def setAge(self, age):
        self.age = age
        print('Update age', self.age)
        
    def addChild(self, name, age):
        child = person(name, age, parent = self)
        self.children.append(child)
        print(self.name, 'added child', child.name)
    
    def listChildren(self):
        if len(self.children) > 0:
            print(self.name, 'has children:')
            for c in self.children:
                print('  ', c.name)
        else:
            print(self.name, 'has no children')
    
    def getChildren(self):
        return self.children
```

```python
from people import person

joe = person('Joe Bloggs', 47)

print("Joe's age is ", joe.age)

print("Joe's full name is ", joe.name)

joe.addChild('Dick',7)
joe.addChild('Dora',9)

joe.listChildren()

joekids=joe.getChildren()

print("** Joe's attributes **")
print(vars(joe))

print("** Joe's Children **")
for j in joekids:
    print(j.name,'attributes')
    print(vars(j))
```

