import { coloriTema, formattaDecimale, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const VIOLA = "#a855f7";
const V_SUONO = 340; // m/s, solo per mostrare la frequenza corrispondente a λ

window.katex.render(
  "\\begin{gathered} \\Delta d = k\\lambda \\;\\Rightarrow\\; \\text{costruttiva} \\\\[4pt] \\Delta d = (2k+1)\\dfrac{\\lambda}{2} \\;\\Rightarrow\\; \\text{distruttiva} \\\\[4pt] k = 0, 1, 2, \\dots \\end{gathered}",
  document.getElementById("formula-condizioni"),
  { throwOnError: false, displayMode: true },
);
window.katex.render(
  "\\begin{gathered} d_1 = \\dfrac{D}{2} + x \\qquad d_2 = \\dfrac{D}{2} - x \\qquad \\Delta d = |d_1 - d_2| = 2|x| \\\\[6pt] \\text{massimi: } 2|x| = k\\lambda \\;\\Rightarrow\\; x = \\pm k\\,\\dfrac{\\lambda}{2} \\\\[6pt] \\text{minimi: } 2|x| = (2k+1)\\dfrac{\\lambda}{2} \\;\\Rightarrow\\; x = \\pm(2k+1)\\,\\dfrac{\\lambda}{4} \\end{gathered}",
  document.getElementById("formula-casse"),
  { throwOnError: false, displayMode: true },
);

function fmt(v) {
  return formattaDecimale(Number(v.toFixed(2)));
}

// altoparlante disegnato come magnete + cono, rivolto nella direzione `angolo`
function disegnaCassa(ctx, x, y, angolo, colore, dim = 14) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angolo);
  ctx.fillStyle = colore;
  ctx.strokeStyle = colore;
  ctx.lineWidth = 2;
  ctx.fillRect(-dim * 1.1, -dim * 0.45, dim * 0.7, dim * 0.9);
  ctx.beginPath();
  ctx.moveTo(-dim * 0.4, -dim * 0.45);
  ctx.lineTo(dim * 0.4, -dim);
  ctx.lineTo(dim * 0.4, dim);
  ctx.lineTo(-dim * 0.4, dim * 0.45);
  ctx.closePath();
  ctx.globalAlpha = 0.35;
  ctx.fill();
  ctx.globalAlpha = 1;
  ctx.stroke();
  ctx.restore();
}

function testo(ctx, t, x, y, colore, allinea = "center", dim = 13) {
  ctx.fillStyle = colore;
  ctx.font = `${dim}px -apple-system, sans-serif`;
  ctx.textAlign = allinea;
  ctx.textBaseline = "middle";
  ctx.fillText(t, x, y);
}

// ------------------------------------------------------------------
// 1) Schema: due onde partono in fase da S1 e S2 e si incontrano in P.
//    d2 = d1 + Δd, con Δd = λ (costruttiva) oppure λ/2 (distruttiva).
// ------------------------------------------------------------------
function creaSchema() {
  const canvas = document.getElementById("canvas-schema");
  const risultati = document.getElementById("risultati-schema");
  const bCostr = document.getElementById("bottone-costruttiva");
  const bDistr = document.getElementById("bottone-distruttiva");
  const bRiavvia = document.getElementById("bottone-riavvia");

  let costruttiva = true;
  let t0 = performance.now() / 1000;

  function scegli(c) {
    costruttiva = c;
    bCostr.setAttribute("aria-pressed", String(c));
    bDistr.setAttribute("aria-pressed", String(!c));
    t0 = performance.now() / 1000;
  }
  bCostr.addEventListener("click", () => scegli(true));
  bDistr.addEventListener("click", () => scegli(false));
  bRiavvia.addEventListener("click", () => (t0 = performance.now() / 1000));

  const ANGOLO = (18 * Math.PI) / 180;
  const VEL = 70; // px/s: velocità con cui l'onda avanza sullo schermo
  const FINESTRA = 4; // s di storia nel grafico in P

  return function disegna(tempo) {
    const t = tempo - t0;
    const colori = coloriTema();
    const larga = canvas.getBoundingClientRect().width >= 600;
    canvas.style.height = larga ? "320px" : "560px";
    const { ctx, larghezza, altezza } = preparaCanvas(canvas);
    ctx.clearRect(0, 0, larghezza, altezza);

    // zona dello schema geometrico e zona dei grafici in P
    const geoL = larga ? larghezza * 0.56 : larghezza;
    const geoH = larga ? altezza : 270;
    const graf = larga
      ? { x: geoL + 24, y: 14, w: larghezza - geoL - 34, h: altezza - 28 }
      : { x: 34, y: geoH + 10, w: larghezza - 44, h: altezza - geoH - 20 };

    const lambdaPx = Math.min(85, (geoL - 90) / (4.3 * Math.cos(ANGOLO)), (geoH / 2 - 40) / (4 * Math.sin(ANGOLO)));
    const k = (2 * Math.PI) / lambdaPx;
    const omega = k * VEL;
    const A = Math.min(20, lambdaPx * 0.26);
    const d1 = 3 * lambdaPx;
    const d2 = d1 + (costruttiva ? 1 : 0.5) * lambdaPx;
    const P = { x: geoL - 40, y: geoH / 2 };

    const raggi = [
      { d: d1, dir: { x: -Math.cos(ANGOLO), y: -Math.sin(ANGOLO) }, colore: colori.serie1, nome: "S₁", dist: "d₁" },
      { d: d2, dir: { x: -Math.cos(ANGOLO), y: Math.sin(ANGOLO) }, colore: VIOLA, nome: "S₂", dist: "d₂" },
    ];

    // valore dell'onda i-esima in P all'istante τ (zero finché non è arrivata)
    const inP = (r, tau) => (VEL * tau >= r.d ? A * Math.sin(omega * tau - k * r.d) : 0);

    for (const r of raggi) {
      const S = { x: P.x + r.dir.x * r.d, y: P.y + r.dir.y * r.d };
      const u = { x: -r.dir.x, y: -r.dir.y }; // da S verso P
      const n = { x: -u.y, y: u.x };
      // raggio (cammino) tratteggiato
      ctx.strokeStyle = colori.griglia;
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(S.x, S.y);
      ctx.lineTo(P.x, P.y);
      ctx.stroke();
      ctx.setLineDash([]);
      // onda che avanza da S verso P
      const fronte = Math.min(r.d, VEL * t);
      ctx.strokeStyle = r.colore;
      ctx.lineWidth = 2.2;
      ctx.beginPath();
      for (let s = 0; s <= fronte; s += 2) {
        const h = A * Math.sin(omega * t - k * s);
        const x = S.x + u.x * s + n.x * h;
        const y = S.y + u.y * s + n.y * h;
        if (s === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
      disegnaCassa(ctx, S.x, S.y, Math.atan2(u.y, u.x), colori.testo, 12);
      testo(ctx, r.nome, S.x - 6, S.y + (r.dir.y < 0 ? -26 : 26), colori.testo, "center", 14);
      // etichetta della distanza, a metà raggio dal lato esterno
      const m = { x: (S.x + P.x) / 2 - n.x * 0, y: (S.y + P.y) / 2 };
      testo(ctx, `${r.dist} = ${fmt(r.d / lambdaPx)} λ`, m.x, m.y + (r.dir.y < 0 ? -A - 16 : A + 16), r.colore);
    }

    // punto P: il pallino si sposta della somma delle due onde
    const somma = inP(raggi[0], t) + inP(raggi[1], t);
    ctx.strokeStyle = colori.griglia;
    ctx.beginPath();
    ctx.moveTo(P.x, P.y - 2.3 * A);
    ctx.lineTo(P.x, P.y + 2.3 * A);
    ctx.stroke();
    ctx.fillStyle = colori.serie3;
    ctx.beginPath();
    ctx.arc(P.x, P.y - somma, 7, 0, Math.PI * 2);
    ctx.fill();
    testo(ctx, "P", P.x + 18, P.y, colori.testo, "left", 15);

    // grafici in P: onda 1, onda 2, somma (tempo che scorre verso sinistra)
    const strisce = [
      { titolo: "onda 1 in P", f: (tau) => inP(raggi[0], tau), colore: colori.serie1, max: A },
      { titolo: "onda 2 in P", f: (tau) => inP(raggi[1], tau), colore: VIOLA, max: A },
      { titolo: "somma in P", f: (tau) => inP(raggi[0], tau) + inP(raggi[1], tau), colore: colori.serie3, max: 2 * A },
    ];
    const hS = graf.h / 3;
    strisce.forEach((st, i) => {
      const y0 = graf.y + hS * i + hS / 2;
      const scalaY = (hS / 2 - 18) / (2 * A); // stessa scala per tutte e tre
      ctx.strokeStyle = colori.griglia;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(graf.x, y0);
      ctx.lineTo(graf.x + graf.w, y0);
      ctx.stroke();
      testo(ctx, st.titolo, graf.x, graf.y + hS * i + 6, colori.testoMuto, "left", 12);
      ctx.strokeStyle = st.colore;
      ctx.lineWidth = i === 2 ? 2.6 : 1.8;
      ctx.beginPath();
      for (let px = 0; px <= graf.w; px += 2) {
        const tau = t - FINESTRA * (1 - px / graf.w);
        const y = y0 - (tau < 0 ? 0 : st.f(tau)) * scalaY;
        if (px === 0) ctx.moveTo(graf.x + px, y);
        else ctx.lineTo(graf.x + px, y);
      }
      ctx.stroke();
    });
    testo(ctx, "adesso →", graf.x + graf.w, graf.y + graf.h + 6, colori.testoMuto, "right", 11);

    const arrivate = VEL * t >= d2;
    risultati.innerHTML = costruttiva
      ? `&Delta;d = d<sub>2</sub> &minus; d<sub>1</sub> = &lambda;: le due onde arrivano in P <strong>in fase</strong>, cresta con cresta. ` +
        (arrivate ? "L'ampiezza in P è <strong>doppia</strong>: interferenza costruttiva." : "Aspetta che arrivino entrambe…")
      : `&Delta;d = d<sub>2</sub> &minus; d<sub>1</sub> = &lambda;/2: le due onde arrivano in P <strong>in opposizione di fase</strong>, cresta con ventre. ` +
        (arrivate ? "In P si annullano: interferenza distruttiva." : "Aspetta che arrivino entrambe…");
  };
}

// ------------------------------------------------------------------
// 2) Due casse una di fronte all'altra, a ±D/2. Tra le casse si forma
//    un'onda stazionaria: massimi in x = kλ/2, minimi in x = (2k+1)λ/4.
// ------------------------------------------------------------------
function creaCasse() {
  const canvas = document.getElementById("canvas-casse");
  const risultati = document.getElementById("risultati-casse");
  const inLambda = document.getElementById("input-lambda");
  const inD = document.getElementById("input-D");
  const valLambda = document.getElementById("valore-lambda");
  const valD = document.getElementById("valore-D");
  const inMassimi = document.getElementById("input-massimi");
  const inMinimi = document.getElementById("input-minimi");
  const inOnde = document.getElementById("input-onde");

  function etichette() {
    valLambda.textContent = fmt(Number(inLambda.value));
    valD.textContent = fmt(Number(inD.value));
  }
  [inLambda, inD].forEach((el) => el.addEventListener("input", etichette));
  etichette();

  const XMAX = 5; // metri visibili a destra e a sinistra del centro
  const OMEGA = 2 * Math.PI * 0.7; // frequenza dell'animazione (rallentata)

  return function disegna(t) {
    const lambda = Number(inLambda.value);
    const D = Number(inD.value);
    const colori = coloriTema();
    const { ctx, larghezza, altezza } = preparaCanvas(canvas);
    ctx.clearRect(0, 0, larghezza, altezza);

    const cx = larghezza / 2;
    const scala = (larghezza - 40) / (2 * XMAX);
    const X = (x) => cx + x * scala;
    const y0 = altezza / 2 - 10;
    const A = Math.min(34, altezza * 0.13);
    const k = (2 * Math.PI) / lambda;
    const meta = D / 2;

    // asse x con tacche ogni metro
    ctx.strokeStyle = colori.griglia;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(X(-XMAX), y0);
    ctx.lineTo(X(XMAX), y0);
    ctx.stroke();
    for (let m = -XMAX; m <= XMAX; m++) {
      ctx.beginPath();
      ctx.moveTo(X(m), altezza - 30);
      ctx.lineTo(X(m), altezza - 24);
      ctx.stroke();
      testo(ctx, `${m}`, X(m), altezza - 14, colori.testoMuto, "center", 11);
    }
    ctx.beginPath();
    ctx.moveTo(X(-XMAX), altezza - 27);
    ctx.lineTo(X(XMAX), altezza - 27);
    ctx.stroke();
    testo(ctx, "x (m)", X(XMAX), altezza - 38, colori.testoMuto, "right", 11);

    // inviluppo e onda risultante, solo tra le casse
    const onda1 = (x) => A * Math.sin(OMEGA * t - k * (x + meta));
    const onda2 = (x) => A * Math.sin(OMEGA * t - k * (meta - x));
    const traccia = (f, colore, spessore, tratteggio = []) => {
      ctx.strokeStyle = colore;
      ctx.lineWidth = spessore;
      ctx.setLineDash(tratteggio);
      ctx.beginPath();
      const passi = Math.max(2, Math.ceil(D * scala / 2));
      for (let i = 0; i <= passi; i++) {
        const x = -meta + (D * i) / passi;
        const y = y0 - f(x);
        if (i === 0) ctx.moveTo(X(x), y);
        else ctx.lineTo(X(x), y);
      }
      ctx.stroke();
      ctx.setLineDash([]);
    };
    traccia((x) => 2 * A * Math.abs(Math.cos(k * x)), colori.griglia, 1.2, [4, 4]);
    traccia((x) => -2 * A * Math.abs(Math.cos(k * x)), colori.griglia, 1.2, [4, 4]);
    if (inOnde.checked) {
      ctx.globalAlpha = 0.7;
      traccia(onda1, colori.serie1, 1.4);
      traccia(onda2, VIOLA, 1.4);
      ctx.globalAlpha = 1;
    }
    traccia((x) => onda1(x) + onda2(x), colori.testo, 2.4);

    // punti di massimo e di minimo: pieni tra le casse, trasparenti fuori
    let nMax = 0;
    let nMin = 0;
    const dentro = (x) => Math.abs(x) <= meta + 1e-9;
    const nLim = Math.ceil(XMAX / (lambda / 4)) + 1;
    // raggio dei pallini: più piccolo se i punti sono molto fitti (schermi stretti, λ piccola)
    const rPunto = Math.max(2.5, Math.min(6.5, (lambda / 4) * scala * 0.38));
    for (let j = -nLim; j <= nLim; j++) {
      const x = (j * lambda) / 4; // multipli di λ/4: pari = massimi, dispari = minimi
      if (Math.abs(x) > XMAX) continue;
      const massimo = j % 2 === 0;
      if (dentro(x)) massimo ? nMax++ : nMin++;
      if (massimo && !inMassimi.checked) continue;
      if (!massimo && !inMinimi.checked) continue;
      ctx.globalAlpha = dentro(x) ? 1 : 0.22;
      if (massimo) {
        ctx.fillStyle = colori.serie3;
        ctx.beginPath();
        ctx.arc(X(x), y0, rPunto, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = colori.serie3;
        ctx.setLineDash([2, 3]);
        ctx.beginPath();
        ctx.moveTo(X(x), y0 - 2 * A - 6);
        ctx.lineTo(X(x), y0 + 2 * A + 6);
        ctx.stroke();
        ctx.setLineDash([]);
      } else {
        ctx.strokeStyle = colori.serie2;
        ctx.lineWidth = rPunto > 4 ? 2.5 : 1.6;
        ctx.beginPath();
        ctx.arc(X(x), y0, rPunto - 0.5, 0, Math.PI * 2);
        ctx.stroke();
      }
      ctx.globalAlpha = 1;
    }

    // casse, rivolte una verso l'altra
    disegnaCassa(ctx, X(-meta) - 14, y0, 0, colori.testo, 16);
    disegnaCassa(ctx, X(meta) + 14, y0, Math.PI, colori.testo, 16);
    testo(ctx, "S₁", X(-meta) - 18, y0 - 34, colori.testo, "center", 14);
    testo(ctx, "S₂", X(meta) + 18, y0 - 34, colori.testo, "center", 14);
    // quota D
    const yq = 18;
    ctx.strokeStyle = colori.testoMuto;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(X(-meta), yq);
    ctx.lineTo(X(meta), yq);
    ctx.moveTo(X(-meta), yq - 5);
    ctx.lineTo(X(-meta), yq + 5);
    ctx.moveTo(X(meta), yq - 5);
    ctx.lineTo(X(meta), yq + 5);
    ctx.stroke();
    ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue("--bg-alt").trim() || "transparent";
    const etichettaD = `D = ${fmt(D)} m`;
    ctx.font = "12px -apple-system, sans-serif";
    const wD = ctx.measureText(etichettaD).width + 8;
    ctx.fillRect(cx - wD / 2, yq - 8, wD, 16);
    testo(ctx, etichettaD, cx, yq, colori.testoMuto, "center", 12);

    risultati.innerHTML =
      `Tra le casse: <strong>${nMax}</strong> massimi (costruttiva) e <strong>${nMin}</strong> minimi (distruttiva). ` +
      `Distanza tra due massimi vicini: &lambda;/2 = ${fmt(lambda / 2)} m. ` +
      `Con il suono (v &asymp; ${V_SUONO} m/s) questa &lambda; corrisponde a f &asymp; ${Math.round(V_SUONO / lambda)} Hz.`;
  };
}

const schema = creaSchema();
const casse = creaCasse();

function tick(ms) {
  const t = ms / 1000;
  schema(t);
  casse(t);
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
