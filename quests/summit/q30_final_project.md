# Quest 30: 王への道

## 導入テキスト

ウホホホホ！！！！！

これが最後のクエストだ！

全ての知識を統合し、小さなプロジェクトを完成させろ。
CLAUDE.md、Skills、Hooks を全て使いこなし、
お前が本当にジャングルの王にふさわしいか証明するのだ！

## 目標

- 全ての学習を活かした小さなプロジェクトを完成させる
- CLAUDE.md、Skills、Hooks を組み合わせて使用する

## 成功条件

- [ ] practice/ フォルダ内にミニプロジェクトを作成
- [ ] CLAUDE.md でプロジェクトルールを定義
- [ ] 少なくとも1つのオリジナルスキルを作成
- [ ] 少なくとも1つのフックを設定

## 報酬

- base_bp: 1000
- first_clear_bonus: 200
- badge: "伝説のゴリラ"
- badge_icon: "🦍"
- badge_description: "全スキルを習得した証"

## ヒント

### hint_1
ミニプロジェクトの例：
- TODOアプリ
- メモ管理ツール
- シンプルなCLIツール

重要なのは「機能の豊富さ」ではなく、
「CLAUDE.md, Skills, Hooks を正しく使えているか」だ。

### hint_2
必要な要素チェックリスト：
- [ ] practice/final-project/ ディレクトリ
- [ ] CLAUDE.md（プロジェクトルール）
- [ ] .claude/skills/[name]/SKILL.md（スキル）
- [ ] .claude/settings.json（フック）
- [ ] 何らかの動作するコード

### hint_3
ミニプロジェクト構成例（メモツール）：

```
practice/final-project/
├── CLAUDE.md                    # プロジェクト設定
├── .claude/
│   ├── skills/
│   │   ├── memo/SKILL.md       # メモ操作スキル
│   │   └── list/SKILL.md       # 一覧表示スキル
│   └── settings.json            # フック設定
├── src/
│   └── memo.js                  # メインコード
└── data/
    └── memos.json               # データファイル
```

**CLAUDE.md例**:
```markdown
# メモツール

## 概要
シンプルなCLIメモ管理ツール

## コマンド
- /memo add [内容] - メモ追加
- /list - 一覧表示

## ルール
- メモは data/memos.json に保存
```

**スキル例** (.claude/skills/memo/SKILL.md):
```markdown
# /memo - メモを操作する

## パラメータ
- add [内容] - 新規追加
- delete [ID] - 削除

## 起動時の動作
1. data/memos.json を読み込む
2. 操作を実行
3. 結果を保存・表示
```

**フック例**:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(data/memos.json)",
        "hooks": [
          { "type": "command", "command": "echo '💾 メモが保存されました'" }
        ]
      }
    ]
  }
}
```

## 関連リファレンス

docs/reference/05_best_practices.md
