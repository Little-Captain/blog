Title: Block 总结
Date: 2017-05-06 12:37:40
Category: iOS
Tags: iOS, Objective-C

## 基本概念

* Block 即`带有`自动变量(`局部变量`)的`匿名函数`
* Block `提供`了类似由 C++ 和 Objective-C 类生成实例或对象来`保持变量值的能力`
* Block 其实就是一个`代码块`，把你想要执行的代码封装在这个代码块里，等到需要的时候再去调用
* Block 是 `OC 对象`. OC 对象? 好像不对? Block 不是函数指针吗? 如果 Block 是函数指针, 那么还有必要把 Block 从栈区拷贝到堆区吗? 还能使用 copy 关键字修饰 Block 属性吗? 用事实说话好吧!

```objc
// 通过使用 OC 运行时机制, 打印出 全局 Block 的继承链
- (void)testGetClassInheritChain {
    
    void (^testBlock)(void) = ^{
        NSLog(@"testBlock");
    };
    
    NSLog(@"%@", [[testBlock class] lc_classInheritChain]);
}
// 打印结果: __NSGlobalBlock__ -> __NSGlobalBlock -> NSBlock -> NSObject
```

* [源码地址](https://github.com/Little-Captain/LCRuntimeTool)

## Block 属性的修饰 (copy, strong, retain, assign)

* Block 本身就是`对象`, 所以可以 `retain` 和 `release`
* Block 在`创建的时候`，它的内存是分配在`栈`(stack)上，而不是在堆(heap)上
* Block 的作于域是属于创建时的作用域，一旦在创建时候的`作用域外`面`调用`这个 Block 将导致`程序崩溃`
* 使用 retain/strong 可以，但是 Block 的 `retain/strong 行为和用 copy 的行为是一样的`, 即将 Block 从栈上拷贝(copy)到堆中, 所以`一般直接使用 copy`

## __block 关键字

* 在 Block 的 {} 体内，是不可以对外面的变量进行更改的, 使用 __block 就能改变 Block 块中变量的值. 不使用 __block 时, 是值捕获; 使用 __block 时, 是地址捕获. 

## __block 和 __weak

* `__block` 不管是 `ARC` 还是 `MRC `模式下都可以使用，可以修饰`对象`，还可以修饰`基本数据类型`
* `__weak` 只能在 `ARC` 模式下使用，也只能修饰`对象`，不能修饰基本数据类型
* `__block 对象`可以在 Block 中被`重新赋值`，`__weak 不可以`

## 使用 Block 传递数据

* 在`数据发送对象`中`定义 Block 属性`
* 在`数据接收对象`中给 Block 赋值, Block 中写具体要做得事情
* 在`数据发送对象`内部调用这个 Block , 就可以把`数据通过 Block 的参数传递`给`数据接收对象`
* 这个过程其实就是`代理设计模式`所描述的过程. 

## Block 使用注意

* `Block `当做参数传递, 如果外界传入的值为`nil`, 直接`调用`会`崩溃`
* Block 引入`循环引用`
    * `堆中 Block 访问了外界对象`, 会对对象进行` retain 操作`, 这时可以`给对象加__block`, 就不会 retain
    * `堆中 Block`会`对`里面的`强指针强引用`, 这很`容易造成循环引用`, 可以用个`中间变量`保存想用的对象, 并加上`__weak`, 也可`消除循环引用`. 即 `weak strong dance`


