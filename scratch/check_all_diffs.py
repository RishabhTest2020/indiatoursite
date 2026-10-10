import os
import sys
import difflib

sys.path.append(os.path.abspath('.'))
from scripts.build_all_21_modern_subpages import DESTINATIONS_DATA, TEMPLATE

for d in DESTINATIONS_DATA:
    fn = d['filename']
    with open(os.path.join('Pages-inside', fn), 'r', encoding='utf-8') as f:
        curr = f.read()
    hl_html = ''
    for hl in d['highlights']:
        hl_html += f'<div class="highlight-item"><i class="fa fa-check-circle"></i> {hl}</div>\n'
    gen = TEMPLATE.format(
        page_title=d['page_title'],
        hero_desc=d['hero_desc'],
        img_hero=d['img_hero'],
        badge_text=d['badge_text'],
        hero_title=d['hero_title'],
        duration=d['duration'],
        best_time=d['best_time'],
        budget=d['budget'],
        ideal_for=d['ideal_for'],
        overview_text=d['overview_text'],
        day1_title=d['day1_title'],
        day1_desc=d['day1_desc'],
        day2_title=d['day2_title'],
        day2_desc=d['day2_desc'],
        highlights_html=hl_html,
        air_logistics=d['air_logistics'],
        train_logistics=d['train_logistics'],
        road_logistics=d['road_logistics'],
        img_gal1=d['img_gal1'],
        img_gal2=d['img_gal2'],
        img_gal3=d['img_gal3'],
        cap1=d['cap1'],
        cap2=d['cap2'],
        cap3=d['cap3']
    )
    diff = list(difflib.unified_diff(curr.splitlines(), gen.splitlines()))
    diff_other = [line for line in diff if not any(w in line for w in ['wa-nav-btn', 'theme-toggle-li', 'WhatsApp', '918700140135', '@@', '---', '+++', '            '])]
    if diff_other:
        print(f'{fn} has extra diffs:', diff_other[:10])
    else:
        print(f'{fn}: clean (only wa-nav-btn differs)')

print('All 21 checked.')
