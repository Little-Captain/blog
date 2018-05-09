Title: nullable&nonnull
Date: 2017-05-08 20:35:18
Category: iOS
Tags: Swift, Objective-C, iOS

直面问题
=======

Swift 中有 optional 和 non-optional. 在 Objective-C 中没有这一概念.
那么在 Swift 和 Objective-C 混合编程的时候, 编译器会统一使用 non-optional 处理, 这样处理往往并不是我们想要的结果.

苹果的解决方案
============

## 引入三对关键字

* \_\_nullable 和 \_\_nonnull
* \_Nonnull 和 \_Nullable
* nonnull 和 nullable
* nonnull: 对象不应该为空
* nullable: 对象可以是 NULL 或 nil
* 三种写法本质上都是互通的，只是放的位置不同

## 使用总结

* nonnull 和 nullable: 属性、方法返回值、方法参数
* \_Nonnull 和 \_Nullable:  C 函数的参数、Block 的参数、Block 的返回值
* \_\_nonnull 和 \_\_nullable: 不建议使用, 用法和 \_Nonnull 和 \_Nullable 一样

## 减小指定的工作量

* 宏: NS\_ASSUME\_NONNULL\_BEGIN 和 NS\_ASSUME\_NONNULL\_END
* 作用: 在这两个宏之间的代码，所有简单指针对象(非多重指针)都被假定为 nonnull ，只需要去指定那些 nullable 指针对象

## 参考
[苹果官方Blog](https://developer.apple.com/swift/blog/?id=25)

