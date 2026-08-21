import { risolviPrimoOrdine } from "../../../assets/js/lib/edo.js";
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

window.katex.render("y' + a\\,y = b", document.getElementById("formula-equazione"), { throwOnError: false });
window.katex.render("y(x) = C\\,e^{-ax} + \\dfrac{b}{a}", document.getElementById("formula-soluzione"), { throwOnError: false });

function aggiornaVisibilitaCauchy() {
  formCauchy.style.display = inputCauchy.checked ? "flex" : "none";
}
inputCauchy.addEventListener("change", aggiornaVisibilitaCauchy);
aggiornaVisibilitaCauchy();

function formattaNumero(v) {
  return Number(v.toFixed(4)).toString();
}

function disegna() {
  erroreProposta.classList.remove("visibile");

  const a = Number(form.a.value);
  const b = Number(form.b.value);
  const conCauchy = inputCauchy.checked;
  const x0 = Number(formCauchy.x0.value);
  const y0 = Number(formCauchy.y0.value);

  const soluzione = risolviPrimoOrdine({
    a, b,
    cauchy: conCauchy ? { x0, y0 } : null,
  });

  avvisoCauchy.classList.toggle("visibile", soluzione.avviso);

  const scope = { a, b, C: soluzione.C };
  let curveProposta = null;
  const testoProposta = inputProposta.value.trim();
  if (testoProposta) {
    try {
      const fn = compilaEspressione(testoProposta);
      curveProposta = (x) => fn({ ...scope, x });
      fn({ ...scope, x: x0 || 0 }); // valuta subito per far emergere eventuali errori
    } catch (e) {
      erroreProposta.textContent = `Soluzione proposta non valida: ${e.message}`;
      erroreProposta.classList.add("visibile");
      curveProposta = null;
    }
  }

  risultati.innerHTML = `<strong>C</strong> = ${formattaNumero(soluzione.C)}` +
    (soluzione.caso === "generale" ? ` &nbsp; (b/a = ${formattaNumero(soluzione.bSuA)})` : "");

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
