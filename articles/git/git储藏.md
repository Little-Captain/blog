Title: git 储藏
Date: 2018-05-10 17:53:19
Category: git
Tags: git, 源代码管理

# what

* “‘储藏”“可以获取你工作目录的中间状态——也就是你修改过的被追踪的文件和暂存的变更——并将它保存到一个未完结变更的堆栈中，随时可以重新应用

# where 

* 当你在一个分支上工作到一半, 需要切换到另一个分支, 又不想做这种无意义的提交, 这就是储藏的使用场景

# how

```bash
# 储藏
git stash
# 列出所有储藏
git stash list
# 应用最新储藏
git stash apply
# 同时应用储藏暂存在 index 中的信息
git stash apply --index
# 移除储藏
git stash drop
# 应用后, 移除
git stash pop
```