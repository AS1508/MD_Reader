#!/usr/bin/env python3
"""mdp - A simple markdown reader for Windows."""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
from tkinterweb import HtmlFrame


def render_markdown(html_frame, header_label, filepath):
    """Read a markdown file and render it as HTML."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except (IOError, OSError) as e:
        messagebox.showerror("Error", f"Cannot open file:\n{e}")
        return False

    if not text.strip():
        html_frame.load_html("<p style='color:#aaa;'><em>Empty file</em></p>")
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
    color: #333;
    padding: 12px 28px;
    max-width: 800px;
    margin: 0 auto;
}}
h1, h2, h3, h4, h5, h6 {{
    margin-top: 20px;
    margin-bottom: 8px;
    font-weight: 500;
    color: #333;
}}
h1 {{ font-size: 24px; }}
h2 {{ font-size: 20px; }}
h3 {{ font-size: 16px; }}
code {{
    background-color: #f8f8f8;
    padding: 2px 5px;
    border-radius: 2px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 13px;
    color: #555;
}}
pre {{
    background-color: #f8f8f8;
    padding: 10px 14px;
    border-radius: 3px;
    overflow-x: auto;
}}
pre code {{
    background: none;
    padding: 0;
}}
blockquote {{
    border-left: 3px solid #e0e0e0;
    margin-left: 0;
    padding-left: 14px;
    color: #777;
}}
table {{
    border-collapse: collapse;
    width: 100%;
}}
th, td {{
    border: 1px solid #eee;
    padding: 6px 10px;
    text-align: left;
}}
th {{ background-color: #fafafa; font-weight: 500; }}
img {{ max-width: 100%; }}
a {{ color: #555; text-decoration: underline; }}
ul, ol {{ padding-left: 20px; }}
</style>
</head>
<body>
{html_content}
</body>
</html>"""
        html_frame.load_html(styled_html)

    filename = os.path.basename(filepath)
    header_label.config(text=filename)
    return True


def open_file(root, html_frame, header_label):
    """Open a markdown file via dialog."""
    filepath = filedialog.askopenfilename(
        title="Open Markdown File",
        filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
    )
    if filepath and render_markdown(html_frame, header_label, filepath):
        root.title(f"mdp - {os.path.basename(filepath)}")


def main():
    root = tk.Tk()
    root.title("mdp")
    root.geometry("900x650")
    root.minsize(400, 300)
    root.configure(bg='#fff')

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    header = tk.Frame(root, bg='#fff', height=32)
    header.grid(row=0, column=0, sticky="ew")
    header.grid_propagate(False)

    header_label = tk.Label(
        header,
        text="No file open",
        bg='#fff',
        fg='#aaa',
        font=('Segoe UI', 11),
        anchor='w',
        padx=16
    )
    header_label.pack(fill='both', expand=True)

    html_frame = HtmlFrame(root, messages_enabled=False)
    html_frame.grid(row=1, column=0, sticky="nsew")
    html_frame.load_html(
        "<p style='color:#aaa; text-align:center; padding-top:40px;'>"
        "Ctrl+O to open a markdown file</p>"
    )

    root.bind("<Control-o>", lambda e: open_file(root, html_frame, header_label))
    root.bind("<Escape>", lambda e: root.quit())

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if os.path.isfile(filepath):
            render_markdown(html_frame, header_label, filepath)
            root.title(f"mdp - {os.path.basename(filepath)}")
        else:
            messagebox.showerror("Error", f"File not found:\n{filepath}")

    root.mainloop()


if __name__ == "__main__":
    main()
