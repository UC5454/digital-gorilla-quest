# Quest 51: 接続の完成

## 🦍 導入

ウホホ！設計図が仕上がってきたな。
次は外部との「接続」——MCPの組み込みだ。

神殿で学んだMCPの力を、お前のAI社員に統合する。
.mcp.jsonを作り、permissionsを設定し、
AI社員が外部ツールと連携できるようにしろ！

## 🎯 目標

- [ ] .mcp.jsonを作成し、最低1つのMCPサーバーを設定する
- [ ] settings.jsonにpermissions設定を追加する
- [ ] MCP経由でのアクセスが動作することを確認する

## 📋 やること

1. `my-first-ai/.mcp.json` を作成する
2. MCPサーバー（Fetch等）を設定する
3. `.claude/settings.json` にpermissions設定を追加する
4. 動作確認する

## 📎 コピペ

```
my-first-ai/.mcp.json を以下の内容で作成して：

{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

permissions設定:
```
my-first-ai/.claude/settings.json を以下の内容で作成して：

{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "mcp__fetch__fetch"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ]
  }
}
```

## ✅ 成功条件

- [ ] `my-first-ai/.mcp.json` が存在し、最低1つのMCPサーバーが設定されている
- [ ] `.claude/settings.json` にpermissions設定がある
- [ ] MCP経由でのアクセス（例: fetch）が動作する

## 📦 成果物

- `my-first-ai/.mcp.json`
- `my-first-ai/.claude/settings.json`

## 🍌 報酬

- base_bp: 220
- first_clear_bonus: 44

## 💡 ヒント

### hint_1
.mcp.jsonはプロジェクトルートに置く。MCPサーバーの名前とコマンドを指定するだけで、Claude Codeが自動的に接続してくれる。

### hint_2
permissionsの設計原則は「最小権限」。allowに必要な操作だけを列挙し、denyに危険な操作を明記する。これでAI社員の行動範囲を安全に制御できる。

### hint_3
Fetch MCPが動くかテスト:
```
Fetch MCPを使って https://example.com のタイトルを取得して
```

もし `uvx` がインストールされていない場合:
```
pip install uv
```
または
```
brew install uv
```

他のMCPサーバー候補:
- `mcp-server-filesystem`: ファイルシステム操作
- `mcp-server-memory`: 永続的な記憶管理
- `mcp-server-brave-search`: Web検索

## 📚 学習ポイント

- .mcp.jsonでAI社員に外部ツールとの接続を追加できる
- permissions設定で安全にAI社員の権限を管理する
- MCPは「AI社員の手足を増やす」仕組み。必要なものだけ追加する

## 📖 関連リファレンス

docs/reference/06_mcp.md
