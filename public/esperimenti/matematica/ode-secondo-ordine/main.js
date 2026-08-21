import { risolviSecondoOrdineOmogenea } from "../../../assets/js/lib/edo.js";
import { compilaEspressione } from "../../../assets/js/lib/espressioni.js";
import { coloriTema, disegnaLinee, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const form = document.getElementById("form-parametri");
const formCauchy = document.getElementById("form-cauchy");
const inputCauchy = document.getElementById("input-cauchy");
const inputProposta = document.getElementById("input-proposta");
const avvisoCauchy = document.getElementById("avviso-cauchy");
const erroreProposta = document.getElementById("errore-proposta");
const risultati = document.getElementById("risultati");
const canvas = document.getElementById("canvas-grafico");

window.katex.render("y'' + p\\,y' + q\\,y = 0", document.getElementById("formula-equazione"), { throwOnError: false });
window.katex.render("r^2 + p\\,r + q = 0", document.getElementById("formula-caratteristica"), { throwOnError: false });
window.katex.render("\\Delta > 0:\\quad y(x) = C_1 e^{r_1 x} + C_2 e^{r_2 x}", document.getElementById("formula-caso1"), { throwOnError: false });
window.katex.render("\\Delta = 0:\\quad y(x) = (C_1 + C_2 x)\\, e^{rx}", document.getElementById("formula-caso2"), { throwOnError: false });
window.katex.render("\\Delta < 0:\\quad y(x) = e^{\\alpha x}\\big(C_1 \\cos(\\beta x) + C_2 \\sin(\\beta x)\\big)", document.getElementById("formula-caso3"), { throwOnError: false });

function aggiornaVisibilitaCauchy() {
  formCauchy.style.display = inputCauchy.checked ? "flex" : "none";
}
inputCauchy.addEventListener("change", aggiornaVisibilitaCauchy);
aggiornaVisibilitaCauchy();

function fmt(v) {
  return Number(v.toFixed(4)).toString();
}

function descrizioneCaso(s) {
  if (s.caso === "reali-distinte") return `Radici reali distinte: r&#8321; = ${fmt(s.r1)}, r&#8322; = ${fmt(s.r2)}`;
  if (s.caso === "reale-doppia") return `Radice reale doppia: r = ${fmt(s.r)}`;
  return `Radici complesse coniugate: &alpha; = ${fmt(s.alpha)}, &beta; = ${fmt(s.beta)}`;
}

function disegna() {
  erroreProposta.classList.remove("visibile");

  const p = Number(form.p.value);
  const q = Number(form.q.value);
  const conCauchy = inputCauchy.checked;
  const x0 = Number(formCauchy.x0.value);
  const y0 = Number(formCauchy.y0.value);
  const y0prime = Number(formCauchy.y0prime.value);

  const soluzione = risolviSecondoOrdineOmogenea({
    p, q,
    cauchy: conCauchy ? { x0, y0, y0prime } : null,
  });

  avvisoCauchy.classList.toggle("visibile", soluzione.avviso);

  const scope = { p, q, C1: soluzione.C1, C2: soluzione.C2 };
  let curveProposta = null;
  const testoProposta = inputProposta.value.trim();
  if (testoProposta) {
    try {
      const fn = compilaEspressione(testoProposta);
      curveProposta = (x) => fn({ ...scope, x });
      fn({ ...scope, x: x0 || 0 });
    } catch (e) {
      erroreProposta.textContent = `Soluzione proposta non valida: ${e.message}`;
      erroreProposta.classList.add("visibile");
      curveProposta = null;
    }
  }

  risultati.innerHTML =
    `${descrizioneCaso(soluzione)}<br>` +
    `<strong>C&#8321;</strong> = ${fmt(soluzione.C1)} &nbsp; <strong>C&#8322;</strong> = ${fmt(soluzione.C2)}`;

  const centro = conCauchy ? x0 : 0;
  const xMin = centro - 6;
  const xMax = centro + 6;

  let yMin = Infinity, yMax = -Infinity;
  const N = 200;
  for (let i = 0; i <= N; i++) {
    const x = xMin + ((xMax - xMin) * i) / N;
    const y = soluzione.valuta(x);
    if (Number.isFinite(y)) { yMin = Math.min(yMin, y); yMax = Math.max(yMax, y); }
  }
  if (!Number.isFinite(yMin)) { yMin = -1; yMax = 1; }
  const margineY = Math.max((yMax - yMin) * 0.2, 0.5);
  yMin -= margineY;
  yMax += margineY;

  const colori = coloriTema();
  const curve = [{ valuta: soluzione.valuta, colore: colori.serie2 }];
  if (curveProposta) curve.push({ valuta: curveProposta, colore: colori.serie3, tratteggiata: true });

  const { ctx, larghezza, altezza } = preparaCanvas(canvas);
  disegnaLinee(ctx, larghezza, altezza, { xMin, xMax, yMin, yMax, curve, etichettaAsseX: "x" });
}

form.addEventListener("submit", (e) => { e.preventDefault(); disegna(); });
formCauchy.addEventListener("submit", (e) => e.preventDefault());
inputProposta.addEventListener("input", disegna);
inputCauchy.addEventListener("change", disegna);
formCauchy.addEventListener("input", disegna);
window.addEventListener("resize", disegna);

disegna();
