import os
import shutil
import argparse
from pathlib import Path

def import_skill(source_path, target_repo_path, skill_name):
    # Security: Ensure paths are resolved and validated
    source_path = Path(source_path).resolve()
    target_repo_path = Path(target_repo_path).resolve()
    
    # 1. Ensure source is not inside target's system paths
    if str(target_repo_path) in str(source_path) and ".skills" not in str(source_path):
         print(f"Error: Source path cannot be inside the target repository's working area (except .skills).")
         return False

    # 2. Determine paths
    neutral_skills_dir = target_repo_path / ".skills"
    claude_skills_dir = Path(target_repo_path) / ".claude" / "skills"
    agents_skills_dir = Path(target_repo_path) / ".agents" / "skills"
    
    target_entity_path = neutral_skills_dir / skill_name
    
    # 1. Create directory
    neutral_skills_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Ensure symlinks exist for tool-specific directories
    def ensure_symlink(link_path):
        parent = link_path.parent
        parent.mkdir(parents=True, exist_ok=True)
        if not link_path.exists() and not link_path.is_symlink():
            print(f"Creating tool-specific symlink: {link_path} -> ../.skills")
            os.symlink("../.skills", link_path)
    
    ensure_symlink(claude_skills_dir)
    ensure_symlink(agents_skills_dir)
    
    # 3. Copy skill entity
    print(f"Copying skill from {source_path} to {target_entity_path}...")
    if target_entity_path.exists():
        print(f"Warning: {target_entity_path} already exists. Overwriting...")
        shutil.rmtree(target_entity_path)
    shutil.copytree(source_path, target_entity_path)
    
    print(f"Successfully imported skill '{skill_name}' to {target_repo_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import a skill from .officials to a project repo with symlink.")
    parser.add_argument("--source", required=True, help="Source path of the skill (absolute or relative to SKILL_MANAGER_ROOT)")
    parser.add_argument("--repo", required=True, help="Target repository root path")
    parser.add_argument("--name", required=True, help="Name of the skill to be created")
    
    args = parser.parse_args()
    
    # Resolve source path using environment variable if not absolute
    source_path = Path(args.source)
    if not source_path.is_absolute():
        hub_root = os.environ.get("SKILL_MANAGER_ROOT")
        if hub_root:
            source_path = Path(hub_root) / args.source
            print(f"Resolving source relative to SKILL_MANAGER_ROOT: {source_path}")
        else:
            # Fallback to current directory relative if no environment variable
            source_path = source_path.resolve()
            
    if not source_path.exists():
        print(f"Error: Source path does not exist: {source_path}")
        exit(1)
        
    import_skill(source_path, args.repo, args.name)
