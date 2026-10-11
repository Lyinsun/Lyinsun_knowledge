---
title: "架构文档范围导航"
repo: "knowledge-base"
category: "architecture"
tags: ["architecture", "navigation", "governance"]
created: "2026-08-10"
updated: "2026-08-11"
status: "active"
---

架构文档按稳定的系统或业务范围组织；本模板不预置任何具体业务分类。

## 范围定义

创建架构正文前，先在下表定义唯一 scope。每个 scope 使用 `architecture/<scope>/`，并从 [`_templates/architecture-scope-readme.md`](../_templates/architecture-scope-readme.md) 创建本地导航。

| 范围 | 目录 | 覆盖内容 |
| --- | --- | --- |
| `<scope-name>` | `<scope-name>/` | <说明该范围的稳定边界> |

## 根目录门禁

`architecture/` 根目录只允许：

- `README.md`：范围定义和导航；
- `overview.md`：可选的跨范围系统总览。

其他正文必须写入 `architecture/<scope>/<page>.md`。无法归类时应先评审 scope 边界，不创建 `misc/`、`others/` 或例外清单。

## 规则

- 范围名和路径使用 lowercase kebab-case。
- 每个 scope 必须有 `README.md`，说明稳定边界并导航范围内页面。
- 架构页同时从 scope README 和 `_index/topic-map.md` 的对应分组可达。
- scope 内只在同类页面形成稳定集合时再增加一层子目录，并为新目录创建 README。
- 面向单个任务的调研、未冻结设计、交付和状态进入 `initiatives/`。
- 迁移旧页面时同步更新 scope README、全局索引、raw manifest、专项导航和已知反向链接。

## 资源导航

- [全局索引](../_index/topic-map.md)
- [知识库目录与内容分层规范](../workflows/knowledge-base-organization.md)
- [专项目录](../initiatives/README.md)
