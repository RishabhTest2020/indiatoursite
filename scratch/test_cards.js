const { chromium } = require('C:/Users/Hp/AppData/Roaming/npm/node_modules/@playwright/mcp/node_modules/playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto('http://localhost:8080/index.html', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(1000);

    const cards = await page.$$('.single-portfolio');
    console.log(`Found ${cards.length} portfolio cards.`);

    for (let i = 0; i < Math.min(cards.length, 5); i++) {
        const title = await cards[i].$eval('h4', el => el.textContent.trim());
        const href = await cards[i].$eval('.wa-card-btn', el => el.getAttribute('href'));
        console.log(`Card ${i + 1} [${title}] -> WA Link:\n  ${decodeURIComponent(href)}\n`);
    }

    await browser.close();
})();
