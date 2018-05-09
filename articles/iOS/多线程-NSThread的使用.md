Title: 多线程-NSThread的使用
Date: 2017-05-10 11:59:29
Category: iOS
Tags: 多线程, iOS, NSThread 

一个NSThread对象就代表一条线程

使用步骤
=======

## 1. 创建线程

* init
    * 具体使用: 自定义线程类继承自NSThread, 重写 main 方法(自定义任务、start 方法中会调用 main 方法)
* initWithTarget

## 2. 启动线程

* start
    * 必须要启动, 不然任务不会执行

相关方法
============

## 主线程相关

* mainThread : 获取主线程
* isMainThread : 类方法
* isMainThread : 对象方法

## 其他方法

* currentThread : 获取当前所在线程
* setName : 设置线程名
* name : 获取线程名

## 其他创建线程方式

* detachNewThreadSelector
    * 创建线程后自动启动线程
    * 分离出子线程

* performSelectorInBackground
    * 隐式创建并启动线程
    * 后台线程

* 2种创建线程方式的优缺点
    * 优点 : 简单快捷
    * 缺点 : 无法拿到线程对象, 无法对线程进行更详细的设置

控制线程状态
==========

## 启动线程

* start
* 进入就绪状态 -> 运行状态。当线程任务执行完毕，自动进入死亡状态

## 阻塞（暂停）线程

* sleepUntilDate
* sleepForTimeInterval

## 强制停止线程

* exit
* 进入死亡状态

## 注意

* 一旦线程停止（死亡）了，就不能再次开启任务

