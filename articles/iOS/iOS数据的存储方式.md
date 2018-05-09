Title: iOS 数据的存储方式
Date: 2017-05-12 10:43:15
Category: iOS
Tags: iOS, 数据持久化

沙盒(磁盘)
=========

## 沙盒简介

* 每个iOS应用程序都有自己的应用沙盒
* 应用沙盒就是文件系统目录,  与其它文件系统隔离
* 应用必须待在自己的沙盒里, 其它应用不能访问该沙盒

## 沙盒的访问

* NSHomeDirectory() : 沙盒的根目录
* Documents
    * 保存应用运行时生成的需要持久化的数据
    * iTunes同步设备时会备份该目录
    * 不允许放缓存大数据
* Library/Caches
    * 保存应用运行时生成的需要持久化的数据
    * iTunes同步设备时不会备份该目录
    * 一般存储体积大、不需要备份的缓存数据
* Library/Preference
    * 保存应用的所有偏好设置
    * iOS的Settings(设置)应用会在该目录中查找应用的设置信息
    * iTunes同步设备时会备份该目录
* tmp
    * 保存应用运行时所需的临时数据
    * 使用完毕后再将相应的文件从该目录删除
    * 应用没有运行时，系统也可能会清除该目录下的文件
    * iTunes同步设备时不会备份该目录

## 应用程序包

* 包含了所有的资源文件和可执行文件
* [NSBundle mainBundle]
    * 获取应用程序包路径
    * 代表 App 本身
* 注意和沙盒做区分

偏好设置
=======

* 小数据
* 保存用户名、密码(MD5)、是否自动登录、字体大小等设置
* NSUserDefaults 实例，通过它来存取偏好设置
* 实质上它是保存在 Library/Preference 中的 plist 文件
* 注意 : UserDefaults 设置数据时，不是立即写入，而是根据时间戳定时地把缓存中的数据写入本地磁盘。所以调用了 set 方法之后数据有可能还没有写入磁盘应用程序就终止了。可以通过调用 synchornize 方法强制立即写入

归档
====

* 整存整取
* 保存自定义对象
* Foundation框架中的基本数据类型遵守了NSCoding协议可以直接用NSKeyedArchiver进行归档和NSKeyedUnarchiver进行解档

## NSCoding 协议

* encodeWithCoder
    * 每次归档对象时，都会调用这个方法
    * 使用encodeObject:forKey:方法归档实例变量
    * 注意调用父类的方法
* initWithCoder
    * 每次从文件中解档对象时，都会调用这个方法
    * 使用decodeObject:forKey方法解码实例变量
    * 注意调用父类的方法

## 扩展

* initWithCoder
    * 初始化解析xib的时候调用
* awakeFromNib
    * 已经从xib中加载完毕时调用

plist
=====

* 小数据
* XML格式
* 属性列表
* 不能存储对象

json
====

* json 文件的序列化和反序列化

数据库
=====

## FMDB

* 大数据
* SQLite3 C代码的OC封装

## CoreData

* 大数据
* 封装SQLite3
* 重量级框架

钥匙串访问
========

* 小数据
* 自动加密
* 存储在系统的钥匙串中, 不随应用的删除而删除
* 第三方框架 : SSKeychain

