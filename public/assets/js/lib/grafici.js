// Utilità condivise per disegnare i grafici canvas delle simulazioni
// (colori da tema, scaling ad alta densità, assi con tick "tondi").

export function coloriTema() {
  const stile = getComputedStyle(document.documentElement);
  return {
    serie1: stile.getPropertyValue("--accent").trim(),
    serie2: stile.getPropertyValue("--serie-2").trim(),
    serie3: stile.getPropertyValue("--serie-3").trim(),
    testo: stile.getPropertyValue("--fg").trim(),
    testoMuto: stile.getPropertyValue("--fg-muted").trim(),
    griglia: stile.getPropertyValue("--border").trim(),
  };
}

export function preparaCanvas(canvas) {
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  canvas.width = Math.round(rect.width * dpr);
  canvas.height = Math.round(rect.height * dpr);
  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  return { ctx, larghezza: rect.width, altezza: rect.height };
}

export function attesa(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Valori "tondi" per i tick di un asse (passo 1/2/5 * potenza di 10).
export function calcolaTick(min, max, countCirca) {
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

export function formattaIntero(v) {
  return Math.round(v).toLocaleString("it-IT");
}

export function formattaDecimale(v) {
  return Number(v.toPrecision(6)).toString().replace(".", ",");
}

// Grafico a due barre affiancate (es. successo / insuccesso).
export function disegnaBarreDue(ctx, larghezza, altezza, { valori, etichette, colori: coloriBarre, yMax }) {
  const colori = coloriTema();
  ctx.clearRect(0, 0, larghezza, altezza);

  const margine = { sopra: 24, sotto: 32, sinistra: 8, destra: 8 };
  const areaAltezza = altezza - margine.sopra - margine.sotto;
  const yScala = (v) => margine.sopra + areaAltezza * (1 - v / yMax);

  ctx.strokeStyle = colori.griglia;
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(margine.sinistra, yScala(0));
  ctx.lineTo(larghezza - margine.destra, yScala(0));
  ctx.stroke();

  const barreLarghezza = (larghezza - margine.sinistra - margine.destra) * 0.28;
  const centri = [larghezza * 0.32, larghezza * 0.68];

  ctx.textAlign = "center";
  ctx.font = "600 13px -apple-system, sans-serif";

  for (let i = 0; i < 2; i++) {
    const x = centri[i] - barreLarghezza / 2;
    const yTop = yScala(valori[i]);
    ctx.fillStyle = coloriBarre[i];
    ctx.fillRect(x, yTop, barreLarghezza, yScala(0) - yTop);

    ctx.fillStyle = colori.testo;
    ctx.fillText(String(valori[i]), centri[i], yTop - 8);

    ctx.fillStyle = colori.testoMuto;
    ctx.font = "12px -apple-system, sans-serif";
    ctx.fillText(etichette[i], centri[i], altezza - 10);
    ctx.font = "600 13px -apple-system, sans-serif";
  }
}

// Anima n prove di Bernoulli(p) in sequenza, aggiornando due contatori
// (successo/insuccesso) fino a esaurimento delle prove, poi resta ferma
// sull'ultimo fotogramma.
export async function animaBernoulliRipetuto(canvas, elementoTitolo, p, n, { intervalloMs, prefissoTitolo, indiciFotogrammi }) {
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

  const { ctx, larghezza, altezza } = preparaCanvas(canvas);
  const colori = coloriTema();

  for (let f = 0; f < indici.length; f++) {
    const fin = indici[f];
    const successi = successiPerFrame[f];
    const insuccessi = fin - successi;
    disegnaBarreDue(ctx, larghezza, altezza, {
      valori: [successi, insuccessi],
      etichette: ["Successo", "Insuccesso"],
      colori: [colori.serie1, colori.serie2],
      yMax: n * 1.15,
    });
    elementoTitolo.textContent = `${prefissoTitolo} — prova ${fin}/${n}`;
    await attesa(intervalloMs);
  }
}

// Grafico a curve continue (es. soluzioni di equazioni differenziali).
// `curve`: array di { valuta(x) => y, colore, tratteggiata }.
export function disegnaLinee(ctx, larghezza, altezza, dati) {
  const { xMin, xMax, yMin, yMax, curve, aree, etichettaAsseX } = dati;
  const colori = coloriTema();
  ctx.clearRect(0, 0, larghezza, altezza);

  const margine = { sopra: 16, sotto: 48, sinistra: 56, destra: 12 };
  const areaAltezza = altezza - margine.sopra - margine.sotto;
  const areaLarghezza = larghezza - margine.sinistra - margine.destra;
  const xScala = (x) => margine.sinistra + areaLarghezza * ((x - xMin) / (xMax - xMin));
  const yScala = (v) => margine.sopra + areaAltezza * (1 - (v - yMin) / (yMax - yMin));

  const tickY = calcolaTick(yMin, yMax, 5);
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

  // asse x: alla quota y=0 se ricade nel range visibile, altrimenti al bordo
  const yAsse = Math.min(Math.max(0, yMin), yMax);
  ctx.strokeStyle = colori.testoMuto;
  ctx.beginPath();
  ctx.moveTo(margine.sinistra, yScala(yAsse));
  ctx.lineTo(larghezza - margine.destra, yScala(yAsse));
  ctx.stroke();

  const tickX = calcolaTick(xMin, xMax, Math.min(8, Math.floor(areaLarghezza / 60)));
  ctx.fillStyle = colori.testoMuto;
  ctx.textAlign = "center";
  for (const v of tickX) {
    const x = xScala(v);
    ctx.beginPath();
    ctx.moveTo(x, yScala(yAsse));
    ctx.lineTo(x, yScala(yAsse) + 5);
    ctx.stroke();
    ctx.fillText(formattaDecimale(v), x, yScala(yAsse) + 18);
  }

  const N = 400;

  // aree ombreggiate sotto una curva (es. probabilità in un intervallo),
  // disegnate prima delle linee così restano "sotto" al tratto della curva
  if (aree) {
    for (const reg of aree) {
      const daClamp = Math.max(reg.da, xMin);
      const aClamp = Math.min(reg.a, xMax);
      if (aClamp <= daClamp) continue;
      ctx.fillStyle = reg.colore;
      ctx.beginPath();
      ctx.moveTo(xScala(daClamp), yScala(yAsse));
      for (let i = 0; i <= N; i++) {
        const x = daClamp + ((aClamp - daClamp) * i) / N;
        let y;
        try { y = reg.valuta(x); } catch { y = 0; }
        if (!Number.isFinite(y)) y = 0;
        ctx.lineTo(xScala(x), yScala(Math.max(yMin, Math.min(yMax, y))));
      }
      ctx.lineTo(xScala(aClamp), yScala(yAsse));
      ctx.closePath();
      ctx.fill();
    }
  }

  for (const c of curve) {
    ctx.strokeStyle = c.colore;
    ctx.lineWidth = 2;
    ctx.setLineDash(c.tratteggiata ? [7, 5] : []);
    ctx.beginPath();
    let inCorso = false;
    for (let i = 0; i <= N; i++) {
      const x = xMin + ((xMax - xMin) * i) / N;
      let y;
      try { y = c.valuta(x); } catch { y = NaN; }
      if (!Number.isFinite(y) || y < yMin - (yMax - yMin) * 2 || y > yMax + (yMax - yMin) * 2) {
        inCorso = false;
        continue;
      }
      const px = xScala(x);
      const py = yScala(y);
      if (!inCorso) { ctx.moveTo(px, py); inCorso = true; }
      else ctx.lineTo(px, py);
    }
    ctx.stroke();
  }
  ctx.setLineDash([]);

  ctx.fillStyle = colori.testoMuto;
  ctx.font = "12px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(etichettaAsseX, (margine.sinistra + larghezza - margine.destra) / 2, altezza - 6);
}

// Istogramma (frequenza osservata) con una o più curve teoriche sovrapposte.
// `curve`: array di { valoriK, pmf, colore, mostraMarker }.
export function disegnaIstogrammaConCurve(ctx, larghezza, altezza, dati) {
  const { kMin, kMax, centri, larghezzaBin, altezzeBarre, yMax, curve, etichettaAsseX } = dati;
  const colori = coloriTema();
  ctx.clearRect(0, 0, larghezza, altezza);

  const margine = { sopra: 16, sotto: 48, sinistra: 52, destra: 12 };
  const areaAltezza = altezza - margine.sopra - margine.sotto;
  const areaLarghezza = larghezza - margine.sinistra - margine.destra;
  const xDominio = [kMin - 1, kMax + 1];
  const xScala = (k) => margine.sinistra + areaLarghezza * ((k - xDominio[0]) / (xDominio[1] - xDominio[0]));
  const yScala = (v) => margine.sopra + areaAltezza * (1 - v / yMax);

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

  ctx.fillStyle = colori.serie1;
  const largBarraPx = Math.max(1, (areaLarghezza / (xDominio[1] - xDominio[0])) * larghezzaBin * 0.9);
  for (let i = 0; i < centri.length; i++) {
    const xCentro = xScala(centri[i]);
    const yTop = yScala(altezzeBarre[i]);
    ctx.fillRect(xCentro - largBarraPx / 2, yTop, largBarraPx, yScala(0) - yTop);
  }

  for (const c of curve) {
    ctx.strokeStyle = c.colore;
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    for (let i = 0; i < c.valoriK.length; i++) {
      const x = xScala(c.valoriK[i]);
      const y = yScala(c.pmf[i]);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    if (c.mostraMarker) {
      ctx.fillStyle = c.colore;
      for (let i = 0; i < c.valoriK.length; i++) {
        const x = xScala(c.valoriK[i]);
        const y = yScala(c.pmf[i]);
        ctx.beginPath();
        ctx.arc(x, y, 2.2, 0, Math.PI * 2);
        ctx.fill();
      }
    }
  }

  ctx.fillStyle = colori.testoMuto;
  ctx.font = "12px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(etichettaAsseX, (margine.sinistra + larghezza - margine.destra) / 2, altezza - 6);
}
