import urllib.request
import urllib.parse
import json

HEADERS = {
    'User-Agent': 'IndiaToursTravelSite/1.0 (https://indiatoursite.local; info@indiatoursite.com)',
    'Referer': 'https://commons.wikimedia.org/'
}

def search(query):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&srlimit=5&format=json'
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return [item['title'] for item in data.get('query', {}).get('search', []) if item['title'].lower().endswith(('.jpg', '.png', '.jpeg'))]

print("Taj Mahal:", search("Taj Mahal Agra Uttar Pradesh India"))
print("Taj Mahal reflection:", search("Taj Mahal in Agra sunrise reflection pool"))
