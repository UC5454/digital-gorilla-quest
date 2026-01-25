# 📚 Skills リファレンス

## Skills とは

Skills（スキル）は、Claude Code のカスタムコマンドを定義する機能です。
繰り返し使う操作をスキルとして定義し、`/skill-name` で呼び出せます。

## ディレクトリ構造

```
project/
└── .claude/
    └── skills/
        └── skill-name/
            └── SKILL.md
```

各スキルは独自のフォルダを持ち、その中に `SKILL.md` を配置します。

## SKILL.md の基本構造

```markdown
# /skill-name - スキルの説明

スキルの詳細な説明をここに書く。

## 起動時の動作

1. 最初にやること
2. 次にやること
3. 最後にやること

## 入力パラメータ

- `param1` - パラメータの説明
- `param2` - オプションのパラメータ

## 出力形式

スキル実行後の出力フォーマットを記述。

## 例

### 基本的な使い方
```
/skill-name
```

### パラメータを指定
```
/skill-name param1 param2
```
```

## スキルの作成例

### 例1: テスト実行スキル

`.claude/skills/test/SKILL.md`:
```markdown
# /test - テストを実行する

プロジェクトのテストを実行し、結果を報告する。

## 起動時の動作

1. `npm test` を実行
2. テスト結果を確認
3. 失敗があれば詳細を表示

## オプション

- `/test all` - 全テスト実行
- `/test [ファイル名]` - 特定ファイルのみ

## 出力形式

✅ 成功: X tests passed
❌ 失敗: X tests failed, Y passed
```

### 例2: コミットスキル

`.claude/skills/commit/SKILL.md`:
```markdown
# /commit - 変更をコミットする

ステージングされた変更を適切なメッセージでコミット。

## 起動時の動作

1. `git status` で変更を確認
2. 変更内容を分析
3. 適切なコミットメッセージを生成
4. ユーザーに確認
5. `git commit` を実行

## コミットメッセージ形式

```
[type]: 概要

- 変更点1
- 変更点2
```

type:
- feat: 新機能
- fix: バグ修正
- docs: ドキュメント
- refactor: リファクタリング
- test: テスト
- chore: その他
```

### 例3: フォーマットスキル

`.claude/skills/format/SKILL.md`:
```markdown
# /format - コードを整形する

指定されたファイルまたはプロジェクト全体を整形。

## 起動時の動作

1. 対象ファイルを特定
2. Prettier を実行（設定があれば）
3. ESLint --fix を実行（設定があれば）
4. 結果を報告

## 使い方

- `/format` - 変更されたファイルを整形
- `/format all` - 全ファイルを整形
- `/format [path]` - 特定パスを整形
```

## 高度な機能

### パラメータの受け取り

スキルは呼び出し時の引数を受け取れます：

```markdown
# /deploy - デプロイを実行

## パラメータ

- 第1引数: 環境（dev/staging/prod）
- 第2引数: オプション（--force など）

## 使用例

```
/deploy staging
/deploy prod --force
```
```

### 他のスキルとの連携

```markdown
# /release - リリースを実行

## 起動時の動作

1. `/test` を実行してテスト通過を確認
2. `/format` でコードを整形
3. `/commit` で変更をコミット
4. タグを作成
5. プッシュ
```

### 条件分岐

```markdown
# /check - プロジェクトをチェック

## 起動時の動作

### package.json がある場合
- `npm audit` を実行
- `npm outdated` を確認

### requirements.txt がある場合
- `pip check` を実行
- 脆弱性をチェック

### どちらもない場合
- 基本的なファイルチェックのみ
```

## ベストプラクティス

### 1. 単一責任

1つのスキルは1つの目的に集中。

✅ 良い例: `/test`, `/format`, `/lint`
❌ 悪い例: `/test-and-format-and-lint`

### 2. 明確な命名

何をするか一目で分かる名前を。

✅ 良い例: `/deploy`, `/backup`, `/status`
❌ 悪い例: `/do-stuff`, `/run`, `/x`

### 3. 確認を入れる

破壊的操作の前は確認を。

```markdown
## 起動時の動作

1. 削除対象を表示
2. ユーザーに確認を求める
3. 確認後のみ実行
```

### 4. エラーハンドリング

失敗時の動作も記述。

```markdown
## エラー時の動作

- テスト失敗: 失敗したテストを一覧表示
- 権限エラー: sudo が必要な旨を通知
```

## トラブルシューティング

**Q: スキルが認識されない**
A: パスを確認 `.claude/skills/[name]/SKILL.md`

**Q: スキルが正しく動作しない**
A: SKILL.md の記述を見直し、曖昧な部分を具体化

**Q: 既存スキルと競合する**
A: 名前を変更するか、パラメータで区別

## 次のステップ

Skills を習得したら：
- Hooks の設定 → `04_hooks.md`
- ベストプラクティス → `05_best_practices.md`
