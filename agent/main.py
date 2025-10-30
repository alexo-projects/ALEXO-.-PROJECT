import os
import random
from datetime import datetime

def get_ai_insight():
    """Generates a random AI insight."""
    insights = [
        "Analyzing blockchain synergy for enhanced efficiency.",
        "Optimizing node allocation for faster data throughput.",
        "Evolving predictive models based on latest network data.",
        "Identifying anomalies in decentralized transactions.",
        "Enhancing data encryption for robust security.",
        "Self-adjusting consensus parameters for network stability."
    ]
    return random.choice(insights)

def update_readme(insight):
    """Updates the README.md with a new insight and timestamp."""
    readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
    
    with open(readme_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Find and update the placeholder
    new_lines = []
    # This flag helps us know when we are inside the AI section
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

if __name__ == "__main__":
    ai_insight = get_ai_insight()
    update_readme(ai_insight)
    print(f"README updated successfully with insight: {ai_insight}")
