# MCP（Model Context Protocol）リファレンス

## MCPとは？

MCP（Model Context Protocol）は、Claude Codeを外部のツールやサービスと接続するための仕組みです。
Webの情報取得、ファイルシステム操作、データベースアクセスなど、Claude Code単体ではできないことを可能にします。

## なぜMCPが必要？

Claude Codeは強力ですが、デフォルトではインターネットにアクセスできず、限られたツールしか使えません。
MCPを使えば：

- **Web情報の取得**: URLからコンテンツを読み取れる
- **外部API連携**: Slack、GitHub、Notionなどのサービスと連携
- **ファイルシステム拡張**: 柔軟なファイル操作が可能に
- **データベース接続**: SQLiteやPostgreSQLに直接アクセス

## .mcp.jsonの構造

MCPサーバーは `.mcp.json` ファイルで設定します。プロジェクトルートに配置します。

```json
{
  "mcpServers": {
    "サーバー名": {
      "command": "実行コマンド",
      "args": ["引数1", "引数2"],
      "env": {
        "環境変数名": "値"
      }
    }
  }
}
```

### 設定例

```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-fetch"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-filesystem", "."]
    }
  }
}
```

## 主要MCPサーバー一覧

### Fetch MCP
URLからWebコンテンツを取得する。

```json
"fetch": {
  "command": "npx",
  "args": ["-y", "@anthropic-ai/mcp-fetch"]
}
```

使い方: Claude Codeに「このURLの内容を読んで」と伝えるだけ。

### Filesystem MCP
ファイルシステムの高度な操作を行う。

```json
"filesystem": {
  "command": "npx",
  "args": ["-y", "@anthropic-ai/mcp-filesystem", "/許可するパス"]
}
```

第3引数でアクセスを許可するディレクトリを指定。セキュリティのため必要最小限に。

### その他の人気MCPサーバー

| サーバー | 用途 | パッケージ |
|----------|------|-----------|
| GitHub | GitHub操作 | @modelcontextprotocol/server-github |
| Slack | Slack連携 | @modelcontextprotocol/server-slack |
| SQLite | データベース | @modelcontextprotocol/server-sqlite |
| Brave Search | Web検索 | @modelcontextprotocol/server-brave-search |

## 権限管理

### アクセス制御の原則

1. **最小権限の原則**: 必要なサーバーだけを有効にする
2. **パス制限**: Filesystem MCPは必要なディレクトリだけに限定
3. **環境変数**: APIキーは `.env` ファイルや環境変数で管理（.mcp.jsonにハードコードしない）

### .mcp.jsonの配置場所

| 場所 | 適用範囲 |
|------|---------|
| プロジェクトルート | そのプロジェクトのみ |
| `~/.claude/` | 全プロジェクト共通 |

## セキュリティ注意事項

1. **APIキーをコミットしない**: `.gitignore` に `.env` を追加
2. **信頼できるMCPサーバーのみ使用**: 公式またはよく知られたパッケージを選ぶ
3. **Filesystem MCPのパスを限定**: `/` や `~` 全体へのアクセスは避ける
4. **定期的な見直し**: 不要になったMCPサーバーは削除する

## トラブルシューティング

### MCPサーバーが起動しない
- `npx` がインストールされているか確認（`which npx`）
- Node.jsのバージョンを確認（v18以上推奨）

### ツールが使えない
- Claude Codeを再起動してみる
- `.mcp.json` のJSON構文エラーがないか確認

### 権限エラー
- Filesystem MCPのパス引数を確認
- 環境変数が正しく設定されているか確認
