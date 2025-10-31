# update_readme.py (potongan penting)
import os
from datetime import datetime

def update_readme_file(insight: str):
    """
    Updates the README.md in repository root with the new insight and a timestamp.
    """
    # Ambil path repo root (dua level di atas jika file berada di src/)
    script_path = os.path.abspath(__file__)
    repo_root = os.path.dirname(os.path.dirname(script_path))  # jika file di src/
    # Jika strukturmu berbeda (mis. src/package/...), naik level sesuai kebutuhan:
    # repo_root = Path(__file__).resolve().parents[1]
    readme_path = os.path.join(repo_root, "README.md")

    if not os.path.isfile(readme_path):
        print(f"⚠️ README.md not found at {readme_path}. Aborting update.")
        return

    with open(readme_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    in_ai_section = False
    inserted = False
    for line in lines:
        if "<!-- AI_STATUS_START -->" in line:
            in_ai_section = True
            new_lines.append(line)
            new_lines.append(f"**Status:** Active & Evolving | 状态: 活跃与进化中\n")
            new_lines.append(f"**Latest Insight:** `{insight}`\n")
            new_lines.append(f"**Last Updated:** `{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}`\n")
            inserted = True
        elif "<!-- AI_STATUS_END -->" in line:
            in_ai_section = False
            new_lines.append(line)
        elif not in_ai_section:
            new_lines.append(line)

    if not inserted:
        # fallback: append AI section at end if markers tidak ditemukan
        new_lines.append("\n<!-- AI_STATUS_START -->\n")
        new_lines.append(f"**Status:** Active & Evolving | 状态: 活跃与进化中\n")
        new_lines.append(f"**Latest Insight:** `{insight}`\n")
        new_lines.append(f"**Last Updated:** `{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}`\n")
        new_lines.append("<!-- AI_STATUS_END -->\n")

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
    print(f"✔️ README.md has been updated at {readme_path}.")
