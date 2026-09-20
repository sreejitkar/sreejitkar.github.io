/**
 * Minimalist Personal Site Script
 * Lightweight theme management & navigation active state
 */

(function () {
  'use strict';

  // 1. Theme Toggle Management
  const themeToggle = document.getElementById('theme-toggle');

  function getPreferredTheme() {
    const saved = localStorage.getItem('theme');
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (themeToggle) {
      themeToggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || getPreferredTheme();
      const nextTheme = current === 'dark' ? 'light' : 'dark';
      applyTheme(nextTheme);
    });
  }

  // Listen for system theme changes if user hasn't overridden
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });

  // 2. Active Nav State
  function setActiveNav() {
    const currentPath = window.location.pathname;
    const navItems = document.querySelectorAll('.nav-item');
    
    navItems.forEach(item => {
      const href = item.getAttribute('href');
      if (!href) return;

      const isHome = (href === '/' || href === './' || href === 'index.html') && 
                     (currentPath === '/' || currentPath.endsWith('index.html') || currentPath === '');
      
      const isMatch = isHome || (href !== '/' && href !== './' && href !== 'index.html' && currentPath.includes(href.replace('.html', '')));

      if (isMatch) {
        item.classList.add('active');
        item.setAttribute('aria-current', 'page');
      } else {
        item.classList.remove('active');
        item.removeAttribute('aria-current');
      }
    });
  }

  // 3. Bookshelf Category Filter
  function initBookshelfFilter() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const bookCards = document.querySelectorAll('.book-card');
    const emptyState = document.getElementById('books-empty-state');

    if (!filterBtns.length || !bookCards.length) return;

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const category = btn.getAttribute('data-filter');

        // Update active button
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Filter cards
        let visibleCount = 0;
        bookCards.forEach(card => {
          const cardCat = card.getAttribute('data-shelf');
          if (category === 'all' || cardCat === category) {
            card.style.display = 'flex';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        });

        if (emptyState) {
          emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
        }
      });
    });
  }

  // 4. Papershelf Domain Filter
  function initPapershelfFilter() {
    const filterBtns = document.querySelectorAll('.paper-filter-btn');
    const paperCards = document.querySelectorAll('.paper-card');
    const emptyState = document.getElementById('papers-empty-state');

    if (!filterBtns.length || !paperCards.length) return;

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const category = btn.getAttribute('data-filter');

        // Update active button
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Filter cards
        let visibleCount = 0;
        paperCards.forEach(card => {
          const cardDomain = card.getAttribute('data-domain');
          if (category === 'all' || cardDomain === category) {
            card.style.display = 'flex';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        });

        if (emptyState) {
          emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
        }
      });
    });
  }

  // Run on DOM ready
  function init() {
    setActiveNav();
    initBookshelfFilter();
    initPapershelfFilter();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
