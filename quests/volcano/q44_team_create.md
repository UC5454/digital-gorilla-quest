# Quest 44: チームの召喚

## 🦍 導入

ウホホ！炎の力を理解したか。
ならば、実際にチームを召喚する時だ！

TeamCreateで「器」を作り、TaskCreateで「仕事」を入れる。
そしてタスク間の依存関係を設定して、作業の流れを設計する。
これがAgent Teamsの基本中の基本だ！

## 🎯 目標

- [ ] TeamCreateでチームを作成する
- [ ] TaskCreateで3つのタスクを登録する
- [ ] blockedByでタスク間の依存関係を設定する

## 📋 やること

1. 「gorilla-research」チームを作成する
2. 3つのタスクを登録する（国内調査、海外調査、レポートまとめ）
3. タスク3（レポートまとめ）をタスク1・2にblockedBy設定する
4. TaskListでタスク一覧と依存関係を確認する

## 📎 コピペ

```
以下の手順でAgent Teamsを構築して：

1. gorilla-researchという名前のチームを作って
2. 以下の3つのタスクを作成して：
   - タスク1: 「国内のゴリラ保護施設を調べる」（調査タスク）
   - タスク2: 「海外のゴリラ保護活動を調べる」（調査タスク）
   - タスク3: 「調査結果を統合レポートにまとめる」（まとめタスク）
3. タスク3はタスク1とタスク2が完了してから開始するように、blockedByを設定して
4. TaskListで現在のタスク状態を表示して
```

## ✅ 成功条件

- [ ] 「gorilla-research」チームが作成されている
- [ ] 3つのタスクが登録されている
- [ ] タスク3がタスク1・2にblockedByで依存している
- [ ] TaskListで依存関係が確認できる

## 📦 成果物

- Agent Teamsのチーム構成（TaskListで確認可能）

## 🍌 報酬

- base_bp: 200
- first_clear_bonus: 40

## 💡 ヒント

### hint_1
TeamCreateはチームの「箱」を作るだけ。中身のタスクはTaskCreateで別途登録する。

### hint_2
blockedByは「このタスクを始める前に、先にこっちを終わらせてね」という依存関係。タスク3のblockedByにタスク1とタスク2のIDを入れると、両方完了するまでタスク3は開始されない。

### hint_3
具体的な流れ:
1. TeamCreateで「gorilla-research」チームを作成
2. TaskCreateでタスク1「国内のゴリラ保護施設を調べる」を作成（IDを記録）
3. TaskCreateでタスク2「海外のゴリラ保護活動を調べる」を作成（IDを記録）
4. TaskCreateでタスク3「調査結果を統合レポートにまとめる」を作成
5. TaskUpdateでタスク3にaddBlockedBy: [タスク1のID, タスク2のID] を設定
6. TaskListで確認 → タスク3のblockedByにタスク1・2のIDが表示される

## 📚 学習ポイント

- TeamCreateはチームの器、TaskCreateはタスクの登録、TaskUpdateは依存関係の設定
- blockedByで「先にやること→後でやること」の順序を制御できる
- 並列可能なタスク（1と2）と直列が必要なタスク（3）を区別することが設計のカギ

## 📖 関連リファレンス

docs/reference/09_agent_teams.md
