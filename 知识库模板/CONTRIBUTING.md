# 贡献规范

## 提交前检查

1. 内容属于正确目录，并使用 `_templates/` 中的模板。
2. 所有工程事实有可追溯的 `sources` 字段；无法验证的内容标为 `draft` 或 `pending`。
3. 使用相对 Markdown 链接，避免本机绝对路径和编辑器专属链接。
4. 不包含凭据、个人数据、真实内部标识、受限原文或生产日志。
5. 运行：

   ```bash
   python3 .agents/skills/knowledge-lint/scripts/check_knowledge_base.py --root .
   git diff --check
   ```

## 命名

- 文件名：小写英文、数字和连字符，例如 `event-delivery-contract.md`。
- 笔记 ID：内容类型前缀加四位编号，例如 `ARC-0001`、`SRV-0001`、`DEC-0001`、`SRC-0001`。
- 一篇笔记只处理一个可清晰命名的主题；通过相对链接关联，而不是复制同一段内容。

## 状态与复审

- `draft`：正在形成，不能作为权威结论。
- `active`：已验证且当前有效。
- `deprecated`：仍保留历史价值，但不建议继续使用。
- `archived`：仅供追溯。

对时效性强的笔记填写 `last_reviewed` 和 `review_after`。过期信息应更新、弃用或明确标记验证缺口。
