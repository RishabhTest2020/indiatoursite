import urllib.request
import urllib.parse
import json
import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{page_title} | Explore India</title>
    <meta name="description" content="{hero_desc}">
    <link rel="icon" href="../img/explore-india-logo.svg" type="image/svg+xml">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/linearicons.css">
    <link rel="stylesheet" href="../css/font-awesome.min.css">
    <link rel="stylesheet" href="../css/bootstrap.css">
    <link rel="stylesheet" href="../css/main.css">
    <link rel="stylesheet" href="../css/modern-custom.css">
</head>
<body class="inside-page-body">

    <!-- Header Navigation -->
    <header class="default-header">
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container">
                <a class="navbar-brand d-flex align-items-center" href="../index.html">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 68" style="height: 44px; width: auto;">
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
                                <a href="GoldenTemple-Info.html">✨ Golden Temple (Amritsar)</a>
                                <a href="Jaipur-Info.html">🏰 Jaipur (Pink City)</a>
                                <a href="Kashmir-Info.html">❄️ Kashmir (Paradise)</a>
                                <a href="Alleppey-Info.html">🚣 Alleppey (Backwaters)</a>
                                <a href="Himachal-Info.html">🏔️ Himachal (Manali)</a>
                                <a href="Jaisalmer-Info.html">🐪 Jaisalmer (Desert)</a>
                                <a href="Udaipur-Info.html">👑 Udaipur (Lakes)</a>
                                <a href="Hampi-Info.html">🏛️ Hampi (UNESCO Ruins)</a>
                            </div>
                        </li>
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
    </header>

    <!-- Subpage Hero Banner -->
    <section class="subpage-hero" style="background-image: url('../img/{img_hero}');">
        <div class="container">
            <span class="subpage-badge"><i class="fa fa-sun-o"></i> {badge_text}</span>
            <h1>{hero_title}</h1>
            <p class="lead">{hero_desc}</p>
            <button class="primary-btn openQueryModal" type="button"><i class="fa fa-paper-plane"></i> Plan {hero_title} Tour</button>
        </div>
    </section>

    <!-- Quick Stats Bar -->
    <div class="container quick-stats-container">
        <div class="quick-stats-card">
            <div class="row">
                <div class="col-lg-3 col-6 mb-3 mb-lg-0">
                    <div class="stat-pill">
                        <div class="stat-icon"><i class="fa fa-clock-o"></i></div>
                        <div class="stat-info">
                            <span class="stat-label">Duration</span>
                            <span class="stat-val">{duration}</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-6 mb-3 mb-lg-0">
                    <div class="stat-pill">
                        <div class="stat-icon"><i class="fa fa-calendar"></i></div>
                        <div class="stat-info">
                            <span class="stat-label">Best Time</span>
                            <span class="stat-val">{best_time}</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-6 mb-3 mb-lg-0">
                    <div class="stat-pill">
                        <div class="stat-icon"><i class="fa fa-tag"></i></div>
                        <div class="stat-info">
                            <span class="stat-label">Budget</span>
                            <span class="stat-val">{budget}</span>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-6">
                    <div class="stat-pill">
                        <div class="stat-icon"><i class="fa fa-heart"></i></div>
                        <div class="stat-info">
                            <span class="stat-label">Ideal For</span>
                            <span class="stat-val">{ideal_for}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Content Area -->
    <section class="pb-5">
        <div class="container">
            <div class="row">
                <div class="col-lg-8">
                    <!-- Overview Card -->
                    <div class="inside-card">
                        <div class="inside-card-header">
                            <h3 class="inside-card-title"><i class="fa fa-university"></i> Overview</h3>
                        </div>
                        <p style="font-size: 1.05rem; line-height: 1.8; color: var(--text-secondary);">
                            {overview_text}
                        </p>
                    </div>

                    <!-- Curated Multi-Day Itinerary -->
                    <div class="inside-card">
                        <div class="inside-card-header">
                            <h3 class="inside-card-title"><i class="fa fa-list-alt"></i> Typical Itinerary</h3>
                        </div>
                        <div class="timeline">
                            <div class="timeline-item">
                                <span class="timeline-badge">Day 1</span>
                                <h4 class="timeline-title">{day1_title}</h4>
                                <p class="timeline-desc">{day1_desc}</p>
                            </div>
                            <div class="timeline-item">
                                <span class="timeline-badge">Day 2</span>
                                <h4 class="timeline-title">{day2_title}</h4>
                                <p class="timeline-desc">{day2_desc}</p>
                            </div>
                        </div>
                    </div>

                    <!-- Key Highlights -->
                    <div class="inside-card">
                        <div class="inside-card-header">
                            <h3 class="inside-card-title"><i class="fa fa-star"></i> Must-Try Experiences</h3>
                        </div>
                        <div class="highlights-list">
                            {highlights_html}
                        </div>
                    </div>

                    <!-- How to Reach -->
                    <div class="inside-card">
                        <div class="inside-card-header">
                            <h3 class="inside-card-title"><i class="fa fa-plane"></i> Logistics</h3>
                        </div>
                        <div class="logistics-grid">
                            <div class="logistics-box">
                                <div class="logistics-icon"><i class="fa fa-plane"></i></div>
                                <h5>By Air</h5>
                                <p>{air_logistics}</p>
                            </div>
                            <div class="logistics-box">
                                <div class="logistics-icon"><i class="fa fa-train"></i></div>
                                <h5>By Train</h5>
                                <p>{train_logistics}</p>
                            </div>
                            <div class="logistics-box">
                                <div class="logistics-icon"><i class="fa fa-car"></i></div>
                                <h5>By Road</h5>
                                <p>{road_logistics}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar CTA -->
                <div class="col-lg-4">
                    <div class="inside-card text-center sticky-top" style="top: 100px;">
                        <h4 style="font-weight: 800; margin-bottom: 12px; color: var(--text-primary);">Book {hero_title}</h4>
                        <p style="font-size: 0.92rem; color: var(--text-secondary); margin-bottom: 20px;">Hotels, premium transport, and local guide included.</p>
                        <button class="primary-btn w-100 openQueryModal mb-3" type="button"><i class="fa fa-envelope-o"></i> Request Quote</button>
                        <a href="tel:08700140135" class="btn btn-outline-secondary w-100 font-weight-bold" style="border-radius: 8px;"><i class="fa fa-phone"></i> Call +91 87001 40135</a>
                    </div>
                </div>
            </div>

            <!-- Curated Gallery Section -->
            <div class="mt-4">
                <h3 class="mb-4 font-weight-bold text-center"><i class="fa fa-camera" style="color: var(--accent-primary);"></i> Visual Gallery</h3>
                <div class="inside-gallery-grid">
                    <div class="inside-gallery-item">
                        <img src="../img/{img_gal1}" alt="Gallery 1">
                        <div class="inside-gallery-overlay"><span class="inside-gallery-title">{cap1}</span></div>
                    </div>
                    <div class="inside-gallery-item">
                        <img src="../img/{img_gal2}" alt="Gallery 2">
                        <div class="inside-gallery-overlay"><span class="inside-gallery-title">{cap2}</span></div>
                    </div>
                    <div class="inside-gallery-item">
                        <img src="../img/{img_gal3}" alt="Gallery 3">
                        <div class="inside-gallery-overlay"><span class="inside-gallery-title">{cap3}</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Universal Query Modal -->
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
    </div>

    <!-- Footer Area -->
    <footer class="footer-area section-gap">
        <div class="container">
            <div class="row">
                <div class="col-lg-5 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <h6>About City Info India Travels</h6>
                        <p>Approved by the Ministry of Tourism, Govt. of India. We craft unforgettable, authentic Indian travel experiences with 24/7 dedicated support and expert local drivers.</p>
                        <p class="footer-text">Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | City Info India Travels</p>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <h6>Quick Links</h6>
                        <ul class="footer-nav">
                            <li><a href="../index.html">Home</a></li>
                            <li><a href="About.html">About Us</a></li>
                            <li><a href="blog.html">Travel Stories</a></li>
                            <li><a href="Recent-Announcement.html">Announcements</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <h6>Contact Us</h6>
                        <p><i class="fa fa-map-marker" style="color:var(--accent-primary);"></i>79, Scindia House, Connaught Place, Janpath, New Delhi</p>
                        <p><i class="fa fa-phone" style="color:var(--accent-primary);"></i> +91 87001 40135</p>
                        <p><i class="fa fa-envelope" style="color:var(--accent-primary);"></i> cityindiainfotravels@gmail.com</p>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <script src="../js/vendor/jquery-2.2.4.min.js"></script>
    <script src="../js/vendor/bootstrap.min.js"></script>
    <script src="../js/modern-custom.js" defer></script>
</body>
</html>"""

DESTINATIONS = [
    {
        "filename": "Jaipur-Info.html",
        "page_title": "Jaipur - The Pink City",
        "badge_text": "Rajasthan • Royal Heritage",
        "hero_title": "Jaipur",
        "hero_desc": "Experience the vibrant culture, majestic forts, and rich heritage of Rajasthan's royal capital.",
        "duration": "3 Days / 2 Nights",
        "best_time": "Oct – March",
        "budget": "₹8,000 – ₹20,000",
        "ideal_for": "History, Culture & Photography",
        "overview_text": "Jaipur, the capital of Rajasthan, is affectionately known as the Pink City. Founded in 1727 by Maharaja Sawai Jai Singh II, it is a magnificent blend of Rajasthani tradition and modern urban life. The city features spectacular hill forts like Amer Fort, the iconic Hawa Mahal with its intricate lattice windows, and bustling bazaars filled with textiles and jewelry.",
        "day1_title": "Amer Fort & City Palace",
        "day1_desc": "Explore the majestic Amer Fort on a hilltop overlooking Maota Lake. In the afternoon, visit the sprawling City Palace complex and the Jantar Mantar observatory.",
        "day2_title": "Hawa Mahal & Local Bazaars",
        "day2_desc": "Photograph the stunning facade of the Hawa Mahal. Spend the rest of the day shopping for traditional handicrafts and jewelry in Johari Bazaar and Bapu Bazaar.",
        "highlights": ["Amer Fort Elephant Ride", "Hawa Mahal Photography", "City Palace Museum", "Jantar Mantar Observatory", "Authentic Rajasthani Thali"],
        "air_logistics": "Jaipur International Airport (JAI) connects to major Indian cities.",
        "train_logistics": "Jaipur Junction (JP) has excellent connectivity including Shatabdi Express.",
        "road_logistics": "NH48 connects Jaipur directly to Delhi (approx 5 hours).",
        "gallery_captions": ["Amer Fort Panorama", "Hawa Mahal Facade", "City Palace Details"],
        "wiki_searches": ["Amer Fort wide angle", "Hawa Mahal Jaipur", "City Palace Jaipur"]
    },
    {
        "filename": "Kashmir-Info.html",
        "page_title": "Kashmir - Paradise on Earth",
        "badge_text": "Jammu & Kashmir • Nature & Valleys",
        "hero_title": "Kashmir Valley",
        "hero_desc": "Discover the pristine beauty of Dal Lake, snow-capped peaks, and lush Mughal gardens in the 'Paradise on Earth'.",
        "duration": "5 Days / 4 Nights",
        "best_time": "April – October",
        "budget": "₹15,000 – ₹35,000",
        "ideal_for": "Nature Lovers & Honeymooners",
        "overview_text": "Kashmir is renowned globally for its unparalleled natural beauty. From the tranquil waters of Dal Lake in Srinagar, dotted with intricately carved houseboats, to the snow-covered slopes of Gulmarg and the breathtaking valleys of Pahalgam, Kashmir offers a surreal experience. The Mughal Gardens, built centuries ago, still bloom with vibrant colors every spring.",
        "day1_title": "Srinagar & Dal Lake",
        "day1_desc": "Arrive in Srinagar and check into a traditional houseboat. Enjoy a relaxing Shikara ride on Dal Lake at sunset, visiting floating markets.",
        "day2_title": "Gulmarg Excursion",
        "day2_desc": "Drive to Gulmarg, the Meadow of Flowers. Take the famous Gondola ride up to Mount Apharwat for spectacular views of the Himalayas.",
        "highlights": ["Houseboat Stay on Dal Lake", "Gulmarg Gondola Ride", "Pahalgam Valley Walk", "Mughal Gardens (Shalimar Bagh)", "Authentic Wazwan Cuisine"],
        "air_logistics": "Srinagar Airport (SXR) receives daily flights from Delhi and Mumbai.",
        "train_logistics": "Jammu Tawi (JAT) is the nearest major railhead, followed by a scenic drive.",
        "road_logistics": "NH44 connects Jammu to Srinagar via the Jawahar Tunnel.",
        "gallery_captions": ["Dal Lake Shikara", "Gulmarg Gondola", "Mughal Gardens"],
        "wiki_searches": ["Dal Lake Shikara", "Gulmarg snow", "Shalimar Bagh Srinagar"]
    },
    {
        "filename": "Alleppey-Info.html",
        "page_title": "Alleppey - Venice of the East",
        "badge_text": "Kerala • Backwaters & Nature",
        "hero_title": "Alleppey Backwaters",
        "hero_desc": "Cruise through tranquil palm-fringed canals and emerald green paddy fields on a traditional Kerala houseboat.",
        "duration": "2 Days / 1 Night",
        "best_time": "September – March",
        "budget": "₹7,000 – ₹18,000",
        "ideal_for": "Relaxation & Romantic Escapes",
        "overview_text": "Alappuzha, also known as Alleppey, is famous for its intricate network of interconnected backwater canals, rivers, and lakes. Known as the 'Venice of the East', its main attraction is the traditional Kettuvallam houseboats. A cruise along these serene waters provides an intimate glimpse into the traditional village life of Kerala, surrounded by lush green coconut groves.",
        "day1_title": "Houseboat Check-in & Cruise",
        "day1_desc": "Board your private houseboat at noon. Cruise through the scenic Vembanad Lake and narrow canals. Enjoy freshly prepared Kerala cuisine on board.",
        "day2_title": "Village Walk & Departure",
        "day2_desc": "Wake up to the sounds of nature. Take a small canoe to explore narrower canals and interact with locals before checking out.",
        "highlights": ["Overnight Houseboat Cruise", "Vembanad Lake Sunset", "Authentic Kerala Fish Curry", "Village Canoe Ride", "Alleppey Beach Sunset"],
        "air_logistics": "Cochin International Airport (COK) is 85 km away.",
        "train_logistics": "Alappuzha Railway Station (ALLP) is well connected to major cities.",
        "road_logistics": "NH66 connects Alleppey directly to Kochi and Trivandrum.",
        "gallery_captions": ["Kerala Houseboat", "Backwater Canals", "Vembanad Lake"],
        "wiki_searches": ["Alleppey Houseboat", "Kerala backwaters Alleppey", "Vembanad Lake"]
    },
    {
        "filename": "Himachal-Info.html",
        "page_title": "Himachal - Mountain Retreat",
        "badge_text": "Himachal Pradesh • Himalayan Escapes",
        "hero_title": "Shimla & Manali",
        "hero_desc": "Escape to the majestic Himalayas. Experience colonial charm, pine forests, and thrilling mountain adventures.",
        "duration": "6 Days / 5 Nights",
        "best_time": "March – June & Dec – Feb",
        "budget": "₹12,000 – ₹28,000",
        "ideal_for": "Adventure & Mountain Lovers",
        "overview_text": "Himachal Pradesh offers a perfect blend of natural beauty and adventure. Shimla, the former summer capital of British India, retains its colonial elegance with the Mall Road and Christ Church. Further north, Manali is a high-altitude resort town surrounded by towering peaks, serving as the gateway to the breathtaking Solang Valley and Rohtang Pass.",
        "day1_title": "Shimla Heritage Walk",
        "day1_desc": "Walk along the famous Ridge and Mall Road. Visit the neo-Gothic Christ Church and the historic Viceregal Lodge.",
        "day2_title": "Manali & Solang Valley",
        "day2_desc": "Drive to Manali. Spend a day in Solang Valley enjoying adventure sports like paragliding, skiing, or ATVs against a stunning alpine backdrop.",
        "highlights": ["Shimla Mall Road Stroll", "Solang Valley Adventures", "Rohtang Pass Snow", "Hadimba Temple Manali", "Toy Train Ride (Kalka-Shimla)"],
        "air_logistics": "Chandigarh Airport or Kullu-Bhuntar Airport for closer access.",
        "train_logistics": "Kalka Railway Station, followed by the scenic Toy Train to Shimla.",
        "road_logistics": "Excellent highway connectivity from Delhi to Shimla and Manali.",
        "gallery_captions": ["Shimla Ridge", "Solang Valley", "Hadimba Temple"],
        "wiki_searches": ["Shimla Ridge winter", "Solang Valley Manali", "Hadimba Temple Manali"]
    },
    {
        "filename": "Jaisalmer-Info.html",
        "page_title": "Jaisalmer - The Golden City",
        "badge_text": "Rajasthan • Desert Safari",
        "hero_title": "Jaisalmer",
        "hero_desc": "Experience the magic of the Thar Desert, golden sandstone forts, and starlit nights on the sand dunes.",
        "duration": "3 Days / 2 Nights",
        "best_time": "October – March",
        "budget": "₹7,000 – ₹18,000",
        "ideal_for": "Desert Adventures & History",
        "overview_text": "Jaisalmer, known as the Golden City, rises dramatically from the heart of the Thar Desert like a mirage. Its centerpiece is the magnificent Jaisalmer Fort, one of the world's few 'living forts' where a quarter of the city's population still resides. The city is famous for its exquisitely carved Haveli architecture, ancient Jain temples, and the unforgettable experience of sleeping under the stars at the Sam Sand Dunes.",
        "day1_title": "Jaisalmer Fort & Havelis",
        "day1_desc": "Explore the narrow alleys of the Golden Fort. Visit the intricately carved Patwon Ki Haveli and the ancient Jain temples inside the fort.",
        "day2_title": "Desert Safari & Camping",
        "day2_desc": "Head out to the Sam Sand Dunes in the evening. Enjoy a thrilling jeep safari, camel ride at sunset, and traditional Kalbelia folk dance by a campfire.",
        "highlights": ["Living Golden Fort", "Sam Sand Dunes Safari", "Patwon Ki Haveli", "Desert Night Camping", "Gadisar Lake Boating"],
        "air_logistics": "Jaisalmer Airport has seasonal flights from Delhi and Jaipur.",
        "train_logistics": "Jaisalmer Railway Station is connected to major cities in Rajasthan.",
        "road_logistics": "Well-connected by desert highways from Jodhpur and Bikaner.",
        "gallery_captions": ["Jaisalmer Fort", "Thar Desert Dunes", "Patwon Ki Haveli"],
        "wiki_searches": ["Jaisalmer Fort", "Sam Sand Dunes Jaisalmer", "Patwon Ki Haveli"]
    },
    {
        "filename": "Udaipur-Info.html",
        "page_title": "Udaipur - City of Lakes",
        "badge_text": "Rajasthan • Royal Romance",
        "hero_title": "Udaipur",
        "hero_desc": "Immerse yourself in the romance of shimmering lakes, grand palaces, and the majestic Aravalli hills.",
        "duration": "3 Days / 2 Nights",
        "best_time": "September – March",
        "budget": "₹9,000 – ₹25,000",
        "ideal_for": "Couples & Luxury Travel",
        "overview_text": "Udaipur, often called the 'Venice of the East', is arguably the most romantic city in India. Set around a series of artificial lakes and framed by the lush Aravalli hills, the city is famous for its palaces. The monumental City Palace towers over Lake Pichola, while the ethereal Lake Palace seems to float on its waters, creating a fairy-tale atmosphere.",
        "day1_title": "City Palace & Lake Pichola",
        "day1_desc": "Explore the sprawling City Palace complex. In the evening, take a sunset boat cruise on Lake Pichola, viewing the Jag Mandir and Lake Palace.",
        "day2_title": "Saheliyon Ki Bari & Sajjangarh",
        "day2_desc": "Visit the beautiful gardens of Saheliyon Ki Bari. Drive up to the Monsoon Palace (Sajjangarh) for panoramic sunset views over the lakes.",
        "highlights": ["Lake Pichola Boat Cruise", "City Palace Museum", "Monsoon Palace Sunset", "Jagdish Temple", "Romantic Lakeside Dining"],
        "air_logistics": "Maharana Pratap Airport (UDR) connects to Delhi and Mumbai.",
        "train_logistics": "Udaipur City Railway Station is well-connected.",
        "road_logistics": "Connected via NH48 from Ahmedabad and Jaipur.",
        "gallery_captions": ["Lake Pichola", "City Palace", "Monsoon Palace"],
        "wiki_searches": ["Lake Pichola Udaipur", "City Palace Udaipur", "Monsoon Palace Udaipur"]
    },
    {
        "filename": "Hampi-Info.html",
        "page_title": "Hampi - UNESCO World Heritage",
        "badge_text": "Karnataka • Ancient Ruins",
        "hero_title": "Hampi Ruins",
        "hero_desc": "Step back in time to the glorious Vijayanagara Empire amidst surreal boulder-strewn landscapes and ancient temples.",
        "duration": "3 Days / 2 Nights",
        "best_time": "October – February",
        "budget": "₹6,000 – ₹15,000",
        "ideal_for": "History, Backpacking & Photography",
        "overview_text": "Hampi, a UNESCO World Heritage site, is a mesmerizing landscape of giant granite boulders and ancient temple ruins. Once the capital of the wealthy Vijayanagara Empire, it is now an open-air museum. The Vittala Temple with its iconic stone chariot, the soaring Virupaksha Temple, and the royal enclosures tell the story of a forgotten empire set against a dramatic natural backdrop.",
        "day1_title": "Sacred Centre & Virupaksha",
        "day1_desc": "Explore the active Virupaksha Temple. Walk along the Tungabhadra river to the Vittala Temple complex to see the musical pillars and Stone Chariot.",
        "day2_title": "Royal Enclosure & Sunset",
        "day2_desc": "Discover the Lotus Mahal and Elephant Stables in the Royal Enclosure. Hike up Matanga Hill or Hemakuta Hill for a breathtaking sunset over the ruins.",
        "highlights": ["Vittala Temple Stone Chariot", "Matanga Hill Sunset", "Virupaksha Temple", "Lotus Mahal", "Coracle Ride on Tungabhadra"],
        "air_logistics": "Jindal Vijaynagar Airport (VDY) or Hubli Airport.",
        "train_logistics": "Hospet Junction (HPT) is just 15 km from Hampi.",
        "road_logistics": "Overnight buses available from Bangalore and Goa.",
        "gallery_captions": ["Virupaksha Temple", "Stone Chariot", "Hampi Boulder Landscape"],
        "wiki_searches": ["Virupaksha Temple Hampi", "Stone Chariot Hampi", "Hampi ruins landscape"]
    }
]

import time

def download_wiki_image(search_query, filename):
    if os.path.exists(filename):
        print(f"Already exists: {filename}")
        return True
        
    print(f"Searching Wikipedia for: {search_query}")
    time.sleep(2) # Respect rate limits
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(search_query)}&utf8=&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if not data['query']['search']: return False
            page_title = data['query']['search'][0]['title']
            url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(page_title)}&prop=images&format=json"
            req = urllib.request.Request(url, headers={'User-Agent': user_agent})
            with urllib.request.urlopen(req) as response:
                img_data = json.loads(response.read().decode())
                pages = img_data['query']['pages']
                page_id = list(pages.keys())[0]
                if 'images' not in pages[page_id]: return False
                valid_images = [img['title'] for img in pages[page_id]['images'] if img['title'].lower().endswith(('.jpg', '.jpeg', '.png'))]
                if not valid_images: return False
                
                # Filter out maps or icons if possible
                valid_images = [i for i in valid_images if 'map' not in i.lower() and 'icon' not in i.lower() and 'logo' not in i.lower()]
                if not valid_images: return False
                
                target_image = valid_images[0]
                url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(target_image)}&prop=imageinfo&iiprop=url&format=json"
                req = urllib.request.Request(url, headers={'User-Agent': user_agent})
                with urllib.request.urlopen(req) as response:
                    url_data = json.loads(response.read().decode())
                    img_pages = url_data['query']['pages']
                    img_page_id = list(img_pages.keys())[0]
                    img_url = img_pages[img_page_id]['imageinfo'][0]['url']
                    
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    img_req = urllib.request.Request(img_url, headers={'User-Agent': user_agent})
                    with urllib.request.urlopen(img_req) as img_resp:
                        with open(filename, 'wb') as f:
                            f.write(img_resp.read())
                    print(f"Downloaded: {filename}")
                    return True
    except Exception as e:
        print(f"Failed {search_query}: {e}")
        return False

def generate_htmls():
    base_dir = r"c:\Users\Hp\PycharmProjects\indiatoursite\Pages-inside"
    img_dir = r"c:\Users\Hp\PycharmProjects\indiatoursite\img"
    
    for dest in DESTINATIONS:
        print(f"Processing {dest['filename']}...")
        
        # Download images
        prefix = dest['filename'].split('-')[0].lower()
        img_hero = f"{prefix}_hero.jpg"
        img_gal1 = f"{prefix}_gal1.jpg"
        img_gal2 = f"{prefix}_gal2.jpg"
        img_gal3 = f"{prefix}_gal3.jpg"
        
        # We need 4 images (hero + 3 gallery). We will search 4 queries.
        queries = dest['wiki_searches']
        if len(queries) < 4:
            queries.append(dest['hero_title']) # Fallback query
            
        download_wiki_image(queries[0], os.path.join(img_dir, img_hero))
        download_wiki_image(queries[1], os.path.join(img_dir, img_gal1))
        download_wiki_image(queries[2], os.path.join(img_dir, img_gal2))
        download_wiki_image(queries[3], os.path.join(img_dir, img_gal3))
        
        # Build highlights HTML
        hl_html = ""
        for hl in dest['highlights']:
            hl_html += f'<div class="highlight-item"><i class="fa fa-check-circle"></i> {hl}</div>\n'
            
        # Render template
        html = TEMPLATE.format(
            page_title=dest['page_title'],
            hero_desc=dest['hero_desc'],
            img_hero=img_hero,
            badge_text=dest['badge_text'],
            hero_title=dest['hero_title'],
            duration=dest['duration'],
            best_time=dest['best_time'],
            budget=dest['budget'],
            ideal_for=dest['ideal_for'],
            overview_text=dest['overview_text'],
            day1_title=dest['day1_title'],
            day1_desc=dest['day1_desc'],
            day2_title=dest['day2_title'],
            day2_desc=dest['day2_desc'],
            highlights_html=hl_html,
            air_logistics=dest['air_logistics'],
            train_logistics=dest['train_logistics'],
            road_logistics=dest['road_logistics'],
            img_gal1=img_hero, # Use hero as first gallery image to ensure we have 3
            img_gal2=img_gal1,
            img_gal3=img_gal2,
            cap1=dest['gallery_captions'][0],
            cap2=dest['gallery_captions'][1],
            cap3=dest['gallery_captions'][2]
        )
        
        # Write to file
        file_path = os.path.join(base_dir, dest['filename'])
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created {file_path}")

if __name__ == '__main__':
    generate_htmls()
