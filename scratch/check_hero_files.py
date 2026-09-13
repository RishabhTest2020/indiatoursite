import os

images = [
    'alleppey_hero.jpg', 'bikaner_hero.jpg', 'camelsafari_hero.jpg', 'colvabeach_hero.jpg',
    'golden_temple_hero.png', 'goldentemple_hero.jpg', 'gwaliorfort_hero.jpg', 'hampi_hero.jpg',
    'himachal_hero.jpg', 'jaipur_hero.jpg', 'jaisalmer_hero.jpg', 'jodhpur_hero.jpg',
    'kashmir_hero.jpg', 'mehrangarhfort_hero.jpg', 'mon_hero.jpg', 'pushkar_hero.jpg',
    'sanchistupa_hero.jpg', 'twang_hero.jpg', 'udaipur_hero.jpg', 'umngotriver_hero.jpg',
    'uttrakhand_hero.jpg', 'vivekanandarock_hero.jpg'
]

for img in images:
    path = os.path.join('img', img)
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"EXISTS: {img:30s} ({size:,} bytes)")
    else:
        print(f"MISSING: {img}")
