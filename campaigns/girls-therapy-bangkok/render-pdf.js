// Compile the 4:5 feed slides into one PDF, one slide per page.
// Built from the rendered PNGs (export/girls-therapy-0X-*.png) so every viewer shows it the same:
// a live HTML→PDF keeps blend modes and SVG filters that some mobile viewers draw as blank pages.
// Run `node render.js` first.
const path = require('path');
const { execFileSync } = require('child_process');
const exp = path.join(__dirname, 'export');
execFileSync('python3', ['-c', `
import glob, sys
from PIL import Image
d = sys.argv[1]
files = sorted(glob.glob(d + '/girls-therapy-0*.png'))
pages = [Image.open(f).convert('RGB') for f in files]
pages[0].save(d + '/Girls-Therapy-NYE-Bangkok.pdf', save_all=True, append_images=pages[1:], resolution=200, quality=92)
print(len(pages), 'pages')
`, exp], { stdio: 'inherit' });
