---
name: skill-picker
description: 各ディレクトリ（core, officials, org, 3rdparty）から最適な AI スキルを選定し、指定したプロジェクトへ「実体（.skills/）」と「リンク（.agents/, .claude/）」の構造でインポートします。
---

# Skill Picker

このスキルは、各種ソース（公式、組織内、サードパーティ、組み込み）からユーザーの要件に合うスキルを探し出し、プロジェクトに統合するプロセスを自動化します。

## ワークフロー

1. **検索 (Search)**:
   - 以下のディレクトリを探索し、要件に合致する `SKILL.md` やディレクトリを探します。
     - `core/skills/` (Skill-Manager 組み込み)
     - `officials/` (公式)
     - `org/skills/` (組織内共有)
     - `3rdparty/` 配下の各リポジトリ
2. **提案 (Propose)**:
   - 見つかったスキルの一覧と、それらがなぜ推奨されるかの理由を提示します。
3. **インポート (Import)**:
   - ユーザーが選択したスキルを `tools/import-skill.py` を使用してインポートします。
   - **命名規則**: `--name` 引数には `{source}-{repo}-{skill_name}` の形式を指定することを推奨します。

## 実行コマンド

```bash
# 例: skills-gemini から画像検索スキルをインポートする場合
python3 tools/import-skill.py \
  --source officials/skills-gemini/skills/image-search \
  --repo . \
  --name official-skills-gemini-image-search
```

### インポート後の構造
インポートが完了すると、ターゲットプロジェクトは以下の構成になります。

```text
{target-repo}
├── .skills/<name>         (Entity: 実体)
├── .agents/skills/        (Link: ../.skills へのリンク)
└── .claude/skills/        (Link: ../.skills へのリンク)
```

## 注意事項
- シンボリックリンクは相対パスで作成されるため、リポジトリを移動してもリンクが維持されます。
- 同名のスキルが既に存在する場合、上書きの確認をユーザーに行ってください。
