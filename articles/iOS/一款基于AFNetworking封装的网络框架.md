Title: 一款基于 AFNetworking 封装的网络框架
Date: 2017-05-09 16:54:37
Category: iOS
Tags: iOS, Objective-C, 网络

[框架地址](https://github.com/Little-Captain/LCNetworking)

AFNetworking 存在的问题
=====================

如果你的项目中使用了 AFNetworking, 就一定会出现内存泄漏的问题. 这个是我在用做测试的时候发现的.

## 问题重现

* 安装 AFNetworking, 使用 AFNetworking 做网络请求
* 使用 Debug Memory Graph 查看内存引用关系

*Debug Memory Graph(Xcode 8.0+)*

![](../assets/images/LCNetworking/Debug Memory Graph.png)

*AFNetworing 的一些对象被 Xcode 标记*

![](../assets/images/LCNetworking/AFN的内存泄漏.png)

图上结果表示: 这些对象无法被释放, 即内存泄漏.

* 使用 Instrument 测试得到类似结果

解决问题
=======

失败的解决办法

* 控制器退出时, 取消所有任务
* 使用 weak strong dance
* ...

成功的解决办法

* 使用单例封装 AFNetworking, 实现自己的网络工具类.

*效果图*

![](../assets/images/LCNetworking/内存泄漏解决.png)

LCNetworking
============

## 特性

* 一款基于 AFNetworking 的框架
* 使用单例模式解决了 AFNetworking 的内存泄漏问题
* 与 AFNetworking 原有 API 完全兼容

## 增加 API

* 获取单例对象

```objc
+ (instancetype)sharedInstance;
```

* GET / POST

```objc
- (nullable NSURLSessionDataTask *)request:...;
```

* 上传文件方法

```objc
- (nullable NSURLSessionDataTask *)upload:...;
```

* 方法持续扩展维护中

