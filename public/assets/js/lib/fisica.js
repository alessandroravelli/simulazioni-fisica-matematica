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
