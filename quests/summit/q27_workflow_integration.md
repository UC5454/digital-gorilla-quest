# Quest 27: 流れを作る

## 導入テキスト

ウホホ！言葉の力を身につけたな。

次は「流れを作る」。
CLAUDE.md、Skills、Hooks を組み合わせて、
完璧なワークフローを構築しろ！

## 目標

- 複数の機能を組み合わせたワークフローを設計する
- 日々の開発作業を効率化する流れを作る

## 成功条件

- [ ] CLAUDE.md + Skills + Hooks を組み合わせた設定を考案した
- [ ] 実際の開発ワークフロー（例：コミット→テスト→プッシュ）を効率化できる

## 報酬

- base_bp: 700
- first_clear_bonus: 140

## ヒント

### hint_1
ワークフローの例：
1. `/status` で状況確認
2. 作業実施
3. `/format` でコード整形（スキル）
4. ファイル保存時に自動リント（フック）
5. `/commit` でコミット

### hint_2
組み合わせの考え方：
- CLAUDE.md: 「何を守るか」を定義
- Skills: 「よく使う操作」をコマンド化
- Hooks: 「自動で行うこと」を設定

### hint_3
統合ワークフロー例：

**CLAUDE.md**:
```markdown
## コミットルール
- feat/fix/docs などのプレフィックスを使う
- 日本語でコミットメッセージを書く

## コマンド
- /commit - コミットする
- /pr - PRを作成する
```

**Skills** (/commit):
```markdown
1. git status で変更確認
2. 変更内容を分析
3. 適切なコミットメッセージを生成
4. ユーザーに確認して commit
```

**Hooks**:
```json
{
  "PostToolUse": [
    {
      "matcher": "Write(*.ts)",
      "hooks": [{ "command": "eslint --fix $TOOL_INPUT" }]
    }
  ]
}
```

## 関連リファレンス

docs/reference/05_best_practices.md
