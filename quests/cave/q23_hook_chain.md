# Quest 23: 連鎖の魔法

## 🦍 導入

ウホホ！条件分岐もマスターしたか！
次は「連鎖」だ。1つの魔法が別の魔法を呼び、さらに別の魔法が発動する——
ファイルを編集したら、自動で行数をカウントし、結果を通知する。
この3段階の連鎖を体験しろ！ウホッ！

## 🎯 目標

- [ ] 複数のHookを連鎖させる方法を理解する
- [ ] PostToolUse(Edit) → wc -l → echo表示の3段階連鎖を実装する
- [ ] 連鎖が正しく動作することを確認する

## 📋 やること

1. `practice/cave/.claude/settings.json` をHookチェーン設定に更新する
2. テスト用ファイルを作成し、Editで編集してHookチェーンの発動を確認する
3. 結果を `practice/cave/chain-test-log.md` に記録する

## 📎 コピペ

```
practice/cave/.claude/settings.json を以下の内容に更新して：

{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo '✏️ ファイルが編集されました'"
          },
          {
            "type": "command",
            "command": "LINES=$(wc -l < \"$CLAUDE_FILE_PATH\" 2>/dev/null || echo '不明'); echo \"📊 現在の行数: ${LINES}行\""
          }
        ]
      }
    ]
  }
}

その後、テスト:
1. practice/cave/chain-test.md を10行くらいの内容で作成して
2. そのファイルをEditで3行追加して
3. Hookチェーンの出力（✏️ + 📊行数）を確認して
4. 結果を practice/cave/chain-test-log.md に記録して
```

## ✅ 成功条件

- [ ] Edit実行時に「✏️ ファイルが編集されました」が表示される
- [ ] 続けて「📊 現在の行数: X行」が表示される
- [ ] 2つのHookが順番に連鎖して実行されている
- [ ] `practice/cave/chain-test-log.md` に結果が記録されている

## 📦 成果物

- `practice/cave/.claude/settings.json`（チェーン設定）
- `practice/cave/chain-test-log.md`（テスト結果）

## 🍌 報酬

- base_bp: 160
- first_clear_bonus: 32

## 💡 ヒント

### hint_1
hooksの配列に複数のオブジェクトを入れると、上から順番に実行される。これがHookチェーンだ！

### hint_2
`$CLAUDE_FILE_PATH` にはツールが操作したファイルのパスが入る。`wc -l` でそのファイルの行数をカウントできる。

### hint_3
Hookチェーンの仕組み:
```json
"hooks": [
  { "type": "command", "command": "ステップ1" },
  { "type": "command", "command": "ステップ2" },
  { "type": "command", "command": "ステップ3" }
]
```
配列の順番通りに実行される。どこかでエラーが出ても `|| true` をつければ次に進む。

## 📚 学習ポイント

- Hookチェーン: hooks配列に複数のコマンドを入れると順番に実行される
- `$CLAUDE_FILE_PATH` で操作対象のファイルパスを取得できる
- 「検知 → 分析 → 通知」のような多段階の自動処理が実現できる

## 📖 関連リファレンス

docs/reference/04_hooks.md
