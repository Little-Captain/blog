Title: iOS 监测网络状态
Date: 2017-05-11 14:02:54
Category: iOS
Tags: iOS, 网络

为什么要监听
==========

* 让用户了解自己的网络状态，防止一些误会, 怪应用无能
* 根据用户的网络状态进行智能处理，节省用户流量，提高用户体验
    * WIFI\3G网络：自动下载高清图片
    * 低速网络：只下载缩略图
    * 没有网络：只显示离线的缓存数据

监测网络状态
==========

* 在网络应用中，需要对用户设备的网络状态进行实时监控
* 苹果官方提供了一个叫Reachability的示例程序，便于开发者检测网络状态

[地址](https://developer.apple.com/library/ios/samplecode/Reachability/Reachability.zip)

* 使用步骤
    * 添加框架SystemConfiguration.framework
    * 添加源代码(Reachability.h 和 Reachability.m)
    * 包含头文件(Reachability.h)
* 实际开发中一般都使用AFNetworking监测
  

