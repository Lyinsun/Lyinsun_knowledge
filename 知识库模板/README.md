# 通用知识库模板

这是一个可直接复制的纯知识库骨架，只包含目录、模板、维护规范和 Agent Skills，不包含任何真实业务页面、原始资料或仓库信息。

## 设计原则

- **索引优先**：Agent 查询时第一个读取 [`_index/topic-map.md`](_index/topic-map.md)。
- **事实源优先**：文档记录结论、边界和入口；实现细节以当前代码、配置、数据或权威来源为准。
- **分层存储**：稳定知识、专项上下文和原始证据分开保存。
- **范围导航**：架构正文先选择稳定 scope，再通过 scope README 和全局索引双重导航。
- **渐进积累**：优先更新已有页面，不为目录整齐批量搬迁历史文档。
- **可追溯**：结论链接到精确的代码路径、`raw/` 快照或外部来源。
- **三段式结构**：正文统一遵循“1. 全景状态图（实/虚线与色块） + 2. 能力演进与子文档路由表 + 3. 详细技术正文”，人类看图表抓重点，AI看正文抓细节。
- **可迁移**：活动文档、模板、脚本和配置只使用相对路径或运行时自定位，不写死个人/机器相关的绝对路径。
- **隐私优先**：不保存凭据、个人敏感信息、受限原文或无关对话噪声。

## 目录结构

```text
.
├── AGENTS.md                   # Agent 工作约定
├── .agents/skills/              # 知识库 Skills
├── _index/topic-map.md          # 全局索引，查询第一入口
├── _templates/                  # 正式页面与专项模板
├── architecture/                # 系统结构；正文按 <scope>/ 组织
├── services/                    # 仓库、服务、应用和对外接口
├── modules/                     # 稳定的业务或功能模块
├── infrastructure/              # 存储、消息、配置、可观测性等基础设施
├── workflows/                   # 开发、发布、运维、排障与治理流程
├── concepts/                    # 术语、规则、枚举与状态机
├── external/                    # 外部资源导航
├── initiatives/                 # 有明确目标和结束条件的专项
└── raw/                         # 原始证据快照与编译映射
```

## 内容分层

| 层级 | 位置 | 判断问题 |
| --- | --- | --- |
| 长期知识 | 七个长期目录 | 脱离当前任务后，结论是否仍应被直接查询？ |
| 专项知识 | `initiatives/<name>/` | 内容是否只服务于一个有明确起止的专项？ |
| 原始证据 | `raw/` | 是否需要保留原貌，以便复核或重新编译？ |

完整规则见 [`workflows/knowledge-base-organization.md`](workflows/knowledge-base-organization.md)。

## 架构范围

架构正文使用 `architecture/<scope>/<page>.md`。每个 scope 表示一个稳定的系统或业务边界，必须在 [`architecture/README.md`](architecture/README.md) 中定义，并拥有自己的 `README.md` 作为本地索引。`architecture/` 根目录只保留范围导航和可选的跨范围总览。

## Skills

| Skill | 用途 | 写入文件 |
| --- | --- | --- |
| `$query` | 按索引查询并给出证据链 | 否 |
| `$lint` | 检查 Schema、索引、链接、重复和覆盖度 | 否 |
| `$add-wiki` | 创建或更新少量知识页面 | 是 |
| `$digest` | 将已解决的对话或实践经验提炼为知识 | 是 |
| `$ingest` | 将原始资料快照编译为一个或多个页面 | 是 |

Skills 位于 `.agents/skills/`。如果使用的 Agent 运行时约定了其他发现路径，请按该运行时的规则映射这些目录，不要维护多份不同步副本。

## 变更与发布

[`workflows/knowledge-base-change-policy.md`](workflows/knowledge-base-change-policy.md) 将小范围知识写入与治理变更分开，并把治理变更按是否影响本仓之外的行为再分两类：目录、模板、Schema、配色和索引重组属仓内治理，与普通知识同路由；Agent 规则、Skill、验证脚本、发布自动化和批量移动删除属跨边界治理，默认独立审查。采用仓库应配置目标分支，未配置时使用仓库默认分支；已授权的修改型任务从干净且已快进到远端最新状态的目标分支基线开始，不假设分支名为 `master`。只有显式执行已批准的实施计划时，才进入“实现 → 测试 → 修复 → 回归”循环；这不是五个知识库 Skill 的默认行为。本模板不默认授权 Git 提交、推送、评审或自动发布。

## 开始使用

1. 复制整个目录到新知识库。
2. 创建架构页前，在 [`architecture/README.md`](architecture/README.md) 定义 scope，并从 `_templates/architecture-scope-readme.md` 创建 scope README。
3. 创建新页面时，严格参考 `_templates/` 对应模板（方案使用 `initiative-readme.md`，架构使用 `architecture.md`，原始快照使用 `raw-snapshot.md`，模块使用 `module.md`，通用 Wiki 使用 `wiki.md`，架构范围导航使用 `architecture-scope-readme.md`），并保持统一的“图-表-文”三段式正文结构。
4. 将新长期页面或专项 `README.md` 登记到 `_index/topic-map.md`。
5. 完成结构、链接和敏感信息校验；写入审计由 Git commit/MR 承担，不创建或提交逐次操作日志。
6. 在仓库级规则中明确目标分支和发布方式；修改型任务按变更策略准备最新基线，提交或发布权限不从本模板推断。
