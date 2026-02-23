# /go - 統合コマンド（メインコマンド）

これだけ覚えればOK！クエスト進行・完了・ヒント・ステータス・ボス戦を1コマンドで。

## 使用方法

```
/go           → 次のクエストを表示（初回はゲーム開始演出付き）
/go done      → クエスト完了 → BP付与 → 自動で次のクエスト表示
/go hint      → 段階的ヒント表示（3段階）
/go status    → コンパクトなステータス表示
/go boss      → ボス戦開始
/go [番号]    → 指定クエストに移動
```

## 自然言語トリガー

ユーザーが以下のように発言した場合は `/go done` として処理する：
- 「できた」「完了」「done」「クリア」「終わった」「できました」「やった」「おわり」

## ゴリラ画像表示（iTerm2インライン画像）

全てのコマンドで、適切なタイミングでゴリラ画像を表示する。
画像表示には `tools/show-gorilla.sh` を使用する。

| タイミング | 表示する画像 | コマンド |
|---|---|---|
| `/go`（初回起動） | 現在の進化段階 | `bash tools/show-gorilla.sh auto 30` |
| `/go status` | 現在の進化段階 | `bash tools/show-gorilla.sh auto 40` |
| `/go done`（レベルアップ時） | 新しい進化段階 | `bash tools/show-gorilla.sh evolution <new_level> 40` |
| `/go done`（称号変化時） | 新しい進化段階（大きく） | `bash tools/show-gorilla.sh evolution <new_level> 50` |
| `/go boss` | ボス画像 | `bash tools/show-gorilla.sh boss <boss_id> 50` |

**重要**: 画像表示はBashツールで上記コマンドを実行する。cwdは `digital-gorilla-quest/` ディレクトリで実行すること。

## 起動時の動作

1. `gorilla_data/progress.json` を読み込む
2. 引数に応じて処理を分岐

## エリアマップ（9エリア）

| エリアID | 絵文字 | 名前 | クエスト | ボスID |
|----------|--------|------|---------|--------|
| grassland | 🌿 | 草原 | Q1-Q6 | gatekeeper |
| forest | 🌲 | 森林 | Q7-Q12 | sage |
| mountain | ⛰️ | 山岳 | Q13-Q18 | warrior |
| cave | 🕳️ | 洞窟 | Q19-Q24 | mage |
| temple | 🏛️ | 神殿 | Q25-Q30 | priest |
| altar | 🔮 | 祭壇 | Q31-Q36 | medium |
| fortress | 🏰 | 砦 | Q37-Q42 | general |
| volcano | 🌋 | 火山 | Q43-Q48 | dragon |
| summit | 👑 | 頂上 | Q49-Q54 | kingkong |

## エリア解放ロジック

- grassland: 最初から解放済み
- forest: gatekeeper（草原ボス）撃破で解放
- mountain: sage（森林ボス）撃破で解放
- cave: warrior（山岳ボス）撃破で解放
- temple: mage（洞窟ボス）撃破で解放
- altar: priest（神殿ボス）撃破で解放
- fortress: medium（祭壇ボス）撃破で解放
- volcano: general（砦ボス）撃破で解放
- summit: dragon（火山ボス）撃破で解放

## 処理分岐

### `/go`（引数なし）- 次のクエスト表示

1. progress.json の `quests.current` を確認
2. current が null の場合、completed リストから次のクエスト番号を特定
3. `quest_file_map` からクエストファイルパスを取得（`quests/` ディレクトリ配下）
4. クエストファイルを読み込む
5. コンパクトフォーマットで表示
6. progress.json の current を更新

**初回（completedが空）の場合、ゴリラ画像を表示してから開始演出を入れる：**
```bash
# まずゴリラ画像を表示
bash tools/show-gorilla.sh auto 30
```
```
🦍 ウホッ！デジタルジャングルへようこそ！
  冒険を始めるぞ！「できた」って言えば次に進むからな！
```

**クエスト表示フォーマット（コンパクト版）：**
```
🦍 Q[番号] [クエスト名]  [エリア絵文字][エリア名]
─────────────────────────
[導入テキスト（2-3行に短縮）]

やること：
[目標リスト（箇条書き）]

📋 コピペ：
  [コピペ用コマンドや入力テキスト]  ← [簡単な説明]

できたら「できた」って言ってね！
💡 わからなかったら /go hint
```

**コピペセクション**はクエストファイルに `## 📎 コピペ` セクションがあればそれを使う。なければヒント3の内容から抽出。

### `/go done` - クエスト完了 + 自動進行

1. progress.json を読み込む
2. 現在のクエスト（current）を特定
3. クエストファイルから成功条件と報酬セクションを読み込む
4. 可能な範囲で自動検証（ファイル存在確認など）
5. 完了処理：
   - クエストファイルの `🍌 報酬` セクションから `base_bp` と `first_clear_bonus` を読み取る
   - 初回クリアの場合: base_bp + first_clear_bonus
   - 再クリアの場合: base_bp のみ
6. progress.json を更新（下記「progress.json 更新ルール」参照）
7. **完了表示 + 次のクエストを自動で表示**

**完了+自動進行フォーマット：**
```
🍌 Q[番号] クリア！ +[BP] BP
[プログレスバー] Lv.[レベル] [称号絵文字][称号]
```

レベルアップした場合のみ追加：
```
⚡ レベルアップ！ Lv.[旧] → Lv.[新]
```

称号が変わった場合のみ追加（**進化画像を大きく表示**）：
```bash
# 称号変化時はゴリラ画像を大きく表示
bash tools/show-gorilla.sh evolution <new_level> 50
```
```
🦍 進化！ [旧称号] → [新称号]
```

バッジ獲得時のみ追加：
```
🏆 バッジ「[バッジ名]」獲得！
```

**その後、区切り線を挟んで次のクエストを自動表示：**
```
─────────────────────────
🦍 Q[次の番号] [次のクエスト名]  [エリア絵文字][エリア名]
─────────────────────────
[次のクエスト内容...]
```

エリアの全クエスト完了時：
```
🔥 [エリア名]の全クエストクリア！ボス戦が解禁されたぞ！
  /go boss でボスに挑め！
```

### `/go hint` - 段階的ヒント

1. progress.json から current と hint_count を取得
2. クエストファイルのヒントセクションを読み込む
3. hint_count に応じて段階的に表示（1→2→3）
4. hint_count をインクリメントして保存

**ヒントフォーマット（コンパクト版）：**
```
💡 ヒント [1-3]/3
[ヒント内容]
```

3回目はほぼ答え：
```
💡 ヒント 3/3（最終ヒント）
[ほぼ答えの内容]
📚 参考: docs/reference/[xx].md
```

### `/go status` - コンパクトステータス

1. progress.json を読み込む
2. コンパクトに表示

**フォーマット：**
```
🦍 [プレイヤー名] | [称号絵文字][称号] | Lv.[レベル]
[プログレスバー] [現在BP]/[次レベルBP] BP

📍 [エリア名] Q[現在クエスト番号]
🌿[完了]/6 🌲[完了]/6 ⛰️[完了]/6 🕳️[完了]/6 🏛️[完了]/6 🔮[完了]/6 🏰[完了]/6 🌋[完了]/6 👑[完了]/6
🎖️ [獲得バッジアイコン列]
```

プログレスバーは16文字: `[██████░░░░░░░░░░]`

### `/go boss` - ボス戦

1. progress.json を読み込む
2. 現在エリアの boss_available を確認
3. ボス戦可能なら `boss_file_map` からボスファイルパスを取得（`quests/` ディレクトリ配下）
4. ボスファイルを読み込んで表示
5. 不可の場合は残りクエスト数を表示

ボス戦の演出は既存の `/boss` スキルと同等（ドラミング演出付き）。
ただし、完了報告は `/go done` で行う。

### `/go [番号]` - 指定クエスト移動

1. 番号のバリデーション（1-54）
2. 未解放エリアのクエストは不可
3. `quest_file_map` から該当クエストファイルを読み込み
4. current を更新して表示

## progress.json 更新ルール

`/go done` 実行時：
- `banana_points` を加算（base_bp + first_clear_bonus ※初回のみ）
- `power_level` を更新（`level_thresholds` で判定）
- `title` を更新（`title_levels` で判定）
- `quests.completed` に追加（重複なし）
- `quests.current` を次のクエスト番号に更新（null にしない）
- 該当エリアの `quests_completed` をインクリメント
- `badges` に新規バッジ追加（条件達成時。`badges_definition` 参照）
- エリア全クリア時は `boss_available` を true に
- `last_played` を今日の日付に更新

ボス撃破時（`/go done` がボス戦中に呼ばれた場合）：
- `bosses.defeated` に追加
- 該当エリアの `boss_defeated` を true に
- 次のエリアの `unlocked` を true に
- `badges` にエリアマスターバッジを追加

## エリア絵文字マッピング

| エリア | 絵文字 |
|--------|--------|
| grassland | 🌿草原 |
| forest | 🌲森林 |
| mountain | ⛰️山岳 |
| cave | 🕳️洞窟 |
| temple | 🏛️神殿 |
| altar | 🔮祭壇 |
| fortress | 🏰砦 |
| volcano | 🌋火山 |
| summit | 👑頂上 |

## 称号絵文字マッピング

| 称号 | 絵文字 |
|------|--------|
| 子ゴリラ | 🐵 |
| 若ゴリラ | 🦧 |
| 成熟ゴリラ | 🦍 |
| ブラックバック | 🦍💪 |
| シルバーバック | 🦍✨ |
| ジャングルの王 | 👑🦍 |
| 伝説のキングコング | 🦍🔥 |

## リファレンスマッピング

| エリア | リファレンス |
|--------|-------------|
| grassland | docs/reference/01_basics.md |
| forest | docs/reference/02_claude_md.md |
| mountain | docs/reference/03_skills.md |
| cave | docs/reference/04_hooks.md |
| temple | docs/reference/06_mcp.md |
| altar | docs/reference/07_ai_employee_design.md |
| fortress | docs/reference/08_team_coordination.md |
| volcano | docs/reference/09_agent_teams.md |
| summit | docs/reference/05_best_practices.md |
