---
title: "专项知识目录"
repo: "knowledge-base"
category: "initiatives"
tags: ["initiatives", "research", "design", "delivery"]
created: "2026-08-10"
updated: "2026-08-10"
---

`initiatives/` 保存有明确目标和结束条件的专项上下文，并把已验证、脱离专项仍成立的结论提升到长期知识目录。

## 最小结构

```text
initiatives/<initiative-name>/
├── README.md          # 必需：目标、范围、状态、结论和本地索引
├── requirements.md    # 可选：需求与验收标准
├── research/          # 可选：调研、对比和证据解释
├── design/            # 可选：方案与决策
├── delivery/          # 可选：实施、验证和发布记录
└── status/            # 可选：需要保留的阶段状态快照
```

只创建实际需要的文件和子目录。

## 索引与状态

- 专项名和文件名使用 lowercase kebab-case。
- 每个专项从 [`_templates/initiative-readme.md`](../_templates/initiative-readme.md) 创建 README。
- 专项正式页面使用 `category: initiatives`，状态使用 `planned/in_progress/blocked/completed/cancelled`。
- 只有专项 README 进入全局索引；子页面由专项 README 导航。
- 专项完成后保留材料，记录最终验证和长期知识去向。

## 当前专项

暂无已登记专项。
