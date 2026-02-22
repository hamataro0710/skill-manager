import os
import argparse
from pathlib import Path

def setup_project(target_repo, project_name="My Project", description="New Project"):
    target_path = Path(target_repo).resolve()
    
    # 0. Ensure target directory exists
    if not target_path.exists():
        print(f"Creating project directory: {target_path}...")
        target_path.mkdir(parents=True, exist_ok=True)
        
    rules_source = target_path / "PROJECT_RULES.md"
    
    # 1. Create PROJECT_RULES.md if it doesn't exist
    if not rules_source.exists():
        print(f"Creating {rules_source}...")
        # Since setup-project.py is in core/tools/, template is in ../blueprints/
        template_path = Path(__file__).parent.parent / "blueprints" / "base" / "PROJECT_RULES.md"
        with open(template_path, 'r') as f:
            content = f.read()
        
        # Simple template replacement
        content = content.replace("{PROJECT_NAME}", project_name)
        content = content.replace("{PROJECT_DESCRIPTION}", description)
        content = content.replace("{TECH_STACK}", "Python, Shell, Markdown")
        
        with open(rules_source, 'w') as f:
            f.write(content)
    
    # 2. Create symbolic links
    links = ["AGENTS.md", "CLAUDE.md"]
    for link_name in links:
        link_path = target_path / link_name
        if link_path.exists() or link_path.is_symlink():
            print(f"Removing existing {link_name}...")
            if link_path.is_dir() and not link_path.is_symlink():
                import shutil
                shutil.rmtree(link_path)
            else:
                link_path.unlink()
        
        print(f"Creating symbolic link: {link_name} -> PROJECT_RULES.md")
        # Relative link is more portable
        os.symlink("PROJECT_RULES.md", link_path)

    # 3. Create .env with SKILL_MANAGER_ROOT
    env_path = target_path / ".env"
    hub_root = Path(__file__).parent.parent.parent.resolve()
    
    print(f"Configuring SKILL_MANAGER_ROOT in {env_path}...")
    env_entry = f"SKILL_MANAGER_ROOT={hub_root}\n"
    
    if env_path.exists():
        with open(env_path, 'r') as f:
            lines = f.readlines()
        
        # Update if exists, otherwise append
        updated = False
        new_lines = []
        for line in lines:
            if line.startswith("SKILL_MANAGER_ROOT="):
                new_lines.append(env_entry)
                updated = True
            else:
                new_lines.append(line)
        
        if not updated:
            new_lines.append(env_entry)
            
        with open(env_path, 'w') as f:
            f.writelines(new_lines)
    else:
        with open(env_path, 'w') as f:
            f.write(env_entry)

    # 4. Ensure .skills directory exists
    skills_dir = target_path / ".skills"
    if not skills_dir.exists():
        print(f"Creating {skills_dir}...")
        skills_dir.mkdir(parents=True, exist_ok=True)

    # 5. Auto-deploy Asset Consultant
    try:
        import sys
        script_dir = str(Path(__file__).parent.resolve())
        if script_dir not in sys.path:
            sys.path.append(script_dir)
            
        from import_skill import import_skill
        print(f"\nDeploying Asset Consultant to the target project...")
        # Try finding in core/skills or .skills
        ac_source = hub_root / "core" / "skills" / "asset-consultant"
        if not ac_source.exists():
            ac_source = hub_root / ".skills" / "core-asset-consultant"
            
        if ac_source.exists():
            import_skill(ac_source, target_path, "core-asset-consultant")
        else:
            print(f"Warning: Asset Consultant source not found at {ac_source}")
    except ImportError:
        print("Warning: Could not import 'import_skill' tool. Skipping auto-deploy of Asset Consultant.")

    print(f"\nSuccessfully set up agent configurations for: {target_repo}")
    print("Now you only need to manage 'PROJECT_RULES.md' for all agents.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unify AGENTS.md and CLAUDE.md using PROJECT_RULES.md.")
    parser.add_argument("--repo", default=".", help="Target repository path (default: current)")
    parser.add_argument("--name", default="My Project", help="Project name")
    parser.add_argument("--desc", default="A new AI-driven project", help="Project description")
    
    args = parser.parse_args()
    setup_project(args.repo, args.name, args.desc)
