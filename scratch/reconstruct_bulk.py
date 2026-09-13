import json
import re

with open('scratch/bulk_generate_slices.json', 'r', encoding='utf-8') as f:
    slices = json.load(f)

full_lines = {}
# Regex to match line format: 123: original line
line_pattern = re.compile(r'^\s*(\d+):\s(.*)$')

for idx, content in slices:
    for line in content.splitlines():
        m = line_pattern.match(line)
        if m:
            num = int(m.group(1))
            val = m.group(2)
            full_lines[num] = val

sorted_nums = sorted(full_lines.keys())
print(f"Total reconstructed lines: {len(sorted_nums)}, min={min(sorted_nums)}, max={max(sorted_nums)}")

# Check for gaps
missing = [n for n in range(min(sorted_nums), max(sorted_nums)+1) if n not in full_lines]
print(f"Missing lines: {missing}")

reconstructed = [full_lines[n] for n in sorted_nums]
with open('scratch/bulk_generate_reconstructed.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(reconstructed))
print("Saved to scratch/bulk_generate_reconstructed.py!")
