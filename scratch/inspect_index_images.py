import re
from html.parser import HTMLParser

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.current_tag = None
        self.current_attrs = {}

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == 'img':
            self.images.append(attr_dict)
        if 'style' in attr_dict and 'url(' in attr_dict['style']:
            m = re.search(r'url\([\'"]?([^\'"]+)[\'"]?\)', attr_dict['style'])
            if m:
                self.images.append({'src': m.group(1), 'type': 'bg', 'tag': tag, 'id': attr_dict.get('id', '')})

parser = ImageParser()
parser.feed(content)

print("=== ALL IMAGES IN index.html ===")
for i, img in enumerate(parser.images):
    print(f"{i+1}: {img}")

# Also let's inspect the sections around portfolio / destinations in index.html
print("\n=== SEARCH FOR PORTFOLIO ITEMS IN index.html ===")
portfolio_blocks = re.findall(r'(<div class="single-portfolio[^>]*>.*?</div>\s*</div>\s*</div>)', content, re.DOTALL)
print(f"Found {len(portfolio_blocks)} single-portfolio blocks")
for idx, b in enumerate(portfolio_blocks):
    src = re.search(r'src="([^"]+)"', b)
    title = re.search(r'<h4><a[^>]*>([^<]+)</a></h4>', b)
    region = re.search(r'<h6>([^<]+)</h6>', b)
    link = re.search(r'<a href="([^"]+)"', b)
    print(f"{idx+1}. Title: {title.group(1) if title else 'N/A'} | Src: {src.group(1) if src else 'N/A'} | Link: {link.group(1) if link else 'N/A'}")
