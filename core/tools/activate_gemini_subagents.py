import os
from pathlib import Path

def extract_meta(content):
    meta = {}
    if content.startswith('---'):
        parts = content.split('---')
        if len(parts) >= 3:
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip()
    return meta

def generate_gemini_manifest(skills_dir):
    subagents = []
    root = Path(skills_dir)
    if not root.exists():
        return

    for item in root.iterdir():
        if not item.is_dir(): continue
        skill_md = item / "SKILL.md"
        if not skill_md.exists(): continue
            
        try:
            with open(skill_md, 'r', encoding='utf-8') as f:
                content = f.read()
                metadata = extract_meta(content)
                name = metadata.get('name', item.name)
                desc = metadata.get('description', 'No description')
                
                # Check if it's a sub-agent candidate
                if any(key in name.lower() for key in ['agent', 'swarm', 'langgraph', 'architect', 'consultant']):
                    subagents.append({"name": name, "description": desc})
        except:
            pass

    print("\n--- GEMINI SUB-AGENT MANIFEST ---")
    print("<available_subagents>")
    for sa in subagents:
        print(f"  <subagent>")
        print(f"    <name>{sa['name']}</name>")
        print(f"    <description>{sa['description']}</description>")
        print(f"  </subagent>")
    print("</available_subagents>")
    print("---------------------------------")

if __name__ == "__main__":
    project_root = Path(__file__).parent.parent.parent
    generate_gemini_manifest(project_root / ".skills")
