// Modello semplificato di un magnete permanente (dipolo puntiforme) e del
// flusso che genera attraverso una spira. Il magnete ha orientazione fissa
// (asse N-S lungo l'asse della spira) e viene trascinato liberamente nel
// piano: la "distanza assiale" e lo "scostamento laterale" sono le due
// coordinate del trascinamento in 2D.
//
// Unità arbitrarie: la costante moltiplicativa che in una trattazione reale
// sarebbe mu_0/(4*pi) è assorbita nel parametro "K" (intensità del
// magnete), quindi i valori calcolati non sono in unità SI ma sono
// coerenti fra loro — utili per l'andamento qualitativo, non per calcoli
// quantitativi reali.

// Componente del campo lungo l'asse del dipolo (= asse della spira), nel
// punto (dx, dy) rispetto al centro del magnete (dx lungo l'asse, dy
// perpendicolare). Dipolo orientato lungo l'asse x locale.
export function campoAssialeDipolo(K, dx, dy) {
  const d2 = dx * dx + dy * dy;
  const d = Math.sqrt(d2);
  if (d < 1e-4) return 0;
  return (K * (2 * dx * dx - dy * dy)) / (d2 * d2 * d);
}

// Flusso (approssimato) attraverso la spira: campo nel centro della spira
// per l'area, assumendo il campo del magnete circa uniforme sulla spira
// (approssimazione ragionevole per una spira piccola o a distanza non
// troppo ravvicinata).
export function flussoSpira(K, areaSpira, magnetX, magnetY) {
  const campo = campoAssialeDipolo(K, -magnetX, -magnetY);
  return campo * areaSpira;
}

// Traccia una linea di campo del dipolo (metà superiore, y >= 0) in
// coordinate locali al magnete (magnete nell'origine, orientato lungo +x).
// Equazione classica delle linee di campo di un dipolo: r = C * sin^2(theta).
export function tracciaLineaCampo(C, nPunti = 60) {
  const punti = [];
  const thetaMin = 0.12;
  for (let i = 0; i <= nPunti; i++) {
    const theta = thetaMin + (Math.PI - 2 * thetaMin) * (i / nPunti);
    const r = C * Math.sin(theta) * Math.sin(theta);
    punti.push({ x: r * Math.cos(theta), y: r * Math.sin(theta) });
  }
  return punti;
}

// --- Onda elettromagnetica trasversale: due componenti perpendicolari
// alla propagazione, "ey" (asse verticale di riferimento) e "exPrime"
// (l'altro asse trasversale, perpendicolare a ey e alla propagazione).
// Usate per rappresentare in prospettiva un'onda che si propaga lungo x.

export function faseOnda(x, t, k, w) {
  return k * x - w * t;
}

// Onda polarizzata linearmente a un angolo fisso (in radianti) rispetto
// all'asse "ey". L'ampiezza oscilla in fase su entrambe le componenti.
export function ondaLineare(fase, thetaRad) {
  const mag = Math.cos(fase);
  return { ey: mag * Math.cos(thetaRad), exPrime: mag * Math.sin(thetaRad) };
}

// Onda polarizzata circolarmente: le due componenti hanno la stessa
// ampiezza ma sono sfasate di 90°, quindi il vettore campo ruota
// mantenendo modulo costante mentre l'onda si propaga.
export function ondaCircolare(fase, verso = 1) {
  return { ey: Math.cos(fase), exPrime: verso * Math.sin(fase) };
}

// Angolo di polarizzazione che varia in modo continuo ma "disordinato"
// nello spazio e nel tempo — usato per rappresentare luce non polarizzata
// (la direzione di oscillazione cambia da un tratto d'onda all'altro,
// senza un piano preferenziale).
export function angoloNonPolarizzato(x, t) {
  return 2.3 * Math.sin(x * 0.013 + t * 0.7) + 1.7 * Math.sin(x * 0.021 - t * 1.3 + 1.1);
}

export function ondaNonPolarizzata(x, t, fase) {
  return ondaLineare(fase, angoloNonPolarizzato(x, t));
}

// Applica un filtro polarizzatore a uno stato di polarizzazione in
// ingresso, restituendo lo stato in uscita (tipo, angolo se lineare,
// irradianza). Un polarizzatore circolare è modellato come lineare +
// lamina a quarto d'onda: trasmette sempre metà dell'irradianza in
// ingresso, qualunque sia lo stato in ingresso (non polarizzata, lineare
// o circolare) — semplificazione pedagogica ma fisicamente coerente.
// Un filtro lineare su luce non polarizzata o circolare trasmette metà
// dell'irradianza (nessuna direzione è privilegiata); su luce già
// polarizzata linearmente segue la legge di Malus.
export function applicaFiltro(statoIngresso, filtro) {
  const irradianzaIngresso = statoIngresso.irradianza;

  if (filtro.tipo === "circolare") {
    return { tipo: "circolare", angolo: 0, irradianza: irradianzaIngresso / 2 };
  }

  if (statoIngresso.tipo === "lineare") {
    const deltaAngolo = filtro.angolo - statoIngresso.angolo;
    const fattore = Math.cos(deltaAngolo) * Math.cos(deltaAngolo);
    return { tipo: "lineare", angolo: filtro.angolo, irradianza: irradianzaIngresso * fattore };
  }

  // ingresso non polarizzato o circolare: nessuna direzione privilegiata
  return { tipo: "lineare", angolo: filtro.angolo, irradianza: irradianzaIngresso / 2 };
}

export function campoDaStato(stato, x, t, fase) {
  if (stato.tipo === "nonpolarizzata") return ondaLineare(fase, angoloNonPolarizzato(x, t));
  if (stato.tipo === "circolare") return ondaCircolare(fase);
  return ondaLineare(fase, stato.angolo);
}

// --- Radiazione di corpo nero: legge di Planck e le due approssimazioni
// storiche che ne derivano nei due limiti opposti (grandi/piccole
// lunghezze d'onda rispetto al picco). Costanti fisiche in unità SI;
// lambda va sempre passata in metri.

const H_PLANCK = 6.62607015e-34; // J*s
const C_LUCE = 299792458; // m/s
const K_BOLTZMANN = 1.380649e-23; // J/K
const B_SPOSTAMENTO_WIEN = 2.897771955e-3; // m*K

// Densità spettrale di radianza (per lunghezza d'onda) di un corpo nero
// a temperatura T, alla lunghezza d'onda lambda (metri, kelvin).
export function planckRadianza(lambda, T) {
  if (lambda <= 0 || T <= 0) return 0;
  const esponente = (H_PLANCK * C_LUCE) / (lambda * K_BOLTZMANN * T);
  if (esponente > 700) return 0; // evita overflow di exp per lambda -> 0
  return (2 * H_PLANCK * C_LUCE * C_LUCE) / (Math.pow(lambda, 5) * (Math.exp(esponente) - 1));
}

// Approssimazione di Rayleigh-Jeans: valida per lambda grande (hc <<
// lambda*kB*T). Diverge per lambda -> 0 ("catastrofe ultravioletta").
export function rayleighJeansRadianza(lambda, T) {
  if (lambda <= 0 || T <= 0) return 0;
  return (2 * C_LUCE * K_BOLTZMANN * T) / Math.pow(lambda, 4);
}

// Approssimazione di Wien: valida per lambda piccolo (hc >> lambda*kB*T).
// Sottostima la coda a grandi lunghezze d'onda.
export function wienRadianza(lambda, T) {
  if (lambda <= 0 || T <= 0) return 0;
  const esponente = (H_PLANCK * C_LUCE) / (lambda * K_BOLTZMANN * T);
  if (esponente > 700) return 0;
  return (2 * H_PLANCK * C_LUCE * C_LUCE) / (Math.pow(lambda, 5) * Math.exp(esponente));
}

// Legge dello spostamento di Wien: lunghezza d'onda (metri) del picco di
// emissione a temperatura T.
export function lambdaPiccoWien(T) {
  return B_SPOSTAMENTO_WIEN / T;
}

// Colore RGB approssimato percepito per una lunghezza d'onda visibile
// (nanometri, circa 380-700). Approssimazione classica (Dan Bruton),
// usata solo per disegnare la fascia arcobaleno di sfondo nei grafici.
export function coloreLunghezzaOnda(nm) {
  let r, g, b;
  if (nm < 440) { r = -(nm - 440) / (440 - 380); g = 0; b = 1; }
  else if (nm < 490) { r = 0; g = (nm - 440) / (490 - 440); b = 1; }
  else if (nm < 510) { r = 0; g = 1; b = -(nm - 510) / (510 - 490); }
  else if (nm < 580) { r = (nm - 510) / (580 - 510); g = 1; b = 0; }
  else if (nm < 645) { r = 1; g = -(nm - 645) / (645 - 580); b = 0; }
  else { r = 1; g = 0; b = 0; }

  let fattore;
  if (nm < 420) fattore = 0.3 + (0.7 * (nm - 380)) / (420 - 380);
  else if (nm < 701) fattore = 1;
  else fattore = 0.3 + (0.7 * (780 - nm)) / (780 - 700);

  const gamma = 0.8;
  const adatta = (c) => (c <= 0 ? 0 : Math.round(255 * Math.pow(c * fattore, gamma)));
  return `rgb(${adatta(r)}, ${adatta(g)}, ${adatta(b)})`;
}
