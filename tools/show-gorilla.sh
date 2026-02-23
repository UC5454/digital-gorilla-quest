#!/bin/bash
# ゴリラ画像をiTerm2インラインで表示するスクリプト
# Usage:
#   show-gorilla.sh evolution <power_level> [width]        - 進化段階の画像を表示
#   show-gorilla.sh boss <boss_id> [width]                 - ボス画像を表示
#   show-gorilla.sh auto [width]                           - progress.jsonから自動判定して表示
#   show-gorilla.sh --dark evolution <power_level> [width] - ダークモード版を表示
#   show-gorilla.sh --dark boss <boss_id> [width]          - ダークモード版ボス画像を表示
#   show-gorilla.sh --dark auto [width]                    - ダークモード版を自動判定表示

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
IMGCAT="/Applications/iTerm.app/Contents/Resources/utilities/imgcat"
IMAGES_DIR="${BASE_DIR}/gorilla_data/images"

# ダークモードフラグ
DARK_MODE=false
if [ "$1" = "--dark" ] || [ "$1" = "-d" ]; then
  DARK_MODE=true
  shift
fi

# imgcatがなければiTerm2プロトコルで直接表示
show_image() {
  local img_path="$1"
  local width="${2:-40}"

  if [ ! -f "$img_path" ]; then
    echo "⚠️ 画像が見つかりません: $img_path"
    return 1
  fi

  if [ -x "$IMGCAT" ]; then
    "$IMGCAT" --width "${width}" "$img_path"
  else
    # iTerm2 inline image protocol fallback
    local b64_data
    b64_data=$(base64 < "$img_path")
    printf '\033]1337;File=inline=1;width=%s;preserveAspectRatio=1:%s\a' "$width" "$b64_data"
  fi
}

# パワーレベルから進化段階の画像ファイルを決定
get_evolution_image() {
  local level=$1
  local subdir=""
  if [ "$DARK_MODE" = true ]; then
    subdir="/dark"
  fi

  if [ "$level" -le 8 ]; then
    echo "${IMAGES_DIR}/evolution${subdir}/child_gorilla.png"
  elif [ "$level" -le 20 ]; then
    echo "${IMAGES_DIR}/evolution${subdir}/young_gorilla.png"
  elif [ "$level" -le 35 ]; then
    echo "${IMAGES_DIR}/evolution${subdir}/mature_gorilla.png"
  elif [ "$level" -le 50 ]; then
    echo "${IMAGES_DIR}/evolution${subdir}/blackback.png"
  elif [ "$level" -le 70 ]; then
    echo "${IMAGES_DIR}/evolution${subdir}/silverback.png"
  elif [ "$level" -le 80 ]; then
    echo "${IMAGES_DIR}/evolution${subdir}/jungle_king.png"
  else
    echo "${IMAGES_DIR}/evolution${subdir}/legendary_kingkong.png"
  fi
}

# ボス画像パスを取得
get_boss_image() {
  local boss_id="$1"
  local subdir=""
  if [ "$DARK_MODE" = true ]; then
    subdir="/dark"
  fi
  echo "${IMAGES_DIR}/bosses${subdir}/boss_${boss_id}.png"
}

# メイン処理
case "$1" in
  evolution)
    level="${2:-1}"
    img=$(get_evolution_image "$level")
    show_image "$img" "${3:-40}"
    ;;
  boss)
    boss_id="$2"
    img=$(get_boss_image "$boss_id")
    show_image "$img" "${3:-50}"
    ;;
  auto)
    # progress.jsonから自動判定
    PROGRESS="${BASE_DIR}/gorilla_data/progress.json"
    if [ ! -f "$PROGRESS" ]; then
      echo "⚠️ progress.json が見つかりません"
      exit 1
    fi
    level=$(python3 -c "import json; print(json.load(open('${PROGRESS}'))['player']['power_level'])")
    img=$(get_evolution_image "$level")
    show_image "$img" "${2:-40}"
    ;;
  *)
    echo "Usage:"
    echo "  show-gorilla.sh [--dark] evolution <power_level> [width]"
    echo "  show-gorilla.sh [--dark] boss <boss_id> [width]"
    echo "  show-gorilla.sh [--dark] auto [width]"
    echo ""
    echo "Options:"
    echo "  --dark, -d    ダークモード版の画像を表示"
    ;;
esac
