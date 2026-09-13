import json

transcript_path = r'C:\Users\Hp\PycharmProjects\indiatoursite\.system_generated\logs\transcript_full.jsonl'
if not os.path.exists(transcript_path):
    transcript_path = r'C:\Users\Hp\.gemini\antigravity-ide\brain\b6a24b34-d684-47b0-b690-16419b294e21\.system_generated\logs\transcript_full.jsonl'

slices = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in [100, 101, 104, 186, 188, 190, 345, 347, 349, 351]:
            obj = json.loads(line)
            content = obj.get('content', '')
            slices.append((idx, content))

print(f"Got {len(slices)} slices")
with open('scratch/bulk_generate_slices.json', 'w', encoding='utf-8') as out:
    json.dump(slices, out, indent=2, ensure_ascii=False)
print("Saved to scratch/bulk_generate_slices.json!")
