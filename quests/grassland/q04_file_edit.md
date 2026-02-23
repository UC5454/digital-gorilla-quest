# Quest 4: ファイルを編集する力

## 🦍 導入

ウホホ！ファイルを創れるようになったか、なかなかやるな！
だが、真のゴリラは「編集」もできなければならない。

「Write」と「Edit」——この2つの違いが分かるか？
Writeは全体を書き直す力。Editは一部だけを書き換える力だ。
さっき作ったself-intro.mdに新しいセクションを追加してみろ！

## 🎯 目標

- [ ] Claude CodeにEditツールでファイルを編集させる
- [ ] 元の内容が残ったまま、新しいセクションが追加されたことを確認する
- [ ] Write（全体上書き）と Edit（部分差替え）の違いを理解する

## 📋 やること

1. 以下のコピペをClaude Codeに送信する
2. Claude Codeがself-intro.mdの一部を編集することを確認する
3. 元の自己紹介セクションが残ったまま、新セクションが追加されたことを確認する
4. WriteとEditの違いを理解する

## 📎 コピペ

```
さっき作った practice/grassland/self-intro.md に、以下のセクションを追加して：

## 今日の目標
- 草原エリアを制覇する
- Claude Codeの基本4ツールを全部使う
- AI社員作りの第一歩を踏み出す
```

## ✅ 成功条件

- [ ] 元の自己紹介セクションが残ったまま、新セクションが追加された
- [ ] Claude CodeがEditツールを使用した
- [ ] Write = 全体上書き、Edit = 部分差替え（old_string → new_string）の違いを理解した

## 📦 成果物

- `practice/grassland/self-intro.md`（更新版）

## 🍌 報酬

- base_bp: 100
- first_clear_bonus: 20

## 💡 ヒント

### hint_1
「追加して」と言えば、Claude Codeは自動的にEditツールを選んでくれるぞ。「書き直して」だとWriteツールが使われる可能性がある。

### hint_2
Editツールは `old_string`（元の文字列）を `new_string`（新しい文字列）に置き換える仕組みだ。追加の場合、ファイル末尾の文字列をold_stringにして、それ + 追加内容をnew_stringにする。

### hint_3
コピペをそのまま送信すればOK。Claude Codeがself-intro.mdを読み、末尾にEditツールで新セクションを追加する。完了後にファイル内容を確認して、元の「# 自己紹介」セクションが残っていることを確認しよう。

## 📚 学習ポイント

- **Editツール**: ファイルの一部を差し替える。old_string → new_string の仕組み
- **Write vs Edit**: Write = ファイル全体を上書き、Edit = 部分的に差し替え
- **使い分け**: 新規作成や全面書き換えはWrite、部分的な追加・修正はEdit

## 📖 関連リファレンス

docs/reference/01_basics.md
