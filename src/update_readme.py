# update_readme.py
import os
from datetime import datetime

# Import the agents from the src package
from src.alexo_agent.data_source import fetch_blockchain_data
from src.alexo_agent.analysis_agent import analyze_network_data
from src.alexo_agent.strategy_agent import develop_strategy
from src.alexo_agent.reporting_agent import generate_insight

def run_agent_chain():
    """
    Runs the full chain of agents, passing output from one to the next.
    运行完整的代理链，将一个代理的输出传递给下一个。
    """
    print("🚀 Starting Alexo AI Agent Chain...")
    # Step 1: Fetch data
    raw_data = fetch_blockchain_data()
    # Step 2: Analyze data
    analysis = analyze_network_data(raw_data)
    # Step 3: Develop strategy
    strategy = develop_strategy(analysis)
    # Step 4: Generate final report/insight
    final_insight = generate_insight(strategy)
    print("✅ Agent chain finished successfully.")
    return final_insight

def update_readme_file(insight: str):
    """
    Updates the README.md with the new insight and a timestamp.
    使用新的见解和时间戳更新 README.md。
    """
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    
    with open(readme_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    in_ai_section = False
    for line in lines:
        if "<!-- AI_STATUS_START -->" in line:
            in_ai_section = True
            new_lines.append(line)
            # Add new content
            new_lines.append(f"**Status:** Active & Evolving | 状态: 活跃与进化中\n")
            new_lines.append(f"**Latest Insight:** `{insight}`\n")
            new_lines.append(f"**Last Updated:** `{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}`\n")
        elif "<!-- AI_STATUS_END -->" in line:
            in_ai_section = False
            new_lines.append(line)
        elif not in_ai_section:
            # Append lines outside the AI section
            new_lines.append(line)
            
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
    print(f"✔️ README.md has been updated.")


if __name__ == "__main__":
    generated_insight = run_agent_chain()
    update_readme_file(generated_insight)
