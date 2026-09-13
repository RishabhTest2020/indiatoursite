import os
import re

PAGES_DIR = r"c:\Users\Hp\PycharmProjects\indiatoursite\Pages-inside"

MAPPING = {
    "Alleppey-Info.html": {
        "hero": "../img/alleppey_hero.jpg",
        "gal1": "../img/alleppey_gal1.jpg",
        "gal2": "../img/alleppey_gal2.jpg",
        "gal3": "../img/alleppey_gal3.jpg",
    },
    "Bikaner-Info.html": {
        "hero": "../img/bikaner_hero.jpg",
        "gal1": "../img/bikaner_gal1.jpg",
        "gal2": "../img/bikaner_gal2.jpg",
        "gal3": "../img/bikaner_gal3.jpg",
    },
    "CamelSafari-Info.html": {
        "hero": "../img/camelsafari_hero.jpg",
        "gal1": "../img/camelsafari_gal1.jpg",
        "gal2": "../img/camelsafari_gal2.jpg",
        "gal3": "../img/camelsafari_gal3.jpg",
    },
    "ColvaBeach-Info.html": {
        "hero": "../img/colvabeach_hero.jpg",
        "gal1": "../img/colvabeach_gal1.jpg",
        "gal2": "../img/colvabeach_gal2.jpg",
        "gal3": "../img/colvabeach_gal3.jpg",
    },
    "GoldenTemple-Info.html": {
        "hero": "../img/golden_temple_hero.png",
        "gal1": "../img/golden_temple_arch.png",
        "gal2": "../img/golden_temple_reflection.png",
        "gal3": "../img/wagah_border.png",
    },
    "GwaliorFort-Info.html": {
        "hero": "../img/gwaliorfort_hero.jpg",
        "gal1": "../img/gwaliorfort_gal1.jpg",
        "gal2": "../img/gwaliorfort_gal2.jpg",
        "gal3": "../img/gwaliorfort_gal3.jpg",
    },
    "Hampi-Info.html": {
        "hero": "../img/hampi_hero.jpg",
        "gal1": "../img/hampi_gal1.jpg",
        "gal2": "../img/hampi_gal2.jpg",
        "gal3": "../img/hampi_gal3.jpg",
    },
    "Himachal-Info.html": {
        "hero": "../img/himachal_hero.jpg",
        "gal1": "../img/himachal_gal1.jpg",
        "gal2": "../img/himachal_gal2.jpg",
        "gal3": "../img/himachal_gal3.jpg",
    },
    "Jaipur-Info.html": {
        "hero": "../img/jaipur_hero.jpg",
        "gal1": "../img/jaipur_gal1.jpg",
        "gal2": "../img/jaipur_gal2.jpg",
        "gal3": "../img/jaipur_gal3.jpg",
    },
    "Jaisalmer-Info.html": {
        "hero": "../img/jaisalmer_hero.jpg",
        "gal1": "../img/jaisalmer_gal1.jpg",
        "gal2": "../img/jaisalmer_gal2.jpg",
        "gal3": "../img/jaisalmer_gal3.jpg",
    },
    "Jodhpur-Info.html": {
        "hero": "../img/jodhpur_hero.jpg",
        "gal1": "../img/jodhpur_gal1.jpg",
        "gal2": "../img/jodhpur_gal2.jpg",
        "gal3": "../img/jodhpur_gal3.jpg",
    },
    "Kashmir-Info.html": {
        "hero": "../img/kashmir_hero.jpg",
        "gal1": "../img/kashmir_gal1.jpg",
        "gal2": "../img/kashmir_gal2.jpg",
        "gal3": "../img/kashmir_gal3.jpg",
    },
    "MehrangarhFort-Info.html": {
        "hero": "../img/mehrangarhfort_hero.jpg",
        "gal1": "../img/mehrangarhfort_gal1.jpg",
        "gal2": "../img/mehrangarhfort_gal2.jpg",
        "gal3": "../img/mehrangarhfort_gal3.jpg",
    },
    "Mon-Info.html": {
        "hero": "../img/mon_hero.jpg",
        "gal1": "../img/mon_gal1.jpg",
        "gal2": "../img/mon_gal2.jpg",
        "gal3": "../img/mon_gal3.jpg",
    },
    "Pushkar-Info.html": {
        "hero": "../img/pushkar_hero.jpg",
        "gal1": "../img/pushkar_gal1.jpg",
        "gal2": "../img/pushkar_gal2.jpg",
        "gal3": "../img/pushkar_gal3.jpg",
    },
    "SanchiStupa-Info.html": {
        "hero": "../img/sanchistupa_hero.jpg",
        "gal1": "../img/sanchistupa_gal1.jpg",
        "gal2": "../img/sanchistupa_gal2.jpg",
        "gal3": "../img/sanchistupa_gal3.jpg",
    },
    "Twang-Info.html": {
        "hero": "../img/twang_hero.jpg",
        "gal1": "../img/twang_gal1.jpg",
        "gal2": "../img/twang_gal2.jpg",
        "gal3": "../img/twang_gal3.jpg",
    },
    "Udaipur-Info.html": {
        "hero": "../img/udaipur_hero.jpg",
        "gal1": "../img/udaipur_gal1.jpg",
        "gal2": "../img/udaipur_gal2.jpg",
        "gal3": "../img/udaipur_gal3.jpg",
    },
    "UmngotRiver-Info.html": {
        "hero": "../img/umngotriver_hero.jpg",
        "gal1": "../img/umngotriver_gal1.jpg",
        "gal2": "../img/umngotriver_gal2.jpg",
        "gal3": "../img/umngotriver_gal3.jpg",
    },
    "Uttrakhand-Info.html": {
        "hero": "../img/uttrakhand_hero.jpg",
        "gal1": "../img/uttrakhand_gal1.jpg",
        "gal2": "../img/uttrakhand_gal2.jpg",
        "gal3": "../img/uttrakhand_gal3.jpg",
    },
    "VivekanandaRockMemorial-Info.html": {
        "hero": "../img/vivekanandarock_hero.jpg",
        "gal1": "../img/vivekanandarock_gal1.jpg",
        "gal2": "../img/vivekanandarock_gal2.jpg",
        "gal3": "../img/vivekanandarock_gal3.jpg",
    }
}

def update_all_pages():
    for filename, images in MAPPING.items():
        filepath = os.path.join(PAGES_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Update Hero background-image
        content = re.sub(
            r'(<section class="subpage-hero"[^>]*style="[^"]*background-image:\s*url\()[^\)]+(\)[^"]*">)',
            rf"\g<1>'{images['hero']}'\g<2>",
            content
        )

        # 2. Update Gallery images
        parts = content.split('<div class="inside-gallery-item">')
        if len(parts) == 4:
            keys = ['gal1', 'gal2', 'gal3']
            new_parts = [parts[0]]
            for i in range(1, 4):
                item_text = parts[i]
                item_text = re.sub(r'(<img\s+src=")[^"]+(")', rf'\g<1>{images[keys[i-1]]}\g<2>', item_text, count=1)
                new_parts.append(item_text)
            content = '<div class="inside-gallery-item">'.join(new_parts)
        else:
            print(f"  Warning: {filename} has {len(parts)-1} gallery items instead of 3!")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {filename}:")
        print(f"  Hero: {images['hero']}")
        print(f"  Gal1: {images['gal1']}")
        print(f"  Gal2: {images['gal2']}")
        print(f"  Gal3: {images['gal3']}")

if __name__ == "__main__":
    update_all_pages()
