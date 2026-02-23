# Quest 46: エージェントの配備

## 🦍 導入

ウホホ！チームを作り、タスクを分解した。
次はいよいよ、エージェントを実際に「配備」する！

Taskツールでエージェントをspawn——つまり生み出して動かす。
しかも、2体を同時に並列で動かすんだ！
炎の力が本格的に目覚めるぞ！

## 🎯 目標

- [ ] Taskツールで2つのエージェントを並列にspawnする
- [ ] subagent_typeの選び方を理解する
- [ ] 2つの調査結果を統合する

## 📋 やること

1. 2つの調査タスクを並列でエージェントに割り当てる
2. 各エージェントのsubagent_typeを選択する
3. 両方の結果が揃ったら統合する
4. 結果を `practice/boss-challenge/volcano/research-result.md` に保存する

## 📎 コピペ

```
以下の2つの調査を並列で実行して：

調査1（Exploreエージェント）: 「ゴリラの種類と生息地」を調べて、要点を3つにまとめる
調査2（Exploreエージェント）: 「ゴリラの知能と道具使用」を調べて、要点を3つにまとめる

両方完了したら、結果を統合して practice/boss-challenge/volcano/research-result.md に保存して。

※ Taskツールを使って、subagent_type="Explore" で2つ並列にspawnすること
```

## ✅ 成功条件

- [ ] 2つのエージェントが並列で起動された
- [ ] 各エージェントがsubagent_type="Explore"で実行された
- [ ] `practice/boss-challenge/volcano/research-result.md` に統合結果が保存されている
- [ ] 統合結果に両方の調査内容が含まれている

## 📦 成果物

- `practice/boss-challenge/volcano/research-result.md`

## 🍌 報酬

- base_bp: 200
- first_clear_bonus: 40

## 💡 ヒント

### hint_1
subagent_typeの選び方:
- `Explore`: 読み取り専用の調査・検索（今回はこれ）
- `general-purpose`: ファイル編集も含む汎用作業
- `Plan`: 設計・計画策定
- `Bash`: コマンド実行のみ

### hint_2
Taskツールで並列spawnするには、1回のレスポンスで2つのTaskツール呼び出しを同時に行う。依存関係がなければClaude Codeは自動的に並列実行する。

### hint_3
Claude Codeに「Taskツールを使って並列で」と明示的に指示すると、2つのTaskツールコールを同時に発行してくれる。

各Taskの指示例:
- Task 1: 「ゴリラの種類と生息地について調べて要点3つにまとめて」（subagent_type: Explore）
- Task 2: 「ゴリラの知能と道具使用について調べて要点3つにまとめて」（subagent_type: Explore）

両方の結果が返ってきたら、general-purposeで統合ファイルを作成する。

## 📚 学習ポイント

- Taskツールでエージェントをspawnし、並列実行できる
- subagent_typeはタスクの性質に合わせて選ぶ（読み取り→Explore、編集→general-purpose）
- 並列実行は「依存関係のないタスク」に適用すると効率が大幅に向上する

## 📖 関連リファレンス

docs/reference/09_agent_teams.md
