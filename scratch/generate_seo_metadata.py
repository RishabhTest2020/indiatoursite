import json
import os
import sys

sys.path.append(os.path.abspath('.'))
from scripts.build_all_21_modern_subpages import DESTINATIONS_DATA

SEO_DATA = {
    "GoldenTemple-Info.html": {
        "title": "Golden Temple Amritsar Tour Packages & Itinerary | City Info India Travels",
        "description": "Book our 2 Days / 1 Night Golden Temple tour package. Experience the holy Amrit Sarovar, Langar seva, and Wagah Border with City Info India Travels."
    },
    "Jaipur-Info.html": {
        "title": "Jaipur Tour Packages & Itinerary | City Info India Travels",
        "description": "Book our 3 Days / 2 Nights Jaipur tour package. Explore Amer Fort, Hawa Mahal, City Palace, and royal Rajasthani heritage with City Info India Travels."
    },
    "Kashmir-Info.html": {
        "title": "Kashmir Valley Tour Packages & Itinerary | City Info India Travels",
        "description": "Explore Kashmir with our 5 Days / 4 Nights tour package. Enjoy Dal Lake houseboats, Gulmarg Gondola, and Mughal gardens with City Info India Travels."
    },
    "Alleppey-Info.html": {
        "title": "Alleppey Backwaters Tour Packages & Itinerary | City Info India Travels",
        "description": "Book our 2 Days / 1 Night Alleppey tour package. Cruise Kerala's scenic backwaters on a luxury houseboat with meals and guided village canoe tours."
    },
    "Himachal-Info.html": {
        "title": "Shimla & Manali Tour Packages & Itinerary | City Info India Travels",
        "description": "Escape on our 6 Days / 5 Nights Himachal tour package. Explore Shimla Ridge, Solang Valley snow sports, and Atal Tunnel with City Info India Travels."
    },
    "Jaisalmer-Info.html": {
        "title": "Jaisalmer Tour Packages & Itinerary | City Info India Travels",
        "description": "Book our 3 Days / 2 Nights Jaisalmer tour package. Discover the living Golden Fort, Sam sand dunes camel safaris, and desert campfire camping."
    },
    "Udaipur-Info.html": {
        "title": "Udaipur Tour Packages & Itinerary | City Info India Travels",
        "description": "Experience royal romance on our 3 Days / 2 Nights Udaipur tour package. Tour City Palace, Lake Pichola boat cruises, and Sajjangarh Monsoon Palace."
    },
    "Hampi-Info.html": {
        "title": "Hampi Ruins Tour Packages & Itinerary | City Info India Travels",
        "description": "Step back in time with our 3 Days / 2 Nights Hampi tour package. Explore UNESCO Vijayanagara ruins, Vittala stone chariot, and Virupaksha Temple."
    },
    "Bikaner-Info.html": {
        "title": "Bikaner Tour Packages & Itinerary | City Info India Travels",
        "description": "Book our 2 Days / 1 Night Bikaner heritage tour package. Explore Junagarh Fort, red sandstone Lalgarh Palace, and authentic desert food culture."
    },
    "CamelSafari-Info.html": {
        "title": "Thar Desert Camel Safari Tour Packages | City Info India Travels",
        "description": "Experience our 2 Days / 1 Night Thar Desert camel safari package. Enjoy sunset dune treks, starlit luxury desert camping, and folk music shows."
    },
    "ColvaBeach-Info.html": {
        "title": "Colva Beach Goa Tour Packages & Itinerary | City Info India Travels",
        "description": "Relax on our 3 Days / 2 Nights Colva Beach Goa tour package. Enjoy white sands, thrilling water sports, Portuguese churches, and Goan dining."
    },
    "GwaliorFort-Info.html": {
        "title": "Gwalior Fort Tour Packages & Itinerary | City Info India Travels",
        "description": "Explore Gwalior Fort on our 2 Days / 1 Night heritage tour package. Marvel at blue-tiled Man Mandir Palace, rock-cut Jain statues, and light shows."
    },
    "Jodhpur-Info.html": {
        "title": "Jodhpur Blue City Tour Packages & Itinerary | City Info India Travels",
        "description": "Discover the Blue City on our 2 Days / 1 Night Jodhpur tour package. Visit Jaswant Thada, blue Brahmin alleys, and iconic Umaid Bhawan Palace."
    },
    "MehrangarhFort-Info.html": {
        "title": "Mehrangarh Fort Jodhpur Tour Packages | City Info India Travels",
        "description": "Book our 1 Day Mehrangarh Fort tour package in Jodhpur. Tour 15th-century cliff-top ramparts, royal palanquin museums, and aerial flying fox zips."
    },
    "Mon-Info.html": {
        "title": "Mon Nagaland Tour Packages & Itinerary | City Info India Travels",
        "description": "Journey to Nagaland with our 4 Days / 3 Nights Mon tour package. Experience Konyak tribal culture, Morung architecture, and border village Longwa."
    },
    "Pushkar-Info.html": {
        "title": "Pushkar Tour Packages & Itinerary | City Info India Travels",
        "description": "Book our 2 Days / 1 Night Pushkar holy tour package. Visit the sacred Brahma Temple, 52 bathing ghats, Savitri hilltop shrine, and desert dunes."
    },
    "SanchiStupa-Info.html": {
        "title": "Sanchi Stupa Tour Packages & Itinerary | City Info India Travels",
        "description": "Discover UNESCO Sanchi Stupa on our 1 Day Buddhist heritage tour package. Explore Ashoka's Great Stupa, carved stone torana gates, and museum."
    },
    "Twang-Info.html": {
        "title": "Tawang Monastery Tour Packages & Itinerary | City Info India Travels",
        "description": "Travel to Arunachal on our 5 Days / 4 Nights Tawang tour package. Cross 13,700 ft Sela Pass to visit India's largest 400-year-old Buddhist gompa."
    },
    "UmngotRiver-Info.html": {
        "title": "Umngot River Dawki Tour Packages & Itinerary | City Info India Travels",
        "description": "Book our 2 Days / 1 Night Dawki tour package. Experience crystal-clear boating on the Umngot River, Meghalaya root bridges, and riverside camping."
    },
    "Uttrakhand-Info.html": {
        "title": "Rishikesh & Haridwar Tour Packages & Itinerary | City Info India Travels",
        "description": "Join our 3 Days / 2 Nights Uttarakhand tour package. Experience Ganges whitewater rafting in Rishikesh, Beatles Ashram, and evening Ganga Aarti."
    },
    "VivekanandaRockMemorial-Info.html": {
        "title": "Vivekananda Rock Memorial Tour Packages | City Info India Travels",
        "description": "Visit Kanyakumari on our 2 Days / 1 Night tour package. Ferry to Vivekananda Rock Memorial, Thiruvalluvar Statue, and Triveni Sangam ocean confluence."
    }
}

# Validate all 21
for d in DESTINATIONS_DATA:
    fn = d['filename']
    assert fn in SEO_DATA, f"Missing SEO for {fn}"
    seo = SEO_DATA[fn]
    title = seo['title']
    desc = seo['description']
    l_desc = len(desc)
    print(f"{fn}:")
    print(f"  Title ({len(title)}c): {title}")
    print(f"  Desc ({l_desc}c): {desc}")
    assert 130 <= l_desc <= 155, f"Description length {l_desc} not in 130-155 for {fn}"

print("\nAll 21 destination SEO descriptions are strictly between 130 and 155 characters!")
