# Obsidian 个人知识库模板

一个可复制、脱敏的 Obsidian 个人知识库骨架：用收件箱接住输入，用项目/领域/资源保存上下文，用知识卡与问答记录沉淀可复用理解。

## 快速开始

1. 复制本目录到新仓库或空目录；不要将这里作为真实知识库直接使用。
2. 在 Obsidian 中打开复制后的目录；应用会自行生成本机 `.obsidian/` 工作区状态。
3. 从 [`Index/Home.md`](Index/Home.md) 开始，并将第一条未分类输入放进 `00-Inbox/`。
4. 需要新页面时从 `99-Templates/` 复制；通过 `[[wikilink]]` 建立关联。
5. 执行 `python3 scripts/check_template.py --root .` 检查结构、示例和常见隐私残留。

## 目录与意图

| 路径 | 用途 |
| --- | --- |
| `00-Inbox/` | 未完成分类的新资料与想法 |
| `01-Projects/` | 有明确目标和结束条件的工作 |
| `02-Areas/` | 长期负责或持续学习的领域 |
| `03-Resources/` | 外部资料及其来源说明 |
| `04-Archives/` | 已完成或不再活跃的内容 |
| `05-Knowledge/` | Concepts、How-Tos、Decisions、Insights 知识卡 |
| `06-QA-Log/` | 问题、证据、答案和后续行动 |
| `99-Templates/` | 新建笔记的标准模板 |
| `Index/` | 入口与 Dataview 内容地图（MOC） |
| `.agents/skills/` | 可选的 AI 知识库维护 Skill |

## 示例与测试

- `01-Projects/示例-知识库整理.md`、`05-Knowledge/How-Tos/示例-从收件箱到知识卡.md`、`06-QA-Log/QA-示例-整理一次输入.md` 是完全合成的最小知识网络。
- `tests/test_check_template.sh` 验证检查器能识别模板根目录；运行 `bash tests/test_check_template.sh`。
- `scripts/check_template.py` 只读检查必需目录、示例、模板字段、绝对路径和常见敏感标识；不自动修复或删除任何内容。

## 隐私与移植边界

模板只保留结构、规范、合成示例和通用 Skill。真实笔记、聊天/会议原文、个人身份、组织或客户标识、项目名称、内部地址、Git remote、令牌、凭据、生产配置及本机 `.obsidian/workspace*` 不得进入模板。库内链接使用相对路径或 `[[wikilink]]`，不要写入用户目录等机器相关路径。

## 配套 Skills

`.agents/skills/` 内提供 `query`、`add-wiki`、`digest`、`ingest`、`lint`。它们描述通用的检索、写入、沉淀、编译和只读健康检查流程；是否由运行时自动发现，取决于所使用的 Agent 平台。
