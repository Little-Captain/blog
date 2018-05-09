Title: iOS 网络-NSURLConnection
Date: 2017-05-11 11:01:33
Category: iOS
Tags: iOS, 网络

作用
====

* 负责发送请求，建立客户端和服务器的连接
* 发送数据给服务器，并收集来自服务器的响应数据

常用相关类
=========

## NSURL

* 请求地址
* 有时必须进行百分号转码, 使用方法stringByAddingPercentEscapesUsingEncoding

## NSURLRequest

* 一个NSURLRequest对象就代表一个请求
* 包含的信息
    * 请求方法
    * 请求头
    * 请求体
    * NSURL对象
    * 请求超时
    * ...

## NSMutableURLRequest

* setTimeoutInterval
    * 超过这个时间就算超时，请求失败
    * 设置请求超时等待时间
* setHTTPMethod
    * 设置请求方法
    * GET或POST
* setHTTPBody
    * 设置请求体
* setValue:forHTTPHeaderField:
    * 设置请求头

使用步骤
=======

## 1. 创建一个NSURL对象
	
* 设置请求路径

## 2. 创建一个NSURLRequest对象
	
* 设置
    * NSURL对象
    * 请求头
    * 请求体

## 3. 发送请求

NSURLConnection常见的发送请求方法

## 同步请求

* sendSynchronousRequest

## 异步请求

### 根据对服务器返回数据的处理方式的不同，又可以分为2种

#### block回调

* sendAsynchronousRequest

#### 代理

* initWithRequest
    * 在startImmediately = NO的情况下，需要调用start方法开始发送请求
* connectionWithRequest
* 遵守NSURLConnectionDataDelegate协议
    * 才能成为代理
    * 而且这个代理是被强引用的
* 代理方法
    * didReceiveResponse : 开始接收到服务器的响应时调用
    * didReceiveData : 接收到服务器返回的数据时调用, 服务器返回的数据比较大时会调用多次
    * didFailWithError : 请求出错时调用, 比如请求超时
    * connectionDidFinishLoading : 服务器返回的数据完全接收完毕后调用


