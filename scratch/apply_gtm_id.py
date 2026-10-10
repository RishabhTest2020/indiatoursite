import os
import re

ROOT_DIR = r"c:\Users\Hp\PycharmProjects\indiatoursite"
PAGES_INSIDE = os.path.join(ROOT_DIR, "Pages-inside")

html_files = [os.path.join(ROOT_DIR, "index.html")]
for f in sorted(os.listdir(PAGES_INSIDE)):
    if f.endswith(".html"):
        html_files.append(os.path.join(PAGES_INSIDE, f))

# Also include the build script
files_to_update = list(html_files)
build_script = os.path.join(ROOT_DIR, "scripts", "build_all_21_modern_subpages.py")
if os.path.exists(build_script):
    files_to_update.append(build_script)

updated_count = 0

for fpath in files_to_update:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace GTM-XXXXXXX with GTM-NR4N55ZR
    new_content = content.replace("GTM-XXXXXXX", "GTM-NR4N55ZR")
    # Also clean up the comment "<!-- Replace GTM-XXXXXXX with your actual Google Tag Manager Container ID -->\n" if desired or keep clean comment
    # Let's clean up any "Replace GTM-XXXXXXX with your actual Google Tag Manager Container ID" line
    new_content = re.sub(
        r"[ \t]*<!-- Replace GTM-XXXXXXX with your actual Google Tag Manager Container ID -->\r?\n?",
        "",
        new_content
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated: {os.path.relpath(fpath, ROOT_DIR)}")

print(f"\nTotal files updated with GTM-NR4N55ZR: {updated_count}")
