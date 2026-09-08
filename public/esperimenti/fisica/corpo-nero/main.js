import {
  coloreLunghezzaOnda,
  inviluppoMassimiWien,
  lambdaPiccoWien,
  planckRadianza,
  rayleighJeansRadianza,
} from "../../../assets/js/lib/fisica.js";
import { coloriTema, disegnaLinee, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const inputTemperatura = document.getElementById("input-temperatura");
const valoreTemperatura = document.getElementById("valore-temperatura");
const inputRJ = document.getElementById("input-rj");
const inputWien = document.getElementById("input-wien");
const inputScalaX = document.getElementById("input-scala-x");
const valoreScalaX = document.getElementById("valore-scala-x");
const inputScalaY = document.getElementById("input-scala-y");
const valoreScalaY = document.getElementById("valore-scala-y");
const formParametri = document.getElementById("form-parametri");
const formOpzioni = document.getElementById("form-opzioni");
const formScale = document.getElementById("form-scale");
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
  "\\lambda_{picco}\\cdot T = b \\qquad\\Longrightarrow\\qquad B_{max}(\\lambda) \\propto \\dfrac{1}{\\lambda^5}",
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

// i valori di B sono sempre grandi (miliardi o più): sull'asse y si usa
// sempre la notazione scientifica, altrimenti le etichette non ci
// starebbero.
function fmtScientifica(v) {
  if (v === 0) return "0";
  return v.toExponential(1).replace(".", ",").replace("e+", "e");
}

// lo slider della scala verticale è logaritmico (i valori in gioco vanno
// da miliardi a migliaia di miliardi a seconda di T): la posizione è
// l'esponente (in centesimi di decade) e non il valore stesso.
function scalaYDaSlider() {
  const esponente = Number(inputScalaY.value) / 100;
  return Math.pow(10, esponente);
}

function disegna() {
  const T = Number(inputTemperatura.value);
  valoreTemperatura.textContent = fmtIntero(T);

  const xMax = Number(inputScalaX.value);
  valoreScalaX.textContent = fmtIntero(xMax);
  const yMax = scalaYDaSlider();
  valoreScalaY.textContent = yMax.toExponential(2).replace(".", ",");

  const lambdaPiccoNm = lambdaPiccoWien(T) * 1e9;

  // l'asse x resta in nm (comodo per leggere le lunghezze d'onda), ma le
  // curve restano espresse nell'unità naturale delle formule, W/m^3: si
  // converte solo il punto in cui valutarle (nm -> m), non il risultato.
  const planckSI = (nm) => planckRadianza(nm * 1e-9, T);
  const rjSI = (nm) => rayleighJeansRadianza(nm * 1e-9, T);
  const wienSI = (nm) => inviluppoMassimiWien(nm * 1e-9);

  const colori = coloriTema();
  const curve = [{ valuta: planckSI, colore: colori.serie1 }];
  if (inputRJ.checked) curve.push({ valuta: rjSI, colore: colori.serie2, tratteggiata: true });
  if (inputWien.checked) curve.push({ valuta: wienSI, colore: colori.serie3, tratteggiata: true });

  const { ctx, larghezza, altezza } = preparaCanvas(canvas);
  disegnaLinee(ctx, larghezza, altezza, {
    xMin: 0,
    xMax,
    yMin: 0,
    yMax,
    curve,
    fasceSfondo: [FASCIA_VISIBILE],
    etichettaAsseX: "λ (nm)",
    formattaY: fmtScientifica,
    margineSinistra: 62,
  });

  risultati.innerHTML =
    `<strong>T</strong> = ${fmtIntero(T)} K &nbsp; ` +
    `<strong>&lambda;<sub>picco</sub></strong> = ${fmt(lambdaPiccoNm)} nm ` +
    `(&lambda;<sub>picco</sub>&middot;T = 2,898&times;10&#8315;&sup3; m&middot;K)`;
}

formParametri.addEventListener("input", disegna);
formOpzioni.addEventListener("change", disegna);
formScale.addEventListener("input", disegna);
formParametri.addEventListener("submit", (e) => e.preventDefault());
formOpzioni.addEventListener("submit", (e) => e.preventDefault());
formScale.addEventListener("submit", (e) => e.preventDefault());
window.addEventListener("resize", disegna);

disegna();
