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

/* --- Fahrschulauto fährt beim Scrollen die Straße am rechten Rand herunter --- */
function initDrive() {
  const drive = document.querySelector('[data-drive]');
  if (!drive) return;
  if (reduceMotion.matches) {
    drive.hidden = true;
    return;
  }
  const car = drive.querySelector('.drive__car');
  const root = document.documentElement;
  let last = window.scrollY;
  let vel = 0;
  let raf = 0;
  let stopTimer = 0;
  const update = () => {
    raf = 0;
    const max = root.scrollHeight - window.innerHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
    const headerH = parseFloat(getComputedStyle(root).getPropertyValue('--header-h')) || 72;
    const top = Math.max(16, headerH + 16 - window.scrollY);
    const body = car.getBoundingClientRect().width * (108 / 60);
    const y = top + p * (window.innerHeight - top - body - 18);
    const dy = window.scrollY - last;
    last = window.scrollY;
    vel = vel * 0.75 + dy * 0.25;
    const steer = Math.max(-9, Math.min(9, Math.sin(p * Math.PI * 14) * Math.min(1, Math.abs(vel) / 30) * 9));
    car.style.transform = `translate3d(0, ${y.toFixed(1)}px, 0) rotate(${steer.toFixed(2)}deg)`;
    if (dy !== 0) {
      car.classList.toggle('is-forward', dy > 0);
      car.classList.toggle('is-reverse', dy < 0);
      car.classList.remove('is-brake');
      clearTimeout(stopTimer);
      stopTimer = setTimeout(() => {
        car.classList.remove('is-forward', 'is-reverse');
        car.classList.add('is-brake');
        setTimeout(() => car.classList.remove('is-brake'), 700);
      }, 160);
    }
  };
  const queue = () => {
    if (!raf) raf = requestAnimationFrame(update);
  };
  window.addEventListener('scroll', queue, { passive: true });
  window.addEventListener('resize', queue);
  update();
}

/* --- Scroll-Effekte: Wort-für-Wort-Überschriften, einfahrende Karten, Parallaxe, Zähler --- */
function splitWords(el) {
  let i = 0;
  const walk = (node) => {
    for (const child of [...node.childNodes]) {
      if (child.nodeType === Node.TEXT_NODE) {
        const parts = child.textContent.split(/(\s+)/);
        const frag = document.createDocumentFragment();
        for (const part of parts) {
          if (!part) continue;
          if (/^\s+$/.test(part)) {
            frag.append(part);
            continue;
          }
          const w = document.createElement('span');
          w.className = 'w';
          const inner = document.createElement('span');
          inner.textContent = part;
          inner.style.setProperty('--i', i++);
          w.append(inner);
          frag.append(w);
        }
        child.replaceWith(frag);
      } else if (child.nodeType === Node.ELEMENT_NODE && !child.classList.contains('visually-hidden')) {
        walk(child);
      }
    }
  };
  walk(el);
}

function countUp(el) {
  const m = el.textContent.trim().match(/^(\d[\d.]*)(\s*[^\d]*)$/);
  if (!m) return;
  const sep = m[1].includes('.') ? '.' : '';
  const target = parseInt(m[1].replace(/\./g, ''), 10);
  const from = target >= 1900 && target <= 2100 ? target - 60 : 0;
  const fmt = (n) => (sep ? n.toLocaleString('de-DE') : String(n)) + m[2];
  const t0 = performance.now();
  const dur = 1400;
  const tick = (t) => {
    const k = Math.min(1, (t - t0) / dur);
    const e = 1 - Math.pow(1 - k, 3);
    el.textContent = fmt(Math.round(from + (target - from) * e));
    if (k < 1) requestAnimationFrame(tick);
  };
  el.textContent = fmt(from);
  requestAnimationFrame(tick);
}

function initScrollFx() {
  if (reduceMotion.matches || !('IntersectionObserver' in window)) return;

  // einmalige Effekte beim Hineinscrollen
  const once = new IntersectionObserver(
    (entries) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        e.target.classList.add('is-in');
        if (e.target.hasAttribute('data-count')) countUp(e.target);
        once.unobserve(e.target);
      }
    },
    { threshold: 0.18, rootMargin: '0px 0px -8% 0px' },
  );
  document
    .querySelectorAll('.sol__h, .revhead h2, .sec-h, .qa__h, .pz__h, .faq__h, .ig__h, .ki__h .l1, .ki__lead h3, .cm__h .small, .pr__h1')
    .forEach((el) => {
      if (el.querySelector('.rot')) return;
      // Überschriften im ersten Bildschirm sofort zeigen (schneller sichtbarer Inhalt beim Laden)
      if (el.getBoundingClientRect().top < window.innerHeight && window.scrollY < 10) return;
      el.setAttribute('data-split', '');
      splitWords(el);
      once.observe(el);
    });
  document.querySelectorAll('.sol__row, .cm__cards, .cm__videos, .tiles, .ki__tiles, .qa__cards').forEach((row) => {
    row.setAttribute('data-row-in', '');
    [...row.children].forEach((c, i) => c.style.setProperty('--i', Math.min(i, 6)));
    once.observe(row);
  });
  document.querySelectorAll('.nf__cards, .pz__steps, .faq__list, .nf__stack').forEach((group) => {
    [...group.children].forEach((c, i) => {
      c.setAttribute('data-pop', '');
      c.style.setProperty('--i', Math.min(i, 8));
      once.observe(c);
    });
  });
  document.querySelectorAll('.cm__h .big, .proof__r b, .social__i b').forEach((el) => {
    if (!/^\d/.test(el.textContent.trim())) return;
    el.setAttribute('data-count', '');
    once.observe(el);
  });

  // laufende Effekte, nur solange sichtbar
  const fx = [];
  const add = (sel, kind, f = 0) =>
    document.querySelectorAll(sel).forEach((el) => {
      fx.push({ el, kind, f, on: false });
    });
  add('.sol__media img', 'hero');
  add('.sol__text', 'heroText');
  add('.cm__hero > picture img', 'zoom');
  add('.pr__media > picture img', 'drift', 0.06);
  add('.tile--photo > picture img, .big--photo > picture img, .cm__vtile img', 'drift', 0.08);
  add('.ki__art > *', 'float', 0.1);
  add('.sol__art img, .nf__circle picture img, .qa__img--ill img', 'driveIn');
  const steps = document.querySelector('[data-steps]');

  const seen = new IntersectionObserver((entries) => {
    for (const e of entries) {
      const item = fx.find((x) => x.el === e.target);
      if (item) item.on = e.isIntersecting;
    }
  });
  fx.forEach((x) => seen.observe(x.el));

  let raf = 0;
  const frame = () => {
    raf = 0;
    const vh = window.innerHeight;
    const sy = window.scrollY;
    for (const x of fx) {
      if (!x.on && x.kind !== 'hero' && x.kind !== 'heroText') continue;
      const r = x.el.getBoundingClientRect();
      const center = r.top + r.height / 2 - vh / 2;
      const p = Math.min(1, Math.max(0, (vh - r.top) / (vh + r.height)));
      let t = '';
      if (x.kind === 'hero') {
        if (sy > vh * 1.2) continue;
        t = `translate3d(0, ${(sy * 0.32).toFixed(1)}px, 0) scale(${(1 + sy * 0.00012).toFixed(4)})`;
      } else if (x.kind === 'heroText') {
        if (sy > vh * 1.2) continue;
        x.el.style.opacity = Math.max(0, 1 - sy / (vh * 0.75)).toFixed(3);
        t = `translate3d(0, ${(sy * 0.18).toFixed(1)}px, 0)`;
      } else if (x.kind === 'zoom') {
        t = `scale(${(1.2 - 0.2 * Math.min(1, p * 1.6)).toFixed(4)})`;
      } else if (x.kind === 'drift') {
        t = `translate3d(0, ${(-center * x.f).toFixed(1)}px, 0) scale(1.14)`;
      } else if (x.kind === 'float') {
        t = `translate3d(0, ${(-center * x.f).toFixed(1)}px, 0) rotate(${(center * -0.006).toFixed(2)}deg)`;
      } else if (x.kind === 'driveIn') {
        const k = Math.min(1, p * 2.2);
        t = `translate3d(${((1 - k) * -26).toFixed(1)}%, 0, 0)`;
      }
      x.el.style.transform = t;
    }
    if (steps) {
      const r = steps.getBoundingClientRect();
      if (r.top < vh && r.bottom > 0) {
        const k = Math.min(0.999, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
        const idx = Math.floor(k * steps.children.length);
        [...steps.children].forEach((s, i) => s.classList.toggle('on', i === idx));
      }
    }
  };
  const queue = () => {
    if (!raf) raf = requestAnimationFrame(frame);
  };
  window.addEventListener('scroll', queue, { passive: true });
  window.addEventListener('resize', queue);
  // erst ab dem ersten Scrollen rechnen, damit das Hero-Bild beim Laden sofort gemalt wird
  if (window.scrollY > 0) frame();
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
initDrive();
initScrollFx();
