#!/usr/bin/env bash
set -euo pipefail

NEW_SECRET="${1:-new-secret.gpg}"
echo "Generating new passphrase..."
openssl rand -base64 64 | gpg --symmetric --cipher-algo AES256 --output "$NEW_SECRET"
echo "New encrypted passphrase stored at $NEW_SECRET"
