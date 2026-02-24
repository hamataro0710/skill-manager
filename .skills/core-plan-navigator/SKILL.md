---
name: plan-navigator
description: Provides a logical compass for the AI's "Plan mode," preventing superficial answers and guiding toward essential solutions. Specifically used in Specialist/Implementation roles to drive deep reasoning.
---

# 🧭 Plan Navigator

## ⚙️ Workflow Integration (SDE/Iterative)

| Workflow | Role of Plan Navigator | Primary User |
| :--- | :--- | :--- |
| **SDE** | Translates high-level specs from `doc-coauthoring` into a 5-phase execution strategy. | **Implementation** |
| **Iterative** | Bridges the gap between current state and desired outcome through logical iteration. | **Implementation** |

## 🧠 Thinking Process (MUST FOLLOW)
Following this flow during new development, debugging, or specification helps prevent shortcut responses.

```dsl
# 5-Phase Flow: EE→CD→CP→AE→AD
EE (EssenceExplore)      : Essence(Why) ⇔ Implementation(How) · Multi-layered establishment & complete purpose definition
CD (ChallengeDiscover)   : Assessment against defined purpose · Ideal ↔ Current gap structuring
CP (ChallengePrioritize) : Prioritization via Impact/Effort/Risk evaluation
AE (ApproachExplore)     : Systematic generation of 5+ methods · AxisBasedGeneration
AD (ApproachDecide)      : Multi-criteria final decision using IntegrationMatrix

# Phase Requirements
EE→CD: Complete Purpose Defined (Why⇔How mutual transcription) ∧ Theme Clarification
CD→CP: Status Assessment ∧ Gap Structuring ∧ Challenge Relationship Mapping
CP→AE: Impact/Effort/Risk Assessment ∧ Dependency Mapping ∧ Priority Finalization
AE→AD: 5+ Approaches Generated (incl. "skip" if applicable) ∧ Pros/Cons/Unknowns
AD→Exit: Multi-criteria Evaluation ∧ Implementation Plan ∧ Trade-off Documentation

# Core Principle
- If there is ambiguity, always ask the user; never proceed with assumptions.
```

---
(User Guide)
- Reference this skill when giving prompt instructions to an AI Agent.
- Effectively prevents "low-effort plans" by ensuring logical grounding.
- To modify or extend the thinking process, edit directly using the notation below:

```
# Notation Guide
#  A → B : Transition from phase A to B
#  A ∧ B : Both conditions A and B must be "Completed" (Logical AND)
#  A ⇔ B : Bi-directional mapping/transcription between A and B
#  A ↔ B : Gap or relationship between A and B
```
