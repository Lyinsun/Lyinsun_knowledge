---
name: add-wiki
description: 创建或更新通用知识库页面，并同步索引和原始来源映射。用户要求“补 wiki”“新增知识库文档”“更新知识页面”或调研后需要持久回填时使用。
---

# Add Wiki

围绕一个主题创建或更新少量高质量页面。先查重，再验证事实；页面记录结论、边界和入口，代码与原始证据负责证明。

## 定位知识库

将包含 `_index/topic-map.md` 和 `workflows/knowledge-base-organization.md` 的最近祖先目录解析为 `KB_ROOT`。如无法唯一定位，停止写入并请求用户指定，不猜测目标目录。

## 写入门禁

1. 读取 `$KB_ROOT/_index/topic-map.md`、`$KB_ROOT/README.md`、`$KB_ROOT/workflows/knowledge-base-organization.md` 和 `$KB_ROOT/workflows/knowledge-base-change-policy.md`。
2. 如位于 Git 仓库，先检查分支和未提交改动；保留用户已有变更，只修改本任务相关文件。
3. 确认用户已授权写入知识库。不把一个只读查询自动扩展为写入。
4. 不写入凭据、个人敏感信息、未获授权的受限原文或无关过程噪声。
5. 如变更扩大到 Agent 规则、Skill、模板、Schema、验证脚本、发布自动化、目录治理或批量移动/删除，改按治理变更路由，不当作普通 wiki 写入。

## 内容路由

| 内容 | 位置 | 索引方式 |
| --- | --- | --- |
| 脱离当前任务仍成立的稳定知识 | 七个长期目录 | 登记 `_index/topic-map.md` |
| 有明确目标和结束条件的专项材料 | `initiatives/<name>/` | 全局只登记专项 README，子页登记本地索引 |
| 需要保留原貌的输入、快照和分析产物 | `raw/` | 登记 `raw/_manifest.md` |

七个长期目录是 `architecture`、`services`、`modules`、`infrastructure`、`workflows`、`concepts` 和 `external`。

架构正文执行额外门禁：

1. 先读取 `$KB_ROOT/architecture/README.md`，选择唯一已定义 scope，或在本次变更中明确定义新 scope。
2. 正文写入 `architecture/<scope>/<page>.md`；根目录只允许 `README.md` 和可选的 `overview.md`。
3. 新 scope 从 `_templates/architecture-scope-readme.md` 创建 README，并同时登记在 `architecture/README.md` 与 topic map。
4. 每篇架构页同时更新 scope README 和 topic map 的对应 scope 分组。
5. 需求、调研、未冻结设计、交付和状态进入 `initiatives/`，不因涉及架构就写入长期架构目录。

## 工作流

### 1. 明确交付范围

- 提炼要回答的问题、稳定结论、事实源和未验证项。
- 判断是更新长期答案还是记录专项过程。

### 2. 查重

先读全局索引，再递归搜索长期目录和 `initiatives/`。命中专项时先读其 README。优先更新已有页面；只在主题、生命周期或受众明显不同时新建页面。

### 3. 验证并分级证据

按以下优先级形成结论：

1. 当前代码、配置、测试和数据。
2. 已维护的知识页面。
3. 授权的只读工具查询或权威外部文档。
4. 用户提供但尚未验证的信息。

冲突时以当前事实源为准，并记录差异。纯代码调研可直接引用精确路径，不为满足形式制造 raw 文件。

### 4. 创建或更新页面

- 普通页面从 `$KB_ROOT/_templates/wiki.md` 开始；专项入口从 `_templates/initiative-readme.md` 开始。
- 架构页从 `_templates/architecture.md` 开始，并保存到 `architecture/<scope>/`。
- 使用规范 frontmatter、一句话摘要、lowercase kebab-case 路径和相对链接。
- 记录结论、适用边界和精确入口，不大段复制代码或原文。
- Markdown 链接使用相对当前页面的路径；引用同级代码仓使用相对知识库根目录的 `../<repo>/<path>`；命令和提示词使用相对工作区根目录的路径并写明执行基准。
- 不在活动文档、Skill、模板、脚本或配置中写入个人/机器相关的绝对路径。工具必须接收绝对路径时，使用 `%h`、`${HOME}`、`${XDG_CONFIG_HOME}`、脚本目录/Git 顶层自定位或安装时生成值。历史 raw 证据只有在保持原始现场确有必要时才保留绝对路径，且不得把它写成当前可执行入口。

### 5. 维护导航

- 按内容路由更新全局索引、专项本地索引和 raw manifest。
- 架构页额外更新所属 scope README 和 topic map 对应分组。

### 6. 校验

检查 frontmatter、一句话摘要、递归相对链接、索引入口、manifest 映射、敏感信息，以及本次改动是否引入个人/机器相关的绝对路径。写入审计由 Git commit/MR 承担，不创建或提交逐次操作日志。涉及架构页时运行 `$KB_ROOT/.agents/skills/lint/scripts/check-architecture-layout.sh "$KB_ROOT"`。如位于 Git 仓库，运行 `git diff --check` 和 `git status --short`。

## 输出

说明创建或更新的页面、稳定/专项/raw 分流、使用的事实源、未验证项、已完成的校验，以及本地修改/提交/发布的各自状态。
