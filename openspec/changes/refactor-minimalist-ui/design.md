## Context

Current `mdp.py` uses a traditional tkinter menubar (File > Open, File > Exit). This adds vertical space and visual weight that distracts from the markdown content. The goal is to strip the UI down to just the content + a thin header.

## Goals / Non-Goals

**Goals:**
- Remove the menubar entirely
- Add a minimal header bar showing the filename
- Style the header to blend into the window (not a distinct bar)
- Simplify CSS for a lighter, less decorative look
- Keep `Ctrl+O` to open files

**Non-Goals:**
- Drag-and-drop file support
- Fullscreen mode
- Custom title bar / removing window decorations
- Toolbar buttons or icons
- Any new files or dependencies

## Decisions

1. **tkinter `Frame` for the header** — a thin frame at the top with a `Label` showing the filename. Simple, no external widgets needed.
   - Alternative: `ttk.Label` with custom styling — same result, more tkinter themes. Not worth it.

2. **Keyboard-only interaction** — `Ctrl+O` opens files, `Esc` still closes (via Exit binding). No menu means users must know the shortcut, but the startup message will show it.
   - Alternative: right-click context menu — adds complexity for no real gain since shortcuts are standard.

3. **CSS simplification** — softer `#333` text, `#f8f8f8` code backgrounds, no heading borders, tighter padding. Removes the GitHub-clone look for something lighter.
   - No dark mode — out of scope, just cleaner light mode.

## Risks / Trade-offs

- [Risk] Users may not discover `Ctrl+O` without a visual menu → Mitigation: Startup placeholder text says "Ctrl+O to open a markdown file"
- [Risk] `Esc` to close is non-standard on Windows → Mitigation: Keep it for power users, but Windows Alt+F4 also works
