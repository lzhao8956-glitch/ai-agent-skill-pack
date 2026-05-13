# -*- coding: utf-8 -*-
"""Gate.io交易机器人完整示例
任何AI Agent复制这段代码就能交易加密货币
"""
import asyncio
from gate_futures import GateFutures

async def trading_bot():
    client = GateFutures(
        api_key='YOUR_API_KEY',
        secret_key='YOUR_SECRET_KEY',
        network='testnet'
    )
    
    # 1. 获取实时行情
    ticker = await client.get_ticker('BTC_USDT')
    print(f"BTC价格: ${ticker['last']}")
    
    # 2. 查余额
    balance = await client.get_balance()
    print(f"可用USDT: {balance.get('available')}")
    
    # 3. 开多仓 0.001 BTC
    order = await client.place_order('BTC_USDT', 'buy', size=0.001)
    print(f"订单ID: {order.get('id')}")
    
    # 4. 查持仓
    positions = await client.get_positions()
    for p in positions:
        print(f"{p['contract']}: {p['size']}张 | 浮盈${p['unrealised_pnl']}")
    
    # 5. 平仓
    await client.close_position('BTC_USDT')
    print("已平仓")

if __name__ == '__main__':
    asyncio.run(trading_bot())
