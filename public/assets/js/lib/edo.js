// Integrazione numerica (Runge-Kutta 4) di equazioni differenziali con
// coefficienti anche non costanti — niente forma chiusa: serve solo a
// disegnare la curva "corretta" da confrontare con la soluzione proposta.

function passoRK4(f, x, y, h) {
  const k1 = f(x, y);
  const k2 = f(x + h / 2, y + (h / 2) * k1);
  const k3 = f(x + h / 2, y + (h / 2) * k2);
  const k4 = f(x + h, y + h * k3);
  return y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
}

// y' = f(x, y), condizione iniziale y(x0) = y0. Integra in avanti fino a
// xMax e indietro fino a xMin, partendo sempre da x0.
export function integraPrimoOrdine(f, x0, y0, xMin, xMax, passiTotali = 400) {
  const h = (xMax - xMin) / passiTotali;

  const puntiX = [x0];
  const puntiY = [y0];
  let x = x0, y = y0;
  const nAvanti = Math.round((xMax - x0) / h);
  for (let i = 0; i < nAvanti && Number.isFinite(y); i++) {
    y = passoRK4(f, x, y, h);
    x += h;
    if (Number.isFinite(y)) { puntiX.push(x); puntiY.push(y); }
  }

  const primaX = [], primaY = [];
  x = x0; y = y0;
  const nIndietro = Math.round((x0 - xMin) / h);
  for (let i = 0; i < nIndietro && Number.isFinite(y); i++) {
    y = passoRK4(f, x, y, -h);
    x -= h;
    if (Number.isFinite(y)) { primaX.unshift(x); primaY.unshift(y); }
  }

  return { puntiX: [...primaX, ...puntiX], puntiY: [...primaY, ...puntiY] };
}

function sommaStato(stato, derivata, scala) {
  return [stato[0] + scala * derivata[0], stato[1] + scala * derivata[1]];
}

function passoRK4Sistema(f, x, stato, h) {
  const k1 = f(x, stato);
  const k2 = f(x + h / 2, sommaStato(stato, k1, h / 2));
  const k3 = f(x + h / 2, sommaStato(stato, k2, h / 2));
  const k4 = f(x + h, sommaStato(stato, k3, h));
  return [
    stato[0] + (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
    stato[1] + (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]),
  ];
}

// y'' + p(x)*y' + q(x)*y = 0, condizioni iniziali y(x0)=y0, y'(x0)=y0prime.
// Integra il sistema equivalente u=y, v=y' (u'=v, v'=-p*v-q*u).
export function integraSecondoOrdineOmogenea(pFn, qFn, x0, y0, y0prime, xMin, xMax, passiTotali = 400) {
  const f = (x, stato) => [stato[1], -pFn(x) * stato[1] - qFn(x) * stato[0]];
  const h = (xMax - xMin) / passiTotali;

  const puntiX = [x0];
  const puntiY = [y0];
  let x = x0, stato = [y0, y0prime];
  const nAvanti = Math.round((xMax - x0) / h);
  for (let i = 0; i < nAvanti && Number.isFinite(stato[0]); i++) {
    stato = passoRK4Sistema(f, x, stato, h);
    x += h;
    if (Number.isFinite(stato[0])) { puntiX.push(x); puntiY.push(stato[0]); }
  }

  const primaX = [], primaY = [];
  x = x0; stato = [y0, y0prime];
  const nIndietro = Math.round((x0 - xMin) / h);
  for (let i = 0; i < nIndietro && Number.isFinite(stato[0]); i++) {
    stato = passoRK4Sistema(f, x, stato, -h);
    x -= h;
    if (Number.isFinite(stato[0])) { primaX.unshift(x); primaY.unshift(stato[0]); }
  }

  return { puntiX: [...primaX, ...puntiX], puntiY: [...primaY, ...puntiY] };
}

// Trasforma la sequenza di punti (x crescenti) calcolata da RK4 in una
// funzione valuta(x) => y, per poterla disegnare con la stessa API delle
// altre curve (interpolazione lineare fra i due punti più vicini).
export function creaInterpolatore({ puntiX, puntiY }) {
  return (x) => {
    if (puntiX.length === 0) return NaN;
    if (x <= puntiX[0]) return puntiY[0];
    if (x >= puntiX[puntiX.length - 1]) return puntiY[puntiY.length - 1];
    let lo = 0, hi = puntiX.length - 1;
    while (hi - lo > 1) {
      const mid = (lo + hi) >> 1;
      if (puntiX[mid] <= x) lo = mid; else hi = mid;
    }
    const t = (x - puntiX[lo]) / (puntiX[hi] - puntiX[lo]);
    return puntiY[lo] + t * (puntiY[hi] - puntiY[lo]);
  };
}
