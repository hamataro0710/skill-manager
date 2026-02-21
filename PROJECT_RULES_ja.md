# Project Rules (Source of Truth) - Skill-Manager

This file is the single source of truth for all AI agents working on this project.

## 📖 Project Overview
- **Name**: Skill-Manager
- **Description**: AIエージェントの資産（スキル、ツール、設定）を一元管理するためのフレームワーク。
- **Core Principle**: **"Agent-Neutral & Minimal Pollution"**
  - 特定のツール固有の隠しディレクトリ（`.gemini/`, `.claude/` 等）を最小限に抑え、可能な限り共通の標準ディレクトリ構造で資産を管理します。

## 🤖 Agent Behavior Guidelines
エージェントは以下のガイドラインに従って行動してください。

### 1. ツール固有フォルダの生成禁止
- 新しいツールを導入する際、ツール独自の `.xxx/` フォルダを安易に作成しないでください。
- 既存の `.skills/`, `tools/`, `blueprints/` などの共通フォルダに機能を統合することを優先してください。

### 2. シングル・ソース・オブ・トゥルース（SSoT）の維持
- `AGENTS.md`, `CLAUDE.md`, `COPILOT.md` 等は、常に `PROJECT_RULES.md` へのシンボリックリンクとしてください。
- 設定の変更は必ず `PROJECT_RULES.md` に対して行い、個別の設定ファイルを書き換えてはいけません。

### 3. 中立的なパス参照
- スキルの実体は常に `.skills/` 直下を参照してください。
- エージェント固有のパス（`.agents/skills/` 等）を「実体」として認識したり、そこへ直接ファイルを書き込んだりしないでください。

### 4. シンボリックリンクによる相互運用
- 複数のツールで同じファイルを共有する場合、コピーではなくシンボリックリンク（相対パス）を活用してください。

## 📂 Directory Roles
- `core/`: **[実体]** Skill-Manager 自体のコア資産（ツール、スキル、テンプレート）。
  - `core/skills/`: 組み込みスキル（`skill-picker` 等）の実体。
  - `core/tools/`: 管理用スクリプト（`import-skill.py` 等）の実体。
  - `core/blueprints/`: 構成テンプレート（`PROJECT_RULES.md` 等）の実体。
- `.skills/`: **[実体]** プロジェクト固有、または Pickup したスキルの実体（コアスキルへのリンクを含む）。
- `tools/`: `core/tools/` へのショートカット（シンボリックリンク）。
- `officials/`, `org/`, `3rdparty/`: **[供給源]** git submodule で管理されるスキル、ツールの集合体。
  - 探しやすさ（Discovery）のため、ディレクトリ名は `{カテゴリ}-{ベンダー}` のプレフィックス形式を遵守してください：
    - `agents-*`: マルチエージェントのオーケストレーション、タスク委譲、エージェントロジックのフレームワーク（例: `agents-langchain`, `agents-microsoft-autogen`）。
    - `mcp-*`: Model Context Protocol に基づく実ツールの実装（例: `mcp-modelcontext`, `mcp-google`）。
    - `skills-*`: 特定の AI モデル向けのガイド、プロンプト集、振る舞い設定（例: `skills-anthropic`, `skills-gemini`）。
    - `blueprints-*`: プロジェクト構成や設定のテンプレート。

## 🛠 Operation Workflows
- **Sync**: `git submodule update` を使用。
- **Import**: `tools/import-skill.py` を介して `.skills/` へ。
- **Apply**: `tools/setup-project.py` を介して他プロジェクトへリンクを張る。

## ✍️ Coding Standards
- **Naming**: `{source}-{repo}-{skill_name}` を遵守。
- **Portability**: ツール固有の絶対パスをハードコードせず、プロジェクトルートからの相対パスを使用する。
