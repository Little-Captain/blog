Title: git 使用经验集锦
Date: 2017-07-31 15:39:05
Category: git
Tags: git, 源代码管理

[toc]

## 修改 Git 的默认编辑器

```bash
# 1. subl 是可以在终端中直接启动的一个文本编辑器
# 2. -w 的意思是: 让 git 等待文本编辑结束. 当用户编辑完成后, 关闭文本就表示结束
git config --global core.editor "subl -w"
```

