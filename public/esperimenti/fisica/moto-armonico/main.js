import {
  accelerazioneArmonica,
  posizioneArmonica,
  spostamentoOnda,
  velocitaArmonica,
} from "../../../assets/js/lib/fisica.js";
import { coloriTema, disegnaLinee, preparaCanvas } from "../../../assets/js/lib/grafici.js";

window.katex.render("x(t) = A\\cos(\\omega t + \\varphi_0)", document.getElementById("formula-x"), { throwOnError: false });
window.katex.render(
  "v(t) = \\dfrac{dx}{dt} = -A\\omega\\sin(\\omega t+\\varphi_0) \\qquad a(t) = \\dfrac{d^2x}{dt^2} = -A\\omega^2\\cos(\\omega t+\\varphi_0) = -\\omega^2 x(t)",
  document.getElementById("formula-va"),
  { throwOnError: false },
);

function fmt(v) {
  return Number(v.toFixed(2)).toString();
}

// disegna un segmento con una punta a freccia in (x1,y1), usata per i
// vettori velocità/accelerazione sul cerchio di riferimento.
function disegnaFreccia(ctx, x0, y0, x1, y1, colore) {
  ctx.strokeStyle = colore;
  ctx.fillStyle = colore;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(x0, y0);
  ctx.lineTo(x1, y1);
  ctx.stroke();
  const angolo = Math.atan2(y1 - y0, x1 - x0);
  const lung = 7;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x1 - lung * Math.cos(angolo - Math.PI / 6), y1 - lung * Math.sin(angolo - Math.PI / 6));
  ctx.lineTo(x1 - lung * Math.cos(angolo + Math.PI / 6), y1 - lung * Math.sin(angolo + Math.PI / 6));
  ctx.closePath();
  ctx.fill();
}

// --- pannello di moto armonico: cerchio di riferimento + grafico
// scorrevole di x(t) (e, se attivati, v(t) e a(t) con ampiezza
// normalizzata ad A per confrontarne le fasi).
function creaPannelloArmonico(suffisso) {
  const inputA = document.getElementById(`input-A-${suffisso}`);
  const valoreA = document.getElementById(`valore-A-${suffisso}`);
  const inputOmega = document.getElementById(`input-omega-${suffisso}`);
  const valoreOmega = document.getElementById(`valore-omega-${suffisso}`);
  const inputFase = document.getElementById(`input-fase-${suffisso}`);
  const valoreFase = document.getElementById(`valore-fase-${suffisso}`);
  const inputVel = document.getElementById(`input-vel-${suffisso}`);
  const inputAcc = document.getElementById(`input-acc-${suffisso}`);
  const canvasCerchio = document.getElementById(`canvas-cerchio-${suffisso}`);
  const canvasGrafico = document.getElementById(`canvas-grafico-${suffisso}`);
  const risultati = document.getElementById(`risultati-${suffisso}`);

  function aggiornaEtichette() {
    valoreA.textContent = inputA.value;
    valoreOmega.textContent = Number(inputOmega.value).toFixed(1);
    valoreFase.textContent = inputFase.value;
  }
  [inputA, inputOmega, inputFase].forEach((el) => el.addEventListener("input", aggiornaEtichette));
  aggiornaEtichette();

  return function disegna(t) {
    const A = Number(inputA.value);
    const omega = Number(inputOmega.value);
    const phi0 = (Number(inputFase.value) * Math.PI) / 180;
    const mostraVel = inputVel.checked;
    const mostraAcc = inputAcc.checked;
    const colori = coloriTema();

    // --- cerchio di riferimento ---
    const cerchio = preparaCanvas(canvasCerchio);
    cerchio.ctx.clearRect(0, 0, cerchio.larghezza, cerchio.altezza);
    const cx = cerchio.larghezza / 2;
    const cy = cerchio.altezza / 2;
    const R = Math.min(A, cerchio.altezza / 2 - 20, cerchio.larghezza / 2 - 20);
    const theta = omega * t + phi0;
    const px = cx + R * Math.cos(theta);
    const py = cy - R * Math.sin(theta);

    cerchio.ctx.strokeStyle = colori.griglia;
    cerchio.ctx.lineWidth = 1;
    cerchio.ctx.beginPath();
    cerchio.ctx.arc(cx, cy, R, 0, Math.PI * 2);
    cerchio.ctx.stroke();
    cerchio.ctx.beginPath();
    cerchio.ctx.moveTo(cx - R, cy);
    cerchio.ctx.lineTo(cx + R, cy);
    cerchio.ctx.stroke();

    cerchio.ctx.strokeStyle = colori.testoMuto;
    cerchio.ctx.beginPath();
    cerchio.ctx.moveTo(cx, cy);
    cerchio.ctx.lineTo(px, py);
    cerchio.ctx.stroke();

    // proiezione sul diametro orizzontale: è il valore x(t)
    cerchio.ctx.strokeStyle = `${colori.serie1}99`;
    cerchio.ctx.setLineDash([4, 4]);
    cerchio.ctx.beginPath();
    cerchio.ctx.moveTo(px, py);
    cerchio.ctx.lineTo(px, cy);
    cerchio.ctx.stroke();
    cerchio.ctx.setLineDash([]);
    cerchio.ctx.fillStyle = colori.serie1;
    cerchio.ctx.beginPath();
    cerchio.ctx.arc(px, cy, 4, 0, Math.PI * 2);
    cerchio.ctx.fill();

    cerchio.ctx.beginPath();
    cerchio.ctx.arc(px, py, 6, 0, Math.PI * 2);
    cerchio.ctx.fill();

    if (mostraVel) {
      // velocità tangenziale (direzione di rotazione); lunghezza non in
      // scala, solo indicativa della direzione.
      const dir = { x: -Math.sin(theta), y: -Math.cos(theta) };
      disegnaFreccia(cerchio.ctx, px, py, px + dir.x * R * 0.4, py + dir.y * R * 0.4, colori.serie2);
    }
    if (mostraAcc) {
      // accelerazione centripeta (sempre verso il centro, dato che la
      // velocità angolare è costante).
      const dir = { x: cx - px, y: cy - py };
      const norma = Math.hypot(dir.x, dir.y) || 1;
      disegnaFreccia(cerchio.ctx, px, py, px + (dir.x / norma) * R * 0.3, py + (dir.y / norma) * R * 0.3, colori.serie3);
    }

    // --- grafico scorrevole: finestra di 4 periodi, curva che sfuma
    // verso il passato (bordo sinistro) ---
    const finestra = ((2 * Math.PI) / omega) * 4;
    const curve = [{ valuta: (tt) => posizioneArmonica(A, omega, tt, phi0), colore: colori.serie1, dissolvenza: true }];
    if (mostraVel) {
      curve.push({ valuta: (tt) => -A * Math.sin(omega * tt + phi0), colore: colori.serie2, dissolvenza: true });
    }
    if (mostraAcc) {
      curve.push({ valuta: (tt) => -A * Math.cos(omega * tt + phi0), colore: colori.serie3, dissolvenza: true });
    }

    const grafico = preparaCanvas(canvasGrafico);
    disegnaLinee(grafico.ctx, grafico.larghezza, grafico.altezza, {
      xMin: t - finestra,
      xMax: t,
      yMin: -A * 1.2,
      yMax: A * 1.2,
      curve,
      etichettaAsseX: "t (s)",
    });

    const T = (2 * Math.PI) / omega;
    risultati.innerHTML =
      `T = ${fmt(T)} s &nbsp; f = ${fmt(1 / T)} Hz &nbsp; ` +
      `x = ${fmt(posizioneArmonica(A, omega, t, phi0))} cm &nbsp; ` +
      `v = ${fmt(velocitaArmonica(A, omega, t, phi0))} cm/s &nbsp; ` +
      `a = ${fmt(accelerazioneArmonica(A, omega, t, phi0))} cm/s&sup2;`;
  };
}

// --- onda trasversale: una corda i cui punti oscillano perpendicolarmente
// alla propagazione (qui verticalmente); alcune particelle sono
// evidenziate per mostrarne il moto solo verticale. ---
function creaOndaTrasversale() {
  const inputA = document.getElementById("input-A-trasv");
  const valoreA = document.getElementById("valore-A-trasv");
  const inputLambda = document.getElementById("input-lambda-trasv");
  const valoreLambda = document.getElementById("valore-lambda-trasv");
  const inputV = document.getElementById("input-v-trasv");
  const valoreV = document.getElementById("valore-v-trasv");
  const inputDir = document.getElementById("input-dir-trasv");
  const canvas = document.getElementById("canvas-trasv");
  const risultati = document.getElementById("risultati-trasv");

  function aggiornaEtichette() {
    valoreA.textContent = inputA.value;
    valoreLambda.textContent = inputLambda.value;
    valoreV.textContent = inputV.value;
  }
  [inputA, inputLambda, inputV].forEach((el) => el.addEventListener("input", aggiornaEtichette));
  aggiornaEtichette();

  return function disegna(t) {
    const A = Number(inputA.value);
    const lambda = Number(inputLambda.value);
    const velocita = Number(inputV.value);
    const verso = Number(inputDir.value);
    const k = (2 * Math.PI) / lambda;
    const omega = k * velocita;
    const colori = coloriTema();
    const { ctx, larghezza, altezza } = preparaCanvas(canvas);
    ctx.clearRect(0, 0, larghezza, altezza);
    const baseline = altezza / 2;

    ctx.strokeStyle = colori.griglia;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(0, baseline);
    ctx.lineTo(larghezza, baseline);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.strokeStyle = colori.serie1;
    ctx.lineWidth = 2;
    ctx.beginPath();
    const passo = 3;
    for (let x = 0; x <= larghezza; x += passo) {
      const y = baseline - spostamentoOnda(x, t, A, k, omega, 0, verso);
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // particelle evidenziate: si muovono solo in verticale
    const nParticelle = 14;
    for (let i = 0; i <= nParticelle; i++) {
      const x = (larghezza / nParticelle) * i;
      const y = baseline - spostamentoOnda(x, t, A, k, omega, 0, verso);
      ctx.strokeStyle = `${colori.serie2}55`;
      ctx.beginPath();
      ctx.moveTo(x, baseline);
      ctx.lineTo(x, y);
      ctx.stroke();
      ctx.fillStyle = colori.serie2;
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI * 2);
      ctx.fill();
    }

    const T = lambda / velocita;
    risultati.innerHTML = `T = ${fmt(T)} s &nbsp; f = ${fmt(1 / T)} Hz &nbsp; k = ${fmt(k)} rad/cm &nbsp; &omega; = ${fmt(omega)} rad/s`;
  };
}

// --- onda longitudinale: particelle disposte lungo x che oscillano lungo
// x stesso, creando compressioni (particelle ravvicinate) e rarefazioni
// (particelle distanziate) — come in una molla o in un'onda di pressione.
function creaOndaLongitudinale() {
  const inputA = document.getElementById("input-A-long");
  const valoreA = document.getElementById("valore-A-long");
  const inputLambda = document.getElementById("input-lambda-long");
  const valoreLambda = document.getElementById("valore-lambda-long");
  const inputV = document.getElementById("input-v-long");
  const valoreV = document.getElementById("valore-v-long");
  const inputDir = document.getElementById("input-dir-long");
  const canvas = document.getElementById("canvas-long");
  const risultati = document.getElementById("risultati-long");

  function aggiornaEtichette() {
    valoreA.textContent = inputA.value;
    valoreLambda.textContent = inputLambda.value;
    valoreV.textContent = inputV.value;
  }
  [inputA, inputLambda, inputV].forEach((el) => el.addEventListener("input", aggiornaEtichette));
  aggiornaEtichette();

  const nParticelle = 60;

  return function disegna(t) {
    const A = Number(inputA.value);
    const lambda = Number(inputLambda.value);
    const velocita = Number(inputV.value);
    const verso = Number(inputDir.value);
    const k = (2 * Math.PI) / lambda;
    const omega = k * velocita;
    const colori = coloriTema();
    const { ctx, larghezza, altezza } = preparaCanvas(canvas);
    ctx.clearRect(0, 0, larghezza, altezza);
    const baseline = altezza / 2;

    const d0 = larghezza / (nParticelle - 1);
    const posizioni = [];
    for (let i = 0; i < nParticelle; i++) {
      const x0 = i * d0;
      posizioni.push(x0 + spostamentoOnda(x0, t, A, k, omega, 0, verso));
    }

    // fasce di compressione (spaziatura minore del riposo) e rarefazione
    // (spaziatura maggiore), colorate in base al rapporto rispetto a d0
    for (let i = 0; i < nParticelle - 1; i++) {
      const spaziatura = Math.max(posizioni[i + 1] - posizioni[i], 1e-6);
      const rapporto = d0 / spaziatura;
      const intensita = Math.max(0, Math.min(1, (rapporto - 1) / 1.5 + 0.5));
      ctx.fillStyle = colori.serie1;
      ctx.globalAlpha = 0.08 + 0.35 * intensita;
      ctx.fillRect(posizioni[i], baseline - 40, posizioni[i + 1] - posizioni[i], 80);
    }
    ctx.globalAlpha = 1;

    ctx.strokeStyle = colori.testo;
    ctx.lineWidth = 2;
    for (const x of posizioni) {
      ctx.beginPath();
      ctx.moveTo(x, baseline - 16);
      ctx.lineTo(x, baseline + 16);
      ctx.stroke();
    }

    const T = lambda / velocita;
    risultati.innerHTML = `T = ${fmt(T)} s &nbsp; f = ${fmt(1 / T)} Hz &nbsp; k = ${fmt(k)} rad/cm &nbsp; &omega; = ${fmt(omega)} rad/s`;
  };
}

const pannello1 = creaPannelloArmonico("1");
const pannello2 = creaPannelloArmonico("2");
const ondaTrasversale = creaOndaTrasversale();
const ondaLongitudinale = creaOndaLongitudinale();

function tick(tempoMs) {
  const t = tempoMs / 1000;
  pannello1(t);
  pannello2(t);
  ondaTrasversale(t);
  ondaLongitudinale(t);
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
