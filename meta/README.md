# Translation Layer

This folder contains the **translation system** for the recall library.  
It is not a secret language — it is a **symbolic shorthand** designed to be universally legible, minimal, and portable.

## Purpose
- Provide a parallel language alongside English for reminders and commit messages.
- Use symbols and tokens to capture themes like Foundation, Flow, Memory, Guardians, Completion, Renewal, etc.
- Keep the repo transparent while adding a creative, ritual layer.

## Vocabulary
The mapping is defined in `translation.json`.  
Examples:

| Concept     | Symbol | Meaning                        |
|-------------|--------|--------------------------------|
| Foundation  | ⧉      | Base, anchor, root             |
| Flow        | ~>     | Continuity, progression        |
| Memory      | ∞      | Recall, persistence            |
| Guardians   | ⚔      | Protection, resilience         |
| Completion  | ◎      | Cycle closed, archive          |
| Renewal     | ✦      | New beginning                  |
| Community   | ☉      | Shared presence                |
| Signal      | ↯      | Marker, runestone              |
| Thread      | ⟲      | Strand in the weave            |
| Map         | ⌖      | Guidance, chart                |

## Usage
Run the translator script on reminder files:
```bash
./translate-reminders.py REMINDERS-*.md > translation-log.txt

