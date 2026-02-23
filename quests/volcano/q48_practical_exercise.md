# Quest 48: 実戦演習

## 🦍 導入

ウホッ！ここまでの炎の術を全て使いこなす時が来た！
researcher → writer → reviewer の3段階ワークフロー。

これは実際のAI組織で使われる本番のパターンだ。
調べて、書いて、チェックする——この一連の流れを
Agent Teamsで完全自動化しろ！

## 🎯 目標

- [ ] 3段階ワークフロー（researcher→writer→reviewer）を設計する
- [ ] Agent Teamsで実行する
- [ ] 最終成果物を保存する

## 📋 やること

1. 「gorilla-article」チームを作成する
2. 3つのタスクを作成する（リサーチ→執筆→レビュー）
3. 依存関係を設定する（DAG構造）
4. エージェントをspawnして実行する
5. 最終成果物を `practice/boss-challenge/volcano/article.md` に保存する

## 📎 コピペ

```
以下の3段階ワークフローをAgent Teamsで実行して：

テーマ: 「AIとゴリラの意外な共通点」

Phase 1 - リサーチ:
  Exploreエージェントで「ゴリラの社会性・知能・コミュニケーション」と「AIの協調動作・学習・対話」の共通点を調べる

Phase 2 - 執筆（Phase 1完了後）:
  general-purposeエージェントで、リサーチ結果を元に500字程度の記事を書く

Phase 3 - レビュー（Phase 2完了後）:
  general-purposeエージェントで、記事の品質チェック・改善を行う

最終成果物を practice/boss-challenge/volcano/article.md に保存して。
```

## ✅ 成功条件

- [ ] 3段階のタスクが正しい依存関係（リサーチ→執筆→レビュー）で実行された
- [ ] `practice/boss-challenge/volcano/article.md` が存在する
- [ ] 記事が500字程度で、テーマに沿った内容になっている
- [ ] レビュー結果が反映されている

## 📦 成果物

- `practice/boss-challenge/volcano/article.md`

## 🍌 報酬

- base_bp: 200
- first_clear_bonus: 40
- badge: agent_master
- badge_icon: 🌋
- badge_description: 覚醒の炎使い

## 💡 ヒント

### hint_1
3段階ワークフローの依存関係: リサーチ → 執筆 → レビュー。全て直列（blockedByで順番を制御）。

### hint_2
Phase 1はExploreエージェント（読み取り専用で高速）、Phase 2・3はgeneral-purposeエージェント（ファイル書き込みが必要）。タスクの性質に合わせてsubagent_typeを選ぶ。

### hint_3
全体の流れ:
1. TeamCreate「gorilla-article」
2. TaskCreate「リサーチ」（blockedByなし）
3. TaskCreate「執筆」（blockedBy: リサーチ）
4. TaskCreate「レビュー」（blockedBy: 執筆）
5. Task spawn（Explore）→ リサーチ実行
6. リサーチ完了 → Task spawn（general-purpose）→ 執筆実行
7. 執筆完了 → Task spawn（general-purpose）→ レビュー実行
8. レビュー完了 → article.md保存
9. shutdown_request → TeamDelete

ポイント: Phase 1のリサーチ結果をPhase 2に正確に引き継ぐことが品質のカギ。

## 📚 学習ポイント

- 「リサーチ→執筆→レビュー」は実際のコンテンツ制作で使われる王道パターン
- DAGの直列設計で、前工程の成果を確実に次工程に引き継ぐ
- subagent_typeの使い分けが効率と品質を左右する

## 📖 関連リファレンス

docs/reference/09_agent_teams.md
