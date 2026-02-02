# 🦍 Digital Gorilla Quest - 最強ゴリラへの道

株式会社デジタルゴリラ社員向けの **RPG型 Claude Code 学習教材** です。

## 🌴 概要

ゴリラがどんどん強くなっていく成長物語として、Claude Code の全機能を習得できます。

- **5つのテリトリー** を制覇
- **30以上のクエスト** をクリア
- **各エリアのボス** を撃破
- 最終目標は **「ジャングルの王」** になること！

## 🗺️ エリアマップ

| エリア | テーマ | 学習内容 |
|--------|--------|----------|
| 🌿 草原 | はじまりの地 | 基本操作 |
| 🌲 森林 | 記憶の森 | CLAUDE.md |
| ⛰️ 山岳 | 技の峰 | Skills |
| 🕳️ 洞窟 | 連鎖の洞窟 | Hooks |
| 👑 頂上 | 王の座 | ベストプラクティス |

## 🚀 始め方

### 1. リポジトリをクローン

```bash
git clone https://github.com/YOUR_USERNAME/digital-gorilla-quest.git
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
| `/go hint` | ヒント表示 |
| `/go status` | ステータス確認 |
| `/go boss` | ボス戦開始 |

### レガシーコマンド（引き続き使用可能）

| コマンド | 機能 |
|----------|------|
| `/jungle` | ゲーム開始・進行案内 |
| `/quest [番号]` | クエスト開始 |
| `/banana` | クエスト完了判定 |
| `/status` | ステータス確認 |
| `/hint` | ヒント表示 |
| `/boss` | ボス戦開始 |

## 📁 ディレクトリ構成

```
.
├── CLAUDE.md                 # ゲーム設定
├── gorilla_data/             # プレイヤーデータ
├── quests/                   # クエストファイル
│   ├── grassland/            # 草原エリア
│   ├── forest/               # 森林エリア
│   ├── mountain/             # 山岳エリア
│   ├── cave/                 # 洞窟エリア
│   └── summit/               # 頂上エリア
├── docs/                     # リファレンス資料
├── practice/                 # 練習用フォルダ
└── .claude/skills/           # ゲームスキル
```

## 📚 前提条件

- [Claude Code](https://github.com/anthropics/claude-code) がインストール済み
- Anthropic API キーが設定済み

## 🦍 ウホッ！頑張れ！

質問や改善提案があれば Issue を作成してください！
