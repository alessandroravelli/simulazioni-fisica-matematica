import {
  angoloNonPolarizzato,
  faseOnda,
  ondaCircolare,
  ondaLineare,
} from "../../../assets/js/lib/fisica.js";
import { coloriTema, preparaCanvas } from "../../../assets/js/lib/grafici.js";

const formFiltro = document.getElementById("form-filtro");
const inputTipo = document.getElementById("input-tipo");
const inputAngolo = document.getElementById("input-angolo");
const campoAngolo = document.getElementById("campo-angolo");
const risultati = document.getElementById("risultati");

const canvasConcetto = document.getElementById("canvas-concetto");
const canvasSorgente = document.getElementById("canvas-sorgente");
const canvasRiferimento = document.getElementById("canvas-riferimento");
const canvasSecondo = document.getElementById("canvas-secondo");

window.katex.render("I = \\dfrac{I_0}{2}", document.getElementById("formula-dimezza"), { throwOnError: false });
window.katex.render("I = I_0 \\cos^2\\theta", document.getElementById("formula-malus"), { throwOnError: false });

function aggiornaVisibilitaAngolo() {
  campoAngolo.style.display = inputTipo.value === "lineare" ? "flex" : "none";
}
inputTipo.addEventListener("change", aggiornaVisibilitaAngolo);
aggiornaVisibilitaAngolo();
formFiltro.addEventListener("submit", (e) => e.preventDefault());

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

function disegnaOnda(canvas, { campoE, campoB }) {
  const colori = coloriTema();
  const { ctx, larghezza, altezza } = preparaCanvas(canvas);
  ctx.clearRect(0, 0, larghezza, altezza);

  const yBase = altezza / 2;
  const margine = 26;
  const xIni = margine, xFin = larghezza - margine;

  ctx.strokeStyle = colori.griglia;
  ctx.lineWidth = 1;
  ctx.setLineDash([5, 5]);
  ctx.beginPath();
  ctx.moveTo(xIni, yBase);
  ctx.lineTo(xFin, yBase);
  ctx.stroke();
  ctx.setLineDash([]);

  function disegnaComponente(campoFn, colore) {
    if (!campoFn) return;
    ctx.strokeStyle = colore;
    ctx.lineWidth = 2;
    const passo = 4;
    const punti = [];
    for (let x = xIni; x <= xFin; x += passo) {
      const { ey, exPrime } = campoFn(x);
      const px = x + exPrime * AMPIEZZA_PX * DEPTH_X;
      const py = yBase - ey * AMPIEZZA_PX + exPrime * AMPIEZZA_PX * DEPTH_Y;
      punti.push({ x0: x, px, py });
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
    punti.forEach((p, i) => {
      if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
    });
    ctx.stroke();
  }

  disegnaComponente(campoB, "#2563eb");
  disegnaComponente(campoE, "#dc2626");

  // freccia direzione di propagazione
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

function tick(tempoMs) {
  const t = tempoMs / 1000;

  // 1) pannello concetto: onda polarizzata lineare, E e B
  disegnaOnda(canvasConcetto, {
    campoE: (x) => ondaLineare(faseOnda(x, t, K, W), 0),
    campoB: (x) => {
      const c = ondaLineare(faseOnda(x, t, K, W), 0);
      return { ey: 0, exPrime: c.ey };
    },
  });

  // 2) sorgente non polarizzata: la direzione di oscillazione varia in
  // modo continuo e disordinato lungo l'onda, invece di restare fissa
  disegnaOnda(canvasSorgente, {
    campoE: (x) => {
      const fase = faseOnda(x, t, K, W);
      return ondaLineare(fase, angoloNonPolarizzato(x, t));
    },
  });

  // 3) dopo il primo polarizzatore (riferimento, verticale = angolo 0)
  disegnaOnda(canvasRiferimento, {
    campoE: (x) => ondaLineare(faseOnda(x, t, K, W), 0),
    campoB: (x) => {
      const c = ondaLineare(faseOnda(x, t, K, W), 0);
      return { ey: 0, exPrime: c.ey };
    },
  });

  // 4) dopo il secondo filtro
  const tipo = inputTipo.value;
  const angoloDeg = Number(inputAngolo.value);
  const thetaRad = (angoloDeg * Math.PI) / 180;

  const I0 = 1;
  const I1 = I0 / 2;
  let I2, scala2;
  if (tipo === "lineare") {
    scala2 = Math.abs(Math.cos(thetaRad));
    I2 = I1 * Math.cos(thetaRad) * Math.cos(thetaRad);
  } else {
    scala2 = Math.SQRT1_2;
    I2 = I1 / 2;
  }

  disegnaOnda(canvasSecondo, {
    campoE: (x) => {
      const fase = faseOnda(x, t, K, W);
      const campo = tipo === "lineare" ? ondaLineare(fase, thetaRad) : ondaCircolare(fase);
      return { ey: campo.ey * scala2, exPrime: campo.exPrime * scala2 };
    },
  });

  const etichettaFiltro = tipo === "lineare" ? `lineare, &theta; = ${angoloDeg}&deg;` : "circolare";
  risultati.innerHTML =
    `<strong>I&#8320;</strong> (sorgente) = ${fmt(I0)} &nbsp; ` +
    `<strong>I&#8321;</strong> (dopo 1&deg; filtro) = ${fmt(I1)} &nbsp; ` +
    `<strong>I&#8322;</strong> (dopo 2&deg; filtro, ${etichettaFiltro}) = ${fmt(I2)}`;

  requestAnimationFrame(tick);
}

requestAnimationFrame(tick);
