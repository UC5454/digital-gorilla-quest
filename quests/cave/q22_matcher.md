# Quest 22: 結晶の選別

## 導入テキスト

ウホッ！最初の連鎖を起こせたな！

だが、全てのアクションに反応していては疲れてしまう。
「matcher」を使って、特定のアクションにだけ反応するようにしろ！

これが結晶の選別だ。

## 目標

- matcher の使い方を理解する
- 特定のツールにのみ反応するフックを設定する

## 成功条件

- [ ] matcher で特定のツール（Bash, Write, Edit など）を指定できる
- [ ] パターンマッチング（例: "Bash(git *)"）を理解した

## 報酬

- base_bp: 600
- first_clear_bonus: 120

## ヒント

### hint_1
matcher の指定方法：
- 単一: `"matcher": "Bash"`
- 複数: `"matcher": ["Bash", "Write"]`
- パターン: `"matcher": "Bash(git *)"`

### hint_2
Git コマンドにだけ反応するフック：
```json
{
  "matcher": "Bash(git *)",
  "hooks": [
    {
      "type": "command",
      "command": "echo 'Git command detected!'"
    }
  ]
}
```

### hint_3
practice/hook-cave/.claude/settings.json を更新：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git push*)",
        "hooks": [
          {
            "type": "command",
            "command": "echo '⚠️ PUSH操作を検知！本当にpushしますか？'"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": ["Write", "Edit"],
        "hooks": [
          {
            "type": "command",
            "command": "echo '📝 ファイルが変更されました'"
          }
        ]
      }
    ]
  }
}
```

## 関連リファレンス

docs/reference/04_hooks.md
