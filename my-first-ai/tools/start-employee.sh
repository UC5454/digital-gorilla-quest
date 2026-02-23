#!/bin/bash
# AI社員起動スクリプトテンプレート
# エリア7（砦）のクエストで、このスクリプトをカスタマイズします

EMPLOYEE_NAME="$1"

if [ -z "$EMPLOYEE_NAME" ]; then
  echo "使い方: bash start-employee.sh <AI社員名>"
  echo "例: bash start-employee.sh assistant"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEAM_DIR="$(dirname "$SCRIPT_DIR")"
EMPLOYEE_DIR="${TEAM_DIR}/${EMPLOYEE_NAME}"

if [ ! -d "$EMPLOYEE_DIR" ]; then
  echo "エラー: ${EMPLOYEE_DIR} が見つかりません"
  exit 1
fi

echo "🦍 ${EMPLOYEE_NAME} を起動します..."
cd "${EMPLOYEE_DIR}" && claude --resume
