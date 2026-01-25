# Quest 21: 最初の連鎖

## 導入テキスト

ウホホ！魔法陣の描き方を覚えたな。

次は最初の連鎖を起こす。
シンプルな PostToolUse フックを設定して、
アクションの後に何かが起きるようにしてみろ！

## 目標

- 最初のフックを設定する
- フックが発動することを確認する

## 成功条件

- [ ] PostToolUse フックを設定した
- [ ] ツール実行後にフックが発動することを確認した

## 報酬

- base_bp: 600
- first_clear_bonus: 120

## ヒント

### hint_1
まずはシンプルに「ツール実行後にメッセージを表示」
するフックを作ってみろ。

### hint_2
ログを出力するフック：
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Tool executed!'"
          }
        ]
      }
    ]
  }
}
```

### hint_3
practice/hook-cave/.claude/settings.json を以下の内容で作成：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '✅ ツールが実行されました！' >> /tmp/claude-hook-log.txt"
          }
        ]
      }
    ]
  }
}
```

これで全てのツール実行後にログが記録される。
/tmp/claude-hook-log.txt を確認してみろ！

## 関連リファレンス

docs/reference/04_hooks.md
