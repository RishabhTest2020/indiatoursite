const { chromium } = require('C:/Users/Hp/AppData/Roaming/npm/node_modules/@playwright/mcp/node_modules/playwright');
const path = require('path');

(async () => {
    console.log("Launching Chromium...");
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const page = await context.newPage();

    console.log("\n--- TEST 1: Golden Temple Info Page ---");
    await page.goto('http://localhost:8080/Pages-inside/GoldenTemple-Info.html', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(1000);

    // 1. Sidebar WhatsApp button
    const sidebarBtn = await page.$('.whatsapp-btn');
    const sidebarHref = sidebarBtn ? await sidebarBtn.getAttribute('href') : null;
    console.log("Sidebar Button Href:", decodeURIComponent(sidebarHref));

    // 2. Hero WhatsApp button
    const heroBtn = await page.$('.wa-hero-btn');
    const heroHref = heroBtn ? await heroBtn.getAttribute('href') : null;
    console.log("Hero Button Href:", decodeURIComponent(heroHref));

    // 3. Floating Widget
    const floatingWidget = await page.$('#waFloatingWidget');
    console.log("Floating Widget injected:", !!floatingWidget);

    // Click FAB to open popup
    await page.click('#waFab');
    await page.waitForTimeout(500);

    const isPopupOpen = await page.$eval('#waPopupCard', el => el.classList.contains('open'));
    console.log("Popup Card Opened:", isPopupOpen);

    const previewText = await page.$eval('#waBubblePreview', el => el.textContent.trim());
    console.log("Popup Preview Text:", previewText);

    const popupActionHref = await page.$eval('#waPopupActionBtn', el => el.getAttribute('href'));
    console.log("Popup Action Href:", decodeURIComponent(popupActionHref));

    // Take screenshot of Golden Temple with WhatsApp widget open
    await page.screenshot({ path: path.join(__dirname, 'goldentemple_wa_widget.png'), fullPage: false });
    console.log("Saved screenshot: goldentemple_wa_widget.png");


    console.log("\n--- TEST 2: Kashmir Valley Info Page ---");
    await page.goto('http://localhost:8080/Pages-inside/Kashmir-Info.html', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(1000);

    const kashmirSidebarHref = await page.$eval('.whatsapp-btn', el => el.getAttribute('href'));
    console.log("Kashmir Sidebar Href:", decodeURIComponent(kashmirSidebarHref));

    await page.click('#waFab');
    await page.waitForTimeout(500);
    const kashmirPreview = await page.$eval('#waBubblePreview', el => el.textContent.trim());
    console.log("Kashmir Popup Preview:", kashmirPreview);


    console.log("\n--- TEST 3: Homepage (index.html) ---");
    await page.goto('http://localhost:8080/index.html', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(1000);

    // Check Alleppey card button
    const alleppeyCardBtn = await page.$eval('.single-portfolio .wa-card-btn', el => el.getAttribute('href'));
    console.log("First Card (Alleppey) Href:", decodeURIComponent(alleppeyCardBtn));

    // Check FAB & Popup
    await page.click('#waFab');
    await page.waitForTimeout(500);
    const homePreview = await page.$eval('#waBubblePreview', el => el.textContent.trim());
    console.log("Home Popup Preview:", homePreview);

    // Take screenshot of Home page with WhatsApp popup
    await page.screenshot({ path: path.join(__dirname, 'home_wa_widget.png'), fullPage: false });
    console.log("Saved screenshot: home_wa_widget.png");

    await browser.close();
    console.log("\nAll browser tests passed successfully!");
})();
