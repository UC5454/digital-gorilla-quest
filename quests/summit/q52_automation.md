# Quest 52: 自動化の完成

## 🦍 導入

ウホッ！接続を完成させたな。
最後のピースは「自動化」だ。

HooksとSkillsを連動させて、AI社員が自律的に動くワークフローを構築する。
タスクが完了したら自動で記録。エラーが起きたら自動で通知。
これが「真の自動化」だ！

## 🎯 目標

- [ ] Hooks + Skills の連動ワークフローを構築する
- [ ] タスク完了時にdaily-logsへ自動記録する仕組みを作る
- [ ] エラー時の通知Hookを設定する

## 📋 やること

1. タスク完了時の自動記録Hookを作成する
2. daily-logs記録用のスキルを作成する
3. エラー通知Hookを設定する
4. 動作をテストする

## 📎 コピペ

```
以下の自動化を設定して：

1. my-first-ai/.claude/commands/log-task.md を作成:
---
description: タスク完了をdaily-logsに記録する
---
以下のタスクをdaily-logsに記録してください:
- 日時: 現在の日時
- タスク内容: $ARGUMENTS
- 結果: 完了
daily-logs/[今日の日付].md に追記する形で保存してください。

2. my-first-ai/.claude/settings.json のpermissionsにHook設定用の権限を追加

3. 動作テスト: /log-task "テストタスク完了" を実行してdaily-logsに記録されることを確認
```

## ✅ 成功条件

- [ ] `/log-task` スキルが作成されている
- [ ] スキル実行でdaily-logsにタスク記録が追記される
- [ ] settings.jsonに必要な権限設定がある

## 📦 成果物

- `my-first-ai/.claude/commands/log-task.md`
- `my-first-ai/.claude/settings.json`（更新）
- `my-first-ai/daily-logs/[日付].md`（テスト記録）

## 🍌 報酬

- base_bp: 220
- first_clear_bonus: 44

## 💡 ヒント

### hint_1
Hooks（settings.json）とSkills（.claude/commands/）は別物だが、組み合わせると強力な自動化ができる。Hooksは「イベント発火」、Skillsは「定型処理」。

### hint_2
daily-logsの自動記録は、AI社員の活動を追跡するための基本機能。日付ごとのファイルに追記していく形が管理しやすい。

### hint_3
log-task.mdの完成版:
```markdown
---
description: タスク完了をdaily-logsに記録する
---
以下のタスクをdaily-logsに記録してください:

1. daily-logs/ フォルダがなければ作成
2. daily-logs/[今日の日付 YYYY-MM-DD].md がなければ新規作成
3. 以下のフォーマットで追記:

### [現在時刻]
- タスク: $ARGUMENTS
- 結果: 完了
- 記録者: [AI社員名]
```

テスト方法: Claude Code上で `/log-task テストタスクの完了記録` と入力。daily-logsに記録されていれば成功。

## 📚 学習ポイント

- Hooksは「いつ動くか」、Skillsは「何をするか」を定義する
- 両者の組み合わせで「自動化ワークフロー」が構築できる
- daily-logsへの自動記録は、AI社員運用の基本インフラ

## 📖 関連リファレンス

docs/reference/04_hooks.md
