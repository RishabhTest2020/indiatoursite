import os

ROOT_DIR = r"c:\Users\Hp\PycharmProjects\indiatoursite"
PAGES_INSIDE = os.path.join(ROOT_DIR, "Pages-inside")

html_files = [os.path.join(ROOT_DIR, "index.html")]
for f in sorted(os.listdir(PAGES_INSIDE)):
    if f.endswith(".html"):
        html_files.append(os.path.join(PAGES_INSIDE, f))

print(f"Total HTML files to verify for GA4: {len(html_files)}")

issues = []

for filepath in html_files:
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. GA4 snippet check
    if "googletagmanager.com/gtag/js?id=G-QWM7WPBCMF" not in content:
        issues.append(f"[{rel_path}] Missing gtag.js src for G-QWM7WPBCMF")
    if "gtag('config', 'G-QWM7WPBCMF')" not in content:
        issues.append(f"[{rel_path}] Missing gtag('config', 'G-QWM7WPBCMF')")

    # 2. Check position: should be inside <head> before other scripts
    head_start = content.find("<head")
    head_end = content.find("</head>")
    if head_start == -1 or head_end == -1:
        issues.append(f"[{rel_path}] Malformed head tag")
    else:
        head_content = content[head_start:head_end]
        gtag_pos = head_content.find("gtag/js?id=G-QWM7WPBCMF")
        gtm_pos = head_content.find("gtm.js?id=GTM-NR4N55ZR")
        if gtag_pos == -1:
            issues.append(f"[{rel_path}] gtag script not in <head>")
        elif gtm_pos != -1 and gtag_pos > gtm_pos:
            issues.append(f"[{rel_path}] gtag script is AFTER GTM script in <head>")

    # 3. Check for leftover GTM-XXXXXXX
    if "GTM-XXXXXXX" in content:
        issues.append(f"[{rel_path}] Unconfigured placeholder GTM-XXXXXXX still present")

if not issues:
    print("SUCCESS: All 26 HTML files have the GA4 (G-QWM7WPBCMF) snippet correctly positioned in <head>!")
else:
    print(f"FOUND {len(issues)} ISSUES:")
    for iss in issues:
        print(" - " + iss)
