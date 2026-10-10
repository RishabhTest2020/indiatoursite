import os
import re

ROOT_DIR = r"c:\Users\Hp\PycharmProjects\indiatoursite"
PAGES_INSIDE = os.path.join(ROOT_DIR, "Pages-inside")

html_files = [os.path.join(ROOT_DIR, "index.html")]
for f in sorted(os.listdir(PAGES_INSIDE)):
    if f.endswith(".html"):
        html_files.append(os.path.join(PAGES_INSIDE, f))

files_to_update = list(html_files)
build_script = os.path.join(ROOT_DIR, "scripts", "build_all_21_modern_subpages.py")
if os.path.exists(build_script):
    files_to_update.append(build_script)

cleaned_count = 0

for fpath in files_to_update:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"[ \t]*<!--[^\n]*with your actual Google Tag Manager Container ID[^\n]*-->\r?\n?",
        "",
        content
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        cleaned_count += 1

print(f"Cleaned comments in {cleaned_count} files.")
