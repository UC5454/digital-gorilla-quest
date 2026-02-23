# Quest 53: 起動テスト

## 🦍 導入

ウホホ！全てのパーツが揃った。
CLAUDE.md、Skills、Hooks、MCP、INBOX——全てだ。

いよいよ、お前のAI社員を本番さながらにテストする時が来た。
起動→タスク受信→処理→成果物保存→記録。
この全行程が自動で完了するか、最終テストだ！

## 🎯 目標

- [ ] start-employee.shでAI社員を起動する
- [ ] INBOXに実タスクを送信して処理させる
- [ ] 成果物がoutputs/に保存される
- [ ] daily-logsに活動が記録される

## 📋 やること

1. AI社員のINBOXにタスクメッセージを書き込む
2. start-employee.shでAI社員を起動する
3. AI社員がINBOXを読み、タスクを処理することを確認する
4. 成果物がoutputs/に保存されることを確認する
5. daily-logsに活動記録が残ることを確認する

## 📎 コピペ

ステップ1: INBOXにタスクを書き込む
```
[AI社員名]/INBOX.md の「未処理」セクションに以下を追記して：

【テストより】「Claude Codeの活用Tips」を5つリストアップして、outputs/tips-list.md に保存してください。完了したらdaily-logsに記録してください。
```

ステップ2: AI社員を起動
```
tools/start-employee.sh [AI社員名]
```

ステップ3: 結果確認
```
以下のファイルが存在するか確認して：
1. outputs/tips-list.md — 成果物
2. daily-logs/[今日の日付].md — 活動記録
3. [AI社員名]/INBOX.md — メッセージが✅処理済みになっている
```

## ✅ 成功条件

- [ ] start-employee.shでAI社員が正常に起動した
- [ ] INBOXのタスクメッセージが処理された（✅マーク）
- [ ] `outputs/tips-list.md` が存在し、5つのTipsが書かれている
- [ ] `daily-logs/[日付].md` に活動記録がある
- [ ] 全行程が（最初の起動コマンド以外）自動で完了した

## 📦 成果物

- `my-first-ai/outputs/tips-list.md`
- `my-first-ai/daily-logs/[日付].md`

## 🍌 報酬

- base_bp: 220
- first_clear_bonus: 44

## 💡 ヒント

### hint_1
起動テストのポイントは「最初のコマンド1つだけで、残りが全て自動で動くこと」。もし途中で止まったら、CLAUDE.mdのstartupやskillsの記述を見直そう。

### hint_2
よくある失敗パターン:
- CLAUDE.mdのstartupにINBOX確認が書かれていない → AI社員がメッセージを見ない
- outputs/ディレクトリが存在しない → ファイル保存に失敗
- daily-logs記録のルールが曖昧 → 記録されない

### hint_3
チェックリスト:
1. `[AI社員名]/CLAUDE.md` の `<startup>` に `INBOX.md` の確認が含まれている？
2. `outputs/` ディレクトリが存在する？（なければ事前に作成）
3. `daily-logs/` ディレクトリが存在する？
4. CLAUDE.mdに「タスク完了時はdaily-logsに記録する」と書いてある？
5. INBOXのメッセージ形式が正しい？（「未処理」セクション内にある？）

全てYesなら、start-employee.sh一発で全自動実行されるはず。

## 📚 学習ポイント

- AI社員の価値は「起動→処理→保存→記録」の全自動サイクルにある
- CLAUDE.mdの各セクションが正しく連携して初めて、自律動作が実現する
- テストは「全行程が自動で回るか」を最終確認する重要なステップ

## 📖 関連リファレンス

docs/reference/08_team_coordination.md
