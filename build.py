import glob
import os
import re

def build():
    # 1. Get core CSS files directly in src/ (sorted alphabetically)
    core_files = sorted(glob.glob("src/*.css"))
    
    # 2. Get plugin/feature CSS files from subdirectories (sorted alphabetically)
    plugin_files = []
    for root, dirs, files in os.walk("src"):
        # Skip the root src/ folder itself to avoid duplicates
        if os.path.normpath(root) == os.path.normpath("src"):
            continue
        for file in files:
            if file.endswith(".css"):
                plugin_files.append(os.path.join(root, file))
    plugin_files.sort()
    
    all_files = core_files + plugin_files
    print("Found files to compile:")
    for f in all_files:
        print(f"  - {f}")
        
    out_lines = []
    for filepath in all_files:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                # 1. Remove single-line comments: /* ... */
                processed = re.sub(r'/\*.*?\*/', '', line)
                # 2. Strip trailing whitespaces
                processed = processed.rstrip()
                # 3. If line is not empty, keep it
                if processed:
                    out_lines.append(processed)
                    
    # Write to root theme.css
    with open("theme.css", "w", encoding="utf-8") as out:
        out.write("\n".join(out_lines) + "\n")
    print("theme.css successfully compiled!")

if __name__ == "__main__":
    build()
