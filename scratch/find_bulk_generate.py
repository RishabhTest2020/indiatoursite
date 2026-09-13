import json

transcript_path = r'C:\Users\Hp\.gemini\antigravity-ide\brain\b6a24b34-d684-47b0-b690-16419b294e21\.system_generated\logs\transcript_full.jsonl'

matches = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if 'bulk_generate.py' in line:
            obj = json.loads(line)
            matches.append((idx, obj.get('step_index'), obj.get('type'), obj.get('source')))

print(f"Total matches: {len(matches)}")
for m in matches:
    print(m)
