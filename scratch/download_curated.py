import urllib.request
import urllib.parse
import json
import time
import os

HEADERS = {
    'User-Agent': 'IndiaToursTravelSite/1.0 (https://indiatoursite.local; info@indiatoursite.com)',
    'Referer': 'https://commons.wikimedia.org/'
}

IMG_DIR = r"c:\Users\Hp\PycharmProjects\indiatoursite\img"

def get_image_info(title):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url|size|mime&format=json'
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for pid, page in pages.items():
            info = page.get('imageinfo', [{}])[0]
            return info.get('url'), info.get('width'), info.get('height')
    return None, None, None

def download_file(url, out_path):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp, open(out_path, 'wb') as out_f:
        out_f.write(resp.read())
    print(f"Downloaded: {out_path} ({os.path.getsize(out_path):,} bytes)")

DOWNLOADS = [
    ("File:Taj Mahal, Agra, India edit2.jpg", "india_hero_banner.jpg"),
    ("File:Jaipur 03-2016 02 Amber Fort.jpg", "jaipur_hero.jpg"),
    ("File:City Palace Jaipur - Peacock Gate of Pitam Niwas Chowk.jpg", "jaipur_gal2.jpg"),
    ("File:Jal Mahal at the sunset.jpg", "jaipur_gal3.jpg"),
]

for title, filename in DOWNLOADS:
    url, w, h = get_image_info(title)
    print(f"{title} -> {w}x{h} : {url}")
    if url:
        out_path = os.path.join(IMG_DIR, filename)
        download_file(url, out_path)
        time.sleep(1.0)
