import json
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

clips = json.load(open('workspace_clips_raw.json', encoding='utf-8'))
for c in clips:
    meta = c.get('metadata', {})
    for k, v in meta.items():
        if isinstance(v, (list, dict)) and k not in ['image_config', 'model_badges']:
            print(f"Clip {c.get('id')} meta key '{k}': {str(v)[:200]}")
    if c.get('action_config'):
        print(f"Clip {c.get('id')} action_config: {str(c.get('action_config'))[:200]}")
    break
