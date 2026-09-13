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
        return [item['title'] for item in data.get('query', {}).get('search', [])]

print("Amer Fort:", search("Amber Fort Jaipur Maota Lake"))
print("Jal Mahal:", search("Jal Mahal Jaipur sunset"))
print("City Palace Jaipur:", search("City Palace Jaipur Peacock Gate courtyard"))
print("India Banner:", search("Taj Mahal sunrise panorama reflection"))
