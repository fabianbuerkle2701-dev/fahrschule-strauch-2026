#!/bin/sh
# Vorschau auf GitHub Pages veröffentlichen: baut die Seite, setzt die Pfade auf den
# Unterordner und schiebt dist/ in den Branch gh-pages.
# Aufruf: sh scripts/deploy-pages.sh
# Seite: https://fabianbuerkle2701-dev.github.io/fahrschule-strauch-2026/
set -e
REPO=fahrschule-strauch-2026
rm -rf dist
npm run build
node scripts/pages-base.mjs /$REPO
touch dist/.nojekyll
cd dist
git init -q -b gh-pages
git add -A
git commit -q -m "Vorschau aus $(cd .. && git rev-parse --short HEAD)"
git push -q -f "$(cd .. && git remote get-url origin)" gh-pages
rm -rf .git
echo "✓ veröffentlicht: https://fabianbuerkle2701-dev.github.io/$REPO/"
