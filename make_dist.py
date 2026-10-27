#!/usr/bin/env python3
"""Build the deployment-ready dist/ folder.

Run:  python3 make_dist.py
Then upload the WHOLE dist/ folder to Netlify Drop / Cloudflare Pages /
GitHub Pages. Keep _redirects and 404.html so clean URLs work on refresh.

For a double-clickable offline copy, run  python3 make_offline.py  instead —
it produces a single self-contained HTML file with everything inlined.
"""
import os
import shutil
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
DIST = os.path.join(ROOT, "dist")

print("1/2  Building with Vite…")
subprocess.run(["npm", "run", "build"], check=True)

print("2/2  Adding SPA fallbacks…")
# Netlify / Cloudflare Pages read _redirects (already in public/).
# GitHub Pages serves 404.html for unknown paths — a copy of index.html makes
# clean URLs such as /guides/... work there too.
shutil.copyfile(os.path.join(DIST, "index.html"), os.path.join(DIST, "404.html"))
print("     wrote dist/404.html")

readme = """ThreadTrend Studio — deployment build
======================================

HOW TO PUBLISH
  Upload this ENTIRE folder (not just index.html) to a free static host:
    • Netlify Drop        → app.netlify.com/drop  (drag this folder)
    • Cloudflare Pages    → Workers & Pages → Create → Pages → Direct Upload
    • GitHub Pages        → push this folder, enable Pages from the branch root

  _redirects  → SPA fallback for Netlify / Cloudflare Pages
  404.html    → SPA fallback for GitHub Pages
  Both are already included. Deep links like /style-guides will work.

  Set a custom domain, then replace the placeholder domain in
  public/robots.txt and public/sitemap.xml (in the SOURCE project) with your
  real domain, rebuild, and submit the sitemap to Google Search Console.

DO NOT DOUBLE-CLICK index.html
  Browsers block ES modules loaded from file://. For a portable, offline,
  double-clickable copy use the separate single-file build:
      ThreadTrend-Studio-React-Offline.html
  It contains the whole app, CSS and all images inline.

NOTE
  Edits made in /manager are stored only in that browser. Export from
  /manager and replace src/data/*.ts in the source project to publish them.
  See the project README.md for every manual setup step.
"""
open(os.path.join(DIST, "README-DIST.txt"), "w", encoding="utf-8").write(readme)
print("     wrote dist/README-DIST.txt")

size = sum(os.path.getsize(os.path.join(b, f)) for b, _, fs in os.walk(DIST) for f in fs)
print(f"\n✅ Deployment build ready: dist/ ({size / 1024 / 1024:.2f} MB)")
