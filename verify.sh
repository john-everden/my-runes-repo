#!/usr/bin/env bash
set -euo pipefail

echo "Runestone scan"
git grep -n --no-color "rune-" || echo "No runestones found."

echo
echo "Forbidden filename check:"
git ls-files | grep -Ei "secret|\.gpg|\.pem|\.key|id_rsa" || echo "No forbidden files tracked."
