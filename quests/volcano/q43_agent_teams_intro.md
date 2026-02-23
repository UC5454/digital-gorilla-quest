# Quest 43: 炎の覚醒

## 🦍 導入

ウホッ！火山の入口にようこそ、勇者ゴリラよ！
ここから先は、これまでとは次元の違う力を手に入れる。

砦ではINBOXで「非同期」に連携する方法を学んだ。
だが火山には、もっと強力な力がある——**Agent Teams**だ。
複数のエージェントを「同時に」動かす、炎の術を覚えろ！

## 🎯 目標

- [ ] 3つの協働方式（Subagent / Agent Teams / INBOX連携）の違いを理解する
- [ ] それぞれの使い分けを説明できる
- [ ] Agent Teamsが最適なシーンを判断できる

## 📋 やること

1. 以下のコピペでClaude Codeに3方式の違いを聞く
2. 返答を読んで、それぞれの特徴を理解する
3. 比較表を `practice/boss-challenge/volcano/comparison.md` に保存する

## 📎 コピペ

```
Claude Codeには3つの協働方式があるよね。それぞれの違いを比較表にまとめて practice/boss-challenge/volcano/comparison.md に保存して：

1. Subagent（Taskツール）: セッション内で軽量な子エージェントを起動
2. Agent Teams（TeamCreate/TaskCreate）: 重量級の並列エージェントチーム
3. INBOX連携（ファイルベース）: 非同期のAI社員間メッセージング

比較軸: 実行方式、同期/非同期、適したタスク、メリット、デメリット
```

## ✅ 成功条件

- [ ] `practice/boss-challenge/volcano/comparison.md` が存在する
- [ ] 3つの方式の比較が表形式でまとめられている
- [ ] 各方式の「適したタスク」が具体的に記述されている

## 📦 成果物

- `practice/boss-challenge/volcano/comparison.md`

## 🍌 報酬

- base_bp: 200
- first_clear_bonus: 40

## 💡 ヒント

### hint_1
3方式の最大の違いは「いつ使うか」。軽い調査→Subagent。重い並列作業→Agent Teams。恒久的な業務→INBOX連携。

### hint_2
| 方式 | 実行方式 | 最適なシーン |
|------|---------|-------------|
| Subagent | セッション内・軽量 | ちょっとした調査やファイル探索 |
| Agent Teams | 並列プロセス・重量 | 複数人が同時に別タスクを実行 |
| INBOX連携 | ファイルベース・非同期 | 日常業務の引き継ぎ・報告 |

### hint_3
使い分けの判断基準:
- **今すぐ、この場で完結させたい** → Subagent（Taskツール、subagent_type指定）
- **複数の重いタスクを同時並行で処理したい** → Agent Teams（TeamCreate→TaskCreate→Task spawn）
- **日常的にAI社員がやり取りを続ける** → INBOX連携（ファイル書き込み→start-employee.sh）

Agent Teamsは「一時的なプロジェクトチーム」、INBOX連携は「常設の部署間連絡」と考えるとイメージしやすい。

## 📚 学習ポイント

- 協働方式は3種類あり、タスクの性質に応じて使い分ける
- Subagentは軽量・同期的、Agent Teamsは重量・並列、INBOX連携は非同期・恒久的
- 適材適所の選択が、AI活用の効率を大きく左右する

## 📖 関連リファレンス

docs/reference/09_agent_teams.md
