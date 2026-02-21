# Project Rules (Source of Truth) - Skill-Manager

This file is the single source of truth for all AI agents working on this project.

## 📖 Project Overview
- **Name**: Skill-Manager
- **Description**: A framework for unifying AI agent assets (skills, tools, and configurations).
- **Core Principle**: **"Agent-Neutral & Minimal Pollution"**
  - Minimize hidden directories specific to particular tools (e.g., `.gemini/`, `.claude/`) and prioritize managing assets within a common standard directory structure.

## 🤖 Agent Behavior Guidelines
Agents must follow these guidelines:

### 1. Prohibition of Tool-Specific Folders
- When introducing a new tool, do not create tool-specific `.xxx/` folders without careful consideration.
- Prioritize integrating functions into existing common folders like `.skills/`, `tools/`, and `blueprints/`.

### 2. Maintain Single Source of Truth (SSoT)
- Always make `AGENTS.md`, `CLAUDE.md`, `COPILOT.md`, etc., symbolic links to `PROJECT_RULES.md`.
- Changes to settings must be made to `PROJECT_RULES.md`, and individual configuration files must not be modified directly.

### 3. Neutral Path Reference
- Skill entities should always be referenced under the `.skills/` directory.
- Do not recognize agent-specific paths (e.g., `.agents/skills/`) as "entities" or write files directly into them.

### 4. Interoperability via Symbolic Links
- When sharing the same file across multiple tools, use symbolic links (relative paths) instead of copies.

## 📂 Directory Roles
- `core/`: **[Entity]** Core assets of Skill-Manager itself (tools, skills, templates).
  - `core/skills/`: Entities for built-in skills (e.g., `asset-consultant`, `plan-navigator`).
  - `core/tools/`: Entities for management scripts (e.g., `import-skill.py`).
  - `core/blueprints/`: Entities for configuration templates (e.g., `PROJECT_RULES.md`).
- `.skills/`: **[Entity]** Project-specific or picked-up skill entities (including links to core skills).
- `tools/`: Shortcut (symbolic link) to `core/tools/`.
- `officials/`, `org/`, `3rdparty/`: **[Source]** Collections of skill entities managed via git submodules.
  - Directories must follow the `{category}-{vendor}` naming convention for easy discovery:
    - `agents-*`: Frameworks for multi-agent orchestration, task handoffs, and agent logic (e.g., `agents-langchain`, `agents-microsoft-autogen`).
    - `mcp-*`: Real tool implementations using the Model Context Protocol (e.g., `mcp-modelcontext`, `mcp-google`).
    - `skills-*`: Guides, prompt collections, and behavioral configurations for specific AI models (e.g., `skills-anthropic`, `skills-gemini`).
    - `blueprints-*`: Templates for project structures and configurations.

## 🛠 Operation Workflows
- **Sync**: Use `git submodule update`.
- **Import**: Via `tools/import-skill.py` into `.skills/`.
- **Apply**: Via `tools/setup-project.py` to link into other projects.

## ✍️ Coding Standards
- **Naming**: Follow `{source}-{repo}-{skill_name}`.
- **Portability**: Do not hardcode absolute paths specific to any tool; use relative paths from the project root.
