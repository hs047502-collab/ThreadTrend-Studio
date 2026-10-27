# ThreadTrend Studio — React + TypeScript + Tailwind CSS

A complete, working **fashion affiliate content website**: affordable men’s streetwear (graphic T-shirts, hoodies, sneakers, casual outfits), aimed at readers in the United States.

Static, free to host, no backend, no API keys, no paid services. Built as a real React application — every route, component and data file in this README actually exists and runs.

> **Status:** working local preview (port 3000) + a single-file offline build. **Nothing has been published publicly.** Do not deploy until you confirm.

---

## ⚡ বাংলায় দ্রুত শুরু (Quick start)

| তুমি যা চাও | যা করবে |
|---|---|
| **এখুনি সাইট দেখতে** | উপরের **Live Preview** (port 3000) — অথবা `ThreadTrend-Studio-React-Offline.html` ফাইলটা ডাবল-ক্লিক করো (সব ভেতরে, ইন্টারনেট লাগবে না) |
| **নিজের কম্পিউটারে চালাতে** | `npm install` → `npm run dev` → `http://localhost:3000` |
| **Product / দাম / link বদলাতে** | `/manager` (Studio Manager) → Products ট্যাব → Export `products.ts` → `src/data/`-এ replace |
| **নিজের ডিজাইন আপলোড করতে** | `/manager` → Designs → **Add design** → ছবি সিলেক্ট → সাথে সাথে `/my-designs`-এ দেখা যাবে |
| **নতুন আর্টিকেল লিখতে** | `/manager` → Articles → **Add article**, অথবা সরাসরি `src/data/articles.ts` এডিট |
| **Affiliate link বসাতে** | `/manager` → Products → pencil → **Affiliate URL** → link paste → সাথে সাথেই সাইটে “Check price” বাটন বাস্তব লিংক হয়ে যাবে (নতুন ট্যাবে খুলবে)। `https://` ছাড়াও `store.com/x` লিখলেও চলবে। বানানো link কখনো দিও না |
| **Publish করতে** | `python3 make_dist.py` → পুরো **`dist/` ফোল্ডার** Netlify Drop-এ ড্রাগ করো (শুধু index.html নয়) |
| **ছবি বদলাতে** | সব ছবি `public/images/`-এ • সাইট কোথায় কোন ছবি ব্যবহার করছে: `src/data/*.ts` • নতুন ইলাস্ট্রেশন: `python3 scripts/make_illustrations.py` |
| **Social link বদলাতে** | `/manager` → Settings → Facebook / Pinterest / Instagram / YouTube / TikTok URL (খালি রাখলে সেই আইকনটাই দেখাবে না) |
| **সবচেয়ে বড় নোট** | Contact form, newsletter, analytics, POD checkout — **কোনোটাই connected নয়**। সাইটে স্পষ্ট লেখা আছে। §9 দেখো |

---

## 1. What this is

An independent menswear publishing site: style guides, outfit ideas, buying guides, structured product write-ups, a design portfolio and clear affiliate disclosures.

| | |
|---|---|
| **Brand** | ThreadTrend Studio · *Wear Your Style. Discover Your Trend.* |
| **Niche** | Affordable men’s streetwear — graphic tees, hoodies, sneakers, casual outfits |
| **Audience** | United States, English (US), plus international readers |
| **Palette** | `#111111` ink · `#FFFFFF` white · `#F7F5F0` cream · `#D8C3A5` beige · `#666666` stone |
| **Typography** | System serif display + system sans body — zero web-font requests |
| **Cost** | $0. No domain, subscription, paid API or paid integration was purchased |

### Honesty rules baked into the build

We deliberately **do not invent**: brand names, prices, ratings, user reviews, stock levels, hands-on testing, partnerships, testimonials, business addresses, contact details or affiliate URLs.

- Every product is a clearly labelled **demo listing** (`demo: true`) with `brand: ''`, `price: null`, `specs: []`, `affiliateUrl: ''`.
- A CTA becomes an external link **only** when you supply a real `https://` affiliate URL. It then gets `rel="sponsored nofollow noopener noreferrer"`. Until then it is visibly disabled and explained.
- `affiliateStatus` in `src/data/site.ts` states plainly that **no affiliate programme is active**.
- Review pages say outright when a product has **not** been handled. There is a `handsOnTested` flag that you should only tick if true.
- The contact form and newsletter do not pretend to send anything.

---

## 2. Three ways to view the site

| # | Method | Command / file | Notes |
|---|---|---|---|
| 1 | **Live dev preview** | `npm run dev` → `http://localhost:3000` | Hot reload while editing |
| 2 | **Offline single file** | `ThreadTrend-Studio-React-Offline.html` (in `/home/user`) | Double-click. ~3.4 MB: JS, CSS and all 45 images inlined. Uses `#/hash` routes. Regenerate with `python3 make_offline.py` |
| 3 | **Built site (deployable)** | `python3 make_dist.py` → `dist/` | Clean URLs, `_redirects` + `404.html` for SPA fallback. Upload the whole folder |

`src/main.tsx` switches to `HashRouter` automatically on `file://` or when `window.__TTS_OFFLINE__` is set — which is why the offline file works with no server.

Do **not** double-click `dist/index.html`: browsers block ES modules on `file://`. Use option 2 for that.

---

## 3. Stack & project structure (all files included)

```
threadtrend-studio-react/
├── index.html                     # HTML shell, meta, OG tags, favicon
├── package.json                   # react, react-dom, react-router-dom, vite, tailwind, typescript
├── tsconfig.json · vite.config.ts  # strict TS · base '/', host 0.0.0.0, port 3000
├── tailwind.config.js · postcss.config.js
├── public/
│   ├── images/                    # 72 assets: logo, favicon, 29 photography files
│   │                              # (JPG) + original SVG illustrations/mockups
│   ├── _redirects                 # SPA fallback: Netlify / Cloudflare Pages
│   ├── 404.html                   # styled 404 page
│   ├── robots.txt · sitemap.xml    # 38 URLs — replace the placeholder domain
├── scripts/
│   ├── make_sitemap.py            # rebuilds sitemap.xml from the data files
│   └── make_illustrations.py      # regenerates every SVG illustration (original art)
├── src/
│   ├── main.tsx                   # Router + ContentProvider
│   ├── App.tsx                    # every route
│   ├── index.css                  # Tailwind layers + design system
│   ├── types.ts                   # Product / Article / Design / SiteSettings
│   ├── lib/
│   │   ├── affiliate.ts           # normalises affiliate URLs (bare domain → https), safety checks
│   │   ├── seo.ts                 # useSEO: title, description, canonical, OG, robots
│   │   ├── storage.ts             # safe localStorage, file→dataURL, downloads, slugify
│   │   └── ContentContext.tsx     # local "CMS" state shared by all pages
│   ├── data/
│   │   ├── site.ts                # ⭐ settings, hero copy, nav categories, values
│   │   ├── products.ts            # ⭐ 13 demo product listings (no brand/price/link)
│   │   ├── articles.ts            # ⭐ 11 original articles (typed blocks)
│   │   └── designs.ts             # ⭐ 6 design placeholders
│   ├── components/
│   │   ├── Layout.tsx             # disclosure bar, header, mobile nav, search overlay, footer
│   │   ├── Cards.tsx              # ProductCard, ArticleCard, CategoryCard, DesignCard, StatCard
│   │   ├── Disclosure.tsx         # DisclosureNotice, DisclosurePanel, DemoSetupNotice
│   │   ├── UI.tsx                 # Badge, SectionHeading, Breadcrumbs, PageHeader, EmptyState…
│   │   ├── ArticleBody.tsx        # typed article block renderer with [inline links](/path)
│   │   ├── SocialLinks.tsx        # Follow row, driven by settings.social (footer + contact)
│   │   ├── Newsletter.tsx         # demo signup, honest "not connected"
│   │   └── Icons.tsx              # inline SVG icon set (no icon library)
│   └── pages/
│       ├── Home.tsx               # hero, values, categories, latest, comparisons, picks, newsletter
│       ├── CategoryPage.tsx       # /mens-fashion /womens-fashion /shoes-accessories
│       ├── GuidesIndex.tsx        # /style-guides /outfit-ideas /shopping-guides (filter + search)
│       ├── ArticlePage.tsx        # /guides/:slug + sticky TOC + related
│       ├── ReviewsIndex.tsx       # /reviews (filter + search)
│       ├── ReviewPage.tsx         # /reviews/:slug, honesty panel, disabled-until-approved CTA
│       ├── About.tsx · Contact.tsx
│       ├── LegalPrivacy.tsx · LegalTerms.tsx · LegalDisclosure.tsx
│       ├── LegalPages.tsx         # barrel re-export for the three pages above
│       ├── MyDesigns.tsx · Manager.tsx · SearchPage.tsx · NotFound.tsx
├── make_dist.py · make_offline.py
└── README.md                      # this file
```

**Routes:** `/` · `/mens-fashion` · `/womens-fashion` · `/shoes-accessories` · `/style-guides` · `/outfit-ideas` · `/shopping-guides` · `/guides/:slug` (11) · `/reviews` · `/reviews/:slug` (13) · `/about` · `/contact` · `/privacy-policy` · `/terms` · `/affiliate-disclosure` · `/my-designs` · `/manager` (noindex) · `/search` (noindex) · `*` (404)

Three short aliases redirect to the section they belong to, so older links never 404: `/t-shirts` → `/mens-fashion#streetwear`, `/hoodies` → `/mens-fashion#casual`, `/sneakers` → `/shoes-accessories`.

T-shirt, hoodie and sneaker content itself lives where the design puts it: the **section anchors** on `/mens-fashion` (`#streetwear`, `#casual`), the shoe/accessory category page, the **review filter pills** (which include T-Shirts, Sneakers, Boots, Bags) and the `/shopping-guides` articles — exactly as in the approved layout.

---

## 4. Local development

```bash
npm install
npm run dev            # http://localhost:3000  (host 0.0.0.0, preview-friendly)
npm run typecheck      # tsc --noEmit  — passes with zero errors
npm run build          # tsc --noEmit && vite build
npm run preview        # serve the built dist/ locally
python3 make_dist.py   # build + dist/404.html + README-DIST.txt
python3 make_offline.py# build + single-file offline HTML (inlines all images)
python3 scripts/make_sitemap.py        # rebuild public/sitemap.xml from the data
python3 scripts/make_illustrations.py  # regenerate the SVG artwork
```

---

## 5. Editing content

### 5.1 Studio Manager (`/manager`, noindex)

- **Products** — add / edit / delete listings. Brand, specs, pros/cons, verified price, retailer, **approved affiliate URL (with a live “Live on the site” status + Test link)**, demo & tested flags, image URL. Export `products.ts`.
- **Articles** — add / edit / delete. Body format: blank line = paragraph, `## ` = heading, `### ` = subheading, `- ` = bullet, `> ` = quote. Export `articles.ts`.
- **Designs** — upload an image (≤1.5 MB, stored as a data URL), edit title/description/category/status. Export `designs.ts`.
- **Settings** — contact email, site URL, **five social URLs (Facebook, Pinterest, Instagram, YouTube, TikTok)**, disclosure text, affiliate-status line, demo bar, last-updated date. Export a `site-settings.ts` snippet.
- **Export / Backup** — full JSON backup, import backup, reset everything.

> **Limitation, stated in the UI too:** browser `localStorage`, not a database. Edits live in one browser, are not synced, and do **not** change the deployed site. Export + replace `src/data/*.ts` and rebuild (see §12). In a sandboxed viewer storage is blocked — the UI warns and edits last only for the session.

#### Editing checklist (the short version)

| What you want to change | Where | Live immediately? |
|---|---|---|
| Add / edit a product | `/manager` → Products → **Add product** / pencil | Yes, in this browser |
| Add an affiliate link | `/manager` → Products → pencil → **Affiliate URL** → paste → done | Yes — the public button becomes a real link on home, category, review and search cards |
| Remove an affiliate link | Clear the field | Yes — the button returns to the disabled “Link not set” state |
| Add / edit an article | `/manager` → Articles | Yes |
| Upload a design | `/manager` → Designs → Add design | Yes |
| Social links, email, disclosure text, preview bar | `/manager` → Settings | Yes |
| Publish any of the above to the live site | Export the `.ts` file from the tab → replace the file in `src/data/` → `python3 make_dist.py` | After rebuild (§12) |

Affiliate URLs are normalised, so **`https://store.com/x`, `store.com/x` and `www.store.com` all work**. The link opens in a new tab with `rel="sponsored nofollow noopener noreferrer"`, and a disclosure sits beside it.

### 5.2 Products & affiliate URLs (by hand)

```ts
{
  id: 'p-001', slug: 'heavyweight-cotton-tee',
  name: 'Heavyweight Cotton Crew Tee', brand: 'REAL BRAND',
  category: 'men', section: 'T-Shirts & Tops',
  image: '/images/product-heavyweight-tee.jpg', imageAlt: 'Describe the image',
  summary: '…', description: '…',
  specs: [{ label: 'Material', value: '100% cotton' }],   // verified only
  pros: ['…'], cons: ['…'],                              // include trade-offs
  price: 29.99, currency: 'USD', priceVerified: true, priceCheckedAt: '27 October 2026',
  retailer: 'Real Store',
  affiliateUrl: 'https://your-approved-link',             // any http(s) or bare domain
  demo: false, featured: true, tags: ['basics'],
  handsOnTested: false,                                  // true ONLY if you used it
}
```

Rules: get approved first; never invent a link; verify the price and date; publish only verifiable specs; use images you own or are licensed to use (most programmes require their own links/API); rebuild afterwards.

### 5.3 Articles

`src/data/articles.ts` holds 11 original articles built from typed blocks:

```ts
body: [
  p('Paragraph with an [internal link](/guides/how-to-choose-sneakers).'),
  h2('A heading'), h3('A subheading'),
  ul(['bullet']), ol(['step']), quote('Pull quote'),
  note('Title', 'Highlighted aside'),
  img('/images/article-capsule.svg', 'Descriptive alt', 'Optional caption'),
]
```

Set `slug`, `title`, `excerpt`, `category` (`Style Guides` / `Outfit Ideas` / `Buying Guides` / `Basics` / `Clothing Reviews` / `Budget Finds`), `readingTime`, `updated`, `image`, `imageAlt`, `tags`, `related`.

### 5.4 Images

| Kind | Files | How to change |
|---|---|---|
| Product photos | `public/images/product-*.jpg` (10) | Replace with your own shots at the same paths, or point `image` in `products.ts` elsewhere. Keep 4:3, ≤1600 px, and write a real `alt` |
| Illustrations | 32 `*.svg` (hero, categories, articles, designs, comparisons) | Edit `scripts/make_illustrations.py` and re-run — every shape is original geometry, no third-party art |
| Brand | `logo.png`, `favicon.png`, `og-cover.png` | Swap in your own; keep the same filenames |

**About the imagery:** product photos in this build were AI-generated for the project (no brand logos, no borrowed photography). 12 products are listed but 10 photos exist — the two accessory listings intentionally use SVG illustrations, because the daily AI-generation limit was reached mid-build. To finish the set, generate or photograph `product-cap.jpg` and `product-tote.jpg`, save them in `public/images/`, then change the two `image:` fields in `src/data/products.ts` from `accessories-cap.svg` / `accessories-tote.svg` to the new `.jpg` paths. Everything else stays the same.

---

## 6. Affiliate setup (the part that earns money)

1. Apply to programmes that fit affordable streetwear — brand-direct programmes, Awin, Impact, CJ, ShareASale, Rakuten. Amazon Associates is the easiest entry point but has the strictest rules.
2. Read the programme’s image and trademark rules before using any product photo.
3. Get your approved, tagged link (`?tag=…`, `?ref=…`, deep link, etc.).
4. Paste it into `affiliateUrl` in `/manager` or `products.ts`, set `demo: false`, add the verified price + date, rebuild.
5. The card and review page then render an external CTA with `rel="sponsored nofollow noopener noreferrer"`, plus disclosure directly beside it. It opens in a **new tab**, so the reader never loses your site.
6. Keep prices current — update `priceCheckedAt` monthly and say so.

**Never** hand-edit an affiliate URL into `Layout.tsx` or anywhere outside the data files: the CTA logic lives in `Cards.tsx` / `ReviewPage.tsx` and reads only `product.affiliateUrl` through `src/lib/affiliate.ts`.

### 6.1 How the link behaves for visitors

| State of `affiliateUrl` | What a visitor sees |
|---|---|
| empty | Disabled “Link not set” chip + “Affiliate link not configured” panel — nothing is clickable |
| `https://…` (or a bare domain) | “Check price” / “Check current price” button → opens the retailer in a new tab, `rel="sponsored nofollow noopener noreferrer"`, disclosure beside it |

## 6A. Social profiles

Facebook and Pinterest are wired up in `src/data/site.ts` → `DEFAULT_SETTINGS.social` and appear as icon links in:

- the **footer** on every page (opens in a new tab, `rel="noopener noreferrer"`, no invented profiles), and
- the **Contact** page, under “Follow the studio”.

```ts
social: {
  facebook:  'https://www.facebook.com/ThreadTrendStudio',
  pinterest: 'https://www.pinterest.com/threadtrendstudioofficial/',
  instagram: '',   // empty = icon is not rendered at all
  youtube: '',
  tiktok: '',
},
```

Change or add them in `/manager` → Settings (they update instantly in your browser) or in `src/data/site.ts` for the permanent build. An empty field simply disappears — no placeholder account is ever shown.

---

## 7. Legal & disclosure pages

- `/affiliate-disclosure` — plain-English explanation, current status line, how links work, what we will never do.
- `/privacy-policy` — no analytics, no ad cookies, localStorage note, GDPR/CCPA rights, children, security, changes.
- `/terms` — informational content only, we are not the seller, no warranty, IP, acceptable use, third-party links, services not connected, governing-law placeholder to fill in.
- `/about` — what the site is, editorial standards (six rules), how it is funded, and an explicit list of what is **not** connected.
- `/contact` — validates locally, then shows “Message prepared — but not sent” with the exact steps to connect an endpoint.

A disclosure bar sits above the header on every page, and `DisclosureNotice` / `DisclosurePanel` appear inside product grids, product cards, review pages and article footers.

> These are good-faith templates, **not legal advice**. Have them reviewed for your jurisdiction before commercial launch.

---

## 8. SEO

Implemented: unique `<title>` + meta description per route (`useSEO`), canonical URLs, Open Graph + Twitter cards with a 1200×630 `og-cover.png`, semantic landmarks (`header/nav/main/article/aside/footer`), one `<h1>` per page with logical `h2/h3`, descriptive `alt` on every image, clean URLs, internal links throughout, `robots.txt`, a 38-URL `sitemap.xml`, and `noindex` on `/manager`, `/search` and the 404 page.

Before publishing: replace `https://www.yourdomain.com` in `public/robots.txt` and `public/sitemap.xml`, set `siteUrl` in `src/data/site.ts`, rebuild, then submit the sitemap in Google Search Console / Bing Webmaster Tools. No ranking guarantees.

---

## 9. Integrations that are NOT connected (and how to connect them free)

| Feature | Current state | Free way to connect |
|---|---|---|
| **Contact form** | Validates locally, shows “not sent”. No data leaves the browser | Create a free endpoint (Formspree / Web3Forms / Netlify Forms). Replace `onSubmit` in `src/pages/Contact.tsx` with a `fetch()` POST. Add a real email in `site.ts` |
| **Newsletter** | Demo; stores nothing | Add a MailerLite / Buttondown / ConvertKit embed in `src/components/Newsletter.tsx`, then update `/privacy-policy` |
| **Analytics** | None. No cookies, no trackers | Cloudflare Web Analytics or Umami free tier; update the privacy policy and add consent if required |
| **Cookie consent** | Not needed — no non-essential cookies are set | Enable your host’s consent tool if you add analytics/ads |
| **Social links** | Empty by default; footer shows a setup note instead of invented profiles | Add real URLs in `/manager → Settings` or `site.ts` |
| **Affiliate programmes** | Not applied, not approved, not linked | Apply → get approved → paste tagged links (§6) |
| **Designs / POD** | Portfolio only. No cart, checkout or fulfilment | A shop needs a POD account (Printful/Printify), real product data, tax/shipping rules and a payment provider |
| **CMS / database** | `localStorage` via `/manager` | Optional free headless CMS (Sanity/Contentful/Strapi) mapped to `src/types.ts` |
| **Email / domain** | Empty. Nothing invented | Buy/connect a domain, set a real address, update `siteUrl`, sitemap, robots |

---

## 10. Performance & accessibility

- Static build: **352 KB JS (106 KB gzipped) + 37 KB CSS (6.9 KB gzipped)**. Images are local; product JPGs are ~90–280 KB, illustrations 8–19 KB SVG.
- Lazy loading on all non-hero images; explicit `width`/`height` on the logo; system font stacks — no CDN, no web fonts, no icon library.
- Skip-to-content link, `aria-label`s on icon-only buttons, keyboard-friendly search overlay (Esc closes), `<details>`-free but fully semantic markup, visible `:focus-visible` rings, `prefers-reduced-motion` respected, breadcrumbs with `aria-current`.
- Filter buttons use `aria-pressed`; tables have `caption`/`th scope`; every form control has a real `<label>`.

---

## 11. Deployment (free, only when you confirm)

```bash
python3 make_dist.py
```

Upload the **whole `dist/` folder** (not just `index.html`):

- **Netlify Drop** — `app.netlify.com/drop`, drag the folder. `_redirects` handles SPA routes.
- **Cloudflare Pages** — Workers & Pages → Create → Pages → Direct Upload.
- **GitHub Pages** — push `dist/` contents, enable Pages; `404.html` handles SPA routes.

Then: connect a custom domain, replace the placeholder domain in `robots.txt`/`sitemap.xml`, set `siteUrl`, rebuild + redeploy, submit the sitemap.

---

## 12. Publishing edits made in Studio Manager

1. In `/manager`, export `products.ts`, `articles.ts`, `designs.ts` and a full JSON backup.
2. Replace the matching files in `src/data/`.
3. Copy uploaded design images into `public/images/designs/` and rewrite their paths to `/images/designs/<file>` (uploads are data URLs inside `designs.ts` otherwise).
4. Mirror Settings into `src/data/site.ts` (fresh browsers read that file first).
5. `python3 make_dist.py` → deploy `dist/` → `python3 make_offline.py` to refresh the offline copy.

---

## 13. Quality checks performed (real Chromium, Playwright)

Tested against the dev server and the offline single file:

- ✅ Verified against the approved reference build: all **18 routes render identical text and identical class-for-class markup** (checked by diffing rendered DOM, not screenshots).
- ✅ **21 URLs** load with exactly **one `<h1>`**, a unique `<title>`, a meta description, `lang="en"` and **no console/page errors**.
- ✅ **Zero broken images** on every route, **zero images without `alt`** on public pages.
- ✅ **Zero horizontal overflow** at 390 px and 1440 px on every route; also checked at 1024 / 1280 px for the header.
- ✅ Header nav no longer wraps at 1024 px (whitespace-nowrap + tightened sizing); display headings resized for phones.
- ✅ Mobile menu opens; hero CTAs navigate to `/mens-fashion` and `/outfit-ideas`.
- ✅ Guide search box + category pills, review filter pills, search page (`/search?q=`), 404 for unknown slugs.
- ✅ Review CTA honesty: demo listing shows a disabled “Affiliate link not set yet”, **0** `rel="sponsored"` links exist.
- ✅ Contact form: 3 validation alerts on empty submit, then the “Message prepared — but not sent” panel.
- ✅ Studio Manager edit persists to `localStorage` and renders on the public review page.
- ✅ Offline single file: hash routing works, images inline, no errors, inside a 390 px viewport.
- ✅ `tsc --noEmit` and `vite build` pass with zero errors.

Not covered by automation: real-device testing, Lighthouse scoring, and legal review.

---

## 14. Troubleshooting

| Problem | Fix |
|---|---|
| Blank page opening `dist/index.html` directly | Browsers block ES modules on `file://`. Use the offline HTML or `npm run preview` |
| Deep-link 404 after deploy | Upload `_redirects` (Netlify/Cloudflare) or `404.html` (GitHub Pages) |
| Images missing after deploy | Upload the whole `dist/`, host at a domain root, or change `base` in `vite.config.ts` |
| Manager edits disappeared | They live in one browser — export and publish (§12) |
| “Link not set” on a card | No approved affiliate URL yet — add one (§6) |
| “Not verified yet” price | Set `price`, `priceVerified: true`, `priceCheckedAt` |
| Social icons missing | Expected until real URLs are added |
| Contact form says “not sent” | Expected — connect an endpoint (§9) |

---

## 15. What needs an account or money later

Nothing in this build does. Later you may want: a domain (~$10–14/yr, optional), affiliate programme approval (free, not guaranteed), free tiers for a form/email/analytics provider, and — only if you add a shop — a POD account plus a payment provider with their own fees. None of it is activated here, and the site never claims otherwise.

---

**Reminder:** this is a working local preview. **Do not publish publicly before you confirm.** When ready, follow §11 — or ask me to walk you through it.
