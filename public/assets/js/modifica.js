// Pulsanti per il docente (li inserisce il Worker solo per il ruolo
// docente): "Modifica" apre la nota della pagina corrente nell'editor web
// di GitHub, "Nuova nota" crea un file nella stessa cartella. Dopo il
// salvataggio ("Commit changes") Cloudflare ricostruisce il sito da solo.
(async () => {
  const REPO = "https://github.com/alessandroravelli/simulazioni-fisica-matematica";
  const RADICE = "sito/content";

  let slug = decodeURIComponent(location.pathname).replace(/^\/+/, "").replace(/\.html$/, "");
  if (slug === "" || slug.endsWith("/")) slug += "index";

  let indice;
  try {
    indice = await fetch("/static/contentIndex.json").then((r) => r.json());
  } catch {
    return;
  }

  const voce = indice[slug];
  const percorsoFile = voce && voce.filePath;
  const codifica = (p) => p.split("/").map(encodeURIComponent).join("/");
  const cartella = percorsoFile ? percorsoFile.split("/").slice(0, -1).join("/") : "";

  const barra = document.createElement("div");
  barra.className = "barra-docente";

  const pulsante = (testo, href, titolo) => {
    const a = document.createElement("a");
    a.textContent = testo;
    a.href = href;
    a.title = titolo;
    a.target = "_blank";
    a.rel = "noopener";
    barra.append(a);
  };

  if (percorsoFile) {
    pulsante("✎ Modifica", `${REPO}/edit/main/${codifica(`${RADICE}/${percorsoFile}`)}`,
      `Modifica ${percorsoFile} su GitHub`);
  }
  pulsante("＋ Nuova nota", `${REPO}/new/main/${codifica(cartella ? `${RADICE}/${cartella}` : RADICE)}`,
    "Crea una nuova nota in questa cartella su GitHub");

  document.body.append(barra);
})();
