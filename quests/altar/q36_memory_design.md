# Quest 36: 記憶の設計 startup & memory_actions

## 🦍 導入

ウホホホ！ここまで来たか！祭壇最後の試練だ。
AI社員と普通のAIを分ける最大の違い——それは「記憶」だ。
起動時に何を読み込むか。毎日何を記録するか。何を確認せずに実行するか。
この3つが設計できれば、お前のAI社員は「生きている」と言える！ウホッ！

## 🎯 目標

- [ ] startup（起動時に読むファイル）を設計する
- [ ] memory_actions（daily-logsの書き方）を設計する
- [ ] confirmation_rules（確認禁止ルール）を設定する
- [ ] CurrentTask.md, INBOX.md, daily-logs/_template.md を作成する

## 📋 やること

1. startup / memory_actions / confirmation_rules をCLAUDE.mdに追加する
2. 運用に必要なファイル群を作成する
3. daily-logsのテンプレートを作成する

## 📎 コピペ

```
my-first-ai/CLAUDE.md を読んで、以下のセクションを追加して：

<startup>
起動時に以下のファイルを読み込むこと:
- @CurrentTask.md（進行中タスク）
- @INBOX.md（受信メッセージ）
- @daily-logs/（当日分のログ）
</startup>

<memory_actions>
毎回の対話終了時に、以下の手順でdaily-logsに記録すること:
1. daily-logs/YYYY-MM-DD.md ファイルを確認（あれば追記、なければ新規）
2. 記録項目: 作業内容/学んだ教訓/明日のアクション
</memory_actions>

<confirmation_rules>
## 確認禁止ルール
- ❌ 「確認しますか？」「進めてもいいですか？」は禁止
- ✅ 自分で判断して即実行する
- ✅ 実行結果の報告はOK
</confirmation_rules>

さらに、以下のファイルも作成して：

1. my-first-ai/CurrentTask.md
   ```
   # 現在のタスク
   ステータス: 待機中
   ```

2. my-first-ai/INBOX.md
   ```
   # INBOX
   ## 未処理
   （なし）
   ## 処理済み
   ```

3. my-first-ai/daily-logs/_template.md
   ```
   # [AI社員名] Daily Log - YYYY-MM-DD

   ## 今日の作業
   -

   ## 学んだ教訓
   -

   ## 明日のアクション
   -
   ```
```

## ✅ 成功条件

- [ ] CLAUDE.mdに `<startup>` セクションが追加されている
- [ ] CLAUDE.mdに `<memory_actions>` セクションが追加されている
- [ ] CLAUDE.mdに `<confirmation_rules>` セクションが追加されている
- [ ] `my-first-ai/CurrentTask.md` が作成されている
- [ ] `my-first-ai/INBOX.md` が作成されている
- [ ] `my-first-ai/daily-logs/_template.md` が作成されている

## 📦 成果物

- `my-first-ai/CLAUDE.md`（startup/memory_actions/confirmation_rules追加済み）
- `my-first-ai/CurrentTask.md`
- `my-first-ai/INBOX.md`
- `my-first-ai/daily-logs/_template.md`

## 🍌 報酬

- base_bp: 200
- first_clear_bonus: 40
- badge: soul_designer
- badge_icon: 🔮
- badge_description: 魂の設計者

## 💡 ヒント

### hint_1
記憶の3要素:
- **startup**: 「朝起きて最初に確認すること」。新聞やメールチェックのようなもの
- **memory_actions**: 「日記をつけること」。経験を記録し、次に活かす
- **confirmation_rules**: 「いちいち許可を求めない」。自律的に判断して動く

### hint_2
startup の設計のコツ:
- 必要最小限のファイルだけ読む（多すぎると起動が遅くなる）
- 最重要ファイルを先に（CurrentTask → INBOX → daily-logs）
- 過去のログは「必要な時だけ」参照する（全部読むと重い）

### hint_3
confirmation_rules が重要な理由:
- AIはデフォルトで「許可を求める」傾向がある
- これを明示的に禁止しないと、毎回「これでいいですか？」と聞いてくる
- AI社員は自律的に動くのが前提。確認は例外時のみ

daily-logsのテンプレートは `_template.md` として保存し、毎日コピーして使う。

## 📚 学習ポイント

- startup = 起動時の初期化処理。必要なコンテキストを最速で取得する
- memory_actions = 経験の記録。日々の学びを蓄積し、AI社員を「育てる」
- confirmation_rules = 自律性の担保。いちいち確認を求めないルールを明示する
- この3つが揃って初めて、AIは「社員」として自律的に動ける

## 📖 関連リファレンス

docs/reference/07_ai_employee_design.md
