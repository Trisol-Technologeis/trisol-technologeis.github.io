(() => {
  const nav = document.getElementById("nav");
  const burger = nav.querySelector(".burger");
  burger.addEventListener("click", () => burger.setAttribute("aria-expanded", nav.classList.toggle("open")));
  document.getElementById("year").textContent = new Date().getFullYear();

  // highlight the section being read in the contents sidebar
  const links = [...document.querySelectorAll(".toc a")];
  const byId = new Map(links.map(a => [a.hash.slice(1), a]));
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    links.forEach(a => a.classList.remove("active"));
    byId.get(e.target.id)?.classList.add("active");
  }), { rootMargin: "-20% 0px -70% 0px" });
  document.querySelectorAll(".prose section").forEach(s => io.observe(s));
})();
