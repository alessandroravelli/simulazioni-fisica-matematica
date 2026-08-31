import {
  applicaFiltro,
  campoDaStato,
  faseOnda,
  ondaLineare,
} from "../../../assets/js/lib/fisica.js";
import { coloriTema, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const formFiltri = document.getElementById("form-filtri");
const formFiltro2 = document.getElementById("form-filtro2");
const inputNumero = document.getElementById("input-numero");
const inputTipo1 = document.getElementById("input-tipo1");
const inputAngolo1 = document.getElementById("input-angolo1");
const campoAngolo1 = document.getElementById("campo-angolo1");
const inputTipo2 = document.getElementById("input-tipo2");
const inputAngolo2 = document.getElementById("input-angolo2");
const campoAngolo2 = document.getElementById("campo-angolo2");
const risultati = document.getElementById("risultati");

const canvasConcetto = document.getElementById("canvas-concetto");
const canvasOnda = document.getElementById("canvas-onda");

window.katex.render("E_R = \\dfrac{E_{R,i}}{2}", document.getElementById("formula-dimezza"), { throwOnError: false });
window.katex.render("E_R = E_{R,i} \\cos^2\\theta", document.getElementById("formula-malus"), { throwOnError: false });

function aggiornaVisibilita() {
  const dueFiltri = inputNumero.value === "2";
  formFiltro2.style.display = dueFiltri ? "flex" : "none";
  campoAngolo1.style.display = inputTipo1.value === "lineare" ? "flex" : "none";
  campoAngolo2.style.display = inputTipo2.value === "lineare" ? "flex" : "none";
}
inputNumero.addEventListener("change", aggiornaVisibilita);
inputTipo1.addEventListener("change", aggiornaVisibilita);
inputTipo2.addEventListener("change", aggiornaVisibilita);
aggiornaVisibilita();
formFiltri.addEventListener("submit", (e) => e.preventDefault());
formFiltro2.addEventListener("submit", (e) => e.preventDefault());

// --- costanti dell'onda e proiezione prospettica ---
const LAMBDA_PX = 100;
const K = (2 * Math.PI) / LAMBDA_PX;
const W = 3.0; // rad/s
const AMPIEZZA_PX = 42;
const DEPTH_X = 0.82;
const DEPTH_Y = -0.44;

function fmt(v) {
  return Number(v.toFixed(3)).toString();
}

function proietta(ey, exPrime) {
  return { dx: exPrime * DEPTH_X, dy: -ey + exPrime * DEPTH_Y };
}

function disegnaAssePropagazione(ctx, colori, xIni, xFin, yBase, altezza) {
  ctx.strokeStyle = colori.griglia;
  ctx.lineWidth = 1;
  ctx.setLineDash([5, 5]);
  ctx.beginPath();
  ctx.moveTo(xIni, yBase);
  ctx.lineTo(xFin, yBase);
  ctx.stroke();
  ctx.setLineDash([]);

  ctx.strokeStyle = colori.testoMuto;
  ctx.fillStyle = colori.testoMuto;
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(xIni, altezza - 14);
  ctx.lineTo(xFin, altezza - 14);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(xFin, altezza - 14);
  ctx.lineTo(xFin - 8, altezza - 19);
  ctx.lineTo(xFin - 8, altezza - 9);
  ctx.closePath();
  ctx.fill();
  ctx.font = "11px -apple-system, sans-serif";
  ctx.textAlign = "left";
  ctx.fillText("propagazione", xIni, altezza - 20);
}

function disegnaComponenteOnda(ctx, campoFn, colore, xIni, xFin, yBase) {
  ctx.strokeStyle = colore;
  ctx.lineWidth = 2;
  const passo = 4;
  const punti = [];
  for (let x = xIni; x <= xFin; x += passo) {
    const { ey, exPrime } = campoFn(x);
    const proj = proietta(ey, exPrime);
    punti.push({ x0: x, px: x + proj.dx * AMPIEZZA_PX, py: yBase + proj.dy * AMPIEZZA_PX });
  }
  ctx.globalAlpha = 0.3;
  for (let i = 0; i < punti.length; i += 6) {
    const p = punti[i];
    ctx.beginPath();
    ctx.moveTo(p.x0, yBase);
    ctx.lineTo(p.px, p.py);
    ctx.stroke();
  }
  ctx.globalAlpha = 1;
  ctx.beginPath();
  punti.forEach((p, i) => { if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py); });
  ctx.stroke();
}

// --- pannello concetto: onda lineare semplice, con E e B ---
function disegnaOndaConcetto(t) {
  const colori = coloriTema();
  const { ctx, larghezza, altezza } = preparaCanvas(canvasConcetto);
  ctx.clearRect(0, 0, larghezza, altezza);
  const yBase = altezza / 2;
  const margine = 26;
  const xIni = margine, xFin = larghezza - margine;

  disegnaAssePropagazione(ctx, colori, xIni, xFin, yBase, altezza);
  disegnaComponenteOnda(ctx, (x) => {
    const c = ondaLineare(faseOnda(x, t, K, W), 0);
    return { ey: 0, exPrime: c.ey };
  }, "#2563eb", xIni, xFin, yBase);
  disegnaComponenteOnda(ctx, (x) => ondaLineare(faseOnda(x, t, K, W), 0), "#dc2626", xIni, xFin, yBase);
}

// --- oggetto polarizzatore disegnato nel punto di transizione ---
function disegnaFiltro(ctx, colori, x, yBase, filtro, etichetta) {
  const raggioX = 11;
  const raggioY = AMPIEZZA_PX * 1.2;

  ctx.fillStyle = colori.bgAlt2 ?? colori.griglia;
  ctx.globalAlpha = 0.35;
  ctx.beginPath();
  ctx.ellipse(x, yBase, raggioX, raggioY, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.globalAlpha = 1;
  ctx.strokeStyle = colori.testo;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.ellipse(x, yBase, raggioX, raggioY, 0, 0, Math.PI * 2);
  ctx.stroke();

  if (filtro.tipo === "lineare") {
    const dir = proietta(Math.cos(filtro.angolo), Math.sin(filtro.angolo));
    const norma = Math.hypot(dir.dx, dir.dy) || 1;
    const lung = raggioY * 0.95;
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(x - (dir.dx / norma) * lung, yBase - (dir.dy / norma) * lung);
    ctx.lineTo(x + (dir.dx / norma) * lung, yBase + (dir.dy / norma) * lung);
    ctx.stroke();
  } else {
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(x, yBase, raggioX * 0.55, raggioY * 0.55, 0, 0.3, Math.PI * 1.9);
    ctx.stroke();
  }

  ctx.fillStyle = colori.testoMuto;
  ctx.font = "11px -apple-system, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(etichetta, x, yBase - raggioY - 10);
}

// --- animazione principale: più zone (stati di polarizzazione diversi)
// separate da uno o due oggetti polarizzatore ---
function disegnaOndaConFiltri(t, { zone, filtri }) {
  const colori = coloriTema();
  const { ctx, larghezza, altezza } = preparaCanvas(canvasOnda);
  ctx.clearRect(0, 0, larghezza, altezza);
  const yBase = altezza / 2;
  const margine = 26;
  const xIni = margine, xFin = larghezza - margine;

  disegnaAssePropagazione(ctx, colori, xIni, xFin, yBase, altezza);

  zone.forEach((z) => {
    ctx.save();
    ctx.beginPath();
    ctx.rect(z.xDa, 0, z.xA - z.xDa, altezza);
    ctx.clip();
    disegnaComponenteOnda(ctx, z.campoE, "#dc2626", xIni, xFin, yBase);
    ctx.restore();
  });

  filtri.forEach((f) => disegnaFiltro(ctx, colori, f.x, yBase, f.filtro, f.etichetta));
}

function tick(tempoMs) {
  const t = tempoMs / 1000;

  disegnaOndaConcetto(t);

  // --- stati di polarizzazione, calcolati una volta per frame ---
  const numeroFiltri = Number(inputNumero.value);
  const filtro1 = {
    tipo: inputTipo1.value,
    angolo: (Number(inputAngolo1.value) * Math.PI) / 180,
  };
  const statoSorgente = { tipo: "nonpolarizzata", angolo: 0, irradianza: 1 };
  const stato1 = applicaFiltro(statoSorgente, filtro1);

  let filtro2 = null, stato2 = null;
  if (numeroFiltri === 2) {
    filtro2 = {
      tipo: inputTipo2.value,
      angolo: filtro1.angolo + (Number(inputAngolo2.value) * Math.PI) / 180,
    };
    stato2 = applicaFiltro(stato1, filtro2);
  }

  // --- geometria delle zone lungo il canvas principale ---
  const rectOnda = canvasOnda.getBoundingClientRect();
  const margine = 26;
  const xIni = margine, xFin = rectOnda.width - margine;
  const xFiltro1 = numeroFiltri === 2 ? xIni + (xFin - xIni) * 0.34 : xIni + (xFin - xIni) * 0.42;
  const xFiltro2 = xIni + (xFin - xIni) * 0.7;

  const scala1 = Math.sqrt(stato1.irradianza);
  const scala2 = stato2 ? Math.sqrt(stato2.irradianza) : 1;

  const zone = [
    { xDa: xIni - 100, xA: xFiltro1, campoE: (x) => campoDaStato(statoSorgente, x, t, faseOnda(x, t, K, W)) },
  ];

  if (numeroFiltri === 1) {
    zone.push({
      xDa: xFiltro1, xA: xFin + 100,
      campoE: (x) => {
        const c = campoDaStato(stato1, x, t, faseOnda(x, t, K, W));
        return { ey: c.ey * scala1, exPrime: c.exPrime * scala1 };
      },
    });
  } else {
    zone.push({
      xDa: xFiltro1, xA: xFiltro2,
      campoE: (x) => {
        const c = campoDaStato(stato1, x, t, faseOnda(x, t, K, W));
        return { ey: c.ey * scala1, exPrime: c.exPrime * scala1 };
      },
    });
    zone.push({
      xDa: xFiltro2, xA: xFin + 100,
      campoE: (x) => {
        const c = campoDaStato(stato2, x, t, faseOnda(x, t, K, W));
        return { ey: c.ey * scala2, exPrime: c.exPrime * scala2 };
      },
    });
  }

  const filtri = [{ x: xFiltro1, filtro: filtro1, etichetta: "Filtro 1" }];
  if (numeroFiltri === 2) filtri.push({ x: xFiltro2, filtro: filtro2, etichetta: "Filtro 2" });

  disegnaOndaConFiltri(t, { zone, filtri });

  const nomeStato = (s) => (
    s.tipo === "lineare" ? `lineare ${Math.round((s.angolo * 180) / Math.PI)}&deg;`
    : s.tipo === "circolare" ? "circolare"
    : "non polarizzata"
  );

  let html =
    `<strong>E<sub>R</sub></strong> sorgente = ${fmt(statoSorgente.irradianza)} (${nomeStato(statoSorgente)}) &nbsp; ` +
    `<strong>E<sub>R</sub></strong> dopo filtro 1 = ${fmt(stato1.irradianza)} (${nomeStato(stato1)})`;
  if (stato2) {
    html += ` &nbsp; <strong>E<sub>R</sub></strong> dopo filtro 2 = ${fmt(stato2.irradianza)} (${nomeStato(stato2)})`;
  }
  risultati.innerHTML = html;

  requestAnimationFrame(tick);
}

requestAnimationFrame(tick);
