const { chromium } = require('C:/Users/Hp/AppData/Roaming/npm/node_modules/@playwright/mcp/node_modules/playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle' });
  const services = await page.$('.services-area');
  if (services) {
    await services.screenshot({ path: 'scratch/services_fixed.png' });
    console.log('Services fixed screenshot saved');
  }

  // Dark mode test
  await page.evaluate(() => document.body.classList.add('dark-mode'));
  await page.waitForTimeout(300);
  if (services) {
    await services.screenshot({ path: 'scratch/services_dark.png' });
    console.log('Services dark mode screenshot saved');
  }
  
  const imgs = await page.$$eval('.single-service img', els => els.map(e => ({
    src: e.src,
    naturalWidth: e.naturalWidth,
    naturalHeight: e.naturalHeight,
    complete: e.complete
  })));
  console.log('Images in single-service:', JSON.stringify(imgs, null, 2));

  await browser.close();
})();
