# Quest 41: 連携ワークフロー

## 🦍 導入

ウホッ！2体のAI社員が揃った！
だが、ただ並んでいるだけでは群れとは言えん。

「連携」——1体目がタスクを完了したら、2体目にバトンを渡す。
人間が介入しなくても、AI社員同士が自律的に協働する仕組みを作れ！

## 🎯 目標

- [ ] AI社員Aがタスクを実行し、結果をAI社員BのINBOXに送信する流れを設計する
- [ ] AI社員BをINBOXメッセージに基づいて起動し、後続タスクを実行させる
- [ ] 人間の介入なしで一連のワークフローが動作することを確認する

## 📋 やること

1. AI社員Aに「タスク実行→結果をBのINBOXに書き込む」指示を出す
2. AI社員Bを起動し、INBOXのメッセージを処理させる
3. 全体の流れが人間の介入なしで動くことを確認する

## 📎 コピペ

ステップ1: AI社員Aへの指示
```
以下のタスクを実行して：
1. 「Claude Codeの便利な使い方」を3つリストアップして practice/boss-challenge/fortress/tips.md に保存
2. 完了したら [AI社員Bの名前]/INBOX.md の「未処理」セクションに以下を追記:
   【[AI社員Aの名前]より】tips.md を作成しました。内容をレビューして、改善点があれば追記してください。
```

ステップ2: AI社員Bの起動
```
tools/start-employee.sh [AI社員Bの名前]
```

または直接指示:
```
あなたは[AI社員Bの名前]です。CLAUDE.mdを読んで、INBOX.mdを確認し、未処理メッセージを処理してください。
```

## ✅ 成功条件

- [ ] AI社員Aが `practice/boss-challenge/fortress/tips.md` を作成した
- [ ] AI社員BのINBOX.mdにメッセージが書き込まれている
- [ ] AI社員Bがメッセージを処理し、tips.mdをレビュー・改善した
- [ ] 一連の流れに人間の手動介入がない

## 📦 成果物

- `practice/boss-challenge/fortress/tips.md`（AI社員Aが作成、Bがレビュー）
- `[AI社員B]/INBOX.md`（メッセージ処理の記録）

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
連携のキーは「INBOXへの書き込み」と「起動スクリプト」の2つ。AI社員AがINBOXに書き込み→AI社員Bを起動→Bが自動でINBOXを読む、という流れだ。

### hint_2
AI社員AのCLAUDE.mdに「タスク完了時はBのINBOXに報告する」と書いておくと、毎回指示しなくても自動で連携するようになる。

### hint_3
全体の流れ:
1. AI社員Aを起動 → 指示を実行 → tips.mdを作成
2. AI社員Aが `[AI社員B]/INBOX.md` に結果メッセージを追記
3. `tools/start-employee.sh [AI社員B名]` でBを起動
4. AI社員Bは起動時にINBOXを確認（CLAUDE.mdのstartupルール）
5. 未処理メッセージを発見 → tips.mdを読んでレビュー → 改善を追記
6. メッセージに✅をつけて処理済みへ

ポイント: AI社員Bの CLAUDE.md の `<startup>` に「INBOX.mdを確認する」と書いてあれば、Bは自動的にメッセージを読んで行動する。

## 📚 学習ポイント

- AI社員間の連携は「INBOX書き込み→起動→INBOX確認→処理」のサイクルで回る
- 人間の介入なしでAI社員同士が協働できる仕組みが構築できる
- CLAUDE.mdのstartupルールが、自律的な行動の起点になる

## 📖 関連リファレンス

docs/reference/08_team_coordination.md
