# 双向关联规范

## 目标

让笔记之间拥有类似 Wiki 的可导航关系，同时不依赖 Obsidian 或任何特定编辑器。实现方式是标准 Markdown 相对链接加上明确的反向链接，不依赖自动生成的“反向链接面板”。

## 关系模式

### 两篇工程笔记

当架构笔记 A 依赖服务笔记 B：

1. A 的“相关内容”链接到 B；
2. B 的“架构上下文”或“相关内容”链接回 A；
3. 两端都使用相对路径，因此仓库整体移动后仍可访问。

```markdown
<!-- architecture/ARC-0001-example-event-delivery.md -->
- [投递服务](../services/SRV-0001-example-delivery-service.md)

<!-- services/SRV-0001-example-delivery-service.md -->
- [事件投递架构](../architecture/ARC-0001-example-event-delivery.md)
```

### 来源与派生笔记

来源记录和权威笔记形成另一种双向关系：来源的“派生笔记”必须列出所有结论，而每篇结论也必须在“来源”中链接回来源记录。Agent 新增、拆分或弃用一篇权威笔记时，应在同一轮更新这两个方向。

### 索引与关系地图

- `index/topic-map.md`：按主题寻找权威入口。
- `index/relationship-map.md`：理解一个主题网络中的关键关系。
- 二者是导航，不替代笔记之间的双向链接。

## 维护规则

- 新建或删除关系时，同一次提交更新两端。
- 拆分一篇笔记时，将原笔记的入站和出站关系迁移到合适的新笔记。
- 每次新增权威笔记，都将其加入主题地图；关系较复杂时更新关系地图。
- 运行 `knowledge-lint`。它会对工程笔记之间、以及来源与派生笔记之间缺失的反向链接给出警告。
- 这些提示默认用于 AI 排查，不是自动门禁；仅在明确需要严格发布检查时使用 `--strict`。

## 可工作实例

查看 [`index/relationship-map.md`](../index/relationship-map.md)，其中的合成“事件投递”网络展示了所有上述关系。
