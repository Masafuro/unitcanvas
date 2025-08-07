#!/usr/bin/env python3
"""
Generate subset fonts based on HTML files that use class names starting with f_.
This version relies only on the Python standard library (html.parser) and
fontTools' pyftsubset CLI, so it removes the BeautifulSoup dependency.

Usage:
    python subset_font_builder.py

Requirements:
    - Python 3.8+
    - fonttools (pip install fonttools)
    - The original TTF files placed in the `fonts/` directory, e.g. fonts/NotoSansJP.ttf
    - HTML files containing <tag class="f_FontName">Text</tag>
    - pyftsubset must be on PATH (installed with fonttools)

The script scans HTML files defined by HTML_PATTERNS, extracts the characters
used with each font prefix, and produces subset WOFF2 and WOFF files under
`subfonts/`.
"""

import os
import glob
import subprocess
from html.parser import HTMLParser

# ---------- Configuration ----------
FONTS_DIR = "fonts"          # Directory containing original .ttf files
OUTPUT_DIR = "subfonts"       # Directory where subset fonts will be written
HTML_PATTERNS = ["index.html", os.path.join("pages", "*.html")]  # HTML files to scan


class FontTextExtractor(HTMLParser):
    """Collect text nodes associated with class names starting with f_."""

    def __init__(self):
        super().__init__()
        self.font_stack: list[list[str]] = []  # Stack of font lists for each level
        self.collected: dict[str, list[str]] = {}

    def handle_starttag(self, tag, attrs):
        class_attr = dict(attrs).get("class", "")
        fonts = [c[2:] for c in class_attr.split() if c.startswith("f_")]
        self.font_stack.append(fonts)

    def handle_endtag(self, tag):
        if self.font_stack:
            self.font_stack.pop()

    def handle_data(self, data):
        stripped = data.strip()
        if not stripped:
            return
        active_fonts = {f for fonts in self.font_stack for f in fonts}
        for font in active_fonts:
            self.collected.setdefault(font, []).append(stripped)


def extract_text_by_font(html_path: str) -> dict[str, list[str]]:
    """Return {font_name: [text,...]} for one HTML file."""

    parser = FontTextExtractor()
    with open(html_path, encoding="utf-8") as fp:
        parser.feed(fp.read())
    return parser.collected


# ---------- Main routine ----------

def main() -> None:
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Collect HTML files
    html_files: list[str] = []
    for pattern in HTML_PATTERNS:
        html_files.extend(glob.glob(pattern))

    if not html_files:
        print("対象のHTMLファイルが見つかりませんでした。")
        return

    # Aggregate text per font across all HTML files
    all_font_texts: dict[str, list[str]] = {}
    for html in html_files:
        font_texts = extract_text_by_font(html)
        for font, texts in font_texts.items():
            all_font_texts.setdefault(font, []).extend(texts)

    if not all_font_texts:
        print("サブセット化対象のフォントクラスがHTMLから検出されませんでした。")
        return

    # Generate subset fonts
    for font, texts in all_font_texts.items():
        # Remove control characters except space (U+0020)
        unique_chars = {c for c in "".join(texts) if not c.isspace() or c == " "}
        if not unique_chars:
            print(f"[{font}] 抽出文字なし、スキップ")
            continue

        unicodes = ",".join(f"U+{ord(c):04X}" for c in sorted(unique_chars))
        input_path = os.path.join(FONTS_DIR, f"{font}.ttf")
        if not os.path.isfile(input_path):
            print(f"フォントファイルが見つかりません: {input_path}")
            continue

        # WOFF2 subset
        woff2_out = os.path.join(OUTPUT_DIR, f"{font}.woff2")
        subprocess.run([
            "pyftsubset",
            input_path,
            f"--output-file={woff2_out}",
            "--flavor=woff2",
            f"--unicodes={unicodes}",
        ], check=True)

        # WOFF subset
        woff_out = os.path.join(OUTPUT_DIR, f"{font}.woff")
        subprocess.run([
            "pyftsubset",
            input_path,
            f"--output-file={woff_out}",
            "--flavor=woff",
            f"--unicodes={unicodes}",
        ], check=True)

        print(f"[{font}] サブセットフォントを生成しました: {woff2_out}, {woff_out}")


if __name__ == "__main__":
    main()
