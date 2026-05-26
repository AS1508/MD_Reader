## 1. Project Setup

- [x] 1.1 Create `mdp.py` main application file with shebang and imports
- [x] 1.2 Create `requirements.txt` with dependencies (`markdown`, `tkinterweb`)
- [x] 1.3 Create `.gitignore` for Python project (venv, __pycache__, dist, build)

## 2. GUI Foundation

- [x] 2.1 Build main tkinter window with title, size, and basic layout
- [x] 2.2 Add File menu with Open and Exit items
- [x] 2.3 Add HtmlFrame widget for rendering markdown output

## 3. File Handling

- [x] 3.1 Implement File > Open with native file dialog filtered to `.md` files
- [x] 3.2 Read selected file content and pass to renderer
- [x] 3.3 Support opening a file via command-line argument on startup
- [x] 3.4 Show error message for missing or unreadable files
- [x] 3.5 Update window title to show "mdp - <filename>"

## 4. Markdown Rendering

- [x] 4.1 Implement markdown-to-HTML conversion using `markdown` library
- [x] 4.2 Add basic CSS styling for rendered HTML (headings, code blocks, lists, etc.)
- [x] 4.3 Handle edge cases: empty file, large files (no crash)

## 5. Packaging

- [x] 5.1 Create PyInstaller `.spec` file to bundle into single Windows `.exe`
- [x] 5.2 Test packaged executable on Windows
