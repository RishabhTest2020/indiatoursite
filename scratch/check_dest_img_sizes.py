import os
import struct

DEST_IMG_MAP = {
    "Golden Temple": "img/golden_temple_hero.png",
    "Gwalior Fort": "img/gwaliorfort_hero.jpg",
    "Twang": "img/twang_hero.jpg",
    "Alleppey": "img/alleppey_hero.jpg",
    "Camel Safari": "img/camelsafari_hero.jpg",
    "Sanchi Stupa": "img/sanchistupa_hero.jpg",
    "Umngot river": "img/umngotriver_hero.jpg",
    "Vivekananda Rock Memorial": "img/vivekanandarock_hero.jpg",
    "Mehrangarh Fort": "img/mehrangarhfort_hero.jpg",
    "Hampi": "img/hampi_hero.jpg",
    "Mon": "img/mon_hero.jpg",
    "Colva Beach": "img/colvabeach_hero.jpg",
    "Jaipur": "img/jaipur_hero.jpg",
    "Udaipur": "img/udaipur_hero.jpg",
    "Pushkar": "img/pushkar_hero.jpg",
    "Jaisalmer": "img/jaisalmer_hero.jpg",
    "Jodhpur": "img/jodhpur_hero.jpg",
    "Bikaner": "img/bikaner_hero.jpg",
    "Kashmir": "img/kashmir_hero.jpg",
    "Himachal": "img/himachal_hero.jpg",
    "Uttrakhand": "img/uttrakhand_hero.jpg"
}

def get_image_size(file_path):
    """Get image dimensions without external libraries."""
    with open(file_path, 'rb') as f:
        data = f.read(32)
        if data.startswith(b'\x89PNG\r\n\x1a\n'):
            w, h = struct.unpack('>LL', data[16:24])
            return w, h
        f.seek(0)
        data = f.read(2)
        if data.startswith(b'\xff\xd8'):
            f.seek(0)
            size = os.path.getsize(file_path)
            # Simple JPEG dimension parser
            f.seek(2)
            while True:
                b = f.read(1)
                if not b:
                    break
                if b != b'\xff':
                    continue
                marker = f.read(1)
                while marker == b'\xff':
                    marker = f.read(1)
                if marker in [b'\xc0', b'\xc1', b'\xc2', b'\xc3']:
                    f.read(3)
                    h, w = struct.unpack('>HH', f.read(4))
                    return w, h
                elif marker in [b'\xd9', b'\xda']:
                    break
                else:
                    len_bytes = f.read(2)
                    if len(len_bytes) < 2:
                        break
                    length = struct.unpack('>H', len_bytes)[0]
                    f.seek(length - 2, 1)
    return None, None

for dest, img_path in DEST_IMG_MAP.items():
    if os.path.exists(img_path):
        w, h = get_image_size(img_path)
        size_kb = os.path.getsize(img_path) // 1024
        print(f"{dest:28s} -> {img_path:28s} ({w}x{h}, {size_kb} KB)")
    else:
        print(f"MISSING: {dest:28s} -> {img_path}")
