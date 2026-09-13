import glob
import os
import re

all_clean = True
for f in sorted(glob.glob('Pages-inside/*-Info.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    header_count = c.count('<header class="default-header">')
    footer_count = c.count('<footer class="footer-area section-gap">')
    modal_count = c.count('<div id="queryModal">')
    chat_count = c.count('<div class="chat-widget-container">')
    gal_imgs = re.findall(r'<div class="row gallery[\s\S]*?</div>\s*<div class="text-center', c)
    img_tags = re.findall(r'<img\s+src="([^"]+)"', gal_imgs[0]) if gal_imgs else []
    
    is_ok = (header_count == 1 and footer_count == 1 and modal_count == 1 and chat_count == 1 and len(img_tags) == 3)
    if not is_ok:
        all_clean = False
        print(f"ANOMALY in {os.path.basename(f)}: header={header_count}, footer={footer_count}, modal={modal_count}, chat={chat_count}, gallery_imgs={len(img_tags)}")
    else:
        print(f"CLEAN: {os.path.basename(f)}: 3 gallery images, 1 header, 1 footer, 1 modal, 1 chat widget.")

print(f"\nALL PAGES 100% CLEAN: {all_clean}")
