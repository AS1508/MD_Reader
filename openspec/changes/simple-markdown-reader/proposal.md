## Why

Reading markdown files on Windows currently requires a code editor (like VS Code) or a full browser. There is no simple, lightweight viewer that just opens a `.md` file and renders it cleanly. This tool fills that gap with a minimal, no-fuss markdown reader.

## What Changes

- New Windows desktop application that opens and renders `.md` files
- Basic markdown rendering: headings, bold, italic, code blocks, lists, links, images
- File open dialog to select markdown files
- Simple, clean GUI with rendered output

## Capabilities

### New Capabilities
- `markdown-rendering`: Parse markdown text and render it as formatted HTML/output in the GUI
- `file-handling`: Open `.md` files from the filesystem via file dialog

### Modified Capabilities
<!-- None, this is a new project -->

## Impact

- New Python-based desktop application
- Dependencies: Python `markdown` library for parsing, `tkinter` for GUI (bundled with Python on Windows)
- Packaged as a standalone Windows executable via PyInstaller
