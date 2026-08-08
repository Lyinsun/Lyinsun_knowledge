---
id: DEC-0001
title: Example Reliability Decision
status: active
owner: TEAM-A
last_reviewed: 2026-08-08
review_after: 2027-02-08
verification: verified
sources:
  - SRC-0001
related:
  - ../architecture/ARC-0001-example-event-delivery.md
---

# 示例可靠性决策

## 背景

合成投递服务需要在“持续自动重试”与“保留人工复核点”之间做出选择。

## 决定

采用有限次数的自动重试；达到上限后将投递标为 `needs-review`。

## 备选方案与取舍

| 方案 | 优点 | 代价 | 结论 |
| --- | --- | --- | --- |
| 无限重试 | 操作简单 | 可能掩盖持续失败 | 不采用 |
| 有限重试加复核 | 故障可见、可控 | 需要复核流程 | 采用 |

## 来源

- [SRC-0001 合成设计来源](../sources/SRC-0001-synthetic-design.md)

## 相关内容

- [ARC-0001 示例事件投递架构](../architecture/ARC-0001-example-event-delivery.md)
- [示例关系地图](../index/relationship-map.md)
