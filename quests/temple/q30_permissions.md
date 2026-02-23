# Quest 30: 権限とセキュリティ

## 🦍 導入

ウホホホ！MCPの力を使いこなせるようになったか！
だが、力には責任が伴う。最後の試練は「権限とセキュリティ」だ。
AIに何を許可し、何を禁止するか——この設計が甘いと大事故が起きる。
permissions設計の極意を学べ！ウホッ！

## 🎯 目標

- [ ] Claude Codeのpermissions（allow / deny）設定を理解する
- [ ] AI社員ごとの権限分離の考え方を学ぶ
- [ ] 権限マトリクス表を設計する

## 📋 やること

1. Claude Codeのpermissions設定の仕組みを学ぶ
2. 実際の権限設計を考える（AI社員ごとに何を許可/禁止するか）
3. `practice/temple/permission-design.md` に権限マトリクス表を作成する

## 📎 コピペ

```
Claude Codeのpermissions設計について教えて：
1. settings.jsonでのallow/deny設定の書き方
2. ツール単位での権限制御の方法
3. 「最小権限の原則」とは何か

その上で、以下の3人のAI社員を想定した権限マトリクス表を設計して：
- リサーチャー（Web検索・情報収集が仕事）
- ライター（記事執筆・ファイル作成が仕事）
- エンジニア（コード実装・コマンド実行が仕事）

各AI社員に対して、以下のツールのallow/denyを設計：
Read, Write, Edit, Bash, Fetch MCP, Filesystem MCP

結果を practice/temple/permission-design.md に保存して。
```

## ✅ 成功条件

- [ ] allow / deny の設定方法を説明できる
- [ ] 最小権限の原則（必要な権限だけを付与する）を理解した
- [ ] 3人のAI社員の権限マトリクス表が設計されている
- [ ] `practice/temple/permission-design.md` が作成されている

## 📦 成果物

- `practice/temple/permission-design.md`（権限マトリクス表）

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36
- badge: mcp_master
- badge_icon: 🔌
- badge_description: 接続の達人

## 💡 ヒント

### hint_1
「最小権限の原則」= 仕事に必要な権限だけを与え、それ以外は禁止する。リサーチャーにBash権限は不要だし、ライターにgit push権限は危険だ！

### hint_2
settings.jsonでの権限設定例:
```json
{
  "permissions": {
    "allow": ["Read", "Write", "Edit"],
    "deny": ["Bash(rm *)", "Bash(git push*)"]
  }
}
```
allowで許可するツール、denyで禁止するパターンを指定。

### hint_3
権限マトリクスの考え方:

| ツール | リサーチャー | ライター | エンジニア |
|--------|------------|---------|-----------|
| Read | ✅ allow | ✅ allow | ✅ allow |
| Write | ❌ deny | ✅ allow | ✅ allow |
| Edit | ❌ deny | ✅ allow | ✅ allow |
| Bash | ❌ deny | ❌ deny | ✅ allow |
| Fetch MCP | ✅ allow | ❌ deny | ✅ allow |
| Filesystem | ❌ deny | ❌ deny | ✅ allow |

これはあくまで例。業務内容に合わせて調整する。

## 📚 学習ポイント

- 最小権限の原則: 必要な権限だけを与え、不要な権限は禁止する
- allow / deny で細かくツールのアクセス制御ができる
- AI社員ごとに異なる権限設計をすることで、セキュリティと効率を両立できる

## 📖 関連リファレンス

docs/reference/06_mcp.md
