---
name: agent-governor
description: Orchestrates agentic governance by synchronizing the asset index and visualizing active capabilities via .skills/ACTIVE_ASSETS.md. Use this to maintain the AI's "eyes" and audit the project's agentic ecosystem.
---

# 🛡️ Agent Governor (Intelligence Governance)

The Agent Governor is the central authority for maintaining the **Observability** and **Integrity** of the agentic ecosystem. It ensures the AI has a clear view of available tools and a documented understanding of active capabilities.

## 🧭 Mandatory Protocol

### 1. Synchronize Sight (Index)
Before any audit, ensure the AI's "eyes" are fresh.
- **Action**: Run `python3 core/tools/scan-assets.py`.
- **Insight**: Read `.skills/ASSET_INDEX.md` and report any new discoveries found in `.skills/ASSET_DIFF.md`.

### 2. Audit Deployment (Active Assets)
Examine the `.skills/` directory to see what is actually deployed.
- **Action**: List all entities in `.skills/`.
- **Rationale**: Update **`.skills/ACTIVE_ASSETS.md`** with the role and rationale for each asset in the current project context.

### 3. Visualize & Record
Ensure the relationship between Orchestrators, Tools, and Expertise is clear.
- **Action**: Use Mermaid diagrams in `.skills/ACTIVE_ASSETS.md` to map the capability flow.

## 📂 Managed Files (within .skills/)
- **`ASSET_INDEX.md`**: The full catalog of potential assets.
- **`ASSET_DIFF.md`**: Recent changes in the asset library.
- **`ACTIVE_ASSETS.md`**: The definitive map of currently deployed capabilities.

## 🛠 Usage Trigger
- **After Update**: Run whenever submodules are updated or new skills are imported.
- **System Check**: Run whenever the user asks "What can you do?" or "How are you configured?"

## 📝 Best Practices
- **Proactive Reporting**: Always mention new assets from `ASSET_DIFF.md` to keep the user informed.
- **Contextual Integrity**: Ensure every active asset has a defined "Why" in the ACTIVE_ASSETS.md.
