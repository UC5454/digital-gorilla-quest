# Quest 3: ファイルを創る力

## 🦍 導入

ウホッ！ファイルを「読む」ことはマスターしたな！
だが、読むだけじゃ世界は変わらない。

次はファイルを「創る」力を手に入れるぞ！
Claude Codeに頼めば、お前の代わりにファイルを作ってくれる。
まずは自己紹介ファイルを作ってみろ！

## 🎯 目標

- [ ] Claude CodeにWriteツールでファイルを作成させる
- [ ] practice/grassland/self-intro.md が作成されたことを確認する
- [ ] Accept / Reject の許可ダイアログを体験する

## 📋 やること

1. 以下のコピペをClaude Codeに送信する
2. Claude Codeがファイルを作成しようとすると許可ダイアログが出る
3. 内容を確認して Accept（許可）する
4. ファイルが作成されたことを確認する

## 📎 コピペ

```
practice/grassland/self-intro.md に、以下の自己紹介を書いて：

# 自己紹介
- 名前: [自分の名前を入れて]
- 今の気分: ワクワクしてる
- Claude Codeで一番やりたいこと: AI社員を作ること
```

## ✅ 成功条件

- [ ] `practice/grassland/self-intro.md` が作成された
- [ ] Claude CodeがWriteツールを使用した
- [ ] Accept / Reject の許可ダイアログを体験した

## 📦 成果物

- `practice/grassland/self-intro.md`

## 🍌 報酬

- base_bp: 100
- first_clear_bonus: 20

## 💡 ヒント

### hint_1
Claude Codeはフォルダが存在しなければ自動的に作ってくれるぞ。パスを指定するだけでOKだ。

### hint_2
ファイル作成時に「この操作を許可しますか？」というダイアログが表示される。内容を確認してAcceptを選べば実行される。Rejectすればキャンセルだ。

### hint_3
コピペをそのまま送信すれば、Claude Codeが `practice/grassland/self-intro.md` をWriteツールで作成する。許可ダイアログが出たら内容を確認してAcceptしよう。

## 📚 学習ポイント

- **Writeツール**: ファイルを新規作成する（既存ファイルがあれば全体を上書き）
- **許可ダイアログ**: Claude Codeはファイル操作時にユーザーの許可を求める。安全装置だ
- **Accept / Reject**: 内容を確認してから許可・拒否を選べる

## 📖 関連リファレンス

docs/reference/01_basics.md
