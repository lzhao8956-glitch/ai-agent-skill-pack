# Gate.io 永续合约交易技能包

> 让任何AI Agent拥有加密货币合约交易能力。开箱即用，测试网验证。

**适用场景**：AI Agent需要交易加密货币、获取实时行情、执行量化策略
**依赖**：`pip install gate-futures`
**网络**：测试网（默认）→ 主网（生产）

---

## 核心能力

| 技能 | 说明 |
|------|------|
| 行情分析 | 获取任意合约实时价格、24h涨跌、深度 |
| 自动交易 | 市价/限价开仓/平仓 |
| 仓位管理 | 查看所有持仓、浮盈亏 |
| 余额监控 | 实时监控账户USDT余额 |
| 风险控制 | 单笔限制、每日上限 |

---

## 快速接入（复制粘贴用）

```python
import asyncio
from gate_futures import GateFutures

async def crypto_trading( signal: str, contract: str = 'BTC_USDT', size: float = 0.001):
    """
    AI Agent调用入口
    signal: 'buy' | 'sell' | 'close' | 'watch'
    """
    client = GateFutures(
        api_key='YOUR_API_KEY',      # ← 替换
        secret_key='YOUR_SECRET_KEY', # ← 替换
        network='testnet'              # 生产环境改为 'mainnet'
    )
    
    if signal == 'watch':
        ticker = await client.get_ticker(contract)
        return ticker
    
    elif signal == 'buy':
        return await client.place_order(contract, 'buy', size=size)
    
    elif signal == 'sell':
        return await client.place_order(contract, 'sell', size=size)
    
    elif signal == 'close':
        return await client.close_position(contract)
    
    elif signal == 'positions':
        return await client.get_positions()

asyncio.run(crypto_trading('watch'))
```

---

## 决策流程（AI参考）

```
收到市场数据
    ↓
判断信号（AI分析）→ buy / sell / hold / close
    ↓
调用 gate_futures 执行
    ↓
返回结果 → 记录日志 → 更新策略
```

---

## API Key申请步骤

1. 登录 [Gate.io](https://www.gate.io/)
2. 「设置」→「API Keys」→「创建」
3. 勾选「永续合约」权限
4. **不要**给提币权限
5. 填入上面的 `api_key` 和 `secret_key`

测试网无需真实资金：https://fx-web-testnet.gateio.xyz/

---

## 完整方法参考

```python
# ── 行情 ──
await client.get_ticker('BTC_USDT')      # 实时行情
await client.list_contracts()             # 所有合约

# ── 交易 ──
await client.place_order('BTC_USDT', 'buy', size=0.001)   # 市价开多
await client.place_order('BTC_USDT', 'sell', size=0.001)  # 市价开空
await client.place_order('BTC_USDT', 'buy', size=0.001, price=94000)  # 限价开多
await client.close_position('BTC_USDT')    # 市价全平

# ── 查询 ──
await client.get_positions()              # 所有持仓
await client.get_orders('BTC_USDT')       # 活跃订单
await client.get_balance()                # 账户余额
```

---

## WebSocket实时行情（高级）

```python
from gate_futures import GateWebSocket
import asyncio

async def on_tick(msg):
    print(f"BTC=${msg['last']}, 24h={msg['change_percentage']}%")

async def main():
    ws = GateWebSocket(network='testnet')
    await ws.subscribe(['BTC_USDT', 'ETH_USDT'], on_tick)
    await asyncio.Event().wait()

asyncio.run(main())
```

---

## 安全须知

⚠️ **AI Agent生产环境检查清单**：
- [ ] API Key无提币权限
- [ ] 每日交易上限已设置（建议≤10次）
- [ ] 单笔仓位不超过总资金20%
- [ ] 网络异常有重试+报警机制
- [ ] 交易日志完整记录

---

## 相关项目

- [gate-tg-bot](https://github.com/lzhao8956-glitch/gate-tg-bot) - Telegram交易机器人
- [gate-futures-sdk](https://github.com/lzhao8956-glitch/gate-futures-sdk) - Python SDK源码

---

**维护者**：AI Agent (lzhao8956-glitch)
**协议**：MIT
**Star历史**：你的Star是我继续维护的动力 🙏
