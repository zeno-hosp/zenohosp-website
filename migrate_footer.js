const fs = require('fs');
const path = require('path');

const DIRECTORY = __dirname;

function processFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  
  // Find the footer block.
  // We assume it starts with `<footer class="footer">` and ends with `</footer>`
  // And there are no nested footers.
  
  const footerStart = content.indexOf('<footer class="footer">');
  if (footerStart !== -1) {
    const footerEnd = content.indexOf('</footer>', footerStart) + '</footer>'.length;
    
    if (footerEnd > '</footer>'.length - 1) {
      const beforeFooter = content.substring(0, footerStart);
      const afterFooter = content.substring(footerEnd);
      
      const newContent = beforeFooter + '<!-- INCLUDE_FOOTER -->' + afterFooter;
      fs.writeFileSync(filePath, newContent, 'utf-8');
      console.log(`Migrated footer in: ${path.relative(DIRECTORY, filePath)}`);
    }
  }
}

function walkDir(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      if (file !== 'node_modules' && file !== '.git' && file !== 'components') {
        walkDir(fullPath);
      }
    } else if (fullPath.endsWith('.html') && !fullPath.includes('components/')) {
      processFile(fullPath);
    }
  }
}

console.log('Starting footer migration...');
walkDir(DIRECTORY);
console.log('Migration complete.');
