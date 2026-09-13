import os
import re

WORKSPACE = r'c:\Users\Hp\PycharmProjects\indiatoursite'
PAGES_DIR = os.path.join(WORKSPACE, 'Pages-inside')

DESTINATIONS_DATA = {
    "Alleppey-Info.html": {
        "hero": "../img/alleppey_hero.jpg",
        "gal1": ("../img/alleppey_gal1.jpg", "Kerala Houseboat on Backwaters"),
        "gal2": ("../img/alleppey_gal2.jpg", "Backwater Canals and Lagoons"),
        "gal3": ("../img/alleppey_gal3.jpg", "Vembanad Lake Sunset")
    },
    "Bikaner-Info.html": {
        "hero": "../img/bikaner_hero.jpg",
        "gal1": ("../img/bikaner_gal1.jpg", "Junagarh Fort Gateway & Courtyard"),
        "gal2": ("../img/bikaner_gal2.jpg", "Lalgarh Palace Architecture"),
        "gal3": ("../img/bikaner_gal3.jpg", "National Camel Research Centre")
    },
    "CamelSafari-Info.html": {
        "hero": "../img/camelsafari_hero.jpg",
        "gal1": ("../img/camelsafari_gal1.jpg", "Camel Caravan across Sand Dunes"),
        "gal2": ("../img/camelsafari_gal2.jpg", "Desert Camping under Starlit Skies"),
        "gal3": ("../img/camelsafari_gal3.jpg", "Golden Thar Desert Dunes")
    },
    "ColvaBeach-Info.html": {
        "hero": "../img/colvabeach_hero.jpg",
        "gal1": ("../img/colvabeach_gal1.jpg", "Watersports & Parasailing at Colva"),
        "gal2": ("../img/colvabeach_gal2.jpg", "Sunset over Arabian Sea at Colva"),
        "gal3": ("../img/colvabeach_gal3.jpg", "Basilica of Bom Jesus, Old Goa")
    },
    "GoldenTemple-Info.html": {
        "hero": "../img/golden_temple_hero.png",
        "gal1": ("../img/golden_temple_arch.png", "Intricate Gold Dome Architecture"),
        "gal2": ("../img/golden_temple_reflection.png", "Amrit Sarovar Holy Pool Reflection"),
        "gal3": ("../img/wagah_border.png", "Wagah Border Beating Retreat Ceremony")
    },
    "GwaliorFort-Info.html": {
        "hero": "../img/gwaliorfort_hero.jpg",
        "gal1": ("../img/gwaliorfort_gal1.jpg", "Man Mandir Palace Blue Ceramic Tiles"),
        "gal2": ("../img/gwaliorfort_gal2.jpg", "Sas Bahu Temple Intricate Sculptures"),
        "gal3": ("../img/gwaliorfort_gal3.jpg", "Gopachal Monumental Rock-Cut Jain Colossi")
    },
    "Hampi-Info.html": {
        "hero": "../img/hampi_hero.jpg",
        "gal1": ("../img/hampi_gal1.jpg", "Sacred Courtyard of Virupaksha Temple"),
        "gal2": ("../img/hampi_gal2.jpg", "Stone Chariot at Vittala Temple"),
        "gal3": ("../img/hampi_gal3.jpg", "Hemakuta Hill Boulder Landscape")
    },
    "Himachal-Info.html": {
        "hero": "../img/himachal_hero.jpg",
        "gal1": ("../img/himachal_gal1.jpg", "Christ Church & The Ridge, Shimla"),
        "gal2": ("../img/himachal_gal2.jpg", "Solang Valley Mountain Adventures"),
        "gal3": ("../img/himachal_gal3.jpg", "Ancient Wooden Hadimba Devi Temple")
    },
    "Jaipur-Info.html": {
        "hero": "../img/jaipur_hero.jpg",
        "gal1": ("../img/jaipur_gal1.jpg", "Ganesh Pol Courtyards of Amer Fort"),
        "gal2": ("../img/jaipur_gal2.jpg", "Iconic 953-Lattice Hawa Mahal Facade"),
        "gal3": ("../img/jaipur_gal3.jpg", "City Palace Peacock Gate Details")
    },
    "Jaisalmer-Info.html": {
        "hero": "../img/jaisalmer_hero.jpg",
        "gal1": ("../img/jaisalmer_gal1.jpg", "Chandraprabhu Jain Temples inside Fort"),
        "gal2": ("../img/jaisalmer_gal2.jpg", "Sam Sand Dunes Thar Desert Sunset"),
        "gal3": ("../img/jaisalmer_gal3.jpg", "Patwon Ki Haveli Jharokha Facade")
    },
    "Jodhpur-Info.html": {
        "hero": "../img/jodhpur_hero.jpg",
        "gal1": ("../img/jodhpur_gal1.jpg", "Jaswant Thada White Marble Memorial"),
        "gal2": ("../img/jodhpur_gal2.jpg", "Blue City Brahmapuri Rooftop Panorama"),
        "gal3": ("../img/jodhpur_gal3.jpg", "Umaid Bhawan Royal Sandstone Palace")
    },
    "Kashmir-Info.html": {
        "hero": "../img/kashmir_hero.jpg",
        "gal1": ("../img/kashmir_gal1.jpg", "Traditional Carved Wooden Houseboats"),
        "gal2": ("../img/kashmir_gal2.jpg", "Gulmarg Gondola & Snow Slopes"),
        "gal3": ("../img/kashmir_gal3.jpg", "Shalimar & Nishat Mughal Gardens")
    },
    "MehrangarhFort-Info.html": {
        "hero": "../img/mehrangarhfort_hero.jpg",
        "gal1": ("../img/mehrangarhfort_gal1.jpg", "Historic Cannons on Ramparts"),
        "gal2": ("../img/mehrangarhfort_gal2.jpg", "Blue City Panorama from Battlements"),
        "gal3": ("../img/mehrangarhfort_gal3.jpg", "Phool Mahal Royal Gilded Interiors")
    },
    "Mon-Info.html": {
        "hero": "../img/mon_hero.jpg",
        "gal1": ("../img/mon_gal1.jpg", "Longwa Village Thatched Morung Houses"),
        "gal2": ("../img/mon_gal2.jpg", "Highland Valleys and Tea Gardens"),
        "gal3": ("../img/mon_gal3.jpg", "Konyak Naga Warrior Regalia and Culture")
    },
    "Pushkar-Info.html": {
        "hero": "../img/pushkar_hero.jpg",
        "gal1": ("../img/pushkar_gal1.jpg", "Varaha & Brahma Ghats along Holy Lake"),
        "gal2": ("../img/pushkar_gal2.jpg", "Jagatpita Brahma Mandir Spire"),
        "gal3": ("../img/pushkar_gal3.jpg", "Vibrant Pushkar Camel Fair Gathering")
    },
    "SanchiStupa-Info.html": {
        "hero": "../img/sanchistupa_hero.jpg",
        "gal1": ("../img/sanchistupa_gal1.jpg", "Carved Southern Torana Gateway"),
        "gal2": ("../img/sanchistupa_gal2.jpg", "Ashoka Pillar & Ancient Monasteries"),
        "gal3": ("../img/sanchistupa_gal3.jpg", "Gupta Temple 17 Buddhist Monument")
    },
    "Twang-Info.html": {
        "hero": "../img/twang_hero.jpg",
        "gal1": ("../img/twang_gal1.jpg", "Kakaling Painted Entrance Gateway"),
        "gal2": ("../img/twang_gal2.jpg", "Sela Pass & Frozen Sela Lake at 13,700 ft"),
        "gal3": ("../img/twang_gal3.jpg", "Sangetsar (Madhuri) Alpine Lake")
    },
    "Udaipur-Info.html": {
        "hero": "../img/udaipur_hero.jpg",
        "gal1": ("../img/udaipur_gal1.jpg", "Sunset Wooden Boat Cruise on Pichola"),
        "gal2": ("../img/udaipur_gal2.jpg", "Grand Granite Facade of City Palace"),
        "gal3": ("../img/udaipur_gal3.jpg", "Sajjangarh Monsoon Palace on Mountain")
    },
    "UmngotRiver-Info.html": {
        "hero": "../img/umngotriver_hero.jpg",
        "gal1": ("../img/umngotriver_gal1.jpg", "Transparent Canoe Ride showing Riverbed"),
        "gal2": ("../img/umngotriver_gal2.jpg", "Double-Decker Living Root Bridge, Nongriat"),
        "gal3": ("../img/umngotriver_gal3.jpg", "Turquoise Cascades of Krang Suri Waterfall")
    },
    "Uttrakhand-Info.html": {
        "hero": "../img/uttrakhand_hero.jpg",
        "gal1": ("../img/uttrakhand_gal1.jpg", "Lakshman Jhula Suspension Bridge"),
        "gal2": ("../img/uttrakhand_gal2.jpg", "Ganga Aarti at Har Ki Pauri, Haridwar"),
        "gal3": ("../img/uttrakhand_gal3.jpg", "Gun Hill Panorama of Mussoorie")
    },
    "VivekanandaRockMemorial-Info.html": {
        "hero": "../img/vivekanandarock_hero.jpg",
        "gal1": ("../img/vivekanandarock_gal1.jpg", "133-ft Thiruvalluvar Statue at Sunrise"),
        "gal2": ("../img/vivekanandarock_gal2.jpg", "Dhyana Mandapam Architecture on Rock"),
        "gal3": ("../img/vivekanandarock_gal3.jpg", "Sunrise over Triveni Sangam (Three Oceans)")
    }
}

DESTINATIONS_DROPDOWN_HTML = """                                <div class="dropdown-header" style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-secondary); padding:4px 12px; letter-spacing:0.5px;">Popular Destinations</div>
                                <a href="GoldenTemple-Info.html">✨ Golden Temple (Amritsar)</a>
                                <a href="Jaipur-Info.html">🏰 Jaipur (Pink City)</a>
                                <a href="Kashmir-Info.html">❄️ Kashmir (Paradise)</a>
                                <a href="Alleppey-Info.html">🚣 Alleppey (Backwaters)</a>
                                <a href="Himachal-Info.html">🏔️ Himachal (Manali)</a>
                                <a href="Jaisalmer-Info.html">🐪 Jaisalmer (Desert)</a>
                                <a href="Udaipur-Info.html">👑 Udaipur (Lakes)</a>
                                <a href="Hampi-Info.html">🏛️ Hampi (UNESCO Ruins)</a>
                                <a href="MehrangarhFort-Info.html">🚩 Mehrangarh Fort (Jodhpur)</a>
                                <a href="Uttrakhand-Info.html">🕉️ Uttarakhand (Rishikesh)</a>
                                <a href="Twang-Info.html">🌄 Tawang (Monastery)</a>
                                <a href="ColvaBeach-Info.html">🏖️ Colva Beach (Goa)</a>
                                <div class="dropdown-divider" style="height:1px; background:var(--card-border); margin:6px 0;"></div>
                                <a href="../index.html#middle" style="font-weight:700; color:var(--accent-primary) !important;">🗺️ View All Destinations &rarr;</a>"""

def build_header(filename):
    return f"""    <!-- Header Navigation -->
    <header class="default-header">
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container">
                <a class="navbar-brand d-flex align-items-center" href="../index.html">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 68" style="height: 48px; width: auto;">
                        <style>
                            .brand-primary {{ fill: #0f2952; transition: fill 0.3s ease; }}
                            .brand-accent {{ fill: #e85d07; }}
                            .brand-secondary {{ fill: #2c6e49; transition: fill 0.3s ease; }}
                            body.dark-mode .brand-primary {{ fill: #ffffff !important; }}
                            body.dark-mode .brand-secondary {{ fill: #8cc084 !important; }}
                        </style>
                        <g id="emblem" transform="translate(4, 4)">
                            <path d="M 6 44 L 17 26 L 24 33 L 33 21 L 42 34 L 50 44 Z" fill="#a5cbdc" fill-opacity="0.4" />
                            <path d="M 12 44 V 35 H 14 V 32 H 18 V 35 H 20 V 44 H 18 V 37 H 14 V 44 Z" fill="#c88c5c" />
                            <path d="M 23 44 H 35 V 39 H 23 Z M 27 39 C 27 33, 31 33, 31 39 Z M 29 33 V 31 Z" fill="#e2af66" />
                            <line x1="29" y1="33" x2="29" y2="31" stroke="#e2af66" stroke-width="1.5" />
                            <path d="M 22 44 H 23 V 31 H 22 Z M 35 44 H 36 V 31 H 35 Z" fill="#e2af66" />
                            <path d="M 38 44 L 40 23 H 41 L 43 44 Z" fill="#a25b49" />
                            <circle cx="43" cy="20" r="3.5" fill="#ffb703" />
                            <path d="M 10 44 A 22 22 0 1 1 48 38" fill="none" stroke="#0f2952" stroke-width="3" stroke-linecap="round" class="brand-primary" />
                            <path d="M 22 11 A 22 22 0 0 1 47 22" fill="none" stroke="#e85d07" stroke-width="2" stroke-linecap="round" />
                            <path d="M 8 32 A 22 22 0 0 0 24 53" fill="none" stroke="#2c6e49" stroke-width="2" stroke-linecap="round" class="brand-secondary" />
                            <path d="M 14 47 C 22 38, 38 38, 46 47 C 38 56, 22 56, 14 47 Z" fill="#0f2952" class="brand-primary" />
                        </g>
                        <g id="brand-text" transform="translate(68, 0)">
                            <text x="0" y="32" font-family="'Outfit', 'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="700" class="brand-primary">City Info</text>
                            <path d="M 18.5 11 C 17 11, 16.2 12.2, 16.2 13.5 C 16.2 15.5, 18.5 18, 18.5 18 C 18.5 18, 20.8 15.5, 20.8 13.5 C 20.8 12.2, 20 11, 18.5 11 Z" fill="#e85d07" />
                            <circle cx="18.5" cy="13.5" r="0.9" fill="#ffffff" />
                            <text x="96" y="32" font-family="'Outfit', 'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="700" class="brand-accent">India</text>
                            <text x="0" y="47" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="700" class="brand-secondary" letter-spacing="6.5">TRAVELS</text>
                        </g>
                    </svg>
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="lnr lnr-menu"></span>
                </button>
                <div class="collapse navbar-collapse justify-content-end align-items-center" id="navbarSupportedContent">
                    <ul class="navbar-nav align-items-center">
                        <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                        <li class="nav-item custom-dropdown">
                            <a class="nav-link active" href="../index.html#middle">Destinations <i class="fa fa-angle-down"></i></a>
                            <div class="custom-dropdown-menu">
{DESTINATIONS_DROPDOWN_HTML}
                            </div>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="../index.html#middle">Explore Themes</a></li>
                        <li class="nav-item"><a class="nav-link" href="blog.html">Travel Stories</a></li>
                        <li class="nav-item"><a class="nav-link" href="About.html">Our Motto</a></li>
                        <li class="nav-item"><a class="nav-link" href="Recent-Announcement.html">Announcements</a></li>
                        <li class="nav-item theme-toggle-li">
                            <button class="theme-toggle-btn" id="themeToggle" type="button" aria-label="Toggle Dark Mode">
                                <i class="fa fa-moon-o moon-icon"></i>
                                <i class="fa fa-sun-o sun-icon"></i>
                            </button>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>"""

SUBPAGE_FOOTER_HTML = """    <!-- Footer Area -->
    <footer class="footer-area section-gap">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-6 mb-4 mb-lg-0">
                    <div class="single-footer-widget">
                        <h6>About City Info India Travels</h6>
                        <p>Approved by the Ministry of Tourism, Govt. of India. We curate authentic, unforgettable travel experiences across India's most iconic destinations with 24/7 dedicated support.</p>
                        <p class="footer-text" style="margin-top: 16px;">Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | City Info India Travels</p>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6 col-sm-6 mb-4 mb-lg-0">
                    <div class="single-footer-widget">
                        <h6>Quick Links</h6>
                        <ul class="footer-nav">
                            <li><a href="../index.html">Home</a></li>
                            <li><a href="../index.html#middle">Destinations</a></li>
                            <li><a href="About.html">Our Motto</a></li>
                            <li><a href="blog.html">Travel Stories</a></li>
                            <li><a href="Recent-Announcement.html">Announcements</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 mb-4 mb-lg-0">
                    <div class="single-footer-widget">
                        <h6>Contact Us</h6>
                        <p><i class="fa fa-map-marker" style="color:var(--accent-primary); margin-right:8px;"></i>79, Scindia House, Connaught Place, Janpath, New Delhi</p>
                        <p><i class="fa fa-phone" style="color:var(--accent-primary); margin-right:8px;"></i>+91 87001 40135</p>
                        <p><i class="fa fa-envelope" style="color:var(--accent-primary); margin-right:8px;"></i>cityinfonetservices45@gmail.com</p>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <h6>Stay Connected</h6>
                        <p>Subscribe for seasonal offers and travel guides.</p>
                        <div id="mc_embed_signup">
                            <form target="_blank" action="https://formspree.io/f/xzzgaydr" method="POST" class="form-inline footer-newsletter-form">
                                <input class="form-control" name="EMAIL" placeholder="Your Email" required type="email" style="font-size: 13px;">
                                <button class="click-btn btn btn-default" type="submit"><i class="fa fa-paper-plane" aria-hidden="true"></i></button>
                            </form>
                        </div>
                        <div class="footer-social d-flex align-items-center" style="margin-top: 16px;">
                            <a href="https://www.facebook.com/share/1L5AW4uipD/" target="_blank" aria-label="Facebook"><i class="fa fa-facebook"></i></a>
                            <a href="https://www.instagram.com/travels_cityinfoindia?igsh=MWp5cWM5YmFocDhmNg==" target="_blank" aria-label="Instagram"><i class="fa fa-instagram"></i></a>
                            <a href="https://g.co/kgs/16ismLt" target="_blank" aria-label="Google Reviews"><i class="fa fa-google"></i></a>
                        </div>
                    </div>
                </div>							
            </div>
        </div>
    </footer>"""

QUERY_MODAL_HTML = """    <!-- Universal Query Modal -->
    <div id="queryModal">
        <div class="modal-content-custom">
            <button id="closeQueryModal" type="button">&times;</button>
            <h4 style="font-weight: 700; margin-bottom: 8px;">Plan Your Trip</h4>
            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 20px;">Send us your requirements for a customized package.</p>
            <form id="contact" action="https://formspree.io/f/xzzgaydr" method="POST">
                <input name="email" type="email" placeholder="Your Email Address" required style="width:100%; margin-bottom:12px; padding:12px; border-radius:8px; border:1px solid var(--card-border); background:var(--bg-primary); color:var(--text-primary);">
                <textarea name="message" placeholder="Tell us your dates, group size & requirements..." required style="width:100%; min-height:90px; margin-bottom:16px; padding:12px; border-radius:8px; border:1px solid var(--card-border); background:var(--bg-primary); color:var(--text-primary);"></textarea>
                <button class="primary-btn w-100" type="submit">Send Custom Enquiry</button>
            </form>
            <div id="queryMsg" style="margin-top:12px; color:#16a34a; font-weight:600; display:none; text-align:center;">Thank you! Your query has been submitted successfully.</div>
        </div>
    </div>"""

CHAT_WIDGET_HTML = """    <!-- Floating Inquiry Assistant Widget -->
    <div class="chat-widget-container">
        <div class="chat-fab" id="chatFab">
            <i class="fa fa-comments-o"></i>
            <div class="chat-fab-badge" style="display:none;"></div>
        </div>
        <div class="chat-panel" id="chatPanel">
            <div class="chat-header">
                <img src="../img/logoex.jpg" alt="Local Guide">
                <div class="chat-header-info">
                    <h5>Local Travel Guide</h5>
                    <span>Online</span>
                </div>
                <button class="chat-close" id="chatClose"><i class="fa fa-times"></i></button>
            </div>
            <div class="chat-body" id="chatBody">
                <!-- Messages dynamic loaded -->
            </div>
            <div class="chat-footer">
                <form class="chat-form" id="chatForm">
                    <input type="text" id="chatInput" placeholder="Type a message or click option..." required>
                    <button type="submit" class="chat-send-btn"><i class="fa fa-paper-plane-o"></i></button>
                </form>
            </div>
        </div>
    </div>"""

def rebuild_destination(filename):
    filepath = os.path.join(PAGES_DIR, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    data = DESTINATIONS_DATA[filename]

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else f"Explore India - {filename.split('-')[0]}"

    # Extract banner-content
    banner_content_match = re.search(r'<div class="banner-content">([\s\S]*?)</div>', content)
    if banner_content_match:
        banner_content_inner = banner_content_match.group(1).strip()
    else:
        dest_name = filename.split('-')[0]
        banner_content_inner = f"""<h5>Be part of this Wonderful Journey</h5>
            <h1>Explore {dest_name}!</h1>
            <button class="primary-btn openQueryModal" type="button">Send Us Query</button>"""

    # Ensure query button has openQueryModal class
    banner_content_inner = re.sub(r'id="openQueryModal"', 'class="primary-btn openQueryModal"', banner_content_inner)
    if 'openQueryModal' not in banner_content_inner:
        banner_content_inner = banner_content_inner.replace('class="primary-btn"', 'class="primary-btn openQueryModal"')

    # Extract #middle section
    middle_match = re.search(r'(<div id="middle">[\s\S]*?</div>)', content)
    if middle_match:
        middle_html = middle_match.group(1).strip()
    else:
        middle_html = '<div id="middle"><h3>About this Destination</h3><p>Experience the beauty and culture.</p></div>'

    # Clean any mojibake in middle_html
    middle_html = middle_html.replace('Ã¢â€šÂ¹', '₹').replace('Ã¢Â‚¬â€œ', '–').replace('Ã¢Â‚¬Â¢', '•')

    # Build clean HTML
    clean_html = f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{title}</title>
    <link rel="icon" href="../img/explore-india-logo.svg" type="image/svg+xml">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/linearicons.css">
    <link rel="stylesheet" href="../css/font-awesome.min.css">
    <link rel="stylesheet" href="../css/bootstrap.css">
    <link rel="stylesheet" href="../css/main.css">
    <link rel="stylesheet" href="../css/modern-custom.css">
    <style>
        .banner-area {{
            background-image: url('{data['hero']}');
            background-size: cover;
            background-position: center;
            color: #fff;
            text-align: center;
            padding: 140px 20px;
            position: relative;
        }}
        .banner-area .overlay {{
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.65) 0%, rgba(15, 23, 42, 0.8) 100%);
            position: absolute;
            top: 0; bottom: 0; left: 0; right: 0;
            z-index: 1;
        }}
        .banner-content {{ position: relative; z-index: 2; max-width: 800px; margin: 0 auto; }}
        .banner-content h1 {{ font-size: 2.8rem; font-weight: 800; color: #fff; margin: 12px 0 20px 0; }}
        .banner-content h5 {{ text-transform: uppercase; letter-spacing: 2px; font-weight: 600; color: #f9a826; }}
        #middle {{
            background-color: var(--card-bg, #fff);
            color: var(--text-primary, #1e293b);
            margin: 40px auto;
            max-width: 1140px;
            padding: 40px;
            border-radius: 16px;
            box-shadow: var(--card-shadow, 0 10px 30px rgba(0, 0, 0, 0.08));
            border: 1px solid var(--card-border, #e2e8f0);
        }}
        #middle h3 {{ color: var(--accent-primary, #e85d07); font-weight: 700; margin-top: 20px; margin-bottom: 15px; }}
        #middle p, #middle ul, #middle li {{ color: var(--text-secondary, #475569); line-height: 1.8; }}
        .row.gallery img {{
            width: 100%;
            height: 240px;
            object-fit: cover;
            border-radius: 14px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
        }}
        .row.gallery img:hover {{
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 14px 32px rgba(0, 0, 0, 0.2);
        }}
    </style>
</head>
<body class="inside-page-body">

{build_header(filename)}

    <!-- Hero Section -->
    <section class="banner-area">
        <div class="overlay"></div>
        <div class="banner-content">
            {banner_content_inner}
        </div>
    </section>

    <!-- Main Overview Content -->
    {middle_html}

    <!-- Visual Gallery Section -->
    <section class="py-5" style="background: var(--bg-secondary, #fafafa); margin-top: 40px;">
        <div class="container">
            <h3 class="mb-4 text-center font-weight-bold" style="color: var(--text-primary);"><i class="fa fa-camera" style="color: var(--accent-primary, #e85d07); margin-right: 8px;"></i> Visual Gallery</h3>
            <div class="row gallery justify-content-center">
                <div class="col-md-4 col-sm-6 mb-4 text-center">
                    <img src="{data['gal1'][0]}" alt="{data['gal1'][1]}">
                    <p class="font-weight-bold mt-2 mb-0" style="font-size: 0.95rem; color: var(--text-primary, #333);">{data['gal1'][1]}</p>
                </div>
                <div class="col-md-4 col-sm-6 mb-4 text-center">
                    <img src="{data['gal2'][0]}" alt="{data['gal2'][1]}">
                    <p class="font-weight-bold mt-2 mb-0" style="font-size: 0.95rem; color: var(--text-primary, #333);">{data['gal2'][1]}</p>
                </div>
                <div class="col-md-4 col-sm-6 mb-4 text-center">
                    <img src="{data['gal3'][0]}" alt="{data['gal3'][1]}">
                    <p class="font-weight-bold mt-2 mb-0" style="font-size: 0.95rem; color: var(--text-primary, #333);">{data['gal3'][1]}</p>
                </div>
            </div>
            <div class="text-center mt-4">
                <button class="primary-btn openQueryModal" type="button"><i class="fa fa-envelope-o" style="margin-right: 6px;"></i> Book / Plan Tour Here</button>
            </div>
        </div>
    </section>

{QUERY_MODAL_HTML}

{SUBPAGE_FOOTER_HTML}

{CHAT_WIDGET_HTML}

    <script src="../js/vendor/jquery-2.2.4.min.js"></script>
    <script src="../js/vendor/bootstrap.min.js"></script>
    <script src="../js/modern-custom.js" defer></script>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(clean_html)
    print(f"Cleanly rebuilt: {filename}")

def main():
    for filename in sorted(DESTINATIONS_DATA.keys()):
        rebuild_destination(filename)

if __name__ == '__main__':
    main()
