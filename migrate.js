/**
 * migrate.js — one-time prep step before running build.js
 *
 * For every HTML file (outside components/):
 *   1. Strips stray <!-- Footer --> comment lines
 *   2. Replaces <footer class="footer">...</footer> with <!-- INCLUDE_FOOTER -->
 *   3. Replaces <div class="platform-strip">...</div> with <!-- INCLUDE_PLATFORM_STRIP -->
 *
 * After this runs, execute `node build.js` to inject the shared components.
 * To update a component later: edit components/*.html, re-run migrate.js + build.js.
 */

const fs = require('fs');
const path = require('path');

const DIRECTORY = __dirname;

// Find the outermost block starting with `openTag` using a div-depth counter.
function findDivBlock(content, openTag) {
  const start = content.indexOf(openTag);
  if (start === -1) return null;

  let depth = 0;
  let i = start;
  while (i < content.length) {
    if (content[i] === '<') {
      if (/^<div[\s>]/.test(content.slice(i))) depth++;
      else if (content.slice(i, i + 6) === '</div>') {
        depth--;
        if (depth === 0) return { start, end: i + 6 };
      }
    }
    i++;
  }
  return null;
}

function processFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  const original = content;

  // 1. Strip stray <!-- Footer --> comment lines (any indentation)
  content = content.replace(/[ \t]*<!-- Footer -->[ \t]*\n/g, '');

  // 2. Replace <footer class="footer">...</footer> with marker
  const footerOpen = '<footer class="footer">';
  const footerStart = content.indexOf(footerOpen);
  if (footerStart !== -1) {
    const footerEnd = content.indexOf('</footer>', footerStart) + '</footer>'.length;
    if (footerEnd > '</footer>'.length - 1) {
      content = content.slice(0, footerStart) + '  <!-- INCLUDE_FOOTER -->' + content.slice(footerEnd);
    }
  }

  // 3. Replace <div class="platform-strip">...</div> with marker
  const stripBlock = findDivBlock(content, '<div class="platform-strip">');
  if (stripBlock) {
    content =
      content.slice(0, stripBlock.start) +
      '  <!-- INCLUDE_PLATFORM_STRIP -->' +
      content.slice(stripBlock.end);
  }

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`  migrated → ${path.relative(DIRECTORY, filePath)}`);
  }
}

function walkDir(dir) {
  for (const file of fs.readdirSync(dir)) {
    const full = path.join(dir, file);
    if (fs.statSync(full).isDirectory()) {
      if (!['node_modules', '.git', 'components'].includes(file)) walkDir(full);
    } else if (full.endsWith('.html')) {
      processFile(full);
    }
  }
}

console.log('Migrating components...');
walkDir(DIRECTORY);
console.log('Migration complete. Run `node build.js` to inject components.');
