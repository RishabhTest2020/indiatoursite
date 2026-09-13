import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

items = re.findall(r'<div class="single-portfolio[^>]*>.*?</div>\s*</div>\s*</div>', content, re.DOTALL)
print(f"Total cards: {len(items)}")

for idx, itm in enumerate(items):
    title_m = re.search(r'<h4><a[^>]*>([^<]+)</a></h4>', itm)
    src_m = re.search(r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"', itm)
    state_m = re.search(r'<span class="state-badge">([^<]+)</span>', itm)
    link_m = re.search(r'<a href="([^"]+)"', itm)
    
    title = title_m.group(1) if title_m else "N/A"
    src = src_m.group(1) if src_m else "N/A"
    alt = src_m.group(2) if src_m else "N/A"
    state = state_m.group(1) if state_m else "N/A"
    link = link_m.group(1) if link_m else "N/A"
    print(f"Card {idx+1:2d}: {title:28s} | State: {state:18s} | Current img: {src:15s} | Link: {link}")
