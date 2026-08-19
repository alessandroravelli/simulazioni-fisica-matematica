import {
  binomialPmf,
  calcolaBin,
  campionaDaTabella,
  creaTabellaCampionamento,
  finestraVisualizzazione,
  indiciFotogrammi,
  poissonPmf,
} from "../../../assets/js/lib/stats.js";
import {
  animaBernoulliRipetuto,
  attesa,
  coloriTema,
  disegnaIstogrammaConCurve,
  preparaCanvas,
} from "../../../assets/js/lib/grafici.js";

const form = document.getElementById("form-parametri");
const bottoneGenera = document.getElementById("bottone-genera");
const canvasSingolo = document.getElementById("canvas-singolo");
const canvasDistribuzione = document.getElementById("canvas-distribuzione");
const titoloSingolo = document.getElementById("titolo-singolo");
const titoloDistribuzione = document.getElementById("titolo-distribuzione");
const testoP = document.getElementById("testo-p");

const INTERVALLO_MS = 90;

window.katex.render("P(X = k) = \\dfrac{\\lambda^{k} e^{-\\lambda}}{k!}", document.getElementById("formula"), {
  throwOnError: false,
});

function aggiornaTestoP() {
  const lambda = Number(form.lambda.value);
  const n = Number(form.n.value);
  if (!(lambda > 0) || !(n > lambda)) {
    testoP.textContent = "n deve essere maggiore di λ, altrimenti p = λ/n non è una probabilità valida.";
    return null;
  }
  const p = lambda / n;
  testoP.textContent = `p = λ/n = ${p.toPrecision(4)}`;
  return p;
}

form.lambda.addEventListener("input", aggiornaTestoP);
form.n.addEventListener("input", aggiornaTestoP);

async function animaDistribuzione(p, n, lambda, numRipetizioni) {
  const tabella = creaTabellaCampionamento(n, p);
  const campione = new Float64Array(numRipetizioni);
  for (let i = 0; i < numRipetizioni; i++) campione[i] = campionaDaTabella(tabella);

  const { kMin, kMax } = finestraVisualizzazione(n, p, campione);
  const { larghezzaBin, centri, nBin } = calcolaBin(kMin, kMax, 200);
  const ampiezzaFinestra = kMax - kMin + 1;
  const mostraMarker = ampiezzaFinestra <= 60;

  const valoriK = [];
  for (let k = kMin; k <= kMax; k++) valoriK.push(k);
  const pmfBinomiale = valoriK.map((k) => binomialPmf(k, n, p));
  const pmfPoisson = valoriK.map((k) => poissonPmf(k, lambda));

  const binDi = (k) => {
    let idx = Math.floor((k - kMin) / larghezzaBin);
    if (idx < 0) idx = 0;
    if (idx >= nBin) idx = nBin - 1;
    return idx;
  };

  const conteggiFinali = new Int32Array(nBin);
  for (let i = 0; i < numRipetizioni; i++) conteggiFinali[binDi(campione[i])] += 1;
  let yMax = 0;
  for (let i = 0; i < pmfBinomiale.length; i++) yMax = Math.max(yMax, pmfBinomiale[i], pmfPoisson[i]);
  for (let i = 0; i < nBin; i++) yMax = Math.max(yMax, conteggiFinali[i] / numRipetizioni / larghezzaBin);
  yMax *= 1.3;

  const { ctx, larghezza, altezza } = preparaCanvas(canvasDistribuzione);
  const colori = coloriTema();
  const indici = indiciFotogrammi(numRipetizioni);
  const conteggi = new Int32Array(nBin);
  const altezzeBarre = new Float64Array(nBin);

  let ultimoIndice = 0;
  for (let f = 0; f < indici.length; f++) {
    const fin = indici[f];
    for (let i = ultimoIndice; i < fin; i++) conteggi[binDi(campione[i])] += 1;
    ultimoIndice = fin;

    for (let i = 0; i < nBin; i++) altezzeBarre[i] = conteggi[i] / fin / larghezzaBin;

    disegnaIstogrammaConCurve(ctx, larghezza, altezza, {
      kMin, kMax, centri, larghezzaBin, altezzeBarre, yMax,
      curve: [
        { valoriK, pmf: pmfBinomiale, colore: colori.serie2, mostraMarker },
        { valoriK, pmf: pmfPoisson, colore: colori.serie3, mostraMarker },
      ],
      etichettaAsseX: "Numero di eventi",
    });
    titoloDistribuzione.textContent = `Distribuzione da ripetizioni — ripetizione ${fin}/${numRipetizioni}`;
    await attesa(INTERVALLO_MS);
  }
}

// --- Orchestrazione ---

let animazioneInCorso = false;

async function avvia(p, n, lambda, numRipetizioni) {
  animazioneInCorso = true;
  bottoneGenera.disabled = true;
  try {
    await Promise.all([
      animaBernoulliRipetuto(canvasSingolo, titoloSingolo, p, n, {
        intervalloMs: INTERVALLO_MS,
        prefissoTitolo: "Singolo esperimento",
        indiciFotogrammi,
      }),
      animaDistribuzione(p, n, lambda, numRipetizioni),
    ]);
  } finally {
    animazioneInCorso = false;
    bottoneGenera.disabled = false;
  }
}

form.addEventListener("submit", (evento) => {
  evento.preventDefault();
  if (animazioneInCorso) return;
  const lambda = Number(form.lambda.value);
  const n = Math.round(Number(form.n.value));
  const numRipetizioni = Math.round(Number(form.ripetizioni.value));
  const p = aggiornaTestoP();
  if (p === null || !(numRipetizioni >= 1)) return;
  avvia(p, n, lambda, numRipetizioni);
});

const pIniziale = aggiornaTestoP();
if (pIniziale !== null) {
  avvia(pIniziale, Math.round(Number(form.n.value)), Number(form.lambda.value), Math.round(Number(form.ripetizioni.value)));
}
