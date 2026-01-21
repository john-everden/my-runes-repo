#!/usr/bin/env bash
set -euo pipefail

# Simple runestone verifier
echo "Runestone scan"
echo "--------------"

# Count runestones in repo
count=$(git grep -n --no-color -E "rune-[0-9a-fA-F]{8}-[A-Z]{3,4}" | wc -l)
echo "Total runestone occurrences: $count"

# List files containing runestones
echo
echo "Files containing runestones:"
git grep -n --no-color -E "rune-[0-9a-fA-F]{8}-[A-Z]{3,4}" || true

# Quick check for accidental secret files
echo
echo "Quick secret file check (common patterns):"
git ls-files | grep -Ei "secret|\.gpg|secret\." || echo "No obvious secret filenames tracked."

exit 0

