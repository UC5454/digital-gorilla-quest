# Quest 24: 3つのハンドラー

## 🦍 導入

ウホホホ！連鎖の魔法を操れるようになったか！
洞窟最後の試練だ。Hookには3つの「ハンドラー」がある。
command——シェルの力で即座に実行する。
prompt——AIに追加の指示を送り込む。
agent——サブエージェントを召喚して複雑な仕事を任せる。
この3つを使い分けられれば、お前は真の魔術師だ！ウホッ！

## 🎯 目標

- [ ] command / prompt / agent の3つのハンドラーの違いを理解する
- [ ] promptハンドラーでセキュリティチェックを実装する
- [ ] 用途に応じたハンドラーの使い分けを説明できる

## 📋 やること

1. 3つのハンドラーの特徴を学ぶ
2. promptハンドラーを使ったセキュリティチェックHookを設定する
3. テストして結果を記録する

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
            "command": "echo '📝 ファイル作成検知'"
          },
          {
            "type": "prompt",
            "prompt": "今作成したファイルの内容を確認し、以下をチェックしてください：1. APIキーやパスワードなどの機密情報が含まれていないか 2. 個人情報（メールアドレス、電話番号等）が含まれていないか。問題があれば警告、なければ「✅ セキュリティチェック通過」と表示してください。"
          }
        ]
      }
    ]
  }
}

その後、テスト:
1. practice/cave/safe-file.md に「Hello World」とだけ書いて（→ チェック通過するはず）
2. practice/cave/danger-file.md に「APIキー: sk-abc123xyz」と書いて（→ 警告が出るはず）
3. 結果を practice/cave/handler-test-log.md に記録して
```

## ✅ 成功条件

- [ ] commandハンドラーで即座にメッセージが表示される
- [ ] promptハンドラーでAIによるセキュリティチェックが実行される
- [ ] 安全なファイルでは「チェック通過」、危険なファイルでは「警告」が出る
- [ ] `practice/cave/handler-test-log.md` に結果が記録されている

## 📦 成果物

- `practice/cave/.claude/settings.json`（3ハンドラー設定）
- `practice/cave/handler-test-log.md`（テスト結果）

## 🍌 報酬

- base_bp: 160
- first_clear_bonus: 32
- badge: chain_mage
- badge_icon: 🔗
- badge_description: 連鎖の魔術師

## 💡 ヒント

### hint_1
3つのハンドラーの使い分け:
- **command**: 速い、シンプル、シェルコマンドで済む処理に
- **prompt**: AIの判断力が必要な処理に（内容チェック、要約等）
- **agent**: 複雑で時間がかかる処理に（コードレビュー、リファクタリング等）

### hint_2
promptハンドラーの書き方:
```json
{
  "type": "prompt",
  "prompt": "AIへの指示文をここに書く"
}
```
promptはAIに追加の指示を送る。commandより遅いが、内容の「意味」を理解した処理ができる。

### hint_3
ハンドラーの選び方フローチャート:
1. 単純なシェルコマンドで済む？ → **command**（echo, wc, grep等）
2. AIに内容を読んで判断してほしい？ → **prompt**（レビュー、チェック等）
3. 複雑な複数ステップの処理？ → **agent**（リファクタリング、テスト生成等）

速度: command（即座）> prompt（数秒）> agent（数十秒）

## 📚 学習ポイント

- command: 高速・単純。シェルコマンド実行。ログ記録や通知に最適
- prompt: 中速・柔軟。AIの判断力で内容チェックや要約ができる
- agent: 低速・最強。サブエージェントが複雑なタスクを自律的に実行する
- 速度とパワーのトレードオフを理解し、用途に応じて使い分けることが極意

## 📖 関連リファレンス

docs/reference/04_hooks.md
