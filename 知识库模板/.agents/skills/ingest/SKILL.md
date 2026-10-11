---
name: ingest
description: 从外部文档、代码仓库、会议记录、网页或本地文件编译通用知识库内容。用户说“ingest”“导入资料”“从这份材料生成知识库”，或一份原始来源需要归档并级联更新多个页面时使用。
---

# Ingest

将一个原始资料源保存为可追溯快照，再把其中的可验证主张编译到已有或新增页面。保持原始资料、专项过程和长期答案分层。

## 定位与写入门禁

将包含 `_index/topic-map.md` 和 `workflows/knowledge-base-organization.md` 的最近祖先目录解析为 `KB_ROOT`。读取这两个文件、`README.md` 和 `workflows/knowledge-base-change-policy.md`。如位于 Git 仓库，先检查已有改动并保留无关内容。未得到写入授权或无法唯一定位时停止写入。如任务扩大到 Skill、模板、Schema、目录治理或批量搬迁，改按治理变更路由。

## 核心不变量

- `raw/` 保存经授权和脱敏的原始证据，原则上不可变；来源更新时新建快照。
- `initiatives/` 保存经整理的专项上下文，不是 raw 的别名。
- 七个长期目录保存脱离当前资料和任务仍成立的答案。
- 一份来源可以更新多个页面，一个页面也可以引用多份来源。
- 导入资料与当前事实源冲突时，以当前事实源为准，并显式记录资料的时间或适用边界。

## 工作流

### 1. 识别来源与复制边界

记录来源类型、标题、URL 或路径、获取日期和权限边界。使用对应的只读工具读取外部资料。不把访问凭据、token、受限整篇原文或不必要的个人信息写入仓库。

### 2. 保存 raw 快照

| 来源 | 目录 |
| --- | --- |
| 外部或本地文档 | `raw/documents/` |
| 代码分析输出 | `raw/code-analysis/` |
| 会议记录 | `raw/meetings/` |
| 网页、对话或其他 | `raw/other/` |

使用带日期的 lowercase kebab-case 文件名和 `_templates/raw-snapshot.md`。更新 `raw/_manifest.md`，记录来源、快照、脱敏说明和编译目标。

### 3. 建立编译计划

从来源中列出可验证主张，并为每项选择目标：长期页面、专项页面，或只保留 raw。先读全局索引并递归搜索已有内容，优先原地更新，不做无关目录迁移。命中架构内容时先读 `architecture/README.md` 和所属 scope README；架构根目录除 `README.md` / `overview.md` 外不接受正文。

### 4. 验证并编译

- 对实现主张核对当前代码、配置和测试。
- 对运行时主张使用授权范围内的只读查询，记录环境和时间。
- 无法验证的内容标注为“来源主张”或“待验证”，不写成当前事实。
- 普通页面使用 `_templates/wiki.md`，专项入口使用 `_templates/initiative-readme.md`。
- 架构正文使用 `_templates/architecture.md`，选择唯一 scope 后写入 `architecture/<scope>/<page>.md`，并同步 scope README 和 topic map 对应分组。
- 任务型调研、未冻结设计和交付状态进入 `initiatives/`，不编译为长期架构事实。

### 5. 级联导航

更新全局索引、专项本地索引、架构 scope README 和 raw manifest。多个页面共享结论时选择一个事实源，其他页面只摘要并链接。

### 6. 校验

检查 frontmatter、相对链接、manifest、索引和敏感信息；写入审计由 Git commit/MR 承担，不创建或提交逐次操作日志。运行 `.agents/skills/lint/scripts/check-architecture-layout.sh "$KB_ROOT"`，如使用 Git，再运行 `git diff --check` 和 `git status --short`。

## 输出

报告 raw 快照位置、编译或更新的页面、稳定/专项分流、验证结果、脱敏处理、覆盖度、未验证项，以及本地修改/提交/发布的各自状态。
