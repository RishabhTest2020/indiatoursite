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

REMAINING_TASKS = [
    {
        "filename": "alleppey_gal1.jpg",
        "queries": ["Houseboat in Kerala Backwaters", "Kettuvallam interior", "Alappuzha houseboat deck", "Kerala houseboat bedroom", "Houseboat cruise Kerala"]
    },
    {
        "filename": "alleppey_gal2.jpg",
        "queries": ["Canals of Alappuzha", "Alappuzha canal canoe", "Kerala backwater narrow canal", "Alleppey backwaters village", "Backwaters of Kerala canoe"]
    },
    {
        "filename": "alleppey_gal3.jpg",
        "queries": ["Vembanad Lake", "Sunset at Vembanad Lake", "Nehru Trophy Boat Race Alappuzha", "Snake boat race Kerala", "Vembanad Lake Alappuzha"]
    },
    {
        "filename": "hampi_gal1.jpg",
        "queries": ["Virupaksha temple complex Hampi", "Hampi Virupaksha courtyard", "Virupaksha sanctum", "Virupaksha Temple inner"]
    },
    {
        "filename": "hampi_gal2.jpg",
        "queries": ["Stone Chariot Vittala Temple Hampi", "Vittala Temple Stone Chariot", "Stone chariot Hampi", "Stone Chariot, Hampi"]
    },
    {
        "filename": "hampi_gal3.jpg",
        "queries": ["Hemakuta Hill temples Hampi", "Sunset at Hemakuta Hill", "Hampi landscape boulders sunset", "Matanga Hill Hampi", "Hemakuta hill"]
    },
    {
        "filename": "himachal_gal1.jpg",
        "queries": ["Christ Church Shimla Ridge", "The Ridge Shimla evening", "Shimla Ridge Christ Church neo-gothic", "Christ Church Shimla"]
    },
    {
        "filename": "himachal_gal2.jpg",
        "queries": ["Solang Valley Manali landscape", "Solang Valley adventure Manali paragliding", "Solang Valley snow", "Solang Nullah Manali"]
    },
    {
        "filename": "himachal_gal3.jpg",
        "queries": ["Hadimba Devi Temple Manali", "Hidimba Devi Temple Manali cedar", "Hadimba Temple Manali wooden", "Dhungari Temple Manali"]
    },
    {
        "filename": "jaisalmer_gal1.jpg",
        "queries": ["Chandraprabhu Jain Temple Jaisalmer Fort", "Jain temple Jaisalmer Fort carvings", "Jaisalmer Fort interior street", "Jain temples of Jaisalmer"]
    },
    {
        "filename": "jaisalmer_gal2.jpg",
        "queries": ["Sam Sand Dunes Thar desert sunset", "Thar desert dunes Jaisalmer sunset", "Sam sand dunes camels", "Dunes of Sam Jaisalmer"]
    },
    {
        "filename": "jaisalmer_gal3.jpg",
        "queries": ["Patwon Ki Haveli facade Jaisalmer", "Patwa Haveli Jaisalmer jharokha", "Patwon Ki Haveli interior", "Patwon-ki-Haveli Jaisalmer"]
    },
    {
        "filename": "udaipur_gal1.jpg",
        "queries": ["Boat on Lake Pichola Udaipur sunset", "Sunset Lake Pichola boat cruise", "Lake Pichola boat ghats", "Boating Lake Pichola"]
    },
    {
        "filename": "udaipur_gal2.jpg",
        "queries": ["City Palace Udaipur facade lake view", "City Palace, Udaipur courtyard", "City Palace complex Udaipur", "City Palace Udaipur"]
    },
    {
        "filename": "udaipur_gal3.jpg",
        "queries": ["Sajjangarh Monsoon Palace Udaipur", "Monsoon Palace Udaipur hill", "Saheliyon ki Bari Udaipur fountains", "Saheliyon-ki-Bari Udaipur"]
    },
    {
        "filename": "mon_hero.jpg",
        "queries": ["Mon district Nagaland landscape", "Hills of Mon Nagaland", "Landscape of Mon Nagaland", "Nagaland misty mountains", "Mon Nagaland village"]
    }
]

def search_commons_files(query):
    time.sleep(1.0)
    url = f'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&srlimit=8&format=json'
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('query', {}).get('search', [])
            titles = []
            for item in items:
                t = item.get('title', '')
                tl = t.lower()
                if any(bad in tl for bad in ['.svg', '.webm', '.ogv', '.pdf', '.tif', 'map', 'locator', 'flag', 'icon', 'plan', 'chart', 'symbol', 'logo']):
                    continue
                if any(tl.endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
                    titles.append(t)
            return titles
    except Exception as e:
        print(f"  Search error: {e}")
        return []

def get_image_url(file_title):
    time.sleep(0.7)
    url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json'
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                ii = p.get('imageinfo', [{}])[0]
                return ii.get('thumburl') or ii.get('url')
    except Exception as e:
        print(f"  URL error: {e}")
        return None

def download_file(img_url, target_path):
    req = urllib.request.Request(img_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            if len(data) < 10000:
                return False
            with open(target_path, 'wb') as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"  Download error: {e}")
        return False

def main():
    print(f"Downloading {len(REMAINING_TASKS)} targeted images with force overwrite...")
    for task in REMAINING_TASKS:
        filename = task["filename"]
        target_path = os.path.join(IMG_DIR, filename)
        print(f"\nProcessing {filename}...")
        
        success = False
        for q in task["queries"]:
            print(f"  Searching '{q}'...")
            titles = search_commons_files(q)
            for t in titles:
                url = get_image_url(t)
                if not url:
                    continue
                print(f"    Downloading {t} -> {url[:60]}...")
                if download_file(url, target_path):
                    print(f"    SUCCESS: Saved {filename} ({os.path.getsize(target_path)} bytes)")
                    success = True
                    break
            if success:
                break
        if not success:
            print(f"  FAILED to download {filename}")

if __name__ == "__main__":
    main()
