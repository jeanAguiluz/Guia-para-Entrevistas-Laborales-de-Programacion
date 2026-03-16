from __future__ import annotations

import argparse
import html
import subprocess
import sys
from pathlib import Path
import shutil


BROWSER_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
]


HTML_TEMPLATE = """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <style>
      @page {{
        size: A4;
        margin: 18mm 14mm;
      }}

      html, body {{
        margin: 0;
        padding: 0;
        background: #ffffff;
        color: #111111;
      }}

      body {{
        font-family: Consolas, "Courier New", monospace;
        font-size: 11pt;
        line-height: 1.45;
      }}

      pre {{
        margin: 0;
        white-space: pre-wrap;
        word-break: break-word;
        overflow-wrap: anywhere;
      }}
    </style>
  </head>
  <body>
    <pre>{content}</pre>
  </body>
</html>
"""


def find_browser() -> Path:
    for candidate in BROWSER_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No compatible Chromium browser was found.")


def collect_readmes(repo_root: Path) -> list[Path]:
    return sorted(path for path in repo_root.rglob("*") if path.is_file() and path.name.lower() == "readme.md")


def export_pdf(browser_path: Path, html_path: Path, pdf_path: Path, profile_dir: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        str(browser_path),
        "--headless",
        "--disable-gpu",
        "--no-first-run",
        "--allow-file-access-from-files",
        f"--user-data-dir={profile_dir}",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        html_path.resolve().as_uri(),
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0 or not pdf_path.exists():
        raise RuntimeError(
            f"Failed to export {html_path} to PDF.\n"
            f"Exit code: {result.returncode}\n"
            f"STDOUT: {result.stdout}\n"
            f"STDERR: {result.stderr}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Export all README.md files in the repo to PDF.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root to scan.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path.cwd() / "pdf-readmes",
        help="Directory where PDFs will be written.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    output_dir = args.output_dir.resolve()
    temp_root = output_dir / ".tmp"
    html_root = temp_root / "html"
    profile_root = temp_root / "browser-profile"
    browser_path = find_browser()
    readmes = collect_readmes(repo_root)

    if not readmes:
        print("No README.md files were found.", file=sys.stderr)
        return 1

    if temp_root.exists():
        shutil.rmtree(temp_root)

    html_root.mkdir(parents=True, exist_ok=True)
    profile_root.mkdir(parents=True, exist_ok=True)

    try:
        for readme_path in readmes:
            relative_path = readme_path.relative_to(repo_root)
            pdf_path = output_dir / relative_path.with_suffix(".pdf")

            html_dir = html_root / relative_path.parent
            html_dir.mkdir(parents=True, exist_ok=True)
            html_path = html_dir / relative_path.with_suffix(".html").name

            content = readme_path.read_text(encoding="utf-8")
            html_path.write_text(
                HTML_TEMPLATE.format(
                    title=html.escape(str(relative_path)),
                    content=html.escape(content),
                ),
                encoding="utf-8",
            )

            export_pdf(browser_path, html_path, pdf_path, profile_root)
            print(f"PDF created: {pdf_path}")
    finally:
        if temp_root.exists():
            shutil.rmtree(temp_root, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
