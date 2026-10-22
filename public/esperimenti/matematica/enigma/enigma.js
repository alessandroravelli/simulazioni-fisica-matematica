// Motore della macchina Enigma (modelli I, M3 e M4) con i cablaggi storici.
// Nessuna dipendenza dal browser: si può provare anche con node.

export const ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// cablaggio (lettera in uscita per A, B, C, ...) e lettere della finestra
// in cui il rotore fa scattare quello alla sua sinistra
export const ROTORI = {
  I: { cablaggio: "EKMFLGDQVZNTOWYHXUSPAIBRCJ", tacche: "Q" },
  II: { cablaggio: "AJDKSIRUXBLHWTMCQGZNPYFVOE", tacche: "E" },
  III: { cablaggio: "BDFHJLCPRTXVZNYEIWGAKMUSQO", tacche: "V" },
  IV: { cablaggio: "ESOVPZJAYQUIRHXLNFTGKDCMWB", tacche: "J" },
  V: { cablaggio: "VZBRGITYUPSDNHLXAWMJQOFECK", tacche: "Z" },
  VI: { cablaggio: "JPGVOUMFYQBENHZRDKASXLICTW", tacche: "ZM" },
  VII: { cablaggio: "NZJHGRCXMYSWBOUFAIVLPEKQDT", tacche: "ZM" },
  VIII: { cablaggio: "FKQHTLXOCBJSPDZRAMEWNIUYGV", tacche: "ZM" },
  // rotori sottili della M4: stanno nella quarta posizione e non girano mai
  Beta: { cablaggio: "LEYJVCNIXWPBQMDRTAKZGFUHOS", tacche: "" },
  Gamma: { cablaggio: "FSOKANUERHMBTIYCWLQPZXVGJD", tacche: "" },
};

export const RIFLETTORI = {
  B: "YRUHQSLDPXNGOKMIEBFZCWVJAT",
  C: "FVPJIAOYEDRZXWGCTKUQSBNMHL",
  "B sottile": "ENKQAUYWJICOPBLMDXZVFTHRGS",
  "C sottile": "RDOBJNTKVEHMLFCWZAXGYIPSUQ",
};

export const MODELLI = {
  I: { nome: "Enigma I (esercito e aviazione)", rotori: ["I", "II", "III", "IV", "V"], riflettori: ["B", "C"], quarto: null },
  M3: { nome: "Enigma M3 (marina)", rotori: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"], riflettori: ["B", "C"], quarto: null },
  M4: {
    nome: "Enigma M4 (sommergibili, dal 1942)",
    rotori: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"],
    riflettori: ["B sottile", "C sottile"],
    quarto: ["Beta", "Gamma"],
  },
};

const mod = (n) => ((n % 26) + 26) % 26;
const indice = (lettera) => ALFABETO.indexOf(lettera);

// Pannello delle prese: "AB CD EF" → scambia A↔B, C↔D, E↔F.
// Restituisce { mappa, errore }.
export function leggiPannello(testo) {
  const mappa = [...Array(26).keys()];
  const coppie = testo.toUpperCase().split(/[^A-Z]+/).filter(Boolean);
  const usate = new Set();
  for (const c of coppie) {
    if (c.length !== 2) return { mappa, errore: `"${c}" non è una coppia di lettere` };
    const [a, b] = [indice(c[0]), indice(c[1])];
    if (a === b) return { mappa, errore: `"${c}": una lettera non può essere collegata a se stessa` };
    for (const x of [c[0], c[1]]) {
      if (usate.has(x)) return { mappa, errore: `la lettera ${x} è collegata due volte` };
      usate.add(x);
    }
    mappa[a] = b;
    mappa[b] = a;
  }
  if (coppie.length > 13) return { mappa, errore: "al massimo 13 cavi" };
  return { mappa, errore: null, cavi: coppie.length };
}

function creaRotore(nome, anello, posizione) {
  const { cablaggio, tacche } = ROTORI[nome];
  const avanti = [...cablaggio].map(indice);
  const indietro = new Array(26);
  avanti.forEach((u, i) => (indietro[u] = i));
  return {
    nome,
    anello, // Ringstellung, 0 = A (01)
    posizione, // lettera nella finestra, 0 = A
    tacche: [...tacche].map(indice),
    allaTacca() {
      return this.tacche.includes(this.posizione);
    },
    passo() {
      this.posizione = mod(this.posizione + 1);
    },
    // contatto d'ingresso (rispetto alla macchina) → contatto d'uscita
    avanti(c) {
      const s = this.posizione - this.anello;
      return mod(avanti[mod(c + s)] - s);
    },
    indietro(c) {
      const s = this.posizione - this.anello;
      return mod(indietro[mod(c + s)] - s);
    },
  };
}

// impostazioni = { rotori: ["I","II","III"] (da sinistra a destra), quarto: "Beta" | null,
//                  anelli: [0,0,0(,0)], posizioni: [0,0,0(,0)], riflettore: "B", pannello: "AB CD" }
// Per la M4 anelli[0] e posizioni[0] sono quelli del quarto rotore.
export function creaEnigma(impostazioni) {
  const { quarto, riflettore } = impostazioni;
  const nomi = quarto ? [quarto, ...impostazioni.rotori] : [...impostazioni.rotori];
  const rotori = nomi.map((n, i) => creaRotore(n, impostazioni.anelli[i], impostazioni.posizioni[i]));
  const rifl = [...RIFLETTORI[riflettore]].map(indice);
  const pannello = leggiPannello(impostazioni.pannello || "").mappa;

  // i tre rotori che girano sono sempre gli ultimi tre (sinistro, centrale, destro)
  const [sx, cx, dx] = rotori.slice(-3);

  function scatta() {
    // il "doppio passo": se il centrale è alla tacca, avanza insieme al sinistro
    if (cx.allaTacca()) {
      cx.passo();
      sx.passo();
    } else if (dx.allaTacca()) {
      cx.passo();
    }
    dx.passo();
  }

  // cifra una lettera: prima scattano i rotori, poi passa la corrente.
  // Restituisce la lettera e il percorso (contatti 0–25) per disegnarlo.
  function premi(lettera) {
    scatta();
    const percorso = [];
    let c = indice(lettera);
    percorso.push({ dove: "tastiera", c });
    c = pannello[c];
    percorso.push({ dove: "pannello", c });
    for (let i = rotori.length - 1; i >= 0; i--) {
      c = rotori[i].avanti(c);
      percorso.push({ dove: rotori[i].nome, c });
    }
    c = rifl[c];
    percorso.push({ dove: "riflettore", c });
    for (let i = 0; i < rotori.length; i++) {
      c = rotori[i].indietro(c);
      percorso.push({ dove: rotori[i].nome, c });
    }
    c = pannello[c];
    percorso.push({ dove: "pannello", c });
    return { lettera: ALFABETO[c], percorso };
  }

  return {
    rotori,
    premi,
    posizioni: () => rotori.map((r) => ALFABETO[r.posizione]).join(""),
    imposta: (i, p) => (rotori[i].posizione = mod(p)),
  };
}

// Numero di chiavi possibili con n cavi nel pannello: 26! / ((26−2n)! · n! · 2^n)
export function combinazioniPannello(n) {
  let num = 1n;
  for (let k = 26 - 2 * n + 1; k <= 26; k++) num *= BigInt(k);
  let den = 1n;
  for (let k = 2; k <= n; k++) den *= BigInt(k);
  return num / (den * 2n ** BigInt(n));
}
