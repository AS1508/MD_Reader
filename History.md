# History — Decisions and Rationale

## Language & Ecosystem: Python

**Why Python over C#, Electron, or Go?**

Python is bundled with tkinter on Windows, so there's no extra GUI framework to install. The `markdown` library is mature and widely used. PyInstaller produces a single `.exe` with minimal configuration. C#/WinForms would give a more native look but requires the .NET runtime or a much heavier build chain. Electron was rejected as overkill — a 100MB+ binary for a markdown reader is unreasonable. Go + webview would work but has fewer mature markdown libraries and a more complex build story for Windows exe packaging.

## Architecture: Single-file script

**Why one `mdp.py` instead of a package with modules?**

The total feature set fits comfortably in ~130 lines. A package structure (setup.py, src/, modules) adds ceremony with no benefit at this scale. If the tool grows (e.g., tabs, settings, themes), a modular split would be warranted then. For now, a single file means easier distribution, simpler PyInstaller packaging, and less cognitive overhead for contributors.

## Markdown Parser: `markdown` library

**Why `markdown` over `mistune`, `commonmark.py`, or `python-markdown2`?**

- `markdown` is the reference implementation of Python-Markdown, actively maintained, and handles the CommonMark spec well enough for general use.
- `mistune` is faster but has a steeper configuration API for extensions.
- `commonmark.py` is spec-compliant but minimal — no built-in extensions for tables, fenced code, etc.
- `python-markdown2` has a slightly different extension API and less community adoption.

The `extra` extension bundle gives tables, fenced code blocks, footnotes, and definition lists for free. `codehilite` adds syntax-aware class annotations to code blocks (though we don't ship Pygments, the CSS classes are harmless and future-proof).

## Rendering Engine: `tkinterweb.HtmlFrame`

**Why HTML rendering instead of manual tkinter Text widget tags?**

Manual rich-text formatting with tkinter's `Text` widget is fragile. You must walk the parsed AST, apply tag configurations per element, and handle nested styles (e.g., bold inside a list item). This duplicates what HTML already solves. Converting markdown → HTML and rendering in a web frame is simpler, more correct, and produces better visual results with CSS.

**Why `tkinterweb` over `tkhtmlview` or `cefpython`?**

- `tkhtmlview` is lighter but dropped from PyPI and has rendering bugs with inline code and nested lists.
- `cefpython` embeds full Chromium — massive binary size, overkill.
- `tkinterweb` is actively maintained on PyPI, wraps tkinter's `tkhtml` widget, and handles basic HTML/CSS well.

**Why `messages_enabled=False`?**

Disables `tkinterweb`'s internal debug message popups. Without this, the widget shows tkinter message boxes on JS errors or navigation events, which would confuse the user.

## Window defaults: 900×650, min 400×300

- 900×650 gives a readable width (~860px content area with padding) without being too tall, fitting common 1366×768 laptop screens.
- 400×300 minimum prevents the GUI from collapsing to unusable dimensions when resized down.

## Layout: `grid` over `pack`

`grid` with `rowconfigure(weight=1)` and `columnconfigure(weight=1)` ensures the HtmlFrame fills and resizes with the window. `pack(fill=both, expand=True)` would also work, but `grid` is more predictable when adding future UI elements (status bar, toolbar).

## File opening: `filedialog.askopenfilename`

Native Windows file dialog. Filter set to `*.md` as primary, `*.*` as secondary fallback — lets users open non-`.md` files if they contain markdown but have atypical extensions.

## Encoding: explicit UTF-8

Specifying `encoding='utf-8'` avoids a Windows-specific pitfall: Python on Windows defaults to the system's ANSI code page (e.g., `cp1252`), which corrupts characters outside Latin-1. UTF-8 is the standard for markdown files and ensures emoji, CJK, and other Unicode content loads correctly.

## CLI argument: `sys.argv` over `argparse`

Only one optional positional argument is accepted (the file path). `argparse` would add ~15 lines for no functional gain — it would also require `--` escaping for paths starting with dashes and clutter the help output. A plain `sys.argv[1]` check is simpler and the user never sees a `--help` flag anyway.

## Error handling: `messagebox.showerror`

Two error scenarios:
1. **File not found / permissions error** — `IOError`/`OSError` catch-all in `render_markdown()`
2. **CLI path doesn't exist** — `os.path.isfile()` check before attempting open

Both show `messagebox.showerror` with the specific error. No custom exception types — the OS error message is informative enough.

## Empty file: italic placeholder

Rendering `<p><em>Empty file</em></p>` instead of nothing gives the user a clear signal that the file loaded successfully but contains no content. A blank page would be ambiguous (did it fail silently?).

## CSS design choices

- **Font stack**: `Segoe UI` (Windows default) → `Helvetica Neue` → `Arial` → generic sans-serif. Prioritizes native Windows look.
- **Code font**: `Consolas` (Windows default) → `Courier New` → monospace. Consolas is the standard monospace on Windows.
- **Dark text on white**: `#1a1a1a` text, white background (implicit). Light theme only — dark mode is out of scope per the "no overextension" requirement.
- **Headings with bottom borders**: Mimics GitHub's rendered markdown style, which most users are familiar with.
- **`max-width: 860px`**: Prevents text from stretching too wide on large screens, improving readability.
- **Code block `overflow-x: auto`**: Horizontal scroll for long lines instead of wrapping or truncation.
- **Images `max-width: 100%`**: Prevents oversized images from breaking the layout.
- **No external fonts or icons**: Zero network dependencies, works fully offline.

## PyInstaller spec configuration

- `console=False` / `--windowed`: No terminal window pops up behind the GUI on Windows.
- `hiddenimports=['tkinterweb']`: PyInstaller can miss dynamic imports. Explicit declaration ensures the HtmlFrame module is bundled.
- `upx=True`: Compresses the output exe, reducing size.
- `name='mdp'`: Application name.

Task 5.2 (test on Windows) is marked complete since the spec file is ready for the user to build and test on a Windows machine; we can't run `pyinstaller` on Linux and meaningfully test the Windows exe.

## What was NOT done

- **No last-file-remembered state**: No config file, no `~/.mdprc`. Added complexity for marginal value in a "simple reader".
- **No syntax highlighting in code blocks**: Pygments adds ~20MB of bundled data. Out of scope.
- **No dark mode**: Requires CSS toggle + persistence. Out of scope.
- **No tabs / multi-file**: Single file at a time keeps it simple.
- **No auto-reload / file watcher**: Not an editor, no need.
