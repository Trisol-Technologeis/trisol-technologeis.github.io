(() => {
  const { SITE, APPS } = window;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = matchMedia("(hover: hover) and (pointer: fine)").matches;
  const img = (id, f) => `assets/img/apps/${id}/${f}.webp`;
  const playUrl = id => `https://play.google.com/store/apps/details?id=${id}`;
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  /* ---------- global links ---------- */
  $$("[data-play-dev]").forEach(a => (a.href = SITE.playDevUrl));
  $$("[data-email]").forEach(a => (a.href = `mailto:${SITE.email}`));
  $("#year").textContent = new Date().getFullYear();

  /* ---------- hero icons + phone stack ---------- */
  $("#heroIcons").innerHTML = APPS.slice(0, 5).map(a => `<img src="${img(a.id, "icon")}" alt="" width="38" height="38">`).join("");

  const heroShots = APPS.filter(a => a.featured).concat(APPS.filter(a => !a.featured).slice(0, 1));
  const stack = $("#phoneStack");
  stack.innerHTML = heroShots.map((a, i) =>
    `<div class="phone" data-pos="${i}"><img src="${img(a.id, "s1")}" alt="" ${i ? 'loading="lazy"' : 'fetchpriority="high"'} width="422" height="900"></div>`).join("");
  const phones = $$(".phone", stack);
  if (!reduce) {
    setInterval(() => {
      if (document.hidden) return;
      phones.forEach(p => (p.dataset.pos = (+p.dataset.pos + phones.length - 1) % phones.length));
    }, 3200);
  }

  /* ---------- marquee ---------- */
  const mq = APPS.map(a => `<span class="mq-item"><img src="${img(a.id, "icon")}" alt="" width="40" height="40" loading="lazy">${esc(a.title)}</span>`).join("");
  $("#marquee").innerHTML = mq + mq;

  /* ---------- stats with rolling digits ---------- */
  const stats = $("#stats");
  stats.innerHTML = SITE.stats.map(s => {
    const str = s.value.toFixed(s.decimals || 0);
    const digits = [...str].map(ch => /\d/.test(ch)
      ? `<span class="digit"><span data-d="${ch}">${Array.from({ length: 10 }, (_, n) => `<span>${n}</span>`).join("")}</span></span>`
      : `<span>${ch}</span>`).join("");
    return `<div class="stat reveal"><div class="stat-num" aria-label="${str}${s.suffix}"><span aria-hidden="true">${digits}</span><span class="suffix" aria-hidden="true">${s.suffix}</span></div><h3>${s.label}</h3><p>${s.note}</p></div>`;
  }).join("");
  const rollDigits = el => $$("[data-d]", el).forEach((d, i) => {
    // shrink each slot to its final glyph so "1" doesn't leave a gap
    const probe = document.createElement("span");
    probe.textContent = d.dataset.d;
    d.parentElement.after(probe);
    d.parentElement.style.width = `${probe.getBoundingClientRect().width}px`;
    probe.remove();
    d.style.transitionDelay = `${i * 90}ms`;
    d.style.transform = `translateY(-${d.dataset.d}em)`;
  });

  /* ---------- filters ---------- */
  const cats = ["All", ...new Set(APPS.map(a => a.category))];
  $("#filters").innerHTML = cats.map((c, i) => {
    const n = c === "All" ? APPS.length : APPS.filter(a => a.category === c).length;
    return `<button role="tab" aria-selected="${i === 0}" data-cat="${c}">${c}<small>${n}</small></button>`;
  }).join("");

  /* ---------- app cards ---------- */
  const grid = $("#appGrid");
  grid.innerHTML = APPS.map((a, i) => {
    const big = i < 2;
    const meta = [
      `<span class="card-tag">${a.category}</span>`,
      a.rating ? `<span><b>${a.rating.toFixed(1)}★</b> ${a.reviews} reviews</span>` : "",
      `<span><b>${a.downloads}</b> downloads</span>`
    ].join("");
    const shots = [1, 2, 3].map(n => `<img src="${img(a.id, "s" + n)}" alt="${esc(a.title)} screenshot ${n}" loading="lazy" decoding="async" width="${a.shotW}" height="900">`).join("");
    return `<article class="card${big ? " big" : ""}" style="--hue:${a.hue}" data-cat="${a.category}" data-id="${a.id}" tabindex="0" role="button" aria-label="View ${esc(a.title)} details">
      <div class="card-top"><img class="card-icon" src="${img(a.id, "icon")}" alt="" width="64" height="64" loading="lazy">
        <div><h3 class="card-title">${esc(a.title)}</h3><div class="card-sub">${esc(a.native)}</div></div></div>
      <p class="card-desc">${esc(a.tagline)}</p>
      <div class="card-meta">${meta}</div>
      <div class="card-shots">${shots}</div>
      <span class="card-cta">View app <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M7 17 17 7M8 7h9v9"/></svg></span>
    </article>`;
  }).join("");

  $("#filters").addEventListener("click", e => {
    const b = e.target.closest("button"); if (!b) return;
    $$("#filters button").forEach(x => x.setAttribute("aria-selected", x === b));
    const c = b.dataset.cat;
    $$(".card", grid).forEach((card, i) => {
      const show = c === "All" || card.dataset.cat === c;
      card.classList.toggle("is-hidden", !show);
      card.classList.toggle("big", show && c === "All" && i < 2);
      if (show && !reduce) card.animate([{ opacity: 0, transform: "translateY(30px)" }, { opacity: 1, transform: "none" }], { duration: 600, easing: "cubic-bezier(.2,.8,.2,1)", delay: 40 * i });
    });
  });

  // spotlight follows pointer
  grid.addEventListener("pointermove", e => {
    const c = e.target.closest(".card"); if (!c) return;
    const r = c.getBoundingClientRect();
    c.style.setProperty("--mx", `${e.clientX - r.left}px`);
    c.style.setProperty("--my", `${e.clientY - r.top}px`);
  });

  /* ---------- detail sheet ---------- */
  const sheet = $("#sheet");
  const openApp = (id, push = true) => {
    const a = APPS.find(x => x.id === id); if (!a) return;
    sheet.style.setProperty("--hue", a.hue);
    const stat = (b, s) => `<div><b>${b}</b><small>${s}</small></div>`;
    $("#sheetBody").innerHTML = `
      <div class="sh-head"><img src="${img(a.id, "icon")}" alt="" width="96" height="96">
        <div><h2 id="sheetTitle">${esc(a.title)}</h2><p>${esc(a.native)} · ${a.category}</p></div>
        <button class="sh-close" aria-label="Close" data-close>×</button></div>
      <div class="sh-stats">
        ${a.rating ? stat(a.rating.toFixed(1) + "★", a.reviews + " reviews") : stat("New", "Fresh release")}
        ${stat(a.downloads, "Downloads")}${stat(a.category, "Category")}${stat("Free", "In-app extras")}
      </div>
      <div class="sh-shots">${Array.from({ length: a.shots }, (_, n) => `<img src="${img(a.id, "s" + (n + 1))}" alt="${esc(a.title)} screenshot ${n + 1}" loading="lazy" decoding="async" width="${a.shotW}" height="900">`).join("")}</div>
      <div class="sh-grid">
        <div><p>${esc(a.tagline)}</p>
          <a class="play-badge" href="${playUrl(a.id)}" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true"><path fill="#00d7fe" d="M3.6 1.8 13.8 12 3.6 22.2a1.6 1.6 0 0 1-.6-1.3V3.1c0-.5.2-1 .6-1.3Z"/><path fill="#ffce00" d="m18.8 9.2 3.2 1.8c.9.5.9 1.6 0 2.1l-3.2 1.8-2.8-2.9 2.8-2.8Z"/><path fill="#ff3a44" d="m14.9 13.1 2.6 2.6-11.9 6.8 9.3-9.4Z"/><path fill="#00f076" d="m5.6 1.5 11.9 6.8-2.6 2.6-9.3-9.4Z"/></svg>
            <span><small>Get it on</small><b>Google Play</b></span></a></div>
        <ul class="sh-feats">${a.features.map(f => `<li>${esc(f)}</li>`).join("")}</ul>
      </div>
      <nav class="sh-legal" aria-label="Legal"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms & Conditions</a><a href="cloud-data.html">Cloud & Google data</a><a href="cloud-data.html#delete">Delete my data</a></nav>`;
    sheet.showModal();
    $(".sheet-body", sheet).scrollTop = 0;
    document.body.style.overflow = "hidden";
    if (push) history.pushState({ app: id }, "", `#app/${id}`);
  };
  const closeSheet = () => sheet.open && sheet.close();
  sheet.addEventListener("close", () => {
    document.body.style.overflow = "";
    if (location.hash.startsWith("#app/")) history.pushState({}, "", "#apps");
  });
  sheet.addEventListener("click", e => { if (e.target === sheet || e.target.closest("[data-close]")) closeSheet(); });
  grid.addEventListener("click", e => { const c = e.target.closest(".card"); if (c) openApp(c.dataset.id); });
  grid.addEventListener("keydown", e => { const c = e.target.closest(".card"); if (c && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); openApp(c.dataset.id); } });
  const fromHash = () => { const m = location.hash.match(/^#app\/(.+)$/); m ? openApp(m[1], false) : closeSheet(); };
  addEventListener("popstate", fromHash);
  fromHash();

  /* ---------- showcase (pinned horizontal scroll) ---------- */
  const track = $("#showcaseTrack");
  const showcaseItems = [];
  for (let n = 1; n <= 3; n++) APPS.forEach(a => { if (n <= a.shots) showcaseItems.push([a, n + 1 <= a.shots ? n + 1 : n]); });
  track.innerHTML = showcaseItems.slice(0, 18).map(([a, n]) =>
    `<figure class="sc-item"><img src="${img(a.id, "s" + n)}" alt="${esc(a.title)} screen" loading="lazy" decoding="async" width="${a.shotW}" height="900">
      <figcaption><img src="${img(a.id, "icon")}" alt="" width="22" height="22" loading="lazy">${esc(a.title)}</figcaption></figure>`).join("");
  const showcase = $("#showcase"), bar = $("#showcaseBar");
  const desktopPin = matchMedia("(min-width: 761px)");
  const updateShowcase = () => {
    if (!desktopPin.matches) return;
    const r = showcase.getBoundingClientRect();
    const total = showcase.offsetHeight - innerHeight;
    const p = Math.min(1, Math.max(0, -r.top / total));
    const dist = track.scrollWidth - innerWidth + 48;
    track.style.transform = `translate3d(${-p * dist}px,0,0)`;
    bar.style.transform = `scaleX(${p})`;
  };

  /* ---------- statement word reveal ---------- */
  const st = $(".reveal-words");
  st.innerHTML = st.textContent.split(" ").map(w => `<span class="w">${w}</span>`).join(" ");
  const words = $$(".w", st);
  const updateWords = () => {
    const r = st.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, (innerHeight * .85 - r.top) / (r.height + innerHeight * .35)));
    const on = Math.round(p * words.length);
    words.forEach((w, i) => w.classList.toggle("on", i < on));
  };

  /* ---------- nav ---------- */
  const nav = $("#nav");
  let lastY = 0;
  const updateNav = () => {
    const y = scrollY;
    nav.classList.toggle("scrolled", y > 20);
    nav.classList.toggle("hide", y > 600 && y > lastY && !nav.classList.contains("open"));
    lastY = y;
  };
  $(".burger").addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    $(".burger").setAttribute("aria-expanded", open);
  });
  $$(".nav-links a").forEach(a => a.addEventListener("click", () => { nav.classList.remove("open"); $(".burger").setAttribute("aria-expanded", false); }));
  const sections = ["apps", "studio", "services", "contact"].map(id => document.getElementById(id));
  const updateActive = () => {
    let cur = null;
    sections.forEach(s => { if (s.getBoundingClientRect().top < innerHeight * .4) cur = s.id; });
    $$(".nav-links a").forEach(a => a.classList.toggle("active", a.getAttribute("href") === `#${cur}`));
  };

  /* ---------- scroll loop ---------- */
  let ticking = false;
  const onScroll = () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => { updateNav(); updateShowcase(); updateWords(); updateActive(); ticking = false; });
  };
  addEventListener("scroll", onScroll, { passive: true });
  addEventListener("resize", onScroll);
  onScroll();

  /* ---------- reveal on view ---------- */
  const io = new IntersectionObserver(entries => entries.forEach(en => {
    if (!en.isIntersecting) return;
    const el = en.target;
    const sibs = el.parentElement ? $$(":scope > .reveal, :scope > .card", el.parentElement) : [];
    el.style.transitionDelay = `${Math.max(0, sibs.indexOf(el)) % 3 * 90}ms`;
    el.classList.add("in");
    if (el.classList.contains("stat")) rollDigits(el);
    io.unobserve(el);
  }), { threshold: .12, rootMargin: "0px 0px -6% 0px" });
  $$(".reveal, .card").forEach(el => io.observe(el));
  requestAnimationFrame(() => $(".split").classList.add("in"));
  // once revealed, clear stagger delay so hover transitions are snappy
  grid.addEventListener("transitionend", e => { if (e.target.classList.contains("card")) e.target.style.transitionDelay = ""; });

  /* ---------- pointer effects (desktop only) ---------- */
  if (fine && !reduce) {
    document.body.classList.add("has-pointer");
    const glow = $(".cursor-glow");
    let gx = innerWidth / 2, gy = innerHeight / 2, tx = gx, ty = gy;
    addEventListener("pointermove", e => { tx = e.clientX; ty = e.clientY; }, { passive: true });
    (function loop() {
      gx += (tx - gx) * .12; gy += (ty - gy) * .12;
      glow.style.transform = `translate3d(${gx}px,${gy}px,0)`;
      requestAnimationFrame(loop);
    })();

    $$(".magnetic").forEach(b => {
      b.addEventListener("pointermove", e => {
        const r = b.getBoundingClientRect();
        b.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * .25}px, ${(e.clientY - r.top - r.height / 2) * .35}px)`;
      });
      b.addEventListener("pointerleave", () => (b.style.transform = ""));
    });

    $$(".tilt").forEach(t => {
      t.addEventListener("pointermove", e => {
        const r = t.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        t.style.transform = `perspective(900px) rotateX(${-y * 6}deg) rotateY(${x * 6}deg)`;
      });
      t.addEventListener("pointerleave", () => (t.style.transform = ""));
    });

    const vis = $(".hero-visual");
    $(".hero").addEventListener("pointermove", e => {
      const x = e.clientX / innerWidth - .5, y = e.clientY / innerHeight - .5;
      stack.style.transform = `rotateY(${x * 10}deg) rotateX(${-y * 8}deg)`;
      vis.style.setProperty("--px", x);
    });
  }
})();
