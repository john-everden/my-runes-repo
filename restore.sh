#!/usr/bin/env bash
set -euo pipefail

SECRET_FILE="${1:-~/.local/share/garden-secret/secret.gpg}"
BLOB_FILE="${2:-blobs/test_vector.txt}"

./tools/garden_secret_wrapper.sh "$SECRET_FILE" -- dec -b - < "$BLOB_FILE"
