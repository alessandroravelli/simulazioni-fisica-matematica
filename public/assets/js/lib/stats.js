// Funzioni statistiche condivise per le simulazioni. Porting della logica
// validata in Python (vedi Bernoulli.py): calcolo in scala logaritmica per
// evitare overflow con n grande, finestra attorno alla media, raggruppamento
// barre con normalizzazione per ampiezza del gruppo.

const LANCZOS_G = 7;
const LANCZOS_COEF = [
  0.99999999999980993, 676.5203681218851, -1259.1392167224028,
  771.32342877765313, -176.61502916214059, 12.507343278686905,
  -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7,
];

// log(Gamma(x)), approssimazione di Lanczos. Usata solo con x >= 1 in questo
// modulo (argomenti sempre della forma intero+1), quindi non serve la
// formula di riflessione per x < 0.5.
export function logGamma(x) {
  let a = LANCZOS_COEF[0];
  const xm1 = x - 1;
  const t = xm1 + LANCZOS_G + 0.5;
  for (let i = 1; i < LANCZOS_G + 2; i++) {
    a += LANCZOS_COEF[i] / (xm1 + i);
  }
  return 0.5 * Math.log(2 * Math.PI) + (xm1 + 0.5) * Math.log(t) - t + Math.log(a);
}

export function logBinomialPmf(k, n, p) {
  if (p <= 0) return k === 0 ? 0 : -Infinity;
  if (p >= 1) return k === n ? 0 : -Infinity;
  return (
    logGamma(n + 1) - logGamma(k + 1) - logGamma(n - k + 1) +
    k * Math.log(p) + (n - k) * Math.log(1 - p)
  );
}

export function binomialPmf(k, n, p) {
  return Math.exp(logBinomialPmf(k, n, p));
}

export function densitaNormale(x, mu, sigma) {
  const z = (x - mu) / sigma;
  return Math.exp(-0.5 * z * z) / (sigma * Math.sqrt(2 * Math.PI));
}

// Integrazione numerica (Simpson) — la CDF della normale non ha una
// primitiva elementare, quindi l'area sotto la curva si calcola così
// invece che con una formula chiusa.
export function integraSimpson(f, a, b, n = 1000) {
  if (n % 2 !== 0) n += 1;
  const h = (b - a) / n;
  let somma = f(a) + f(b);
  for (let i = 1; i < n; i++) {
    somma += f(a + i * h) * (i % 2 === 0 ? 2 : 4);
  }
  return (somma * h) / 3;
}

export function logPoissonPmf(k, lambda) {
  if (lambda <= 0) return k === 0 ? 0 : -Infinity;
  return k * Math.log(lambda) - lambda - logGamma(k + 1);
}

export function poissonPmf(k, lambda) {
  return Math.exp(logPoissonPmf(k, lambda));
}

export function mediaDevStd(n, p) {
  const media = n * p;
  const devStd = Math.sqrt(n * p * (1 - p));
  return { media, devStd };
}

// Tabella di cumulata troncata attorno alla media, per campionare da
// Binomiale(n, p) in tempo O(log larghezza) per campione dopo una
// costruzione O(larghezza) fatta una sola volta (non per ripetizione).
export function creaTabellaCampionamento(n, p) {
  const { media, devStd } = mediaDevStd(n, p);
  const margine = Math.max(12 * devStd, 20);
  const kLo = Math.max(0, Math.floor(media - margine));
  const kHi = Math.min(n, Math.ceil(media + margine));
  const larghezza = kHi - kLo + 1;

  const pmf = new Float64Array(larghezza);
  pmf[0] = binomialPmf(kLo, n, p);
  for (let i = 1; i < larghezza; i++) {
    const k = kLo + i - 1; // passo da k a k+1
    pmf[i] = pmf[i - 1] * ((n - k) / (k + 1)) * (p / (1 - p));
  }

  const cumulativa = new Float64Array(larghezza);
  let somma = 0;
  for (let i = 0; i < larghezza; i++) {
    somma += pmf[i];
    cumulativa[i] = somma;
  }

  return { kLo, kHi, cumulativa, totale: somma };
}

export function campionaDaTabella(tabella) {
  const u = Math.random() * tabella.totale;
  const { cumulativa, kLo } = tabella;
  let lo = 0;
  let hi = cumulativa.length - 1;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (cumulativa[mid] >= u) hi = mid;
    else lo = mid + 1;
  }
  return kLo + lo;
}

// Finestra attorno alla media per la visualizzazione, allargata per
// includere comunque tutti i valori osservati nel campione.
export function finestraVisualizzazione(n, p, campione) {
  const { media, devStd } = mediaDevStd(n, p);
  const margine = Math.max(5 * devStd, 5);
  let minOsservato = media;
  let maxOsservato = media;
  for (let i = 0; i < campione.length; i++) {
    if (campione[i] < minOsservato) minOsservato = campione[i];
    if (campione[i] > maxOsservato) maxOsservato = campione[i];
  }
  let kMin = Math.max(0, Math.floor(Math.min(media - margine, minOsservato)));
  let kMax = Math.min(n, Math.ceil(Math.max(media + margine, maxOsservato)));
  if (kMax <= kMin) {
    kMin = Math.max(0, kMin - 1);
    kMax = Math.min(n, kMax + 1);
  }
  return { kMin, kMax };
}

// Raggruppa [kMin, kMax] in al massimo maxBarre barre. Se larghezzaBin > 1,
// l'altezza di una barra va normalizzata dividendo anche per larghezzaBin
// (bug preso e risolto: senza questa divisione le barre raggruppate
// risultano artificialmente più alte della curva teorica, che resta
// calcolata punto per punto).
export function calcolaBin(kMin, kMax, maxBarre = 200) {
  const ampiezzaFinestra = kMax - kMin + 1;
  const larghezzaBin = Math.max(1, Math.ceil(ampiezzaFinestra / maxBarre));
  const bordi = [];
  for (let k = kMin; k <= kMax + larghezzaBin; k += larghezzaBin) bordi.push(k);
  const centri = [];
  for (let i = 0; i < bordi.length - 1; i++) {
    centri.push(bordi[i] + (larghezzaBin - 1) / 2);
  }
  return { larghezzaBin, bordi, centri, nBin: bordi.length - 1 };
}

// Indici (1..totale) da usare come fotogrammi dell'animazione,
// raggruppando più elementi per fotogramma se totale è molto grande.
export function indiciFotogrammi(totale, maxFotogrammi = 150) {
  const passo = Math.max(1, Math.ceil(totale / maxFotogrammi));
  const indici = [];
  for (let i = passo; i <= totale; i += passo) indici.push(i);
  if (indici.length === 0 || indici[indici.length - 1] !== totale) indici.push(totale);
  return indici;
}
