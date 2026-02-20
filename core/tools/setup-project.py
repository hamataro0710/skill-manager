import os
import argparse
from pathlib import Path

def setup_project(target_repo, project_name="My Project", description="New Project"):
    target_path = Path(target_repo).resolve()
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

    print(f"\nSuccessfully set up agent configurations for: {target_repo}")
    print("Now you only need to manage 'PROJECT_RULES.md' for all agents.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unify AGENTS.md and CLAUDE.md using PROJECT_RULES.md.")
    parser.add_argument("--repo", default=".", help="Target repository path (default: current)")
    parser.add_argument("--name", default="My Project", help="Project name")
    parser.add_argument("--desc", default="A new AI-driven project", help="Project description")
    
    args = parser.parse_args()
    setup_project(args.repo, args.name, args.desc)
