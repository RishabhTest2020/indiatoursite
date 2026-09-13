import json

with open('scratch/bulk_generate_slices.json', 'r', encoding='utf-8') as f:
    slices = json.load(f)

for idx, content in slices:
    lines = content.splitlines()
    first_line = lines[0] if lines else ""
    last_line = lines[-1] if lines else ""
    print(f"Slice from line {idx}: {len(lines)} lines. First: {first_line[:80]} | Last: {last_line[:80]}")
