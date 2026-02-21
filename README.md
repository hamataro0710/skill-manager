# Skill-Manager

**A management framework for unifying AI agent assets (skills, tools, and configurations) across organizations, streamlining the distribution and maintenance of official and internal skills.**

## 🌟 Vision

The pace of AI development is staggering, making it increasingly difficult to keep up with the latest skill definitions and toolsets through individual effort alone. Furthermore, while users favor different AI agents (Gemini, Claude, Codex, etc.), the subtle differences in directory structures and paths required by each create barriers to asset reuse.

`Skill-Manager` abstracts and absorbs these differences, providing an environment where **"users can use their preferred agent while seamlessly sharing and reusing organizational knowledge."**

### Core Values
1.  **Anti-Fragmentation**: Absorbs subtle path differences (e.g., `.agents/`, `.claude/`) through a symbolic link layer, allowing a single skill definition to be used across all agents.
2.  **Maintenance-First Architecture**: Prioritizes providing a structure (Architecture) for "which skills are trustworthy" and "how to maintain them" over providing complex tools or UIs.
3.  **Collaborative Defense**: Integrates official repositories (Google, Anthropic, OpenAI, etc.) as submodules, maintaining a state where teams can efficiently select (pickup) "certified official assets" without security concerns.

## 📂 Directory Structure

```text
.
├── core/                # [Entity] Core assets of Skill-Manager itself (Tools, Skills, etc.)
│   ├── skills/          # Built-in skills (e.g., asset-consultant, plan-navigator)
│   ├── tools/           # Management scripts
│   └── blueprints/      # Templates for project-specific configurations
├── .skills/             # [Entity] Actual content of skills picked up for the project
├── tools/               # Symbolic link to core/tools
├── .agents/skills/      # Interface for Gemini CLI (Link to ../.skills)
├── .claude/skills/      # Interface for Claude Code (Link to ../.skills)
├── org/skills/          # Skills shared and distributed within the organization
├── 3rdparty/{repo}/     # Third-party repositories (Git Submodules, etc.)
├── officials/           # Official repositories from various companies (Git Submodules)
└── README.md
```

## 🚀 Roadmap
- [x] **Multi-Agent Support**: Baseline support for Gemini, Claude, and Codex (OpenAI).
- [ ] **Personality Extension**: Unifying and making sub-agent definitions with specific roles (personalities) distributable.
- [ ] **Skill Discovery**: Strengthening the mechanism for easily selecting the most suitable official skills for specific tasks.
- [ ] **Organizational Templates**: Templates under `org/skills/` that automatically apply internal standard prompts and naming conventions.

## ✨ Benefits of Organizational Adoption
- **Single Source of Truth**: All skill entities are managed in a neutral `.skills/` directory, with links from each agent's specific directory (`.agents/`, `.claude/`).
- **Unified Instructions**: By linking `AGENTS.md` and `CLAUDE.md` to `PROJECT_RULES.md`, consistent behavior is guaranteed regardless of the agent.
- **Portability**: Internal common tools defined in `org/skills/` can be instantly deployed in any project using the same command.

## 🏷️ Skill Naming Convention
To avoid conflicts and clarify origins, we recommend managing skills using the following format:
`{source}-{repo_name}-{skill_name}`

- **Example**: `official-skills-anthropic-mcp-builder` (Distributed from official source)
- **Example**: `org-internal-security-audit` (Common within organization)
- **Example**: `3rdparty-awesome-tools-translator` (External repository)

## 🚀 Getting Started
Since this repository refers to external official repositories as submodules, cloning with the `--recursive` option is required.

### Example Post-Import Project Structure
By running `tools/setup-project.py`, the target project will be configured so that a single skill entity can be referenced from multiple agents.
**Unified Setup:**
```bash
python tools/setup-project.py --repo {your-project-path} --name "My Project"
```

```text
{your-project}
├── PROJECT_RULES.md         # [Entity] Common rules for all agents
├── AGENTS.md                # Link to PROJECT_RULES.md
├── CLAUDE.md                # Link to PROJECT_RULES.md
├── .skills/                 # [Entity] Skill definitions (editing here reflects in all agents)
│   └── {picked-skill}/
├── .agents/
│   └── skills/              # Link to .skills/
├── .claude/
│   └── skills/              # Link to .skills/
└── {your-files}
```
