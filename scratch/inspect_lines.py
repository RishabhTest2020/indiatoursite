import json

transcript_path = r'C:\Users\Hp\.gemini\antigravity-ide\brain\b6a24b34-d684-47b0-b690-16419b294e21\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in [1033, 1035, 1041]:
            obj = json.loads(line)
            print(f"\n--- LINE {idx} ---")
            tc = obj.get('tool_calls', [])
            for c in tc:
                print("Tool name:", c.get('name'))
                print("Args keys:", list(c.get('args', {}).keys()))
                if 'CommandLine' in c.get('args', {}):
                    print("CommandLine:", c['args']['CommandLine'][:200])
                if 'TargetFile' in c.get('args', {}):
                    print("TargetFile:", c['args']['TargetFile'])
                    with open(f'scratch/call_{idx}.json', 'w', encoding='utf-8') as out:
                        json.dump(c, out, indent=2, ensure_ascii=False)
