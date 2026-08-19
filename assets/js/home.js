import { CATEGORIE, ESPERIMENTI } from "./registry.js";

const elenco = document.getElementById("elenco");

for (const [chiave, nome] of Object.entries(CATEGORIE)) {
  const esperimentiCategoria = ESPERIMENTI.filter((e) => e.categoria === chiave);
  if (esperimentiCategoria.length === 0) continue;

  const sezione = document.createElement("section");
  sezione.innerHTML = `<h2>${nome}</h2>`;

  const lista = document.createElement("ul");
  lista.className = "elenco-esperimenti";
  for (const esperimento of esperimentiCategoria) {
    const voce = document.createElement("li");
    voce.innerHTML = `<a href="${esperimento.path}">${esperimento.titolo}</a>`;
    lista.appendChild(voce);
  }

  sezione.appendChild(lista);
  elenco.appendChild(sezione);
}
