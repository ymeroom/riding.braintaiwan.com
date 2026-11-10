// Build print-ready PDFs of the hand-drawn sketches.
//   node scripts_v2/build_print.js            (all days + combined files)
//   node scripts_v2/build_print.js 2 5        (only these days, no combined files)
// Output: sketches/print/dayN-postcard.pdf, dayN-a5.pdf, all-postcard.pdf, all-a5.pdf
// Each page is trim size + 3 mm bleed on every side; artwork stays inside a 6 mm safe margin.
// Requires the pre-installed Playwright; reads sketches/dayN.html (run build_sketches.py first).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SK = path.join(ROOT, 'sketches');
const OUT = path.join(SK, 'print');
const BLEED = 3;
const FORMATS = {
  postcard: { w: 100, h: 148, label: '明信片 100×148 mm' },
  a5: { w: 148, h: 210, label: 'A5 148×210 mm' },
};
const STYLE_NAME = ['', '絵巻', '旅のしおり', '鳥瞰図', '木版'];

async function grab(page, n) {
  await page.goto('file://' + path.join(SK, `day${n}.html`));
  return page.evaluate(() => ({
    defs: document.querySelector('svg[aria-hidden="true"]').outerHTML,
    title: document.querySelector('h1').textContent.trim(),
    svgs: [1, 2, 3, 4].map((v) => {
      const s = document.querySelector(`#v${v} svg`).cloneNode(true);
      s.removeAttribute('style');
      s.querySelectorAll('[filter="url(#grain)"]').forEach((e) => e.remove()); // paper noise: huge when rasterised
      const vb = s.getAttribute('viewBox').split(/\s+/).map(Number);
      return { html: s.outerHTML, w: vb[2], h: vb[3] };
    }),
  }));
}

function splitScroll(item) {
  // emaki is read right-to-left: right half on the top row, left half below
  const half = item.w / 2;
  const row = (x0) => item.html.replace(/viewBox="[^"]*"/, `viewBox="${x0} 0 ${half} ${item.h}"`);
  return {
    w: half, h: item.h * 2 + 40,
    html: `<div style="display:flex;flex-direction:column;justify-content:space-between;height:100%">${row(half)}${row(0)}</div>`,
    rows: true,
  };
}

function sheet(fmt, item, day, v, title) {
  const F = FORMATS[fmt];
  if (item.w / item.h > 2.2) item = splitScroll(item);
  const land = item.w / item.h > 1.05;
  const W = (land ? F.h : F.w) + 2 * BLEED;
  const H = (land ? F.w : F.h) + 2 * BLEED;
  const safe = BLEED + 6;
  const capH = 7;
  const aw = W - 2 * safe;
  const ah = H - 2 * safe - capH;
  const sc = Math.min(aw / item.w, ah / item.h);
  const w = item.w * sc;
  const h = item.h * sc;
  const name = `${fmt}-${land ? 'land' : 'port'}`;
  return {
    name, W, H,
    html: `<section class="pg ${name}"><div class="art" style="width:${w.toFixed(2)}mm;height:${h.toFixed(2)}mm;margin-top:${(safe + (ah - h) / 2).toFixed(2)}mm">${item.html}</div>`
      + `<div class="cap" style="top:${(H - safe - capH + 2).toFixed(2)}mm">${title}　・　${STYLE_NAME[v]}　・　riding.braintaiwan.com</div></section>`,
  };
}

function doc(defs, sheets) {
  const sizes = {};
  sheets.forEach((s) => (sizes[s.name] = s));
  const pages = Object.values(sizes).map((s) => `@page ${s.name}{size:${s.W}mm ${s.H}mm;margin:0} .${s.name}{page:${s.name};width:${s.W}mm;height:${s.H}mm}`).join('\n');
  return `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Klee+One:wght@400;600&family=Yuji+Syuku&family=Noto+Serif+TC:wght@500&display=block">
<style>${pages}
*{box-sizing:border-box}html,body{margin:0;padding:0}
.pg{position:relative;overflow:hidden;break-after:page;background:#f3ecdf;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.art{margin:0 auto}.art>svg{display:block;width:100%;height:100%}.art div>svg{display:block;width:100%;height:auto}
.cap{position:absolute;left:0;right:0;text-align:center;font:7pt "Klee One","Noto Serif TC",serif;color:#6e6458;letter-spacing:.06em}
</style></head><body>${defs}${sheets.map((s) => s.html).join('')}</body></html>`;
}

async function render(browser, html, file) {
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  await page.pdf({ path: file, preferCSSPageSize: true, printBackground: true });
  await page.close();
}

(async () => {
  const only = process.argv.slice(2).map(Number).filter(Boolean);
  const days = only.length ? only : Array.from({ length: 19 }, (_, i) => i + 1);
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const all = { postcard: [], a5: [] };
  let defs = '';
  for (const n of days) {
    const g = await grab(page, n);
    defs = g.defs;
    for (const fmt of Object.keys(FORMATS)) {
      const sh = g.svgs.map((it, i) => sheet(fmt, it, n, i + 1, g.title.replace(/\s+/g, ' ')));
      // ids inside a day's svgs (gradients/clips) are day-specific, so combining days is safe
      all[fmt].push(...sh);
      await render(browser, doc(g.defs, sh), path.join(OUT, `day${n}-${fmt}.pdf`));
    }
    console.log('day', n, 'done');
  }
  if (!only.length) {
    for (const fmt of Object.keys(FORMATS)) {
      await render(browser, doc(defs, all[fmt]), path.join(OUT, `all-${fmt}.pdf`));
      console.log('all', fmt, 'done');
    }
  }
  await browser.close();
})();
