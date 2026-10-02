// Fahrschule Strauch: Navigation, Reveals, Fahrt durch den Ablauf, Karussell, Parallaxe.
// Ohne Abhängigkeiten. Alles respektiert prefers-reduced-motion.

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const desktop = window.matchMedia('(min-width: 1024px)');
const clamp = (v, min = 0, max = 1) => Math.min(max, Math.max(min, v));

/* --- Header: wird nach dem ersten Scrollen zur schwebenden Pille --------- */
function initHeader() {
  const header = document.querySelector('[data-header]');
  if (!header) return;
  const sentinel = document.createElement('div');
  sentinel.setAttribute('aria-hidden', 'true');
  sentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:24px;pointer-events:none';
  document.body.prepend(sentinel);
  new IntersectionObserver(([entry]) => {
    header.classList.toggle('is-scrolled', !entry.isIntersecting);
  }).observe(sentinel);
}

/* --- Mobiles Menü --------------------------------------------------------- */
function initMenu() {
  const menu = document.querySelector('[data-menu]');
  const openBtn = document.querySelector('[data-menu-open]');
  if (!menu || !openBtn) return;
  const closeBtn = menu.querySelector('[data-menu-close]');
  let lastFocus = null;

  const focusables = () => [...menu.querySelectorAll('a[href], button:not([disabled])')];

  const open = () => {
    lastFocus = document.activeElement;
    menu.hidden = false;
    openBtn.setAttribute('aria-expanded', 'true');
    document.documentElement.style.overflow = 'hidden';
    requestAnimationFrame(() => {
      menu.classList.add('is-open');
      // erst sichtbar, dann fokussierbar
      requestAnimationFrame(() => closeBtn.focus({ preventScroll: true }));
    });
  };
  const close = () => {
    menu.classList.remove('is-open');
    openBtn.setAttribute('aria-expanded', 'false');
    document.documentElement.style.overflow = '';
    const done = () => {
      if (!menu.classList.contains('is-open')) menu.hidden = true;
    };
    reduceMotion.matches ? done() : setTimeout(done, 340);
    (lastFocus || openBtn).focus({ preventScroll: true });
  };

  openBtn.addEventListener('click', open);
  closeBtn.addEventListener('click', close);
  menu.addEventListener('click', (e) => {
    if (e.target.closest('a')) close();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('is-open')) close();
  });
  menu.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
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
    }
  });
  desktop.addEventListener('change', (e) => {
    if (e.matches && menu.classList.contains('is-open')) close();
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

/* --- Straßen-Hilfen ------------------------------------------------------- */
function placeOnPath(path, length, at) {
  const p = path.getPointAtLength(clamp(at, 0, length));
  const q = path.getPointAtLength(clamp(at + 1, 0, length));
  const angle = (Math.atan2(q.y - p.y, q.x - p.x) * 180) / Math.PI;
  return { x: p.x, y: p.y, angle };
}

/* --- Hero: Auto steht auf der Straße ------------------------------------- */
function initHeroCar() {
  const svg = document.querySelector('[data-hero-road]');
  if (!svg) return;
  const path = svg.querySelector('.road-asphalt');
  const car = svg.querySelector('.hero__car');
  const length = path.getTotalLength();
  const { x, y, angle } = placeOnPath(path, length, length * 0.255);
  car.setAttribute('transform', `translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${angle.toFixed(1)})`);
}

/* --- Ablauf: Auto fährt mit dem Scrollfortschritt durch sechs Stationen -- */
function initJourney() {
  const section = document.querySelector('[data-journey]');
  if (!section) return null;
  const steps = [...section.querySelectorAll('[data-step]')];
  const labels = steps.map((s) => s.querySelector('.step__title').textContent.trim());
  const svgNS = 'http://www.w3.org/2000/svg';

  const roads = [...section.querySelectorAll('[data-road]')].map((svg) => {
    const vertical = svg.dataset.road === 'v';
    const path = svg.querySelector('.road-asphalt');
    const trail = svg.querySelector('[data-trail]');
    const car = svg.querySelector('[data-car]');
    const length = path.getTotalLength();
    const [a, b] = vertical ? [0.07, 0.93] : [0.08, 0.92];
    const fractions = steps.map((_, i) => a + ((b - a) * i) / (steps.length - 1));
    trail.style.strokeDasharray = `${length} ${length}`;
    trail.style.strokeDashoffset = `${length}`;

    const group = svg.querySelector('[data-stations]');
    const stations = fractions.map((f, i) => {
      const { x, y } = placeOnPath(path, length, f * length);
      const g = document.createElementNS(svgNS, 'g');
      g.setAttribute('class', 'station');
      const c = document.createElementNS(svgNS, 'circle');
      c.setAttribute('cx', x);
      c.setAttribute('cy', y);
      c.setAttribute('r', vertical ? 15 : 36);
      g.append(c);
      const t = document.createElementNS(svgNS, 'text');
      t.setAttribute('x', x);
      t.setAttribute('y', y + (vertical ? 5.5 : 11.5));
      t.setAttribute('text-anchor', 'middle');
      if (!vertical) t.setAttribute('font-size', '33');
      t.textContent = String(i + 1);
      g.append(t);
      const title = document.createElementNS(svgNS, 'title');
      title.textContent = labels[i];
      g.append(title);
      group.append(g);
      return g;
    });
    const scale = vertical ? 1 : 1.5;
    return { svg, path, trail, car, length, fractions, stations, vertical, scale };
  });

  let current = -1;
  const update = () => {
    const anchor = window.innerHeight * 0.55;
    const centers = steps.map((s) => {
      const r = s.getBoundingClientRect();
      return r.top + r.height / 2;
    });
    // Abschnitt zwischen zwei Stationen bestimmen und interpolieren
    let progress; // 0 … steps.length-1, kontinuierlich
    if (reduceMotion.matches) progress = steps.length - 1;
    else if (anchor <= centers[0]) progress = clamp((anchor - (centers[0] - window.innerHeight * 0.5)) / (window.innerHeight * 0.5), 0, 1) - 1;
    else if (anchor >= centers[centers.length - 1]) progress = steps.length - 1;
    else {
      let i = 0;
      while (i < centers.length - 1 && anchor > centers[i + 1]) i++;
      progress = i + (anchor - centers[i]) / (centers[i + 1] - centers[i]);
    }

    const active = Math.round(clamp(progress, 0, steps.length - 1));
    if (active !== current) {
      current = active;
      steps.forEach((s, i) => {
        s.classList.toggle('is-active', i === active && progress > -0.5);
        s.classList.toggle('is-done', i < active);
      });
    }

    for (const road of roads) {
      if (!road.svg.getClientRects().length) continue;
      const { fractions, length } = road;
      let f;
      if (progress < 0) f = fractions[0] * (1 + progress * 0.6);
      else {
        const i = Math.min(Math.floor(progress), fractions.length - 2);
        const t = progress - i;
        f = fractions[i] + (fractions[i + 1] - fractions[i]) * clamp(t);
      }
      const at = f * length;
      const { x, y, angle } = placeOnPath(road.path, length, at);
      road.car.setAttribute('transform', `translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${angle.toFixed(1)}) scale(${road.scale})`);
      road.trail.style.strokeDashoffset = `${(length - at).toFixed(1)}`;
      road.stations.forEach((g, i) => g.classList.toggle('is-passed', progress >= i - 0.02));
    }
  };

  update();
  return { section, update };
}

/* --- Parallaxe Fuhrpark-Panorama (nur Desktop) --------------------------- */
function initParallax() {
  const img = document.querySelector('[data-parallax]');
  if (!img) return null;
  const frame = img.closest('.frame');
  const update = () => {
    if (reduceMotion.matches || !desktop.matches) {
      img.style.transform = '';
      return;
    }
    const r = frame.getBoundingClientRect();
    const t = clamp((window.innerHeight - r.top) / (window.innerHeight + r.height));
    img.style.transform = `translate3d(0, ${((t - 0.5) * -10).toFixed(2)}%, 0)`;
  };
  update();
  return { section: frame, update };
}

/* --- Scroll-Schleife: läuft nur, solange ein Abschnitt sichtbar ist ------ */
function initScrollLoop(handlers) {
  const active = new Set();
  let ticking = false;
  const run = () => {
    ticking = false;
    active.forEach((h) => h.update());
  };
  const request = () => {
    if (!ticking && active.size) {
      ticking = true;
      requestAnimationFrame(run);
    }
  };
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      const h = handlers.find((x) => x.section === entry.target);
      if (!h) continue;
      entry.isIntersecting ? active.add(h) : active.delete(h);
    }
    request();
  });
  handlers.forEach((h) => io.observe(h.section));
  window.addEventListener('scroll', request, { passive: true });
  window.addEventListener('resize', () => handlers.forEach((h) => h.update()), { passive: true });
  reduceMotion.addEventListener('change', () => handlers.forEach((h) => h.update()));
}

/* --- Karussell (Team, mobil) --------------------------------------------- */
function initScrollers() {
  document.querySelectorAll('[data-scroller]').forEach((root) => {
    const track = root.querySelector('[data-scroller-track]');
    const bar = root.querySelector('[data-scroller-bar]');
    const prev = root.querySelector('[data-scroller-prev]');
    const next = root.querySelector('[data-scroller-next]');
    const step = () => {
      const item = track.children[0];
      return item ? item.getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 0) : 300;
    };
    const update = () => {
      const max = track.scrollWidth - track.clientWidth;
      const ratio = track.scrollWidth ? (track.scrollLeft + track.clientWidth) / track.scrollWidth : 1;
      bar?.style.setProperty('--p', clamp(ratio).toFixed(3));
      if (prev) prev.disabled = track.scrollLeft <= 2;
      if (next) next.disabled = track.scrollLeft >= max - 2;
    };
    const behavior = () => (reduceMotion.matches ? 'auto' : 'smooth');
    prev?.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: behavior() }));
    next?.addEventListener('click', () => track.scrollBy({ left: step(), behavior: behavior() }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update, { passive: true });
    update();
  });
}

/* --- Team-Bühne: Fahrlehrer per Avatar wählen ------------------------- */
function initCrew() {
  const root = document.querySelector('[data-crew]');
  if (!root) return;
  const slides = [...root.querySelectorAll('[data-crew-slide]')];
  const picks = [...root.querySelectorAll('[data-crew-pick]')];
  const quote = root.querySelector('[data-crew-quote]');
  const name = root.querySelector('[data-crew-name]');
  const role = root.querySelector('[data-crew-role]');
  const replay = (el) => {
    el.classList.remove('is-changing');
    void el.offsetWidth; // Animation neu starten
    el.classList.add('is-changing');
  };
  const show = (i) => {
    const pick = picks[i];
    slides.forEach((s, k) => s.classList.toggle('is-active', k === i));
    picks.forEach((p, k) => p.setAttribute('aria-pressed', String(k === i)));
    quote.innerHTML = `<p>„${pick.dataset.quote}“</p>`;
    name.textContent = pick.dataset.name;
    role.textContent = pick.dataset.role;
    if (!reduceMotion.matches) [quote, name].forEach(replay);
  };
  picks.forEach((pick, i) => {
    pick.addEventListener('click', () => show(i));
    pick.addEventListener('keydown', (e) => {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      e.preventDefault();
      const next = (i + (e.key === 'ArrowRight' ? 1 : -1) + picks.length) % picks.length;
      picks[next].focus();
      show(next);
    });
  });
  // Bilder der anderen Fahrlehrer vorladen, sobald die Bühne in Sicht kommt
  new IntersectionObserver(([entry], io) => {
    if (!entry.isIntersecting) return;
    slides.forEach((s) => s.querySelector('img').setAttribute('loading', 'eager'));
    io.disconnect();
  }, { rootMargin: '400px' }).observe(root);
}

/* --- Sprungnavigation: aktiven Abschnitt markieren --------------------- */
function initSubnav() {
  const nav = document.querySelector('[data-subnav]');
  if (!nav) return;
  const links = [...nav.querySelectorAll('a[href^="#"]')];
  const map = new Map(links.map((a) => [document.querySelector(a.getAttribute('href')), a]));
  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        links.forEach((a) => a.classList.remove('is-current'));
        const link = map.get(entry.target);
        if (!link) continue;
        link.classList.add('is-current');
        const list = link.closest('ul');
        const x = link.offsetLeft - list.clientWidth / 2 + link.offsetWidth / 2;
        list.scrollTo({ left: x, behavior: reduceMotion.matches ? 'auto' : 'smooth' });
      }
    },
    { rootMargin: '-45% 0px -50% 0px' },
  );
  map.forEach((_, section) => section && io.observe(section));
}

/* --- Start ---------------------------------------------------------------- */
initHeader();
initMenu();
initReveal();
initHeroCar();
initScrollers();
initSubnav();
initCrew();
const loops = [initJourney(), initParallax()].filter(Boolean);
if (loops.length) initScrollLoop(loops);
