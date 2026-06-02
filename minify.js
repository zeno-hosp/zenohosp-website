/**
 * minify.js — CSS bundler + minifier for deploy
 *
 * 1. Reads css/main.css, resolves all @import chains into one bundle
 * 2. Minifies the bundle and writes back to css/main.css
 * 3. Minifies every other CSS file in css/ in place
 * 4. Reports size savings
 *
 * Run: node minify.js
 * In deploy pipeline: node migrate.js && node build.js && node minify.js
 */

const fs   = require('fs');
const path = require('path');

const CSS_DIR = path.join(__dirname, 'css');

// ── Simple but effective CSS minifier ────────────────────────────────────────
function minifyCss(css) {
  return css
    // Remove /* block comments */ (including multiline)
    .replace(/\/\*[\s\S]*?\*\//g, '')
    // Collapse all whitespace runs (spaces, tabs, newlines) to a single space
    .replace(/\s+/g, ' ')
    // Remove spaces around structural characters
    .replace(/\s*([{}:;,>~+])\s*/g, '$1')
    // Remove trailing semicolons before closing brace
    .replace(/;}/g, '}')
    // Remove leading/trailing whitespace
    .trim();
}

// ── Resolve @import url(...) recursively into one flat CSS string ─────────────
function bundle(filePath, visited = new Set()) {
  const realPath = path.resolve(filePath);
  if (visited.has(realPath)) return '';
  visited.add(realPath);

  const dir = path.dirname(realPath);
  let content;
  try {
    content = fs.readFileSync(realPath, 'utf-8');
  } catch (e) {
    console.warn(`  [warn] Cannot read: ${filePath}`);
    return '';
  }

  // Replace each @import url('...') with the contents of the referenced file
  return content.replace(
    /@import\s+url\(['"]?([^'")]+)['"]?\)\s*;/g,
    (_, importedPath) => {
      const resolved = path.join(dir, importedPath);
      return bundle(resolved, visited);
    }
  );
}

// ── Get all CSS files (excluding main.css — handled separately) ───────────────
function getAllCssFiles(dir) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...getAllCssFiles(full));
    } else if (entry.isFile() && entry.name.endsWith('.css')) {
      if (full !== path.join(CSS_DIR, 'main.css')) {
        results.push(full);
      }
    }
  }
  return results;
}

function fmt(bytes) {
  return (bytes / 1024).toFixed(1) + ' KB';
}

// ── Main ──────────────────────────────────────────────────────────────────────
console.log('Minifying CSS...\n');

let totalBefore = 0;
let totalAfter  = 0;

// 1. Bundle + minify main.css
const mainPath   = path.join(CSS_DIR, 'main.css');
const bundled    = bundle(mainPath);
const minified   = minifyCss(bundled);
const mainBefore = fs.statSync(mainPath).size;

// Include all the imported files' sizes in the "before" count
// (they get folded into main.css, so they'll no longer be needed at runtime)
const importedFiles = getAllCssFiles(CSS_DIR);

// Write bundled + minified main.css
fs.writeFileSync(mainPath, minified, 'utf-8');
const mainAfter = fs.statSync(mainPath).size;

// Report the total bundle saving (sum of all files before vs one file after)
let importedBefore = 0;
for (const f of importedFiles) {
  importedBefore += fs.statSync(f).size;
}

totalBefore += mainBefore + importedBefore;
totalAfter  += mainAfter;

console.log(`  main.css (bundled + minified)`);
console.log(`    Before: ${fmt(mainBefore + importedBefore)} (main + ${importedFiles.length} imports)`);
console.log(`    After:  ${fmt(mainAfter)} (single file)\n`);

// 2. Minify each page-specific CSS file individually
//    (loaded directly via <link> on specific pages — keep separate)
const pageSpecificDirs = [
  path.join(CSS_DIR, 'pages'),
  path.join(CSS_DIR, 'layout'),
  path.join(CSS_DIR, 'base'),
];

for (const dir of pageSpecificDirs) {
  if (!fs.existsSync(dir)) continue;
  for (const file of fs.readdirSync(dir)) {
    if (!file.endsWith('.css')) continue;
    const full = path.join(dir, file);
    const content = fs.readFileSync(full, 'utf-8');
    // Skip already-minified files (single line or empty)
    if (content.trim().length === 0) continue;
    const before   = Buffer.byteLength(content, 'utf-8');
    const mini     = minifyCss(content);
    const after    = Buffer.byteLength(mini, 'utf-8');
    fs.writeFileSync(full, mini, 'utf-8');
    totalBefore += before;
    totalAfter  += after;
    const saving = Math.round(100 - (after / before) * 100);
    console.log(`  ${path.relative(CSS_DIR, full).padEnd(36)} ${fmt(before)} → ${fmt(after)} (−${saving}%)`);
  }
}

console.log(`\n${'─'.repeat(52)}`);
console.log(`  Total CSS: ${fmt(totalBefore)} → ${fmt(totalAfter)}  (saved ${fmt(totalBefore - totalAfter)})`);
console.log(`  Reduction: ${Math.round(100 - (totalAfter / totalBefore) * 100)}%`);
