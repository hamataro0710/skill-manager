# Skill-Manager

**組織内の複数AIエージェントの管理を共通化し、公式・社内スキルの配布とメンテナンスを効率化するための管理フレームワーク**

## 🌟 ビジョン (Vision)

AI開発の速度は凄まじく、個人の努力だけで最新のスキル定義やツールセットに追従し続けることは困難になりつつあります。また、ユーザーごとに好みのAIエージェント（Gemini, Claude, Codex等）は異なりますが、それぞれが要求する微細なディレクトリ構造やパスの違いが、資産の再利用を妨げる壁となっています。

`Skill-Manager` は、これらの差異を抽象化して吸収し、**「個人の好みのエージェントを使い分けつつ、組織の知見をシームレスに共有・再利用できる環境」**を提供します。

### 核心となる価値
1.  **Anti-Fragmentation (断片化の防止)**: エージェントごとの微細なパスの違い（`.agents/`, `.claude/`等）をシンボリックリンク層で吸収し、一つのスキル定義をあらゆるエージェントで使い回せるようにします。
2.  **Maintenance-First Architecture (メンテナンス重視の構成)**: 複雑なツールやUIを提供することよりも、「どのスキルが信頼できるか」「どう維持管理するか」という構造（Architecture）の提供を優先します。
3.  **Collaborative Defense (組織による追従)**: 公式リポジトリ（Google, Anthropic, OpenAI等）をサブモジュールとして統合し、セキュリティ懸念のない「認定済み公式資産」をチームで効率的に選定（Pickup）できる状態を維持します。

## 📂 ディレクトリ構成 (Structure)

```text
.
├── core/                # [実体] Skill-Manager 自体のコア資産 (Tools, Skills, etc.)
│   ├── skills/          # 組み込みスキルの実体 (skill-picker)
│   ├── tools/           # 管理用スクリプトの実体
│   └── blueprints/      # 各プロジェクト用設定の雛形
├── .skills/             # [実体] プロジェクトで Pickup したスキルの実体
├── tools/               # core/tools へのシンボリックリンク
├── .agents/skills/      # Gemini CLI 用窓口 (../.skills へのリンク)
├── .claude/skills/      # Claude Code 用窓口 (../.skills へのリンク)
├── org/skills/          # 組織内 (社内・チーム内) で共通利用・配布するスキル
├── 3rdparty/{repo}/     # サードパーティの各リポジトリ (Git Submodules 等)
├── officials/           # 各社の公式リポジトリ (Git Submodules)
└── README.md
```

## 🚀 ロードマップ (Roadmap)
- [x] **Multi-Agent Support**: Gemini, Claude, Codex(OpenAI) の最低ラインの対応。
- [ ] **Personality Extension**: 特定の役割（人格）を持つ Sub-agent の定義を共通化し、配布可能にする。
- [ ] **Skill Discovery**: 膨大な公式スキル群から、用途に最適なものをより容易に選定できる仕組みの強化。
- [ ] **Organizational Templates**: `org/skills/` 配下で、社内標準のプロンプトや命名規則を自動適用するテンプレート。

## ✨ 組織導入のメリット
- **シングル・ソース・オブ・トゥルース**: スキルの実体はすべて中立的な `.skills/` で管理され、各エージェント（`.agents/`, `.claude/`）からはリンクを貼るだけです。
- **指示書の一元化**: `AGENTS.md` や `CLAUDE.md` を `PROJECT_RULES.md` へのリンクにすることで、エージェントを問わず一貫した振る舞いを保証します。
- **ポータビリティ**: `org/skills/` に定義された社内共通ツールは、どのプロジェクトでも同じコマンドで即座に導入可能です。

**一元管理のセットアップ:**
```bash
python tools/setup-project.py --repo {your-project-path} --name "My Project"
```

## 🏷️ スキル命名規則 (Naming Convention)
組織全体でスキルの衝突を避け、出自を明確にするために、以下の形式で管理することを推奨しています。
`{source}-{repo_name}-{skill_name}`

- **例**: `official-claude-skills-mcp-builder` (公式からの配布)
- **例**: `org-internal-security-audit` (組織内共通)
- **例**: `3rdparty-awesome-tools-translator` (外部リポジトリ)

## 🚀 セットアップ (Getting Started)
このリポジトリは外部の公式リポジトリをサブモジュールとして参照しているため、`--recursive` オプションを使用したクローンが必要です。
