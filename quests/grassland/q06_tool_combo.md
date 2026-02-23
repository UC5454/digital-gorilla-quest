# Quest 6: ツールの組み合わせ

## 🦍 導入

ウホホーッ！4つのツールを全て手に入れたな！
だが、本当の力はツールを「組み合わせる」ことで生まれる。

ここからが面白いぞ。1つの指示で4つのツールを全部使わせてみろ！
お前は「What（何をするか）」を伝えるだけ。
「How（どうやるか）」はClaude Codeが自分で判断する。これが本当の力だ！

## 🎯 目標

- [ ] 1つの指示でClaude Codeに4つのツール全てを使わせる
- [ ] today-summary.md が作成され、「Q6クリア！」が追記されていることを確認する
- [ ] 「Whatを伝えてHowは任せる」という使い方を理解する

## 📋 やること

1. 以下のコピペをClaude Codeに送信する
2. Claude Codeが4つのツールを自動的に使い分ける様子を観察する
3. today-summary.mdの内容を確認する

## 📎 コピペ

```
以下を全部やって：
1. practice/grassland/ にあるファイルの一覧を確認（Bash）
2. self-intro.md を読んで内容を把握（Read）
3. practice/grassland/today-summary.md を新規作成して、「今日学んだ4つのツール」をまとめる（Write）
4. today-summary.md の最後に「Q6クリア！」と追記する（Edit）
```

## ✅ 成功条件

- [ ] Bashツール（ls実行）が使われた
- [ ] Readツール（self-intro.md読み込み）が使われた
- [ ] Writeツール（today-summary.md作成）が使われた
- [ ] Editツール（「Q6クリア！」追記）が使われた
- [ ] `practice/grassland/today-summary.md` が存在し、内容が正しい

## 📦 成果物

- `practice/grassland/today-summary.md`

## 🍌 報酬

- base_bp: 100
- first_clear_bonus: 20
- badge: cli_user
- badge_icon: 💪
- badge_description: CLI使い

## 💡 ヒント

### hint_1
4つのタスクを1回の指示で全部伝えてみよう。Claude Codeが自動で順番に実行してくれるぞ。

### hint_2
Claude Codeはタスクの依存関係も理解する。「ファイル一覧を確認→読む→作成→追記」という順番を自動で判断して実行するぞ。

### hint_3
コピペをそのまま送信すればOK。Claude Codeが (1) Bashでls実行 → (2) Readでself-intro.md読み込み → (3) Writeでtoday-summary.md作成 → (4) Editで「Q6クリア！」追記、という流れを自動実行する。

## 📚 学習ポイント

- **What（何を）を伝えてHow（どうやるか）は任せる**: これがClaude Codeの最も重要な使い方
- **ツールの自動選択**: Claude Codeはタスクの内容から最適なツールを自動で選ぶ
- **複合タスク**: 複数の操作を1回の指示でまとめて実行できる

## 📖 関連リファレンス

docs/reference/01_basics.md
