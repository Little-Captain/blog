Title: 多线程-iOS中的实现方案
Date: 2017-05-09 18:03:27
Category: iOS
Tags: 多线程, iOS

| 方案 | 简介 | 语言 | 线程生命周期 | 使用频率 |
| --- | --- | --- | --- | --- |
| pthread | 一套通用的多线程API<br>适用于Unix/Linux/Windows等系统<br>跨平台/可移植<br>使用难度大 | C | 程序员管理 | 几乎不用 |
| NSThread | 使用更加面向对象<br>简单易用，可直接操作线程对象 | OC | 程序员管理 | 偶尔使用 |
| GCD | 旨在替代NSThread等线程技术<br>充分利用设备的多核 | C | 自动管理 | 经常使用 |
| NSOperation | 基于GCD（底层是GCD）<br>比GCD多了一些更简单实用的功能<br>使用更加面向对象 | OC | 自动管理 | 经常使用 |

