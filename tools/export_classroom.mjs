// Render the verified classroom views for offline use. Requires Playwright Core and Chrome.
import { createRequire } from 'node:module';
import { mkdir } from 'node:fs/promises';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_CORE || 'playwright-core');
const base = process.env.CLASSROOM_URL || 'http://localhost:8793';
const browser = await chromium.launch({executablePath: process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless:true});
const page = await browser.newPage({viewport:{width:1920,height:1080}});
await mkdir('evidence',{recursive:true});
await page.goto(base+'/classroom/start-here.html');
await page.evaluate(()=>document.fonts.ready);
await page.pdf({path:'evidence/Small-Worlds-Part-2-Workbook.pdf',format:'Letter',printBackground:true,preferCSSPageSize:true});
await page.goto(base+'/?print');
await page.evaluate(()=>document.fonts.ready);
await page.waitForTimeout(1000);
await page.evaluate(({base})=>{
 document.title='Small Worlds: AI for Unreal Engine — Part 2';
 document.querySelectorAll('a[href]').forEach(a=>{
  if(a.href.startsWith(base))a.href=a.href.replace(base,'https://ibrews.github.io/creative-ai-masterclass-2-deck');
 });
},{base});
await page.pdf({path:'evidence/Small-Worlds-Part-2-Slides.pdf',width:'13.333in',height:'7.5in',printBackground:true,preferCSSPageSize:true});
await browser.close();
console.log('Workbook and slide PDFs exported.');
