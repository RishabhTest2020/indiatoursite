const { chromium } = require('C:/Users/Hp/AppData/Roaming/npm/node_modules/@playwright/mcp/node_modules/playwright');
const path = require('path');

const ARTIFACT_DIR = 'C:\\Users\\Hp\\.gemini\\antigravity-ide\\brain\\b6a24b34-d684-47b0-b690-16419b294e21';

const DESTINATION_PAGES = [
    'Alleppey-Info.html',
    'Bikaner-Info.html',
    'CamelSafari-Info.html',
    'ColvaBeach-Info.html',
    'GoldenTemple-Info.html',
    'GwaliorFort-Info.html',
    'Hampi-Info.html',
    'Himachal-Info.html',
    'Jaipur-Info.html',
    'Jaisalmer-Info.html',
    'Jodhpur-Info.html',
    'Kashmir-Info.html',
    'MehrangarhFort-Info.html',
    'Mon-Info.html',
    'Pushkar-Info.html',
    'SanchiStupa-Info.html',
    'Twang-Info.html',
    'Udaipur-Info.html',
    'UmngotRiver-Info.html',
    'Uttrakhand-Info.html',
    'VivekanandaRockMemorial-Info.html'
];

(async () => {
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
    const page = await context.newPage();

    let totalFailedImages = 0;
    let totalCheckedPages = 0;

    for (const pageName of DESTINATION_PAGES) {
        const url = `http://localhost:8080/Pages-inside/${pageName}`;
        console.log(`\nTesting ${pageName}...`);

        let failedReqs = [];
        page.on('response', response => {
            if (response.status() >= 400 && response.url().includes('img/')) {
                failedReqs.push(`${response.status()}: ${response.url()}`);
            }
        });

        await page.goto(url, { waitUntil: 'networkidle' });
        totalCheckedPages++;

        // Verify Gallery Images
        const galleryImgs = await page.$$eval('.row.gallery img', imgs => 
            imgs.map(img => ({
                src: img.src,
                naturalWidth: img.naturalWidth,
                naturalHeight: img.naturalHeight,
                complete: img.complete
            }))
        );

        console.log(`  Gallery images count: ${galleryImgs.length}`);
        galleryImgs.forEach((img, idx) => {
            const isOk = img.complete && img.naturalWidth > 0;
            console.log(`    Gal ${idx + 1}: ${img.src.split('/').pop()} (${img.naturalWidth}x${img.naturalHeight}) - ${isOk ? 'OK' : 'FAILED'}`);
            if (!isOk) totalFailedImages++;
        });

        // Verify Banner Background Image
        const bannerBg = await page.$eval('.banner-area', el => {
            return window.getComputedStyle(el).backgroundImage;
        });
        console.log(`  Banner BG: ${bannerBg}`);

        if (['Alleppey-Info.html', 'Bikaner-Info.html', 'UmngotRiver-Info.html', 'Hampi-Info.html', 'Kashmir-Info.html'].includes(pageName)) {
            const screenshotPath = path.join(ARTIFACT_DIR, `gallery_${pageName.replace('.html', '')}.png`);
            const gallerySection = await page.$('.row.gallery');
            if (gallerySection) {
                await gallerySection.scrollIntoViewIfNeeded();
                await page.waitForTimeout(400);
                await page.screenshot({ path: screenshotPath, fullPage: false });
                console.log(`  Saved screenshot: ${screenshotPath}`);
            }
        }
    }

    await browser.close();
    console.log(`\n========================================`);
    console.log(`Verification Complete: ${totalCheckedPages} pages tested.`);
    console.log(`Total Failed Images: ${totalFailedImages}`);
    console.log(`========================================`);
    process.exit(totalFailedImages > 0 ? 1 : 0);
})();
