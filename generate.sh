#!/usr/bin/env bash
cd "$(dirname "$0")"

echo "============================================"
echo "  Velocity Spanish - Video Generator"
echo "============================================"
echo ""
echo "[1] Long-form video"
echo "[2] Reels (short)"
echo ""
read -p "Choose (1 or 2): " MODE
echo ""

if [ "$MODE" = "2" ]; then
    python3 facebook_reels_automation.py
    exit 0
fi

read -p "Number of phrases (default 60): " PHRASES
PHRASES=${PHRASES:-60}

read -p "Category (blank = random): " CATEGORY
echo ""

if [ -n "$CATEGORY" ]; then
    python3 youtube_longform_automation.py --phrases "$PHRASES" --category "$CATEGORY"
else
    python3 youtube_longform_automation.py --phrases "$PHRASES"
fi

echo ""
echo "Done!"
