# Quest 25: 神殿の門をくぐる

## 🦍 導入

ウホッ！洞窟を制覇したお前に、神殿の門が開かれた！
ここは「接続の神殿」——Claude Codeが外の世界と繋がる聖域だ。
MCP（Model Context Protocol）という力を使えば、Web、ファイルシステム、データベース...
あらゆる外の世界の力を手に入れることができる！
まずはその全体像を掴め！ウホホ！

## 🎯 目標

- [ ] MCPの概念（Claude Codeが外部サービスと繋がるための仕組み）を理解する
- [ ] MCPがあるとできること、ないとできないことを把握する
- [ ] このリポジトリの .mcp.json を確認し、接続済みサーバーを把握する

## 📋 やること

1. 以下のコピペをClaude Codeに送信する
2. MCPの概念を理解する
3. `practice/temple/mcp-overview.md` に学んだ内容をまとめる

## 📎 コピペ

```
以下を教えて：
1. MCPって何？一言で説明して
2. MCPがないとClaude Codeは何ができて何ができない？
3. このリポジトリの .mcp.json を読んで接続済みサーバーを教えて
4. MCPを「AIのUSB-C」と呼ぶ理由を説明して

学んだ内容を practice/temple/mcp-overview.md にまとめて。
```

## ✅ 成功条件

- [ ] MCPが「AIと外部サービスを繋ぐ標準プロトコル」だと説明できる
- [ ] MCP未接続時はローカルファイル操作のみ、接続時はWeb/外部サービス利用可能と理解した
- [ ] .mcp.json に設定されているサーバー名を把握した
- [ ] `practice/temple/mcp-overview.md` が作成されている

## 📦 成果物

- `practice/temple/mcp-overview.md`（MCP概要まとめ）

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
MCPは「Model Context Protocol」の略だ。Claude Codeが外の世界と通信するための共通規格だぞ！

### hint_2
MCPのイメージ:
- MCP**なし**: Claude Codeはローカルのファイルを読み書きするだけ（引きこもり状態）
- MCP**あり**: Web検索、Google Drive、Gmail、Slack、データベース...何でもアクセス可能（世界と繋がった状態）

MCPは「AIのUSB-C」。1つのポートで様々なデバイスに繋がるように、1つのプロトコルで様々なサービスに繋がる。

### hint_3
`.mcp.json` はプロジェクトのルートにある。中身はJSON形式で、以下のような構造:
```json
{
  "mcpServers": {
    "サーバー名": {
      "command": "実行コマンド",
      "args": ["引数1", "引数2"]
    }
  }
}
```
`cat .mcp.json` で中身を確認できる。

## 📚 学習ポイント

- MCPは「AIと外部サービスを繋ぐ標準プロトコル」。USB-Cのように統一規格
- Claude Code単体 = ローカルファイル操作のみ。MCP接続 = Web・外部サービス全てにアクセス可能
- .mcp.json にMCPサーバーの接続設定が書かれている

## 📖 関連リファレンス

docs/reference/06_mcp.md
