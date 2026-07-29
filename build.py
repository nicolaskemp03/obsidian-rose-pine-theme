#!/usr/bin/env python3
"""
Build script for the Rosé Pine Obsidian theme.

Compiles src/theme.scss → theme.css using Dart Sass.

Requires: npm install -g sass
  Or run via npx: npx sass src/theme.scss theme.css --no-source-map
"""

import subprocess
import shutil
import sys


def check_sass():
    """Check if sass is available via global install or npx."""
    if shutil.which("sass"):
        return ["sass"]
    # Fall back to npx
    if shutil.which("npx"):
        return ["npx", "-y", "sass"]
    return None


def build():
    sass_cmd = check_sass()
    if sass_cmd is None:
        print("ERROR: Dart Sass is not installed.")
        print("Install it with:  npm install -g sass")
        print("Or ensure npx is available (comes with Node.js).")
        sys.exit(1)

    cmd = sass_cmd + [
        "src/theme.scss",
        "theme.css",
        "--no-source-map",
        "--style=expanded",
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("ERROR: Sass compilation failed!")
        print(result.stderr)
        sys.exit(1)

    print(result.stdout, end="")
    print("theme.css successfully compiled!")


if __name__ == "__main__":
    build()
