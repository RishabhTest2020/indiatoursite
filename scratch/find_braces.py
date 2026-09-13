with open('scripts/build_all_21_modern_subpages.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_template = False
for num, line in enumerate(lines, 1):
    if 'TEMPLATE = """' in line:
        in_template = True
        continue
    if in_template and '"""' in line:
        in_template = False
        break
    if in_template:
        # replace {{ and }}
        s = line.replace('{{', '').replace('}}', '')
        # Check if there are braces that are not valid placeholders
        for part in s.split('{')[1:]:
            if '}' in part:
                field = part.split('}')[0]
                valid_fields = [
                    'page_title', 'hero_desc', 'img_hero', 'badge_text', 'hero_title',
                    'duration', 'best_time', 'budget', 'ideal_for', 'overview_text',
                    'day1_title', 'day1_desc', 'day2_title', 'day2_desc', 'highlights_html',
                    'air_logistics', 'train_logistics', 'road_logistics', 'img_gal1',
                    'img_gal2', 'img_gal3', 'cap1', 'cap2', 'cap3'
                ]
                if field not in valid_fields:
                    print(f"Line {num}: unknown field '{field}' -> {line.strip()}")
            else:
                print(f"Line {num}: unclosed brace -> {line.strip()}")
        if '}' in s and '{' not in s:
            print(f"Line {num}: stray closing brace -> {line.strip()}")
