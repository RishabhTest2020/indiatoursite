import re

file_path = r'c:\Users\Hp\PycharmProjects\indiatoursite\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update <head> up to <body>
head_pattern = r'<!DOCTYPE html>[\s\S]*?<body[^>]*>'
new_head = """<!DOCTYPE html>
	<html lang="en" class="no-js">
	<head>
		<!-- Google Tag Manager -->
		<!-- Replace GTM-XXXXXXX with your actual Google Tag Manager Container ID -->
		<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
		new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
		j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
		'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
		})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
		<!-- End Google Tag Manager -->

		<!-- Mobile Specific Meta -->
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<meta charset="UTF-8">

		<!-- Site Title & SEO Metadata -->
		<title>Explore India Tour Packages & Custom Itineraries | City Info India Travels</title>
		<meta name="description" content="Discover Incredible India with City Info India Travels. Book custom tour packages, cultural itineraries, desert safaris, and Himalayan holiday circuits.">
		<meta name="keywords" content="India tour packages, travel agency India, Delhi Agra Jaipur tour, Rajasthan desert safari, Kashmir packages, Kerala backwaters">
		<meta name="author" content="City Info India Travels">
		<link rel="canonical" href="https://cityinfoindiatravels.com/">

		<!-- Open Graph / Facebook -->
		<meta property="og:type" content="website">
		<meta property="og:url" content="https://cityinfoindiatravels.com/">
		<meta property="og:title" content="Explore India Tour Packages & Custom Itineraries | City Info India Travels">
		<meta property="og:description" content="Discover Incredible India with City Info India Travels. Book custom tour packages, cultural itineraries, desert safaris, and Himalayan holiday circuits.">
		<meta property="og:image" content="https://cityinfoindiatravels.com/img/india_hero_banner.jpg">

		<!-- Twitter -->
		<meta name="twitter:card" content="summary_large_image">
		<meta name="twitter:url" content="https://cityinfoindiatravels.com/">
		<meta name="twitter:title" content="Explore India Tour Packages & Custom Itineraries | City Info India Travels">
		<meta name="twitter:description" content="Discover Incredible India with City Info India Travels. Book custom tour packages, cultural itineraries, desert safaris, and Himalayan holiday circuits.">
		<meta name="twitter:image" content="https://cityinfoindiatravels.com/img/india_hero_banner.jpg">

		<!-- Favicon-->
		<link rel="shortcut icon" href="img/explore-india-logo.svg">
		<link rel="icon" href="img/explore-india-logo.svg" type="image/svg+xml">

		<!-- Google Fonts -->
		<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"> 

		<!-- Structured Data (JSON-LD) -->
		<script type="application/ld+json">
		{
			"@context": "https://schema.org",
			"@type": "TravelAgency",
			"name": "City Info India Travels",
			"url": "https://cityinfoindiatravels.com/",
			"logo": "https://cityinfoindiatravels.com/img/explore-india-logo.svg",
			"image": "https://cityinfoindiatravels.com/img/india_hero_banner.jpg",
			"description": "City Info India Travels offers authentic, custom India tour packages, cultural itineraries, Rajasthan desert safaris, and Himalayan expeditions.",
			"telephone": "+918700140135",
			"priceRange": "$$",
			"address": {
				"@type": "PostalAddress",
				"streetAddress": "79, Scindia House, Connaught Place, Janpath",
				"addressLocality": "New Delhi",
				"addressRegion": "Delhi",
				"postalCode": "110001",
				"addressCountry": "IN"
			}
		}
		</script>

		<!-- CSS -->
		<link rel="stylesheet" href="css/linearicons.css">
		<link rel="stylesheet" href="css/font-awesome.min.css">
		<link rel="stylesheet" href="css/bootstrap.css">
		<link rel="stylesheet" href="css/magnific-popup.css">
		<link rel="stylesheet" href="css/nice-select.css">					
		<link rel="stylesheet" href="css/animate.min.css">
		<link rel="stylesheet" href="css/owl.carousel.css">
		<link rel="stylesheet" href="css/main.css">
		<link rel="stylesheet" href="css/modern-custom.css">
	</head>
	<body>
		<!-- Google Tag Manager (noscript) -->
		<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
		height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
		<!-- End Google Tag Manager (noscript) -->"""

content = re.sub(head_pattern, new_head, content, count=1)

# 2. Add loading="lazy" to package card images in portfolio section
def add_lazy_to_card_img(match):
    img_tag = match.group(0)
    if 'loading="lazy"' in img_tag:
        return img_tag
    return img_tag[:-1] + ' loading="lazy">'

content = re.sub(r'<img src="img/[^"]+" alt="[^"]+">', add_lazy_to_card_img, content)
content = re.sub(r'<img class="img-fluid" src="img/[^"]+" alt="[^"]+">', add_lazy_to_card_img, content)

# 3. Footer WhatsApp contact
footer_phone = '<p><i class="fa fa-phone" style="color:var(--accent-primary); margin-right:8px;"></i>+91 87001 40135</p>'
if 'wa-dynamic-btn' not in content[content.find('Contact Us'):]:
    footer_phone_replacement = """<p><i class="fa fa-phone" style="color:var(--accent-primary); margin-right:8px;"></i>+91 87001 40135</p>
									<p><i class="fa fa-whatsapp" style="color:var(--wa-green, #25D366); margin-right:8px;"></i><a href="https://wa.me/918700140135" class="wa-dynamic-btn" target="_blank" rel="noopener noreferrer" style="color:inherit; font-weight:600;">+91 87001 40135 (WhatsApp)</a></p>"""
    content = content.replace(footer_phone, footer_phone_replacement, 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully with GTM, SEO, OG, JSON-LD, lazy loading and WhatsApp footer!")
