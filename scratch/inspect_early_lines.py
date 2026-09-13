import json

transcript_path = r'C:\Users\Hp\.gemini\antigravity-ide\brain\b6a24b34-d684-47b0-b690-16419b294e21\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in [188, 189, 190, 225, 226, 231, 232, 348, 349]:
            obj = json.loads(line)
            print(f"\n================ LINE {idx} (step {obj.get('step_index')}) ================")
            print("Type:", obj.get('type'), "Source:", obj.get('source'))
            content = obj.get('content', '')
            if content:
                print("Content len:", len(content))
                # print snippet
                idx_match = content.find('Nature Lovers')
                if idx_match != -1:
                    print(content[max(0, idx_match-300):min(len(content), idx_match+400)])
            tc = obj.get('tool_calls', [])
            if tc:
                print("Tool calls:", len(tc))
                for c in tc:
                    print("  Tool:", c.get('name'))
                    args = c.get('args', {})
                    if 'TargetFile' in args:
                        print("  TargetFile:", args['TargetFile'])
                        with open(f'scratch/script_{idx}.py', 'w', encoding='utf-8') as out_f:
                            out_f.write(args.get('CodeContent', ''))
                        print(f"  Wrote code content to scratch/script_{idx}.py!")
