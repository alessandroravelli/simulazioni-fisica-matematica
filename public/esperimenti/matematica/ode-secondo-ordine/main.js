import { creaInterpolatore, integraSecondoOrdineOmogenea } from "../../../assets/js/lib/edo.js";
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

window.katex.render("y'' + p(x)\\,y' + q(x)\\,y = 0", document.getElementById("formula-equazione"), { throwOnError: false });

function aggiornaVisibilitaCauchy() {
  formCauchy.style.display = inputCauchy.checked ? "flex" : "none";
}
inputCauchy.addEventListener("change", aggiornaVisibilitaCauchy);
aggiornaVisibilitaCauchy();

function fmt(v) {
  return Number(v.toFixed(4)).toString();
}

function disegna() {
  erroreProposta.classList.remove("visibile");

  const testoP = form.p.value.trim();
  const testoQ = form.q.value.trim();
  let pFn, qFn;
  try {
    const compilataP = compilaEspressione(testoP || "0");
    const compilataQ = compilaEspressione(testoQ || "0");
    pFn = (x) => compilataP({ x });
    qFn = (x) => compilataQ({ x });
    pFn(0); qFn(0);
  } catch (e) {
    risultati.innerHTML = `<strong>Errore in p(x) o q(x):</strong> ${e.message}`;
    return;
  }

  const conCauchy = inputCauchy.checked;
  const x0 = conCauchy ? Number(formCauchy.x0.value) : 0;
  const y0 = conCauchy ? Number(formCauchy.y0.value) : 0;
  const y0prime = conCauchy ? Number(formCauchy.y0prime.value) : 0;
  avvisoCauchy.classList.toggle("visibile", !conCauchy);

  const xMin = x0 - 6;
  const xMax = x0 + 6;
  const integrazione = integraSecondoOrdineOmogenea(pFn, qFn, x0, y0, y0prime, xMin, xMax);
  const valutaCorretta = creaInterpolatore(integrazione);

  let curveProposta = null;
  const testoProposta = inputProposta.value.trim();
  if (testoProposta) {
    try {
      const fn = compilaEspressione(testoProposta);
      curveProposta = (x) => fn({ x });
      fn({ x: x0 });
    } catch (e) {
      erroreProposta.textContent = `Soluzione proposta non valida: ${e.message}`;
      erroreProposta.classList.add("visibile");
      curveProposta = null;
    }
  }

  risultati.innerHTML =
    `Condizioni iniziali usate: <strong>x&#8320;</strong> = ${fmt(x0)}, ` +
    `<strong>y(x&#8320;)</strong> = ${fmt(y0)}, <strong>y'(x&#8320;)</strong> = ${fmt(y0prime)}`;

  let yMin = Infinity, yMax = -Infinity;
  for (let i = 0; i < integrazione.puntiY.length; i++) {
    const y = integrazione.puntiY[i];
    if (Number.isFinite(y)) { yMin = Math.min(yMin, y); yMax = Math.max(yMax, y); }
  }
  if (!Number.isFinite(yMin)) { yMin = -1; yMax = 1; }
  const margineY = Math.max((yMax - yMin) * 0.2, 0.5);
  yMin -= margineY;
  yMax += margineY;

  const colori = coloriTema();
  const curve = [{ valuta: valutaCorretta, colore: colori.serie2 }];
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
