import os
import re
from pathlib import Path

def extract_existing_paths(index_path):
    paths = set()
    if not index_path.exists():
        return paths
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'`([^`]+)`', line)
                if match:
                    paths.add(match.group(1))
    except Exception as e:
        print(f"Warning: Could not read existing index for diffing: {e}")
    return paths

def scan_assets(root_path):
    assets = []
    root = Path(root_path)
    scan_dirs = ["officials", "3rdparty", "org", "core"]
    
    for d in scan_dirs:
        dir_path = root / d
        if not dir_path.exists():
            continue
            
        for item in dir_path.rglob("*"):
            if not item.is_dir():
                continue
            
            skill_md = item / "SKILL.md"
            if skill_md.exists():
                assets.append({
                    "name": item.name,
                    "path": str(item.relative_to(root)),
                    "type": "skill",
                    "description": extract_description(skill_md)
                })
                continue
            
            if "mcp-" in item.parent.name or item.parent.name == "src":
                if (item / "package.json").exists() or (item / "pyproject.toml").exists() or (item / "requirements.txt").exists():
                    assets.append({
                        "name": f"mcp-{item.name}",
                        "path": str(item.relative_to(root)),
                        "type": "mcp-tool",
                        "description": f"MCP tool detected: {item.name}"
                    })
    return assets

def extract_description(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(500) 
            if "description:" in content:
                desc = content.split("description:")[1].split("\n")[0].strip()
                return desc
            return "No description available."
    except:
        return "Could not read description."

def write_md_table(file_path, title, description, assets):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"{description}\n\n")
        f.write("| Name | Type | Path | Description |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for a in assets:
            f.write(f"| {a['name']} | {a['type']} | `{a['path']}` | {a['description']} |\n")

if __name__ == "__main__":
    project_root = Path(__file__).parent.parent.parent
    skills_dir = project_root / ".skills"
    skills_dir.mkdir(exist_ok=True)
    
    index_path = skills_dir / "ASSET_INDEX.md"
    diff_path = skills_dir / "ASSET_DIFF.md"
    
    old_paths = extract_existing_paths(index_path)
    found_assets = scan_assets(project_root)
    new_assets = [a for a in found_assets if a['path'] not in old_paths]
    
    write_md_table(index_path, "Asset Index - Skill-Manager", 
                  "This index is automatically generated for AI discovery.", found_assets)
    
    if new_assets:
        write_md_table(diff_path, "Latest Asset Updates", 
                      f"Detected {len(new_assets)} new assets in the latest scan.", new_assets)
        print(f"✨ Found {len(new_assets)} new assets! Check .skills/ASSET_DIFF.md for details.")
    else:
        if diff_path.exists():
            os.remove(diff_path)
        print("No new assets detected.")
    
    print(f"Index updated with {len(found_assets)} items in .skills/.")
