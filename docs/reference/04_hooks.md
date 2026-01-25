# 📚 Hooks リファレンス

## Hooks とは

Hooks（フック）は、Claude Code の特定のアクションの前後に自動実行される処理です。
Git の hooks に似た仕組みで、ワークフローを自動化できます。

## 設定場所

設定ファイル: `~/.claude/settings.json` または `./.claude/settings.json`

⚠️ **注意**: プロジェクトローカルの設定は `.claude/`（ドットで始まる）フォルダ内に配置します。

```json
{
  "hooks": {
    "PreToolUse": [...],
    "PostToolUse": [...],
    "Notification": [...],
    "Stop": [...]
  }
}
```

## フックの種類

| フック | タイミング | 用途 |
|--------|----------|------|
| `PreToolUse` | ツール実行前 | 検証、ロギング |
| `PostToolUse` | ツール実行後 | 後処理、通知 |
| `Notification` | 通知発生時 | 外部連携 |
| `Stop` | セッション終了時 | クリーンアップ |

## 基本構文

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Running: $TOOL_INPUT'"
          }
        ]
      }
    ]
  }
}
```

## matcher の指定

### 特定のツールにマッチ

```json
{
  "matcher": "Bash"
}
```

### 複数のツールにマッチ

```json
{
  "matcher": ["Bash", "Write", "Edit"]
}
```

### パターンでマッチ

```json
{
  "matcher": "Bash(git *)"
}
```

### 全てにマッチ

```json
{
  "matcher": "*"
}
```

## フックのタイプ

### 1. command タイプ

シェルコマンドを実行：

```json
{
  "type": "command",
  "command": "echo 'Hook executed!'"
}
```

### 2. script タイプ

スクリプトファイルを実行：

```json
{
  "type": "script",
  "script": "./scripts/my-hook.sh"
}
```

## 環境変数

フック内で使用可能な環境変数：

| 変数 | 説明 |
|------|------|
| `$TOOL_NAME` | ツール名 |
| `$TOOL_INPUT` | ツールへの入力 |
| `$TOOL_OUTPUT` | ツールの出力（PostToolUseのみ） |
| `$SESSION_ID` | セッションID |

## 実用的な例

### 例1: Git 操作前の確認

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git push*)",
        "hooks": [
          {
            "type": "command",
            "command": "echo '⚠️ Push operation detected'"
          }
        ]
      }
    ]
  }
}
```

### 例2: ファイル変更のログ

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": ["Write", "Edit"],
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date): File modified\" >> ~/.claude/file-changes.log"
          }
        ]
      }
    ]
  }
}
```

### 例3: コード整形の自動実行

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.js)",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $TOOL_INPUT"
          }
        ]
      }
    ]
  }
}
```

### 例4: Slack 通知

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Claude notification\"}' $SLACK_WEBHOOK_URL"
          }
        ]
      }
    ]
  }
}
```

### 例5: セッション終了時のクリーンアップ

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "rm -f /tmp/claude-temp-*"
          }
        ]
      }
    ]
  }
}
```

## 高度な設定

### 条件付き実行

```json
{
  "matcher": "Bash",
  "hooks": [
    {
      "type": "command",
      "command": "if [ \"$TOOL_INPUT\" = 'rm -rf' ]; then echo 'DANGER!' && exit 1; fi"
    }
  ]
}
```

### 複数フックの連鎖

```json
{
  "matcher": "Write",
  "hooks": [
    {
      "type": "command",
      "command": "echo 'Step 1: Validation'"
    },
    {
      "type": "command",
      "command": "echo 'Step 2: Logging'"
    },
    {
      "type": "command",
      "command": "echo 'Step 3: Notification'"
    }
  ]
}
```

## ベストプラクティス

### 1. 軽量に保つ

フックは頻繁に実行されるので、重い処理は避ける。

✅ 良い例: ログ出力、簡単なチェック
❌ 悪い例: 大きなビルド、外部API連続呼び出し

### 2. エラーハンドリング

フックの失敗が本体に影響しないように：

```bash
command || true  # 失敗しても続行
```

### 3. 非同期処理

時間のかかる処理はバックグラウンドで：

```bash
nohup long-running-command &
```

### 4. デバッグ用ログ

問題調査のためにログを残す：

```json
{
  "type": "command",
  "command": "echo \"$(date): $TOOL_NAME - $TOOL_INPUT\" >> ~/.claude/hooks.log"
}
```

## トラブルシューティング

**Q: フックが実行されない**
A: settings.json の構文を確認、matcher の指定を見直す

**Q: フックがエラーになる**
A: コマンドを直接ターミナルで実行してテスト

**Q: フックが遅い**
A: 重い処理はバックグラウンド実行に変更

**Q: 環境変数が展開されない**
A: シングルクォートではなくダブルクォートを使用

## 次のステップ

Hooks を習得したら：
- ベストプラクティス → `05_best_practices.md`
