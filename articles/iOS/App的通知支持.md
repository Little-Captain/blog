Title: App 的通知支持
Date: 2017-09-13 16:45:19
Category: iOS
Tags: iOS, 推送通知

请求用户授权
==========

```objc
UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
[center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert + UNAuthorizationOptionSound)
   completionHandler:^(BOOL granted, NSError * _Nullable error) {
      // 通过授权结果完成进一步操作
}];
```

* 获取准确的用户授权信息使用 `UNUserNotificationCenter` 对象的 `getNotificationSettingsWithCompletionHandler:` 方法

配置类别和可操作的通知
==================

## 针对 App 注册通知类别

```objc
UNNotificationCategory* generalCategory = [UNNotificationCategory
     categoryWithIdentifier:@"GENERAL"
     actions:@[]
     intentIdentifiers:@[]
     options:UNNotificationCategoryOptionCustomDismissAction];
 
// 注册通知类别
UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
[center setNotificationCategories:[NSSet setWithObjects:generalCategory, nil]];
```

## 将自定义操作添加到类别中

```objc
UNNotificationCategory* generalCategory = [UNNotificationCategory
      categoryWithIdentifier:@"GENERAL"
      actions:@[]
      intentIdentifiers:@[]
      options:UNNotificationCategoryOptionCustomDismissAction];
 
// 创建自定义操作
UNNotificationAction* snoozeAction = [UNNotificationAction
      actionWithIdentifier:@"SNOOZE_ACTION"
      title:@"Snooze"
      options:UNNotificationActionOptionNone];
 
UNNotificationAction* stopAction = [UNNotificationAction
      actionWithIdentifier:@"STOP_ACTION"
      title:@"Stop"
      options:UNNotificationActionOptionForeground];
 
// 创建带有自定义操作的通知类别
UNNotificationCategory* expiredCategory = [UNNotificationCategory
      categoryWithIdentifier:@"TIMER_EXPIRED"
      actions:@[snoozeAction, stopAction]
      intentIdentifiers:@[]
      options:UNNotificationCategoryOptionNone];
 
// 注册通知类别
UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
[center setNotificationCategories:[NSSet setWithObjects:generalCategory, expiredCategory,
      nil]];
```

## 获取 App 的通知设置

* 用户可以随时在系统设置中改变应用的通知设置
* 通过使用 `UNUserNotificationCenter` 对象的 `getNotificationSettingsWithCompletionHandler:` 方法获取包含当前`授权状态`和`通知环境`的 `UNNotificationSettings` 对象

# 管理已被递送的通知

* 已被递送的通知没有被 App 或用户及时处理, 它们会一直显示在通知中心.
* 使用 `UNUserNotificationCenter` 对象的 `getDeliveredNotificationsWithCompletionHandler:` 方法`获取`在通知中心显示的`通知列表`
* 如果发现通知中心的通知已经过时, 可以使用 `removeDeliveredNotificationsWithIdentifiers:` 方法移除它们

