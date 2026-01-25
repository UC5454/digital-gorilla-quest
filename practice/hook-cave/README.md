# 🔗 フック洞窟

ここはフック設定を練習する場所です。

## 構造

```
hook-cave/
└── .claude/
    └── settings.json
```

## settings.json テンプレート

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'コマンド実行前！'"
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
            "command": "echo 'ファイルが変更されました！'"
          }
        ]
      }
    ]
  }
}
```

## matcher の書き方

- 単一ツール: `"matcher": "Bash"`
- 複数ツール: `"matcher": ["Bash", "Write"]`
- パターン: `"matcher": "Bash(git *)"`
- 全て: `"matcher": "*"`

ウホッ！連鎖の魔法を習得せよ！ 🦍
