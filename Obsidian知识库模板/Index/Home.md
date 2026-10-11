---
title: "知识库主页"
date: 2026-08-23
tags: [index, home]
status: active
domain: Knowledge-Management
aliases: [Home]
---

# 知识库主页

从收件箱开始收集；从项目、领域、资源保留上下文；从知识卡和问答记录沉淀可复用理解。

| 分类 | 入口 |
| --- | --- |
| 收件箱 | [[00-Inbox]] |
| 项目 | [[MOC-Projects]] |
| 知识 | [[MOC-Knowledge]] |
| 问答 | [[MOC-QA]] |

## 最近更新

```dataview
table date as "日期", status as "状态"
from ""
where !contains(file.path, "Index") and !contains(file.path, "99-Templates")
sort date desc
limit 15
```
