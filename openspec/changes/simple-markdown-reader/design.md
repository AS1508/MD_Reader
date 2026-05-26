## Context

A new Windows desktop application with zero prior code. The user wants a simple markdown reader — open a `.md` file and see it rendered. No editing, no live preview, no multi-file navigation.

**Constraints:**
- Windows target platform
- Minimal dependencies
- Simple to build and package

## Goals / Non-Goals

**Goals:**
- Open `.md` files via File > Open or command-line argument
- Render markdown with formatted output (headings, bold, italic, code, lists, links)
- Package as a standalone Windows `.exe`

**Non-Goals:**
- Markdown editing
- Live preview / auto-reload on file change
- Multiple tabs or file navigation
- Syntax highlighting in code blocks
- Custom themes or styling
- Cross-platform support (Linux/macOS) — though it will likely work

## Decisions

1. **Python + tkinter** over C#/WinForms, Electron, or Go+webview
   - tkinter is bundled with Python on Windows, no extra GUI framework needed
   - Python has excellent markdown parsing via the `markdown` library
   - PyInstaller can produce a single `.exe` easily
   - Trade-off: Not a native-feeling Windows app, but good enough for "simple"

2. **HTML-based rendering via `tkinterweb.HtmlFrame`** over manual rich-text formatting
   - Converts markdown → HTML using `markdown` library
   - HtmlFrame renders HTML directly in a tkinter widget
   - Much simpler than manual formatting with tkinter Text tags
   - Alternative considered: Opening in default browser — rejected because user wants a standalone app

3. **Single-file Python script** — no package structure needed for this scope
   - One `mdp.py` file with all logic
   - Straightforward to run and package

## Risks / Trade-offs

- [Risk] `tkinterweb` is a third-party dependency and may have rendering quirks → Mitigation: Use minimal CSS; test with common markdown patterns
- [Risk] Embedded HTML rendering may not look pixel-perfect on all Windows versions → Mitigation: Accept slight visual variation; focus on readability over polish
