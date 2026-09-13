import json
import re

transcript_path = r'C:\Users\Hp\.gemini\antigravity-ide\brain\b6a24b34-d684-47b0-b690-16419b294e21\.system_generated\logs\transcript_full.jsonl'

dest_keys = ['GoldenTemple-Info.html', 'Bikaner-Info.html', 'GwaliorFort-Info.html', 'UmngotRiver-Info.html']

matches = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        for k in dest_keys:
            if k in line and 'duration' in line:
                matches.append((idx, k))
                break

print("Found matches with duration & destination:", len(matches))
for m in matches[:10]:
    print(m)
