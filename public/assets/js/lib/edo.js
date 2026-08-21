// Risoluzione in forma chiusa di equazioni differenziali ordinarie lineari
// a coefficienti costanti (primo ordine, e secondo ordine omogenee) — i casi
// standard con soluzione nota, niente calcolo simbolico generico.

function risolviSistema2x2(a11, a12, a21, a22, b1, b2) {
  const det = a11 * a22 - a12 * a21;
  return { C1: (b1 * a22 - a12 * b2) / det, C2: (a11 * b2 - b1 * a21) / det };
}

// y' + a*y = b
export function risolviPrimoOrdine({ a, b, cauchy }) {
  const avviso = !cauchy;

  if (a === 0) {
    const C = cauchy ? cauchy.y0 - b * cauchy.x0 : 0;
    return { caso: "a-zero", C, avviso, valuta: (x) => b * x + C };
  }

  const bSuA = b / a;
  const C = cauchy ? (cauchy.y0 - bSuA) * Math.exp(a * cauchy.x0) : 0;
  return { caso: "generale", C, bSuA, avviso, valuta: (x) => C * Math.exp(-a * x) + bSuA };
}

// y'' + p*y' + q*y = 0
export function risolviSecondoOrdineOmogenea({ p, q, cauchy }) {
  const avviso = !cauchy;
  const delta = p * p - 4 * q;

  if (delta > 1e-9) {
    const r1 = (-p + Math.sqrt(delta)) / 2;
    const r2 = (-p - Math.sqrt(delta)) / 2;
    let C1 = 0, C2 = 0;
    if (cauchy) {
      const { x0, y0, y0prime } = cauchy;
      ({ C1, C2 } = risolviSistema2x2(
        Math.exp(r1 * x0), Math.exp(r2 * x0),
        r1 * Math.exp(r1 * x0), r2 * Math.exp(r2 * x0),
        y0, y0prime,
      ));
    }
    return {
      caso: "reali-distinte", r1, r2, C1, C2, avviso,
      valuta: (x) => C1 * Math.exp(r1 * x) + C2 * Math.exp(r2 * x),
    };
  }

  if (delta > -1e-9) {
    const r = -p / 2;
    let C1 = 0, C2 = 0;
    if (cauchy) {
      const { x0, y0, y0prime } = cauchy;
      ({ C1, C2 } = risolviSistema2x2(
        Math.exp(r * x0), x0 * Math.exp(r * x0),
        r * Math.exp(r * x0), (1 + r * x0) * Math.exp(r * x0),
        y0, y0prime,
      ));
    }
    return {
      caso: "reale-doppia", r, C1, C2, avviso,
      valuta: (x) => (C1 + C2 * x) * Math.exp(r * x),
    };
  }

  const alpha = -p / 2;
  const beta = Math.sqrt(-delta) / 2;
  let C1 = 0, C2 = 0;
  if (cauchy) {
    const { x0, y0, y0prime } = cauchy;
    const e = Math.exp(alpha * x0);
    ({ C1, C2 } = risolviSistema2x2(
      e * Math.cos(beta * x0), e * Math.sin(beta * x0),
      e * (alpha * Math.cos(beta * x0) - beta * Math.sin(beta * x0)),
      e * (alpha * Math.sin(beta * x0) + beta * Math.cos(beta * x0)),
      y0, y0prime,
    ));
  }
  return {
    caso: "complesse", alpha, beta, C1, C2, avviso,
    valuta: (x) => Math.exp(alpha * x) * (C1 * Math.cos(beta * x) + C2 * Math.sin(beta * x)),
  };
}
