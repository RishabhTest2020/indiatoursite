import os
import re

for f in sorted(os.listdir('img')):
    if f.endswith(('.jpg', '.png')) and not f.startswith(('s1', 's2', 's3', 'p', 'b', 'd', 'r', 'l', 'm', 'fav')):
        path = os.path.join('img', f)
        size = os.path.getsize(path)
        # Try to find text strings in binary (e.g., File: or description or camera model)
        with open(path, 'rb') as fp:
            data = fp.read(4096)
        # Search for interesting strings
        strings = re.findall(b'[\x20-\x7e]{6,}', data)
        desc = [s.decode('latin1', errors='ignore') for s in strings if any(k in s.lower() for k in [b'file:', b'http', b'canon', b'nikon', b'sony', b'commons', b'adobe', b'wikimedia'])]
        print(f"{f:26s} ({size//1024:4d} KB) | Meta: {desc[:2]}")
