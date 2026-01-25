# Quest 19: 連鎖の洞窟へ

## 導入テキスト

ウホホホ！技の峰を制覇したお前は、いよいよ「連鎖の洞窟」に潜る！

この洞窟では、光る結晶が連鎖反応を起こして輝いている。
これが「Hooks」の力だ。

あるアクションが起きると、自動的に別のアクションが発動する。
まさに連鎖の魔法！

## 目標

- Hooks の概念を理解する
- どのような場面で使えるか把握する

## 成功条件

- [ ] Hooks が「特定のアクションの前後に自動実行される処理」であることを理解した
- [ ] 4種類のフック（PreToolUse, PostToolUse, Notification, Stop）を挙げられる

## 報酬

- base_bp: 500
- first_clear_bonus: 100

## ヒント

### hint_1
docs/reference/04_hooks.md を読んでみろ！
Hooks の詳しい説明があるぞ。

### hint_2
4種類のフック：
- PreToolUse: ツール実行「前」に発動
- PostToolUse: ツール実行「後」に発動
- Notification: 通知発生時に発動
- Stop: セッション終了時に発動

### hint_3
使用例：
- ファイル保存後に自動でフォーマット
- Git push 前に警告を表示
- 危険なコマンド実行前に確認
- セッション終了時にログを保存

## 関連リファレンス

docs/reference/04_hooks.md
