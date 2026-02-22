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
- [ ] **P4-1: アーキテクチャ図の画像化と README 反映**
  - `docs/architecture-overview.drawio` を PNG 出力し、README に埋め込む。

---

## 📍 現在のステータス
- **Completed**: 基盤構築 (P1) および 知能の自動配備 (P2)。
- **Special Note**: ツール名を Python インポート互換のためハイフンからアンダースコアへ変更 (`setup_project.py`, `import_skill.py`, etc.)。
- **Next Task**: `P3-1: scan_assets.py の診断モード追加`
