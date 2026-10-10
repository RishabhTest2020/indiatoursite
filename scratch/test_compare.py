import os
import sys

sys.path.append(os.path.abspath('.'))
from scripts.build_all_21_modern_subpages import DESTINATIONS_DATA, TEMPLATE

with open('Pages-inside/Jaipur-Info.html', 'r', encoding='utf-8') as f:
    current = f.read()

dest = [d for d in DESTINATIONS_DATA if d['filename'] == 'Jaipur-Info.html'][0]
hl_html = ''
for hl in dest['highlights']:
    hl_html += f'<div class="highlight-item"><i class="fa fa-check-circle"></i> {hl}</div>\n'

generated = TEMPLATE.format(
    page_title=dest['page_title'],
    hero_desc=dest['hero_desc'],
    img_hero=dest['img_hero'],
    badge_text=dest['badge_text'],
    hero_title=dest['hero_title'],
    duration=dest['duration'],
    best_time=dest['best_time'],
    budget=dest['budget'],
    ideal_for=dest['ideal_for'],
    overview_text=dest['overview_text'],
    day1_title=dest['day1_title'],
    day1_desc=dest['day1_desc'],
    day2_title=dest['day2_title'],
    day2_desc=dest['day2_desc'],
    highlights_html=hl_html,
    air_logistics=dest['air_logistics'],
    train_logistics=dest['train_logistics'],
    road_logistics=dest['road_logistics'],
    img_gal1=dest['img_gal1'],
    img_gal2=dest['img_gal2'],
    img_gal3=dest['img_gal3'],
    cap1=dest['cap1'],
    cap2=dest['cap2'],
    cap3=dest['cap3']
)

print('Exact match?', current == generated)
if current != generated:
    print('Current length:', len(current), 'Generated length:', len(generated))
    import difflib
    diff = list(difflib.unified_diff(current.splitlines(), generated.splitlines(), lineterm=''))
    print('Diff lines:', len(diff))
    for line in diff[:20]:
        print(line)
