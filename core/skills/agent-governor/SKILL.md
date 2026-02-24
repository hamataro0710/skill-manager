---
name: agent-governor
description: Orchestrates agentic governance by mapping assets to a 3-layer lifecycle structure (Workflow Phase, Specialist Skills, Common Foundation). Acts as the 'Process Lead' to ensure the Capability Map (ACTIVE_ASSETS.md) accurately reflects the project's strategic and execution layers.
---

# 🛡️ Agent Governor (Intelligence Governance)

The Agent Governor is the central authority for maintaining the **Observability** and **Integrity** of the agentic ecosystem. it ensures that every deployed asset is aligned within a **3-Layer Lifecycle Matrix**.

## 🧭 Mandatory Protocol

### 1. Identify Context (Ask the User)
Before updating the Map, you **must** confirm the project's nature to align the lifecycle phases.
- **Project Type**: Is this Software Development, Strategic Consulting, Academic Research, or something else?
- **Workflow Phases**: Confirm if the standard phases (Planning → Development → Test → Deployment) fit the project.
- **Primary Goal**: What is the "Ideal State" we are trying to reach?

### 2. Audit & Map (3-Layer Alignment)
Maintain the **`.skills/ACTIVE_ASSETS.md`** by mapping all active entities into the following layers:

- **Layer 1: Workflow Phase (Horizontal)**
    - Map the project lifecycle (e.g., Planning → Development → Test → Deployment).
- **Layer 2: Specialist Skills (Vertical/Specific)**
    - Assign phase-specific agents and tools (e.g., Swarm for Development, Skill Creator for Test).
- **Layer 3: Common Foundation & Setup (Base Infrastructure)**
    - Place core infrastructure assets that span all phases (e.g., Plan Navigator, Doc Co-authoring, Agent Governor, Asset Consultant).

### 3. Visualize the Lifecycle Matrix
Update the Mermaid diagram in `ACTIVE_ASSETS.md` to reflect this matrix.
- **Horizontal Flow**: Visualize the phase transitions.
- **Vertical Alignment**: Show which specialist skills support which phases.
- **Foundation Support**: Visualize the core infrastructure supporting the entire lifecycle.

## 📂 Managed Files (within .skills/)
- **`ACTIVE_ASSETS.md`**: The definitive matrix map of phases, specialist skills, and foundations.
- **`ASSET_INDEX.md`**: The full catalog of potential assets for discovery.

## 🛠 Usage Trigger
- **Environmental Change**: Run after importing new skills or changing the project's lifecycle phases.
- **Capability Inquiry**: Run whenever the user asks "How is our intelligence structured?" or "What tools support which phase?"

## 📝 Best Practices
- **Infrastructure First**: Ensure `agent-governor` and `asset-consultant` are always recognized as **Foundation** assets, as they manage the environment itself.
- **Functional Integrity**: A skill without a clear placement in the 3-layer matrix is considered "unmanaged" and should be flagged.
