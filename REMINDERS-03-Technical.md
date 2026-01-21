# Reminders 03 — Technical

- fd:3 passphrase flow example:
  ./tools/garden_secret_wrapper.sh ~/.local/share/garden-secret/secret.gpg -- dec -b - < blobs/test_vector.txt

- Clipboard-safe recovery:
  ./tools/garden_secret_wrapper.sh ~/.local/share/garden-secret/secret.gpg -- dec -b - < blobs/test_vector.txt | pbcopy
