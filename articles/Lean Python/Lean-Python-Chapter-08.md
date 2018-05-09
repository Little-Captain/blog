Title: Lean Python(Chapter 08)
Date: 2017-09-23 16:42:57
Category: Lean Python
Tags: Python

> Testing Your Code

模块化编程与代码测试
=================

* 模块化编程是测试更为容易

测试驱动的开发(TDD)
============

> 1. 开发代码前先写测试
> 2. 运行测试, 观察失败, 然后添加和修正代码, 使测试通过
> 3. 当测试通过后, 寻求改进代码设计的机会

* 对于大型项目, TDD 能够最好的模块化你的代码

单元测试框架 : unittest
=====================

```python
def calc(a, op, b):
    if op not in '+-/*':
        return None, 'Operator must be +-/*'
    try:
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '/':
            result = a / b
        else:
            result = a * b
    except Exception as e:
        return None,e.__class__.__name__
    return result,str(result)
```

```python
import unittest
import calc

class testCalc(unittest.TestCase):
    
    def testSimpleAdd(self):
        result, msg = calc.calc(1, '+', 1)
        self.assertEqual(result, 2.0)
    
    def testLargeProduct(self):
        result, msg = calc.calc(123456789.0, '*', 987654321.0)
        self.assertEqual(result, 1.2193263111263526e+17)
        
    def testDivByZero(self):
        result, msg = calc.calc(6, '/', 0.0)
        self.assertEqual(msg, 'ZeroDivisionError')

# 创建 test suite
TestSuite = unittest.TestSuite()
# 添加 test 到 suite 中
TestSuite.addTest(testCalc("testSimpleAdd"))
TestSuite.addTest(testCalc("testLargeProduct"))
TestSuite.addTest(testCalc("testDivByZero"))
# 创建 Test runner
runner = unittest.TextTestRunner()
# 执行测试
runner.run(TestSuite)
```

