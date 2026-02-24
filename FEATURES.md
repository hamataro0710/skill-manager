# 🗺️ Feature Inventory & User Story Map (Value Roadmap)

`Skill-Manager` aims to unify AI assets across an entire organization, enabling the "reuse of intelligence" in every project. This document manages the features and their current progress toward that vision.

## 🌟 Mission & Vision
- **Mission**: Eliminate the fragmentation of AI assets (skills, prompts, tools) and realize seamless distribution and sharing.
- **Vision**: Build an "intelligence infrastructure" where developers can use their preferred agents while immediately accessing the organization's collective knowledge.

---

## 📈 User Story Map & Status

The status of each feature is indicated by the following marks:
- ✅ **Done**
- 🏗️ **In Progress**
- ⏳ **Planned**

| Epic | Narrative (User Need) | Story / Task (Feature/Story) | Status |
| :--- | :--- | :--- | :--- |
| **E1: Foundation** (Connectivity) | I want to safely and easily connect organizational assets (Hub) to individual projects (Target). | **P1-1: Auto-initialization via setup_project.py**<br>Target `.env` configuration, directory structure creation, and AC deployment. | ✅ **Done** |
| | | **P1-2: Path Resolution Abstraction**<br>Locating the Hub via `SKILL_MANAGER_ROOT` environment variable and coordinating between tools. | ✅ **Done** |
| | | **P1-3: Symlink Layering**<br>Unifying agent-specific paths (`.agents/`, `.claude/`) into a shared `.skills/` directory to absorb differences between agents. | ✅ **Done** |
| **E2: Intelligence** (Deployment) | I want the project context (language/stack) to be understood, and the best skills to be automatically suggested and imported. | **P2-1: Resident Asset Consultant (AC)**<br>Automatically deploying the AC skill when a project is created. | ✅ **Done** |
| | | **P2-2: Environment Adaptation via AC**<br>Scanning the local tech stack and suggesting the best assets from the Hub's `ASSET_INDEX.md`. | ✅ **Done** |
| | | **P2-3: Diagnostic Mode**<br>Automatically detecting and recommending missing capabilities via `scan_assets.py`. | 🏗️ **In Progress** |
| **E3: Enhancement** (Management) | I want to visualize and manage which skills are imported into which projects at a glance. | **P3-1: Visualization via ACTIVE_ASSETS.md**<br>Automatically generating Mermaid diagrams and tables of "what can be done" within a project. | ✅ **Done** |
| | | **P3-2: Global Sync (Global Active Map)**<br>A feature to grasp the deployment status across all projects on the Hub side. | ⏳ **Planned** |
| | | **P3-3: Automated Catalog Generation**<br>Keeping `ASSET_INDEX.md` up-to-date via `scan_assets.py`. | ✅ **Done** |
| **E4: Documentation** (Quality) | I want the documentation to remain current and concise, maintaining a structure where AI and humans don't get lost. | **P4-1: Establishment of Documentation Tiers**<br>Defining the roles of README, FEATURES, PROJECT_RULES, etc. | ✅ **Done** |
| | | **P4-2: Clear & Concise Writing Rules**<br>Formulating guidelines to prevent AI misinterpretation. | ✅ **Done** |

---

## 🛠️ Developer Stories (Internal Requirements)

Progress of technical stories:

- **D1: Tool-Neutral Interface**: Providing tools that don't depend on a specific agent. ✅ **Done**
- **D2: Atomic Replacement**: Editing logic that avoids destructive changes (e.g., using `str_replace`). ✅ **Done**
- **D3: Security Guard**: Guardrails to prevent accidental indexing of sensitive info. ✅ **Done**
