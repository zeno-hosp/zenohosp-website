const fs = require('fs');
const path = require('path');

const DIRECTORY = __dirname;

function readComponent(name) {
  try {
    return fs.readFileSync(path.join(DIRECTORY, 'components', name), 'utf-8');
  } catch (err) {
    console.error(`  [warn] Could not read components/${name} — skipping.`);
    return null;
  }
}

function getRelativeRoot(filePath) {
  const rel = path.relative(DIRECTORY, filePath);
  const depth = rel.split(path.sep).length - 1;
  return depth === 0 ? './' : '../'.repeat(depth);
}

function resolveRoot(content, rootPath) {
  return content.replace(/\{\{ROOT\}\}/g, rootPath);
}

function processFile(filePath, footer, strip) {
  let content = fs.readFileSync(filePath, 'utf-8');
  let changed = false;
  const root = getRelativeRoot(filePath);

  if (footer && content.includes('<!-- INCLUDE_FOOTER -->')) {
    content = content.replace(/<!-- INCLUDE_FOOTER -->/g, resolveRoot(footer, root));
    changed = true;
    console.log(`  footer  → ${path.relative(DIRECTORY, filePath)}`);
  }

  if (strip && content.includes('<!-- INCLUDE_PLATFORM_STRIP -->')) {
    content = content.replace(/<!-- INCLUDE_PLATFORM_STRIP -->/g, resolveRoot(strip, root));
    changed = true;
    console.log(`  strip   → ${path.relative(DIRECTORY, filePath)}`);
  }

  if (changed) fs.writeFileSync(filePath, content, 'utf-8');
}

function walkDir(dir, footer, strip) {
  for (const file of fs.readdirSync(dir)) {
    const full = path.join(dir, file);
    if (fs.statSync(full).isDirectory()) {
      if (!['node_modules', '.git', 'components'].includes(file)) walkDir(full, footer, strip);
    } else if (full.endsWith('.html')) {
      processFile(full, footer, strip);
    }
  }
}

console.log('Building...');
const footer = readComponent('footer.html');
const strip  = readComponent('platform-strip.html');
walkDir(DIRECTORY, footer, strip);
console.log('Done.');
