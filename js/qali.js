/**
 * QALI.labs — Micro-interactions & Telemetry Engine
 * Zero dependencies, < 2.5KB vanilla JavaScript.
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeManagement();
  initCapabilityInteractions();
  initTelemetryCursor();
  initEmailCopy();
  initKeyboardNavigation();
});

/**
 * Adaptive Theme Toggle (Light / Dark Mode)
 */
function initThemeManagement() {
  const themeToggle = document.getElementById('theme-toggle');

  function getActiveTheme() {
    const saved = localStorage.getItem('qali-theme') || localStorage.getItem('theme');
    if (saved) return saved;
    return 'dark'; // Default to technical dark aesthetic for QALI.labs
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('qali-theme', theme);
    localStorage.setItem('theme', theme);

    const metaThemeColor = document.querySelector('meta[name="theme-color"]');
    if (metaThemeColor) {
      metaThemeColor.setAttribute('content', theme === 'dark' ? '#000000' : '#ffffff');
    }

    if (themeToggle) {
      themeToggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || getActiveTheme();
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
    });
  }

  // Listen to OS preference change if not explicitly overridden
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('qali-theme') && !localStorage.getItem('theme')) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });
}

/**
 * Interactive Capabilities List & Schematic Viewport Switcher
 */
function initCapabilityInteractions() {
  const rows = document.querySelectorAll('.capability-row');
  const panes = document.querySelectorAll('.schematic-pane');
  const viewportTitle = document.getElementById('viewport-title');
  const viewportLatency = document.getElementById('viewport-latency');

  if (!rows.length || !panes.length) return;

  const titles = {
    '01': 'SYS_01 // DISTRIBUTED KERNEL & DATA BUS',
    '02': 'SYS_02 // NEURAL LATENT ATTENTION TENSOR',
    '03': 'SYS_03 // VIEWPORT SUB-PIXEL GEOMETRY',
    '04': 'SYS_04 // RUNTIME TRACE & LATENCY SPECTROGRAM',
    '05': 'SYS_05 // ARCHITECTURAL INFLECTION MATRIX'
  };

  const latencies = {
    '01': '0.12ms',
    '02': '1.40ms',
    '03': '0.04ms',
    '04': '0.08ms',
    '05': '0.21ms'
  };

  function activate(id) {
    rows.forEach(r => {
      const match = r.getAttribute('data-cap') === id;
      r.classList.toggle('is-active', match);
      r.setAttribute('aria-selected', match ? 'true' : 'false');
    });

    panes.forEach(p => {
      p.classList.toggle('active', p.id === `schematic-${id}`);
    });

    if (viewportTitle && titles[id]) {
      viewportTitle.textContent = titles[id];
    }
    if (viewportLatency && latencies[id]) {
      viewportLatency.textContent = `TRACE: ${latencies[id]}`;
    }
  }

  rows.forEach(row => {
    const id = row.getAttribute('data-cap');

    row.addEventListener('mouseenter', () => {
      activate(id);
      document.body.classList.add('cursor-active');
    });

    row.addEventListener('mouseleave', () => {
      document.body.classList.remove('cursor-active');
    });

    row.addEventListener('focus', () => {
      activate(id);
    });

    row.addEventListener('click', (e) => {
      e.preventDefault();
      activate(id);
    });
  });
}

/**
 * Precision Telemetry Cursor with Coordinate Readout
 */
function initTelemetryCursor() {
  // Only activate for mouse/pointer devices
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    return;
  }

  const cursor = document.getElementById('telemetry-cursor');
  const hud = document.getElementById('cursor-hud');
  if (!cursor || !hud) return;

  let mouseX = -100;
  let mouseY = -100;
  let rafId = null;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    if (!rafId) {
      rafId = requestAnimationFrame(() => {
        cursor.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
        const padX = String(Math.round(mouseX)).padStart(4, '0');
        const padY = String(Math.round(mouseY)).padStart(4, '0');
        hud.textContent = `LOC: [${padX}, ${padY}]`;
        rafId = null;
      });
    }
  }, { passive: true });

  // Add cursor active state for all links and buttons
  document.querySelectorAll('a, button, [role="button"]').forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-active'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-active'));
  });
}

/**
 * Email copy helper with telemetry feedback
 */
function initEmailCopy() {
  const trigger = document.getElementById('email-copy-btn');
  const feedback = document.getElementById('copy-feedback');

  if (!trigger) return;

  trigger.addEventListener('click', async () => {
    const email = trigger.getAttribute('data-email') || 'labs.sreejitkar@gmail.com';
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(email);
      } else {
        const textarea = document.createElement('textarea');
        textarea.value = email;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
      }

      if (feedback) {
        feedback.textContent = 'ADDRESS COPIED // BUFFER READY';
        feedback.classList.add('active');
        setTimeout(() => {
          feedback.classList.remove('active');
        }, 2400);
      }
    } catch (err) {
      window.location.href = `mailto:${email}`;
    }
  });
}

/**
 * Keyboard Navigation for Capabilities List
 */
function initKeyboardNavigation() {
  const rows = Array.from(document.querySelectorAll('.capability-row'));
  rows.forEach((row, idx) => {
    row.addEventListener('keydown', (e) => {
      let targetIdx = null;
      if (e.key === 'ArrowDown') {
        targetIdx = (idx + 1) % rows.length;
      } else if (e.key === 'ArrowUp') {
        targetIdx = (idx - 1 + rows.length) % rows.length;
      }

      if (targetIdx !== null) {
        e.preventDefault();
        rows[targetIdx].focus();
        rows[targetIdx].click();
      }
    });
  });
}
