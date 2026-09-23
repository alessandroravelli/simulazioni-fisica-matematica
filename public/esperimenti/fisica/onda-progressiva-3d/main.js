import { ondaProgressiva } from "../../../assets/js/lib/fisica.js";
import { coloriTema, disegnaLinee, preparaCanvas, proiettaIsometrica } from "../../../assets/js/lib/grafici.js";

// --- parametri fissi dell'onda progressiva: periodo T = 5 s, velocità di
// propagazione v = 4 unità/s, quindi lunghezza d'onda lambda = v*T = 20.
// Il dominio mostrato è largo 2 lambda in x e 2 periodi in t.
const OMEGA = (2 * Math.PI) / 5;
const V = 4;
const PHI0 = 0;
const LAMBDA = V * ((2 * Math.PI) / OMEGA);
const LX = 2 * LAMBDA;
const TMAX = 2 * ((2 * Math.PI) / OMEGA);

window.katex.render(
  "y(x,t) = \\sin\\!\\left(\\omega\\left(t - \\dfrac{x}{v}\\right) + \\varphi_0\\right)",
  document.getElementById("formula-onda"),
  { throwOnError: false },
);

function fmt(v) {
  return Number(v.toFixed(2)).toString();
}

// --- superficie 3D (pseudo-3D isometrica) di y(x,t), con le due curve
// "solo nel tempo" (x fisso) e "solo nello spazio" (t fisso) evidenziate,
// e un pallino che rappresenta l'osservatore nel loro punto di incontro.
function creaSuperficie3D() {
  const canvas = document.getElementById("canvas-3d");
  const SCALA_X = 4;
  const SCALA_T = 16;
  const SCALA_Y = 55;

  function disegnaCurvaSpaziale(ctx, proietta, t, colore, spessore) {
    ctx.strokeStyle = colore;
    ctx.lineWidth = spessore;
    ctx.beginPath();
    const N = 70;
    for (let i = 0; i <= N; i++) {
      const x = (LX * i) / N;
      const p = proietta(x, t, ondaProgressiva(x, t, OMEGA, V, PHI0));
      if (i === 0) ctx.moveTo(p.x, p.y);
      else ctx.lineTo(p.x, p.y);
    }
    ctx.stroke();
  }

  function disegnaCurvaTemporale(ctx, proietta, x, colore, spessore) {
    ctx.strokeStyle = colore;
    ctx.lineWidth = spessore;
    ctx.beginPath();
    const N = 70;
    for (let i = 0; i <= N; i++) {
      const t = (TMAX * i) / N;
      const p = proietta(x, t, ondaProgressiva(x, t, OMEGA, V, PHI0));
      if (i === 0) ctx.moveTo(p.x, p.y);
      else ctx.lineTo(p.x, p.y);
    }
    ctx.stroke();
  }

  return function disegna(xOss, tOss) {
    const colori = coloriTema();
    const { ctx, larghezza, altezza } = preparaCanvas(canvas);
    ctx.clearRect(0, 0, larghezza, altezza);

    const originX = larghezza / 2;
    const originY = altezza * 0.28;
    const proietta = (x, t, y) => {
      const p = proiettaIsometrica(x * SCALA_X, t * SCALA_T, y * SCALA_Y);
      return { x: originX + p.dx, y: originY + p.dy };
    };

    // pavimento: il rettangolo x in [0,LX], t in [0,TMAX], y = 0
    ctx.strokeStyle = colori.griglia;
    ctx.lineWidth = 1;
    const angoli = [
      [0, 0], [LX, 0], [LX, TMAX], [0, TMAX],
    ].map(([x, t]) => proietta(x, t, 0));
    ctx.beginPath();
    angoli.forEach((p, i) => (i === 0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y)));
    ctx.closePath();
    ctx.stroke();

    // curve di sfondo (la "griglia" della superficie), poi le due
    // evidenziate sopra
    const N_SFONDO = 6;
    for (let i = 1; i < N_SFONDO; i++) disegnaCurvaSpaziale(ctx, proietta, (TMAX * i) / N_SFONDO, colori.griglia, 1);
    for (let i = 1; i < N_SFONDO; i++) disegnaCurvaTemporale(ctx, proietta, (LX * i) / N_SFONDO, colori.griglia, 1);

    disegnaCurvaSpaziale(ctx, proietta, tOss, colori.serie3, 2.5);
    disegnaCurvaTemporale(ctx, proietta, xOss, colori.serie2, 2.5);

    // etichette degli assi
    ctx.fillStyle = colori.testoMuto;
    ctx.font = "12px -apple-system, sans-serif";
    const pX = proietta(LX, 0, 0);
    const pT = proietta(0, TMAX, 0);
    ctx.textAlign = "left";
    ctx.fillText("x", pX.x + 6, pX.y + 4);
    ctx.textAlign = "right";
    ctx.fillText("t", pT.x - 6, pT.y + 4);

    // il pallino: noi, nel punto (xOss, tOss)
    const yOss = ondaProgressiva(xOss, tOss, OMEGA, V, PHI0);
    const pMarcatore = proietta(xOss, tOss, yOss);
    const pPiede = proietta(xOss, tOss, 0);
    ctx.strokeStyle = `${colori.serie1}77`;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(pPiede.x, pPiede.y);
    ctx.lineTo(pMarcatore.x, pMarcatore.y);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = colori.serie1;
    ctx.beginPath();
    ctx.arc(pMarcatore.x, pMarcatore.y, 7, 0, Math.PI * 2);
    ctx.fill();

    return yOss;
  };
}

// --- pagina: sliders + i due grafici 2D coerenti con la superficie ---
const inputXOss = document.getElementById("input-x-oss");
const valoreXOss = document.getElementById("valore-x-oss");
const inputTOss = document.getElementById("input-t-oss");
const valoreTOss = document.getElementById("valore-t-oss");
const titoloXFisso = document.getElementById("titolo-x-fisso");
const titoloTFisso = document.getElementById("titolo-t-fisso");
const risultati = document.getElementById("risultati-3d");
const canvasTempo = document.getElementById("canvas-tempo");
const canvasSpazio = document.getElementById("canvas-spazio");

inputXOss.max = LX;
inputTOss.max = TMAX;

const disegnaSuperficie = creaSuperficie3D();

function aggiorna() {
  const xOss = Number(inputXOss.value);
  const tOss = Number(inputTOss.value);
  valoreXOss.textContent = fmt(xOss);
  valoreTOss.textContent = fmt(tOss);
  titoloXFisso.textContent = fmt(xOss);
  titoloTFisso.textContent = fmt(tOss);

  const colori = coloriTema();
  const yOss = disegnaSuperficie(xOss, tOss);

  // grafico "solo nel tempo": y(t) a x = xOss fisso, coerente con la
  // curva serie2 evidenziata sulla superficie
  const graficoTempo = preparaCanvas(canvasTempo);
  disegnaLinee(graficoTempo.ctx, graficoTempo.larghezza, graficoTempo.altezza, {
    xMin: 0,
    xMax: TMAX,
    yMin: -1.2,
    yMax: 1.2,
    curve: [{ valuta: (t) => ondaProgressiva(xOss, t, OMEGA, V, PHI0), colore: colori.serie2 }],
    marcatori: [{ x: tOss, y: yOss, colore: colori.serie1 }],
    etichettaAsseX: "t (s)",
  });

  // grafico "solo nello spazio": y(x) a t = tOss fisso, coerente con la
  // curva serie3 evidenziata sulla superficie
  const graficoSpazio = preparaCanvas(canvasSpazio);
  disegnaLinee(graficoSpazio.ctx, graficoSpazio.larghezza, graficoSpazio.altezza, {
    xMin: 0,
    xMax: LX,
    yMin: -1.2,
    yMax: 1.2,
    curve: [{ valuta: (x) => ondaProgressiva(x, tOss, OMEGA, V, PHI0), colore: colori.serie3 }],
    marcatori: [{ x: xOss, y: yOss, colore: colori.serie1 }],
    etichettaAsseX: "x",
  });

  risultati.innerHTML = `Quello che vediamo, in x = ${fmt(xOss)} e t = ${fmt(tOss)} s: <strong>y = ${fmt(yOss)}</strong>`;
}

inputXOss.addEventListener("input", aggiorna);
inputTOss.addEventListener("input", aggiorna);
window.addEventListener("resize", aggiorna);
aggiorna();

// --- onda sferica: superficie ondulata su un piano (x,y), animata nel
// tempo, con l'ampiezza che si attenua allontanandosi dalla sorgente
// (al centro). Nessuno slider: serve solo a mostrare il caso con più
// coordinate spaziali.
function creaOndaSferica() {
  const canvas = document.getElementById("canvas-sferica");
  const OMEGA_S = (2 * Math.PI) / 3;
  const V_S = 6;
  const R_MAX = 18;
  const SCALA = 11;
  const SCALA_Y = 40;

  function ampiezza(r) {
    return 1 / (1 + r * 0.12);
  }
  function quota(x, y, t) {
    const r = Math.hypot(x, y);
    return ampiezza(r) * Math.sin(OMEGA_S * (t - r / V_S));
  }

  return function disegna(t) {
    const colori = coloriTema();
    const { ctx, larghezza, altezza } = preparaCanvas(canvas);
    ctx.clearRect(0, 0, larghezza, altezza);

    const originX = larghezza / 2;
    const originY = altezza * 0.4;
    const proietta = (x, y, h) => {
      const p = proiettaIsometrica(x * SCALA, y * SCALA, h * SCALA_Y);
      return { x: originX + p.dx, y: originY + p.dy };
    };

    // anelli concentrici (r fisso, theta variabile)
    const N_ANELLI = 9;
    const N_THETA = 72;
    for (let a = 1; a <= N_ANELLI; a++) {
      const r = (R_MAX * a) / N_ANELLI;
      ctx.strokeStyle = colori.serie1;
      ctx.globalAlpha = 0.15 + 0.6 * ampiezza(r);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let i = 0; i <= N_THETA; i++) {
        const theta = (2 * Math.PI * i) / N_THETA;
        const x = r * Math.cos(theta);
        const y = r * Math.sin(theta);
        const p = proietta(x, y, quota(x, y, t));
        if (i === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
      }
      ctx.stroke();
    }
    ctx.globalAlpha = 1;

    // raggi radiali (theta fisso, r variabile), come griglia della
    // superficie
    const N_RAGGI = 12;
    const N_R = 40;
    ctx.strokeStyle = colori.griglia;
    ctx.lineWidth = 1;
    for (let s = 0; s < N_RAGGI; s++) {
      const theta = (2 * Math.PI * s) / N_RAGGI;
      ctx.beginPath();
      for (let i = 0; i <= N_R; i++) {
        const r = (R_MAX * i) / N_R;
        const x = r * Math.cos(theta);
        const y = r * Math.sin(theta);
        const p = proietta(x, y, quota(x, y, t));
        if (i === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
      }
      ctx.stroke();
    }

    // la sorgente, al centro
    const pCentro = proietta(0, 0, quota(0, 0, t));
    ctx.fillStyle = colori.serie2;
    ctx.beginPath();
    ctx.arc(pCentro.x, pCentro.y, 5, 0, Math.PI * 2);
    ctx.fill();
  };
}

const disegnaSferica = creaOndaSferica();
function tickSferica(tempoMs) {
  disegnaSferica(tempoMs / 1000);
  requestAnimationFrame(tickSferica);
}
requestAnimationFrame(tickSferica);
