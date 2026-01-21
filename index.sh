#!/usr/bin/env bash
set -euo pipefail

echo "Runestone index:"
git grep -n --no-color "rune-" | awk -F: '{print $1": "$2}' | sort | uniq
