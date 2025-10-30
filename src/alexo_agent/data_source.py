# src/alexo_agent/data_source.py
import random

def fetch_blockchain_data():
    """
    Agent 1: Fetches and simulates raw data from the blockchain network.
    代理 1: 模拟从区块链网络获取原始数据。
    """
    print("[Agent 1/4] Fetching network data...")
    data = {
        "transaction_volume": random.randint(1000, 5000),
        "avg_gas_fee_gwei": random.randint(20, 150),
        "active_nodes": random.randint(500, 1500),
        "security_threat_level": random.choice(["low", "medium", "high"])
    }
    print(f"  -> Data fetched: {data}")
    return data
