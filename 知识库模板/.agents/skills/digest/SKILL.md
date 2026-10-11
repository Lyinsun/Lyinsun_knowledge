---
name: digest
description: 将已经解决的对话、排障或开发经验提炼为通用知识库内容。用户说“digest”“消化”“沉淀这次经验”，或任务结束后需要保存结论、踩坑、决策和边界时使用。
---

# Digest

把对话中的可复用经验变成可查询、可追溯的知识，不把聊天流水或未验证猜测伪装成稳定结论。

## 定位与写入门禁

将包含 `_index/topic-map.md` 和 `workflows/knowledge-base-organization.md` 的最近祖先目录解析为 `KB_ROOT`。读取这两个文件、`README.md` 和 `workflows/knowledge-base-change-policy.md`。如位于 Git 仓库，先检查已有改动并保留无关内容。未得到写入授权或无法唯一定位时停止写入。如任务扩大到 Skill、模板、Schema、目录治理或批量搬迁，改按治理变更路由。

## 值得沉淀的内容

- 已验证的根因、关键链路、接口契约和恢复步骤。
- 已尝试但失败的方案，以及可复用的失败原因。
- 有明确取舍的设计决策、适用边界和残余风险。
- 以后查询时能减少重复阅读或排障的入口信息。

临时命令输出、凭据、个人敏感信息、未验证猜测和只对当前会话有意义的过程噪声不进入知识库。

## 路由规则

| 提取结果 | 位置 |
| --- | --- |
| 脱离当前任务仍成立 | 七个长期目录，优先更新已有页面 |
| 只服务于一个有明确起止的专项 | `initiatives/<name>/`，由专项 README 导航 |
| 对话原貌对追溯必不可少 | `raw/other/YYYY-MM-DD_<slug>.md`，登记 manifest |

架构类稳定结论先读 `architecture/README.md`，选择唯一 scope，写入 `architecture/<scope>/<page>.md`，并同时更新 scope README 与 topic map 对应分组。未冻结设计、调研和状态仍进入 `initiatives/`。

## 工作流

1. **提炼而非转录**：按“问题 → 结论 → 依据 → 失败尝试 → 适用边界 → 后续动作”整理，区分事实、推断和未验证信息。
2. **查重与定位**：先读全局索引，再递归搜索长期目录与 `initiatives/`；命中专项时先读 README。
3. **按需保存对话快照**：只有原话、时间顺序或完整上下文对复核有价值时才创建 raw；先删除凭据、个人信息和无关内容。
4. **更新知识**：普通页面使用 `_templates/wiki.md`，架构页使用 `_templates/architecture.md`，专项入口使用 `_templates/initiative-readme.md`。专项形成稳定结论时更新长期页面，用链接代替重复正文。
5. **更新导航**：按内容路由更新全局/本地索引、scope README 和 raw manifest。
6. **校验**：检查 frontmatter、相对链接、索引、来源和敏感信息；写入审计由 Git commit/MR 承担，不创建或提交逐次操作日志。运行 `.agents/skills/lint/scripts/check-architecture-layout.sh "$KB_ROOT"`，如使用 Git，再运行 `git diff --check` 和 `git status --short`。

## 输出

报告提取的稳定知识、保留在专项的内容、是否保存 raw 对话、更新的索引、仍未验证的边界，以及本地修改/提交/发布的各自状态。
