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

1. **Ecosystem Synchronization**: Curates certified official repositories (Google, Anthropic, etc.) as **submodules** and scans them as needed via `scan_assets.py`. It ensures you stay at the forefront of AI evolution without manual research.
2. **Contextual Intelligence Mapping**: The **Asset Consultant** acts as both a strategic advisor (Diagnosis) and a process lead (Structure). It filters the vast catalog to identify, configure, and govern assets that fit your specific tech stack and project phase.
3. **Verified Knowledge Circulation**: A bi-directional flow where local breakthroughs are mapped to organizational patterns and shared back to the Hub. It transforms individual wins into a "Living Foundation" for the whole team.
4. **Agent-Agnostic Abstraction**: A symbolic link layer that maps agent-specific configurations (`.claude/`, `.agents/`, etc.) into a standardized structure. It allows you to swap "brains" (agents) while keeping your "tools" (skills) intact.
5. **Bridge-Link Architecture**: A parallel directory structure connecting the Hub and Projects. It keeps individual projects lightweight by injecting only the necessary intelligence on-demand, ensuring instant synchronization across the organization.

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

## 🛠️ Roadmap
For a detailed task list and current progress, please see **[todos.md](todos.md)**.

- [ ] **Diagnostic Mode**: Suggest missing capabilities via `Asset Consultant`.
- [ ] **Global Sync**: Visualize active capabilities across projects.

## 🏷️ Skill Naming Convention
`{source}-{repo_name}-{skill_name}` (e.g., `official-skills-anthropic-pdf-reader`)
