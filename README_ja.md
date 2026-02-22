# Skill-Manager

**組織全体の AI エージェント資産（スキル、ツール、設定）を統合し、公式および社内スキルの配布とメンテナンスを効率化するための管理フレームワーク。**

## 🌟 ビジョン

`Skill-Manager` は、各種 AI エージェント（Gemini, Claude, Codex など）が要求するディレクトリ構造やパスの微妙な違いを吸収し、**「ユーザーが好みのエージェントを使いながら、組織のナレッジ（スキル）をシームレスに共有・再利用できる」**環境を提供します。

## 🏗️ アーキテクチャ: 並列接続モデル

`Skill-Manager` は、並列なディレクトリ構造を通じて、ローカルプロジェクトとグローバルな資産リポジトリ（ハブ）を接続します。**Asset Consultant** は、ハブとプロジェクトの双方に配備され、アセットやリソースの管理と同期を担います。

![Architecture Overview](docs/architecture-overview.drawio.png)

### 🧠 コア・コンセプト

- **並列ディレクトリ構造**: グローバルハブとターゲットプロジェクトは、ファイルシステム上で並列に配置され、相互に連携します。
- **Asset Consultant の同期**: ハブとプロジェクトの双方に配備された `Asset Consultant` が、共通のインデックスとローカルの文脈を同期します。
- **オンデマンドなインポート**: 必要なスキルのみをハブのレジストリからプロジェクトの `.skills/` ディレクトリへ選択的に導入します。
- **自動化されたガバナンス**: `Agent Governor` がアセットインデックスと配備状況を常時監査し、整合性を維持します。

### 📂 ディレクトリ構成イメージ (Mental Model)

グローバルハブとローカルプロジェクトの関係：

```text
{path}/{to}/{parent}/
├── skill-manager/                # 【Global Hub / Source】
│   ├── .skills/                  #
│   │   ├── ASSET_INDEX.md        # AIが資産を発見するためのマスターカタログ
│   │   └── core-asset-consultant/# 知的な架け橋（ソース）の実体
│   ├── core/
│   │   └── tools/                # デプロイツール (import_skill.py, setup_project.py)
│   ├── officials/                # Google, Anthropic 等の公式スキル
│   └── org/                      # 社内共通スキル
│
└── my-target-project/            # 【Local Work / Destination】
    ├── .env                      # SKILL_MANAGER_ROOT={hubの絶対パス} を保持
    ├── PROJECT_RULES.md          # プロジェクト固有の共通ルール
    ├── AGENTS.md                 # 🔗 PROJECT_RULES.md へのリンク
    ├── CLAUDE.md                 # 🔗 PROJECT_RULES.md へのリンク
    ├── .skills/                  # インポートされたスキルの実体
    │   └── core-asset-consultant/ # 現場に常駐する「知的な架け橋」
    ├── .agents/skills/           # 🔗 .skills/ へのリンク (Gemini用)
    └── .claude/skills/           # 🔗 .skills/ へのリンク (Claude用)
```

## 🚀 はじめかた (Bootstrap Workflow)

`skill-manager` ディレクトリから、わずか 2 ステップでターゲットプロジェクトをセットアップできます。

1.  **ハブの準備**:
    ```bash
    git clone --recursive {this-repo-url}
    cd skill-manager
    python3 core/tools/scan_assets.py
    ```

2.  **ターゲットプロジェクトの初期化**:
    ```bash
    python3 core/tools/setup_project.py --repo {your-target-project-path} --name "My Project"
    ```
    *これにより、`.env` の構成、ディレクトリ構造の作成、および `Asset Consultant` のデプロイが自動的に行われます。*

## ✨ コア・バリュー
1.  **脱・断片化 (Anti-Fragmentation)**: シンボリックリンク層により、エージェントごとのパスの違いを吸収。
2.  **メンテナンス優先 (Maintenance-First)**: 複雑な UI よりも「どのスキルが信頼できるか」「どう維持するか」の構造を重視。
3.  **共同防御 (Collaborative Defense)**: 各社の公式リポジトリをサブモジュールとして統合し、安全な資産のみをピックアップ可能。

## 🚀 ロードマップ
- [x] **ブリッジ・アーキテクチャ**: グローバルハブとローカルプロジェクトの動的連携。
- [x] **自動導入フロー**: 単一コマンドによるターゲットプロジェクトのセットアップ。
- [ ] **診断モード (Diagnostic)**: `asset-consultant` による不足能力の自動スキャンと提案の強化。
- [ ] **グローバル同期**: `ACTIVE_ASSETS.md` を通じた複数プロジェクト間の能力の可視化。

## 🏷️ スキル命名規則
衝突を避け、出所を明確にするため以下の形式を推奨します：
`{source}-{repo_name}-{skill_name}` (例: `official-skills-anthropic-pdf-reader`)
