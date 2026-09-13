import os
import re

PAGES_DIR = r'c:\Users\Hp\PycharmProjects\indiatoursite\Pages-inside'

# List of all 21 destination pages
DESTINATION_FILES = [f for f in os.listdir(PAGES_DIR) if f.endswith('-Info.html')]
print(f"Found {len(DESTINATION_FILES)} destination info pages.")

updated_count = 0

for filename in sorted(DESTINATION_FILES):
    filepath = os.path.join(PAGES_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Nav bar WhatsApp button
    if 'wa-nav-btn' not in content:
        nav_pattern = r'(<li class="nav-item theme-toggle-li">)'
        nav_replacement = """                        <li class="nav-item">
                            <a class="wa-nav-btn wa-dynamic-btn" href="https://wa.me/918700140135" target="_blank" rel="noopener noreferrer"><i class="fa fa-whatsapp"></i> WhatsApp</a>
                        </li>
\\1"""
        new_content = re.sub(nav_pattern, nav_replacement, content, count=1)
        if new_content != content:
            content = new_content
            modified = True

    # 2. Hero WhatsApp button
    if 'wa-hero-btn' not in content:
        hero_btn_pattern = r'(<button class="primary-btn openQueryModal"[^>]*>.*?</button>)'
        hero_btn_replacement = """\\1
            <a href="https://wa.me/918700140135" class="wa-hero-btn wa-dynamic-btn" target="_blank" rel="noopener noreferrer"><i class="fa fa-whatsapp"></i> WhatsApp Us</a>"""
        new_content = re.sub(hero_btn_pattern, hero_btn_replacement, content, count=1)
        if new_content != content:
            content = new_content
            modified = True

    # 3. Sidebar WhatsApp CTA button
    if 'whatsapp-btn' not in content:
        sidebar_pattern = r'(<div class="inside-card text-center sticky-top"[^>]*>[\s\S]*?<p[^>]*>.*?</p>)'
        sidebar_replacement = """\\1
                        <a href="https://wa.me/918700140135" class="whatsapp-btn w-100 mb-3 wa-dynamic-btn" target="_blank" rel="noopener noreferrer"><i class="fa fa-whatsapp"></i> Chat on WhatsApp &bull; Instant Quote</a>"""
        new_content = re.sub(sidebar_pattern, sidebar_replacement, content, count=1)
        if new_content != content:
            content = new_content
            modified = True

    # 4. Footer WhatsApp link
    if 'fa-whatsapp' not in content:
        footer_pattern = r'(<p><i class="fa fa-phone"[^>]*></i>\s*\+?91\s*87001\s*40135</p>)'
        footer_replacement = """\\1
                        <p><i class="fa fa-whatsapp" style="color:var(--wa-green, #25D366); margin-right:8px;"></i> <a href="https://wa.me/918700140135" class="wa-dynamic-btn" target="_blank" rel="noopener noreferrer" style="color:inherit; font-weight:600;">+91 87001 40135 (WhatsApp)</a></p>"""
        new_content = re.sub(footer_pattern, footer_replacement, content, count=1)
        if new_content != content:
            content = new_content
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"Updated: {filename}")
    else:
        print(f"Already updated or pattern mismatch: {filename}")

print(f"\nTotal subpages updated: {updated_count}/{len(DESTINATION_FILES)}")
