import { densitaNormale, integraSimpson } from "../../../assets/js/lib/stats.js";
import { coloriTema, disegnaLinee, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const formParametri = document.getElementById("form-parametri");
const formArea = document.getElementById("form-area");
const inputTipo = document.getElementById("input-tipo");
const campoB = document.getElementById("campo-b");
const risultati = document.getElementById("risultati");
const canvas = document.getElementById("canvas-grafico");

window.katex.render(
  "f(x) = \\dfrac{1}{\\sigma\\sqrt{2\\pi}}\\, e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}",
  document.getElementById("formula"),
  { throwOnError: false },
);

function aggiornaVisibilitaB() {
  campoB.style.display = inputTipo.value === "tra" ? "flex" : "none";
}
inputTipo.addEventListener("change", () => { aggiornaVisibilitaB(); disegna(); });
aggiornaVisibilitaB();

function fmt(v) {
  return Number(v.toFixed(4)).toString();
}

function disegna() {
  const mu = Number(formParametri.mu.value);
  const sigma = Math.max(1e-6, Number(formParametri.sigma.value));
  const tipo = inputTipo.value;
  const a = Number(formArea.a.value);
  const b = Number(formArea.b.value);

  const densita = (x) => densitaNormale(x, mu, sigma);

  const xMin = mu - 5 * sigma;
  const xMax = mu + 5 * sigma;

  let da, a2, etichetta;
  if (tipo === "tra") {
    da = Math.min(a, b); a2 = Math.max(a, b);
    etichetta = `P(${fmt(da)} &le; X &le; ${fmt(a2)})`;
  } else if (tipo === "minore") {
    da = xMin - 10 * sigma; a2 = a;
    etichetta = `P(X &le; ${fmt(a)})`;
  } else {
    da = a; a2 = xMax + 10 * sigma;
    etichetta = `P(X &ge; ${fmt(a)})`;
  }

  const probabilita = integraSimpson(densita, da, a2, 2000);
  risultati.innerHTML = `<strong>${etichetta}</strong> = ${fmt(probabilita)}`;

  const yMax = densitaNormale(mu, mu, sigma) * 1.25;

  const colori = coloriTema();
  const { ctx, larghezza, altezza } = preparaCanvas(canvas);
  disegnaLinee(ctx, larghezza, altezza, {
    xMin, xMax, yMin: 0, yMax,
    curve: [{ valuta: densita, colore: colori.serie2 }],
    aree: [{ valuta: densita, da, a: a2, colore: `${colori.serie1}55` }],
    etichettaAsseX: "x",
  });
}

formParametri.addEventListener("input", disegna);
formArea.addEventListener("input", disegna);
formArea.addEventListener("submit", (e) => e.preventDefault());
formParametri.addEventListener("submit", (e) => e.preventDefault());
window.addEventListener("resize", disegna);

disegna();
