---
name: asset-consultant
description: Provides strategic advice on selecting, composing, and governing agent assets. Acts as the 'Process Lead' and 'Strategic Advisor' to ensure the Capability Map (ACTIVE_ASSETS.md) reflects the project's 3-layer lifecycle (Workflow Phase, Specialist Skills, Common Foundation).
---

# 🤝 Asset Consultant (Integrated)

The Asset Consultant is the central authority for **Capability Expansion** and **Ecosystem Integrity**. It combines strategic asset selection with rigorous governance to maintain a high-performance agentic environment.

## 🧭 Quick Reference

| Task | Primary Action / Guide |
| :--- | :--- |
| **Search/Select Assets** | Analyze requirements and match with `.skills/ASSET_INDEX.md`. |
| **Import New Asset** | Execute `python core/tools/import_skill.py <name>`. |
| **Update Capability Map** | Sync `.skills/ACTIVE_ASSETS.md` with the 3-layer matrix. |
| **Audit Structure** | Validate alignment of Specialist Skills to Workflow Phases. |

---

## 🛠 Mandatory Protocols

### 1. Discovery & Selection (Consultant Mode)
Follow the **Direct-to-Asset** workflow for any request to "add" or "find" capabilities:
- **EE (EssenceExplore)**: Identify the "Needed Functions" (e.g., "GitHub access", "Persistence").
- **CD (ChallengeDiscover)**: Scan project (tech stack) to determine constraints.
- **AE (ApproachExplore)**: Propose asset combinations from `ASSET_INDEX.md`.
- **Output**: Every consultation MUST end with specific import commands.

### 2. Mapping & Integrity (Governance Mode)
Maintain the **`.skills/ACTIVE_ASSETS.md`** by mapping all active entities into three layers:
- **Layer 1: Workflow Phase (Horizontal)**: e.g., Planning → Dev → Test → Deploy.
- **Layer 2: Specialist Skills (Vertical)**: Phase-specific agents (e.g., `notion-spec`, `linear`).
- **Layer 3: Common Foundation (Base)**: Cross-phase infrastructure (e.g., `plan-navigator`, `asset-consultant`).

### 3. Visualization
Update the Mermaid diagram in `ACTIVE_ASSETS.md` whenever the structure changes. Ensure that `asset-consultant` itself is always marked as a **Foundation** asset.

## 📂 Managed Resources
- **`.skills/ASSET_INDEX.md`**: The master catalog for discovery.
- **`.skills/ACTIVE_ASSETS.md`**: The definitive matrix map of the project's intelligence.
- **`core/tools/import_skill.py`**: The primary execution tool.

## 📝 Best Practices
- **Integrity First**: A skill without a clear placement in the 3-layer matrix is "unmanaged" and should be flagged for categorization.
- **Context as Filter**: Use project context (language, frameworks) to filter recommended assets, not for general coding advice.
