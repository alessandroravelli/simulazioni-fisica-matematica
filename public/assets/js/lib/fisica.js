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
