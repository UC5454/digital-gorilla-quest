# Quest 21: 最初の魔法

## 🦍 導入

ウホホ！設定の書は手に入れた。
いよいよ、最初の魔法を実際に発動させる時が来た！
ファイルを作成した瞬間に、自動で通知が飛ぶ——その瞬間を目撃しろ！
百聞は一見に如かず、まずは体験だ！ウホッ！

## 🎯 目標

- [ ] Q20で作成したHookが実際に発動することを確認する
- [ ] PostToolUse（Write）の動作を体験する
- [ ] Hook発動のログを確認する

## 📋 やること

1. `practice/cave/` ディレクトリに移動（Claude Codeのカレントディレクトリを変更）
2. Claude Codeでテスト用ファイルを作成し、Hookが発動するか確認する
3. 発動結果を `practice/cave/hook-test-log.md` に記録する

## 📎 コピペ

```
practice/cave/ をカレントディレクトリにして、以下を実行して：
1. practice/cave/test-hook.txt に「Hookテスト！」と書き込む
2. Hookが発動したか確認する（「📝 ファイルが作成されました！」が出るはず）
3. practice/cave/hook-test-log.md に結果を記録する（発動した/しなかった、出力内容）
```

## ✅ 成功条件

- [ ] `practice/cave/test-hook.txt` が作成された
- [ ] PostToolUse Hookが発動し、echo通知が出力された
- [ ] `practice/cave/hook-test-log.md` に結果が記録されている

## 📦 成果物

- `practice/cave/test-hook.txt`（テスト用ファイル）
- `practice/cave/hook-test-log.md`（発動結果ログ）

## 🍌 報酬

- base_bp: 160
- first_clear_bonus: 32

## 💡 ヒント

### hint_1
Hookが発動するには、Claude Codeのカレントディレクトリが `practice/cave/` である必要がある。`.claude/settings.json` はカレントディレクトリから読み込まれるぞ！

### hint_2
もしHookが発動しなかった場合:
- settings.jsonのパスが正しいか確認（`practice/cave/.claude/settings.json`）
- JSONの文法エラーがないか確認
- matcherの値が正確に「Write」になっているか確認

### hint_3
Claude Codeのセッションを一度終了して再起動すると、settings.jsonが再読み込みされる。Hookの設定変更後は再起動を試してみよう。

## 📚 学習ポイント

- Hookは設定するだけでは意味がない。実際に発動して初めて価値が生まれる
- settings.jsonはカレントディレクトリの `.claude/` から読み込まれる
- 設定変更後はセッション再起動が必要な場合がある

## 📖 関連リファレンス

docs/reference/04_hooks.md
