# Skill-Manager

**A management framework for unifying AI agent assets (skills, tools, and configurations) across organizations, streamlining the synchronization, curation, and circulation of official and internal intelligence.**

## 🌟 Vision

`Skill-Manager` abstracts the complexities of AI agent implementations, providing an environment where **"teams can use their preferred agents to access context-aware organizational knowledge while staying in sync with the latest AI evolution."**

## 🎯 Why Skill-Manager? (Jobs to be Done)

Skill-Manager doesn't just manage files; it automates the "progress" of your AI agent workflows.

1. **"Stay ahead via Ecosystem Sync (Stay Updated)"**
   - **Job:** Instantly inject the latest "best practices" (prompts, tool definitions, MCP configs, implementation patterns) from official sources (Google, Anthropic, etc.) into your local projects.
   - **Value:** Zero-effort sync with the fast-moving ecosystem. Your agent is always "up-to-date and at its smartest."

2. **"Contextual Alignment & Diagnostics (Tailored Intelligence)"**
   - **Job:** Let the AI analyze your tech stack and domain to suggest and auto-configure only the most relevant assets from the vast catalog.
   - **Value:** Eliminates the "blank page" problem. Your agent starts with a deep understanding of *your* environment, rather than just being a generic assistant.

3. **"Knowledge Circulation & Sharing (Break down Silos)"**
   - **Job:** Effortlessly share successful local patterns (prompts, tools, rules) with the entire organization, allowing other teams to benefit from your innovation instantly.
   - **Value:** Replaces "Knowledge Monopolies" with a "Shared Wisdom Loop." Ensures that a win in one project becomes a starting point for everyone else, maximizing the ROI of every internal development effort.

4. **"Agent Agility & Task-Specific Optimization (Anti Lock-in)"**
   - **Job:** Flexibly switch or combine multiple AI agents (Claude, Gemini, etc.) within a single project, utilizing each one's unique strengths without re-configuring your assets.
   - **Value:** Breaks agent lock-in. Your organizational knowledge and tools remain a constant foundation, even as you swap the underlying "brain" to match the specific requirements of the task.

## 🏗️ Architecture: Parallel & Connected Model

`Skill-Manager` connects local projects to a global asset repository through a parallel directory structure. The **Asset Consultant** is deployed in both the Hub and the Target Project to manage and synchronize assets and resources across the workspace.

![Architecture Overview](docs/architecture-overview.drawio.png)

### 🧠 Core Concepts

- **Parallel Structure**: The Hub (source) and Target Project (work_dir) reside on the same filesystem level, linked via configuration.
- **Dual-Resident Consultant**: The `Asset Consultant` operates in both environments, maintaining a synchronized view of global assets and local context.
- **On-Demand Importing**: Skills are selectively imported from the Hub's registry into the project's `.skills/` directory as needed.
- **Automated Governance**: The `Agent Governor` continuously audits the asset index and active deployments to ensure system integrity.

### 📂 Directory Structure (Logical Concept)

`Skill-Manager` maintains a clear separation between common assets and project-specific work:
- **Global Hub**: A central repository of skills (officials, internal, and 3rd-party).
- **Target Project**: Your local workspace that imports only the necessary skills.

For a detailed physical directory structure and the "Bridge-Link Model" explanation, please refer to **[Architectural Design & Strategy](docs/architectural-design.md)**.

## 🚀 Getting Started (Bootstrap Workflow)

You can set up a target project in two steps from the `skill-manager` directory:

1.  **Prepare the Hub**:
    ```bash
    git clone --recursive {this-repo-url}
    cd skill-manager
    python3 core/tools/scan_assets.py
    ```

2.  **Initialize Target Project**:
    ```bash
    python3 core/tools/setup_project.py --repo {your-target-project-path} --name "My Project"
    ```
    *This will automatically configure `.env`, create the directory structure, and deploy the `Asset Consultant`.*

## ✨ Core Values
1.  **Anti-Fragmentation**: Absorbs subtle path differences through a symbolic link layer.
2.  **Maintenance-First**: Prioritizes structure and trust over complex UIs.
3.  **Collaborative Defense**: Curates certified official assets (Google, Anthropic, etc.) as submodules.

## 🛠️ Roadmap
For a detailed task list and current progress, please see **[todos.md](todos.md)**.

- [x] **Bridge Architecture**: Dynamic link between Global Hub and Local Projects.
- [x] **Auto-Bootstrap**: Single-command setup for target projects.
- [ ] **Diagnostic Mode**: Suggest missing capabilities via `Asset Consultant`.
- [ ] **Global Sync**: Visualize active capabilities across projects.

## 🏷️ Skill Naming Convention
`{source}-{repo_name}-{skill_name}` (e.g., `official-skills-anthropic-pdf-reader`)
