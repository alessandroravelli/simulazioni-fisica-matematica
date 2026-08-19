import { CATEGORIE, ESPERIMENTI } from "./registry.js";

const elenco = document.getElementById("elenco");

for (const [chiave, nome] of Object.entries(CATEGORIE)) {
  const esperimentiCategoria = ESPERIMENTI.filter((e) => e.categoria === chiave);
  if (esperimentiCategoria.length === 0) continue;

  const sezione = document.createElement("section");
  sezione.className = "categoria";
  sezione.innerHTML = `<h2>${nome}</h2>`;

  const griglia = document.createElement("div");
  griglia.className = "griglia-esperimenti";
  for (const esperimento of esperimentiCategoria) {
    const card = document.createElement("a");
    card.className = "card-esperimento";
    card.href = esperimento.path;
    card.innerHTML = `<span class="card-titolo">${esperimento.titolo}</span><span class="card-freccia">&rarr;</span>`;
    griglia.appendChild(card);
  }

  sezione.appendChild(griglia);
  elenco.appendChild(sezione);
}
