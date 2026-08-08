---
id: IFC-0001
title: Example Delivery Contract
status: active
owner: TEAM-A
last_reviewed: 2026-08-08
review_after: 2027-02-08
verification: verified
sources:
  - SRC-0001
related:
  - ../services/SRV-0001-example-delivery-service.md
  - ../workflows/WFL-0001-example-change-flow.md
---

# 示例投递接口契约

## 范围

定义合成投递请求的最小字段和响应状态，用于演示接口笔记与服务、流程的关联。

## 契约

| 字段 | 含义 | 示例 |
| --- | --- | --- |
| `event_id` | 合成事件标识 | `event-123` |
| `payload` | 最小化内容 | `example-payload` |
| `delivery_state` | 投递状态 | `accepted` |

## 来源

- [SRC-0001 合成设计来源](../sources/SRC-0001-synthetic-design.md)

## 相关内容

- [SRV-0001 示例投递服务](../services/SRV-0001-example-delivery-service.md)
- [WFL-0001 示例变更流程](../workflows/WFL-0001-example-change-flow.md)
- [示例关系地图](../index/relationship-map.md)
