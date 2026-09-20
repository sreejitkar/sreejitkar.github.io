#!/usr/bin/env python3
"""
Goodreads RSS Bookshelf Sync Script
Fetches Sreejit's Goodreads RSS feed and builds bookshelf.html
"""

import urllib.request
import ssl
import subprocess
import xml.etree.ElementTree as ET
import html
import os
import sys

RSS_URL = "https://www.goodreads.com/review/list_rss/179933801?key=aTpZ_AKCdgxeSs5Ur9670QSqXDlQnVi1taJ1ZdeqvQ97kgs4&shelf=%23ALL%23"

def fetch_rss():
    # Attempt with unverified SSL context first for macOS Python environments
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(
            RSS_URL,
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        )
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
            return response.read()
    except Exception:
        # Fallback to system curl
        res = subprocess.run(["curl", "-s", RSS_URL], capture_output=True, check=True)
        return res.stdout

def clean_shelf(s):
    if not s:
        return 'read'
    s = s.lower().strip()
    if 'currently-reading' in s:
        return 'currently-reading'
    if 'did-not-finish' in s:
        return 'did-not-finish'
    if 'to-read' in s:
        return 'to-read'
    return 'read'

def format_date(d_str):
    if not d_str:
        return ''
    try:
        parts = d_str.split()
        if len(parts) >= 4:
            return f"{parts[2]} {parts[3]}"
    except Exception:
        pass
    return ''

def parse_books(xml_data):
    root = ET.fromstring(xml_data)
    items = root.find('channel').findall('item')
    books = []
    
    for item in items:
        title = item.find('title').text or 'Untitled'
        author = ' '.join((item.find('author_name').text or 'Unknown').split())
        book_id = item.find('book_id').text or ''
        user_rating = int(item.find('user_rating').text or 0)
        raw_shelf = item.find('user_shelves').text if item.find('user_shelves') is not None else ''
        shelf = clean_shelf(raw_shelf)
        read_at = item.find('user_read_at').text if item.find('user_read_at') is not None and item.find('user_read_at').text else ''
        date_added = item.find('user_date_added').text if item.find('user_date_added') is not None and item.find('user_date_added').text else ''
        avg_rating = item.find('average_rating').text or ''
        
        # High quality image fallback
        large_img = item.find('book_large_image_url').text if item.find('book_large_image_url') is not None else ''
        med_img = item.find('book_medium_image_url').text if item.find('book_medium_image_url') is not None else ''
        small_img = item.find('book_image_url').text if item.find('book_image_url') is not None else ''
        img = large_img or med_img or small_img or ''
        
        url = f"https://www.goodreads.com/book/show/{book_id}"
        
        books.append({
            'id': book_id,
            'title': title,
            'author': author,
            'shelf': shelf,
            'rating': user_rating,
            'read_at': format_date(read_at),
            'date_added': format_date(date_added),
            'avg_rating': avg_rating,
            'image': img,
            'url': url
        })
    return books

def render_html(books):
    total = len(books)
    reading_cnt = sum(1 for b in books if b['shelf'] == 'currently-reading')
    read_cnt = sum(1 for b in books if b['shelf'] == 'read')
    toread_cnt = sum(1 for b in books if b['shelf'] == 'to-read')
    dnf_cnt = sum(1 for b in books if b['shelf'] == 'did-not-finish')

    cards_html = []
    for b in books:
        t_esc = html.escape(b['title'])
        a_esc = html.escape(b['author'])
        shelf = b['shelf']
        
        # Badge
        if shelf == 'currently-reading':
            badge_html = '<span class="book-badge reading"><span class="badge-dot"></span>Reading</span>'
        elif shelf == 'read':
            badge_html = '<span class="book-badge read">&#10003; Read</span>'
        elif shelf == 'to-read':
            badge_html = '<span class="book-badge to-read">Want to Read</span>'
        elif shelf == 'did-not-finish':
            badge_html = '<span class="book-badge dnf">DNF</span>'
        else:
            badge_html = f'<span class="book-badge">{html.escape(shelf)}</span>'
        
        # Rating & meta
        rating_html = ""
        if b['rating'] > 0:
            stars = "★" * b['rating'] + "☆" * (5 - b['rating'])
            rating_html = f'<span class="book-stars" title="Sreejit\'s rating: {b["rating"]}/5">{stars}</span>'
        elif b['avg_rating']:
            rating_html = f'<span class="book-avg-rating"><span class="star-glyph">★</span> {html.escape(b["avg_rating"])} avg</span>'
        
        date_str = b['read_at'] if b['read_at'] else (f"Added {b['date_added']}" if b['date_added'] else "")
        meta_date = f'<span class="book-date">{html.escape(date_str)}</span>' if date_str else ''

        card = f'''          <!-- Book: {t_esc} -->
          <article class="book-card" data-shelf="{shelf}">
            <div class="book-cover-wrap">
              <img src="{html.escape(b['image'])}" alt="{t_esc} cover" class="book-cover" loading="lazy" onerror="this.style.display='none';this.parentElement.classList.add('no-cover');">
              <div class="book-cover-fallback" aria-hidden="true">📖</div>
            </div>
            <div class="book-info">
              <div class="book-header-row">
                {badge_html}
              </div>
              <h3 class="book-title">
                <a href="{html.escape(b['url'])}" target="_blank" rel="noopener noreferrer">{t_esc}</a>
              </h3>
              <div class="book-author">{a_esc}</div>
              <div class="book-footer">
                {rating_html}
                {meta_date}
              </div>
            </div>
          </article>'''
        cards_html.append(card)

    all_cards = "\n".join(cards_html)

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bookshelf &mdash; Sreejit Kar</title>
  <meta name="description" content="Bookshelf and reading log of Sreejit Kar. Tracked in real-time via Goodreads: science fiction, systems engineering, history, and non-fiction.">
  <meta name="author" content="Sreejit Kar">
  
  <meta property="og:title" content="Bookshelf &mdash; Sreejit Kar">
  <meta property="og:description" content="Bookshelf and reading log of Sreejit Kar. Tracked in real-time via Goodreads.">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@100..900&family=Geist+Mono:wght@100..900&display=swap" rel="stylesheet">

  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="stylesheet" href="css/style.css">

  <script>
    (function() {{
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme) {{
        document.documentElement.setAttribute('data-theme', savedTheme);
      }} else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {{
        document.documentElement.setAttribute('data-theme', 'dark');
      }}
    }})();
  </script>
</head>
<body>
  <a href="#content" class="skip-link">Skip to content</a>

  <div class="site-wrapper">
    <!-- Sidebar / Nav Column -->
    <aside class="sidebar">
      <div class="sidebar-sticky">
        <header class="sidebar-header">
          <a href="index.html" class="brand-mark" aria-label="Sreejit Kar — Home">
            <svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <linearGradient id="orbit-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#10b981"/>
                  <stop offset="100%" stop-color="#00f0ff"/>
                </linearGradient>
                <filter id="neon-glow" x="-50%" y="-50%" width="200%" height="200%">
                  <feGaussianBlur stdDeviation="1.5" result="blur"/>
                  <feMerge>
                    <feMergeNode in="blur"/>
                    <feMergeNode in="SourceGraphic"/>
                  </feMerge>
                </filter>
              </defs>
              <rect width="36" height="36" rx="9" fill="currentColor" fill-opacity="0.08" stroke="url(#orbit-grad)" stroke-width="1.2" stroke-opacity="0.45" class="mark-squircle"/>
              <path d="M 18 7 A 11 11 0 0 1 29 18" stroke="url(#orbit-grad)" stroke-width="1.8" stroke-linecap="round"/>
              <path d="M 27 23 A 11 11 0 0 1 9 23" stroke="currentColor" stroke-opacity="0.25" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="2 2.5"/>
              <path d="M 7 18 A 11 11 0 0 1 15 7.5" stroke="url(#orbit-grad)" stroke-width="1.8" stroke-linecap="round"/>
              <circle cx="18" cy="7" r="2.2" fill="#10b981" filter="url(#neon-glow)"/>
              <circle cx="27.5" cy="23.5" r="1.8" fill="#00f0ff" filter="url(#neon-glow)"/>
              <circle cx="8.5" cy="23.5" r="1.8" fill="currentColor" fill-opacity="0.6"/>
              <circle cx="18" cy="18" r="3.2" fill="url(#orbit-grad)" filter="url(#neon-glow)"/>
              <circle cx="18" cy="18" r="1.4" fill="#ffffff"/>
            </svg>
          </a>

          <h1 class="author-name mobile-only">
            <a href="index.html">Sreejit Kar</a>
          </h1>

          <button id="theme-toggle" class="theme-toggle-btn" type="button" aria-label="Toggle theme">
            <svg class="sun-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
            <svg class="moon-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
            </svg>
          </button>
        </header>

        <nav class="nav-menu" aria-label="Main Navigation">
          <a href="index.html" class="nav-item">
            <span class="nav-dot"></span>
            <span>About</span>
          </a>
          <a href="projects.html" class="nav-item">
            <span class="nav-dot"></span>
            <span>Projects</span>
          </a>
          <a href="writing.html" class="nav-item">
            <span class="nav-dot"></span>
            <span>Writing</span>
          </a>
          <a href="bookshelf.html" class="nav-item active" aria-current="page">
            <span class="nav-dot"></span>
            <span>Bookshelf</span>
          </a>
        </nav>
      </div>
    </aside>

    <!-- Main Content Column -->
    <main id="content" class="main-content">
      <header class="hero-header">
        <div class="hero-watermark" aria-hidden="true">BOOKSHELF</div>
        <div class="hero-content">
          <h1 class="hero-title">Bookshelf</h1>
          <div class="hero-subtitle">
            <span class="hero-pulse" aria-hidden="true"></span>
            <span>{total} books tracked &middot; Synced via <a href="https://www.goodreads.com/review/list/179933801" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline;">Goodreads</a></span>
          </div>
        </div>
      </header>

      <div class="content-inner">
        <!-- Filter Bar -->
        <div class="books-filter" role="tablist" aria-label="Book Shelves">
          <button class="filter-btn active" data-filter="all" type="button">
            All <span class="filter-count">{total}</span>
          </button>
          <button class="filter-btn" data-filter="currently-reading" type="button">
            Reading <span class="filter-count">{reading_cnt}</span>
          </button>
          <button class="filter-btn" data-filter="read" type="button">
            Read <span class="filter-count">{read_cnt}</span>
          </button>
          <button class="filter-btn" data-filter="to-read" type="button">
            Want to Read <span class="filter-count">{toread_cnt}</span>
          </button>
          <button class="filter-btn" data-filter="did-not-finish" type="button">
            DNF <span class="filter-count">{dnf_cnt}</span>
          </button>
        </div>

        <!-- Books Grid -->
        <div class="books-grid" id="books-grid">
{all_cards}
        </div>

        <div id="books-empty-state" class="book-empty-state">
          No books found in this category.
        </div>
      </div>

      <!-- Footer -->
      <footer class="site-footer">
        <div>&copy; 2026 Sreejit Kar</div>
        <div class="footer-social-links">
          <a href="mailto:sreejitkar999@gmail.com" class="social-icon-link" title="Email" aria-label="Email">
            <svg viewBox="0 0 20 20" fill="currentColor">
              <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/>
              <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/>
            </svg>
          </a>
          <a href="https://github.com/sreejitkar" target="_blank" rel="noopener noreferrer" class="social-icon-link" title="GitHub" aria-label="GitHub">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
            </svg>
          </a>
          <a href="https://www.linkedin.com/in/sreejitkar/" target="_blank" rel="noopener noreferrer" class="social-icon-link" title="LinkedIn" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
            </svg>
          </a>
          <a href="https://twitter.com/quid_pro_kyu" target="_blank" rel="noopener noreferrer" class="social-icon-link" title="X (Twitter)" aria-label="X (Twitter)">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
          </a>
          <a href="https://www.instagram.com/sreejittt/" target="_blank" rel="noopener noreferrer" class="social-icon-link" title="Instagram" aria-label="Instagram">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
            </svg>
          </a>
        </div>
      </footer>
    </main>
  </div>

  <script src="js/main.js"></script>
</body>
</html>'''
    return page_html

def main():
    print("Fetching Goodreads RSS feed...")
    try:
        xml_data = fetch_rss()
    except Exception as e:
        print(f"Error fetching live RSS ({e}), checking scratch_rss.xml fallback...")
        if os.path.exists('scratch_rss.xml'):
            with open('scratch_rss.xml', 'rb') as f:
                xml_data = f.read()
        else:
            raise

    books = parse_books(xml_data)
    print(f"Parsed {len(books)} books.")

    html_out = render_html(books)
    with open('bookshelf.html', 'w', encoding='utf-8') as f:
        f.write(html_out)
    print("Wrote bookshelf.html successfully.")

if __name__ == '__main__':
    main()
