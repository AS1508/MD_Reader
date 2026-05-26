## Why

The current UI has a traditional menubar and dense styling that adds visual noise. A minimalist redesign puts the markdown content first — less chrome, fewer distractions, quicker access via keyboard.

## What Changes

- **BREAKING**: Remove File menubar. Keyboard shortcuts (`Ctrl+O`, `Esc`) replace menu interaction.
- Add a minimal header bar showing just the filename — no buttons, no chrome.
- Simplify CSS: softer palette, no heading borders, lighter code blocks, reduced padding.
- Window title and CLI arg behavior unchanged.

## Capabilities

### New Capabilities
- `minimal-header`: Thin header bar displaying the current filename — no buttons or menu

### Modified Capabilities
- `file-handling`: File > Open menu replaced by `Ctrl+O` keyboard shortcut and context menu
- `markdown-rendering`: CSS restyled for a cleaner, more minimal appearance

## Impact

- Only `mdp.py` is modified. No new dependencies, no new files.
- Existing keyboard shortcut `Ctrl+O` is kept; menu-based opening is removed.
