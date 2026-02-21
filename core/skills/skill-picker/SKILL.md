---
name: skill-picker
description: Selects the best AI skills from various directories (core, officials, org, 3rdparty) and imports them with a structure of "Entity (.skills/)" and "Links (.agents/, .claude/)".
---

# Skill Picker

This skill automates the process of finding and integrating skills that match user requirements from various sources (official, internal org, third-party, built-in).

## Workflow

1. **Search**:
   - Explores the following directories to find `SKILL.md` or directories matching requirements:
     - `core/skills/` (Skill-Manager built-in)
     - `officials/` (Official)
     - `org/skills/` (Internal Organization)
     - `3rdparty/` (Third-party repositories)
2. **Propose**:
   - Presents a list of found skills and reasons for recommendation.
3. **Import**:
   - Imports the selected skill using `tools/import-skill.py`.
   - **Naming Convention**: Use the format `{source}-{repo}-{skill_name}` for the `--name` argument.

## Command Execution

```bash
# Example: Importing an image-search skill from gemini-skills
python3 tools/import-skill.py 
  --source officials/skills-gemini/skills/image-search 
  --repo . 
  --name official-skills-gemini-image-search
```

### Post-Import Structure
Once imported, the target project will have the following structure:

```text
{target-repo}
├── .skills/<name>         (Entity: Actual content)
├── .agents/skills/        (Link: Relative link to ../.skills)
└── .claude/skills/        (Link: Relative link to ../.skills)
```

## Precautions
- Symbolic links are created with relative paths, so they remain valid even if the repository is moved.
- If a skill with the same name already exists, confirm with the user before overwriting.
