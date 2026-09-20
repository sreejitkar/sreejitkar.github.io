# Personal Website — Sreejit Kar

A minimalist, high-craft, lightweight personal website designed for hosting on [GitHub Pages](https://pages.github.com/).

Inspired by [Mitchell Hashimoto's personal website](https://mitchellh.com/) and classic typographic minimalism.

## Features

- **Zero Runtime Overhead / Dependencies:** Pure HTML5, modern CSS3, and ~1KB of vanilla JavaScript. Zero `node_modules`, zero build steps, 100/100 Lighthouse performance.
- **Typographic Craft:** Timeless serif prose paired with crisp sans-serif headings and monospace accents.
- **Adaptive Dark Mode:** Automatic system preference detection + manual toggle button with local persistence (`localStorage`) and zero flash of unstyled content (anti-FOUC).
- **Mitchell Hashimoto-style Navigation:** Sticky sidebar with active dot indicator that scales dynamically based on current page.
- **Responsive Architecture:** Seamless transition between desktop two-column sidebar layout and mobile-friendly view.
- **GitHub Pages Ready:** Includes `.nojekyll`, `404.html`, responsive SVG favicon, and Open Graph metadata.

## File Structure

```text
.
├── index.html                    # About / Home page
├── projects.html                 # Projects & open-source work
├── writing.html                  # Essays and technical notes index
├── writing/
│   └── simplicity-in-distributed-systems.html # Sample essay page
├── 404.html                      # Custom 404 page for GitHub Pages
├── favicon.svg                   # Adaptive SVG monogram favicon
├── .nojekyll                     # Tells GitHub Pages to bypass Jekyll processing
├── css/
│   └── style.css                 # Complete theme and layout stylesheet
├── js/
│   └── main.js                   # Minimal theme switcher and active nav handler
└── README.md                     # Documentation
```

## Local Preview

You can preview the site locally using Python's built-in web server:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

Alternatively, you can directly double-click `index.html` to view it in any modern browser.

## Deploying to GitHub Pages

### Option 1: Root User Site (`sreejitkar.github.io`)
If you want the site hosted at `https://sreejitkar.github.io`:
1. Push this repository's contents to your `sreejitkar.github.io` repository on GitHub:
   ```bash
   git remote add origin git@github.com:sreejitkar/sreejitkar.github.io.git
   git branch -M main
   git push -u origin main --force
   ```
2. In your GitHub repository, go to **Settings → Pages**.
3. Under **Build and deployment**, set Source to **Deploy from a branch** and choose `main` / `/ (root)`.

### Option 2: Project Repository (`sreejitkar.github.io/me`)
If you prefer keeping this in a repository named `me`:
1. Create a repository named `me` on GitHub.
2. Push your code:
   ```bash
   git remote add origin git@github.com:sreejitkar/me.git
   git branch -M main
   git push -u origin main
   ```
3. In your repo settings, go to **Settings → Pages** and enable GitHub Pages on branch `main`.

### Custom Domain (Optional)
To use a custom domain (e.g. `sreejitkar.com`):
1. Create a file named `CNAME` containing your domain name:
   ```bash
   echo "sreejitkar.com" > CNAME
   ```
2. Commit and push it to GitHub.
3. Configure your DNS provider with GitHub Pages CNAME / A records.
