Title: git 基本操作
Date: 2017-05-08 07:59:19
Category: git
Tags: git, 源代码管理

常用单命令操作
============

* `git init`: 初始化本地仓库
* `git status`: 查看文件状态
* `git add .`: 添加文件到暂缓区
* `git commit -m "注释"`: 从暂缓区提交文件到本地代码仓库
* `git tag -a '标签' -m "注释"`: 打标签

* `git tag`: 查看标签
* `git tag -d '标签名称'`: 删除标签
* `git remote add origin 远程仓库地址`: 给本地仓库添加远程仓库关联地址
* `git push origin master`: 上传本地代码到远程仓库
* `git push --tags`: 上传标签到远程仓库
* `git push origin :标签`: 从远程仓库删除标签

常用多命令操作
============

## 忽略已跟踪文件
* 如果某些文件已经被跟踪了， 再放入到.gitinore可能会失效
* 忽略: `git update-index --assume-unchanged filename`
* 撤销: `git update-index --no-assume-unchanged filename`
* 正确步骤
  * 将该文件从跟踪文件中移除: `git rm --cached 文件名`
  * 修改gitignore文件: 添加要被忽略的文件
  * `git add .`: 添加变化
  * `git commit`: 提交

