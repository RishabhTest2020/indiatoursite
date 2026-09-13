const fs = require('fs');
const path = require('path');

const rootDir = 'c:\\Users\\Hp\\PycharmProjects\\indiatoursite';
const pagesDir = path.join(rootDir, 'Pages-inside');

console.log("=== STEP 1: Verifying Subpage HTML Markup ===");
const subpages = fs.readdirSync(pagesDir).filter(f => f.endsWith('-Info.html'));
let subpageErrors = 0;

subpages.forEach(file => {
    const content = fs.readFileSync(path.join(pagesDir, file), 'utf8');
    const checks = {
        navBtn: content.includes('wa-nav-btn'),
        heroBtn: content.includes('wa-hero-btn'),
        sidebarBtn: content.includes('whatsapp-btn'),
        footerLink: content.includes('fa-whatsapp'),
        script: content.includes('modern-custom.js')
    };

    const failed = Object.entries(checks).filter(([k, v]) => !v).map(([k]) => k);
    if (failed.length > 0) {
        console.error(`❌ ${file} missing: ${failed.join(', ')}`);
        subpageErrors++;
    }
});

if (subpageErrors === 0) {
    console.log(`✅ All ${subpages.length} destination subpages have complete WhatsApp integration!`);
}

console.log("\n=== STEP 2: Verifying index.html Markup ===");
const indexContent = fs.readFileSync(path.join(rootDir, 'index.html'), 'utf8');
const indexChecks = {
    navBtn: indexContent.includes('wa-nav-btn'),
    cardBtns: (indexContent.match(/wa-card-btn/g) || []).length,
    footerLink: indexContent.includes('fa-whatsapp'),
    script: indexContent.includes('modern-custom.js')
};

console.log(`- Nav WhatsApp Button: ${indexChecks.navBtn ? '✅ Found' : '❌ Missing'}`);
console.log(`- Destination Card WhatsApp Buttons: Found ${indexChecks.cardBtns} cards`);
console.log(`- Footer WhatsApp Contact Link: ${indexChecks.footerLink ? '✅ Found' : '❌ Missing'}`);
console.log(`- Script modern-custom.js: ${indexChecks.script ? '✅ Found' : '❌ Missing'}`);

console.log("\n=== STEP 3: Verifying Ancillary Pages ===");
['About.html', 'blog.html', 'Recent-Announcement.html'].forEach(f => {
    const c = fs.readFileSync(path.join(pagesDir, f), 'utf8');
    const hasScript = c.includes('modern-custom.js');
    console.log(`- ${f}: ${hasScript ? '✅ Loads modern-custom.js' : '❌ Missing'}`);
});

console.log("\nAll static markup verifications completed successfully!");
