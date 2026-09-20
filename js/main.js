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
    const metaThemeColor = document.querySelector('meta[name="theme-color"]');
    if (metaThemeColor) {
      metaThemeColor.setAttribute('content', theme === 'dark' ? '#282a36' : '#ffffff');
    }
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

  // 2. Navigation State & Scroll-Spy
  function initNavigation() {
    const currentPath = window.location.pathname;
    const isHome = currentPath === '/' || 
                   currentPath.endsWith('/index.html') || 
                   currentPath.endsWith('/') || 
                   (!currentPath.includes('.html') && !currentPath.includes('/writing/'));

    const navItems = document.querySelectorAll('.nav-item');
    if (!navItems.length) return;

    function scrollActiveNavIntoView(activeItem) {
      if (!activeItem || window.innerWidth >= 768) return;
      const navMenu = document.querySelector('.nav-menu');
      if (!navMenu) return;

      const itemLeft = activeItem.offsetLeft;
      const itemWidth = activeItem.offsetWidth;
      const menuWidth = navMenu.offsetWidth;
      const targetScroll = itemLeft - (menuWidth / 2) + (itemWidth / 2);

      navMenu.scrollTo({
        left: targetScroll,
        behavior: 'smooth'
      });
    }

    if (!isHome) {
      // Subpage matching
      navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (!href) return;

        let isMatch = false;
        if (currentPath.includes('/writing/') || currentPath.endsWith('writing.html')) {
          isMatch = href.includes('writing.html');
        } else if (currentPath.includes('bookshelf.html')) {
          isMatch = href.includes('bookshelf.html');
        } else if (currentPath.includes('papershelf.html')) {
          isMatch = href.includes('papershelf.html');
        } else if (currentPath.includes('projects.html')) {
          isMatch = href.includes('work') || href.includes('projects.html');
        }

        if (isMatch) {
          item.classList.add('active');
          item.setAttribute('aria-current', 'page');
          scrollActiveNavIntoView(item);
        } else {
          item.classList.remove('active');
          item.removeAttribute('aria-current');
        }
      });
      return;
    }

    // Homepage: Dynamic in-page scrollspy
    const hashLinks = document.querySelectorAll('.nav-menu a[href^="#"]');
    if (!hashLinks.length) return;

    const sections = ['contact', 'now', 'work', 'about']
      .map(id => document.getElementById(id))
      .filter(Boolean);

    function setActiveSection(id) {
      let activeEl = null;
      hashLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === `#${id}`) {
          link.classList.add('active');
          link.setAttribute('aria-current', 'page');
          activeEl = link;
        } else {
          link.classList.remove('active');
          link.removeAttribute('aria-current');
        }
      });
      if (activeEl) {
        scrollActiveNavIntoView(activeEl);
      }
    }

    function onScroll() {
      const scrollY = window.scrollY || window.pageYOffset;
      const windowHeight = window.innerHeight;
      const docHeight = document.documentElement.scrollHeight;

      // Reached bottom of page -> activate contact
      if (scrollY + windowHeight >= docHeight - 40) {
        setActiveSection('contact');
        return;
      }

      // Near top of page -> activate about
      if (scrollY < 120) {
        setActiveSection('about');
        return;
      }

      // Detect section based on top offset
      let activeId = 'about';
      for (const section of sections) {
        const rect = section.getBoundingClientRect();
        if (rect.top <= windowHeight * 0.35) {
          activeId = section.id;
          break;
        }
      }
      setActiveSection(activeId);
    }

    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          onScroll();
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });

    // Click handler for instant active state update
    hashLinks.forEach(link => {
      link.addEventListener('click', () => {
        const targetId = link.getAttribute('href').replace('#', '');
        setActiveSection(targetId);
      });
    });

    // Check if initial URL has hash
    if (window.location.hash) {
      const targetId = window.location.hash.replace('#', '');
      if (document.getElementById(targetId)) {
        setActiveSection(targetId);
        return;
      }
    }

    onScroll();
  }

  // 3. Papershelf Domain Filter
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

  // 5. Header Scroll Elevation (Mobile Sticky Header)
  function initHeaderScroll() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;

    let ticking = false;
    function updateScrollState() {
      if (window.innerWidth < 768) {
        if (window.scrollY > 8) {
          sidebar.classList.add('is-scrolled');
        } else {
          sidebar.classList.remove('is-scrolled');
        }
      } else {
        sidebar.classList.remove('is-scrolled');
      }
    }

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          updateScrollState();
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });

    window.addEventListener('resize', updateScrollState, { passive: true });
    updateScrollState();
  }

  // Run on DOM ready
  function init() {
    initNavigation();
    initPapershelfFilter();
    initHeaderScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
