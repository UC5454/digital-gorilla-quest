# Quest 27: Webの力

## 🦍 導入

ウホホ！設計図は読めるようになった。
次は実際にMCPの力を使ってみろ！
Fetch MCP——これはClaude Codeに「Webの力」を与えるサーバーだ。
インターネット上のページを読み取り、情報を手に入れる。
やってみれば、その凄さがわかる！ウホッ！

## 🎯 目標

- [ ] Fetch MCPを使ってWebページの情報を取得する
- [ ] 取得した情報を整理してファイルに保存する
- [ ] MCPの実用性を体験する

## 📋 やること

1. Fetch MCPが .mcp.json に設定されていることを確認する
2. Claude Codeを使ってWebページの情報を取得する
3. 取得した情報を `practice/temple/web-research.md` に保存する

## 📎 コピペ

```
Fetch MCPを使って https://docs.anthropic.com/en/docs/claude-code/overview の内容を取得して、以下をまとめて：
1. Claude Codeとは何か（3行以内）
2. 主な機能3つ
3. 特徴的なポイント

結果を practice/temple/web-research.md に保存して。
```

## ✅ 成功条件

- [ ] Fetch MCPを通じてWebページの情報を取得できた
- [ ] 取得した情報が整理されて保存されている
- [ ] `practice/temple/web-research.md` が作成されている

## 📦 成果物

- `practice/temple/web-research.md`（Web調査結果）

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
Fetch MCPが .mcp.json に設定されていれば、Claude Codeに「このURLの内容を教えて」と頼むだけで自動的にFetch MCPが使われるぞ！

### hint_2
もしFetch MCPが設定されていない場合は、.mcp.json に追加する:
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

### hint_3
URLを指定して「内容をまとめて」と伝えるだけでOK。Claude CodeがFetch MCPを自動的に呼び出し、ページ内容を取得して要約してくれる。特別なコマンドは不要！

## 📚 学習ポイント

- Fetch MCPはClaude Codeに「Webアクセス能力」を与える
- URLを指定するだけで、ページ内容の取得・要約・分析が可能
- MCPを通じてClaude Codeの能力が大幅に拡張される実例

## 📖 関連リファレンス

docs/reference/06_mcp.md
