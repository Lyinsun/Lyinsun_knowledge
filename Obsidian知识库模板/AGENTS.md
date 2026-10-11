# Obsidian Knowledge Base Guidelines

先读 `Index/Home.md` 与相关 MOC，再用 `rg` 查重。新内容优先进入 `00-Inbox/`；只有完成归类后才进入项目、领域、资源、知识卡或归档。

每篇非模板笔记都应有 `title`、`date`、`tags`、`status`、`domain` frontmatter，并以一句摘要开头。问答记录额外填写 `question_type` 和 `related`。使用 `[[wikilink]]` 关联笔记，依靠 Dataview MOC 发现内容，不维护重复的静态清单。

修改前确认用户授权与既有内容，禁止删除或覆盖不在当前任务范围内的笔记。运行 `python3 scripts/check_template.py --root .` 仅用于只读检查；修复问题前先说明范围。

不要写入身份、组织、项目、客户、内部地址、凭据、聊天原文、未授权资料或机器相关绝对路径。不要提交 `.obsidian/workspace*` 等个人 UI 状态。
