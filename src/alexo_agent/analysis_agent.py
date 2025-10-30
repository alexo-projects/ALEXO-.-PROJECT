# src/alexo_agent/analysis_agent.py

def analyze_network_data(data: dict):
    """
    Agent 2: Analyzes the raw data to produce a structured finding.
    代理 2: 分析原始数据以产生结构化的发现。
    """
    print("[Agent 2/4] Analyzing data for key findings...")
    if data["security_threat_level"] == "high":
        finding = "High security threat detected."
    elif data["avg_gas_fee_gwei"] > 100:
        finding = "High network congestion detected via gas fees."
    elif data["transaction_volume"] > 4500:
        finding = "Unusually high transaction volume observed."
    else:
        finding = "Network operating within normal parameters."
    
    analysis = {"finding": finding, "source_data": data}
    print(f"  -> Analysis complete: {analysis['finding']}")
    return analysis
