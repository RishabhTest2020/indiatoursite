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

TASKS = [
    {
        "dest": "alleppey",
        "slots": {
            "hero": ["Kerala Backwaters Alleppey houseboat", "Alappuzha houseboat", "Kerala backwaters cruise"],
            "gal1": ["Kerala Houseboat interior deck Alappuzha", "Houseboat in Kerala Backwaters", "Kettuvallam backwater"],
            "gal2": ["Alleppey backwater narrow canal canoe", "Canals of Alappuzha", "Alappuzha canal boat"],
            "gal3": ["Vembanad Lake sunset boat", "Vembanad Lake Alappuzha", "Nehru Trophy Boat Race Alappuzha"]
        }
    },
    {
        "dest": "bikaner",
        "slots": {
            "hero": ["Junagarh Fort Bikaner front facade", "Junagarh Fort, Bikaner", "Junagarh Fort Rajasthan"],
            "gal1": ["Junagarh Fort Bikaner entrance courtyard", "Karan Mahal Junagarh Fort", "Junagarh Fort gateway"],
            "gal2": ["Lalgarh Palace Bikaner", "The Laxmi Niwas Palace Bikaner", "Rampuria Haveli Bikaner"],
            "gal3": ["Camels at Camel Research Farm, Bikaner", "National Camel Research Centre Bikaner", "Karni Mata temple Deshnoke"]
        }
    },
    {
        "dest": "camelsafari",
        "slots": {
            "hero": ["Camels of Sum Desert Thar sunset Jaisalmer", "Camel caravan Thar desert sunset", "Camels in Thar Desert"],
            "gal1": ["Camel safari Sam Sand Dunes Thar Desert", "Camel riding Thar desert Jaisalmer", "Dunes of Thar Desert"],
            "gal2": ["Desert camp tents Sam Sand Dunes Jaisalmer", "Camp in Thar desert Rajasthan", "Desert camping Jaisalmer"],
            "gal3": ["Sunrise over Thar desert sand dunes ripples", "Sand dunes ripples Thar desert", "Sam Sand Dunes sunset"]
        }
    },
    {
        "dest": "colvabeach",
        "slots": {
            "hero": ["Colva Beach Goa palms sea", "Colva Beach, Goa, India", "Colva beach Goa sunset"],
            "gal1": ["Parasailing Goa beach watersports", "Water sports Goa beach parasailing", "Goa beach boats"],
            "gal2": ["Sunset Colva Beach South Goa", "Goa beach sunset palms", "South Goa beach sunset"],
            "gal3": ["Basilica of Bom Jesus Old Goa front", "Basilica of Bom Jesus, Old Goa", "Bom Jesus Church Goa"]
        }
    },
    {
        "dest": "gwaliorfort",
        "slots": {
            "hero": ["Gwalior Fort panorama hill view", "Gwalior Fort entrance", "Gwalior Fort hill"],
            "gal1": ["Man Singh Palace Gwalior Fort blue tiles", "Man Mandir Palace Gwalior Fort", "Man Singh Palace Gwalior"],
            "gal2": ["Sas Bahu Temple Gwalior carvings", "Sasbahu temple Gwalior Fort", "Sasbahu temple Gwalior"],
            "gal3": ["Gopachal rock-cut Jain monuments Gwalior", "Gopachal Parvat Jain colossi Gwalior", "Teli ka Mandir Gwalior Fort"]
        }
    },
    {
        "dest": "hampi",
        "slots": {
            "hero": ["Virupaksha Temple gopuram Hampi", "Virupaksha Temple, Hampi", "Hampi Virupaksha"],
            "gal1": ["Virupaksha Temple inner courtyard sanctum", "Virupaksha temple complex Hampi", "Hampi temple carvings"],
            "gal2": ["Stone Chariot Vittala Temple Hampi", "Vittala Temple Stone Chariot", "Stone Chariot Hampi"],
            "gal3": ["Hampi boulder landscape Hemakuta Hill sunset", "Hemakuta Hill temples Hampi", "Hampi landscape boulders"]
        }
    },
    {
        "dest": "himachal",
        "slots": {
            "hero": ["Himalayan mountains Himachal Pradesh snow panorama", "Himalayas Himachal Pradesh snow peaks", "Spiti valley snow peaks"],
            "gal1": ["Christ Church Ridge Shimla", "The Ridge Shimla evening", "Shimla Ridge Christ Church"],
            "gal2": ["Solang Valley Manali landscape snow", "Solang Valley adventure Manali", "Solang Valley Manali"],
            "gal3": ["Hadimba Devi Temple Manali cedar forest", "Hadimba Temple Manali", "Hidimba Devi Temple Manali"]
        }
    },
    {
        "dest": "jaisalmer",
        "slots": {
            "hero": ["Jaisalmer Fort golden sandstone hill", "Jaisalmer Fort exterior panorama", "Jaisalmer Fort"],
            "gal1": ["Jain temple inside Jaisalmer Fort carvings", "Chandraprabhu Jain Temple Jaisalmer Fort", "Jain temple Jaisalmer Fort"],
            "gal2": ["Sam Sand Dunes Thar desert sunset", "Sam sand dunes Jaisalmer sunset", "Thar desert dunes Jaisalmer"],
            "gal3": ["Patwon Ki Haveli Jaisalmer jharokha", "Patwon ki Haveli facade Jaisalmer", "Patwa Haveli Jaisalmer"]
        }
    },
    {
        "dest": "jodhpur",
        "slots": {
            "hero": ["Mehrangarh Fort Jodhpur hill view", "Mehrangarh Fort panorama", "Mehrangarh Fort from below"],
            "gal1": ["Jaswant Thada white marble memorial Jodhpur", "Jaswant Thada Dawn", "Jaswant Thada Jodhpur"],
            "gal2": ["Blue city Jodhpur houses Brahmapuri view", "Blue city Jodhpur view from above", "Blue houses Jodhpur"],
            "gal3": ["Umaid Bhawan Palace Jodhpur front", "Umaid Bhawan Palace, Jodhpur", "Umaid Bhawan Palace"]
        }
    },
    {
        "dest": "mehrangarhfort",
        "slots": {
            "hero": ["Mehrangarh Fort ramparts walls Jodhpur", "Mehrangarh Fort bastion", "Mehrangarh Fort walls"],
            "gal1": ["Mehrangarh Fort cannons overlooking city", "Cannons on Mehrangarh Fort ramparts", "Kilkila cannon Mehrangarh Fort"],
            "gal2": ["View of blue city from Mehrangarh Fort", "Jodhpur blue city from Mehrangarh ramparts", "Blue houses from Mehrangarh"],
            "gal3": ["Phool Mahal Mehrangarh Fort royal interior", "Sheesh Mahal Mehrangarh Fort Jodhpur", "Mehrangarh Fort museum interior"]
        }
    },
    {
        "dest": "mon",
        "slots": {
            "hero": ["Mon district Nagaland landscape hills", "Hills of Mon district Nagaland", "Nagaland misty mountains landscape"],
            "gal1": ["Longwa village Mon Nagaland", "Traditional house Longwa Mon Nagaland", "Morung Naga village"],
            "gal2": ["Misty hills landscape Nagaland Mon", "Nagaland mountain landscape", "Hills in Mon Nagaland"],
            "gal3": ["Konyak Naga traditional warrior dress", "Konyak tribal elder Nagaland", "Konyak Naga portrait"]
        }
    },
    {
        "dest": "pushkar",
        "slots": {
            "hero": ["Pushkar Lake ghats white temples", "Pushkar lake Rajasthan ghats", "Pushkar Lake view"],
            "gal1": ["Varaha Ghat Brahma Ghat Pushkar lake", "Ghats of Pushkar lake", "Evening at Pushkar lake"],
            "gal2": ["Brahma Temple Pushkar entrance spire", "Brahma Temple, Pushkar", "Jagatpita Brahma Mandir Pushkar"],
            "gal3": ["Camels of Pushkar Camel Fair festival", "Pushkar Fair camels Rajasthan", "Pushkar Camel Fair 2015"]
        }
    },
    {
        "dest": "sanchistupa",
        "slots": {
            "hero": ["Great Stupa at Sanchi dome monument", "Great Stupa, Sanchi", "Sanchi Stupa 1 panorama"],
            "gal1": ["Sanchi Stupa 1 Southern Gateway Torana", "Sanchi Torana carvings", "Northern Gateway Sanchi Stupa"],
            "gal2": ["Ashoka Pillar ruins Sanchi monastery", "Sanchi monastery ruins", "Monastery ruins Sanchi"],
            "gal3": ["Temple 17 Sanchi Buddhist monument", "Gupta Temple 17 Sanchi", "Sanchi Stupa 3"]
        }
    },
    {
        "dest": "twang",
        "slots": {
            "hero": ["Tawang Monastery Arunachal Pradesh ridge", "Tawang Monastery panorama", "Tawang Gompa"],
            "gal1": ["Tawang Monastery Kakaling gateway entrance", "Kakaling gateway Tawang", "Tawang monastery entrance"],
            "gal2": ["Sela Pass Tawang prayer flags lake", "Sela Pass gate Arunachal Pradesh", "Sela Lake Arunachal Pradesh"],
            "gal3": ["Sangetsar Lake Madhuri Lake Tawang", "Sangetsar Lake Arunachal Pradesh", "PTSO Lake Tawang"]
        }
    },
    {
        "dest": "udaipur",
        "slots": {
            "hero": ["Taj Lake Palace Lake Pichola Udaipur", "Lake Palace Udaipur Lake Pichola", "Jag Niwas Lake Palace Udaipur"],
            "gal1": ["Boat on Lake Pichola Udaipur sunset", "Sunset Lake Pichola boat cruise", "Lake Pichola boat"],
            "gal2": ["City Palace Udaipur facade lake view", "City Palace, Udaipur", "City Palace complex Udaipur"],
            "gal3": ["Sajjangarh Monsoon Palace Udaipur hill", "Monsoon Palace Sajjangarh Udaipur", "Saheliyon ki Bari Udaipur fountains"]
        }
    },
    {
        "dest": "umngotriver",
        "slots": {
            "hero": ["Umngot river Dawki crystal clear boat floating", "Dawki river Umngot boat", "Boating Dawki Shillong Meghalaya"],
            "gal1": ["Dawki river transparent water pebbles canoe", "Clear water Umngot Dawki", "Dawki river canoe Meghalaya"],
            "gal2": ["Double decker living root bridge Nongriat Meghalaya", "Living root bridges Nongriat village Meghalaya", "Living root bridge Cherrapunji"],
            "gal3": ["Krang Suri falls Meghalaya turquoise waterfall", "Krang Suri Falls Jaintia Hills", "Elephant Falls Shillong Meghalaya"]
        }
    },
    {
        "dest": "uttrakhand",
        "slots": {
            "hero": ["Rishikesh Ganga river Himalayas view", "Ganges River in Rishikesh view", "Rishikesh Himalayan foothills"],
            "gal1": ["Lakshman Jhula bridge Rishikesh Ganges", "Lakshman Jhula Rishikesh", "Laxman Jhula Rishikesh Uttarakhand"],
            "gal2": ["Har Ki Pauri evening Ganga Aarti Haridwar lamps", "Har Ki Pauri Ganga Aarti Haridwar", "Ganga Aarti at Har Ki Pauri Haridwar"],
            "gal3": ["Mussoorie hills landscape Uttarakhand mountains", "Gun Hill Mussoorie Himalayas", "Mussoorie mountain view Uttarakhand"]
        }
    },
    {
        "dest": "vivekanandarock",
        "slots": {
            "hero": ["Vivekananda Rock Memorial Kanyakumari island ocean", "Vivekananda Rock Memorial, Kanyakumari", "Vivekananda Rock Memorial ocean"],
            "gal1": ["Thiruvalluvar Statue Kanyakumari sunrise ocean", "Thiruvalluvar Statue at Kanyakumari", "Thiruvalluvar Statue sunrise"],
            "gal2": ["Vivekananda Rock Memorial mandapam temple", "Dhyana Mandapam Vivekananda Rock", "Vivekananda Rock Memorial entrance"],
            "gal3": ["Kanyakumari sunrise Triveni Sangam waves", "Kanyakumari seashore sunrise", "Three seas confluence Kanyakumari sunrise"]
        }
    }
]

def search_commons_files(query):
    time.sleep(1.2)  # Respect API rate limits
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
        print(f"  Search error for '{query}': {e}")
        return []

def get_image_url(file_title):
    time.sleep(0.8)
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
        print(f"  URL error for '{file_title}': {e}")
        return None

def download_file(img_url, target_path):
    req = urllib.request.Request(img_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            if len(data) < 10000:
                print(f"  Warning: downloaded image too small ({len(data)} bytes)")
                return False
            with open(target_path, 'wb') as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"  Download error from {img_url}: {e}")
        return False

def main():
    print(f"Starting destination image acquisition to {IMG_DIR}...")
    used_titles_per_dest = {}

    for task in TASKS:
        dest = task["dest"]
        print(f"\n==========================================")
        print(f"Processing destination: {dest.upper()}")
        print(f"==========================================")
        used_titles_per_dest[dest] = set()

        for slot_name, queries in task["slots"].items():
            filename = f"{dest}_{slot_name}.jpg"
            target_path = os.path.join(IMG_DIR, filename)

            # Check if already distinct and downloaded
            if os.path.exists(target_path):
                # Verify it's not a dummy clone
                size = os.path.getsize(target_path)
                print(f"Checking existing {filename} (size {size} bytes)...")
                # If size is identical to hero and it's gal slot, we must re-download!
                hero_path = os.path.join(IMG_DIR, f"{dest}_hero.jpg")
                if slot_name != "hero" and os.path.exists(hero_path):
                    if size == os.path.getsize(hero_path):
                        print(f"  {filename} is duplicate of hero! Overwriting with distinct image...")
                    else:
                        print(f"  {filename} already exists and is distinct. Skipping.")
                        continue
                elif slot_name == "hero":
                    # Check if hero was a clone of others
                    pass

            downloaded = False
            for query in queries:
                print(f"  Searching for [{slot_name}]: '{query}'...")
                file_titles = search_commons_files(query)
                for title in file_titles:
                    if title in used_titles_per_dest[dest]:
                        continue # Don't reuse image within same destination!
                    
                    img_url = get_image_url(title)
                    if not img_url:
                        continue
                    
                    print(f"    Trying {title} -> {img_url[:65]}...")
                    if download_file(img_url, target_path):
                        used_titles_per_dest[dest].add(title)
                        print(f"    SUCCESS: Saved {filename} ({os.path.getsize(target_path)} bytes)")
                        downloaded = True
                        break
                if downloaded:
                    break
            
            if not downloaded:
                print(f"  FAILED to download distinct image for {filename}!")

if __name__ == "__main__":
    main()
