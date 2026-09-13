import os
import json

transcript_path = r'C:\Users\Hp\.gemini\antigravity-ide\brain\b6a24b34-d684-47b0-b690-16419b294e21\.system_generated\logs\transcript.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 190:
            obj = json.loads(line)
            with open('scratch/step_190.json', 'w', encoding='utf-8') as out:
                json.dump(obj, out, indent=2, ensure_ascii=False)
            print(f"Dumped step 190: keys={list(obj.keys())}")
            if 'tool_calls' in obj:
                for tc in obj['tool_calls']:
                    print("Tool call name:", tc.get('name'))
                    fn = tc.get('function', {})
                    print("Function name:", fn.get('name'))
                    args = fn.get('arguments', {})
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except:
                            pass
                    if isinstance(args, dict):
                        for k in args.keys():
                            print("  arg:", k)
