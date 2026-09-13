import glob
import os
import re

for f in sorted(glob.glob('Pages-inside/*-Info.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    banner = re.findall(r'\.banner-area\s*\{[^}]*background-image:\s*url\([\'"]?([^\'")]+)[\'"]?\)', c)
    gallery = re.findall(r'<div class=["\']row gallery["\']>([\s\S]*?)</div>', c)
    imgs = re.findall(r'<img\s+src=["\']([^"\']+)["\']', gallery[0]) if gallery else []
    print(f"{os.path.basename(f)}:")
    print(f"  Banner: {banner[0] if banner else None}")
    print(f"  Gallery ({len(imgs)}): {imgs}")
