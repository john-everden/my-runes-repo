# Recall Library Reminders

This file captures the mnemonic and rituals for maintaining the recall library.

---

## Mnemonic: k qk qk qk k

- **k** — Keep: publish public runestones; keep hints and passphrases offline.  
- **qk** — Quiet Key: never display the real key; use fd:3 flow to decrypt quietly.  
- **qk qk qk** — Triple Quiet: encrypted storage, hardware backup, scheduled rotation.  
- **k qk qk qk k** — Lifecycle: publish anchors → protect keys → test recovery → rotate → archive.

---

## Garden Rituals

🌱 **Planting anchors**  
Each runestone is a seed. Publish it in files or manifests as a public marker.

🌿 **Quiet tending**  
Decrypt passphrases silently (fd:3 flow). Never print them, never commit them.

🌳 **Triple quiet**  
- Encrypted storage (soil)  
- Hardware/paper backup (roots)  
- Rotation policy (seasons)

🌸 **Lifecycle**  
Keep → Quiet → Quiet → Quiet → Keep

---

## Practical Steps

1. **Add runestone**: insert a token comment in a file.  
2. **Update manifest**: record rune, file, date, author.  
3. **Verify**: run `./verify.sh` to list anchors and check for forbidden files.  
4. **Push**: commit and let CI scan for secrets.  
5. **Record hint offline**: never in Git, always in secure storage.

---

## Safety Notes

- Never commit passphrases, `.gpg` files, private keys, or plaintext secrets.  
- Back up encrypted passphrase and GPG private key offline.  
- Prefer public-key encryption for multi-device recovery.  
- Sign manifests with your PGP key to prove provenance.

