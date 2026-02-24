# 🚀 Skill-Manager Bootstrap Workflow

このドキュメントでは、`skill-manager`（倉庫）から新しい `Target Project`（現場）を立ち上げ、自律的な資産管理を開始するまでの標準的な手順を定義します。

---

## Phase 1: Global Hub の準備 (User Action)
まず、手元の環境に `skill-manager` をクローンし、最新の公式資産を取り込みます。

```bash
# クローン（サブモジュールを含む）
git clone --recursive https://github.com/your-org/skill-manager.git
cd skill-manager

# 資産のインデックスを生成（カタログの最新化）
python core/tools/scan-assets.py
```

## Phase 2: ターゲットプロジェクトの初期化 (Bootstrap)
Hub 側からターゲットプロジェクトに対して、最初の「紐付け」と「知能のデプロイ」を行います。

```bash
# ターゲットプロジェクトの基本構成を作成
python core/tools/setup-project.py --repo {target-path} --name "My Project"
```

### 🛠️ `setup-project.py` が内部で行うこと
1.  **基本ファイル生成**: `PROJECT_RULES.md`, `AGENTS.md`, `CLAUDE.md` 等の配置。
2.  **接続の鍵 (Persistence)**: `{target-path}/.env` に `SKILL_MANAGER_ROOT={absolute-hub-path}` を書き込む。
3.  **知能の初号機デプロイ**: `{target-path}/.skills/core-asset-consultant` を Hub からコピー。

---

## Phase 3: 現場での自立運用 (Target Runtime)
以降、ユーザーはターゲットプロジェクトに移動し、そこにある `Asset Consultant` と対話するだけで環境を拡張できます。

### 🧠 Asset Consultant の動作ロジック
ターゲットプロジェクト内でエージェントが `asset-consultant` を起動すると、以下の順序でコンテキストを解決します。

1.  **Demand sensing (現場の把握)**:
    - カレントディレクトリ（`.`）を `Target` と認識。
    - 言語スタックや既存スキルをスキャン。
2.  **Supply discovery (倉庫の参照)**:
    - `.env` の `SKILL_MANAGER_ROOT` を辿り、Hub 側の `ASSET_INDEX.md` を読み取る。
3.  **Action planning (提案 & 実行)**:
    - 不足しているスキルを Hub からインポートするための `import-skill.py` コマンドを生成。

---

## 🛡️ セキュリティ・ガードレール
- **Path Validation**: Hub 参照パスが正規の `skill-manager` 構造（`ASSET_INDEX.md` の存在）を持っているか、ツール実行前に必ず検証する。
- **User Confirmation**: 外部パスからの資産インポートや、環境変数の書き換えを伴う操作は、必ずユーザーの明示的な承認を求める。

---

## 📈 今後のロードマップ (Bootstrap 関連)
- [ ] **One-liner Setup**: `curl` や `npx` 相当のコマンドで、クローン不要のセットアップを実現。
- [ ] **Auto-Update Signal**: Hub 側で `SKILL.md` が更新された際、現場の `asset-consultant` に通知を送る仕組み。
