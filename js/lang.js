/* переключатель языка: русский (по умолчанию), қазақша, english */
(function () {
  var D = window.I18N || {};
  var IDX = { kk: 0, en: 1 };
  var LABEL = { ru: "RU", kk: "KK", en: "EN" };
  var HTML_LANG = { ru: "ru", kk: "kk", en: "en" };
  var current = "ru";
  var origText = new WeakMap();
  var origAttr = new WeakMap();
  var origTitle = document.title;

  function norm(t) { return t.replace(/\s+/g, " ").trim(); }

  function tr(text, lang) {
    if (lang === "ru") return text;
    var e = D[norm(text)];
    return e ? e[IDX[lang]] : text;
  }
  window.i18nT = function (text) { return tr(text, current); };

  function walk(lang) {
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        var p = n.parentNode && n.parentNode.nodeName;
        if (p === "SCRIPT" || p === "STYLE" || p === "NOSCRIPT") return NodeFilter.FILTER_REJECT;
        return /\S/.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var n;
    while ((n = w.nextNode())) {
      if (!origText.has(n)) {
        if (!D[norm(n.nodeValue)]) continue;
        origText.set(n, n.nodeValue);
      }
      var src = origText.get(n);
      if (lang === "ru") { n.nodeValue = src; continue; }
      var m = src.match(/^(\s*)([\s\S]*?)(\s*)$/);
      n.nodeValue = m[1] + tr(src, lang) + m[3];
    }
    document.querySelectorAll("[placeholder]").forEach(function (el) {
      if (!origAttr.has(el)) origAttr.set(el, el.getAttribute("placeholder"));
      el.setAttribute("placeholder", tr(origAttr.get(el), lang));
    });
  }

  function setLang(lang, save) {
    current = lang;
    document.documentElement.lang = HTML_LANG[lang];
    walk(lang);
    document.title = tr(origTitle, lang);
    var cur = document.getElementById("lang-cur");
    if (cur) cur.textContent = LABEL[lang];
    document.querySelectorAll("#lang-menu [data-lang]").forEach(function (b) {
      if (b.getAttribute("data-lang") === lang) b.setAttribute("aria-current", "true");
      else b.removeAttribute("aria-current");
    });
    if (save) { try { localStorage.setItem("lang", lang); } catch (e) {} }
  }

  var btn = document.getElementById("lang-btn");
  var menu = document.getElementById("lang-menu");
  function close() { if (menu) { menu.hidden = true; btn.setAttribute("aria-expanded", "false"); } }
  if (btn && menu) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = menu.hidden;
      menu.hidden = !open;
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    menu.addEventListener("click", function (e) {
      var b = e.target.closest("[data-lang]");
      if (!b) return;
      setLang(b.getAttribute("data-lang"), true);
      close();
    });
    document.addEventListener("click", close);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
  }

  var saved = "ru";
  try { saved = localStorage.getItem("lang") || "ru"; } catch (e) {}
  if (!HTML_LANG[saved]) saved = "ru";
  setLang(saved, false);
})();
