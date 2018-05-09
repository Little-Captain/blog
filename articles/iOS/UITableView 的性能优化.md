Title: UITableView 的性能优化
Date: 2017-05-09 14:51:14
Category: iOS
Tags: iOS, UITableView, 性能优化

重要性
=====

UITableView 是 iOS 开发中最常使用的控件之一, 在各类 App 中都充斥着各种表格. 表格展示的内容如果比较多, 比较复杂, 往往会影响界面的刷新帧率, 在用户的角度就是界面卡顿, 这时必须对 UITableView 进行性能优化.

表格为什么会卡?
=============

iOS 设备的刷新帧率为 60Hz, 也就是一秒钟会有 60 帧图片绘制在屏幕上. 如果在下一帧图片绘制的时候, CPU正忙, 那么这一帧就会被跳过, 频繁出现这种情况, 界面就卡了.
总结: 在两帧之间运算没有做完, 就会出现跳帧

优化方向
=======

实施优化的准则: 测量(主要是使用Instrument看帧率), 而不是猜测

## 关于计算

* 尽量少计算, 所有需要的素材提前计算好!

## 关于圆角

* 控件上不要设置圆角半径, 所有图像渲染的属性, 都要注意!

## 关于创建控件

* 不要动态创建控件, 所有需要的控件, 都要提前创建好, 在显示的时候, 根据数据决定显示 / 隐藏

## 关于控件数量

* cell 中控件的层次越少越好, 数量越少越好!

## 行高一定要缓存

* 表格性能优化中最重要的一环
* 如果系统适配 iOS 8.0+, 推荐使用苹果的自动计算行高, 苹果本身的性能优化已经够好!

```objc
// 设置估算高度, 这个值可以尽量大一点儿, 太大苹果也会通过实际需要进行估算
self.tableView.estimatedRowHeight = 200;
// 设置自动尺寸
self.tableView.rowHeight = UITableViewAutomaticDimension;
```
* 如何缓存行高, 一般通过在 Model 中增加一个 cellHeight 属性, 在给 Model 设置数据时, 就可以计算了(因为 Model 唯一确定行高), 而且要控制器只计算一次. 如果采用 MVVM 模式, 就在 VM 中计算行高并缓存

```objc
- (CGFloat)cellHeight {
    
    if (!_cellHeight) { // 行高还没有计算的
        // 计算行高
    }
    
    return _cellHeight;
}
```

## 高级优化

* 离屏渲染, 启用异步绘制, 让视图在显示前尽量绘制好

```objc
self.layer.drawsAsynchronously = true
```

* 栅格化, 栅格化之后, 会生成一张独立的图像, cell在屏幕上滚动的时候, 本质上滚动的是这张图片

```objective-c
// 启动栅格化
self.layer.shouldRasterize = true
// 设置栅格化的比例, 不然界面显示比较模糊
self.layer.rasterizationScale = UIScreen.main.scale
```

* 如果检测到cell的性能已经很好, 就不需要再离屏渲染了
    * 离屏渲染需要在GPU / CPU 之间快速切换
    * 耗电厉害


