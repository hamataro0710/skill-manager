# 🗺️ Feature Inventory & User Story Map (Value Roadmap)

`Skill-Manager` は、組織全体の AI 資産を統合し、あらゆるプロジェクトで「知能の再利用」を可能にすることをミッションとしています。このドキュメントは、そのビジョンを具体化する機能群と進捗状況を管理します。

## 🌟 Mission & Vision
- **Mission**: AI 資産（スキル・プロンプト・ツール）の断片化を解消し、シームレスな配布と共有を実現する。
- **Vision**: 開発者が好みのエージェントを使いながら、組織の集合知に即座にアクセスできる「知能のインフラ」を構築する。

---

## 📈 User Story Map & Status

各機能の状態を以下のマークで示します：
- ✅ **Done** (完了)
- 🏗️ **In Progress** (進行中)
- ⏳ **Planned** (計画中)

| Epic | Narrative (ユーザーの要望) | Story / Task (機能・ストーリー) | Status |
| :--- | :--- | :--- | :--- |
| **E1: Foundation** (接続基盤) | 組織の資産（Hub）と個別のプロジェクト（Target）を安全かつ簡単に接続したい。 | **P1-1: setup_project.py による自動初期化**<br>ターゲットの `.env` 構成、ディレクトリ構造作成、ACデプロイ。 | ✅ **Done** |
| | | **P1-2: パス解決の抽象化**<br>環境変数 `SKILL_MANAGER_ROOT` による Hub 位置の特定とツール間連携。 | ✅ **Done** |
| | | **P1-3: シンボリックリンク・レイヤー**<br>`.agents/`, `.claude/` を `.skills/` に集約し、エージェント間の差異を吸収。 | ✅ **Done** |
| **E2: Intelligence** (知能の配備) | プロジェクトの文脈（言語・スタック）を理解し、最適なスキルを自動で提案・導入してほしい。 | **P2-1: Asset Consultant (AC) の常駐**<br>プロジェクト作成時に AC スキルを自動デプロイ。 | ✅ **Done** |
| | | **P2-2: AC による環境適応プロンプト**<br>ローカルの技術スタックをスキャンし、Hub の `ASSET_INDEX.md` から最適なものを提案。 | ✅ **Done** |
| | | **P2-3: 診断モード (Diagnostic)**<br>`scan_assets.py` による不足能力の自動検知と推薦。 | 🏗️ **In Progress** |
| **E3: Enhancement** (管理と視認性) | どのプロジェクトにどのスキルが導入されているかを可視化し、一括管理したい。 | **P3-1: ACTIVE_ASSETS.md による可視化**<br>プロジェクト内で「今何ができるか」を Mermaid 図解と表で自動生成。 | ✅ **Done** |
| | | **P3-2: グローバル同期 (Global Active Map)**<br>Hub 側で全プロジェクトの導入状況を一括把握する機能。 | ⏳ **Planned** |
| | | **P3-3: 資産カタログの自動生成**<br>`scan_assets.py` による `ASSET_INDEX.md` の常時最新化。 | ✅ **Done** |
| **E4: Documentation** (品質管理) | ドキュメントが最新かつ簡潔に保たれ、AI と人間が迷わない構造を維持したい。 | **P4-1: ドキュメント階層標準の確立**<br>README, FEATURES, PROJECT_RULES 等の役割分担の定義。 | ✅ **Done** |
| | | **P4-2: 非詩的・簡潔な記述ルールの適用**<br>AI の誤認を防ぐための記述ガイドラインの策定。 | ✅ **Done** |

---

## 🛠️ Developer Stories (Internal Requirements)

技術ストーリーの進捗：

- **D1: Tool-Neutral Interface**: 特定のエージェントに依存しないツール提供。 ✅ **Done**
- **D2: Atomic Replacement**: `str_replace` 等を用いた安全な編集ロジック。 ✅ **Done**
- **D3: Security Guard**: 秘密情報を守るインデックス化ガードレール。 ✅ **Done**
