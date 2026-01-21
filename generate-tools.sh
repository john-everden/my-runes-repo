#!/usr/bin/env bash
set -euo pipefail

# verify.sh — scan for runestones and forbidden filenames
cat > verify.sh <<EOF
#!/usr/bin/env bash
set -euo pipefail

echo "Runestone scan"
git grep -n --no-color "rune-" || echo "No runestones found."

echo
echo "Forbidden filename check:"
git ls-files | grep -Ei "secret|\\.gpg|\\.pem|\\.key|id_rsa" || echo "No forbidden files tracked."
EOF
chmod +x verify.sh

# restore.sh — decrypt blob using fd:3 flow
cat > restore.sh <<EOF
#!/usr/bin/env bash
set -euo pipefail

SECRET_FILE="\${1:-~/.local/share/garden-secret/secret.gpg}"
BLOB_FILE="\${2:-blobs/test_vector.txt}"

./tools/garden_secret_wrapper.sh "\$SECRET_FILE" -- dec -b - < "\$BLOB_FILE"
EOF
chmod +x restore.sh

# rotate.sh — rotate passphrase yearly
cat > rotate.sh <<EOF
#!/usr/bin/env bash
set -euo pipefail

NEW_SECRET="\${1:-new-secret.gpg}"
echo "Generating new passphrase..."
openssl rand -base64 64 | gpg --symmetric --cipher-algo AES256 --output "\$NEW_SECRET"
echo "New encrypted passphrase stored at \$NEW_SECRET"
EOF
chmod +x rotate.sh

# index.sh — build simple runestone index
cat > index.sh <<EOF
#!/usr/bin/env bash
set -euo pipefail

echo "Runestone index:"
git grep -n --no-color "rune-" | awk -F: '{print \$1": "\$2}' | sort | uniq
EOF
chmod +x index.sh

# pre-commit hook installer — block secret files
mkdir -p .git/hooks
cat > .git/hooks/pre-commit <<EOF
#!/usr/bin/env bash
set -euo pipefail

matches=\$(git diff --cached --name-only | grep -Ei "secret|\\.gpg|\\.pem|\\.key|id_rsa" || true)
if [ -n "\$matches" ]; then
  echo "ERROR: Attempting to commit forbidden files:"
  echo "\$matches"
  exit 1
fi
EOF
chmod +x .git/hooks/pre-commit

echo "All helper scripts generated: verify.sh, restore.sh, rotate.sh, index.sh, pre-commit hook."

