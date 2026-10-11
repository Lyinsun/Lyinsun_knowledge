---
title: "知识库目录与内容分层规范"
repo: "knowledge-base"
category: "workflows"
tags: ["knowledge-base", "information-architecture", "governance"]
created: "2026-08-10"
updated: "2026-09-08"
status: "active"
---

知识库使用“七个长期知识目录 + 专项目录 + 原始证据”组织内容，同时用全局和本地索引控制可达性。

## 目标与边界

- 使稳定答案、专项过程和原始证据可以被分别查询。
- 使结论能回链到事实源，但不在知识页面中重复大段代码或原文。
- **实行“新老划断与渐进治理”**：所有新创建的文档必须无条件遵循本规范与三段式结构；对历史存量文档严禁搞一刀切全量形式主义翻新，仅在面临实质性重大重构且收益明确时才渐进升级。
- 不使用 `misc/`、`others/` 等无法表达范围的兜底目录。

## 内容模型

| 层 | 目录 | 判断问题 | 典型内容 |
| --- | --- | --- | --- |
| 长期知识 | `architecture/`、`services/`、`modules/`、`infrastructure/`、`workflows/`、`concepts/`、`external/` | 脱离当前任务后是否仍是直接答案？ | 架构、服务入口、规则、运行手册、术语 |
| 专项知识 | `initiatives/<name>/` | 是否服务于一个有明确目标和结束条件的专项？ | 需求、调研、方案、交付、状态 |
| 原始证据 | `raw/` | 是否需要保留原貌以便复核或重新编译？ | 文档快照、会议原文、代码分析输出、对话快照 |

## 新内容路由

1. 先读取 `_index/topic-map.md` 并递归查重。
2. 有独立原始输入时，将经授权和脱敏后的必要快照保存到 `raw/`，并登记 `_manifest.md`。
3. 有明确专项边界的过程内容进入同一个 `initiatives/<name>/`。
4. 已验证、可复用且脱离专项仍成立的结论，更新到七个长期目录。
5. 专项与长期页面用链接引用同一个事实源，不复制整段正文。

## 长期目录规则

- `architecture/` 正文必须写入 `architecture/<scope>/<page>.md`；根目录只允许 `README.md` 和可选的 `overview.md`。
- 架构 scope 由 [`architecture/README.md`](../architecture/README.md) 定义，每个 scope 必须有 README 作为本地导航，并在全局 topic map 中拥有对应分组。
- 其他长期目录仍遵循“先平铺、后分组”：只有同类页面形成稳定集合时才创建子目录。
- 新子目录必须有范围说明和页面导航。
- 普通页面最多位于长期目录下两层；更深层级应先评审信息架构。
- 任务型调研、未冻结设计、交付和状态进入 `initiatives/`，不因“涉及架构”就放进长期架构目录。

## 专项目录规则

- `initiatives/<name>/README.md` 是唯一必需页面，也是目标、状态、结论和本地索引的事实源。
- 仅在实际需要时创建 `requirements.md`、`research/`、`design/`、`delivery/` 或 `status/`。
- 专项结束时保留材料，把 README 状态改为 `completed` 或 `cancelled`，并记录稳定知识去向。

## 页面正文三段式结构规范

为确保人类与 AI Agent 协同阅读与检索效率，知识库正文统一采用“渐进式展开（Progressive Disclosure）”的三段式结构，必须参考 `_templates/` 对应模板创建：

| 层次 | 内容板块 | 目标受众与核心规范 |
| :--- | :--- | :--- |
| **第一层** | **全景状态图 (Mermaid)** | **人类快速感知通道**。保持图的独立与全貌完整，看图即知系统边界与落地状态。<br>• `实线框+实线连接 (绿色)`：已上线、已实现或稳定运行链路；<br>• `虚线框+虚线连接 (黄色/橙色)`：设计中、规划中或本次专项改造中的链路；<br>• `灰色细边框 (灰度)`：已废弃、计划下线或明确在范围外的链路；<br>• `subgraph`：按业务层级区分模块域。 |
| **第二层** | **能力对比与路由表 (Table)** | **结构化对比与下钻中心**。<br>• 横向对比不同版本（v1/v2/v3）或改造前后的能力矩阵，标注状态（`✅ / 🚧 / ⏳ / ⚠️ / ❌`）与差异说明；<br>• 最后一列直接挂接深度子文档相对路径（`[[子文档路径]]`）或同页小节锚点。 |
| **第三层** | **技术规格与深度细节 (Text)** | **AI 上下文与深度评审通道**。<br>• 详尽记录 DDL 变更、接口协议契约、核心算法伪代码、并发控制、容灾降级指标与未验证债务清单。 |

### 模板映射与派生关系

- **业务方案与改造任务**：使用 `_templates/initiative-readme.md`
- **系统架构与设计**：使用 `_templates/architecture.md`
- **功能模块与核心库**：使用 `_templates/module.md`
- **原始资料与会议快照**：使用 `_templates/raw-snapshot.md`
- **通用技术与规范页面**：使用 `_templates/wiki.md`
- **架构范围导航页**：使用 `_templates/architecture-scope-readme.md`（导航页保持轻量，只做本地索引，不复制正文）
- *注：技术决策（ADR）直接内嵌于方案与架构正文中，不再使用独立的 ADR 模板；代码仓说明以代码仓自带 README 为准，不再维护 `repo-readme.md`。*

### Mermaid 配色约定

全库统一三态，`classDef` 骨架见 [`_templates/architecture.md`](../_templates/architecture.md)，6 个模板保持一致：

| classDef | 样式 | 含义 |
| --- | --- | --- |
| `implemented` | 绿色实线 `fill:#E8F5E9,stroke:#2E7D32` | 已实现、已上线、稳定运行 |
| `inDesign` | 黄色虚线 `fill:#FFF9C4,stroke:#F57F17,stroke-dasharray: 5 5` | 设计中、建设中、计划新增，尚未生效 |
| `deprecated` | 灰色中划线 `fill:#EEEEEE,stroke:#9E9E9E,stroke-dasharray: 2 2` | 已废弃、计划下线、不在本次范围 |

颜色只是辅助：节点和连线文字必须同时写明“当前 / 计划 / 已废弃 / 不在范围”等语义，绿色不得用于尚未发生的计划。

**绿色证据必须注明实际范围**：代码已实现不等于已合入，合入不等于已部署，部署不等于验收通过；raw 快照中“材料已记录 / 已达成共识”也不代表主张已经过代码或运行时核实。引用未合入实现时同时注明分支、完整 commit、路径行号与验证范围。

## 路径与链接规范

知识库必须能够整体复制、重命名或在另一位开发者的 checkout 中使用。活动文档、Skill、模板、脚本和配置不得依赖某台机器的用户名或固定绝对路径。

| 场景 | 规范 | 示例 |
| --- | --- | --- |
| 知识库内 Markdown 链接 | 相对当前页面解析 | `../workflows/knowledge-base-organization.md` |
| 引用同级代码仓或外部目录 | 相对知识库根目录使用 `../<repo>/<path>` | `../<repo>/src/` |
| 提示词、任务说明和命令示例 | 使用相对工作区根目录的路径，并明确执行基准 | `docs/_index/topic-map.md` |
| 仓库脚本 | 从 `${BASH_SOURCE[0]}`、脚本目录或 `git rev-parse --show-toplevel` 解析当前 checkout | `SCRIPT_DIRECTORY/..` |
| 必须接收绝对路径的外部配置 | 使用运行时 specifier、环境变量或由安装器生成 | `%h`、`${HOME}`、`${XDG_CONFIG_HOME}` |

禁止在当前可执行说明或配置中写死 `/home/<user>/...`、`/data00/home/<user>/...` 等个人/机器相关路径。平台固定路径不是工作区引用时可以保留，但应说明它是运行环境合同，而不是 checkout 位置。

历史 `raw/` 快照或排障证据为保持原始现场可以保留当时的绝对路径；这类路径必须具有追溯价值，不得继续作为当前命令、写入目标或自动化入口。修改既有页面时，只修复本次范围内的活动引用，不为统一外观批量改写历史证据。

## Frontmatter Schema

| 字段 | 要求 |
| --- | --- |
| `title` | 必填，页面标题 |
| `repo` | 必填，仓库/系统标识；跨域页面使用 `cross-cutting` |
| `category` | 必填，七个长期分类之一或 `initiatives` |
| `tags` | 必填，字符串数组 |
| `created` / `updated` | 必填，`YYYY-MM-DD` |
| `sources` | 可选，代码、raw 或外部来源列表 |
| `coverage` | 可选，`high/medium/low` |
| `status` | 长期页面使用 `active/stale/archived`；专项页面使用 `planned/in_progress/blocked/completed/cancelled` |
| `as_of` | 可选，仅用于需要明确时间点的专项状态快照 |

正式页面 frontmatter 后的第一段必须是一句话摘要。`_templates/`、`_index/`、`raw/` 和 `.agents/skills/` 使用各自的结构，不套用正式页面 Schema。

## 索引规则

- `_index/topic-map.md` 直接导航每个长期页面和每个专项 README。
- 架构页还必须从所属 scope README 可达；topic map 的架构部分按 scope 分组。
- 专项子页面由专项 README 导航，不进入全局索引。
- `raw/_manifest.md` 维护 raw 快照到编译目标的映射，raw 页面不进入全局索引。
- 索引标题和一句话摘要应与目标页一致。

## 来源与脱敏

- 保存 raw 前确认用户授权和来源的复制边界。
- 删除凭据、密钥、连接串、个人联系方式、不必要的个人标识和无关上下文。
- 不把脱敏后已失去证据价值的内容保存为快照；改为记录来源标识和可验证结论。
- 外部资料更新时新建带日期的快照，不覆盖历史版本。

## 审计与完成检查

写入审计由 Git commit/MR 承担；Skill 不创建或提交逐次操作日志。每次写入后检查：

- [ ] 内容已路由到稳定知识、专项上下文或 raw 证据。
- [ ] 新页面没有与已有页面重复。
- [ ] frontmatter、一句话摘要和相对链接有效。
- [ ] 全局索引、专项本地索引和 raw manifest 已按需要更新。
- [ ] 架构页位于合法 scope，并同步 scope README 和全局 topic map。
- [ ] `architecture/` 根目录没有 `README.md` / `overview.md` 之外的正文。
- [ ] 没有写入凭据、个人敏感信息或未授权原文。
- [ ] 活动文档、Skill、模板、脚本和配置未写入个人/机器相关的绝对路径；必要例外已说明运行时合同或历史证据属性。
- [ ] 如使用 Git，`git diff --check` 通过且未覆盖无关变更。

## 变更与发布

- `/query` 和 `/lint` 严格只读，不创建操作日志，也不自动触发提交或发布。
- `/add-wiki`、`/digest` 和 `/ingest` 只在得到写入授权后修改普通知识，并遵循 [`knowledge-base-change-policy.md`](knowledge-base-change-policy.md)。
- 治理变更按是否影响本仓之外的行为分两类：**仓内治理**（目录调整、模板、Schema、配色、索引重组）与普通知识同路由；**跨边界治理**（Agent 规则、Skill、验证脚本、发布自动化、批量移动或删除）默认隔离并审查。判定依据和处理方式见 [`knowledge-base-change-policy.md`](knowledge-base-change-policy.md)。
- 模板不预设默认分支、直推权限、代码托管平台或发布自动化，不得从模板文字推断外部写入权限。

## 资源导航

- [架构范围导航](../architecture/README.md)
- [专项目录](../initiatives/README.md)
- [Raw 资料清单](../raw/_manifest.md)
- [知识库变更与发布边界](knowledge-base-change-policy.md)
