# Agent Teams ガイド

## Agent Teamsとは？

Agent Teamsは、Claude Codeの中で複数のエージェント（AI）を同時に立ち上げ、並列でタスクを処理する機能です。
AI社員（CLAUDE.md方式）が「恒久的なチーム」なら、Agent Teamsは「一時的なプロジェクトチーム」です。

## AI社員 vs Agent Teams

| 比較項目 | AI社員（CLAUDE.md） | Agent Teams |
|----------|-------------------|-------------|
| 持続性 | 恒久的 | 一時的（タスク完了で解散） |
| 記憶 | daily-logsで蓄積 | セッション内のみ |
| 設定方法 | CLAUDE.mdファイル | TaskCreate/SendMessage |
| 適用場面 | 継続的な業務 | 一時的な並列作業 |
| 起動方法 | start-employee.sh | Task ツール |

## 基本的な流れ

### 1. タスク分解

大きなタスクを並列可能な小タスクに分割。

```
「記事を書いて」
  → タスク1: リサーチ（並列可能）
  → タスク2: 執筆（リサーチ完了後）
  → タスク3: レビュー（執筆完了後）
```

### 2. チーム作成

```
TeamCreate で新しいチームを作成
```

### 3. タスク登録

```
TaskCreate で各タスクを登録
TaskUpdate で依存関係（blockedBy）を設定
```

### 4. エージェント起動

```
Task ツールで各エージェントを並列spawn
```

### 5. メッセージング

```
SendMessage でエージェント間の情報共有
```

### 6. 完了・解散

```
全タスク完了 → shutdown_request → TeamDelete
```

## TaskCreate の使い方

タスクを作成してチームメンバーにアサインします。

```json
{
  "subject": "市場調査を行う",
  "description": "AI市場の最新動向を調査し、レポートにまとめる",
  "activeForm": "市場調査を実行中"
}
```

## TaskUpdate の使い方

タスクの状態更新や依存関係の設定。

```json
{
  "taskId": "1",
  "status": "in_progress",
  "addBlockedBy": ["2"]
}
```

依存関係の例：
- タスク2は、タスク1が完了するまで開始できない
- `addBlockedBy: ["1"]` をタスク2に設定

## SendMessage の使い方

エージェント間でメッセージを送受信。

```json
{
  "type": "message",
  "recipient": "researcher",
  "content": "調査結果をまとめてください",
  "summary": "調査結果の依頼"
}
```

### メッセージタイプ

| type | 用途 |
|------|------|
| message | 特定のエージェントに直接メッセージ |
| broadcast | 全エージェントに一斉送信（慎重に使用） |
| shutdown_request | エージェントの終了要求 |

## DAG（有向非巡回グラフ）設計

タスクの依存関係をDAGとして設計します。

```
タスクA ──→ タスクC ──→ タスクE
              ↑
タスクB ──→ タスクD
```

- A, B: 並列実行可能（依存なし）
- C: Aの完了待ち
- D: Bの完了待ち
- E: C, Dの両方の完了待ち

### 設計のポイント

1. **独立タスクは必ず並列化**: 依存関係がなければ同時実行
2. **クリティカルパスを意識**: 最も時間がかかる経路を特定
3. **細かすぎる分割は避ける**: エージェント間通信のオーバーヘッドがある

## subagent_type の選び方

| やりたいこと | subagent_type | 説明 |
|---|---|---|
| ファイル編集・コード実装・汎用作業 | general-purpose | 全ツール利用可能 |
| コードベース調査・ファイル検索 | Explore | 読み取り専用・高速 |
| 設計・計画策定 | Plan | 読み取り専用 |
| コマンド実行・ビルド・テスト | Bash | Bashのみ |

### 使い分けの指針

- **迷ったら `general-purpose`**: 最も柔軟
- **調査だけなら `Explore`**: 軽量で高速
- **コマンドだけなら `Bash`**: シンプルで確実

## 構成パターン

### リサーチ + 執筆
```
researcher (Explore) → writer (general-purpose)
```

### 実装 + テスト
```
researcher (Explore) → implementer (general-purpose) → tester (Bash)
```

### 並列リサーチ + 統合
```
explorer-1 (Explore) ──→
explorer-2 (Explore) ──→ summarizer (general-purpose)
explorer-3 (Explore) ──→
```

## ベストプラクティス

1. **最小構成で始める**: エージェントは2-4名が適正
2. **明確な指示を与える**: 「何を」「どこに出力」「完了条件」を具体的に
3. **依存関係を正しく設定**: 並列可能なものは必ず並列に
4. **結果を集約する**: 最後にまとめ役のエージェントを置く
5. **使い捨てを恐れない**: Agent Teamsは一時的なもの。気軽に立ち上げて、気軽に解散
