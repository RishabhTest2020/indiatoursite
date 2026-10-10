import json
import os
import sys

sys.path.append(os.path.abspath('.'))
from scripts.build_all_21_modern_subpages import DESTINATIONS_DATA

output = []
for i, d in enumerate(DESTINATIONS_DATA):
    output.append({
        "index": i + 1,
        "filename": d["filename"],
        "hero_title": d["hero_title"],
        "duration": d["duration"],
        "badge_text": d["badge_text"],
        "hero_desc": d["hero_desc"],
        "img_hero": d["img_hero"],
        "budget": d.get("budget", ""),
        "ideal_for": d.get("ideal_for", ""),
        "overview_text": d.get("overview_text", ""),
        "day1_title": d.get("day1_title", ""),
        "day2_title": d.get("day2_title", ""),
        "highlights": d.get("highlights", [])
    })

with open('scratch/dest_info.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Dumped {len(output)} destinations to scratch/dest_info.json")
