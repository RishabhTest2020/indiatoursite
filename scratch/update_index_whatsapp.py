import re

file_path = r'c:\Users\Hp\PycharmProjects\indiatoursite\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Nav bar WhatsApp button
if 'wa-nav-btn' not in content:
    nav_search = '<li class="nav-item theme-toggle-li">'
    nav_replace = """								<li class="nav-item">
									<a class="wa-nav-btn wa-dynamic-btn" href="https://wa.me/918700140135" target="_blank" rel="noopener noreferrer"><i class="fa fa-whatsapp"></i> WhatsApp</a>
								</li>
								<li class="nav-item theme-toggle-li">"""
    content = content.replace(nav_search, nav_replace, 1)

# 2. Footer WhatsApp contact
if 'fa-whatsapp' not in content:
    phone_search = '<p><i class="fa fa-phone" style="color:var(--accent-primary); margin-right:8px;"></i>+91 87001 40135</p>'
    phone_replace = """<p><i class="fa fa-phone" style="color:var(--accent-primary); margin-right:8px;"></i>+91 87001 40135</p>
									<p><i class="fa fa-whatsapp" style="color:var(--wa-green, #25D366); margin-right:8px;"></i><a href="https://wa.me/918700140135" class="wa-dynamic-btn" target="_blank" rel="noopener noreferrer" style="color:inherit; font-weight:600;">+91 87001 40135 (WhatsApp)</a></p>"""
    content = content.replace(phone_search, phone_replace, 1)

# 3. Add WhatsApp quote button inside .card-meta-info in single-portfolio cards
def add_card_btn(match):
    inner = match.group(1)
    if 'wa-card-btn' in inner:
        return match.group(0)
    btn_html = '									<a href="https://wa.me/918700140135" class="wa-card-btn wa-dynamic-btn" title="Chat on WhatsApp for customized quote"><i class="fa fa-whatsapp"></i> Quote</a>\n'
    return f'<div class="card-meta-info">\n{inner}{btn_html}								  </div>'

content = re.sub(r'<div class="card-meta-info">\s*([\s\S]*?)\s*</div>', add_card_btn, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")
