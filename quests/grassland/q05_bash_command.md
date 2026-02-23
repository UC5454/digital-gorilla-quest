# Quest 5: ジャングルの声を聴く

## 🦍 導入

ウホッ！Read、Write、Edit——3つのツールを手に入れたな！
だが、最後の武器がまだだ。

それは「Bash」——ジャングルの声を聴く力だ！
ターミナルのコマンドをClaude Codeに実行させることができる。
これで4つのツールが揃う。さあ、試してみろ！

## 🎯 目標

- [ ] Claude CodeにBashツールでシェルコマンドを実行させる
- [ ] pwd / ls / wc -l / date の結果を確認する
- [ ] 4つのツール（Read / Write / Edit / Bash）の違いを説明できる

## 📋 やること

1. 以下のコピペをClaude Codeに送信する
2. 各コマンドの実行結果を確認する
3. 4つのツールの役割を整理する

## 📎 コピペ

```
以下のコマンドを順番に実行して、結果を教えて：
1. pwd
2. ls practice/grassland/
3. wc -l practice/grassland/self-intro.md
4. date
```

## ✅ 成功条件

- [ ] Claude CodeがBashツールを使ってコマンドを実行した
- [ ] 4つのコマンド全ての結果が表示された
- [ ] 4つのツール（Read / Write / Edit / Bash）の役割の違いを説明できる

## 📦 成果物

- なし（コマンド実行結果の確認がゴール）

## 🍌 報酬

- base_bp: 100
- first_clear_bonus: 20

## 💡 ヒント

### hint_1
Claude Codeにコマンド名を伝えれば、自動的にBashツールで実行してくれるぞ。

### hint_2
4つのツールの役割:
- **Read**: ファイルを読む
- **Write**: ファイルを新規作成・全体上書き
- **Edit**: ファイルの一部を編集
- **Bash**: シェルコマンドの実行

### hint_3
コピペをそのまま送信すればOK。Claude Codeが自動的にBashツールを使って4つのコマンドを順番に実行する。`pwd` は今いるフォルダ、`ls` はファイル一覧、`wc -l` は行数、`date` は現在日時だ。

## 📚 学習ポイント

- **Bashツール**: シェルコマンドを実行できる。ファイル操作以外の万能ツール
- **4ツールの使い分け**: Claude Codeは指示の内容から最適なツールを自動選択する
- **Read / Write / Edit / Bash**: この4つがClaude Codeの基本武器

## 📖 関連リファレンス

docs/reference/01_basics.md
