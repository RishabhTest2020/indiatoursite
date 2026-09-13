import os

other_imgs = [
    'mountain.jpg', 'service-bg.jpg', 's1.png', 's2.png', 's3.png', 'logoex.jpg',
    'fav.png', 'explore-india-logo.svg'
]

for img in other_imgs:
    path = os.path.join('img', img)
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"EXISTS: {img:25s} ({size:,} bytes)")
    else:
        print(f"MISSING: {img}")
