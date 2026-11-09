(function () {
  var C = window.CLINIC || {};

  /* ссылки на whatsapp с готовым текстом */
  function waLink(text) {
    return "https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(text || "Здравствуйте!");
  }
  document.querySelectorAll("[data-wa]").forEach(function (a) {
    a.href = waLink(a.getAttribute("data-wa"));
  });
  document.querySelectorAll("[data-gis]").forEach(function (a) { a.href = C.gis; });
  document.querySelectorAll("[data-tg]").forEach(function (a) { a.href = "https://t.me/" + C.telegram; });
  document.querySelectorAll("[data-ig]").forEach(function (a) { a.href = "https://www.instagram.com/" + C.instagram + "/"; });

  /* команда */
  var list = document.getElementById("team-list");
  if (list && C.team) {
    C.team.forEach(function (p, i) {
      var fig = document.createElement("figure");
      fig.className = "person reveal";
      fig.style.margin = "0";
      var img = document.createElement("img");
      img.src = p.photo;
      img.alt = p.name || "Врач клиники Dinastiya Stom Clinic";
      img.loading = "lazy";
      img.width = 340;
      img.height = 400;
      fig.appendChild(img);
      var frame = document.createElement("div");
      frame.className = "person__photo";
      frame.appendChild(img);
      fig.appendChild(frame);
      if (p.name || p.role || p.about) {
        var cap = document.createElement("figcaption");
        if (p.name) { var b = document.createElement("b"); b.textContent = p.name; cap.appendChild(b); }
        if (p.role) { var s = document.createElement("span"); s.textContent = p.role; cap.appendChild(s); }
        if (p.about) { var a = document.createElement("p"); a.textContent = p.about; cap.appendChild(a); }
        fig.appendChild(cap);
      }
      list.appendChild(fig);
    });
  }

  /* отзывы */
  var rv = document.getElementById("reviews-list");
  if (rv && C.reviews && C.reviews.length) {
    C.reviews.forEach(function (r) {
      var card = document.createElement("article");
      card.className = "review";
      var stars = document.createElement("div");
      stars.className = "stars";
      stars.setAttribute("aria-label", "Оценка " + (r.rating || 5) + " из 5");
      stars.textContent = new Array((r.rating || 5) + 1).join("★");
      var q = document.createElement("p");
      q.className = "review__text";
      q.textContent = r.text;
      var who = document.createElement("div");
      who.className = "review__who";
      var n = document.createElement("b");
      n.textContent = r.name || "Пациент";
      who.appendChild(n);
      var meta = document.createElement("span");
      meta.textContent = "2ГИС" + (r.date ? " · " + r.date : "");
      who.appendChild(meta);
      card.appendChild(stars);
      card.appendChild(q);
      card.appendChild(who);
      rv.appendChild(card);
    });
    rv.hidden = false;
  }

  /* меню */
  var burger = document.getElementById("burger");
  var nav = document.getElementById("nav");
  function closeNav() { nav.classList.remove("is-open"); burger.setAttribute("aria-expanded", "false"); }
  burger.addEventListener("click", function () {
    var open = nav.classList.toggle("is-open");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
  });
  nav.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeNav); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeNav(); });

  /* тень у шапки */
  var header = document.querySelector(".header");
  function onScroll() { header.classList.toggle("is-scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* появление блоков */
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* вопросы: плавное раскрытие */
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.querySelectorAll(".faq details").forEach(function (d) {
    var summary = d.querySelector("summary");
    var body = d.querySelector("p");
    var anim = null, fade = null;
    var ease = "cubic-bezier(.4, 0, .2, 1)";

    summary.addEventListener("click", function (e) {
      e.preventDefault();
      if (reduce || !d.animate) { d.open = !d.open; return; }

      if (anim) anim.cancel();
      if (fade) fade.cancel();

      var borders = d.offsetHeight - d.clientHeight;
      var closedH = summary.offsetHeight + borders;
      var start = d.offsetHeight;
      var opening = !d.open;
      var end;

      d.style.overflow = "hidden";
      if (opening) {
        d.open = true;
        end = d.scrollHeight + borders;
        fade = body.animate(
          [{ opacity: 0, transform: "translateY(-8px)" }, { opacity: 1, transform: "none" }],
          { duration: 420, easing: ease, delay: 60, fill: "backwards" }
        );
      } else {
        end = closedH;
        fade = body.animate(
          [{ opacity: 1, transform: "none" }, { opacity: 0, transform: "translateY(-6px)" }],
          { duration: 220, easing: ease, fill: "forwards" }
        );
      }

      anim = d.animate(
        [{ height: start + "px" }, { height: end + "px" }],
        { duration: opening ? 420 : 340, easing: ease }
      );
      d.classList.toggle("is-closing", !opening);

      anim.onfinish = function () {
        d.open = opening;
        d.style.overflow = "";
        d.classList.remove("is-closing");
        if (!opening && fade) fade.cancel();
        anim = null; fade = null;
      };
      anim.oncancel = function () { d.style.overflow = ""; };
    });
  });

  /* форма -> whatsapp */
  var form = document.getElementById("form");
  var err = document.getElementById("form-error");
  function showError(msg, field) {
    err.textContent = msg; err.hidden = false;
    if (field) { field.classList.add("is-bad"); field.focus(); }
  }
  form.addEventListener("input", function (e) { e.target.classList.remove("is-bad"); err.hidden = true; });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = form.elements.name.value.trim();
    var phone = form.elements.phone.value.trim();
    var topic = form.elements.topic.value;
    var digits = phone.replace(/\D/g, "");
    if (name.length < 2) return showError("Укажите, как к вам обращаться", form.elements.name);
    if (digits.length < 10) return showError("Проверьте номер телефона", form.elements.phone);
    var text = "Здравствуйте! Меня зовут " + name + ". Мой телефон: " + phone + "." +
      (topic ? " Интересует: " + topic + "." : "") + " Прошу связаться со мной для записи на приём.";
    window.open(waLink(text), "_blank", "noopener");
  });
})();
