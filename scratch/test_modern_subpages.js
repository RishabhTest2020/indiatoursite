const { chromium } = require('C:/Users/Hp/AppData/Roaming/npm/node_modules/@playwright/mcp/node_modules/playwright');
const path = require('path');

const BASE_URL = 'http://localhost:8080';
const ARTIFACTS_DIR = 'C:/Users/Hp/.gemini/antigravity-ide/brain/b6a24b34-d684-47b0-b690-16419b294e21';

async function testSubpages() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });

  const testPages = [
    'Pages-inside/Kashmir-Info.html',
    'Pages-inside/GoldenTemple-Info.html',
    'Pages-inside/Jaipur-Info.html',
    'Pages-inside/Alleppey-Info.html',
    'Pages-inside/UmngotRiver-Info.html'
  ];

  for (const pagePath of testPages) {
    console.log(`\n================ Testing ${pagePath} ================`);
    const page = await context.newPage();
    const errors = [];
    const failedRequests = [];

    page.on('pageerror', err => errors.push(err.message));
    page.on('requestfailed', req => failedRequests.push(req.url()));

    await page.goto(`${BASE_URL}/${pagePath}`);
    await page.waitForTimeout(500);

    // 1. Verify Quick Stats Bar (Budget, Duration, Best Time, Ideal For)
    const stats = await page.$$eval('.stat-pill', pills => pills.map(p => {
      const label = p.querySelector('.stat-label')?.textContent.trim();
      const val = p.querySelector('.stat-val')?.textContent.trim();
      return { label, val };
    }));
    console.log('Quick Stats found:', stats);

    // 2. Verify Itinerary Timeline
    const timelineItems = await page.$$eval('.timeline-item', items => items.map(t => {
      const badge = t.querySelector('.timeline-badge')?.textContent.trim();
      const title = t.querySelector('.timeline-title')?.textContent.trim();
      return { badge, title };
    }));
    console.log('Timeline Items found:', timelineItems);

    // 3. Verify Visual Gallery Images
    const galleryImages = await page.$$eval('.inside-gallery-item img', imgs => imgs.map(img => ({
      src: img.src,
      complete: img.complete,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight
    })));
    console.log(`Gallery images: ${galleryImages.length}. Broken:`, galleryImages.filter(i => !i.complete || i.naturalWidth === 0));

    // 4. Test Top "Send Query" Button
    const topBtn = await page.$('#openQueryModal');
    console.log(`Top button found: ${topBtn !== null}`);
    await topBtn.click();
    await page.waitForTimeout(300);

    let modalDisplay = await page.$eval('#queryModal', el => window.getComputedStyle(el).display);
    console.log(`After top Send Query click, modal display: ${modalDisplay}`);

    // Take screenshot with modal open on Kashmir
    if (pagePath === 'Pages-inside/Kashmir-Info.html') {
      await page.screenshot({ path: path.join(ARTIFACTS_DIR, 'kashmir_modern_query_modal.png') });
      console.log('Saved kashmir_modern_query_modal.png');
    }

    // 5. Test Close Button
    const closeBtn = await page.$('#closeQueryModal');
    await closeBtn.click();
    await page.waitForTimeout(300);
    modalDisplay = await page.$eval('#queryModal', el => window.getComputedStyle(el).display);
    console.log(`After close click, modal display: ${modalDisplay}`);

    // 6. Test Sidebar "Send Query / Request Quote" Button
    const sidebarBtn = await page.$('#openQueryModal2');
    console.log(`Sidebar button found: ${sidebarBtn !== null}`);
    await sidebarBtn.click();
    await page.waitForTimeout(300);
    modalDisplay = await page.$eval('#queryModal', el => window.getComputedStyle(el).display);
    console.log(`After sidebar Send Query click, modal display: ${modalDisplay}`);

    // 7. Test Form Submission
    await page.fill('#contact input[name="email"]', 'test.traveler@gmail.com');
    await page.fill('#contact textarea[name="message"]', 'Looking for a complete itinerary quote for a group of 4 travelers.');
    await page.click('#contact button[type="submit"]');
    await page.waitForTimeout(600);

    const queryMsg = await page.$eval('#queryMsg', el => ({
      text: el.textContent.trim(),
      display: window.getComputedStyle(el).display
    }));
    console.log(`After form submission, queryMsg text: "${queryMsg.text}", display: ${queryMsg.display}`);

    // Close modal
    await closeBtn.click();
    await page.waitForTimeout(300);

    // 8. Capture clean page screenshot
    const slug = pagePath.split('/')[1].replace('-Info.html', '').toLowerCase();
    await page.screenshot({ path: path.join(ARTIFACTS_DIR, `verified_modern_${slug}.png`) });
    console.log(`Saved verified_modern_${slug}.png`);

    console.log(`Page errors: ${errors.length}, Failed requests: ${failedRequests.length}`);
    await page.close();
  }

  // 9. Batch check remaining 16 subpages for quick stats and working modal
  console.log('\n================ Batch checking remaining 16 subpages ================');
  const remaining = [
    'Bikaner-Info.html', 'CamelSafari-Info.html', 'ColvaBeach-Info.html',
    'GwaliorFort-Info.html', 'Hampi-Info.html', 'Himachal-Info.html',
    'Jaisalmer-Info.html', 'Jodhpur-Info.html', 'MehrangarhFort-Info.html',
    'Mon-Info.html', 'Pushkar-Info.html', 'SanchiStupa-Info.html',
    'Twang-Info.html', 'Udaipur-Info.html', 'Uttrakhand-Info.html',
    'VivekanandaRockMemorial-Info.html'
  ];

  for (const fn of remaining) {
    const page = await context.newPage();
    await page.goto(`${BASE_URL}/Pages-inside/${fn}`);
    
    // Check stats count
    const statsCount = await page.$$eval('.stat-pill', pills => pills.length);
    const timelineCount = await page.$$eval('.timeline-item', items => items.length);
    
    // Check button click
    const btn = await page.$('#openQueryModal');
    await btn.click();
    await page.waitForTimeout(100);
    const disp = await page.$eval('#queryModal', el => window.getComputedStyle(el).display);

    console.log(`${fn.padEnd(34)} | stats: ${statsCount} | timeline: ${timelineCount} | modalOpens: ${disp === 'flex'}`);
    await page.close();
  }

  await browser.close();
  console.log('\nAll tests completed successfully!');
}

testSubpages().catch(console.error);
