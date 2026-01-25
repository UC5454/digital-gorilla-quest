# 📚 Claude Code 基本リファレンス

## Claude Code とは

Claude Code は、Anthropic が提供する CLI ベースの AI アシスタントツールです。
ターミナルから直接 Claude AI と対話し、開発作業を効率化できます。

## インストール

### 前提条件
- Node.js 18 以上
- npm

### インストールコマンド

```bash
npm install -g @anthropic-ai/claude-code
```

### APIキーの設定（重要！）

Claude Code を使用するには、Anthropic の API キーが必要です。

1. https://console.anthropic.com/ でアカウントを作成
2. APIキーを発行
3. 環境変数に設定：

**Mac/Linux:**
```bash
# ~/.zshrc または ~/.bashrc に追加
export ANTHROPIC_API_KEY="sk-ant-xxxxx..."

# 設定を反映
source ~/.zshrc
```

**Windows:**
システム環境変数に `ANTHROPIC_API_KEY` を追加

⚠️ **重要**: APIキーは絶対に他人に見せたり、GitHubにpushしたりしないでください！

### バージョン確認

```bash
claude --version
```

## 基本的な起動方法

### 対話モード

```bash
claude
```

これで対話型セッションが開始されます。

### ワンショット実行

```bash
claude "質問や指示をここに書く"
```

単発の質問や指示を実行します。

## 主要な機能

### 1. ファイル操作

Claude Code は以下のファイル操作が可能です：

| 操作 | 説明 | 使用例 |
|------|------|--------|
| Read | ファイルを読む | 「CLAUDE.mdを読んで」 |
| Write | ファイルを作成 | 「hello.txtを作成して」 |
| Edit | ファイルを編集 | 「3行目を修正して」 |
| Glob | パターンでファイル検索 | 「*.mdファイルを探して」 |
| Grep | 内容でファイル検索 | 「TODOを含むファイルを探して」 |

### 2. コマンド実行

```
「lsコマンドを実行して」
「git status を確認して」
「npm install を実行して」
```

Bash ツールを通じてシェルコマンドを実行できます。

### 3. Web 検索・取得

```
「最新のReact情報を検索して」
「このURLの内容を確認して」
```

WebSearch、WebFetch ツールで情報収集が可能です。

## 対話中のコマンド

セッション中に使えるスラッシュコマンド：

| コマンド | 説明 |
|----------|------|
| `/help` | ヘルプを表示 |
| `/clear` | 会話履歴をクリア |
| `/exit` | セッションを終了 |
| `/compact` | 会話を要約してコンテキストを節約 |

⚠️ 終了は `/exit` と入力するか、`Ctrl+C` を押します。

## セキュリティ

Claude Code は以下の安全機能を持っています：

- **確認プロンプト**: ファイル変更やコマンド実行前に確認
- **パーミッション管理**: ツールごとの許可設定
- **サンドボックス**: 危険なコマンドの実行制限

## ベストプラクティス

1. **明確な指示を出す**: 曖昧な表現より具体的な指示
2. **コンテキストを与える**: 関連ファイルを読ませてから作業
3. **小さく始める**: 大きな変更は段階的に
4. **確認する**: 重要な操作前は内容を確認

## トラブルシューティング

### よくある問題

**Q: claude コマンドが見つからない**
A: `npm install -g @anthropic-ai/claude-code` でグローバルインストール

**Q: API キーエラー**
A: 環境変数 `ANTHROPIC_API_KEY` が正しく設定されているか確認
```bash
echo $ANTHROPIC_API_KEY
```

**Q: 起動しない・応答がない**
A: ネットワーク接続を確認。APIキーが有効か確認。

**Q: 許可を求められる**
A: Claude Code は安全のため、ファイル変更やコマンド実行前に確認を求めます。
   内容を確認して許可してください。

## 次のステップ

基本を習得したら、以下に進みましょう：
- CLAUDE.md の活用 → `02_claude_md.md`
- Skills の作成 → `03_skills.md`
- Hooks の設定 → `04_hooks.md`
