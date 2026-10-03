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

/* --- Ablauf: das Fahrschulauto fährt beim Scrollen durch sechs Stationen ---
   Pfad und Etappen werden bei Größenänderungen einmal vermessen; beim Scrollen wird nur
   noch nachgeschlagen und geschrieben (kein Messen pro Bild). */
function initJourney() {
  const section = document.querySelector('[data-journey]');
  if (!section) return;
  const steps = [...section.querySelectorAll('[data-step]')];
  const labels = steps.map((st) => st.querySelector('.jr__title').textContent.trim());
  const svgNS = 'http://www.w3.org/2000/svg';
  const wide = window.matchMedia('(min-width: 1000px)');
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));

  const roads = [...section.querySelectorAll('[data-road]')].map((svg) => {
    const vertical = svg.dataset.road === 'v';
    const path = svg.querySelector('.road-asphalt');
    const trail = svg.querySelector('[data-trail]');
    const car = svg.querySelector('[data-car]');
    const length = path.getTotalLength();
    // Punkte einmal vorab berechnen
    const N = 400;
    const pts = Array.from({ length: N + 1 }, (_, i) => path.getPointAtLength((length * i) / N));
    const at = (f) => {
      const x = clamp(f) * N;
      const i = Math.min(N - 1, Math.floor(x));
      const t = x - i;
      const p = pts[i];
      const q = pts[i + 1];
      return { x: p.x + (q.x - p.x) * t, y: p.y + (q.y - p.y) * t, angle: (Math.atan2(q.y - p.y, q.x - p.x) * 180) / Math.PI };
    };
    const [a, b] = vertical ? [0.07, 0.93] : [0.08, 0.92];
    const fractions = steps.map((_, i) => a + ((b - a) * i) / (steps.length - 1));
    trail.style.strokeDasharray = `${length} ${length}`;
    trail.style.strokeDashoffset = `${length}`;
    const group = svg.querySelector('[data-stations]');
    const stations = fractions.map((f, i) => {
      const { x, y } = at(f);
      const g = document.createElementNS(svgNS, 'g');
      g.setAttribute('class', 'station');
      const c = document.createElementNS(svgNS, 'circle');
      c.setAttribute('cx', x);
      c.setAttribute('cy', y);
      c.setAttribute('r', vertical ? 11 : 26);
      const t = document.createElementNS(svgNS, 'text');
      t.setAttribute('x', x);
      t.setAttribute('y', y + (vertical ? 4 : 8.5));
      t.setAttribute('text-anchor', 'middle');
      t.textContent = String(i + 1);
      const title = document.createElementNS(svgNS, 'title');
      title.textContent = labels[i];
      g.append(c, t, title);
      group.append(g);
      return g;
    });
    return { vertical, trail, car, length, fractions, stations, at, scale: vertical ? 0.78 : 1.2, passed: -1 };
  });

  let centers = [];
  let vh = window.innerHeight;
  const measure = () => {
    vh = window.innerHeight;
    centers = steps.map((st) => {
      const r = st.getBoundingClientRect();
      return r.top + window.scrollY + r.height / 2;
    });
    update();
  };

  let current = -2;
  const update = () => {
    let progress; // -1 … steps.length-1, kontinuierlich
    if (reduceMotion.matches) progress = steps.length - 1;
    else {
      const anchor = window.scrollY + vh * 0.55;
      if (anchor <= centers[0]) progress = clamp((anchor - (centers[0] - vh * 0.5)) / (vh * 0.5)) - 1;
      else if (anchor >= centers[centers.length - 1]) progress = steps.length - 1;
      else {
        let i = 0;
        while (i < centers.length - 2 && anchor > centers[i + 1]) i++;
        progress = i + (anchor - centers[i]) / (centers[i + 1] - centers[i]);
      }
    }
    const active = progress < -0.5 ? -1 : Math.round(clamp(progress, 0, steps.length - 1));
    if (active !== current) {
      current = active;
      steps.forEach((st, i) => {
        st.classList.toggle('is-active', i === active);
        st.classList.toggle('is-done', i < active);
      });
    }
    const road = roads.find((r) => r.vertical === wide.matches);
    if (!road) return;
    let f;
    if (progress < 0) f = road.fractions[0] * (1 + progress * 0.6);
    else {
      const i = Math.min(Math.floor(progress), road.fractions.length - 2);
      f = road.fractions[i] + (road.fractions[i + 1] - road.fractions[i]) * clamp(progress - i);
    }
    const { x, y, angle } = road.at(f);
    road.car.setAttribute('transform', `translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${angle.toFixed(1)}) scale(${road.scale})`);
    road.trail.style.strokeDashoffset = `${(road.length * (1 - clamp(f))).toFixed(1)}`;
    const passed = Math.floor(progress + 0.02);
    if (passed !== road.passed) {
      road.passed = passed;
      road.stations.forEach((g, i) => g.classList.toggle('is-passed', i <= passed));
    }
  };

  let visible = false;
  let raf = 0;
  const queue = () => {
    if (visible && !raf)
      raf = requestAnimationFrame(() => {
        raf = 0;
        update();
      });
  };
  new IntersectionObserver(([e]) => {
    visible = e.isIntersecting;
    queue();
  }, { rootMargin: '20% 0px' }).observe(section);
  window.addEventListener('scroll', queue, { passive: true });
  wide.addEventListener('change', measure);
  let pending = 0;
  new ResizeObserver(() => {
    cancelAnimationFrame(pending);
    pending = requestAnimationFrame(measure);
  }).observe(document.body);
  measure();
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
  const from = target >= 1900 && target <= 2100 ? target - 20 : Math.round(target * 0.6);
  const fmt = (n) => (sep ? n.toLocaleString('de-DE') : String(n)) + m[2];
  const t0 = performance.now();
  const dur = 900;
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
    .querySelectorAll('.revhead h2, .sec-h, .qa__h, .pz__h, .faq__h, .ig__h, .ki__h .l1, .ki__lead h3, .cm__h .small')
    .forEach((el) => {
      if (el.querySelector('.rot')) return;
      // Überschriften im ersten Bildschirm sofort zeigen (schneller sichtbarer Inhalt beim Laden)
      if (el.getBoundingClientRect().top < window.innerHeight && window.scrollY < 10) return;
      el.setAttribute('data-split', '');
      splitWords(el);
      once.observe(el);
    });
  document.querySelectorAll('.sol__row, .cm__videos, .tiles, .ki__tiles, .qa__cards').forEach((row) => {
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
  document.querySelectorAll('.cm__h .big, .proof__r b').forEach((el) => {
    if (!/^\d/.test(el.textContent.trim())) return;
    el.setAttribute('data-count', '');
    once.observe(el);
  });

  // laufende Effekte rechnet der Browser selbst über CSS-View-Timelines (hoki.css, data-fx)
  const mark = (sel, kind) => document.querySelectorAll(sel).forEach((el) => el.setAttribute('data-fx', kind));
  mark('.cm__hero > picture img', 'zoom');
  mark('.tile--photo > picture img, .big--photo > picture img, .cm__vtile img', 'drift');
  mark('.ki__art > *', 'float');
  mark('.sol__art img, .nf__circle picture img, .qa__img--ill img', 'drive-in');

  // drei Schritte leuchten nacheinander auf (ein Messwert pro Bild, nur solange sichtbar)
  const steps = document.querySelector('[data-steps]');
  if (!steps) return;
  let visible = false;
  let raf = 0;
  const frame = () => {
    raf = 0;
    if (!visible) return;
    const r = steps.getBoundingClientRect();
    const vh = window.innerHeight;
    const k = Math.min(0.999, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
    const idx = Math.floor(k * steps.children.length);
    [...steps.children].forEach((st, i) => st.classList.toggle('on', i === idx));
  };
  new IntersectionObserver(([e]) => {
    visible = e.isIntersecting;
    if (visible && !raf) raf = requestAnimationFrame(frame);
  }).observe(steps);
  window.addEventListener('scroll', () => {
    if (visible && !raf) raf = requestAnimationFrame(frame);
  }, { passive: true });
}

/* --- Handy: feste Leiste mit Anrufen/Anmelden erscheint nach dem Hero --- */
function initMobileBar() {
  const bar = document.querySelector('[data-mbar]');
  if (!bar) return;
  const hero = document.querySelector('.sol__hero, .pr__hero, .legal--head, .notfound');
  const sentinel = document.createElement('div');
  sentinel.setAttribute('aria-hidden', 'true');
  sentinel.style.cssText = 'position:absolute;left:0;width:1px;height:1px;pointer-events:none';
  sentinel.style.top = `${hero ? Math.round(hero.getBoundingClientRect().bottom + window.scrollY) : 600}px`;
  document.body.append(sentinel);
  new IntersectionObserver(([e]) => bar.classList.toggle('is-on', !e.isIntersecting && e.boundingClientRect.top < 0)).observe(sentinel);
}

initHeader();
initMobileBar();
initMenu();
initReveal();
initRows();
initFlow();
initRotate();
initFaq();
initSteps();
initLangSwitch();
initJourney();
initScrollFx();
