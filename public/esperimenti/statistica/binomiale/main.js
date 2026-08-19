import {
  binomialPmf,
  calcolaBin,
  campionaDaTabella,
  creaTabellaCampionamento,
  finestraVisualizzazione,
  indiciFotogrammi,
} from "../../../assets/js/lib/stats.js";

const form = document.getElementById("form-parametri");
const bottoneGenera = document.getElementById("bottone-genera");
const canvasSingolo = document.getElementById("canvas-singolo");
const canvasDistribuzione = document.getElementById("canvas-distribuzione");
const titoloSingolo = document.getElementById("titolo-singolo");
const titoloDistribuzione = document.getElementById("titolo-distribuzione");

const INTERVALLO_MS = 90;

window.katex.render("P(X = k) = \\binom{n}{k}\\, p^{k} (1-p)^{n-k}", document.getElementById("formula"), {
  throwOnError: false,
});

function coloriTema() {
  const stile = getComputedStyle(document.documentElement);
  return {
    serie1: stile.getPropertyValue("--accent").trim(),
    serie2: stile.getPropertyValue("--serie-2").trim(),
    testo: stile.getPropertyValue("--fg").trim(),
    testoMuto: stile.getPropertyValue("--fg-muted").trim(),
    griglia: stile.getPropertyValue("--border").trim(),
  };
}

function preparaCanvas(canvas) {
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  canvas.width = Math.round(rect.width * dpr);
  canvas.height = Math.round(rect.height * dpr);
  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  return { ctx, larghezza: rect.width, altezza: rect.height };
}

function attesa(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Valori "tondi" per i tick di un asse (passo 1/2/5 * potenza di 10).
function calcolaTick(min, max, countCirca) {
  if (max <= min) return [min];
  const grezzo = (max - min) / countCirca;
  const esponente = Math.floor(Math.log10(grezzo));
  const base = Math.pow(10, esponente);
  const frazione = grezzo / base;
  let passo;
  if (frazione < 1.5) passo = base;
  else if (frazione < 3) passo = 2 * base;
  else if (frazione < 7) passo = 5 * base;
  else passo = 10 * base;

  const tick = [];
  const primo = Math.ceil(min / passo) * passo;
  for (let v = primo; v <= max + passo * 1e-9; v += passo) tick.push(v);
  return tick;
}

function formattaIntero(v) {
  return Math.round(v).toLocaleString("it-IT");
}

function formattaDecimale(v) {
  return Number(v.toPrecision(6)).toString().replace(".", ",");
}

// --- Grafico 1: singolo esperimento (due barre: successo / insuccesso) ---

function disegnaSingolo(ctx, larghezza, altezza, { successi, insuccessi, n }) {
  const colori = coloriTema();
  ctx.clearRect(0, 0, larghezza, altezza);

  const margine = { sopra: 24, sotto: 32, sinistra: 8, destra: 8 };
  const areaAltezza = altezza - margine.sopra - margine.sotto;
  const yMax = n * 1.15;
  const yScala = (v) => margine.sopra + areaAltezza * (1 - v / yMax);

  // asse base
  ctx.strokeStyle = colori.griglia;
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(margine.sinistra, yScala(0));
  ctx.lineTo(larghezza - margine.destra, yScala(0));
  ctx.stroke();

  const barreLarghezza = (larghezza - margine.sinistra - margine.destra) * 0.28;
  const centri = [larghezza * 0.32, larghezza * 0.68];
  const valori = [successi, insuccessi];
  const etichette = ["Successo", "Insuccesso"];
  const colori2 = [colori.serie1, colori.serie2];

  ctx.textAlign = "center";
  ctx.font = "600 13px -apple-system, sans-serif";

  for (let i = 0; i < 2; i++) {
    const x = centri[i] - barreLarghezza / 2;
    const yTop = yScala(valori[i]);
    ctx.fillStyle = colori2[i];
    ctx.fillRect(x, yTop, barreLarghezza, yScala(0) - yTop);

    ctx.fillStyle = colori.testo;
    ctx.fillText(String(valori[i]), centri[i], yTop - 8);

    ctx.fillStyle = colori.testoMuto;
    ctx.font = "12px -apple-system, sans-serif";
    ctx.fillText(etichette[i], centri[i], altezza - 10);
    ctx.font = "600 13px -apple-system, sans-serif";
  }
}

async function animaSingoloEsperimento(p, n) {
  const esiti = new Uint8Array(n);
  const indici = indiciFotogrammi(n);
  const successiPerFrame = new Int32Array(indici.length);

  let cumSuccessi = 0;
  let frameCorrente = 0;
  for (let i = 0; i < n; i++) {
    const successo = Math.random() < p ? 1 : 0;
    esiti[i] = successo;
    cumSuccessi += successo;
    if (frameCorrente < indici.length && i + 1 === indici[frameCorrente]) {
      successiPerFrame[frameCorrente] = cumSuccessi;
      frameCorrente += 1;
    }
  }

  const { ctx, larghezza, altezza } = preparaCanvas(canvasSingolo);

  for (let f = 0; f < indici.length; f++) {
    const fin = indici[f];
    const successi = successiPerFrame[f];
    const insuccessi = fin - successi;
    disegnaSingolo(ctx, larghezza, altezza, { successi, insuccessi, n });
    titoloSingolo.textContent = `Singolo esperimento binomiale — prova ${fin}/${n}`;
    await attesa(INTERVALLO_MS);
  }
}

// --- Grafico 2: distribuzione da ripetizioni (istogramma + PMF teorica) ---

function disegnaDistribuzione(ctx, larghezza, altezza, dati) {
  const { kMin, kMax, centri, larghezzaBin, altezzeBarre, valoriK, pmfTeorica, yMax, mostraMarker } = dati;
  const colori = coloriTema();
  ctx.clearRect(0, 0, larghezza, altezza);

  const margine = { sopra: 16, sotto: 48, sinistra: 52, destra: 12 };
  const areaAltezza = altezza - margine.sopra - margine.sotto;
  const areaLarghezza = larghezza - margine.sinistra - margine.destra;
  const xDominio = [kMin - 1, kMax + 1];
  const xScala = (k) => margine.sinistra + areaLarghezza * ((k - xDominio[0]) / (xDominio[1] - xDominio[0]));
  const yScala = (v) => margine.sopra + areaAltezza * (1 - v / yMax);

  // griglia orizzontale + etichette asse y
  const tickY = calcolaTick(0, yMax, 4);
  ctx.strokeStyle = colori.griglia;
  ctx.lineWidth = 1;
  ctx.fillStyle = colori.testoMuto;
  ctx.font = "11px -apple-system, sans-serif";
  ctx.textAlign = "right";
  ctx.textBaseline = "middle";
  for (const v of tickY) {
    const y = yScala(v);
    ctx.beginPath();
    ctx.moveTo(margine.sinistra, y);
    ctx.lineTo(larghezza - margine.destra, y);
    ctx.stroke();
    ctx.fillText(formattaDecimale(v), margine.sinistra - 8, y);
  }
  ctx.textBaseline = "alphabetic";

  // asse base + tick/etichette asse x
  ctx.strokeStyle = colori.testoMuto;
  ctx.beginPath();
  ctx.moveTo(margine.sinistra, yScala(0));
  ctx.lineTo(larghezza - margine.destra, yScala(0));
  ctx.stroke();

  const tickX = calcolaTick(kMin, kMax, Math.min(7, Math.floor(areaLarghezza / 70)));
  ctx.strokeStyle = colori.testoMuto;
  ctx.fillStyle = colori.testoMuto;
  ctx.textAlign = "center";
  for (const v of tickX) {
    const x = xScala(v);
    ctx.beginPath();
    ctx.moveTo(x, yScala(0));
    ctx.lineTo(x, yScala(0) + 5);
    ctx.stroke();
    ctx.fillText(formattaIntero(v), x, yScala(0) + 18);
  }

  // barre (frequenza osservata)
  ctx.fillStyle = colori.serie1;
  const largBarraPx = Math.max(1, (areaLarghezza / (xDominio[1] - xDominio[0])) * larghezzaBin * 0.9);
  for (let i = 0; i < centri.length; i++) {
    const xCentro = xScala(centri[i]);
    const yTop = yScala(altezzeBarre[i]);
    ctx.fillRect(xCentro - largBarraPx / 2, yTop, largBarraPx, yScala(0) - yTop);
  }

  // curva teorica (distribuzione binomiale B(n,p))
  ctx.strokeStyle = colori.serie2;
  ctx.lineWidth = 1.8;
  ctx.beginPath();
  for (let i = 0; i < valoriK.length; i++) {
    const x = xScala(valoriK[i]);
    const y = yScala(pmfTeorica[i]);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.stroke();

  if (mostraMarker) {
    ctx.fillStyle = colori.serie2;
    for (let i = 0; i < valoriK.length; i++) {
      const x = xScala(valoriK[i]);
      const y = yScala(pmfTeorica[i]);
      ctx.beginPath();
      ctx.arc(x, y, 2.2, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  ctx.fillStyle = colori.testoMuto;
  ctx.font = "12px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("Numero di successi su n prove", (margine.sinistra + larghezza - margine.destra) / 2, altezza - 6);
}

async function animaDistribuzione(p, n, numRipetizioni) {
  const tabella = creaTabellaCampionamento(n, p);
  const campione = new Float64Array(numRipetizioni);
  for (let i = 0; i < numRipetizioni; i++) campione[i] = campionaDaTabella(tabella);

  const { kMin, kMax } = finestraVisualizzazione(n, p, campione);
  const { larghezzaBin, centri, nBin } = calcolaBin(kMin, kMax, 200);
  const ampiezzaFinestra = kMax - kMin + 1;
  const mostraMarker = ampiezzaFinestra <= 60;

  const valoriK = [];
  for (let k = kMin; k <= kMax; k++) valoriK.push(k);
  const pmfTeorica = valoriK.map((k) => binomialPmf(k, n, p));

  const binDi = (k) => {
    let idx = Math.floor((k - kMin) / larghezzaBin);
    if (idx < 0) idx = 0;
    if (idx >= nBin) idx = nBin - 1;
    return idx;
  };

  // y massimo fissato prima dell'animazione (come nel prototipo Python),
  // così l'asse non "salta" durante la costruzione dell'istogramma.
  const conteggiFinali = new Int32Array(nBin);
  for (let i = 0; i < numRipetizioni; i++) conteggiFinali[binDi(campione[i])] += 1;
  let yMax = 0;
  for (let i = 0; i < pmfTeorica.length; i++) yMax = Math.max(yMax, pmfTeorica[i]);
  for (let i = 0; i < nBin; i++) yMax = Math.max(yMax, conteggiFinali[i] / numRipetizioni / larghezzaBin);
  yMax *= 1.3;

  const { ctx, larghezza, altezza } = preparaCanvas(canvasDistribuzione);
  const indici = indiciFotogrammi(numRipetizioni);
  const conteggi = new Int32Array(nBin);
  const altezzeBarre = new Float64Array(nBin);

  let ultimoIndice = 0;
  for (let f = 0; f < indici.length; f++) {
    const fin = indici[f];
    for (let i = ultimoIndice; i < fin; i++) conteggi[binDi(campione[i])] += 1;
    ultimoIndice = fin;

    for (let i = 0; i < nBin; i++) altezzeBarre[i] = conteggi[i] / fin / larghezzaBin;

    disegnaDistribuzione(ctx, larghezza, altezza, {
      kMin, kMax, centri, larghezzaBin, altezzeBarre, valoriK, pmfTeorica, yMax, mostraMarker,
    });
    titoloDistribuzione.textContent = `Distribuzione binomiale — ripetizione ${fin}/${numRipetizioni}`;
    await attesa(INTERVALLO_MS);
  }
}

// --- Orchestrazione ---

let animazioneInCorso = false;

async function avvia(p, n, numRipetizioni) {
  animazioneInCorso = true;
  bottoneGenera.disabled = true;
  try {
    await Promise.all([
      animaSingoloEsperimento(p, n),
      animaDistribuzione(p, n, numRipetizioni),
    ]);
  } finally {
    animazioneInCorso = false;
    bottoneGenera.disabled = false;
  }
}

form.addEventListener("submit", (evento) => {
  evento.preventDefault();
  if (animazioneInCorso) return;
  const p = Number(form.p.value);
  const n = Math.round(Number(form.n.value));
  const numRipetizioni = Math.round(Number(form.ripetizioni.value));
  if (!(p > 0 && p < 1) || !(n >= 1) || !(numRipetizioni >= 1)) return;
  avvia(p, n, numRipetizioni);
});

avvia(Number(form.p.value), Math.round(Number(form.n.value)), Math.round(Number(form.ripetizioni.value)));
