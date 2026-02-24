# 📋 Skill-Manager Implementation Roadmap

このドキュメントは、`Skill-Manager` (Global Hub) と `Target Project` (Local Work) を繋ぐアーキテクチャを実現するためのタスクリストです。

---

## 🚀 依存関係フロー (Dependency Graph)
1. **[P1] Foundation** (パス固定・ツール汎用化)
   ↓
2. **[P2] Intelligence** (知能のデプロイ・環境適応プロンプト)
   ↓
3. **[P3] Enhancement** (診断機能・同期管理)

---

## 🛠️ タスクリスト

### 【P1】接続基盤の構築 (The Bridge Foundation)
- [x] **P1-1: `setup_project.py` の拡張**
  - ターゲットプロジェクトの `.env` に `SKILL_MANAGER_ROOT` (Hubの絶対パス) を書き込む機能を追加。
  - ターゲット側に `.skills/` ディレクトリを自動作成する。
- [x] **P1-2: 既存ツールのパス解決ロジック修正**
  - `import_skill.py`, `scan_assets.py` が環境変数 `SKILL_MANAGER_ROOT` を優先して参照するように変更。
  - カレントディレクトリに依存しない実行モデルの確立。
- [x] **P1-3: パスバリデーションとセキュリティの導入**
  - 指定された Hub パスが正当な `skill-manager` 構造（`ASSET_INDEX.md` 等）を持っているか検証するロジックの追加。

### 【P2】知能のデプロイ (Intelligence Deployment)
- [x] **P2-1: `setup_project.py` への自動インポート組み込み**
  - 初期セットアップ時に `core-asset-consultant` を自動でターゲットの `.skills/` へ配備する。
- [x] **P2-2: `asset-consultant` (SKILL.md) のプロンプト更新**
  - 「カタログは `SKILL_MANAGER_ROOT/ASSET_INDEX.md` から読み取れ」という環境適応ロジックの追加。
  - ターゲットプロジェクトの技術スタック（言語、依存関係）をスキャンする命令の追加。

### 【P3】機能の高度化 (Capability Enhancement)
- [ ] **P3-1: `scan_assets.py` の診断モード (Diagnostic) 追加**
  - カタログ作成だけでなく、ターゲットプロジェクトの「現状（不足しているもの）」を診断する機能の追加。
- [ ] **P3-2: `ACTIVE_ASSETS.md` のグローバル同期**
  - どのプロジェクトにどの資産を配備したかを Hub 側でも追跡・可視化できる仕組みの構築。

### 【P4】仕上げ (Polishing)
- [x] **P4-0: ドキュメント構造の最適化 (Docs Refactoring)**
  - `README.md` を入口に、`architectural-design.md` を技術詳細に、`todos.md` をタスクの単一光源 (SSOT) に整理。
- [ ] **P4-1: アーキテクチャ図の画像化と README 反映**
  - `docs/architecture-overview.drawio` を PNG 出力し、最新の状態を README に反映（必要に応じて）。

---

## 📚 Document Organization & Table of Contents

プロジェクトのドキュメント構造を整理し、ユーザーと AI が迷わず情報を取得できる構成を維持します。

| Layer | Document | Role / Content |
| :--- | :--- | :--- |
| **1. Entry** | `README.md` / `_ja.md` | **入口**: 概要、Mirror & Bridge モデル、コア・コンセプト、クイックスタート。 |
| **2. Capability** | `FEATURES.md` / `_ja.md` | **機能**: User Story Map の基礎。Epic/Story/Task レベルの機能一覧。 |
| **3. Design** | `docs/architectural-design.md` | **詳細設計**: 3レイヤー構造、Bridge-Link Model、中長期ロードマップ。 |
| | `docs/bootstrap-workflow.md` | **手順**: ターゲットプロジェクトの初期化と運用の詳細フロー。 |
| **4. Live Map** | `.skills/ASSET_INDEX.md` | **カタログ**: 全アセット（Official, Org, 3rdparty）の自動生成マスターリスト。 |
| | `.skills/ACTIVE_ASSETS.md` | **配備図**: 現在デプロイされているスキルの役割、依存関係、Mermaid による可視化。 |

## 📊 Graph Architecture (Visualization Strategy)

視覚的な理解を助けるため、用途に応じて 2 種類の図解を使い分けます。

1. **architecture-overview.drawio (Mirror & Bridge モデル)**
   - **配置**: `docs/` (PNG 参照: `README.md`)
   - **目的**: 物理的なディレクトリ構造（Hub ↔ Target）と、`Asset Consultant` による知能のミラーリング（同期）を表現する。
   - **更新**: アーキテクチャの根本的な変更時。

2. **ACTIVE_ASSETS.md (Intelligence Flow)**
   - **配置**: `.skills/` (各プロジェクト内)
   - **目的**: デプロイ済みのスキル（Nav, Swarm, GitHub 等）が、プロジェクト内でどのように「戦略・実行・知識」として連携するかを表現する。
   - **更新**: 新しいスキルがインポートまたは削除された時（Agent Governor が担当）。

---

## 📍 現在のステータス
- **Completed**: 基盤構築 (P1), 知能の自動配備 (P2), ドキュメント構造の最適化 (P4-0)。
- **Special Note**: `README.md` と `architectural-design.md` の重複を排除し、情報の役割分担を明確化しました。
- **Next Task**: `P3-1: scan_assets.py の診断モード追加`
