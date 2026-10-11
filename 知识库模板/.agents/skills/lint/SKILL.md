---
name: lint
description: 只读检查通用知识库健康度，递归检测长期页面和专项的 frontmatter、目录 Schema、索引、断链、陈旧、重复、覆盖度和孤立页面。用户说“lint”“检查知识库”“健康检查”时使用。
---

# Lint

递归检查知识库并输出可执行问题清单。保持严格只读，不自动修复，不写操作日志。

## 只读边界

- 不创建、修改、移动或删除任何文件。
- 不创建或提交逐次操作日志。
- 不因发现旧结构而自动迁移页面。
- 如用户随后要求修复，将 lint 结果作为新任务的输入，另行获得写入授权，并按 `workflows/knowledge-base-change-policy.md` 区分普通知识修复与治理变更。

## 定位知识库

将包含 `_index/topic-map.md` 和 `workflows/knowledge-base-organization.md` 的最近祖先目录解析为 `KB_ROOT`。定位过程只读，不切分支、不拉取远程。

## 检查范围

- 递归检查 `architecture/`、`services/`、`modules/`、`infrastructure/`、`workflows/`、`concepts/` 和 `external/` 的正式长期页面。
- 递归检查 `initiatives/`；每个 `initiatives/<name>/README.md` 是专项入口，子页面由它导航。
- `_templates/`、`_index/`、`raw/` 和 `.agents/skills/` 使用各自规则，不套用正式页面 Schema。

## 检查项

### 1. Frontmatter 与目录 Schema

正式长期和专项页面必须包含 `title`、`repo`、`category`、`tags`、`created` 和 `updated`。检查 category 与顶层目录一致、状态值合法、日期使用 `YYYY-MM-DD`、tags 为数组，以及 frontmatter 后有一句话摘要。

### 2. 结构

- `architecture/` 根目录只允许 `README.md` 和可选的 `overview.md`；其他根目录正文报告为 `error`。
- 每个 `architecture/<scope>/` 必须使用 lowercase kebab-case，在 `architecture/README.md` 定义，并拥有本地 `README.md`。
- 每篇架构正文必须从 scope README 可达，并在 `_index/topic-map.md` 的对应 scope 分组中登记。
- 专项必须有 README，且只创建实际使用的子目录。
- 长期页面超过顶层目录下两层时报告为需评审，不自动判定错误。

### 3. 索引一致性

- 每个长期页面应能从 `_index/topic-map.md` 到达，纯目录入口 README 可由分类链接覆盖。
- 全局索引只列专项 README，专项子页面应从本地 README 到达。
- 索引标题和一句话摘要应与目标页一致。

### 4. 链接与来源

递归解析相对 Markdown 链接，报告不存在的目标、大小写错误和移动后残留链接。无法验证的代码或外部路径标记为 verification gap，不直接判定失效。检查 raw manifest 中的快照和编译目标是否存在。

### 5. 陈旧、覆盖、重复与脱敏

- 检查 `stale/archived` 状态与正文是否一致，但不只凭日期判定内容错误。
- 检查 coverage 与实际来源数量是否明显冲突。
- 检查标题、tags 和摘要高度相似的页面，建议收敛事实源。
- 搜索疑似凭据、密钥、连接串和个人敏感信息；只报告文件与行号，不在输出中重复完整敏感值。

### 6. Skill

- 对 `.agents/skills/*/` 运行可用的 Skill 结构校验器。
- 运行 `.agents/skills/lint/scripts/check-architecture-layout.sh "$KB_ROOT"`，将其失败项并入结构报告。

## 执行完整性

如位于 Git 仓库，在 lint 前后分别记录 `git status --short`；状态应一致。若发生变化，立即报告为工具或流程缺陷。

## 报告格式

| 严重度 | 含义 |
| --- | --- |
| `error` | 断链、必填 Schema 缺失、错误索引或入口不可达 |
| `warning` | 陈旧、覆盖不足、疑似重复、层级需评审或疑似敏感信息 |
| `info` | 合法兼容结构、可选优化和验证缺口 |

每项包含规则、文件、证据和最小修复建议。最后汇总扫描文件数、错误/警告数、未覆盖范围和建议的独立修复任务，不直接实施修复。
