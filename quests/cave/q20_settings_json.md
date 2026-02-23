# Quest 20: 設定の書

## 🦍 導入

ウホッ！Hooksの仕組みはわかったか？
だがな、魔法を唱えるには「魔導書」が必要だ。
Hooksの世界では、それが `settings.json` という設定ファイルだ！
この書に呪文を刻むことで、Hooksが発動するようになる。
さあ、設定の書を読み解いてみろ！ウホホ！

## 🎯 目標

- [ ] settings.jsonの構造を理解する
- [ ] hooks設定の書き方（event / matcher / command）を把握する
- [ ] practice/cave/ にsettings.jsonを作成する

## 📋 やること

1. docs/reference/04_hooks.md のsettings.json解説部分を確認する
2. `practice/cave/.claude/settings.json` を作成する
3. PostToolUse（Write）でecho通知するHookを設定する

## 📎 コピペ

```
practice/cave/.claude/settings.json を以下の内容で作成して：

{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo '📝 ファイルが作成されました！'"
          }
        ]
      }
    ]
  }
}
```

## ✅ 成功条件

- [ ] `practice/cave/.claude/settings.json` が存在する
- [ ] PostToolUse イベントにWriteのmatcherが設定されている
- [ ] commandハンドラーでecho通知が設定されている

## 📦 成果物

- `practice/cave/.claude/settings.json`（Hook設定ファイル）

## 🍌 報酬

- base_bp: 160
- first_clear_bonus: 32

## 💡 ヒント

### hint_1
settings.jsonは `.claude/` フォルダの中に置くぞ。プロジェクトのルートではなく、`.claude/settings.json` のパスだ！

### hint_2
settings.jsonの構造:
```json
{
  "hooks": {
    "イベント名": [
      {
        "matcher": "対象ツール名",
        "hooks": [
          {
            "type": "ハンドラー種別",
            "command": "実行するコマンド"
          }
        ]
      }
    ]
  }
}
```

### hint_3
完全なファイルパスは `practice/cave/.claude/settings.json`。`.claude` ディレクトリがなければ作成する必要がある。コピペのJSONをそのまま使えばOK！

## 📚 学習ポイント

- settings.jsonはHooksの設定ファイル。`.claude/` ディレクトリに配置する
- 構造: `hooks` > `イベント名` > 配列 > `matcher`（対象）+ `hooks`（処理内容）
- matcherでどのツールに反応するかを指定し、hooksで実行する処理を定義する

## 📖 関連リファレンス

docs/reference/04_hooks.md
