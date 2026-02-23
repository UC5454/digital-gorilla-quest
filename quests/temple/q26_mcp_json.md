# Quest 26: .mcp.jsonの設計図

## 🦍 導入

ウホッ！MCPの概念は掴めたか？
次は「.mcp.json」の設計図を読み解く！
command、args、env——この3つの要素が理解できれば、
どんなMCPサーバーでも自分で追加できるようになる。
神殿の力を自分のものにしろ！ウホホ！

## 🎯 目標

- [ ] .mcp.json の3要素（command / args / env）を理解する
- [ ] 新しいMCPサーバーを追加する方法を把握する
- [ ] 構造図を作成してまとめる

## 📋 やること

1. .mcp.json の構造を詳しく学ぶ
2. 各要素（command / args / env）の役割を理解する
3. `practice/temple/mcp-guide.md` に構造図と説明を保存する

## 📎 コピペ

```
.mcp.json の構造を教えて。以下の点を詳しく：
1. command: 何を指定する？
2. args: どんな引数を渡す？
3. env: 環境変数はいつ必要？
4. 新しいMCPサーバーを追加するには何を書けばいい？

具体例として、Fetch MCPサーバーの設定例を見せて。
結果を practice/temple/mcp-guide.md にまとめて。以下の形式で：
- 構造図（JSONの各部分に日本語コメント）
- 3要素の説明表
- サーバー追加手順
```

## ✅ 成功条件

- [ ] command（実行コマンド）/ args（引数）/ env（環境変数）の3要素を説明できる
- [ ] 新しいMCPサーバーの追加方法がわかった
- [ ] `practice/temple/mcp-guide.md` に構造図が保存されている

## 📦 成果物

- `practice/temple/mcp-guide.md`（MCP設定ガイド）

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
.mcp.jsonの3要素は「何を」「どうやって」「どんな環境で」実行するかを定義している。レストランの注文に例えると、command=「料理名」、args=「トッピング指定」、env=「アレルギー情報」だ！

### hint_2
Fetch MCPの設定例:
```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```
- `command`: 実行するプログラム（npx, uvx, node等）
- `args`: プログラムに渡す引数（サーバー名、オプション等）
- `env`: APIキー等の環境変数（必要な場合のみ）

### hint_3
環境変数が必要な例（APIキーが必要なサーバー）:
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```
envはAPIキーやシークレットを渡す時に使う。

## 📚 学習ポイント

- command: MCPサーバーを起動するコマンド（npx, uvx, node等）
- args: サーバーに渡す引数（サーバーパッケージ名、オプション等）
- env: 環境変数（APIキー等、必要な場合のみ指定）
- .mcp.jsonにサーバー設定を追記するだけで、新しい接続が使えるようになる

## 📖 関連リファレンス

docs/reference/06_mcp.md
