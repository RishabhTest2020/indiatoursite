import os
import json

transcript_path = r'C:\Users\Hp\.gemini\antigravity-ide\brain\b6a24b34-d684-47b0-b690-16419b294e21\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'Nature Lovers' in line:
            obj = json.loads(line)
            step_idx = obj.get('step_index')
            source = obj.get('source')
            tool_calls = obj.get('tool_calls', [])
            print(f"Match at line {i}, step_index {step_idx}, source {source}, tool_calls: {len(tool_calls)}")
            if tool_calls:
                for tc in tool_calls:
                    fn = tc.get('function', {})
                    fname = fn.get('name')
                    print(f"  Tool: {fname}")
                    args = fn.get('arguments', {})
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except:
                            pass
                    if isinstance(args, dict):
                        target = args.get('TargetFile') or args.get('CommandLine') or ''
                        print(f"  Target: {target}")
                        if 'TargetFile' in args:
                            with open('scratch/found_template_call.json', 'w', encoding='utf-8') as out:
                                json.dump(args, out, indent=2, ensure_ascii=False)
                            print("Dumped target file call to scratch/found_template_call.json!")
