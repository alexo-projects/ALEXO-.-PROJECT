# src/alexo_agent/strategy_agent.py

def develop_strategy(analysis: dict):
    """
    Agent 3: Develops a strategic action based on the analysis.
    代理 3: 根据分析结果制定战略行动。
    """
    print("[Agent 3/4] Developing strategic action...")
    finding = analysis["finding"]
    
    if "High security threat" in finding:
        action = "Re-routing traffic through enhanced security nodes."
    elif "High network congestion" in finding:
        action = "Activating dynamic fee scaling protocol to stabilize costs."
    elif "high transaction volume" in finding:
        action = "Allocating additional node resources to handle the load."
    else:
        action = "Continuing standard optimization monitoring."
        
    strategy = {"action": action, "reason": finding}
    print(f"  -> Strategy proposed: {strategy['action']}")
    return strategy
