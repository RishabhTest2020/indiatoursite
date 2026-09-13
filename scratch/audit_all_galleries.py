import os
import glob
import re

files = sorted(glob.glob('Pages-inside/*-Info.html'))
print(f"Total destination pages found: {len(files)}")
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    hero_match = re.search(r'class="subpage-hero"[^>]*background-image:\s*url\([\'"]?([^\'")]+)[\'"]?\)', c)
    hero = hero_match.group(1) if hero_match else 'None'
    items = re.findall(r'<div class="inside-gallery-item">[\s\S]*?<img\s+src="([^"]+)"[\s\S]*?<span class="inside-gallery-title">([^<]+)</span>', c)
    print(f"\n=== {os.path.basename(f)} ===")
    print(f"  Hero: {hero}")
    for idx, (img_src, title) in enumerate(items):
        print(f"  Gallery {idx+1} [{title}]: {img_src}")
