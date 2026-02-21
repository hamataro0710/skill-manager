---
name: plan-navigator
description: AIの「Planモード」に論理的な羅針盤を与え、短絡的な回答を防いで本質的な解決策へと導く思考ナビゲーター。
---

# 🧭 Plan Navigator

## 🧠 思考プロセス（MUST FOLLOW）
新規開発やdebug, 仕様策定の際などにフローに沿うことで短絡的な回答を防ぐことができます。

```dsl
# 5-Phase Flow: EE→CD→CP→AE→AD
EE (EssenceExplore)      : 本質(なぜ)⇔展開(どう)の複層的確立・真の目的完全確定
CD (ChallengeDiscover)   : 確定目的基準での現状評価・理想↔現状ギャップ構造化
CP (ChallengePrioritize) : Impact/Effort/Risk評価による優先順位付け
AE (ApproachExplore)     : 5+手法の体系的生成・AxisBasedGeneration
AD (ApproachDecide)      : IntegrationMatrix使用の多基準最終決定

# Phase Requirements
EE→CD: 真の目的完全確定(Why⇔How相互転写) ∧ テーマ明確化
CD→CP: 現状評価 ∧ ギャップ構造化 ∧ Challenge関係マップ作成
CP→AE: 影響度・工数・リスク評価 ∧ 依存関係整理 ∧ 優先順位確定
AE→AD: アプローチ5+生成 ("skip"等も考慮) ∧ Pros/Cons/Unknowns
AD→Exit: 多基準評価 ∧ 実装計画 ∧ トレードオフ文書化

# Core Principle
- 曖昧さがあれば必ずユーザーに問い、仮定で進めないこと。
```

---
(ユーザー向け説明)
- AI Agentにプロンプト指示を出す際に参照させて利用してください。
- 「なんとなくのプラン」を防ぎ、論理的な裏付けを持たせるために有効です。
- 思考プロセスの変更・拡張は、下記の記号法に従って直接編集してください。
```
# Notation Guide
#  A → B : フェーズAからBへの遷移
#  A ∧ B : AとBの両方の条件を「完了」する必要がある (Logical AND)
#  A ⇔ B : AとBの双方向の対応付け・転写
#  A ↔ B : AとBの間のギャップや関係性
```
