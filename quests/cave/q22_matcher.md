# Quest 22: 条件の魔法

## 🦍 導入

ウホッ！最初の魔法は成功したか？
だが、本当の魔術師は「条件」によって魔法を使い分ける！
.mdファイルが作られたら📝、.jsファイルなら💻——
ファイルの種類に応じて別々の反応を返す「条件の魔法」を習得しろ！ウホホ！

## 🎯 目標

- [ ] matcherで条件分岐する方法を理解する
- [ ] 複数のHookを組み合わせて、ファイル種別ごとに異なる通知を実現する
- [ ] .md / .js / .txt で異なる挙動を確認する

## 📋 やること

1. `practice/cave/.claude/settings.json` を更新し、ファイル種別ごとの通知Hookを設定する
2. 3種類のファイル（.md / .js / .txt）を作成して挙動を確認する
3. 結果を `practice/cave/matcher-test-log.md` に記録する

## 📎 コピペ

```
practice/cave/.claude/settings.json を以下の内容に更新して：

{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "if echo \"$CLAUDE_TOOL_INPUT\" | grep -q '\\.md'; then echo '📝 Markdownファイルが作成されました！'; elif echo \"$CLAUDE_TOOL_INPUT\" | grep -q '\\.js'; then echo '💻 JavaScriptファイルが作成されました！'; fi"
          }
        ]
      }
    ]
  }
}

その後、以下のテスト用ファイルを作成して動作確認：
1. practice/cave/test-matcher.md（📝が出るはず）
2. practice/cave/test-matcher.js（💻が出るはず）
3. practice/cave/test-matcher.txt（何も出ないはず）
結果を practice/cave/matcher-test-log.md に記録して。
```

## ✅ 成功条件

- [ ] .mdファイル作成時に「📝 Markdownファイルが作成されました！」が表示される
- [ ] .jsファイル作成時に「💻 JavaScriptファイルが作成されました！」が表示される
- [ ] .txtファイル作成時には何も表示されない
- [ ] `practice/cave/matcher-test-log.md` に全結果が記録されている

## 📦 成果物

- `practice/cave/.claude/settings.json`（更新済み）
- `practice/cave/matcher-test-log.md`（テスト結果）

## 🍌 報酬

- base_bp: 160
- first_clear_bonus: 32

## 💡 ヒント

### hint_1
matcherは「どのツールに反応するか」を決める。Hookの中でさらに条件分岐するには、commandの中でif文を使うぞ！

### hint_2
`$CLAUDE_TOOL_INPUT` にはツールに渡された入力（ファイルパス等）が入る。これをgrepで検査すれば、ファイル拡張子で分岐できる。

### hint_3
シェルのif文の基本形:
```bash
if echo "$CLAUDE_TOOL_INPUT" | grep -q '\.md'; then
  echo '📝 Markdown！'
elif echo "$CLAUDE_TOOL_INPUT" | grep -q '\.js'; then
  echo '💻 JavaScript！'
fi
```
`.txt` の条件がないので、.txtファイルでは何も出力されない。

## 📚 学習ポイント

- matcherはツール単位のフィルタリング、コマンド内の条件分岐でさらに細かい制御ができる
- `$CLAUDE_TOOL_INPUT` でツールへの入力内容を取得できる
- 複数の条件を組み合わせることで、柔軟な自動処理が実現できる

## 📖 関連リファレンス

docs/reference/04_hooks.md
