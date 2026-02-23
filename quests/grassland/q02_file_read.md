# Quest 2: ファイルを読む力

## 🦍 導入

ウホホ！最初の会話、上出来だったな！
だが、ゴリラの力はまだまだこんなもんじゃない。

Claude Codeの最初の武器——それは「ファイルを読む力」だ。
このプロジェクトにある `README.md` と `CLAUDE.md` を読ませてみろ。
すると...あることに気づくはずだ。ウホッ！

## 🎯 目標

- [ ] Claude CodeにReadツールでファイルを読ませる
- [ ] CLAUDE.mdが「設定ファイル」だと理解する
- [ ] なぜゴリラ口調で話すのか、その仕組みを理解する

## 📋 やること

1. 以下のコピペをClaude Codeに送信する
2. README.mdとCLAUDE.mdの内容を確認する
3. CLAUDE.mdがClaude Codeの「人格設定」ファイルであることを理解する
4. ゴリラ口調の原因がCLAUDE.mdに書かれていることを確認する

## 📎 コピペ

```
README.md と CLAUDE.md を両方読んで、以下を教えて：
1. README.md には何が書いてある？
2. CLAUDE.md には何が書いてある？
3. なぜ君はゴリラの口調で話してるの？
```

## ✅ 成功条件

- [ ] Claude CodeがReadツールを使ってファイルを読んだ
- [ ] CLAUDE.md = Claude Codeの設定ファイルだと理解した
- [ ] ゴリラ口調の設定がCLAUDE.mdに書かれていると理解した

## 📦 成果物

- なし（理解がゴール）

## 🍌 報酬

- base_bp: 100
- first_clear_bonus: 20

## 💡 ヒント

### hint_1
Claude Codeは指示すると自動的にReadツールを使ってファイルを読んでくれるぞ。特別なコマンドは不要だ。

### hint_2
CLAUDE.mdはClaude Codeの「記憶」のようなもので、起動時に自動で読み込まれる。ここに書かれた設定通りにClaude Codeは振る舞う。ゴリラ口調もここで設定されているぞ。

### hint_3
そのままコピペを送信すれば、Claude Codeが自動的にReadツールで両ファイルを読み、3つの質問に答えてくれる。CLAUDE.mdの中に「ゴリラ」「ウホ」などの設定が見つかるはずだ。

## 📚 学習ポイント

- **Readツール**: Claude Codeがファイルを読むための基本ツール
- **CLAUDE.md**: Claude Codeの設定ファイル。ここに書いた内容がAIの振る舞いを決める
- **AI社員設計の基盤**: CLAUDE.mdを書き換えれば、AIの人格・ルール・スキルを自在に設定できる

## 📖 関連リファレンス

docs/reference/01_basics.md
