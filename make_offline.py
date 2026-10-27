#!/usr/bin/env python3
"""Create ONE completely self-contained HTML file (no server, no folder).

Run:  python3 make_offline.py
Output: /home/user/ThreadTrend-Studio-React-Offline.html

It inlines the built JS, CSS and every image as data URIs, and the app
automatically switches to HashRouter when opened from file://.
Double-click it — the entire 30+ route site works offline.
"""
import base64
import mimetypes
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = "/home/user/ThreadTrend-Studio-React-Offline.html"
os.chdir(ROOT)

# 1. Build + relative image paths
subprocess.run(["python3", "make_dist.py"], check=True)

DIST = os.path.join(ROOT, "dist")
IMGDIR = os.path.join(DIST, "images")

# 2. Data URI map for every image
img_map = {}
for name in sorted(os.listdir(IMGDIR)):
    p = os.path.join(IMGDIR, name)
    if not os.path.isfile(p):
        continue
    ext = name.rsplit(".", 1)[-1].lower()
    mime = "image/svg+xml" if ext == "svg" else mimetypes.guess_type(name)[0] or "application/octet-stream"
    with open(p, "rb") as f:
        img_map[name] = f"data:{mime};base64," + base64.b64encode(f.read()).decode()
print(f"embedded {len(img_map)} images ({sum(len(v) for v in img_map.values()) // 1024} KB of data URIs)")

html = open(os.path.join(DIST, "index.html"), encoding="utf-8").read()

# 3. Inline CSS
def inline_css(m):
    path = os.path.join(DIST, m.group(1).lstrip("./"))
    css = open(path, encoding="utf-8").read().replace("</style", "<\\/style")
    return "<style>\n" + css + "\n</style>"

html, ncss = re.subn(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"[^>]*>', inline_css, html)
print("inlined CSS files:", ncss)

# 4. Inline JS, with image references swapped to a shared lookup map
import json
map_js = "const __TTS_IMG_MAP__=" + json.dumps(img_map, separators=(",", ":")) + ";\n"

def inline_js(m):
    path = os.path.join(DIST, m.group(1).lstrip("./"))
    js = open(path, encoding="utf-8").read()
    # quoted "/images/x.jpg" -> shared map lookup (avoids huge duplication)
    js, n = re.subn(r'(["\'])(?:\./)?/images/([^"\']+)\1',
                    lambda q: '__TTS_IMG_MAP__[' + json.dumps(q.group(2)) + ']', js)
    print("  rewrote", n, "image references in JS")
    js = js.replace("</script", "<\\/script")
    return "<script>\n" + map_js + js + "\n</script>"

html, njs = re.subn(r'<script[^>]+src="([^"]+)"[^>]*></script>', inline_js, html)
print("inlined JS files:", njs)

# 5. Remaining HTML-level image attributes (favicon, OG image)
html = re.sub(r'(["\'])(?:\./)?/images/([^"\']+)\1',
              lambda m: m.group(1) + img_map.get(m.group(2), "/images/" + m.group(2)) + m.group(1), html)

# 5b. Vite puts the bundle in <head>. A classic inline script there would run
#     before <body> exists (React createRoot error #299), so move it to the end.
script_match = re.search(r"<script>\n.*?</script>", html, re.S)
if script_match:
    script_tag = script_match.group(0)
    html = html.replace(script_tag, "", 1)
    html = html.replace("</body>", script_tag + "\n  </body>", 1)
    print("moved inline script to end of <body>")

# 6. Add a clear owner note
note = """<!--
  ThreadTrend Studio — OFFLINE SINGLE-FILE PREVIEW
  ------------------------------------------------------------------
  100% self-contained: React app, CSS, all JS and all images are inlined.
  Double-click this file — no server, no internet, no other files needed.
  Navigation uses #hash routes because browsers block ES modules on file://.

  This is a PORTABLE PREVIEW, not the deployable source. To publish, use the
  full React project (threadtrend-studio-react) and upload its dist/ folder.
  See README.md in the project.
-->
"""
html = html.replace("<head>", "<head>\n" + note, 1)
# Always use hash routing in this portable bundle (also works inside sandboxed
# file viewers, where the protocol is not file: but there is still no server).
html = html.replace("<head>", "<head>\n  <script>window.__TTS_OFFLINE__=true;</script>", 1)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("wrote", OUT, f"({os.path.getsize(OUT) / 1024 / 1024:.2f} MB)")
