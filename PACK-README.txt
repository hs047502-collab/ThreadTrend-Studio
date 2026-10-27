ThreadTrend Studio — complete package (v2.2, 27 October 2026)
=============================================================

What's inside
-------------
threadtrend-studio-react/            Full React + TypeScript + Tailwind source
  ├── README.md                      Setup, editing, affiliate + social guide, deployment
  ├── CHANGELOG.md                   What changed in each version
  ├── src/                           All pages, components, data files
  ├── public/                        Images (72), robots.txt, sitemap.xml, _redirects, 404.html
  ├── scripts/                       make_sitemap.py, make_illustrations.py
  ├── dist/                          READY TO DEPLOY (drag this whole folder to Netlify Drop)
  ├── index.html · package.json · tsconfig.json · vite.config.ts · tailwind.config.js
  └── make_dist.py · make_offline.py

ThreadTrend-Studio-React-Offline.html   One single file — double-click it, works offline, no install

Quick start
-----------
1. See it immediately:  double-click ThreadTrend-Studio-React-Offline.html
2. Or run the source:   cd threadtrend-studio-react && npm install && npm run dev
                        then open http://localhost:3000
3. Edit anything:       open http://localhost:3000/manager  (products, articles, designs,
                        affiliate links, social links, disclosure text)
4. Publish:             python3 make_dist.py  → upload the whole dist/ folder

Affiliate links
---------------
/manager → Products → pencil → "Affiliate URL" → paste your approved link → done.
With or without https:// — both work. The button opens the retailer in a new tab with
rel="sponsored nofollow noopener noreferrer". Leave the field empty and the button stays
disabled ("Link not set"), so no visitor ever clicks a broken or invented link.

Social profiles already wired
-----------------------------
Facebook  https://www.facebook.com/ThreadTrendStudio
Pinterest https://www.pinterest.com/threadtrendstudioofficial/
Shown in the footer of every page and on the Contact page. Edit them in /manager → Settings.

Honesty rules kept in this build
--------------------------------
No invented brands, prices, ratings, reviews, stock or partnerships. All 13 listings are
labelled demo placeholders with empty brand/price/link. The contact form and newsletter say
clearly that no service is connected. Nothing has been published publicly.

Notes
-----
- node_modules is NOT included (run npm install — it is free and takes ~30 seconds).
- dist/ IS included, so you can publish without touching Node at all.
