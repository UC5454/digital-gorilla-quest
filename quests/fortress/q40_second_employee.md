# Quest 40: 2体目のAI社員

## 🦍 導入

ウホッ！ここまで育ててきた1体目のAI社員は順調か？
だがな、一匹では群れとは呼べん。2体目を生み出す時が来た！

1体目とは「違う役割」のAI社員を作れ。
リサーチャーがいるならライターを。ライターがいるならレビュアーを。
役割の分担が、群れの力を何倍にもするんだ！

## 🎯 目標

- [ ] 1体目とは異なる役割の2体目AI社員を設計する
- [ ] 2体目のCLAUDE.mdを作成する（全セクション含む）
- [ ] members.yamlに2体目を追加する

## 📋 やること

1. 2体目のAI社員の役割を決める（1体目と異なるもの）
2. 新しいディレクトリを作成する
3. CLAUDE.mdを作成する（identity, role, persona, skills, startup, inbox_rules）
4. INBOX.mdを作成する
5. members.yamlに2体目の情報を追加する

## 📎 コピペ

```
以下のAI社員を作成して：

1. my-first-ai/[2体目の名前]/ ディレクトリを作成
2. CLAUDE.md を以下の構成で作成（100行程度）:

# [2体目の名前] - [役割名]

<agent name="[名前]" role="[役割]">

<identity>
[一人称、性格、特徴を3行程度で]
</identity>

<role>
## 責任範囲
[何を担当するか箇条書き]

## 判断基準
[迷った時の優先順位]
</role>

<persona>
## コミュニケーションスタイル
[話し方の特徴、口調の例]
</persona>

<skills>
## 得意なこと
[箇条書き]

## ワークフロー
[メインの作業手順]
</skills>

<startup>
起動時に以下を読み込む:
- CLAUDE.md
- INBOX.md
</startup>

<inbox_rules>
[Q38で学んだ連携ルール]
</inbox_rules>

</agent>

3. INBOX.md を作成
4. members.yaml に追記
```

## ✅ 成功条件

- [ ] 2体目のAI社員ディレクトリが存在する
- [ ] CLAUDE.mdに全セクション（identity, role, persona, skills, startup, inbox_rules）が含まれている
- [ ] 1体目とは異なる役割が設定されている
- [ ] members.yamlに2体目が追加されている

## 📦 成果物

- `my-first-ai/[2体目の名前]/CLAUDE.md`
- `my-first-ai/[2体目の名前]/INBOX.md`
- `my-first-ai/members.yaml`（更新）

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
役割のアイデア: リサーチャー、ライター、レビュアー、コーダー、秘書、デザイナー、マーケター。1体目と「補完関係」になる役割がベストだ。

### hint_2
CLAUDE.mdは100行程度で十分。大事なのは「全セクションが揃っていること」と「1体目と明確に役割が違うこと」。完璧を目指さず、まず形を作ろう。

### hint_3
2体目の例（1体目がリサーチャーの場合）:
```yaml
# members.yamlへの追記
  - name: "ライターB"
    role: "ライター"
    team: "direct"
    directory: "ライターB"
    inbox: "ライターB/INBOX.md"
    description: "リサーチ結果を元に記事を執筆するAI社員"
```

CLAUDE.mdでは、1体目との連携方法（「リサーチャーからINBOXで調査結果を受け取り、記事化する」等）を明記すると、自律的に連携できるようになる。

## 📚 学習ポイント

- AI社員は「1体完璧」より「複数体で補完」の方が強い
- 役割分担を明確にすることで、各AI社員が専門性を発揮できる
- members.yamlで組織全体を一元管理する習慣をつける

## 📖 関連リファレンス

docs/reference/08_team_coordination.md
