# 🧩 アクティブ・アセット (能力マップ)

このファイルは、本プロジェクトに現在配備されているエージェントの知能とツールを文書化したものです。**Agent Governor** によって管理されています。

## 🗺️ インテリジェンス・フロー (プロジェクト・ライフサイクル)

```mermaid
graph TB
    %% Horizontal Flow
    subgraph Flow [1. ワークフロー・フェーズ]
        direction LR
        F1[プロジェクト計画] --> F2[開発] --> F3[テスト] --> F4[デプロイ]
    end

    %% Role-Specific Specialist Skills
    subgraph RoleSkills [2. スペシャリスト・スキル]
        direction LR
        S1[計画/管理<br/>(Planner, Notion, Linear)] --- S2[実装エージェント<br/>(Swarm 等)] --- S3[検証スキル<br/>(Skill Creator 等)] --- S4[アクション・エンジン<br/>(GitHub 等)]
    end

    %% Base Intelligence (Common/Setup)
    subgraph Foundation [3. 共通基盤 & セットアップ]
        direction LR
        B1[論理的羅針盤:<br/>Plan Navigator] --- B2[ドキュメント定義:<br/>Co-authoring] --- B3[ガバナンス:<br/>Agent Governor] --- B4[セットアップ/導入:<br/>Asset Consultant]
    end

    %% Vertical Alignment (Visual Mapping)
    F1 --- S1
    F2 --- S2
    F3 --- S3
    F4 --- S4
    
    RoleSkills --- Foundation

    %% Styles
    classDef phase fill:#fff,stroke:#333,stroke-width:2px;
    classDef skill fill:#f9f,stroke:#333,stroke-width:1px;
    classDef base fill:#dfd,stroke:#333,stroke-width:2px;
    
    class F1,F2,F3,F4 phase;
    class S1,S2,S3,S4 skill;
    class B1,B2,B3,B4 base;
```

## 📋 ロール & スキル・マッピング

| カテゴリ | 主要アセット | 根拠 |
| :--- | :--- | :--- |
| **共通基盤 (Setup & Base)** | `plan-navigator`, `doc-coauthoring`, `agent-governor`, `asset-consultant` | **Hubと現場を繋ぐインフラ。** 論理的な深さ、ドキュメント標準、環境の完全性、そして新しい能力を導入する力を提供します。 |
| **プロジェクト計画** | `microsoft-planner`, `openai-notion-spec`, `openai-linear` | 要件の分析、実装計画の作成、および Notion/Linear を使用したタスク/バックログ管理。 |
| **開発** | `swarm` (マルチエージェント) | 役割ベースの専門エージェントによる複雑な実装タスクの実行。 |
| **テスト** | `skill-creator`, `plan-navigator` (TDD) | ロジックの検証とエージェント行動の洗練による品質保証。 |
| **デプロイ** | `mcp-smithery-github` | PR、Issue、GitHub Actions を介した本番環境とのインタラクション。 |

## ⚙️ プロフェッショナル・ワークフロー
- **Spec-Driven Evolution (SDE)**: `openai-notion-spec` を使用して PRD/仕様書を具体的な実装計画に橋渡しし、計画からデプロイまでの進化を駆動します。
- **反復的検証 (Iterative Validation)**: ライフサイクルの各段階において「理想 ↔ 現状」のギャップを埋めるための継続的な検証を行います。

## 📋 アセット・レジストリ

| 名前 | カテゴリ | ワークフローにおける役割 | 根拠 |
| :--- | :--- | :--- | :--- |
| **core-plan-navigator** | Expertise | **共通基盤** | 5段階の深い推論を保証し、浅いショートカットを防止します。 |
| **official-skills-anthropic-doc-coauthoring** | Expertise | **共通基盤** | 高品質なドキュメント執筆と仕様策定のためのプロトコルです。 |
| **core-agent-governor** | Governance | **共通基盤** | 環境の維持、インデックスの同期、リポジトリの完全性を保証します。 |
| **core-asset-consultant** | Orchestrator | **共通基盤** | Hubからの資産探索、設計、インポートの主要インターフェースです。 |
| **official-microsoft-planner** | Expertise | **計画** | コードを一切変更せずに、詳細な実装計画を作成する計画スペシャリストです。 |
| **official-openai-notion-spec** | Expertise | **計画 / SDE** | Notion上の仕様を実装プラン、タスク、および進捗管理に変換します。 |
| **official-openai-linear** | Tool | **計画** | Linear で Issue、プロジェクト、およびチームのワークフローを管理します。 |
| **official-agents-openai-swarm** | Orchestrator | **開発** | 複雑な実行タスクのための専門エージェント構成を可能にします。 |
| **3rdparty-mcp-smithery-github** | Tool | **デプロイ** | GitHubのPRやIssueと直接やり取りする能力を付与します。 |
| **official-mcp-modelcontext-memory** | Tool | **全般** | 意思決定を想起するための永続メモリを提供します。 |
| **official-skills-anthropic-skill-creator** | Expertise | **テスト / 進化** | 新しいスキルの作成・洗練のための標準ガイドです。 |
