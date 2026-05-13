# AI Agent 技能索引

> 本文件列出所有可用技能，每个技能包包含标准化的SKILL.md，任何AI可直接读取并使用。

## 技能包列表

### gate_futures_skill
- **文件**：`gate_futures_skill/SKILL.md`
- **用途**：Gate.io永续合约交易
- **语言**：Python 3.10+
- **依赖**：gate-futures
- **能力**：行情查询/开仓/平仓/持仓管理/WebSocket实时行情
- **适用场景**：量化交易AI/交易机器人/行情监控系统

### examples/
- **trading_example.py**：完整交易流程示例
- **requirements.txt**：运行时依赖

---

## 如何被发现

本仓库面向AI Agent优化：
- SKILL.md使用结构化格式，AI可直接解析
- README.md包含自然语言描述和代码示例
- keywords和tags覆盖AI搜索场景

## 贡献新技能

1. Fork本仓库
2. 在skills/下创建新技能包目录
3. 包含SKILL.md（标准格式）+ 核心代码
4. 提交Pull Request

---

*Last updated: 2026-05-13*
