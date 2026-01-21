# Contributing to Runestones

Guidelines for adding public runestones and keeping hints offline.

- **Public tokens only**: Add only the token string (e.g., `rune-7f4b2a1c-HYDR`) to files or RUNES.md.
- **Hints stay offline**: Keep one-word hints or passphrase reminders offline (paper, password manager, hardware key).
- **One runestone per file**: Prefer a single runestone comment per file to keep indexing simple.
- **No secrets**: Never commit passphrases, `.gpg` files, private keys, or other secret material.
- **Verification**: Run `./verify.sh` locally before committing.
- **CI**: The repository includes a workflow that fails on common secret filenames. If CI fails, remove the offending file and force a clean commit.

