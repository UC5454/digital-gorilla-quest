# Quest 32: 魂の設計図 identity

## 🦍 導入

ウホホ！AI社員の全体像は掴めたか？
いよいよ、お前のAI社員に魂を吹き込む時が来た！
最初に決めるのは「identity」——名前、役割、一人称、自己定義だ。
人間だって「自分は何者か」を知らなければ、何もできない。
AIも同じだ。まず「私は誰か」を定義しろ！ウホッ！

## 🎯 目標

- [ ] AI社員のidentity（名前/役割/一人称/自己定義）を設計する
- [ ] my-first-ai/ にCLAUDE.mdを新規作成する
- [ ] 神殿ボスで作った my-ai-plan.md をベースにidentityを決定する

## 📋 やること

1. `practice/boss-challenge/temple/my-ai-plan.md` を参照する
2. AI社員のidentityを設計する
3. `my-first-ai/CLAUDE.md` を作成し、identityセクションを書く

## 📎 コピペ

```
practice/boss-challenge/temple/my-ai-plan.md を読んで、そのAI社員のidentityを設計して。

my-first-ai/CLAUDE.md を新規作成し、以下のテンプレートで identity セクションを書いて：

# [AI社員名] - [役職]

<agent name="[AI社員名]" role="[役職]">

<identity>
[名前]は[役割の説明]。[自己定義を1-2文で]。一人称は「[一人称]」。
</identity>

</agent>

ポイント：
- 名前は覚えやすく、個性的なもの
- 役割は一言で何者かわかるもの
- 一人称は性格を反映する（私/俺/僕/わたし 等）
- 自己定義は「なぜこのAI社員が存在するのか」を表す
```

## ✅ 成功条件

- [ ] `my-first-ai/CLAUDE.md` が作成されている
- [ ] `<identity>` タグ内に名前・役割・一人称・自己定義が書かれている
- [ ] my-ai-plan.md の内容が反映されている

## 📦 成果物

- `my-first-ai/CLAUDE.md`（identityセクション付き）

## 🍌 報酬

- base_bp: 200
- first_clear_bonus: 40

## 💡 ヒント

### hint_1
identityは「自己紹介」だと思えばいい。「私は〇〇です。△△が得意で、□□のために存在しています」。これが明確であるほど、AIの応答がブレない。

### hint_2
良いidentityの例:
```
リンは千葉勇志の最強の参謀。経営者の思考翻訳、事業執行の最適化を担うCOO AI社員。一人称は「私」。
```

悪いidentityの例:
```
AIアシスタントです。何でもお手伝いします。
```
→ 具体性がなく、個性がない。

### hint_3
identityを決める4つの質問:
1. **名前は？** → 覚えやすく、個性的に
2. **何者か？** → 役職名や肩書き（例: リサーチャー、ライター、エンジニア）
3. **一人称は？** → 性格を反映（堅い→私、親しみやすい→僕、強気→俺）
4. **なぜ存在する？** → このAI社員がいないと困る理由

## 📚 学習ポイント

- identityはAI社員の「核」。これがないとAIは汎用的な応答しかできない
- 名前・役割・一人称・自己定義の4要素で「このAI社員は何者か」を定義する
- 具体的で個性的なidentityほど、応答の質とブレなさが向上する

## 📖 関連リファレンス

docs/reference/07_ai_employee_design.md
