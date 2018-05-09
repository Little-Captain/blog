Title: ipa 包中的 PNG 文件的正常化
Date: 2017-06-29 12:34:24
Category: iOS
Tags: 文件处理, iOS

# 问题描述

* 将`图片`拖入 `iOS 工程`后, `Xcode` 会对其进行`特殊处理`, 导致图片能在 Apple 相关系统上正常显示, 其他系统都不能正常显示. 
* 之所以能在 Apple 相关系统上正常显示是因为苹果的底层方法实现就做了相应处理.

# 问题解决

* `通过苹果的方法把这些特殊图片读入系统, 然后重新保存为 PNG 图片即可`.

将这段代码加入你的 `Mac 控制台工程`, 生成一个可执行程序(如 ipaPNGnormalizer), 在命令行中使用即可, `第一个参数`为需要正常化处理的 `PNG 文件夹路径`. 处理后会在这个目录下创建一个 decode 文件夹, 这个文件夹下存放所有的正常化后的 PNG 图片

``` objc
#import <Foundation/Foundation.h>
#import <Cocoa/Cocoa.h>

#define NSLog(FORMAT, ...) printf("%s\n", [[NSString stringWithFormat:FORMAT, ##__VA_ARGS__] UTF8String])

BOOL saveImage(NSImage *image, NSString *path);

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        
        if (argc < 2) {
            NSLog(@"请输入包含待处理的 PNG 图片的路径");
            return 0;
        }
        
        NSString *fileRootPath = [NSString stringWithCString:argv[1] encoding:NSUTF8StringEncoding];
        
        NSURL *diskCacheURL = [NSURL fileURLWithPath:fileRootPath isDirectory:YES];
        NSArray *resourceKeys = @[NSURLIsDirectoryKey, NSURLNameKey];
        
        // This enumerator prefetches useful properties for our cache files.
        NSDirectoryEnumerator *fileEnumerator = [[NSFileManager defaultManager] enumeratorAtURL:diskCacheURL
                                                                     includingPropertiesForKeys:resourceKeys
                                                                                        options:NSDirectoryEnumerationSkipsHiddenFiles
                                                                        errorHandler:NULL];
        
        NSString *decodeFileRootPath = [fileRootPath stringByAppendingPathComponent:@"decode"];
        
        [[NSFileManager defaultManager] createDirectoryAtPath:decodeFileRootPath
                                  withIntermediateDirectories:YES
                                                   attributes:nil
                                                        error:NULL];
        // 统计 png 图片
        NSMutableArray *allFiles = [NSMutableArray array];
        for (NSURL *fileURL in fileEnumerator) {
            
            NSDictionary *resourceValues = [fileURL resourceValuesForKeys:resourceKeys error:NULL];
            
            if ([resourceValues[NSURLIsDirectoryKey] boolValue]) {
                continue;
            }
            NSString *fileName = resourceValues[NSURLNameKey];
            if (![[fileName pathExtension] isEqualToString:@"png"]) {
                continue;
            }
            [allFiles addObject:fileName];
        }
        NSLog(@"共有 %zd 张 PNG 图片", allFiles.count);
        
        NSUInteger count = 0;
        for (NSString *fileName in allFiles) {
            NSString *originFilePath = [fileRootPath stringByAppendingPathComponent:fileName];
            NSString *decodeFilePath = [decodeFileRootPath stringByAppendingPathComponent:fileName];
            NSImage *image = [[NSImage alloc] initWithContentsOfFile:originFilePath];
            if (saveImage(image, decodeFilePath)) {
                ++count;
                NSLog(@"进度 - %.2f%%", 100.0 * count / allFiles.count);
            }
        }
        
        NSLog(@"共转换 %zd 张图片", count);
    }
    return 0;
}

BOOL saveImage(NSImage *image, NSString *path) {

    [image lockFocus];
    NSBitmapImageRep *bits = [[NSBitmapImageRep alloc]initWithFocusedViewRect:NSMakeRect(0, 0, image.size.width, image.size.height)];
    [image unlockFocus];

    NSDictionary *imageProps = [NSDictionary dictionaryWithObject:[NSNumber numberWithFloat:1.0] forKey:NSImageCompressionFactor];

    NSData *imageData = [bits representationUsingType:NSPNGFileType properties:imageProps];

    return [imageData writeToFile:path atomically:YES];
}
```

# 完善

* 同时集成正常化和压缩处理, 新建一个 shell 脚本文件(如 pngNormalizer.sh), 加入如下代码

``` bash
# /bin/bash

ipaPNGnormalizer ./
zip -r decode decode/
```

* 将这个脚本文件放入包含需要正常化的 PNG 的文件中, 然后在终端输入如下命令

``` bash
./pngNormalizer.sh
``` 

* 至此任务完成, 将 `decode.zip` 拷给其他小伙伴就可以了


