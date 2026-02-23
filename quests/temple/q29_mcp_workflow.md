# Quest 29: MCPワークフロー

## 🦍 導入

ウホホ！個別のMCPは使えるようになった。
だが、真の力はMCPを「組み合わせる」ことで生まれる！
Web検索で情報を集め、整理し、ファイルに保存する——
この一連の流れを1つのワークフローとして実行する。
複合MCPワークフローの力を体験しろ！ウホッ！

## 🎯 目標

- [ ] 複数のMCPを組み合わせたワークフローを実行する
- [ ] 「情報収集 → 整理 → 保存」の一連の流れを体験する
- [ ] MCPワークフローの設計パターンを理解する

## 📋 やること

1. Fetch MCPでWebから情報を収集する
2. 収集した情報をClaude Codeで整理・分析する
3. 結果を `practice/temple/mcp-workflow-result.md` に保存する

## 📎 コピペ

```
以下のMCPワークフローを実行して：

Step 1: 情報収集
Fetch MCPを使って、以下のURLから情報を取得して：
- https://docs.anthropic.com/en/docs/claude-code/overview

Step 2: 整理
取得した情報から以下を抽出して：
- Claude Codeの主な機能（5つ以上）
- 開発者にとってのメリット（3つ以上）
- 注意点やベストプラクティス（3つ以上）

Step 3: 保存
整理した結果を practice/temple/mcp-workflow-result.md に保存して。
フォーマット: 各セクションに見出しをつけた読みやすいMarkdown
```

## ✅ 成功条件

- [ ] Fetch MCPで情報を取得できた
- [ ] 情報が構造化されて整理されている
- [ ] `practice/temple/mcp-workflow-result.md` が読みやすいMarkdownで保存されている

## 📦 成果物

- `practice/temple/mcp-workflow-result.md`（ワークフロー実行結果）

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
MCPワークフローは「入力→処理→出力」のパイプラインだ。各ステップでMCPやClaude Codeの能力を使い分ける。

### hint_2
ワークフローの設計パターン:
1. **収集**: MCP（Fetch, Search等）で外部から情報を取得
2. **処理**: Claude Codeの言語能力で分析・整理・要約
3. **出力**: Write/Editで結果をファイルに保存

このパターンはあらゆるリサーチタスクに応用できる。

### hint_3
コピペをそのまま送信すれば、Claude Codeが自動的に3ステップを順番に実行してくれる。途中でエラーが出たら、そのステップだけやり直せばOK。

## 📚 学習ポイント

- MCPワークフロー = 「収集→処理→出力」のパイプライン
- 複数のMCP + Claude Codeの言語能力を組み合わせることで強力なワークフローが作れる
- この「調べて→まとめて→保存して」のパターンは実務で最も使用頻度が高い

## 📖 関連リファレンス

docs/reference/06_mcp.md
