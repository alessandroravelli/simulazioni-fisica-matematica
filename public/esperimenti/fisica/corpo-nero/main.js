import {
  coloreLunghezzaOnda,
  lambdaPiccoWien,
  planckRadianza,
  rayleighJeansRadianza,
  wienRadianza,
} from "../../../assets/js/lib/fisica.js";
import { coloriTema, disegnaLinee, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const inputTemperatura = document.getElementById("input-temperatura");
const valoreTemperatura = document.getElementById("valore-temperatura");
const inputRJ = document.getElementById("input-rj");
const inputWien = document.getElementById("input-wien");
const formParametri = document.getElementById("form-parametri");
const formOpzioni = document.getElementById("form-opzioni");
const risultati = document.getElementById("risultati");
const canvas = document.getElementById("canvas-grafico");

window.katex.render(
  "B_\\lambda(\\lambda,T) = \\dfrac{2hc^2}{\\lambda^5}\\dfrac{1}{e^{hc/(\\lambda k_B T)}-1}",
  document.getElementById("formula-planck"),
  { throwOnError: false },
);
window.katex.render(
  "B_\\lambda^{RJ}(\\lambda,T) = \\dfrac{2 c k_B T}{\\lambda^4}",
  document.getElementById("formula-rj"),
  { throwOnError: false },
);
window.katex.render(
  "B_\\lambda^{W}(\\lambda,T) = \\dfrac{2hc^2}{\\lambda^5}\\, e^{-hc/(\\lambda k_B T)}",
  document.getElementById("formula-wien"),
  { throwOnError: false },
);

// fascia arcobaleno (380-700 nm) per lo sfondo del grafico, costruita
// campionando il colore percepito a intervalli regolari.
const FASCIA_VISIBILE = (() => {
  const tappe = [];
  for (let nm = 380; nm <= 700; nm += 20) {
    tappe.push({ offset: (nm - 380) / (700 - 380), colore: coloreLunghezzaOnda(nm) });
  }
  return { da: 380, a: 700, tappe, alpha: 0.4 };
})();

function fmt(v) {
  return Number(v.toFixed(3)).toString();
}

function fmtIntero(v) {
  return Math.round(v).toLocaleString("it-IT");
}

function disegna() {
  const T = Number(inputTemperatura.value);
  valoreTemperatura.textContent = fmtIntero(T);

  const lambdaPiccoM = lambdaPiccoWien(T);
  const lambdaPiccoNm = lambdaPiccoM * 1e9;
  const bPicco = planckRadianza(lambdaPiccoM, T);

  // gli assi si riscalano sulla temperatura corrente: il picco resta
  // sempre ben visibile, indipendentemente da quanto è caldo il corpo.
  const xMax = lambdaPiccoNm * 4;
  const planckNorm = (nm) => planckRadianza(nm * 1e-9, T) / bPicco;
  const rjNorm = (nm) => rayleighJeansRadianza(nm * 1e-9, T) / bPicco;
  const wienNorm = (nm) => wienRadianza(nm * 1e-9, T) / bPicco;

  const colori = coloriTema();
  const curve = [{ valuta: planckNorm, colore: colori.serie1 }];
  if (inputRJ.checked) curve.push({ valuta: rjNorm, colore: colori.serie2, tratteggiata: true });
  if (inputWien.checked) curve.push({ valuta: wienNorm, colore: colori.serie3, tratteggiata: true });

  const { ctx, larghezza, altezza } = preparaCanvas(canvas);
  disegnaLinee(ctx, larghezza, altezza, {
    xMin: 0,
    xMax,
    yMin: 0,
    yMax: 1.15,
    curve,
    fasceSfondo: [FASCIA_VISIBILE],
    etichettaAsseX: "λ (nm)",
  });

  risultati.innerHTML =
    `<strong>T</strong> = ${fmtIntero(T)} K &nbsp; ` +
    `<strong>&lambda;<sub>picco</sub></strong> = ${fmt(lambdaPiccoNm)} nm ` +
    `(legge dello spostamento di Wien, &lambda;<sub>picco</sub>&middot;T = 2,898&times;10&#8315;&sup3; m&middot;K)`;
}

formParametri.addEventListener("input", disegna);
formOpzioni.addEventListener("change", disegna);
formParametri.addEventListener("submit", (e) => e.preventDefault());
formOpzioni.addEventListener("submit", (e) => e.preventDefault());
window.addEventListener("resize", disegna);

disegna();
