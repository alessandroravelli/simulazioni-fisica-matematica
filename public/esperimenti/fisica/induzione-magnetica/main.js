import { campoAssialeDipolo, flussoSpira, tracciaLineaCampo } from "../../../assets/js/lib/fisica.js";
import { coloriTema, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const form = document.getElementById("form-parametri");
const risultati = document.getElementById("risultati");
const canvas = document.getElementById("canvas-grafico");
const checkLineeMagnete = document.getElementById("check-linee-magnete");
const checkLineeSpira = document.getElementById("check-linee-spira");

window.katex.render(
  "\\varepsilon = -\\dfrac{d\\Phi}{dt}",
  document.getElementById("formula"),
  { throwOnError: false },
);

// --- stato ---
let magnetX = -2.4; // unità fisiche: lungo l'asse della spira (0 = centro spira)
let magnetY = 0; // unità fisiche: scostamento perpendicolare all'asse
let trascinando = false;
let offsetTrascinamento = { x: 0, y: 0 };

let flussoPrecedente = null;
let tempoPrecedente = null;
let correnteVisualizzata = 0;
let faseCorrente = 0;

function parametri() {
  return {
    K: Number(form.intensita.value),
    raggio: Number(form.raggio.value),
    R: Math.max(0.05, Number(form.resistenza.value)),
  };
}

const COLORE_N = "#dc2626";
const COLORE_S = "#2563eb";
const COLORE_CORRENTE = "#f59e0b";

// --- scala fisica <-> pixel ---
let scala = 60; // px per unità fisica, ricalcolata a ogni frame in base al canvas
let centroPx = { x: 0, y: 0 };
let dimensioniCanvas = { larghezza: 0, altezza: 0 };

function fisicaAPixel(x, y) {
  return { x: centroPx.x + x * scala, y: centroPx.y + y * scala };
}

function pixelAFisica(x, y) {
  return { x: (x - centroPx.x) / scala, y: (y - centroPx.y) / scala };
}

// --- interazione mouse/touch ---
function posizioneEvento(evento) {
  const rect = canvas.getBoundingClientRect();
  return { x: evento.clientX - rect.left, y: evento.clientY - rect.top };
}

canvas.addEventListener("pointerdown", (evento) => {
  const pos = posizioneEvento(evento);
  const magnetPx = fisicaAPixel(magnetX, magnetY);
  const distanza = Math.hypot(pos.x - magnetPx.x, pos.y - magnetPx.y);
  if (distanza < scala * 1.1) {
    trascinando = true;
    offsetTrascinamento = { x: magnetPx.x - pos.x, y: magnetPx.y - pos.y };
    canvas.classList.add("trascinamento");
    try { canvas.setPointerCapture(evento.pointerId); } catch { /* alcuni browser/dispositivi non supportano la cattura per questo pointer */ }
  }
});

canvas.addEventListener("pointermove", (evento) => {
  if (!trascinando) return;
  const pos = posizioneEvento(evento);
  const fisica = pixelAFisica(pos.x + offsetTrascinamento.x, pos.y + offsetTrascinamento.y);
  const margine = 0.3;
  const minX = -(centroPx.x / scala) + margine;
  const maxX = (dimensioniCanvas.larghezza - centroPx.x) / scala - margine;
  const minY = -(centroPx.y / scala) + margine;
  const maxY = (dimensioniCanvas.altezza - centroPx.y) / scala - margine;
  magnetX = Math.max(minX, Math.min(maxX, fisica.x));
  magnetY = Math.max(minY, Math.min(maxY, fisica.y));
});

function fineTrascinamento() {
  trascinando = false;
  canvas.classList.remove("trascinamento");
}
canvas.addEventListener("pointerup", fineTrascinamento);
canvas.addEventListener("pointercancel", fineTrascinamento);

// --- disegno ---
function disegnaFreccia(ctx, x1, y1, x2, y2, colore, larghezzaLinea = 2) {
  ctx.strokeStyle = colore;
  ctx.fillStyle = colore;
  ctx.lineWidth = larghezzaLinea;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  const angolo = Math.atan2(y2 - y1, x2 - x1);
  const dimPunta = 7;
  ctx.beginPath();
  ctx.moveTo(x2, y2);
  ctx.lineTo(x2 - dimPunta * Math.cos(angolo - 0.4), y2 - dimPunta * Math.sin(angolo - 0.4));
  ctx.lineTo(x2 - dimPunta * Math.cos(angolo + 0.4), y2 - dimPunta * Math.sin(angolo + 0.4));
  ctx.closePath();
  ctx.fill();
}

function disegnaScena(larghezza, altezza, ctx, corrente) {
  const colori = coloriTema();
  ctx.clearRect(0, 0, larghezza, altezza);

  centroPx = { x: larghezza * 0.62, y: altezza / 2 };
  scala = Math.min(larghezza / 7, altezza / 5.5);
  dimensioniCanvas = { larghezza, altezza };

  // asse (linea tratteggiata)
  ctx.strokeStyle = colori.griglia;
  ctx.lineWidth = 1;
  ctx.setLineDash([5, 5]);
  ctx.beginPath();
  ctx.moveTo(8, centroPx.y);
  ctx.lineTo(larghezza - 8, centroPx.y);
  ctx.stroke();
  ctx.setLineDash([]);

  // --- spira, vista di taglio: ellisse verticale ---
  const rx = Math.max(10, 14);
  const ry = Math.max(18, scala * Number(form.raggio.value));
  ctx.strokeStyle = colori.testo;
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.ellipse(centroPx.x, centroPx.y, rx, ry, 0, 0, Math.PI * 2);
  ctx.stroke();

  // corrente indotta: pallini animati lungo l'ellisse
  const nPallini = 14;
  const intensitaVisiva = Math.min(1, Math.abs(corrente) / 1.5);
  if (intensitaVisiva > 0.02) {
    const raggioPallino = 3 + 2.5 * intensitaVisiva;
    for (let k = 0; k < nPallini; k++) {
      const phi = faseCorrente + (k * Math.PI * 2) / nPallini;
      const px = centroPx.x + rx * Math.cos(phi);
      const py = centroPx.y + ry * Math.sin(phi);
      ctx.globalAlpha = 0.45 + 0.55 * intensitaVisiva;
      ctx.fillStyle = COLORE_CORRENTE;
      ctx.beginPath();
      ctx.arc(px, py, raggioPallino, 0, Math.PI * 2);
      ctx.fill();
      ctx.globalAlpha = 1;
    }
  }

  // campo indotto dalla spira: freccia orizzontale al centro
  if (intensitaVisiva > 0.02) {
    const verso = corrente >= 0 ? 1 : -1;
    const lunghezza = 26 + 34 * intensitaVisiva;
    ctx.globalAlpha = 0.5 + 0.5 * intensitaVisiva;
    disegnaFreccia(
      ctx, centroPx.x - (verso * lunghezza) / 2, centroPx.y,
      centroPx.x + (verso * lunghezza) / 2, centroPx.y,
      colori.serie3, 3,
    );
    ctx.globalAlpha = 1;
  }

  // --- linee di campo del magnete: molto estese, per vedere quanto
  // entrano nella spira. Disegnate in coordinate del magnete, orientate
  // lungo +x (verso N), poi traslate nella posizione del magnete. ---
  const magnetPx = fisicaAPixel(magnetX, magnetY);
  const lunghezzaMagnete = scala * 0.95;
  const spessoreMagnete = scala * 0.34;

  function disegnaFamigliaLineeCampo(centro, dimensioni, verso, colore) {
    ctx.strokeStyle = colore;
    ctx.lineWidth = 1.4;
    dimensioni.forEach((dim, i) => {
      if (dim <= 0) return;
      const opacita = Math.max(0.12, 0.6 - i * 0.11);
      ctx.globalAlpha = opacita;
      const superiore = tracciaLineaCampo(dim * scala);
      ctx.beginPath();
      superiore.forEach((p, j) => {
        const x = centro.x + verso * p.x, y = centro.y + p.y;
        if (j === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      });
      ctx.stroke();
      ctx.beginPath();
      superiore.forEach((p, j) => {
        const x = centro.x + verso * p.x, y = centro.y - p.y;
        if (j === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      });
      ctx.stroke();
    });
    ctx.globalAlpha = 1;
  }

  if (checkLineeMagnete.checked) {
    disegnaFamigliaLineeCampo(magnetPx, [0.5, 1.0, 1.7, 2.6, 3.7, 5.0], 1, colori.testoMuto);
  }

  // --- linee di campo indotte dalla spira: stesso tipo di curva, centrate
  // sulla spira, orientate secondo il verso della corrente indotta (si
  // oppongono a quelle del magnete quando il flusso aumenta) ---
  if (checkLineeSpira.checked && intensitaVisiva > 0.03) {
    const versoIndotto = corrente >= 0 ? 1 : -1;
    const dimensioniIndotte = [0.4, 0.85, 1.4].map((d) => d * intensitaVisiva);
    disegnaFamigliaLineeCampo(centroPx, dimensioniIndotte, versoIndotto, colori.serie3);
  }

  // --- magnete: barra N/S (N verso +x, S verso -x — fisso) ---
  const mezzaLung = lunghezzaMagnete / 2;
  const mezzoSpess = spessoreMagnete / 2;
  ctx.fillStyle = COLORE_S;
  ctx.fillRect(magnetPx.x - mezzaLung, magnetPx.y - mezzoSpess, mezzaLung, spessoreMagnete);
  ctx.fillStyle = COLORE_N;
  ctx.fillRect(magnetPx.x, magnetPx.y - mezzoSpess, mezzaLung, spessoreMagnete);
  ctx.strokeStyle = colori.testo;
  ctx.lineWidth = 1.5;
  ctx.strokeRect(magnetPx.x - mezzaLung, magnetPx.y - mezzoSpess, lunghezzaMagnete, spessoreMagnete);

  ctx.fillStyle = "#fff";
  ctx.font = "700 13px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText("N", magnetPx.x + mezzaLung / 2, magnetPx.y);
  ctx.fillText("S", magnetPx.x - mezzaLung / 2, magnetPx.y);
  ctx.textBaseline = "alphabetic";
}

// --- ciclo di animazione ---
function fmt(v) {
  return Number(v.toFixed(3)).toString();
}

function tick(tempo) {
  const { K, raggio, R } = parametri();
  const area = Math.PI * raggio * raggio;
  const flusso = flussoSpira(K, area, magnetX, magnetY);

  let derivataFlusso = 0;
  if (flussoPrecedente !== null && tempoPrecedente !== null) {
    const dt = Math.max(0.001, (tempo - tempoPrecedente) / 1000);
    derivataFlusso = (flusso - flussoPrecedente) / dt;
  }
  flussoPrecedente = flusso;
  tempoPrecedente = tempo;

  const fem = -derivataFlusso;
  const correnteIstantanea = fem / R;
  correnteVisualizzata += (correnteIstantanea - correnteVisualizzata) * 0.25;

  const dtSec = 1 / 60;
  faseCorrente += correnteVisualizzata * 0.6 * dtSec;

  const { ctx, larghezza, altezza } = preparaCanvas(canvas);
  disegnaScena(larghezza, altezza, ctx, correnteVisualizzata);

  const direzione = Math.abs(correnteVisualizzata) < 0.01
    ? "&mdash;"
    : (correnteVisualizzata >= 0 ? "antioraria" : "oraria");

  risultati.innerHTML =
    `<strong>&Phi;</strong> = ${fmt(flusso)} &nbsp; ` +
    `<strong>f.e.m. indotta</strong> = ${fmt(fem)} &nbsp; ` +
    `<strong>Corrente indotta</strong> = ${fmt(correnteVisualizzata)} (${direzione})`;

  requestAnimationFrame(tick);
}

form.addEventListener("submit", (e) => e.preventDefault());
requestAnimationFrame(tick);
