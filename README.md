# Skill-Manager

**組織内の複数AIエージェント（Gemini, Claude等）の管理を共通化し、公式・社内・組織内スキルの配布とメンテナンスを効率化するための管理フレームワーク**

## 📖 概要 (Overview)

AIエージェントの導入が進む組織において、「エージェントごとに異なるツール定義」や「開発チームごとの車輪の再発明」が大きな管理コストとなっています。

このリポジトリは、各社の公式リポジトリを **Submodules** として一元管理し、さらに組織独自（Internal）のスキルを共通化することで、以下の価値を提供します：

1.  **Multi-Agent Efficiency (複数エージェントの効率化)**: Gemini CLI (`.agents/`) と Claude Code (`.claude/`) など、異なるエージェント間で同じスキル定義をシンボリックリンクで共有。一箇所の修正がすべてのエージェントに即座に反映されます。
2.  **Organizational Standardization (組織標準化)**: `org/skills/` を通じて、社内共通のプロンプトエンジニアリング、命名規則、セキュリティポリシーを適用した「認定スキル」を各プロジェクトへ迅速に配布します。
3.  **Latest Catch-up (公式追従)**: 膨大な公式スキル群（OpenAI, Google, Anthropic等）を常に同期し、プロジェクト要件にマッチする最適な機能を検索・選定（Pickup）できる状態を維持します。

## 📂 ディレクトリ構成 (Structure)

```text
.
├── core/                # [実体] Skill-Manager 自体のコア資産 (Tools, Skills, etc.)
│   ├── skills/          # 組み込みスキルの実体 (skill-picker)
│   ├── tools/           # 管理用スクリプトの実体
│   └── blueprints/      # 各プロジェクト用設定の雛形
├── .skills/             # [実体] プロジェクトで Pickup したスキルの実体
│   └── skill-picker/    # core/skills/skill-picker へのリンク
├── tools/               # core/tools へのシンボリックリンク
├── .agents/skills/      # Gemini CLI 用窓口 (../.skills へのリンク)
├── .claude/skills/      # Claude Code 用窓口 (../.skills へのリンク)
├── org/skills/          # 組織内 (社内・チーム内) で共通利用・配布するスキル
├── 3rdparty/{repo}/     # サードパーティの各リポジトリ (Git Submodules 等)
├── officials/           # 各社の公式リポジトリ (Git Submodules)
└── README.md
```

### ✨ 組織導入のメリット：メンテナンスの効率化
本フレームワークでは、エージェントごとの設定を個別にメンテナンスする必要はありません。

- **シングル・ソース・オブ・トゥルース**: スキルの実体はすべて中立的な `.skills/` で管理され、各エージェント（`.agents/`, `.claude/`）からはリンクを貼るだけです。
- **指示書の一元化**: プロジェクトの基本ルール（`PROJECT_RULES.md`）を `AGENTS.md` や `CLAUDE.md` から参照させることで、エージェントの種類を問わず一貫した振る舞いを保証します。
- **スキルのポータビリティ**: `org/skills/` に定義された社内共通ツールは、どのプロジェクトでも同じコマンド（`python tools/import-skill.py`）で即座に導入可能です。

**一元管理のセットアップ:**
```bash
python tools/setup-project.py --repo {your-project-path} --name "My Project"
```
実行後、ターゲットプロジェクトには以下のリンクが自動作成され、複数エージェント対応が即座に完了します：
- `AGENTS.md` -> `PROJECT_RULES.md`
- `CLAUDE.md` -> `PROJECT_RULES.md`

### 🏷️ スキル命名規則 (Naming Convention)
組織全体でスキルの衝突を避け、出自を明確にするために、以下の形式で管理することを推奨しています。

`{source}-{repo_name}-{skill_name}`

- **例**: `official-claude-skills-mcp-builder` (公式からの配布)
- **例**: `org-internal-security-audit` (組織内共通)
- **例**: `3rdparty-awesome-tools-translator` (外部リポジトリ)

- **Pickup**: 大規模な `officials/` から必要なものだけをプロジェクトにコピー。
- **Share**: 便利なスキルを `org/` や `3rdparty/` に集約し、チームやコミュニティ間で再利用可能。
- **Auto-Sync**: 実体を一箇所修正すれば、リンクを介してすべてのエージェントに即座に反映されます。

ご利用のプロジェクトでも、このシンボリックリンク構造を自動設定する仕組みを提供します。

## 利用方法
### 🚀 セットアップ (Getting Started)
このリポジトリは外部の公式リポジトリをサブモジュールとして参照しているため、--recursive オプションを使用したクローンが必要です。

### プロジェクトごとにskillsを管理する場合

```text
{your-project}
├── .agents/
│   └── skills/              # エージェント用スキル (シンボリックリンク)
│       └── {picked-skill}/
├── .claude/
│   └── skills/          # .skills/ へのシンボリックリンク
├── .skills/             # スキル定義の実体
│   └── {picked-skill}/
└── {your-files}
```
