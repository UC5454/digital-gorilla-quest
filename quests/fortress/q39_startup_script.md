# Quest 39: 覚醒の儀式

## 🦍 導入

ウホホ！掟を定め、伝令を整えた。
だが、仲間を「起こす」方法がなければ、群れは眠ったままだ！

`start-employee.sh` ——これがAI社員を呼び覚ます「覚醒の儀式」だ。
シェルスクリプトでAI社員を一発起動できるようにしろ！

## 🎯 目標

- [ ] AI社員起動スクリプト（start-employee.sh）を作成する
- [ ] 実行権限を付与する
- [ ] スクリプトを実行してAI社員が起動することを確認する

## 📋 やること

1. `my-first-ai/tools/` ディレクトリを作成する
2. `start-employee.sh` を作成する
3. `chmod +x` で実行権限を付与する
4. スクリプトを実行してAI社員の起動をテストする

## 📎 コピペ

```
my-first-ai/tools/ フォルダを作成して、その中に start-employee.sh を以下の内容で作成して：

#!/bin/bash

EMPLOYEE_NAME="$1"
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

if [ -z "$EMPLOYEE_NAME" ]; then
  echo "使い方: ./start-employee.sh [AI社員名]"
  echo "例: ./start-employee.sh アシスタントA"
  exit 1
fi

EMPLOYEE_DIR="$BASE_DIR/$EMPLOYEE_NAME"

if [ ! -d "$EMPLOYEE_DIR" ]; then
  echo "エラー: $EMPLOYEE_NAME のディレクトリが見つかりません"
  exit 1
fi

echo "🦍 $EMPLOYEE_NAME を起動します..."
cd "$EMPLOYEE_DIR"
claude --print "あなたは${EMPLOYEE_NAME}です。CLAUDE.mdを読んで、INBOX.mdを確認してください。"
```

実行権限付与:
```
chmod +x my-first-ai/tools/start-employee.sh を実行して
```

## ✅ 成功条件

- [ ] `my-first-ai/tools/start-employee.sh` が存在する
- [ ] 実行権限が付与されている（`chmod +x` 済み）
- [ ] 引数なしで実行すると使い方が表示される

## 📦 成果物

- `my-first-ai/tools/start-employee.sh`

## 🍌 報酬

- base_bp: 180
- first_clear_bonus: 36

## 💡 ヒント

### hint_1
シェルスクリプトは `#!/bin/bash` で始まる。これは「このファイルをbashで実行する」という宣言だ。

### hint_2
`$1` はスクリプトに渡された最初の引数。`./start-employee.sh アシスタントA` と実行すれば、`$1` は「アシスタントA」になる。

### hint_3
スクリプトの流れ:
1. 引数チェック（名前が空なら使い方を表示して終了）
2. ディレクトリ存在チェック（なければエラー）
3. AI社員のディレクトリに移動
4. `claude --print` でClaude Codeを起動し、AI社員として動作させる

`claude --print` は対話モードではなく、1回の指示を実行して結果を表示するモード。テスト時はこれで十分。

## 📚 学習ポイント

- シェルスクリプトでAI社員の起動を自動化できる
- 引数チェックやエラーハンドリングは、堅牢なスクリプトの基本
- `claude --print` で非対話的にClaude Codeを実行できる

## 📖 関連リファレンス

docs/reference/08_team_coordination.md
