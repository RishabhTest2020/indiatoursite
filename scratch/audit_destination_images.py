import os
import glob
import re

all_good = True

for f in sorted(glob.glob('Pages-inside/*-Info.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # banner
    banner_match = re.search(r'\.banner-area\s*\{[^}]*background-image:\s*url\([\'"]?([^\'")]+)[\'"]?\)', c)
    banner = banner_match.group(1) if banner_match else None
    
    # gallery
    gal_imgs = re.findall(r'<div class="row gallery[\s\S]*?</div>\s*</div>', c)
    extracted_imgs = []
    if gal_imgs:
        extracted_imgs = re.findall(r'<img\s+src="([^"]+)"', gal_imgs[0])
    
    all_imgs = [banner] + extracted_imgs if banner else extracted_imgs
    
    disk_checks = []
    for img_path in all_imgs:
        clean_path = img_path.replace('../', '')
        exists = os.path.exists(clean_path)
        size = os.path.getsize(clean_path) if exists else 0
        disk_checks.append((clean_path, exists, size))
    
    is_distinct = (len(set(all_imgs)) == 4) and (len(all_imgs) == 4)
    all_exist = all(item[1] and item[2] > 10000 for item in disk_checks)
    
    status = "PASS" if (is_distinct and all_exist) else "FAIL"
    if status == "FAIL":
        all_good = False
    print(f"[{status}] {os.path.basename(f)}: distinct={is_distinct}, all_exist={all_exist}, imgs={all_imgs}")

print("\n====================================")
print(f"ALL 21 DESTINATIONS AUDIT: {'PASSED' if all_good else 'FAILED'}")
print("====================================")
