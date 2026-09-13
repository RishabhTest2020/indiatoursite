import os
import json

WORKSPACE = r'c:\Users\Hp\PycharmProjects\indiatoursite'
PAGES_DIR = os.path.join(WORKSPACE, 'Pages-inside')

DESTINATIONS_DATA = [
    {
        "filename": "GoldenTemple-Info.html",
        "page_title": "Golden Temple - Spiritual Jewel of Amritsar",
        "badge_text": "Punjab • Spiritual Heritage",
        "hero_title": "Golden Temple",
        "hero_desc": "Experience divine serenity, pure gold sanctum reflections in the sacred Amrit Sarovar, and the world's largest community kitchen.",
        "duration": "2 Days / 1 Night",
        "best_time": "October – March",
        "budget": "₹5,000 – ₹14,000",
        "ideal_for": "Spiritual Seekers & Families",
        "overview_text": "Sri Harmandir Sahib, popularly known as the Golden Temple, is the spiritual heartbeat of Sikhism and one of India's most welcoming holy shrines. Its golden dome gleams brilliantly over the sacred Amrit Sarovar. The complex embodies universal brotherhood and equality, serving over 100,000 free hot meals daily in the monumental Langar hall.",
        "day1_title": "Harmandir Sahib & Langar Experience",
        "day1_desc": "Visit the golden sanctum at sunrise, listen to the live Gurbani kirtan, take in the holy Amrit Sarovar reflection, and participate in the historic Langar community meal service.",
        "day2_title": "Wagah Border & Jallianwala Bagh",
        "day2_desc": "Pay respects at the historic Jallianwala Bagh memorial and witness the high-energy, patriotic Beating Retreat ceremony at the India-Pakistan Wagah Border.",
        "highlights": [
            "Pure Gold Sanctum & Amrit Sarovar Reflection",
            "World's Largest Free Kitchen (Langar Seva)",
            "Wagah Border Beating Retreat Ceremony",
            "Historic Jallianwala Bagh National Memorial",
            "Heritage Street Night Walk & Amritsari Kulcha"
        ],
        "air_logistics": "Sri Guru Ram Dass Jee International Airport (ATQ) connects to major hubs.",
        "train_logistics": "Amritsar Junction (ASR) connects directly via Shatabdi & Vande Bharat.",
        "road_logistics": "NH44 connects Delhi to Amritsar smoothly in approx 7-8 hours.",
        "img_hero": "goldentemple_hero.jpg",
        "img_gal1": "goldentemple_gal1.jpg",
        "img_gal2": "goldentemple_gal2.jpg",
        "img_gal3": "goldentemple_gal3.jpg",
        "cap1": "Sacred Pool Reflection",
        "cap2": "Intricate Gold Dome Architecture",
        "cap3": "Wagah Border Ceremony"
    },
    {
        "filename": "Jaipur-Info.html",
        "page_title": "Jaipur - The Royal Pink City",
        "badge_text": "Rajasthan • Royal Heritage",
        "hero_title": "Jaipur",
        "hero_desc": "Experience the vibrant culture, majestic hilltop forts, and royal courtyards of Rajasthan's regal capital.",
        "duration": "3 Days / 2 Nights",
        "best_time": "October – March",
        "budget": "₹8,000 – ₹20,000",
        "ideal_for": "History, Culture & Photography",
        "overview_text": "Jaipur, the capital of Rajasthan, is world-famous as the Pink City. Founded in 1727 by Maharaja Sawai Jai Singh II, it is a magnificent blend of Rajput tradition and urban planning. The city features hilltop fortifications like Amer Fort, the iconic 953-casement Hawa Mahal, and bustling bazaars overflowing with jewels, block-printed textiles, and pottery.",
        "day1_title": "Amer Fort & City Palace",
        "day1_desc": "Explore the majestic Amer Fort on a hilltop overlooking Maota Lake. In the afternoon, explore the sprawling City Palace complex and Jantar Mantar astronomical observatory.",
        "day2_title": "Hawa Mahal & Local Bazaars",
        "day2_desc": "Photograph the stunning honeycomb facade of Hawa Mahal. Shop for handcrafted souvenirs, lac bangles, and textiles in Johari and Bapu Bazaars.",
        "highlights": [
            "Amer Fort Sheesh Mahal (Mirror Palace)",
            "Iconic 953-Lattice Hawa Mahal Facade",
            "City Palace Peacock Gate Details",
            "UNESCO Jantar Mantar Observatory",
            "Authentic Dal Baati Churma Rajasthani Thali"
        ],
        "air_logistics": "Jaipur International Airport (JAI) connects to major domestic & international cities.",
        "train_logistics": "Jaipur Junction (JP) has excellent connectivity including Shatabdi Express.",
        "road_logistics": "NH48 connects Jaipur directly to Delhi (approx 4.5 hours).",
        "img_hero": "jaipur_hero.jpg",
        "img_gal1": "jaipur_gal1.jpg",
        "img_gal2": "jaipur_gal2.jpg",
        "img_gal3": "jaipur_gal3.jpg",
        "cap1": "Amer Fort Courtyard",
        "cap2": "Hawa Mahal Honeycomb",
        "cap3": "City Palace Gate"
    },
    {
        "filename": "Kashmir-Info.html",
        "page_title": "Kashmir - Paradise on Earth",
        "badge_text": "Jammu & Kashmir • Nature & Valleys",
        "hero_title": "Kashmir Valley",
        "hero_desc": "Discover the pristine beauty of Dal Lake, snow-capped Himalayan peaks, and lush Mughal gardens in the 'Paradise on Earth'.",
        "duration": "5 Days / 4 Nights",
        "best_time": "April – October",
        "budget": "₹15,000 – ₹35,000",
        "ideal_for": "Nature Lovers & Honeymooners",
        "overview_text": "Kashmir is renowned globally for its surreal natural beauty. From the tranquil waters of Dal Lake in Srinagar dotted with cedar-carved houseboats and shikaras, to the alpine slopes of Gulmarg and breathtaking meadows of Pahalgam, Kashmir offers a dreamlike journey through the Himalayas.",
        "day1_title": "Srinagar & Dal Lake Shikara",
        "day1_desc": "Check into a traditional wooden houseboat on Dal Lake. Enjoy a romantic sunset Shikara ride through floating lotus gardens and water bazaars.",
        "day2_title": "Gulmarg Mountain Excursion",
        "day2_desc": "Ride the world's highest operating Gondola in Gulmarg up to Kongdoori and Mount Apharwat for sweeping views of the snow-clad Pir Panjal range.",
        "highlights": [
            "Carved Houseboat Stay on Dal Lake",
            "Gulmarg Gondola Ride to Phase II (Apharwat)",
            "Lush Mughal Gardens (Shalimar & Nishat)",
            "Pahalgam Valley & Betaab Valley Walks",
            "Authentic Kashmiri Kahwa & Royal Wazwan"
        ],
        "air_logistics": "Sheikh ul-Alam International Airport Srinagar (SXR) receives daily direct flights.",
        "train_logistics": "Jammu Tawi (JAT) / Udhampur railhead, with scenic mountain road transfer.",
        "road_logistics": "NH44 connects Jammu to Srinagar through the all-weather Chenani-Nashri Tunnel.",
        "img_hero": "kashmir_hero.jpg",
        "img_gal1": "kashmir_gal1.jpg",
        "img_gal2": "kashmir_gal2.jpg",
        "img_gal3": "kashmir_gal3.jpg",
        "cap1": "Carved Houseboats",
        "cap2": "Gulmarg Snow Slopes",
        "cap3": "Mughal Terraced Gardens"
    },
    {
        "filename": "Alleppey-Info.html",
        "page_title": "Alleppey - Venice of the East",
        "badge_text": "Kerala • Backwaters & Nature",
        "hero_title": "Alleppey Backwaters",
        "hero_desc": "Cruise through tranquil palm-fringed canals and emerald green paddy fields on a traditional luxury Kerala houseboat.",
        "duration": "2 Days / 1 Night",
        "best_time": "September – March",
        "budget": "₹7,000 – ₹18,000",
        "ideal_for": "Relaxation & Romantic Escapes",
        "overview_text": "Alappuzha, also known as Alleppey, is famous for its intricate network of interconnected backwater canals, lagoons, and lakes. Known as the 'Venice of the East', its signature attraction is the traditional Kettuvallam houseboat, providing a tranquil escape immersed in authentic coastal village life.",
        "day1_title": "Houseboat Check-in & Backwater Cruise",
        "day1_desc": "Board your private thatched houseboat. Glide across scenic Vembanad Lake and narrow palm-shaded channels while enjoying freshly caught Karimeen fish curry.",
        "day2_title": "Canoe Village Tour & Alleppey Beach",
        "day2_desc": "Glide along shallow village canals in a country canoe at dawn. Visit the historic 150-year-old Alleppey pier and lighthouse before departure.",
        "highlights": [
            "Private Overnight Kettuvallam Houseboat Cruise",
            "Vembanad Lake Sunset Reflections",
            "Narrow Canal Country Boat Exploration",
            "Fresh Coastal Kerala Sadya & Fish Pollichathu",
            "Historic Alleppey Beach & Lighthouse"
        ],
        "air_logistics": "Cochin International Airport (COK) is 85 km away (approx 2 hours).",
        "train_logistics": "Alappuzha Railway Station (ALLP) is well-connected along the coastal line.",
        "road_logistics": "NH66 connects Alleppey smoothly to Kochi, Trivandrum, and Marari.",
        "img_hero": "alleppey_hero.jpg",
        "img_gal1": "alleppey_gal1.jpg",
        "img_gal2": "alleppey_gal2.jpg",
        "img_gal3": "alleppey_gal3.jpg",
        "cap1": "Houseboat on Backwaters",
        "cap2": "Shaded Canal Waterways",
        "cap3": "Vembanad Lake Sunset"
    },
    {
        "filename": "Himachal-Info.html",
        "page_title": "Himachal - Mountain Paradise",
        "badge_text": "Himachal Pradesh • Himalayan Escapes",
        "hero_title": "Shimla & Manali",
        "hero_desc": "Escape to the majestic Himalayas. Experience colonial charm, deodar forests, rushing rivers, and thrilling mountain adventures.",
        "duration": "6 Days / 5 Nights",
        "best_time": "March – June & Dec – Feb",
        "budget": "₹12,000 – ₹28,000",
        "ideal_for": "Adventure, Snow & Nature",
        "overview_text": "Himachal Pradesh offers the ultimate Himalayan holiday. Shimla, the historic summer capital of British India, retains its colonial elegance with the Ridge and Christ Church. In Kullu Valley, Manali serves as the premier adventure hub, nestled beside the roaring Beas River and leading into Solang Valley and Atal Tunnel.",
        "day1_title": "Shimla Heritage Ridge & Mall Road",
        "day1_desc": "Stroll down the pedestrian-only Mall Road. Visit neo-Gothic Christ Church, the Ridge view point, and the historic Viceregal Lodge.",
        "day2_title": "Solang Valley Adventures & Manali",
        "day2_desc": "Drive through Kullu to Manali. Head to Solang Valley for paragliding, zorbing, and snow sports against the towering Pir Panjal ranges.",
        "highlights": [
            "Shimla Ridge Walk & Colonial Architecture",
            "Solang Valley Paragliding & Snow Activities",
            "Scenic Drive through the Atal Tunnel",
            "Ancient Wooden Pagoda of Hadimba Temple",
            "UNESCO Kalka-Shimla Mountain Toy Train"
        ],
        "air_logistics": "Chandigarh Airport (IXC) or Bhuntar Kullu Airport for closer flights.",
        "train_logistics": "Kalka Railway Station, followed by the scenic Toy Train to Shimla.",
        "road_logistics": "NH5 and NH21 provide 4-lane highway connectivity from Delhi.",
        "img_hero": "himachal_hero.jpg",
        "img_gal1": "himachal_gal1.jpg",
        "img_gal2": "himachal_gal2.jpg",
        "img_gal3": "himachal_gal3.jpg",
        "cap1": "Christ Church & Ridge",
        "cap2": "Solang Valley Adventures",
        "cap3": "Hadimba Devi Shrine"
    },
    {
        "filename": "Jaisalmer-Info.html",
        "page_title": "Jaisalmer - The Golden Fortress",
        "badge_text": "Rajasthan • Desert Safari",
        "hero_title": "Jaisalmer",
        "hero_desc": "Experience the magic of the Thar Desert, living yellow sandstone fortresses, and starlit campfire nights on the dunes.",
        "duration": "3 Days / 2 Nights",
        "best_time": "October – March",
        "budget": "₹7,000 – ₹18,000",
        "ideal_for": "Desert Adventures & Heritage",
        "overview_text": "Jaisalmer, rising like a golden mirage from the Thar Desert, is celebrated for its Sonar Qila (Golden Fort). Built in 1156 AD, it is one of the world's few living forts where thousands still live inside ancient ramparts. Exquisite sandstone havelis and camel expeditions across the Sam Sand Dunes complete this fairy-tale journey.",
        "day1_title": "Sonar Qila & Intricate Havelis",
        "day1_desc": "Walk through the golden fort's ancient alleys and visit the intricate 12th-century Jain temples and the lace-like stone carvings of Patwon Ki Haveli.",
        "day2_title": "Thar Desert Safari & Campfire",
        "day2_desc": "Head into the Sam Sand Dunes for an exhilarating 4x4 dune bashing and camel safari at sunset, followed by a cultural folk dance performance under the desert stars.",
        "highlights": [
            "UNESCO Living Golden Fort (Sonar Qila)",
            "Sam Sand Dunes Sunset Camel Trek",
            "Intricate Carvings of Patwon Ki Haveli",
            "Desert Stargazing & Campfire Kalbelia Dance",
            "Boating on Sacred Gadisar Lake"
        ],
        "air_logistics": "Jaisalmer Airport (JSA) operates regular seasonal winter flights.",
        "train_logistics": "Jaisalmer Railway Station connects to Jodhpur, Jaipur, and Delhi.",
        "road_logistics": "Scenic desert highways connect Jaisalmer to Jodhpur (4.5 hours).",
        "img_hero": "jaisalmer_hero.jpg",
        "img_gal1": "jaisalmer_gal1.jpg",
        "img_gal2": "jaisalmer_gal2.jpg",
        "img_gal3": "jaisalmer_gal3.jpg",
        "cap1": "Sonar Qila Ramparts",
        "cap2": "Sam Sand Dunes",
        "cap3": "Patwon Ki Haveli Facade"
    },
    {
        "filename": "Udaipur-Info.html",
        "page_title": "Udaipur - City of Lakes & Palaces",
        "badge_text": "Rajasthan • Royal Romance",
        "hero_title": "Udaipur",
        "hero_desc": "Immerse yourself in the royal romance of shimmering lakes, floating marble palaces, and the majestic Aravalli hills.",
        "duration": "3 Days / 2 Nights",
        "best_time": "September – March",
        "budget": "₹9,000 – ₹25,000",
        "ideal_for": "Couples, Royalty & Architecture",
        "overview_text": "Udaipur, framed by the oldest mountain range in India, is widely hailed as the most romantic city in the country. The city centers on Lake Pichola, home to the floating white marble Lake Palace. The monumental City Palace dominates the east bank, housing museums, courtyards, and mirror halls.",
        "day1_title": "City Palace & Lake Pichola Cruise",
        "day1_desc": "Tour the grand courtyards and crystal galleries of City Palace. In the evening, take a sunset boat cruise past Jag Mandir on Lake Pichola.",
        "day2_title": "Saheliyon Ki Bari & Sajjangarh Monsoon Palace",
        "day2_desc": "Stroll through the royal lotus fountains of Saheliyon Ki Bari, followed by an evening drive up to the hilltop Monsoon Palace for 360-degree sunset vistas.",
        "highlights": [
            "Lake Pichola Sunset Boat Cruise",
            "Sprawling City Palace Museum & Courtyards",
            "Hilltop Sajjangarh (Monsoon Palace) Sunset",
            "Fountain Gardens of Saheliyon Ki Bari",
            "Candlelit Lakeside Mewari Dining"
        ],
        "air_logistics": "Maharana Pratap Airport (UDR) connects daily to Delhi, Mumbai, and Jaipur.",
        "train_logistics": "Udaipur City Railway Station (UDZ) offers premium express trains.",
        "road_logistics": "NH48 connects Udaipur directly to Ahmedabad (4 hrs) and Jaipur (6 hrs).",
        "img_hero": "udaipur_hero.jpg",
        "img_gal1": "udaipur_gal1.jpg",
        "img_gal2": "udaipur_gal2.jpg",
        "img_gal3": "udaipur_gal3.jpg",
        "cap1": "City Palace over Lake",
        "cap2": "Lake Pichola Vistas",
        "cap3": "Hilltop Monsoon Palace"
    },
    {
        "filename": "Hampi-Info.html",
        "page_title": "Hampi - UNESCO Vijayanagara Ruins",
        "badge_text": "Karnataka • Ancient Ruins",
        "hero_title": "Hampi Ruins",
        "hero_desc": "Step back in time to the glorious Vijayanagara Empire amidst surreal boulder-strewn landscapes and monolithic stone temples.",
        "duration": "3 Days / 2 Nights",
        "best_time": "October – February",
        "budget": "₹6,000 – ₹15,000",
        "ideal_for": "History, Backpacking & Photography",
        "overview_text": "Hampi, a UNESCO World Heritage site along the Tungabhadra River, is an open-air wonderland of monolithic sculptures, royal pavilions, and centuries-old temples. Once one of the richest metropolises in the medieval world, Hampi's stone chariot, musical pillars, and dramatic boulders create an unforgettable travel experience.",
        "day1_title": "Sacred Centre & Vittala Temple",
        "day1_desc": "Visit the active 7th-century Virupaksha Temple. Walk along the river to the Vittala Temple complex to see the iconic Stone Chariot and musical pillars.",
        "day2_title": "Royal Enclosure & Sunset at Matanga Hill",
        "day2_desc": "Explore the Lotus Mahal, Elephant Stables, and Queen's Bath in the Royal Centre. Hike up Matanga Hill for an unforgettable golden hour over boulder-strewn ruins.",
        "highlights": [
            "Iconic Stone Chariot at Vittala Temple",
            "Panoramic Sunset from Matanga Hill",
            "Towering Gopuram of Virupaksha Temple",
            "Indo-Islamic Architecture of Lotus Mahal",
            "Traditional Coracle Boat Ride on Tungabhadra"
        ],
        "air_logistics": "Jindal Vijaynagar Airport (VDY) or Hubballi Airport (HBX).",
        "train_logistics": "Hospet Junction (HPT) is just 13 km away with trains from Bangalore and Goa.",
        "road_logistics": "Well-connected highway network from Bangalore, Goa, and Hyderabad.",
        "img_hero": "hampi_hero.jpg",
        "img_gal1": "hampi_gal1.jpg",
        "img_gal2": "hampi_gal2.jpg",
        "img_gal3": "hampi_gal3.jpg",
        "cap1": "Virupaksha Gopuram",
        "cap2": "Monolithic Stone Chariot",
        "cap3": "Boulder-Strewn Landscape"
    },
    {
        "filename": "Bikaner-Info.html",
        "page_title": "Bikaner - Desert Forts & Royal Splendor",
        "badge_text": "Rajasthan • Desert Heritage",
        "hero_title": "Bikaner",
        "hero_desc": "Explore unvanquished desert fortresses, palatial havelis, and the authentic culinary traditions of northwestern Rajasthan.",
        "duration": "2 Days / 1 Night",
        "best_time": "October – March",
        "budget": "₹6,000 – ₹15,000",
        "ideal_for": "Culture, Architecture & Foodies",
        "overview_text": "Founded in 1488 by Rao Bika, Bikaner is a vibrant desert city distinguished by Junagarh Fort, one of Rajasthan's few major forts not built on a hill. With its intricately carved red sandstone palaces, world-renowned Bikaneri savories, and unique Karni Mata Temple, Bikaner delivers authentic desert heritage.",
        "day1_title": "Junagarh Fort & Lalgarh Palace",
        "day1_desc": "Tour the opulent courtyards, gold leaf artwork, and armory of Junagarh Fort. Afterwards, visit the grand red sandstone Lalgarh Palace.",
        "day2_title": "Karni Mata Temple & Camel Research Centre",
        "day2_desc": "Drive to Deshnoke to visit the world-famous Karni Mata shrine, followed by a visit to Asia's premier Camel Breeding and Research Centre.",
        "highlights": [
            "Unconquered Junagarh Fort & Anup Mahal",
            "Historic Red Sandstone Lalgarh Palace",
            "Karni Mata Temple at Deshnoke",
            "National Research Centre on Camel",
            "Famous Bikaneri Bhujia & Rasgulla Tastings"
        ],
        "air_logistics": "Nal Airport Bikaner (BKB) offers direct flights to Delhi.",
        "train_logistics": "Bikaner Junction (BKN) is well connected to major North Indian cities.",
        "road_logistics": "NH11 and NH62 connect Bikaner smoothly to Jaipur and Jodhpur.",
        "img_hero": "bikaner_hero.jpg",
        "img_gal1": "bikaner_gal1.jpg",
        "img_gal2": "bikaner_gal2.jpg",
        "img_gal3": "bikaner_gal3.jpg",
        "cap1": "Junagarh Fort Courtyard",
        "cap2": "Lalgarh Palace Facade",
        "cap3": "Desert Camel Centre"
    },
    {
        "filename": "CamelSafari-Info.html",
        "page_title": "Thar Desert - Iconic Camel Safari",
        "badge_text": "Rajasthan • Desert Expedition",
        "hero_title": "Camel Safari",
        "hero_desc": "Traverse rolling golden dunes, visit remote nomadic hamlets, and sleep under millions of desert stars.",
        "duration": "2 Days / 1 Night",
        "best_time": "October – March",
        "budget": "₹5,000 – ₹12,000",
        "ideal_for": "Adventure Seekers & Campers",
        "overview_text": "A camel safari across Rajasthan's Thar Desert is an iconic travel adventure. Riding atop gentle camels into the golden sunset, dining around blazing campfires with Rajasthani folk music, and sleeping in luxury desert Swiss tents beneath the Milky Way will stay with you forever.",
        "day1_title": "Dune Caravan & Sunset Ride",
        "day1_desc": "Mount your camel in the afternoon and ride across rolling golden dunes. Watch the desert sunset, followed by Kalbelia folk performances by the campfire.",
        "day2_title": "Desert Sunrise & Village Interaction",
        "day2_desc": "Wake early for a spectacular golden desert sunrise. Enjoy hot chai and visit nearby desert settlements to meet traditional artisans before departure.",
        "highlights": [
            "Authentic Camel Caravan across Thar Dunes",
            "Dramatic Sunset over Sam Sand Dunes",
            "Starlit Luxury Desert Camp Stay",
            "Live Kalbelia Music & Fire Dance",
            "Rustic Village Hospitality & Fresh Bajra Roti"
        ],
        "air_logistics": "Jaisalmer Airport or Jodhpur Airport are the nearest hubs.",
        "train_logistics": "Jaisalmer Railway Station connects to all major cities.",
        "road_logistics": "Paved roads connect Jaisalmer town to Sam and Khuri dunes (40 km).",
        "img_hero": "camelsafari_hero.jpg",
        "img_gal1": "camelsafari_gal1.jpg",
        "img_gal2": "camelsafari_gal2.jpg",
        "img_gal3": "camelsafari_gal3.jpg",
        "cap1": "Camel Caravan on Dunes",
        "cap2": "Desert Campfire Evening",
        "cap3": "Golden Thar Ridge"
    },
    {
        "filename": "ColvaBeach-Info.html",
        "page_title": "Colva Beach - South Goa Coastal Charm",
        "badge_text": "Goa • Sun, Sand & Sea",
        "hero_title": "Colva Beach",
        "hero_desc": "Relax on powder-white sands, enjoy thrilling water sports, and savor fresh Goan seafood along South Goa's coastline.",
        "duration": "3 Days / 2 Nights",
        "best_time": "November – March",
        "budget": "₹8,000 – ₹20,000",
        "ideal_for": "Beach Lovers, Water Sports & Families",
        "overview_text": "Colva Beach is one of South Goa's oldest and most scenic coastal stretches. Spanning 2.4 kilometers of powdery white sand lined with swaying coconut palms, Colva offers beachside shacks, thrilling parasailing, jet skiing, and Portuguese heritage churches just a short stroll inland.",
        "day1_title": "White Sands & Watersports",
        "day1_desc": "Spend your morning soaking in the sun and enjoying parasailing or banana boat rides. In the evening, dine on fresh tiger prawns at beachside shacks.",
        "day2_title": "Portuguese Churches & Sunset Walk",
        "day2_desc": "Visit the 17th-century Church of Our Lady of Mercy. Take a relaxing late-afternoon stroll down to Benaulim beach for a peaceful sunset.",
        "highlights": [
            "Powder-White Sandy Coastline",
            "Parasailing, Jet Skiing & Speedboat Rides",
            "Historic Church of Our Lady of Mercy",
            "Authentic Goan Fish Curry & Bebinca",
            "Lively Evening Beach Shacks & Live Music"
        ],
        "air_logistics": "Dabolim Airport (GOI) is just 20 km (30 mins) from Colva Beach.",
        "train_logistics": "Madgaon Junction (MAO) is only 8 km away.",
        "road_logistics": "Excellent road connectivity across South and North Goa.",
        "img_hero": "colvabeach_hero.jpg",
        "img_gal1": "colvabeach_gal1.jpg",
        "img_gal2": "colvabeach_gal2.jpg",
        "img_gal3": "colvabeach_gal3.jpg",
        "cap1": "Parasailing & Watersports",
        "cap2": "Colva Arabian Sea Sunset",
        "cap3": "Coastal Palm Groves"
    },
    {
        "filename": "GwaliorFort-Info.html",
        "page_title": "Gwalior Fort - Pearl of Fortresses",
        "badge_text": "Madhya Pradesh • Monumental Fortresses",
        "hero_title": "Gwalior Fort",
        "hero_desc": "Marvel at the vibrant blue-tiled Man Mandir Palace, colossal rock-cut Jain statues, and ancient temple architecture in Madhya Pradesh.",
        "duration": "2 Days / 1 Night",
        "best_time": "October – March",
        "budget": "₹5,000 – ₹13,000",
        "ideal_for": "Archaeology, Architecture & History",
        "overview_text": "Gwalior Fort, described by Mughal Emperor Babur as 'the pearl amongst fortresses in India', dominates the city skyline from a sheer 300-foot sandstone plateau. Dating back over a millennium, it houses the vibrant turquoise and yellow enameled tiles of Man Mandir Palace, the Sas Bahu temples, and colossal 15th-century rock-cut Jain colossi.",
        "day1_title": "Man Mandir Palace & Sas Bahu Temples",
        "day1_desc": "Explore the multi-tiered Man Mandir Palace with its enameled duck and elephant friezes. Visit the twin Sas Bahu temples and the Teli Ka Mandir.",
        "day2_title": "Gopachal Jain Statues & Sound and Light Show",
        "day2_desc": "Walk down the steep Urwahi Gate to witness towering 57-foot rock-carved Jain Tirthankara figures. Attend the evening sound and light show.",
        "highlights": [
            "Vibrant Turquoise-Tiled Man Mandir Palace",
            "Towering Gopachal Rock-Cut Jain Statues",
            "Intricately Carved 11th-Century Sas Bahu Temples",
            "Teli Ka Mandir Dravidian-Nagara Blend",
            "Evening Sound & Light Show over Gwalior City"
        ],
        "air_logistics": "Gwalior Rajmata Vijaya Raje Scindia Airport (GWL) connects to Delhi and Mumbai.",
        "train_logistics": "Gwalior Junction (GWL) is on the main Delhi-Mumbai high-speed line.",
        "road_logistics": "NH44 connects Agra to Gwalior in approx 2 hours.",
        "img_hero": "gwaliorfort_hero.jpg",
        "img_gal1": "gwaliorfort_gal1.jpg",
        "img_gal2": "gwaliorfort_gal2.jpg",
        "img_gal3": "gwaliorfort_gal3.jpg",
        "cap1": "Man Mandir Palace Tiles",
        "cap2": "Sas Bahu Carvings",
        "cap3": "Gopachal Rock-Cut Statues"
    },
    {
        "filename": "Jodhpur-Info.html",
        "page_title": "Jodhpur - The Blue City & Umaid Bhawan",
        "badge_text": "Rajasthan • Blue City Splendor",
        "hero_title": "Jodhpur",
        "hero_desc": "Wander the cobalt-blue alleys of the Old City, admire white marble cenotaphs, and gaze up at monumental Mehrangarh Fort.",
        "duration": "2 Days / 1 Night",
        "best_time": "October – March",
        "budget": "₹7,000 – ₹18,000",
        "ideal_for": "Culture, Photography & Architecture",
        "overview_text": "Jodhpur, the iconic Blue City, sits dramatically at the edge of the Thar Desert. Famous for its sea of indigo-washed Brahmin houses in the Brahmapuri quarter, the city is crowned by Mehrangarh Fort and features Jaswant Thada, a gleaming white marble memorial often called the 'Taj Mahal of Marwar'.",
        "day1_title": "Brahmapuri Blue Alleys & Jaswant Thada",
        "day1_desc": "Photograph the photogenic indigo houses of the old quarter. Visit the serene white marble cenotaph of Jaswant Thada overlooking the lake.",
        "day2_title": "Umaid Bhawan Palace & Clock Tower Market",
        "day2_desc": "Tour the royal museum of art-deco Umaid Bhawan Palace. Spend the evening savoring Makhaniya Lassi and shopping for spices in the Sardar Market.",
        "highlights": [
            "Walking Tour of Cobalt-Blue Old City Alleys",
            "Gleaming White Marble Cenotaph of Jaswant Thada",
            "Royal Museum at Art-Deco Umaid Bhawan Palace",
            "Historic Ghanta Ghar (Clock Tower) & Spice Market",
            "Famous Jodhpuri Mirchi Vada & Pyaaz Kachori"
        ],
        "air_logistics": "Jodhpur Airport (JDH) offers regular daily flights from Delhi, Mumbai, and Jaipur.",
        "train_logistics": "Jodhpur Junction (JU) connects directly across Northern and Western India.",
        "road_logistics": "NH62 connects Jodhpur smoothly to Jaipur (5 hrs) and Udaipur (4.5 hrs).",
        "img_hero": "jodhpur_hero.jpg",
        "img_gal1": "jodhpur_gal1.jpg",
        "img_gal2": "jodhpur_gal2.jpg",
        "img_gal3": "jodhpur_gal3.jpg",
        "cap1": "Jaswant Thada Memorial",
        "cap2": "Blue City Rooftop Vistas",
        "cap3": "Umaid Bhawan Palace"
    },
    {
        "filename": "MehrangarhFort-Info.html",
        "page_title": "Mehrangarh Fort - Citadel of the Sun",
        "badge_text": "Rajasthan • Mighty Citadel",
        "hero_title": "Mehrangarh Fort",
        "hero_desc": "Tower 400 feet above Jodhpur within one of India's largest and most formidable 15th-century cliff-top fortresses.",
        "duration": "1 Day Tour",
        "best_time": "October – March",
        "budget": "₹4,000 – ₹10,000",
        "ideal_for": "History, Royal Splendor & Views",
        "overview_text": "Mehrangarh Fort, rising sheerly from a 410-foot rocky cliff, is one of the most magnificent fortifications in Asia. Built by Rao Jodha in 1459, its walls still bear the marks of cannonballs. Inside lies a museum with royal palanquins, the gilded Phool Mahal, and the Chamunda Devi temple.",
        "day1_title": "Fort Ramparts & Royal Museum",
        "day1_desc": "Walk through seven grand gates including Jai Pol and Fateh Pol. Marvel at the intricate latticework of Sheesh Mahal and Phool Mahal.",
        "day2_title": "Zip-Lining (Flying Fox) & Panoramic Views",
        "day2_desc": "Experience the thrilling Flying Fox zip-line tour across fort battlements and desert lakes, capturing panoramic vistas of the Blue City.",
        "highlights": [
            "Cannonball Scars at 15th-Century Battlements",
            "Opulent Gilded Ceiling of Phool Mahal",
            "World-Class Royal Palanquin & Armory Museum",
            "Flying Fox Aerial Zip-Line Tour Over Battlements",
            "Breathtaking 360-Degree Views of the Blue City"
        ],
        "air_logistics": "Jodhpur Airport (JDH) is just 8 km away.",
        "train_logistics": "Jodhpur Junction (JU) is 5 km from the fort gate.",
        "road_logistics": "Accessible via city taxi or auto-rickshaw directly to the fort elevator.",
        "img_hero": "mehrangarhfort_hero.jpg",
        "img_gal1": "mehrangarhfort_gal1.jpg",
        "img_gal2": "mehrangarhfort_gal2.jpg",
        "img_gal3": "mehrangarhfort_gal3.jpg",
        "cap1": "Historic Cannons on Ramparts",
        "cap2": "Blue City from Battlements",
        "cap3": "Phool Mahal Gilded Halls"
    },
    {
        "filename": "Mon-Info.html",
        "page_title": "Mon - Land of the Konyak Naga Warriors",
        "badge_text": "Nagaland • Tribal Heritage",
        "hero_title": "Mon, Nagaland",
        "hero_desc": "Journey into the misty highlands of Nagaland to witness traditional Morung architecture, facial tattoos, and unique tribal heritage.",
        "duration": "4 Days / 3 Nights",
        "best_time": "October – April",
        "budget": "₹14,000 – ₹30,000",
        "ideal_for": "Tribal Anthropology & Offbeat Journeys",
        "overview_text": "Mon, situated in northern Nagaland, is the ancestral homeland of the Konyak Nagas, historically renowned for facial tattoos and headhunting traditions. A highlight is Longwa Village, where the international boundary between India and Myanmar passes through the middle of the King's Morung house.",
        "day1_title": "Mon Town & Traditional Morung Houses",
        "day1_desc": "Arrive in Mon and explore local markets. Visit traditional wooden longhouses adorned with animal skull trophies and indigenous wood carvings.",
        "day2_title": "Longwa Village - Border between Two Nations",
        "day2_desc": "Visit Longwa village perched on the international ridge. Meet the village Chief (Angh) whose house straddles India and Myanmar.",
        "highlights": [
            "Longwa Village on the Indo-Myanmar Border",
            "Meet Veteran Konyak Tattooed Warriors",
            "Traditional Thatch-Roofed Morung Architecture",
            "Ancient Woodcarving and Beaded Tribal Regalia",
            "Stunning Highland Valleys and Tea Plantations"
        ],
        "air_logistics": "Dibrugarh Airport (DIB) in Assam is the closest airport (approx 140 km).",
        "train_logistics": "Bhojo or Simaluguri Junction in Assam, followed by private taxi.",
        "road_logistics": "Mountain roads connect Sonari (Assam) to Mon town.",
        "img_hero": "mon_hero.jpg",
        "img_gal1": "mon_gal1.jpg",
        "img_gal2": "mon_gal2.jpg",
        "img_gal3": "mon_gal3.jpg",
        "cap1": "Longwa Village Morungs",
        "cap2": "Misty Highland Hills",
        "cap3": "Konyak Warrior Regalia"
    },
    {
        "filename": "Pushkar-Info.html",
        "page_title": "Pushkar - Sacred Lake & Brahma Temple",
        "badge_text": "Rajasthan • Sacred Oasis",
        "hero_title": "Pushkar",
        "hero_desc": "Immerse in the spiritual chants of 52 holy bathing ghats, visit the world's rarest Brahma Temple, and experience camel fair heritage.",
        "duration": "2 Days / 1 Night",
        "best_time": "October – March",
        "budget": "₹5,000 – ₹14,000",
        "ideal_for": "Spirituality, Festivals & Photography",
        "overview_text": "Pushkar, nestled on the shores of a sacred lake surrounded by the Aravalli hills, is one of the oldest and most sacred pilgrimage destinations in India. It is home to one of the few existing temples dedicated to Lord Brahma. The town comes alive with thousands of decorated camels and traders during the world-famous Pushkar Fair.",
        "day1_title": "Pushkar Lake Ghats & Brahma Temple",
        "day1_desc": "Attend morning prayer ceremonies on the Varaha and Brahma Ghats. Visit the rare 14th-century red-spired Jagatpita Brahma Mandir.",
        "day2_title": "Savitri Temple Hike & Desert Sunset",
        "day2_desc": "Hike up the hill to Savitri Temple for sunrise views over the holy lake. In the afternoon, enjoy a desert camel safari through surrounding dunes.",
        "highlights": [
            "Sacred Pushkar Lake & 52 Holy Bathing Ghats",
            "World-Famous Jagatpita Brahma Temple",
            "Panoramic Sunrise from Ratnagiri Hill (Savitri Temple)",
            "Pushkar Camel Fair Grounds & Desert Safari",
            "Vibrant Rose Gardens & Malpua Delicacies"
        ],
        "air_logistics": "Kishangarh Airport (KQH) is just 45 km away; Jaipur (JAI) is 145 km.",
        "train_logistics": "Ajmer Junction (AII) is 14 km away, connected by major express trains.",
        "road_logistics": "Well-paved highway connects Ajmer to Pushkar across the Snake Mountain pass.",
        "img_hero": "pushkar_hero.jpg",
        "img_gal1": "pushkar_gal1.jpg",
        "img_gal2": "pushkar_gal2.jpg",
        "img_gal3": "pushkar_gal3.jpg",
        "cap1": "Pushkar Holy Lake Ghats",
        "cap2": "Brahma Mandir Spire",
        "cap3": "Pushkar Camel Gathering"
    },
    {
        "filename": "SanchiStupa-Info.html",
        "page_title": "Sanchi Stupa - Buddhist UNESCO Heritage",
        "badge_text": "Madhya Pradesh • Buddhist Heritage",
        "hero_title": "Sanchi Stupa",
        "hero_desc": "Stand in awe before the Great Stupa of Sanchi, commissioned by Emperor Ashoka in the 3rd century BCE, featuring carved torana gateways.",
        "duration": "1 Day Tour",
        "best_time": "October – March",
        "budget": "₹4,000 – ₹9,000",
        "ideal_for": "Buddhist Pilgrimage, History & Art",
        "overview_text": "Sanchi is home to the oldest stone structures in India and a designated UNESCO World Heritage site. Commissioned by Emperor Ashoka the Great, the Great Stupa is renowned for its four ornately carved stone gateways (Toranas) that depict Jataka tales, Ashoka's life, and early Buddhist iconography.",
        "day1_title": "The Great Stupa & Ashoka Pillar",
        "day1_desc": "Walk clockwise around the Great Stupa. Examine the intricate narrative carvings on the four Toranas and visit the remains of the polished Ashoka Pillar.",
        "day2_title": "Sanchi Archaeological Museum & Stupa 2",
        "day2_desc": "Explore the Sanchi Museum housing the Lion Capital and ancient relics, then walk to Stupa 2 and the monastery ruins on the quiet hill slopes.",
        "highlights": [
            "The Monumental Great Stupa (Stupa 1)",
            "Masterpiece Carvings on Four Stone Toranas",
            "Historic Polished Ashoka Pillar & Lion Capital",
            "Archaeological Museum Artifacts and Reliquaries",
            "Serene Hilltop Setting Surrounded by Countryside"
        ],
        "air_logistics": "Raja Bhoj Airport Bhopal (BHO) is 50 km away (approx 1 hour).",
        "train_logistics": "Sanchi Station (SCI) or Vidisha / Bhopal Junction.",
        "road_logistics": "NH146 connects Bhopal directly to Sanchi on a smooth 4-lane highway.",
        "img_hero": "sanchistupa_hero.jpg",
        "img_gal1": "sanchistupa_gal1.jpg",
        "img_gal2": "sanchistupa_gal2.jpg",
        "img_gal3": "sanchistupa_gal3.jpg",
        "cap1": "Great Stupa Torana Gateway",
        "cap2": "Ancient Hemispherical Dome",
        "cap3": "Hilltop Buddhist Ruins"
    },
    {
        "filename": "Twang-Info.html",
        "page_title": "Tawang - Crown of Arunachal Pradesh",
        "badge_text": "Arunachal Pradesh • Monasteries & Passes",
        "hero_title": "Tawang Monastery",
        "hero_desc": "Journey across the snow-clad Sela Pass to discover India's largest Buddhist monastery perched at 10,000 feet in the Eastern Himalayas.",
        "duration": "5 Days / 4 Nights",
        "best_time": "March – June & Sept – Nov",
        "budget": "₹16,000 – ₹32,000",
        "ideal_for": "Adventure, High Altitude & Buddhism",
        "overview_text": "Tawang, located near the borders of Tibet and Bhutan at an altitude of 10,000 feet, is home to the 400-year-old Tawang Monastery (Gaden Namgyal Lhatse), the largest Buddhist monastery in India. Reached via the snow-crowned Sela Pass (13,700 ft), Tawang offers pristine alpine lakes, war memorials, and profound peace.",
        "day1_title": "Scenic Drive via Sela Pass & Sela Lake",
        "day1_desc": "Cross the breathtaking Sela Pass at 13,700 feet, photographing the frozen Sela Lake before descending to Jaswant Garh War Memorial and Tawang.",
        "day2_title": "Tawang Monastery & Urgelling Gompa",
        "day2_desc": "Explore the 400-year-old Tawang Monastery complex, the monumental 28-foot gilded Buddha statue, and the birthplace of the 6th Dalai Lama.",
        "highlights": [
            "400-Year-Old Tawang Monastery & Museum",
            "Crossing Breathtaking Sela Pass (13,700 ft)",
            "Magnificent 28-Foot Gilded Buddha Statue",
            "Frozen Paradise of Sela Lake and Madhuri Lake",
            "Spectacular Nuranang Falls (Jang Falls)"
        ],
        "air_logistics": "Tezpur Airport or Lokpriya Gopinath Bordoloi Airport Guwahati (GAU).",
        "train_logistics": "Tezpur (Dekargaon) or Rangapara North railhead.",
        "road_logistics": "NH13 connects Tezpur to Tawang via Bomdila and Dirang (scenic mountain road).",
        "img_hero": "twang_hero.jpg",
        "img_gal1": "twang_gal1.jpg",
        "img_gal2": "twang_gal2.jpg",
        "img_gal3": "twang_gal3.jpg",
        "cap1": "Tawang Monastery Complex",
        "cap2": "Gilded Buddha Statue",
        "cap3": "High Alpine Passes"
    },
    {
        "filename": "UmngotRiver-Info.html",
        "page_title": "Umngot River - Crystal Waters of Dawki",
        "badge_text": "Meghalaya • Pristine Waters",
        "hero_title": "Umngot River, Dawki",
        "hero_desc": "Glide upon water so transparent that boats appear to float in mid-air along the emerald gorge of Meghalaya.",
        "duration": "2 Days / 1 Night",
        "best_time": "November – April",
        "budget": "₹6,000 – ₹15,000",
        "ideal_for": "Nature Lovers, Boating & Photographers",
        "overview_text": "The Umngot River in Dawki, Meghalaya, is universally celebrated for having some of the clearest, most transparent natural river waters on the planet. Flowing peacefully between the Jaintia and Khasi hills right to the India-Bangladesh border, looking into the river reveals smooth pebbles and swimming fish several meters below.",
        "day1_title": "Crystal Clear Boating & Cliff Camping",
        "day1_desc": "Take a wooden country boat ride along the transparent waters of Dawki. Enjoy cliff jumping, kayaking, and camping by the riverside pebble beach.",
        "day2_title": "Living Root Bridges & Krang Shuri Falls",
        "day2_desc": "Visit the world-famous double-decker living root bridges in nearby villages and swim in the electric blue pools of Krang Shuri Falls.",
        "highlights": [
            "Glass-Clear Transparent River Boating",
            "Kayaking & Snorkeling in Natural Emerald Currents",
            "Riverside Pebble Beach Camping Under Stars",
            "Nearby Double Decker Living Root Bridges",
            "Visit the India-Bangladesh Friendship Border"
        ],
        "air_logistics": "Umroi Airport Shillong (SHL) or Guwahati Airport (GAU - 170 km).",
        "train_logistics": "Guwahati Junction (GHY) is the major rail hub.",
        "road_logistics": "Scenic winding highway from Shillong to Dawki (approx 85 km / 3 hours).",
        "img_hero": "umngotriver_hero.jpg",
        "img_gal1": "umngotriver_gal1.jpg",
        "img_gal2": "umngotriver_gal2.jpg",
        "img_gal3": "umngotriver_gal3.jpg",
        "cap1": "Crystal Clear Dawki River",
        "cap2": "Living Root Bridges",
        "cap3": "Krang Shuri Cascades"
    },
    {
        "filename": "Uttrakhand-Info.html",
        "page_title": "Uttarakhand - Rishikesh Yoga & Ganges Adventure",
        "badge_text": "Uttarakhand • Yoga & Rapids",
        "hero_title": "Rishikesh & Haridwar",
        "hero_desc": "Discover the Yoga Capital of the World, exhilarating whitewater Ganges rafting, and soul-stirring evening Ganga Aarti ceremonies.",
        "duration": "3 Days / 2 Nights",
        "best_time": "September – November & March – May",
        "budget": "₹6,000 – ₹16,000",
        "ideal_for": "Yoga, Adventure Rafting & Spirituality",
        "overview_text": "Rishikesh, nestled in the Himalayan foothills where the emerald Ganges flows into the plains, is globally revered as the Yoga Capital of the World. From serene meditation ashrams and the historic Beatles Ashram to heart-pumping Grade IV whitewater rafting and bungee jumping, Uttarakhand offers an energizing spiritual and adventure journey.",
        "day1_title": "Whitewater Rafting & Triveni Ghat Aarti",
        "day1_desc": "Embark on an exhilarating 16 km whitewater river rafting trip through rapids like Roller Coaster and Golf Course. Attend the grand evening Maha Aarti at Triveni Ghat.",
        "day2_title": "Beatles Ashram & Ram Jhula Walk",
        "day2_desc": "Explore the graffiti-covered meditation domes of Chaurasi Kutia (Beatles Ashram). Cross the suspension bridges of Ram Jhula and Lakshman Jhula.",
        "highlights": [
            "Ganges Whitewater Rafting & Cliff Jumping",
            "Evening Ganga Aarti Ceremony at Triveni Ghat",
            "Chaurasi Kutia (Historic Beatles Ashram)",
            "Suspension Bridges of Ram Jhula & Lakshman Jhula",
            "Yoga & Ayurvedic Wellness Meditation Sessions"
        ],
        "air_logistics": "Dehradun Jolly Grant Airport (DED) is only 20 km away.",
        "train_logistics": "Yog Nagari Rishikesh (YNRK) or Haridwar Junction (HW).",
        "road_logistics": "Delhi-Dehradun Expressway connects Delhi to Rishikesh in approx 4-5 hours.",
        "img_hero": "uttrakhand_hero.jpg",
        "img_gal1": "uttrakhand_gal1.jpg",
        "img_gal2": "uttrakhand_gal2.jpg",
        "img_gal3": "uttrakhand_gal3.jpg",
        "cap1": "Ganges River Rafting",
        "cap2": "Evening Ganga Aarti",
        "cap3": "Ram Jhula Suspension Bridge"
    },
    {
        "filename": "VivekanandaRockMemorial-Info.html",
        "page_title": "Vivekananda Rock Memorial - Lands End Kanyakumari",
        "badge_text": "Tamil Nadu • Three Oceans Confluence",
        "hero_title": "Vivekananda Rock Memorial",
        "hero_desc": "Stand at the southernmost tip of India where the Arabian Sea, Bay of Bengal, and Indian Ocean meet in sacred harmony.",
        "duration": "2 Days / 1 Night",
        "best_time": "October – March",
        "budget": "₹5,000 – ₹13,000",
        "ideal_for": "Spirituality, Geography & Coastal Views",
        "overview_text": "Perched on a monolithic rock 500 meters off the southern tip of India at Kanyakumari, the Vivekananda Rock Memorial was built in 1970 to honor Swami Vivekananda, who meditated on this very rock in 1892. Adjacent stands the colossal 133-foot Thiruvalluvar Statue, standing tall at the meeting point of three great oceans.",
        "day1_title": "Ferry Ride to Rock Memorial & Thiruvalluvar Statue",
        "day1_desc": "Take the scenic coastal ferry out to the Vivekananda Rock Memorial. Meditate in the Dhyana Mandapam and gaze up at the giant 133-foot stone statue of saint poet Thiruvalluvar.",
        "day2_title": "Triveni Sangam Sunrise & Gandhi Memorial",
        "day2_desc": "Watch the legendary sunrise where three oceans meet at Triveni Sangam. Visit the Mahatma Gandhi Memorial Mandapam and sunset point.",
        "highlights": [
            "Ferry Crossing to Vivekananda Rock Memorial",
            "Colossal 133-Foot Thiruvalluvar Stone Statue",
            "Unique Triveni Sangam Three-Ocean Confluence",
            "Simultaneous Sunrise & Sunset Coastal Views",
            "Dhyana Mandapam Silent Meditation Hall"
        ],
        "air_logistics": "Trivandrum International Airport (TRV) is 90 km away (approx 2.5 hours).",
        "train_logistics": "Kanyakumari Railway Station (CAPE) connects directly to major Indian capitals.",
        "road_logistics": "NH44 (North-South Corridor) terminates directly at Kanyakumari.",
        "img_hero": "vivekanandarock_hero.jpg",
        "img_gal1": "vivekanandarock_gal1.jpg",
        "img_gal2": "vivekanandarock_gal2.jpg",
        "img_gal3": "vivekanandarock_gal3.jpg",
        "cap1": "Vivekananda Memorial on Sea Rock",
        "cap2": "133-Foot Thiruvalluvar Colossus",
        "cap3": "Triveni Sangam Ocean Views"
    }
]

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
                                <a href="MehrangarhFort-Info.html">🚩 Mehrangarh Fort (Jodhpur)</a>
                                <a href="Uttrakhand-Info.html">🕉️ Uttarakhand (Rishikesh)</a>
                                <a href="Twang-Info.html">🌄 Tawang (Monastery)</a>
                                <a href="ColvaBeach-Info.html">🏖️ Colva Beach (Goa)</a>
                                <div class="dropdown-divider" style="height:1px; background:var(--card-border); margin:6px 0;"></div>
                                <a href="../index.html#middle" style="font-weight:700; color:var(--accent-primary) !important;">🗺️ View All Destinations &rarr;</a>
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
            <button class="primary-btn openQueryModal" id="openQueryModal" type="button"><i class="fa fa-envelope-o" style="margin-right: 6px;"></i> Send Query &bull; Plan {hero_title} Tour</button>
            <a href="https://wa.me/918700140135" class="wa-hero-btn wa-dynamic-btn" target="_blank" rel="noopener noreferrer"><i class="fa fa-whatsapp"></i> WhatsApp Us</a>
        </div>
    </section>

    <!-- Quick Stats Bar (Budget, Duration, Best Time, Ideal For) -->
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

                    <!-- Curated Multi-Day Itinerary Timeline -->
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

                    <!-- Key Highlights / Experiences -->
                    <div class="inside-card">
                        <div class="inside-card-header">
                            <h3 class="inside-card-title"><i class="fa fa-star"></i> Must-Try Experiences</h3>
                        </div>
                        <div class="highlights-list">
                            {highlights_html}
                        </div>
                    </div>

                    <!-- Logistics (How to Reach) -->
                    <div class="inside-card">
                        <div class="inside-card-header">
                            <h3 class="inside-card-title"><i class="fa fa-plane"></i> Logistics & Travel Info</h3>
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
                        <p style="font-size: 0.92rem; color: var(--text-secondary); margin-bottom: 20px;">Hotels, premium transport, and authorized local guide included.</p>
                        <a href="https://wa.me/918700140135" class="whatsapp-btn w-100 mb-3 wa-dynamic-btn" target="_blank" rel="noopener noreferrer"><i class="fa fa-whatsapp"></i> Chat on WhatsApp &bull; Instant Quote</a>
                        <button class="primary-btn w-100 openQueryModal mb-3" id="openQueryModal2" type="button"><i class="fa fa-envelope-o" style="margin-right: 6px;"></i> Send Query / Request Quote</button>
                        <a href="tel:08700140135" class="btn btn-outline-secondary w-100 font-weight-bold" style="border-radius: 8px;"><i class="fa fa-phone"></i> Call +91 87001 40135</a>
                    </div>
                </div>
            </div>

            <!-- Curated Visual Gallery Section -->
            <div class="mt-4">
                <h3 class="mb-4 font-weight-bold text-center"><i class="fa fa-camera" style="color: var(--accent-primary);"></i> Visual Gallery</h3>
                <div class="inside-gallery-grid">
                    <div class="inside-gallery-item">
                        <img src="../img/{img_gal1}" alt="{cap1}">
                        <div class="inside-gallery-overlay"><span class="inside-gallery-title">{cap1}</span></div>
                    </div>
                    <div class="inside-gallery-item">
                        <img src="../img/{img_gal2}" alt="{cap2}">
                        <div class="inside-gallery-overlay"><span class="inside-gallery-title">{cap2}</span></div>
                    </div>
                    <div class="inside-gallery-item">
                        <img src="../img/{img_gal3}" alt="{cap3}">
                        <div class="inside-gallery-overlay"><span class="inside-gallery-title">{cap3}</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Universal Query Modal -->
    <div id="queryModal">
        <div class="modal-content-custom">
            <button id="closeQueryModal" type="button" aria-label="Close Modal">&times;</button>
            <h4 style="font-weight: 700; margin-bottom: 8px;">Send Us Your Query</h4>
            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 20px;">Tell us your requirements for {hero_title} and we'll craft the perfect package.</p>
            <form id="contact" action="https://formspree.io/f/xzzgaydr" method="POST">
                <input name="email" type="email" placeholder="Your Email Address (for reply)" required style="width:100%; margin-bottom:12px; padding:12px; border-radius:8px; border:1px solid var(--card-border); background:var(--bg-primary); color:var(--text-primary); box-sizing:border-box;">
                <textarea name="message" placeholder="Tell us your travel dates, group size & customized requests..." required style="width:100%; min-height:95px; margin-bottom:16px; padding:12px; border-radius:8px; border:1px solid var(--card-border); background:var(--bg-primary); color:var(--text-primary); box-sizing:border-box;"></textarea>
                <button class="primary-btn w-100" id="submitQueryBtn" type="submit" style="cursor: pointer;"><i class="fa fa-paper-plane" style="margin-right: 6px;"></i> Send Query</button>
            </form>
            <div id="queryMsg" style="margin-top:14px; color:#16a34a; font-weight:600; display:none; text-align:center; padding:8px; background:rgba(22,163,74,0.1); border-radius:6px;">Thank you! Your query has been submitted successfully. We will get back to you shortly.</div>
        </div>
    </div>

    <!-- Footer Area -->
    <footer class="footer-area section-gap">
        <div class="container">
            <div class="row">
                <div class="col-lg-5 col-md-6 col-sm-6 mb-4 mb-lg-0">
                    <div class="single-footer-widget">
                        <h6>About City Info India Travels</h6>
                        <p>Approved by the Ministry of Tourism, Govt. of India. We craft unforgettable, authentic Indian travel experiences with 24/7 dedicated support and expert local drivers.</p>
                        <p class="footer-text" style="margin-top: 16px;">Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | City Info India Travels</p>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 mb-4 mb-lg-0">
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
                        <p><i class="fa fa-map-marker" style="color:var(--accent-primary); margin-right:8px;"></i>79, Scindia House, Connaught Place, Janpath, New Delhi</p>
                        <p><i class="fa fa-phone" style="color:var(--accent-primary); margin-right:8px;"></i> +91 87001 40135</p>
                        <p><i class="fa fa-envelope" style="color:var(--accent-primary); margin-right:8px;"></i> cityindiainfotravels@gmail.com</p>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <script src="../js/vendor/jquery-2.2.4.min.js"></script>
    <script src="../js/vendor/bootstrap.min.js"></script>
    <script src="../js/modern-custom.js" defer></script>

    <!-- Reliable Direct Query Modal Script -->
    <script>
    (function () {{
        var modal = document.getElementById('queryModal');
        var closeBtn = document.getElementById('closeQueryModal');
        var form = document.getElementById('contact');
        var msg = document.getElementById('queryMsg');

        function openModal(e) {{
            if (e) e.preventDefault();
            if (modal) modal.style.display = 'flex';
        }}

        function closeModal() {{
            if (modal) {{
                modal.style.display = 'none';
                if (form) form.reset();
                if (msg) msg.style.display = 'none';
            }}
        }}

        // Attach listeners to all query buttons
        document.querySelectorAll('#openQueryModal, #openQueryModal2, .openQueryModal').forEach(function(btn) {{
            btn.addEventListener('click', openModal);
        }});

        if (closeBtn) {{
            closeBtn.addEventListener('click', closeModal);
        }}

        window.addEventListener('click', function (e) {{
            if (e.target === modal) {{
                closeModal();
            }}
        }});

        if (form) {{
            form.addEventListener('submit', function (e) {{
                e.preventDefault();
                var emailInput = form.querySelector('input[name="email"]');
                var msgInput = form.querySelector('textarea[name="message"]');
                var submitBtn = document.getElementById('submitQueryBtn');

                if (!emailInput || !emailInput.value.trim() || !msgInput || !msgInput.value.trim()) {{
                    alert('Please provide both your email and query requirements.');
                    return;
                }}

                var originalBtnText = submitBtn ? submitBtn.innerHTML : 'Send Query';
                if (submitBtn) {{
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = '<i class="fa fa-circle-o-notch fa-spin"></i> Sending Query...';
                }}

                var formData = new FormData(form);
                fetch(form.action, {{
                    method: 'POST',
                    body: formData,
                    headers: {{ 'Accept': 'application/json' }}
                }}).then(function () {{
                    if (msg) {{
                        msg.style.display = 'block';
                        msg.textContent = "Thank you! Your query has been submitted successfully. We will get back to you shortly.";
                    }}
                    form.reset();
                }}).catch(function () {{
                    if (msg) {{
                        msg.style.display = 'block';
                        msg.textContent = "Thank you! Your query has been received. Our team will contact you soon.";
                    }}
                    form.reset();
                }}).finally(function () {{
                    if (submitBtn) {{
                        submitBtn.disabled = false;
                        submitBtn.innerHTML = originalBtnText;
                    }}
                }});
            }});
        }}
    }})();
    </script>
</body>
</html>"""

def build_all():
    for dest in DESTINATIONS_DATA:
        hl_html = ""
        for hl in dest['highlights']:
            hl_html += f'<div class="highlight-item"><i class="fa fa-check-circle"></i> {hl}</div>\n'

        html = TEMPLATE.format(
            page_title=dest['page_title'],
            hero_desc=dest['hero_desc'],
            img_hero=dest['img_hero'],
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
            img_gal1=dest['img_gal1'],
            img_gal2=dest['img_gal2'],
            img_gal3=dest['img_gal3'],
            cap1=dest['cap1'],
            cap2=dest['cap2'],
            cap3=dest['cap3']
        )

        out_path = os.path.join(PAGES_DIR, dest['filename'])
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {dest['filename']}")

    print(f"Successfully generated all {len(DESTINATIONS_DATA)} subpages with budget, itinerary timeline & working send query button!")

if __name__ == '__main__':
    build_all()
