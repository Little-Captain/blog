Title: What is app thinning? (iOS, tvOS, watchOS)
Date: 2018-05-12 06:21:28
Category: Xcode
Tags: Xcode

> 本文章是总结自 Xcode 帮助文档

# 概述

* App Store 和操作系统优化 iOS, tvOS, watchOS 下的应用程序安装包. 
* 这种优化能让你的 App 使用几乎所有设备的特性, 并占用最小的磁盘空间.
* 优化主要有三方面: Slicing(iOS, tvOS), Bitcode, On-Demand Resources (iOS, tvOS)

# Slicing(iOS, tvOS) 二进制切片

* Apple 的设备CPU架构不知一种, 一般有armv7、armv7s、arm64.
* 上传至 App Store 的安装包包含armv7(兼容armv7s)和arm64两种架构. 这种安装包就是通用的安装包
* Apple 会根据, 设备的具体 CPU 架构切片生成对应的安装包
* 通过这样的操作安装包会变为通用包的一般大小
* 注意: 切片操作从 9.0 系统才开始支持

# Bitcode

* Bitcode 是编译程序的一种中间表示
* 如果你上传到 iTunes Connect 的 App 包含 bitcode, 这个 App 将在 App Store 中被重新编译链接. 这样的好处是, 这将允许 Apple 在未来重新优化你的 App 来适应一些新特性, 而不需要再次上传新版本到 App Store
* 对于 iOS, bitcode 默认开启, 但是可以关闭. watchOS 和 tvOS, bitcode 是必须的. 如果你提供 bitcode, 所有的 app 和 app 中的 framework(project 中所有的 target)都必须包含 bitcode!
* `注意`: 打开 bitcode 后, 相应的二进制文件一般会变大, 但是用户实际下载到的 app 安装包会小一点儿(这种变小远不如切片操作来得直接). 因为这种二进制文件只是上传给苹果的中间文件, 苹果会针对不同设备重编译的.

# On-Demand Resources (iOS, tvOS) (按需请求资源)

* 简单的讲就是应用内的资源文件被托管到 Apple 服务器上, 只有在用户真正需要相应的资源时, 才会去获取.
* 用户在即将进入某个页面, 请求这个页面的相应资源. 用户在购买内购项目后, 请求这个内购项目相关的资源.
* 在磁盘空间不足时, 操作系统会自动清除按需资源
* 如果你分发你的应用在 App Store 以外的其他地方, 你需要自己搭建按需请求资源服务















