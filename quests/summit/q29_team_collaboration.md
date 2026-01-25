# Quest 29: 群れの力

## 導入テキスト

ウホホ！守りの心得を身につけたな。

次は「群れの力」。
ゴリラは群れで協力して生きる。
チーム開発での Claude Code の活用法を学べ！

## 目標

- チーム開発での Claude Code 活用法を理解する
- 共有すべきもの、個人で管理すべきものを区別できる

## 成功条件

- [ ] チームで共有すべきファイル（CLAUDE.md, Skills）を理解した
- [ ] 個人で管理すべきファイル（CLAUDE.local.md, 個人設定）を理解した
- [ ] チームでの Claude Code 運用方法を説明できる

## 報酬

- base_bp: 750
- first_clear_bonus: 150

## ヒント

### hint_1
共有すべきもの（Git管理）:
- CLAUDE.md
- .claude/skills/ のチームスキル
- コーディング規約

個人で管理すべきもの:
- CLAUDE.local.md
- ~/.claude/settings.json
- 個人的なフック設定

### hint_2
チーム運用のポイント：
1. CLAUDE.md でコーディング規約を統一
2. よく使うスキルをチームで共有
3. PRレビュー時に Claude Code を活用
4. 新メンバーオンボーディングに活用

### hint_3
チーム運用ガイド：

**共有設定（リポジトリに含める）**:
```
CLAUDE.md                 # プロジェクトルール
.claude/
└── skills/
    ├── lint/SKILL.md     # リントスキル
    ├── test/SKILL.md     # テストスキル
    └── pr/SKILL.md       # PRスキル
```

**個人設定（.gitignoreに追加）**:
```
CLAUDE.local.md           # 個人メモ
.claude/settings.json     # 個人フック（プロジェクト）
```

**新メンバー向け案内**:
1. このリポジトリの CLAUDE.md を読む
2. 利用可能なスキル一覧を確認
3. 個人設定は CLAUDE.local.md で管理

## 関連リファレンス

docs/reference/05_best_practices.md
