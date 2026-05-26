#!/usr/bin/env python3
"""mdp - A simple markdown reader for Windows."""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
from tkinterweb import HtmlFrame


def render_markdown(html_frame, filepath):
    """Read a markdown file and render it as HTML."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except (IOError, OSError) as e:
        messagebox.showerror("Error", f"Cannot open file:\n{e}")
        return False

    if not text.strip():
        html_frame.load_html("<p style='color:#888;'><em>Empty file</em></p>")
    else:
        html_content = markdown.markdown(
            text,
            extensions=['extra', 'codehilite']
        )
        styled_html = f"""<!DOCTYPE html>
<html>
<head>
<style>
body {{
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: #1a1a1a;
    padding: 20px 30px;
    max-width: 860px;
    margin: 0 auto;
}}
h1, h2, h3, h4, h5, h6 {{
    margin-top: 24px;
    margin-bottom: 12px;
    font-weight: 600;
    color: #222;
}}
h1 {{ font-size: 28px; border-bottom: 1px solid #ddd; padding-bottom: 8px; }}
h2 {{ font-size: 22px; border-bottom: 1px solid #eee; padding-bottom: 6px; }}
h3 {{ font-size: 18px; }}
code {{
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 13px;
}}
pre {{
    background-color: #f4f4f4;
    padding: 12px 16px;
    border-radius: 4px;
    overflow-x: auto;
}}
pre code {{
    background: none;
    padding: 0;
}}
blockquote {{
    border-left: 4px solid #ccc;
    margin-left: 0;
    padding-left: 16px;
    color: #555;
}}
table {{
    border-collapse: collapse;
    width: 100%;
}}
th, td {{
    border: 1px solid #ddd;
    padding: 8px 12px;
    text-align: left;
}}
th {{ background-color: #f2f2f2; }}
img {{ max-width: 100%; }}
a {{ color: #0366d6; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
ul, ol {{ padding-left: 24px; }}
</style>
</head>
<body>
{html_content}
</body>
</html>"""
        html_frame.load_html(styled_html)
    return True


def open_file(root, html_frame):
    """Open a markdown file via dialog."""
    filepath = filedialog.askopenfilename(
        title="Open Markdown File",
        filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
    )
    if filepath and render_markdown(html_frame, filepath):
        root.title(f"mdp - {os.path.basename(filepath)}")


def main():
    root = tk.Tk()
    root.title("mdp")
    root.geometry("900x650")
    root.minsize(400, 300)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    html_frame = HtmlFrame(root, messages_enabled=False)
    html_frame.grid(row=0, column=0, sticky="nsew")
    html_frame.load_html(
        "<p style='color:#888; text-align:center; padding-top:40px;'>"
        "File &gt; Open to read a markdown file</p>"
    )

    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(
        label="Open...",
        command=lambda: open_file(root, html_frame),
        accelerator="Ctrl+O"
    )
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menubar)

    root.bind("<Control-o>", lambda e: open_file(root, html_frame))

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if os.path.isfile(filepath):
            render_markdown(html_frame, filepath)
            root.title(f"mdp - {os.path.basename(filepath)}")
        else:
            messagebox.showerror("Error", f"File not found:\n{filepath}")

    root.mainloop()


if __name__ == "__main__":
    main()
