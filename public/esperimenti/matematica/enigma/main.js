import { ALFABETO, MODELLI, ROTORI, RIFLETTORI, combinazioniPannello, creaEnigma, leggiPannello } from "./enigma.js";

const FILE = ["QWERTZUIO", "ASDFGHJK", "PYXCVBNML"]; // disposizione dei tasti della vera Enigma
const $ = (id) => document.getElementById(id);

const selModello = $("input-modello");
const selRiflettore = $("input-riflettore");
const slotRotori = $("slot-rotori");
const inPannello = $("input-pannello");

for (const [chiave, m] of Object.entries(MODELLI)) selModello.add(new Option(m.nome, chiave));

let macchina = null;
let battuto = "";
let uscito = "";
const lampade = {};
const tasti = {};

// ---------------------------------------------------------------- impostazioni

function opzioniLettere(select, conNumero) {
  select.innerHTML = "";
  [...ALFABETO].forEach((l, i) => select.add(new Option(conNumero ? `${String(i + 1).padStart(2, "0")} (${l})` : l, i)));
}

// costruisce gli slot dei rotori (da sinistra a destra) per il modello scelto
function costruisciSlot() {
  const m = MODELLI[selModello.value];
  selRiflettore.innerHTML = "";
  m.riflettori.forEach((r) => selRiflettore.add(new Option(r, r)));
  slotRotori.innerHTML = "";
  const etichette = m.quarto ? ["sottile", "sinistro", "centrale", "destro"] : ["sinistro", "centrale", "destro"];
  const predefiniti = m.quarto ? ["Beta", "I", "II", "III"] : ["I", "II", "III"];
  etichette.forEach((etichetta, i) => {
    const div = document.createElement("div");
    div.className = "slot";
    const scelte = m.quarto && i === 0 ? m.quarto : m.rotori;
    div.innerHTML = `<span class="titolo-slot">${i === 0 && m.quarto ? "4° rotore (sottile)" : `Rotore ${etichetta}`}</span>
      <select class="rotore" aria-label="Rotore ${etichetta}"></select>
      <label>anello</label><select class="anello" aria-label="Anello del rotore ${etichetta}"></select>
      <label>posizione iniziale</label><select class="posizione" aria-label="Posizione iniziale del rotore ${etichetta}"></select>`;
    const sr = div.querySelector(".rotore");
    scelte.forEach((r) => sr.add(new Option(r, r)));
    sr.value = predefiniti[i];
    opzioniLettere(div.querySelector(".anello"), true);
    opzioniLettere(div.querySelector(".posizione"), false);
    slotRotori.append(div);
  });
}

function leggiImpostazioni() {
  const m = MODELLI[selModello.value];
  const slot = [...slotRotori.querySelectorAll(".slot")];
  const nomi = slot.map((s) => s.querySelector(".rotore").value);
  return {
    modello: selModello.value,
    quarto: m.quarto ? nomi[0] : null,
    rotori: m.quarto ? nomi.slice(1) : nomi,
    anelli: slot.map((s) => Number(s.querySelector(".anello").value)),
    posizioni: slot.map((s) => Number(s.querySelector(".posizione").value)),
    riflettore: selRiflettore.value,
    pannello: inPannello.value,
  };
}

// i rotori della stessa macchina devono essere tutti diversi
function rotoriRipetuti(imp) {
  return new Set(imp.rotori).size !== imp.rotori.length;
}

function testoChiave(imp) {
  const anelli = imp.anelli.map((a) => String(a + 1).padStart(2, "0")).join(" ");
  const pos = imp.posizioni.map((p) => ALFABETO[p]).join("");
  const rot = [imp.quarto, ...imp.rotori].filter(Boolean).join(" ");
  const pann = leggiPannello(imp.pannello).errore ? "—" : imp.pannello.toUpperCase().trim() || "nessun cavo";
  return `${imp.modello} · riflettore ${imp.riflettore} · rotori ${rot} · anelli ${anelli} · posizione ${pos} · pannello ${pann}`;
}

function applica() {
  const imp = leggiImpostazioni();
  const pann = leggiPannello(imp.pannello);
  const errori = [];
  if (pann.errore) errori.push(`Pannello: ${pann.errore}.`);
  if (rotoriRipetuti(imp)) errori.push("Ogni rotore si può usare una volta sola.");
  $("errore-pannello").textContent = errori.join(" ");
  if (errori.length) return;
  macchina = creaEnigma(imp);
  battuto = "";
  uscito = "";
  aggiornaNastri();
  aggiornaFinestre();
  spegniLampade();
  disegnaSchema(null);
  $("catena").textContent = "Premi un tasto per vedere il percorso.";
  $("chiave").textContent = `Chiave: ${testoChiave(imp)}`;
  aggiornaConteggio(imp, pann.cavi || 0);
}

function chiaveCasuale() {
  const m = MODELLI[selModello.value];
  const caso = (n) => Math.floor(Math.random() * n);
  const rotori = [...m.rotori].sort(() => Math.random() - 0.5).slice(0, 3);
  const slot = [...slotRotori.querySelectorAll(".slot")];
  const nomi = m.quarto ? [m.quarto[caso(2)], ...rotori] : rotori;
  slot.forEach((s, i) => {
    s.querySelector(".rotore").value = nomi[i];
    s.querySelector(".anello").value = caso(26);
    s.querySelector(".posizione").value = caso(26);
  });
  selRiflettore.value = m.riflettori[caso(m.riflettori.length)];
  const lettere = [...ALFABETO].sort(() => Math.random() - 0.5);
  const coppie = [];
  for (let i = 0; i < 20; i += 2) coppie.push(lettere[i] + lettere[i + 1]);
  inPannello.value = coppie.join(" ");
  applica();
}

// ---------------------------------------------------------------- macchina

function aggiornaFinestre() {
  const cont = $("finestre");
  cont.innerHTML = "";
  macchina.rotori.forEach((r, i) => {
    const f = document.createElement("div");
    f.className = "finestra";
    f.innerHTML = `<button class="freccina" type="button" aria-label="Rotore ${r.nome} avanti">▲</button>
      <span class="lettera">${ALFABETO[r.posizione]}</span>
      <button class="freccina" type="button" aria-label="Rotore ${r.nome} indietro">▼</button>
      <span class="nome">${r.nome}</span>`;
    const [su, giu] = f.querySelectorAll("button");
    su.addEventListener("click", () => { macchina.imposta(i, r.posizione + 1); aggiornaFinestre(); });
    giu.addEventListener("click", () => { macchina.imposta(i, r.posizione - 1); aggiornaFinestre(); });
    cont.append(f);
  });
}

function costruisciTasti() {
  for (const [contenitore, classe, registro] of [[$("lampade"), "lampada", lampade], [$("tastiera"), "tasto", tasti]]) {
    for (const fila of FILE) {
      const riga = document.createElement("div");
      riga.className = "fila";
      for (const l of fila) {
        const el = document.createElement(classe === "tasto" ? "button" : "span");
        el.className = classe;
        el.textContent = l;
        if (classe === "tasto") {
          el.type = "button";
          el.addEventListener("click", () => premi(l));
        }
        registro[l] = el;
        riga.append(el);
      }
      contenitore.append(riga);
    }
  }
}

function spegniLampade() {
  Object.values(lampade).forEach((el) => el.classList.remove("accesa"));
}

const aGruppi = (t) => t.replace(/(.{5})/g, "$1 ").trim();

function aggiornaNastri() {
  $("nastro-in").textContent = aGruppi(battuto);
  $("nastro-out").textContent = aGruppi(uscito);
}

let timerTasto = null;
function premi(lettera) {
  if (!macchina) return;
  const { lettera: out, percorso } = macchina.premi(lettera);
  battuto += lettera;
  uscito += out;
  spegniLampade();
  lampade[out].classList.add("accesa");
  Object.values(tasti).forEach((el) => el.classList.remove("premuto"));
  tasti[lettera].classList.add("premuto");
  clearTimeout(timerTasto);
  timerTasto = setTimeout(() => tasti[lettera].classList.remove("premuto"), 180);
  aggiornaNastri();
  aggiornaFinestre();
  disegnaSchema(percorso);
  scriviCatena(percorso);
}

// ---------------------------------------------------------------- schema del percorso

// colonne da sinistra a destra: riflettore, rotori (sinistro → destro), pannello, tastiera
function disegnaSchema(percorso) {
  const svg = $("schema");
  const n = macchina.rotori.length;
  const bw = 44, gap = 26, rh = 13, top = 34;
  const colonne = ["riflettore", ...macchina.rotori.map((r) => r.nome), "pannello"];
  const W = (colonne.length) * (bw + gap) + 46;
  const H = top + 26 * rh + 10;
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  const xSx = (k) => 10 + k * (bw + gap);
  const xDx = (k) => xSx(k) + bw;
  const y = (c) => top + c * rh + rh / 2;
  let s = "";
  colonne.forEach((nome, k) => {
    s += `<rect class="scatola" x="${xSx(k)}" y="${top - 4}" width="${bw}" height="${26 * rh + 8}" rx="5"/>`;
    const sotto = k >= 1 && k <= n ? ` ${ALFABETO[macchina.rotori[k - 1].posizione]}` : "";
    s += `<text class="titolo" x="${xSx(k) + bw / 2}" y="${top - 12}" text-anchor="middle">${nome}${sotto}</text>`;
    for (let c = 0; c < 26; c++) {
      s += `<circle class="contatto" cx="${xSx(k)}" cy="${y(c)}" r="1.6"/>`;
      if (k > 0) s += `<circle class="contatto" cx="${xDx(k)}" cy="${y(c)}" r="1.6"/>`;
    }
  });
  const kTast = colonne.length;
  for (let c = 0; c < 26; c++) s += `<text class="testo" x="${xSx(kTast) + 8}" y="${y(c) + 3.5}">${ALFABETO[c]}</text>`;
  if (percorso) {
    const c = percorso.map((p) => p.c);
    // andata: tastiera → pannello → rotori da destra a sinistra → riflettore
    const andata = [[xSx(kTast) + 2, y(c[0])], [xDx(n + 1), y(c[0])], [xSx(n + 1), y(c[1])]];
    for (let i = 0; i < n; i++) {
      const k = n - i; // colonna del rotore attraversato
      andata.push([xDx(k), y(c[1 + i])], [xSx(k), y(c[2 + i])]);
    }
    andata.push([xDx(0), y(c[1 + n])], [xSx(0) + 12, y(c[1 + n])]);
    // ritorno: riflettore → rotori da sinistra a destra → pannello → lampada
    const r0 = c[2 + n];
    const ritorno = [[xSx(0) + 12, y(r0)], [xDx(0), y(r0)]];
    for (let i = 0; i < n; i++) {
      const k = 1 + i;
      ritorno.push([xSx(k), y(c[2 + n + i])], [xDx(k), y(c[3 + n + i])]);
    }
    const cf = c[c.length - 1];
    ritorno.push([xSx(n + 1), y(c[c.length - 2])], [xDx(n + 1), y(cf)], [xSx(kTast) + 2, y(cf)]);
    const d = (pts) => "M" + pts.map(([a, b]) => `${a.toFixed(1)},${b.toFixed(1)}`).join(" L");
    s += `<path class="andata" d="${d(andata)}"/><path class="ritorno" d="${d(ritorno)}"/>`;
    s += `<path class="andata" d="M${xSx(0) + 12},${y(c[1 + n])} L${xSx(0) + 12},${y(r0)}" stroke-dasharray="3 2"/>`;
    s += `<text class="testo in" x="${xSx(kTast) + 8}" y="${y(c[0]) + 3.5}">${ALFABETO[c[0]]}</text>`;
    s += `<text class="testo out" x="${xSx(kTast) + 8}" y="${y(cf) + 3.5}">${ALFABETO[cf]}</text>`;
  }
  svg.innerHTML = s;
}

function scriviCatena(percorso) {
  const n = macchina.rotori.length;
  const nomeTappa = (p) => (p.dove === "tastiera" ? "tasto" : p.dove === "pannello" ? "pannello" : p.dove === "riflettore" ? "riflettore" : `rotore ${p.dove}`);
  const parti = percorso.map((p, i) => {
    const classe = i <= n + 2 ? "a" : "r";
    return `<span class="${classe}">${nomeTappa(p)} ${ALFABETO[p.c]}</span>`;
  });
  parti.push(`<span class="r">lampada ${ALFABETO[percorso[percorso.length - 1].c]}</span>`);
  $("catena").innerHTML = parti.join(" → ");
}

// ---------------------------------------------------------------- messaggio intero e conteggio

function elaboraMessaggio(cifra) {
  const imp = leggiImpostazioni();
  if (leggiPannello(imp.pannello).errore || rotoriRipetuti(imp)) {
    $("risultato").textContent = "Correggi prima le impostazioni.";
    return;
  }
  let testo = $("messaggio").value.toUpperCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  testo = cifra ? testo.trim().replace(/\s+/g, "X") : testo.replace(/\s+/g, "");
  testo = testo.replace(/[^A-Z]/g, "");
  const m = creaEnigma(imp);
  const uscita = [...testo].map((l) => m.premi(l).lettera).join("");
  $("risultato").textContent = cifra ? aGruppi(uscita) : uscita.replace(/X/g, " ");
}

const fmtGrande = (n) => n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");

function aggiornaConteggio(imp, cavi) {
  const m = MODELLI[imp.modello];
  const k = m.rotori.length;
  const disposizioni = k * (k - 1) * (k - 2);
  const quarti = m.quarto ? m.quarto.length : 1;
  const nRot = m.quarto ? 4 : 3;
  const posizioni = 26n ** BigInt(nRot);
  const pann = combinazioniPannello(cavi);
  const tot = BigInt(disposizioni * quarti) * posizioni * pann;
  const esp = tot.toString().length - 1;
  $("conteggio").innerHTML = `
    <p>Con il modello scelto e <strong>${cavi}</strong> cavi nel pannello:</p>
    <ul>
      <li>scelta e ordine dei rotori: ${disposizioni}${m.quarto ? " × 2 (Beta o Gamma)" : ""}</li>
      <li>posizioni iniziali: 26<sup>${nRot}</sup> = ${fmtGrande(posizioni)}</li>
      <li>collegamenti del pannello: ${fmtGrande(pann)}</li>
    </ul>
    <p>In totale <strong>${fmtGrande(tot)}</strong> ≈ 10<sup>${esp}</sup> chiavi diverse
    (senza contare anelli e riflettore). Provarle tutte a mano era impossibile:
    a Bletchley Park Alan Turing sfruttò invece una debolezza della macchina,
    <strong>nessuna lettera viene mai cifrata in se stessa</strong>, per scartare
    in fretta la maggior parte delle chiavi con le «bombe» elettromeccaniche.</p>`;
}

// ---------------------------------------------------------------- avvio ed eventi

costruisciTasti();
costruisciSlot();
applica();

selModello.addEventListener("change", () => { costruisciSlot(); applica(); });
selRiflettore.addEventListener("change", applica);
slotRotori.addEventListener("change", applica);
inPannello.addEventListener("input", applica);
$("bottone-iniziale").addEventListener("click", applica);
$("bottone-casuale").addEventListener("click", chiaveCasuale);
$("bottone-cancella").addEventListener("click", () => { battuto = ""; uscito = ""; aggiornaNastri(); spegniLampade(); });
$("bottone-cifra").addEventListener("click", () => elaboraMessaggio(true));
$("bottone-decifra").addEventListener("click", () => elaboraMessaggio(false));
$("bottone-copia").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(testoChiave(leggiImpostazioni()));
    $("bottone-copia").textContent = "Copiata ✓";
    setTimeout(() => ($("bottone-copia").textContent = "Copia la chiave"), 1500);
  } catch {
    $("bottone-copia").textContent = "Copia non riuscita";
  }
});

document.addEventListener("keydown", (e) => {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  if (["INPUT", "TEXTAREA", "SELECT"].includes(e.target.tagName)) return;
  const l = e.key.toUpperCase();
  if (l.length === 1 && ALFABETO.includes(l)) {
    e.preventDefault();
    premi(l);
  }
});
