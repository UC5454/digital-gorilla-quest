# 🦍 Digital Gorilla Quest v2.0 - 最強ゴリラへの道

RPG型 Claude Code 学習教材。完全初心者が10時間でAI社員を1体作って動かせるようになる。

## 🌴 概要

ゴリラがどんどん強くなっていく成長物語として、Claude Code の全機能を習得できます。

- **9つのエリア** を制覇
- **54のクエスト** をクリア
- **9体のボス** を撃破
- **AI社員を1体構築** して動かす
- 最終目標は **「伝説のキングコング」** になること！

## 🗺️ エリアマップ

| # | エリア | テーマ | 学習内容 |
|---|--------|--------|----------|
| 1 | 🌿 草原 | はじまりの地 | 基本4ツール（Read/Write/Edit/Bash） |
| 2 | 🌲 森林 | 記憶の森 | CLAUDE.md |
| 3 | ⛰️ 山岳 | 技の峰 | Skills |
| 4 | 🕳️ 洞窟 | 連鎖の洞窟 | Hooks |
| 5 | 🏛️ 神殿 | 接続の神殿 | MCP |
| 6 | 🔮 祭壇 | 魂の祭壇 | AI社員設計 |
| 7 | 🏰 砦 | 統率の砦 | チーム連携 |
| 8 | 🌋 火山 | 覚醒の火山 | Agent Teams |
| 9 | 👑 頂上 | 王の座 | 最終プロジェクト |

## 🚀 始め方

### 1. リポジトリをクローン

```bash
git clone https://github.com/UC5454/digital-gorilla-quest.git
cd digital-gorilla-quest
```

### 2. 進捗ファイルを作成

```bash
cp gorilla_data/progress.template.json gorilla_data/progress.json
```

### 3. Claude Code を起動してゲーム開始！

```bash
claude
```

起動したら `/go` と入力してゲームスタート！

## 🎮 コマンド一覧

### メインコマンド（これだけでOK！）

| コマンド | 機能 |
|----------|------|
| **`/go`** | **次のクエストを表示（初回はゲーム開始）** |
| `/go done` or 「できた」 | クエスト完了 → 自動で次へ |
| `/go hint` | ヒント表示（3段階） |
| `/go status` | ステータス確認 |
| `/go boss` | ボス戦開始 |
| `/go [番号]` | 指定クエストへ移動 |

## 📁 ディレクトリ構成

```
.
├── CLAUDE.md                 # ゲーム設定
├── .mcp.json                 # MCP設定（エリア5で使用）
├── gorilla_data/             # プレイヤーデータ
├── quests/                   # クエストファイル
│   ├── grassland/            # 🌿 草原エリア（Q1-Q6）
│   ├── forest/               # 🌲 森林エリア（Q7-Q12）
│   ├── mountain/             # ⛰️ 山岳エリア（Q13-Q18）
│   ├── cave/                 # 🕳️ 洞窟エリア（Q19-Q24）
│   ├── temple/               # 🏛️ 神殿エリア（Q25-Q30）
│   ├── altar/                # 🔮 祭壇エリア（Q31-Q36）
│   ├── fortress/             # 🏰 砦エリア（Q37-Q42）
│   ├── volcano/              # 🌋 火山エリア（Q43-Q48）
│   └── summit/               # 👑 頂上エリア（Q49-Q54）
├── docs/reference/           # リファレンス資料
├── practice/                 # 練習用フォルダ
├── my-first-ai/              # AI社員テンプレート（エリア6以降）
└── .claude/skills/           # ゲームスキル
```

## 📚 前提条件

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) のMax/Proプラン契約済み
- `claude` コマンドで起動できる状態

## 🦍 ウホッ！頑張れ！

質問や改善提案があれば Issue を作成してください！
