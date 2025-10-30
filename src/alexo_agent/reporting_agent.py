# src/alexo_agent/reporting_agent.py

def generate_insight(strategy: dict):
    """
    Agent 4: Generates a concise, human-readable insight for the README.
    代理 4: 为 README 生成简洁、人类可读的见解。
    """
    print("[Agent 4/4] Generating final insight...")
    action = strategy["action"]
    
    insight = f"System Intelligence: {action}"
    
    print(f"  -> Final Insight: \"{insight}\"")
    return insight
