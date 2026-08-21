// Parser/valutatore di espressioni matematiche semplici, usato per
// confrontare la soluzione proposta dallo studente con quella calcolata.
// Supporta: + - * / ^, parentesi, funzioni exp/sin/cos/tan/sqrt/ln/abs,
// costanti pi/e, variabili fornite tramite uno "scope" (es. x, C, C1...).

const FUNZIONI = {
  exp: Math.exp,
  sin: Math.sin,
  cos: Math.cos,
  tan: Math.tan,
  sqrt: Math.sqrt,
  ln: Math.log,
  log: Math.log,
  abs: Math.abs,
};

const COSTANTI = { pi: Math.PI, e: Math.E };

function tokenizza(testo) {
  const tok = [];
  let i = 0;
  while (i < testo.length) {
    const c = testo[i];
    if (/\s/.test(c)) { i++; continue; }
    if (/[0-9.]/.test(c)) {
      let j = i;
      while (j < testo.length && /[0-9.]/.test(testo[j])) j++;
      tok.push({ tipo: "numero", valore: parseFloat(testo.slice(i, j)) });
      i = j;
      continue;
    }
    if (/[a-zA-Z_]/.test(c)) {
      let j = i;
      while (j < testo.length && /[a-zA-Z_0-9]/.test(testo[j])) j++;
      tok.push({ tipo: "identificatore", valore: testo.slice(i, j) });
      i = j;
      continue;
    }
    if ("+-*/^(),".includes(c)) {
      tok.push({ tipo: c });
      i++;
      continue;
    }
    throw new Error(`Carattere non riconosciuto: "${c}"`);
  }
  return tok;
}

// Compila una stringa in una funzione (scope) => numero.
export function compilaEspressione(testo) {
  const tok = tokenizza(testo);
  let pos = 0;

  const guarda = () => tok[pos];
  const consuma = (tipo) => {
    const t = tok[pos];
    if (!t || (tipo && t.tipo !== tipo)) {
      throw new Error(`Espressione non valida vicino a "${t ? (t.valore ?? t.tipo) : "fine"}"`);
    }
    pos++;
    return t;
  };

  function parseEspressione() {
    let nodo = parseTermine();
    while (guarda() && (guarda().tipo === "+" || guarda().tipo === "-")) {
      const op = consuma().tipo;
      nodo = { tipo: "binario", op, sinistro: nodo, destro: parseTermine() };
    }
    return nodo;
  }

  function parseTermine() {
    let nodo = parseUnario();
    while (guarda() && (guarda().tipo === "*" || guarda().tipo === "/")) {
      const op = consuma().tipo;
      nodo = { tipo: "binario", op, sinistro: nodo, destro: parseUnario() };
    }
    return nodo;
  }

  function parseUnario() {
    if (guarda() && (guarda().tipo === "-" || guarda().tipo === "+")) {
      const op = consuma().tipo;
      return { tipo: "unario", op, valore: parseUnario() };
    }
    return parsePotenza();
  }

  function parsePotenza() {
    const base = parsePrimario();
    if (guarda() && guarda().tipo === "^") {
      consuma();
      return { tipo: "binario", op: "^", sinistro: base, destro: parseUnario() };
    }
    return base;
  }

  function parsePrimario() {
    const t = guarda();
    if (!t) throw new Error("Espressione incompleta");
    if (t.tipo === "numero") { consuma(); return { tipo: "numero", valore: t.valore }; }
    if (t.tipo === "(") {
      consuma();
      const nodo = parseEspressione();
      consuma(")");
      return nodo;
    }
    if (t.tipo === "identificatore") {
      consuma();
      if (guarda() && guarda().tipo === "(") {
        consuma();
        const argomenti = [parseEspressione()];
        while (guarda() && guarda().tipo === ",") { consuma(); argomenti.push(parseEspressione()); }
        consuma(")");
        return { tipo: "chiamata", nome: t.valore, argomenti };
      }
      return { tipo: "variabile", nome: t.valore };
    }
    throw new Error(`Espressione non valida vicino a "${t.valore ?? t.tipo}"`);
  }

  const ast = parseEspressione();
  if (pos !== tok.length) throw new Error("Espressione non valida: caratteri in eccesso alla fine");

  function valuta(nodo, scope) {
    switch (nodo.tipo) {
      case "numero": return nodo.valore;
      case "variabile":
        if (nodo.nome in scope) return scope[nodo.nome];
        if (nodo.nome in COSTANTI) return COSTANTI[nodo.nome];
        throw new Error(`Variabile sconosciuta: ${nodo.nome}`);
      case "chiamata": {
        const f = FUNZIONI[nodo.nome];
        if (!f) throw new Error(`Funzione sconosciuta: ${nodo.nome}`);
        return f(...nodo.argomenti.map((a) => valuta(a, scope)));
      }
      case "unario":
        return nodo.op === "-" ? -valuta(nodo.valore, scope) : valuta(nodo.valore, scope);
      case "binario": {
        const s = valuta(nodo.sinistro, scope);
        const d = valuta(nodo.destro, scope);
        if (nodo.op === "+") return s + d;
        if (nodo.op === "-") return s - d;
        if (nodo.op === "*") return s * d;
        if (nodo.op === "/") return s / d;
        if (nodo.op === "^") return Math.pow(s, d);
      }
    }
  }

  return (scope) => valuta(ast, scope);
}
