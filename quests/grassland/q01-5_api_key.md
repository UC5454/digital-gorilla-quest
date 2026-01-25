# Quest 1.5: 力の源を手に入れろ

## 導入テキスト

ウホッ！Claude Codeをインストールできたようだな！

だが、まだ力を使うことはできない。
なぜなら「力の源」がないからだ。

APIキーという名の力の源を手に入れろ！
これがなければ、Claude Codeは動かないぞ。

## 目標

- Anthropic の API キーを取得する
- 環境変数に設定する

## 成功条件

- [ ] Anthropic Console でAPIキーを取得した
- [ ] 環境変数 `ANTHROPIC_API_KEY` を設定した
- [ ] `claude` コマンドが正常に起動する

## 報酬

- base_bp: 250
- first_clear_bonus: 50

## ヒント

### hint_1
まずは https://console.anthropic.com/ にアクセスしてアカウントを作成するんだ。
そこでAPIキーを発行できるぞ。

### hint_2
APIキーを取得したら、環境変数に設定する。

**Mac/Linux の場合:**
```bash
# ~/.zshrc または ~/.bashrc に追加
export ANTHROPIC_API_KEY="sk-ant-xxxxx..."
```

設定後、ターミナルを再起動するか `source ~/.zshrc` を実行。

**Windows の場合:**
システム環境変数に `ANTHROPIC_API_KEY` を追加。

### hint_3
設定が完了したか確認する方法：

```bash
# 環境変数が設定されているか確認
echo $ANTHROPIC_API_KEY

# Claude Code を起動してみる
claude
```

起動して対話画面が表示されれば成功だ！

⚠️ **重要**: APIキーは絶対に他人に見せるな！
GitHubにpushしたり、ファイルに書いたりするのは厳禁だぞ！

## 関連リファレンス

docs/reference/01_basics.md
