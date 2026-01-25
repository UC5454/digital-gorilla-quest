# Quest 20: 魔法陣を描く

## 導入テキスト

ウホッ！連鎖の仕組みを理解したな。

次は「魔法陣」を描く。
Hooks は settings.json というファイルに設定する。
これがお前の魔法陣だ。

## 目標

- settings.json の構造を理解する
- 設定ファイルの場所を把握する

## 成功条件

- [ ] settings.json の基本構造を理解した
- [ ] グローバル（~/.claude/settings.json）とローカル（.claude/settings.json）の違いを理解した

## 報酬

- base_bp: 550
- first_clear_bonus: 110

## ヒント

### hint_1
settings.json の場所：
- グローバル: ~/.claude/settings.json
- ローカル: プロジェクト/.claude/settings.json

ローカルが優先される。

### hint_2
基本構造：
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

### hint_3
practice/hook-cave/.claude/settings.json を作成してみろ：

```json
{
  "hooks": {
    "PreToolUse": [],
    "PostToolUse": []
  }
}
```

これが空の設定ファイルだ。
ここにフックを追加していく。

## 関連リファレンス

docs/reference/04_hooks.md
