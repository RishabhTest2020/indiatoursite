import os
import re
from html.parser import HTMLParser

ROOT_DIR = r"c:\Users\Hp\PycharmProjects\indiatoursite"
PAGES_INSIDE = os.path.join(ROOT_DIR, "Pages-inside")

html_files = [os.path.join(ROOT_DIR, "index.html")]
for f in sorted(os.listdir(PAGES_INSIDE)):
    if f.endswith(".html"):
        html_files.append(os.path.join(PAGES_INSIDE, f))

print(f"Total HTML files to verify: {len(html_files)}")

issues = []

class PageAuditor(HTMLParser):
    def __init__(self, filepath, rel_path):
        super().__init__()
        self.filepath = filepath
        self.rel_path = rel_path
        self.in_title = False
        self.title_text = ""
        self.meta_desc = None
        self.canonical = None
        self.og_props = {}
        self.has_json_ld = False
        self.images = []
        self.assets = []
        self.json_ld_contents = []
        self.in_json_ld = False

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            if attr_dict.get("name") == "description":
                self.meta_desc = attr_dict.get("content")
            if "property" in attr_dict and attr_dict["property"].startswith("og:"):
                self.og_props[attr_dict["property"]] = attr_dict.get("content")
        elif tag == "link":
            if attr_dict.get("rel") == "canonical":
                self.canonical = attr_dict.get("href")
            href = attr_dict.get("href")
            if href:
                self.assets.append(("link", "href", href))
        elif tag == "script":
            if attr_dict.get("type") == "application/ld+json":
                self.has_json_ld = True
                self.in_json_ld = True
            src = attr_dict.get("src")
            if src:
                self.assets.append(("script", "src", src))
        elif tag == "img":
            self.images.append(attr_dict)
            src = attr_dict.get("src")
            if src:
                self.assets.append(("img", "src", src))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_json_ld:
            self.in_json_ld = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data
        if self.in_json_ld:
            self.json_ld_contents.append(data)

for filepath in html_files:
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    is_subpage = "Pages-inside" in rel_path
    is_dest_subpage = is_subpage and "-Info.html" in rel_path
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. GTM Head
    gtm_head_present = "googletagmanager.com/gtm.js" in content and "GTM-NR4N55ZR" in content
    if not gtm_head_present:
        issues.append(f"[{rel_path}] GTM head snippet missing or does not have GTM-NR4N55ZR")

    # 2. GTM Noscript
    gtm_noscript_present = "googletagmanager.com/ns.html?id=GTM-NR4N55ZR" in content and "<noscript>" in content
    if not gtm_noscript_present:
        issues.append(f"[{rel_path}] GTM noscript snippet missing or does not have GTM-NR4N55ZR")

    # Parse with PageAuditor
    auditor = PageAuditor(filepath, rel_path)
    auditor.feed(content)

    # 3. Title
    if not auditor.title_text.strip():
        issues.append(f"[{rel_path}] Missing or empty <title>")

    # 4. Meta Description
    if not auditor.meta_desc:
        issues.append(f"[{rel_path}] Missing <meta name='description'>")
    else:
        desc_len = len(auditor.meta_desc.strip())
        if is_dest_subpage and not (130 <= desc_len <= 155):
            issues.append(f"[{rel_path}] Destination meta description length ({desc_len}) not in 130-155: '{auditor.meta_desc.strip()}'")

    # 5. Canonical
    if not auditor.canonical:
        issues.append(f"[{rel_path}] Missing canonical link")
    elif not auditor.canonical.startswith("https://cityinfoindiatravels.com/"):
        issues.append(f"[{rel_path}] Invalid canonical URL: {auditor.canonical}")

    # 6. Open Graph
    for og in ["og:title", "og:description", "og:type", "og:url", "og:image"]:
        if og not in auditor.og_props or not auditor.og_props[og]:
            issues.append(f"[{rel_path}] Missing {og}")

    # 7. JSON-LD for destination subpages
    if is_dest_subpage:
        if not auditor.has_json_ld:
            issues.append(f"[{rel_path}] Missing JSON-LD")
        else:
            ld_str = " ".join(auditor.json_ld_contents)
            if "TouristTrip" not in ld_str and "TouristDestination" not in ld_str:
                issues.append(f"[{rel_path}] JSON-LD missing TouristTrip/TouristDestination")
            if "8700140135" not in ld_str:
                issues.append(f"[{rel_path}] JSON-LD missing provider phone 8700140135")

    # 8. Images have alt
    for img in auditor.images:
        alt = img.get("alt")
        if alt is None or alt.strip() == "":
            issues.append(f"[{rel_path}] Image missing alt attribute: {img.get('src')}")

    # 9. Local Asset Existence Check
    for tag_name, attr_name, val in auditor.assets:
        if not val.startswith(("http://", "https://", "#", "mailto:", "tel:", "data:", "javascript:")):
            clean_val = val.split("?")[0].split("#")[0]
            if clean_val:
                asset_full = os.path.normpath(os.path.join(os.path.dirname(filepath), clean_val))
                if not os.path.exists(asset_full):
                    issues.append(f"[{rel_path}] Broken local asset {attr_name} in <{tag_name}>: '{val}' -> {asset_full}")

if not issues:
    print("SUCCESS! All 26 HTML files passed all SEO, GTM, JSON-LD, metadata, alt tags, and asset checks!")
else:
    print(f"FOUND {len(issues)} ISSUES:")
    for iss in issues[:40]:
        print(" - " + iss)
