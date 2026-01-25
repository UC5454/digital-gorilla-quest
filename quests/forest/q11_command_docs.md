# Quest 11: コマンドの地図

## 導入テキスト

ウホホ！ルールを定められるようになったな。

次は「コマンドの地図」を作る。
よく使うコマンドを CLAUDE.md に記録しておけば、
いつでも Claude Code に実行させることができる。

## 目標

- CLAUDE.md にコマンド一覧セクションを追加する
- プロジェクト固有のコマンドを文書化する

## 成功条件

- [ ] CLAUDE.md に「コマンド」セクションがある
- [ ] 最低3つのコマンドが記載されている

## 報酬

- base_bp: 350
- first_clear_bonus: 70

## ヒント

### hint_1
プロジェクトでよく使うコマンドを思い出してみろ：
- ビルド
- テスト
- 開発サーバー起動
など

### hint_2
コマンドは以下の形式で書くと良い：
```
## コマンド
- `npm run dev` - 開発サーバー起動
- `npm run build` - ビルド
- `npm test` - テスト実行
```

### hint_3
practice/memory-tree/CLAUDE.md を編集して追加：

## コマンド

### 開発
- `npm run dev` - 開発サーバー起動
- `npm run watch` - ファイル監視モード

### ビルド
- `npm run build` - 本番ビルド
- `npm run build:dev` - 開発ビルド

### テスト
- `npm test` - 全テスト実行
- `npm run test:watch` - テスト監視モード

### その他
- `npm run lint` - リント実行
- `npm run format` - コード整形

## 関連リファレンス

docs/reference/02_claude_md.md
