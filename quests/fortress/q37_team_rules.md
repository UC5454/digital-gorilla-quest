# Quest 37: 群れの掟

## 🦍 導入

ウホッ！ついに砦にたどり着いたか、勇敢なゴリラよ！
ここからは一匹狼では生き残れない。群れの力が必要だ。

群れを率いるには、まず「掟」——組織のルールが必要だ。
誰がいて、誰が何を担当するのか。それを `members.yaml` に刻め！

## 🎯 目標

- [ ] members.yamlの構造を理解する
- [ ] 自分のAI組織のmembers.yamlを作成する
- [ ] 組織名・オーナー・メンバー情報を定義する

## 📋 やること

1. `my-first-ai/` ディレクトリに移動していることを確認する
2. 以下のコピペを使って `members.yaml` を作成する
3. 自分の組織名・名前に合わせてカスタマイズする
4. メンバー（AI社員）の情報を定義する

## 📎 コピペ

```
my-first-ai/members.yaml を以下の内容で作成して：

organization: my-first-ai
owner:
  name: "[あなたの名前]"

members:
  - name: "[AI社員の名前]"
    role: "[役割名]"
    team: "direct"
    directory: "[AI社員のディレクトリ名]"
    inbox: "[AI社員のディレクトリ名]/INBOX.md"
    description: "[一言で何をする社員か]"
```

## ✅ 成功条件

- [ ] `my-first-ai/members.yaml` が存在する
- [ ] organization, owner, members の3つのキーが定義されている
- [ ] 最低1名のAI社員メンバーが登録されている

## 📦 成果物

- `my-first-ai/members.yaml`

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
YAMLはインデント（スペース）が重要だ。タブではなくスペース2つで階層を表現するぞ。

### hint_2
membersは配列（リスト）だ。`-` で始まる各要素が1人のメンバーを表す。name, role, team, directory, inbox, description の6項目を定義しよう。

### hint_3
```yaml
organization: my-first-ai
owner:
  name: "山田太郎"

members:
  - name: "アシスタントA"
    role: "リサーチャー"
    team: "direct"
    directory: "アシスタントA"
    inbox: "アシスタントA/INBOX.md"
    description: "調査・情報収集を担当するAI社員"
```

## 📚 学習ポイント

- members.yamlは組織の「名簿」。誰がいて、何を担当するかを一元管理する
- YAMLは人間が読みやすい構造化データ形式。設定ファイルに最適
- AI社員の組織設計は、人間の組織設計と同じ発想で考える

## 📖 関連リファレンス

docs/reference/08_team_coordination.md
