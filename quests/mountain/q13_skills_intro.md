# Quest 13: 道場への入門

## 導入テキスト

ウホホホ！記憶の森を抜けたお前は、いよいよ「技の峰」に挑む！

この山には、スキルを極めた達人たちの道場がある。
「スキル」とは、お前だけの特別な技。
繰り返し使う操作を一つのコマンドにまとめたものだ。

まずは道場を見学し、スキルの仕組みを理解しろ！

## 目標

- Skills の概念を理解する
- 本プロジェクトの既存スキルを確認する

## 成功条件

- [ ] .claude/skills/ フォルダの構造を理解した
- [ ] 既存スキル（jungle-master, quest, banana など）の存在を確認した

## 報酬

- base_bp: 400
- first_clear_bonus: 80

## ヒント

### hint_1
.claude/skills/ フォルダを見てみろ！
そこに既存のスキルがあるはずだ。

### hint_2
各スキルは独自のフォルダを持ち、その中に SKILL.md がある。
例: .claude/skills/status/SKILL.md

構造を Claude Code に「.claude/skills の中身を確認して」と頼んでみろ。

### hint_3
スキルの基本構造：
```
.claude/
└── skills/
    └── skill-name/
        └── SKILL.md
```

SKILL.md には：
- スキルの説明
- 起動時の動作
- パラメータ
- 出力形式
が書かれている。

## 関連リファレンス

docs/reference/03_skills.md
