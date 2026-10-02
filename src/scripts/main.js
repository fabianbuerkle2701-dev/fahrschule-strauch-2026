// Fahrschule Strauch: Verhalten der Bausteine nach shophoki.com.
// Ohne Abhängigkeiten. Alles respektiert prefers-reduced-motion.

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const isRu = document.documentElement.lang.startsWith('ru');

/* --- Kopfzeile: nach dem ersten Scrollen schwebende Pille ---------------- */
function initHeader() {
  const header = document.querySelector('[data-header]');
  if (!header) return;
  const sentinel = document.createElement('div');
  sentinel.setAttribute('aria-hidden', 'true');
  sentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:40px;pointer-events:none';
  document.body.prepend(sentinel);
  new IntersectionObserver(([entry]) => header.classList.toggle('is-scrolled', !entry.isIntersecting)).observe(sentinel);
}

/* --- Menü-Schublade -------------------------------------------------------- */
function initMenu() {
  const menu = document.querySelector('[data-menu]');
  const openBtn = document.querySelector('[data-menu-open]');
  if (!menu || !openBtn) return;
  const closeBtn = menu.querySelector('[data-menu-x]');
  let lastFocus = null;
  const focusables = () => [...menu.querySelectorAll('a[href], button:not([disabled])')];

  const open = () => {
    lastFocus = document.activeElement;
    menu.hidden = false;
    openBtn.setAttribute('aria-expanded', 'true');
    document.documentElement.style.overflow = 'hidden';
    requestAnimationFrame(() => {
      menu.classList.add('is-open');
      requestAnimationFrame(() => closeBtn.focus({ preventScroll: true }));
    });
  };
  const close = () => {
    if (!menu.classList.contains('is-open')) return;
    menu.classList.remove('is-open');
    openBtn.setAttribute('aria-expanded', 'false');
    document.documentElement.style.overflow = '';
    const done = () => {
      if (!menu.classList.contains('is-open')) menu.hidden = true;
    };
    reduceMotion.matches ? done() : setTimeout(done, 420);
    (lastFocus || openBtn).focus({ preventScroll: true });
  };

  openBtn.addEventListener('click', open);
  menu.querySelectorAll('[data-menu-close]').forEach((el) => el.addEventListener('click', close));
  menu.addEventListener('click', (e) => {
    if (e.target.closest('a')) close();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') close();
  });
  menu.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    const items = focusables();
    const first = items[0];
    const last = items[items.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });
}

/* --- Scroll-Reveal -------------------------------------------------------- */
function initReveal() {
  const items = document.querySelectorAll('[data-reveal]');
  if (!items.length) return;
  if (reduceMotion.matches || !('IntersectionObserver' in window)) {
    items.forEach((el) => el.classList.add('is-visible'));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      }
    },
    { threshold: 0.12, rootMargin: '0px 0px -6% 0px' },
  );
  items.forEach((el) => io.observe(el));
}

/* --- Waagerechte Reihen: Fortschrittsbalken und Pfeil (hoki-*__sbar) ------ */
function initRows() {
  document.querySelectorAll('[data-row]').forEach((row) => {
    let bar = row.nextElementSibling;
    if (!bar || !bar.matches('[data-sbar]')) bar = null;
    const fill = bar?.querySelector('.sbar__fill');
    const next = bar?.querySelector('[data-sbar-next]');
    const step = () => {
      const item = row.firstElementChild;
      const gap = parseFloat(getComputedStyle(row).columnGap) || 0;
      return item ? item.getBoundingClientRect().width + gap : row.clientWidth * 0.8;
    };
    const update = () => {
      const max = row.scrollWidth - row.clientWidth;
      if (bar) bar.hidden = max < 4;
      if (!fill || max < 4) return;
      const visible = row.clientWidth / row.scrollWidth;
      fill.style.width = `${Math.min(100, (visible + (row.scrollLeft / max) * (1 - visible)) * 100)}%`;
    };
    next?.addEventListener('click', () => {
      const max = row.scrollWidth - row.clientWidth;
      const behavior = reduceMotion.matches ? 'auto' : 'smooth';
      if (row.scrollLeft >= max - 4) row.scrollTo({ left: 0, behavior });
      else row.scrollBy({ left: step(), behavior });
    });
    row.addEventListener('scroll', () => requestAnimationFrame(update), { passive: true });
    new ResizeObserver(update).observe(row);
    update();
  });
}

/* --- Instagram-Karussell (Coverflow) ------------------------------------- */
function initFlow() {
  const flow = document.querySelector('[data-flow]');
  if (!flow) return;
  const items = [...flow.querySelectorAll('[data-flow-item]')];
  const n = items.length;
  let active = Math.floor(n / 2);
  let timer = null;

  const render = () => {
    items.forEach((item, i) => {
      let o = i - active;
      if (o > n / 2) o -= n;
      if (o < -n / 2) o += n;
      item.style.setProperty('--o', o);
      item.style.setProperty('--a', Math.abs(o));
      const on = o === 0;
      item.classList.toggle('is-active', on);
      on ? item.setAttribute('aria-current', 'true') : item.removeAttribute('aria-current');
      item.tabIndex = Math.abs(o) <= 1 ? 0 : -1;
    });
  };
  const go = (i) => {
    active = (i + n) % n;
    render();
  };
  items.forEach((item, i) => item.addEventListener('click', () => go(i)));
  flow.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') go(active + 1);
    if (e.key === 'ArrowLeft') go(active - 1);
  });
  // Wischen
  let startX = null;
  flow.addEventListener('pointerdown', (e) => (startX = e.clientX));
  flow.addEventListener('pointerup', (e) => {
    if (startX === null) return;
    const dx = e.clientX - startX;
    startX = null;
    if (Math.abs(dx) > 40) go(active + (dx < 0 ? 1 : -1));
  });
  // langsames automatisches Weiterdrehen, solange sichtbar und nicht berührt
  const stop = () => clearInterval(timer);
  const start = () => {
    stop();
    if (!reduceMotion.matches) timer = setInterval(() => go(active + 1), 4200);
  };
  new IntersectionObserver(([entry]) => (entry.isIntersecting ? start() : stop())).observe(flow);
  flow.addEventListener('pointerenter', stop);
  flow.addEventListener('pointerleave', start);
  flow.addEventListener('focusin', stop);
  render();
}

/* --- Wechselndes Wort in der Überschrift (hoki-rot) ----------------------- */
function initRotate() {
  document.querySelectorAll('[data-rot]').forEach((rot) => {
    const words = [...rot.querySelectorAll('.rot__w')];
    if (words.length < 2 || reduceMotion.matches) return;
    let i = 0;
    setInterval(() => {
      const cur = words[i];
      i = (i + 1) % words.length;
      cur.classList.remove('is-on');
      cur.classList.add('is-out');
      words[i].classList.remove('is-out');
      words[i].classList.add('is-on');
      setTimeout(() => cur.classList.remove('is-out'), 300);
    }, 2400);
  });
}

/* --- FAQ: Filter-Chips --------------------------------------------------- */
function initFaq() {
  document.querySelectorAll('[data-faq]').forEach((faq) => {
    const chips = [...faq.querySelectorAll('[data-faq-chip]')];
    const items = [...faq.querySelectorAll('[data-cat]')];
    chips.forEach((chip) =>
      chip.addEventListener('click', () => {
        const cat = chip.dataset.faqChip;
        chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
        items.forEach((item) => {
          item.hidden = cat !== 'alle' && !item.dataset.cat.split(' ').includes(cat);
          if (item.hidden) item.open = false;
        });
      }),
    );
  });
}

/* --- Drei Schritte (hoki-pz): Schritt unter dem Zeiger hervorheben -------- */
function initSteps() {
  document.querySelectorAll('[data-steps]').forEach((list) => {
    const steps = [...list.children];
    const on = (s) => steps.forEach((x) => x.classList.toggle('on', x === s));
    steps.forEach((s) => {
      s.addEventListener('pointerenter', () => on(s));
      s.addEventListener('focusin', () => on(s));
    });
  });
}

/* --- Sprachwahl: Daumen gleitet vor dem Seitenwechsel ---------------------- */
function initLangSwitch() {
  const sw = document.querySelector('[data-lang-switch]');
  if (!sw) return;
  sw.querySelectorAll('.lang__opt').forEach((opt) => {
    opt.addEventListener('click', (e) => {
      if (opt.hasAttribute('aria-current')) {
        e.preventDefault();
        return;
      }
      if (reduceMotion.matches) return;
      e.preventDefault();
      sw.querySelector('.lang__thumb').style.translate = isRu ? '0 0' : '100% 0';
      sw.querySelectorAll('.lang__opt').forEach((o) => (o === opt ? o.setAttribute('aria-current', 'true') : o.removeAttribute('aria-current')));
      setTimeout(() => (window.location.href = opt.href), 240);
    });
  });
}

initHeader();
initMenu();
initReveal();
initRows();
initFlow();
initRotate();
initFaq();
initSteps();
initLangSwitch();
