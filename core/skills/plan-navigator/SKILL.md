---
name: plan-navigator
description: Provides a logical compass for the AI's "Plan mode," preventing superficial answers and guiding toward essential solutions.
---

# 🧭 Plan Navigator

## 🧠 Thinking Process (MUST FOLLOW)
Following this flow during new development, debugging, or specification helps prevent shortcut responses.

```dsl
# 5-Phase Flow: EE→CD→CP→AE→AD
EE (EssenceExplore)      : Essence(Why) ⇔ Implementation(How) · Full purpose definition
CD (ChallengeDiscover)   : Assessment against defined purpose · Ideal ↔ Current gap structuring
CP (ChallengePrioritize) : Prioritization via Impact/Effort/Risk evaluation
AE (ApproachExplore)     : Systematic generation of 5+ methods · AxisBasedGeneration
AD (ApproachDecide)      : Multi-criteria final decision using IntegrationMatrix

# Phase Requirements
EE→CD: Essential Purpose Defined (Why⇔How mapping) ∧ Theme Clarification
CD→CP: Status Assessment ∧ Gap Structuring ∧ Challenge Mapping
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
#  A ⇔ B : Bi-directional mapping/translation between A and B
#  A ↔ B : Gap or relationship between A and B
```
