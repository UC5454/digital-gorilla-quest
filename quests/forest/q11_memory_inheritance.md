# Quest 11: 記憶の継承

## 🦍 導入

ウホッ！ルールの力も禁止の力も手に入れたな！
ここからは上級編だ。

CLAUDE.mdは実は「3つの層」を持っている。
**プロジェクトルートのCLAUDE.md**、**サブフォルダのCLAUDE.md**、そして**CLAUDE.local.md**。

親フォルダの設定は子フォルダに継承される。
ローカル設定は個人用で、gitにはコミットしない。

この「3層構造」を理解すれば、大規模プロジェクトでも美しく設定を管理できるぞ！

## 🎯 目標

- [ ] CLAUDE.mdの3層構造（ルート → サブフォルダ → CLAUDE.local.md）を理解する
- [ ] 親の設定が子に継承されることを確認する
- [ ] CLAUDE.local.mdの用途（個人設定、git除外）を理解する

## 📋 やること

1. 以下のコピペで3層構造を体験する
2. 親フォルダと子フォルダの設定がどう合成されるか確認する
3. CLAUDE.local.mdの役割を理解する

## 📎 コピペ

```
以下の3つのファイルを作成して：

1. practice/forest/inheritance/CLAUDE.md
内容：
# チーム共通設定（ルート）
- 全員日本語で対応する
- 丁寧語で話す
- コードにはコメントをつける

2. practice/forest/inheritance/sub-project/CLAUDE.md
内容：
# サブプロジェクト設定（子）
- Python 3.12を使用する
- テストは pytest で書く
※ 親の「日本語」「丁寧語」「コメント」ルールも継承される

3. practice/forest/inheritance/CLAUDE.local.md
内容：
# 個人設定（ローカル / git除外）
- エラーメッセージは詳細に表示する
- デバッグ用のprint文を許可する
※ このファイルはgitにコミットしない個人設定

作成後、この3層構造について解説して。
```

## ✅ 成功条件

- [ ] 3つのファイルが作成された
- [ ] 親（ルート）の設定が子（サブプロジェクト）に継承される仕組みを理解した
- [ ] CLAUDE.local.md = 個人設定（git除外）であることを理解した

## 📦 成果物

- `practice/forest/inheritance/CLAUDE.md`
- `practice/forest/inheritance/sub-project/CLAUDE.md`
- `practice/forest/inheritance/CLAUDE.local.md`

## 🍌 報酬

- base_bp: 120
- first_clear_bonus: 24

## 💡 ヒント

### hint_1
CLAUDE.mdの3層構造は、CSSのカスケードに似ている。上位の設定が下位に引き継がれ、下位で上書きもできるぞ。

### hint_2
3層の関係:
1. **プロジェクトルート CLAUDE.md**: チーム全員に適用される共通設定
2. **サブフォルダ CLAUDE.md**: 特定のサブプロジェクトに適用。親の設定を継承+追加
3. **CLAUDE.local.md**: 個人のみ。`.gitignore` に追加してgit管理外にする

### hint_3
コピペをそのまま送信すればOK。3ファイル作成後の解説で、「sub-project/CLAUDE.mdは親の日本語ルール等を引き継ぎつつ、Python固有のルールを追加している」ことが分かればクリアだ。

## 📚 学習ポイント

- **3層構造**: ルート → サブフォルダ → CLAUDE.local.md の継承関係
- **継承と拡張**: 親の設定を引き継ぎつつ、子で追加・上書きができる
- **CLAUDE.local.md**: 個人設定用。gitにコミットしないので、チームメンバーに影響しない

## 📖 関連リファレンス

docs/reference/02_claude_md.md
