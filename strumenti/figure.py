"""Genera le figure SVG degli appunti (ridisegno pulito dei disegni a mano).

Uso:  python3 strumenti/figure.py
Scrive i file .svg nelle cartelle "allegati" accanto alle note in
sito/content. I colori sono scelti per leggersi bene sia sul tema chiaro
sia su quello scuro del sito (le figure sono immagini, quindi non
seguono le variabili CSS del tema).
"""

import math
import os

RADICE = os.path.join(os.path.dirname(__file__), "..", "sito", "content")
DIR_MATE = os.path.join(RADICE, "Appunti", "Matematica", "allegati")
DIR_FIS = os.path.join(RADICE, "Appunti", "Fisica", "allegati")

GRIGIO = "#8b93a1"
BLU = "#3b82f6"
ROSSO = "#ef4444"
VERDE = "#22c55e"
ARANCIO = "#f59e0b"
VIOLA = "#a855f7"
ROSA = "#ec4899"
TEAL = "#14b8a6"

FONT = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif"
FONT_MATH = "'Times New Roman', 'STIX Two Math', Georgia, serif"

PI = math.pi


# ---------------------------------------------------------------- base svg

def svg(larghezza, altezza, corpo):
    colori = [GRIGIO, BLU, ROSSO, VERDE, ARANCIO, VIOLA, ROSA, TEAL, "#c4c9d4"]
    marker = "".join(
        f'<marker id="f{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        for c in colori
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {larghezza} {altezza}" '
        f'width="{larghezza}" height="{altezza}" font-family="{FONT}">'
        f"<defs>{marker}</defs>{corpo}</svg>\n"
    )


def linea(x1, y1, x2, y2, colore=GRIGIO, spessore=2, tratteggio=None, freccia=False):
    extra = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    if freccia:
        extra += f' marker-end="url(#f{colore[1:]})"'
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{colore}" '
            f'stroke-width="{spessore}" stroke-linecap="round"{extra}/>')


def testo(x, y, t, colore=GRIGIO, dim=16, ancora="middle", math_=False, grassetto=False):
    font = f' font-family="{FONT_MATH}" font-style="italic"' if math_ else ""
    peso = ' font-weight="600"' if grassetto else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{colore}" font-size="{dim}" '
            f'text-anchor="{ancora}" dominant-baseline="middle"{font}{peso}>{t}</text>')


def pedice(base, ped):
    """Testo con pedice, da usare dentro testo(...)."""
    return f'{base}<tspan baseline-shift="sub" font-size="70%">{ped}</tspan>'


def punto(x, y, colore=GRIGIO, r=4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{colore}"/>'


def arco_angolo(cx, cy, raggio, da, a, colore=ARANCIO, spessore=2):
    """Arco di angolo (in radianti, verso antiorario matematico)."""
    x1, y1 = cx + raggio * math.cos(da), cy - raggio * math.sin(da)
    x2, y2 = cx + raggio * math.cos(a), cy - raggio * math.sin(a)
    grande = 1 if (a - da) % (2 * PI) > PI else 0
    return (f'<path d="M{x1:.1f},{y1:.1f} A{raggio},{raggio} 0 {grande} 0 {x2:.1f},{y2:.1f}" '
            f'fill="none" stroke="{colore}" stroke-width="{spessore}"/>')


def angolo_retto(x, y, dx, dy, lato=10, colore=GRIGIO):
    """Quadratino d'angolo retto nel vertice (x,y); dx, dy = versi dei cateti."""
    return (f'<path d="M{x + dx * lato:.1f},{y:.1f} L{x + dx * lato:.1f},{y + dy * lato:.1f} '
            f'L{x:.1f},{y + dy * lato:.1f}" fill="none" stroke="{colore}" stroke-width="1.5"/>')


# ------------------------------------------------------- piano e cerchio

class Piano:
    """Cerchio goniometrico: coordinate matematiche -> pixel."""

    def __init__(self, cx, cy, r):
        self.cx, self.cy, self.r = cx, cy, r

    def p(self, x, y):
        return self.cx + x * self.r, self.cy - y * self.r

    def assi(self, margine=0.35, etichette=True):
        cx, cy, r = self.cx, self.cy, self.r
        s = linea(cx - r * (1 + margine), cy, cx + r * (1 + margine), cy, freccia=True)
        s += linea(cx, cy + r * (1 + margine), cx, cy - r * (1 + margine), freccia=True)
        if etichette:
            s += testo(cx + r * (1 + margine) + 4, cy + 14, "x", math_=True, dim=18)
            s += testo(cx + 14, cy - r * (1 + margine) - 2, "y", math_=True, dim=18)
        return s

    def cerchio(self, colore=GRIGIO):
        return (f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" fill="none" '
                f'stroke="{colore}" stroke-width="2"/>')


# ------------------------------------------------------------ grafici

ETICHETTE_PI = {
    -1: "−π/6", 1: "π/6",  # usate solo nell'esempio, in sesti
}


def etichetta_multiplo_pi_mezzi(k):
    return {1: "π/2", 2: "π", 3: "3π/2", 4: "2π", 5: "5π/2", 6: "3π", 7: "7π/2", 8: "4π"}[k]


def grafico(f, xmin, xmax, ymin, ymax, larghezza=640, altezza=260, solido=(0, 2 * PI),
            colore=ROSSO, tick_x=None, tick_y=None, nome=None, nome_pos=None,
            asintoti=(), linee_y=(), etichetta_x="x", etichetta_y="y", altre=()):
    """Grafico di f: tratto pieno nell'intervallo `solido`, tratteggiato fuori.
    `altre`: altre curve (funzione, colore) da disegnare sugli stessi assi."""
    mx, my = 40, 24
    sx = (larghezza - 2 * mx) / (xmax - xmin)
    sy = (altezza - 2 * my) / (ymax - ymin)

    def P(x, y):
        return mx + (x - xmin) * sx, altezza - my - (y - ymin) * sy

    x0, y0 = P(0, 0)
    corpo = ""
    for yy, col in linee_y:
        a, b = P(xmin, yy), P(xmax, yy)
        corpo += linea(a[0], a[1], b[0], b[1], colore=col, spessore=1.2, tratteggio="5 4")
    corpo += linea(mx - 10, y0, larghezza - mx + 18, y0, freccia=True)
    corpo += linea(x0, altezza - 4, x0, 6, freccia=True)
    corpo += testo(larghezza - mx + 26, y0 + 14, etichetta_x, math_=True, dim=18)
    corpo += testo(x0 + 14, 12, etichetta_y, math_=True, dim=18)
    for valore, etichetta, col in (tick_x or []):
        px, py = P(valore, 0)
        corpo += linea(px, y0 - 5, px, y0 + 5)
        corpo += testo(px, y0 + 20, etichetta, colore=col or GRIGIO, dim=15)
    for valore, etichetta in (tick_y or []):
        px, py = P(0, valore)
        corpo += linea(x0 - 5, py, x0 + 5, py)
        corpo += testo(x0 - 12, py, etichetta, dim=15, ancora="end")

    clip = f'<clipPath id="area"><rect x="0" y="{my - 14}" width="{larghezza}" height="{altezza - 2 * my + 28}"/></clipPath>'
    curve = ""
    for fun, col in [(f, colore)] + list(altre):
        # campionamento della curva, spezzata vicino agli asintoti
        n = 900
        tratti = []
        corrente = []
        stato = None
        for i in range(n + 1):
            x = xmin + (xmax - xmin) * i / n
            vicino_asintoto = any(abs(x - a) < 0.03 for a in asintoti)
            y = None if vicino_asintoto else fun(x)
            if y is None or y < ymin - 0.5 or y > ymax + 0.5:
                if corrente:
                    tratti.append((stato, corrente))
                corrente, stato = [], None
                continue
            y = max(ymin - 0.4, min(ymax + 0.4, y))
            dentro = solido[0] - 1e-9 <= x <= solido[1] + 1e-9
            if stato is not None and dentro != stato:
                corrente.append(P(x, y))
                tratti.append((stato, corrente))
                corrente = []
            stato = dentro
            corrente.append(P(x, y))
        if corrente:
            tratti.append((stato, corrente))
        for pieno, punti in tratti:
            if len(punti) < 2:
                continue
            d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punti)
            tr = "" if pieno else ' stroke-dasharray="5 5"'
            curve += (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{2.6 if pieno else 1.6}"'
                      f'{tr} stroke-linejoin="round"/>')
    corpo += f'<defs>{clip}</defs><g clip-path="url(#area)">{curve}</g>'
    if nome:
        nx, ny = nome_pos or (larghezza - 150, 30)
        corpo += testo(nx, ny, nome, colore=colore, dim=18, math_=True)
    return svg(larghezza, altezza, corpo)


def tick_pi_mezzi(fino_a, colore=None):
    return [(k * PI / 2, etichetta_multiplo_pi_mezzi(k), colore) for k in range(1, fino_a + 1)]


# ======================================================== GONIOMETRIA

def gonio_circonferenza():
    pl = Piano(250, 210, 150)
    a = math.atan2(0.6, 0.8)
    px, py = pl.p(0.8, 0.6)
    s = pl.assi() + pl.cerchio()
    s += linea(pl.cx, py, px, py, BLU, 3)
    s += linea(px, py, px, pl.cy, ROSSO, 3)
    s += linea(pl.cx, pl.cy, px, py, GRIGIO, 2.5)
    s += arco_angolo(pl.cx, pl.cy, 36, 0, a)
    s += testo(pl.cx + 50, pl.cy - 13, "α", ARANCIO, 18, math_=True)
    s += testo((pl.cx + px) / 2, py - 14, pedice("x", "P"), BLU, 18, math_=True)
    s += testo(px + 20, (py + pl.cy) / 2, pedice("y", "P"), ROSSO, 18, math_=True)
    s += punto(px, py)
    s += testo(px + 12, py - 16, "P (0,8 ; 0,6)", dim=16, ancora="start")
    s += punto(*pl.p(0, 1)) + testo(pl.cx + 12, pl.cy - pl.r - 14, "(0, 1)", dim=15, ancora="start")
    s += punto(*pl.p(1, 0)) + testo(pl.cx + pl.r + 8, pl.cy + 18, "(1, 0)", dim=15, ancora="start")
    return svg(520, 420, s)


def gonio_triangolo():
    x0, y0, x1, y1 = 40, 180, 300, 40
    s = linea(x0, y0, x1, y0, BLU, 3) + linea(x1, y0, x1, y1, ROSSO, 3) + linea(x0, y0, x1, y1, GRIGIO, 2.5)
    s += angolo_retto(x1, y0, -1, -1)
    s += arco_angolo(x0, y0, 38, 0, math.atan2(y0 - y1, x1 - x0))
    s += testo(x0 + 52, y0 - 12, "α", ARANCIO, 18, math_=True)
    s += testo((x0 + x1) / 2, y0 + 22, pedice("x", "P"), BLU, 18, math_=True)
    s += testo(x1 + 24, (y0 + y1) / 2, pedice("y", "P"), ROSSO, 18, math_=True)
    s += testo((x0 + x1) / 2 - 16, (y0 + y1) / 2 - 16, "1", dim=18, math_=True)
    s += punto(x1, y1) + testo(x1 + 4, y1 - 14, "P", dim=16)
    return svg(360, 220, s)


def gonio_tangente():
    pl = Piano(200, 200, 130)
    a = math.radians(32)
    px, py = pl.p(math.cos(a), math.sin(a))
    tx, ty = pl.p(1, math.tan(a))
    s = pl.assi() + pl.cerchio()
    s += linea(pl.cx + pl.r, pl.cy + pl.r * 0.9, pl.cx + pl.r, pl.cy - pl.r * 1.05, GRIGIO, 1.5)
    s += linea(pl.cx, pl.cy, *pl.p(1.45 * math.cos(a), 1.45 * math.sin(a)), GRIGIO, 1.5)
    s += linea(pl.cx, pl.cy, px, py, GRIGIO, 2.5)
    s += linea(pl.cx, pl.cy, px, pl.cy, BLU, 3)
    s += linea(px, py, px, pl.cy, ROSSO, 3)
    s += linea(tx, pl.cy, tx, ty, VERDE, 3.5)
    s += arco_angolo(pl.cx, pl.cy, 30, 0, a)
    s += testo(pl.cx + 42, pl.cy - 10, "α", ARANCIO, 17, math_=True)
    s += testo((pl.cx + px) / 2, pl.cy + 18, "cos(α)", BLU, 15)
    s += testo(px - 30, py + 4, "sin α", ROSSO, 15)
    s += testo(tx + 40, (pl.cy + ty) / 2, "tan(α)", VERDE, 15)
    s += punto(px, py) + testo(px - 8, py - 14, "P", dim=15)
    s += testo(pl.cx + 12, pl.cy - pl.r - 14, "(0, 1)", dim=14, ancora="start")
    s += testo(pl.cx + pl.r + 8, pl.cy + 18, "(1, 0)", dim=14, ancora="start")
    return svg(420, 400, s)


def gonio_limiti():
    pl = Piano(210, 200, 130)
    s = pl.assi() + pl.cerchio()
    s += linea(*pl.p(0, -1), *pl.p(0, 1), ARANCIO, 3.5)
    s += linea(*pl.p(-1, 0), *pl.p(1, 0), VERDE, 3.5)
    for (x, y), col, t, dx, dy in [((0, 1), BLU, "(0, 1)", 34, -14), ((0, -1), ROSSO, "(0, −1)", 36, 16),
                                   ((1, 0), VERDE, "(1, 0)", 34, -14), ((-1, 0), VIOLA, "(−1, 0)", -36, -14)]:
        X, Y = pl.p(x, y)
        s += punto(X, Y, col, 5) + testo(X + dx, Y + dy, t, col, 15)
    return svg(420, 400, s)


def gonio_angolo_valore(gradi):
    pl = Piano(140, 130, 90)
    s = pl.assi(0.3) + pl.cerchio()
    if gradi == 0:
        s += linea(pl.cx, pl.cy, pl.cx + pl.r, pl.cy, BLU, 3.5)
        s += testo(pl.cx + pl.r / 2, pl.cy + 16, "1", BLU, 16)
        s += testo(pl.cx - 14, pl.cy - 16, "0", ROSSO, 16)
        s += testo(pl.cx + pl.r + 16, pl.cy - 16, "0", VERDE, 16)
    else:
        a = math.radians(gradi)
        px, py = pl.p(math.cos(a), math.sin(a))
        tx, ty = pl.p(1, math.tan(a))
        s += linea(pl.cx, pl.cy, tx, ty, ARANCIO, 2.5)
        s += linea(pl.cx, pl.cy, px, pl.cy, BLU, 3.5)
        s += linea(px, py, px, pl.cy, ROSSO, 3.5)
        s += linea(tx, pl.cy, tx, ty, VERDE, 3.5)
        s += arco_angolo(pl.cx, pl.cy, 26, 0, a)
        s += testo(pl.cx + 38, pl.cy - 9, f"{gradi}°", ARANCIO, 13)
        s += testo((pl.cx + px) / 2, pl.cy + 18, "√3/2", BLU, 15)
        s += testo(px + 14, pl.cy - 12, "1/2", ROSSO, 14, ancora="start")
        s += testo(tx + 8, ty - 8, "√3/3", VERDE, 15, ancora="start")
    return svg(300, 260, s)


def gonio_archi_associati():
    pl = Piano(230, 210, 150)
    a = math.radians(30)
    s = pl.assi() + pl.cerchio()
    raggi = [(a, ARANCIO, None, "α"), (PI - a, VERDE, "6 5", "π − α"),
             (PI + a, BLU, "6 5", "π + α"), (2 * PI - a, ROSSO, "6 5", "2π − α")]
    for ang, col, tr, etichetta in raggi:
        s += linea(pl.cx, pl.cy, *pl.p(1.0 * math.cos(ang), 1.0 * math.sin(ang)), col, 2.5, tr)
        lx, ly = pl.p(1.22 * math.cos(ang), 1.22 * math.sin(ang))
        s += testo(lx, ly, etichetta, col, 17, math_=True)
    # piccoli archi che mostrano l'angolo α rispetto all'asse x
    s += arco_angolo(pl.cx, pl.cy, 40, 0, a, ARANCIO)
    s += arco_angolo(pl.cx, pl.cy, 40, PI - a, PI, VERDE)
    s += arco_angolo(pl.cx, pl.cy, 40, PI, PI + a, BLU)
    s += arco_angolo(pl.cx, pl.cy, 40, 2 * PI - a, 2 * PI, ROSSO)
    return svg(470, 420, s)


def gonio_supplementari():
    pl = Piano(230, 190, 150)
    a = math.radians(32)
    px, py = pl.p(math.cos(a), math.sin(a))
    qx, qy = pl.p(-math.cos(a), math.sin(a))
    s = pl.assi() + pl.cerchio()
    s += linea(pl.cx, pl.cy, px, py, ARANCIO, 2.5)
    s += linea(pl.cx, pl.cy, qx, qy, VERDE, 2.5, "6 5")
    s += linea(px, py, px, pl.cy, ROSSO, 3) + linea(qx, qy, qx, pl.cy, ROSSO, 3)
    s += linea(pl.cx, pl.cy, px, pl.cy, BLU, 3) + linea(pl.cx, pl.cy, qx, pl.cy, BLU, 3)
    s += arco_angolo(pl.cx, pl.cy, 34, 0, a)
    s += arco_angolo(pl.cx, pl.cy, 34, PI - a, PI, VERDE)
    s += arco_angolo(pl.cx, pl.cy, 22, 0, PI - a, GRIGIO, 1.5)
    s += testo(pl.cx + 46, pl.cy - 10, "α", ARANCIO, 17, math_=True)
    s += testo(pl.cx - 46, pl.cy - 10, "α", VERDE, 17, math_=True)
    s += testo(pl.cx - 6, pl.cy - 48, "π − α", GRIGIO, 15, math_=True)
    s += testo(px + 34, (py + pl.cy) / 2, "sin α", ROSSO, 15)
    s += testo(qx - 34, (qy + pl.cy) / 2, "sin α", ROSSO, 15)
    s += testo((pl.cx + px) / 2, pl.cy + 18, "cos α", BLU, 15)
    s += testo((pl.cx + qx) / 2, pl.cy + 18, "−cos α", BLU, 15)
    return svg(470, 390, s)


def gonio_angolo_giro():
    pl = Piano(210, 190, 140)
    a = math.radians(30)
    px, py = pl.p(math.cos(a), math.sin(a))
    s = pl.assi() + pl.cerchio()
    s += linea(pl.cx, pl.cy, px, py, ARANCIO, 2.5)
    s += linea(pl.cx, pl.cy, px, pl.cy, BLU, 3) + linea(px, py, px, pl.cy, ROSSO, 3)
    # spirale: un giro completo più l'angolo α
    punti = []
    for i in range(121):
        t = (2 * PI + a) * i / 120
        rr = 16 + 9 * t / (2 * PI + a)
        punti.append((pl.cx + rr * math.cos(t), pl.cy - rr * math.sin(t)))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punti)
    s += f'<path d="{d}" fill="none" stroke="{GRIGIO}" stroke-width="1.8" marker-end="url(#f{GRIGIO[1:]})"/>'
    s += testo(pl.cx + 38, pl.cy - 8, "α", ARANCIO, 16, math_=True)
    s += testo(pl.cx - 4, pl.cy + 46, "2π + α", GRIGIO, 15, math_=True)
    s += testo(px + 32, (py + pl.cy) / 2, "sin α", ROSSO, 15)
    s += testo((pl.cx + px) / 2 + 10, pl.cy + 18, "cos α", BLU, 14)
    return svg(430, 380, s)


def genera_goniometria():
    figure = {
        "goniometria-circonferenza.svg": gonio_circonferenza(),
        "goniometria-triangolo.svg": gonio_triangolo(),
        "goniometria-tangente.svg": gonio_tangente(),
        "goniometria-limiti.svg": gonio_limiti(),
        "goniometria-angolo-0.svg": gonio_angolo_valore(0),
        "goniometria-angolo-30.svg": gonio_angolo_valore(30),
        "goniometria-archi-associati.svg": gonio_archi_associati(),
        "goniometria-supplementari.svg": gonio_supplementari(),
        "goniometria-angolo-giro.svg": gonio_angolo_giro(),
    }
    t3 = tick_pi_mezzi(6)
    yt = [(1, "1"), (-1, "−1")]
    figure["goniometria-grafico-sin.svg"] = grafico(
        math.sin, -0.9, 3 * PI + 1.2, -1.3, 1.4, solido=(0, 3 * PI), colore=ROSSO,
        tick_x=t3, tick_y=yt, nome="sin(x)", nome_pos=(140, 26))
    figure["goniometria-grafico-cos.svg"] = grafico(
        math.cos, -0.9, 3 * PI + 1.2, -1.3, 1.4, solido=(0, 3 * PI), colore=BLU,
        tick_x=t3, tick_y=yt, nome="cos(x)", nome_pos=(120, 26))
    figure["goniometria-grafico-tan.svg"] = grafico(
        math.tan, -0.9, 3 * PI + 0.6, -3.2, 3.2, solido=(0, 3 * PI), colore=VERDE,
        tick_x=t3, tick_y=[(1, "1"), (-1, "−1")], nome="tan(x)", nome_pos=(150, 26),
        asintoti=(PI / 2, 3 * PI / 2, 5 * PI / 2), altezza=300)

    t2 = tick_pi_mezzi(4)
    base = dict(xmin=-1.0, xmax=2 * PI + 1.6, solido=(0, 2 * PI), colore=ROSSO, tick_x=t2, larghezza=560)
    figure["goniometria-sin-base.svg"] = grafico(
        math.sin, ymin=-1.4, ymax=1.4, tick_y=yt, nome="y = sin x", nome_pos=(470, 30), **base)
    figure["goniometria-sin-meno-1.svg"] = grafico(
        lambda x: math.sin(x) - 1, ymin=-2.3, ymax=0.6, tick_y=[(-1, "−1"), (-2, "−2")],
        nome="y = sin x − 1", nome_pos=(460, 30), **base)
    figure["goniometria-sin-piu-1.svg"] = grafico(
        lambda x: math.sin(x) + 1, ymin=-0.6, ymax=2.3, tick_y=[(1, "1"), (2, "2")],
        nome="y = sin x + 1", nome_pos=(460, 30), **base)
    figure["goniometria-2sin.svg"] = grafico(
        lambda x: 2 * math.sin(x), ymin=-2.4, ymax=2.4, tick_y=[(2, "2"), (1, "1"), (-1, "−1"), (-2, "−2")],
        nome="y = 2 sin x", nome_pos=(470, 30), altezza=300, **base)
    figure["goniometria-sin-x-meno-pi2.svg"] = grafico(
        lambda x: math.sin(x - PI / 2), ymin=-1.4, ymax=1.4, tick_y=yt,
        nome="y = sin(x − π/2)", nome_pos=(450, 30), **base)
    figure["goniometria-sin-x-piu-pi2.svg"] = grafico(
        lambda x: math.sin(x + PI / 2), ymin=-1.4, ymax=1.4, tick_y=yt,
        nome="y = sin(x + π/2)", nome_pos=(450, 30), **base)
    figure["goniometria-sin-2x.svg"] = grafico(
        lambda x: math.sin(2 * x), ymin=-1.4, ymax=1.4, tick_y=yt, nome="y = sin(2x)",
        nome_pos=(470, 30), **{**base, "solido": (0, PI)})
    figure["goniometria-sin-x-mezzi.svg"] = grafico(
        lambda x: math.sin(x / 2), -1.0, 4 * PI + 1.2, -1.4, 1.4, solido=(0, 4 * PI), colore=ROSSO,
        tick_x=tick_pi_mezzi(8), tick_y=yt, nome="y = sin(x/2)", nome_pos=(560, 30), larghezza=680)
    tick_es = [(-PI / 6, "−π/6", ROSSO), (PI / 6, "π/6", ROSSO)] + [
        (k * PI / 2, etichetta_multiplo_pi_mezzi(k), None) for k in range(1, 5)]
    figure["goniometria-esempio-2sin.svg"] = grafico(
        lambda x: 2 * math.sin(x + PI / 6) - 1, -1.2, 2 * PI + 1.4, -3.4, 1.6, solido=(-PI / 6, 11 * PI / 6),
        colore=ROSSO, tick_x=tick_es, tick_y=[(1, "1"), (-1, "−1"), (-2, "−2"), (-3, "−3")],
        nome="y = 2 sin(x + π/6) − 1", nome_pos=(560, 30), larghezza=760, altezza=300)
    return figure


# ============================================================== ONDE

def onde_proiezione():
    pl = Piano(210, 200, 130)
    a = math.radians(40)
    px, py = pl.p(math.cos(a), math.sin(a))
    s = pl.assi() + pl.cerchio()
    s += linea(pl.cx, pl.cy, px, py, ARANCIO, 2.8, freccia=True)
    s += linea(px, py, px, pl.cy, GRIGIO, 1.5, "4 4")
    s += linea(pl.cx, pl.cy, px, pl.cy, BLU, 3.5)
    s += arco_angolo(pl.cx, pl.cy, 30, 0, a, VERDE)
    s += testo(pl.cx + 44, pl.cy - 12, "φ", VERDE, 18, math_=True)
    s += testo((pl.cx + px) / 2 - 18, (pl.cy + py) / 2 - 8, "r⃗", ARANCIO, 19, math_=True)
    # freccia curva dalla proiezione all'etichetta r cos φ
    s += (f'<path d="M{pl.cx + 50},{pl.cy + 16} C{pl.cx + 110},{pl.cy + 90} {pl.cx + 270},{pl.cy + 10} '
          f'{pl.cx + 330},{pl.cy - 120}" fill="none" stroke="{BLU}" stroke-width="2" '
          f'marker-end="url(#f{BLU[1:]})"/>')
    s += testo(pl.cx + 360, pl.cy - 140, "r cos φ", GRIGIO, 18, math_=True)
    return svg(640, 400, s)


def onde_vettori(tipo):
    pl = Piano(200, 200, 130)
    a = math.radians(40)
    px, py = pl.p(math.cos(a), math.sin(a))
    s = pl.assi() + pl.cerchio()
    s += linea(px, py, px, pl.cy, GRIGIO, 1.5, "4 4")
    s += linea(pl.cx, pl.cy, px, pl.cy, BLU, 3.5)
    s += arco_angolo(pl.cx, pl.cy, 30, 0, a, VERDE)
    s += testo(pl.cx + 44, pl.cy - 12, "φ", VERDE, 18, math_=True)
    L = 110
    if tipo == "velocita":
        s += linea(pl.cx, pl.cy, px, py, ARANCIO, 2.5)
        tx, ty = -math.sin(a), -math.cos(a)  # verso tangente (antiorario), y schermo invertita
        ex, ey = px + tx * L, py + ty * L
        s += linea(px, py, ex, ey, ROSSO, 3, freccia=True)
        s += linea(px, py, ex, py, ROSA, 2.5, freccia=True)
        s += linea(ex, py, ex, ey, ROSA, 1.8, "4 4")
        s += testo(ex + 30, ey - 4, pedice("v⃗", "t"), ROSSO, 19, math_=True)
        s += testo((px + ex) / 2, py + 16, "v", ROSA, 17, math_=True)
        s += testo(pl.cx + 40, (pl.cy + py) / 2 - 18, "r⃗", ARANCIO, 18, math_=True)
        return svg(420, 400, s)
    s += linea(pl.cx, pl.cy, px, py, ARANCIO, 2.5)
    ex, ey = px - math.cos(a) * L * 0.8, py + math.sin(a) * L * 0.8
    s += linea(px, py, ex, ey, ROSSO, 3, freccia=True)
    s += linea(px, py, ex, py, ROSA, 2.5, freccia=True)
    s += linea(ex, py, ex, ey, ROSA, 1.8, "4 4")
    s += testo(px + 22, py - 10, pedice("a⃗", "c"), ROSSO, 19, math_=True)
    s += testo((px + ex) / 2, py - 14, "a", ROSA, 17, math_=True)
    return svg(420, 400, s)


def genera_onde():
    return {
        "onde-proiezione.svg": onde_proiezione(),
        "onde-velocita.svg": onde_vettori("velocita"),
        "onde-accelerazione.svg": onde_vettori("accelerazione"),
        "onde-onda-armonica.svg": grafico(
            math.sin, -1.6, 4 * PI + 1.2, -1.45, 1.45, solido=(0, 4 * PI), colore=ROSSO,
            tick_y=[(1, "A"), (-1, "−A")], linee_y=((1, GRIGIO), (-1, GRIGIO)),
            etichetta_x="t", larghezza=640),
    }


# ================================================== PROBABILITÀ

def prob_disintegrazione():
    x0, y0, w, h = 30, 40, 400, 240
    mx, my = x0 + w / 2, y0 + h / 2
    s = ""
    for (x, y, col, nome, lx, ly) in [
        (x0, y0, ROSSO, "H₁", x0 + 22, y0 + 26), (mx, y0, BLU, "H₂", x0 + w - 24, y0 + 26),
        (x0, my, VIOLA, "H₃", x0 + 22, y0 + h - 20), (mx, my, ARANCIO, "H₄", x0 + w - 24, y0 + h - 20)]:
        s += (f'<rect x="{x}" y="{y}" width="{w / 2}" height="{h / 2}" fill="{col}" fill-opacity="0.28" '
              f'stroke="{GRIGIO}" stroke-width="2"/>')
        s += testo(lx, ly, nome, col, 18, math_=True, grassetto=True)
    s += (f'<ellipse cx="{mx}" cy="{my}" rx="150" ry="62" transform="rotate(-18 {mx} {my})" '
          f'fill="{VERDE}" fill-opacity="0.35" stroke="{GRIGIO}" stroke-width="2.5"/>')
    s += testo(mx + 60, my - 78, "A", GRIGIO, 18, math_=True, grassetto=True)
    for dx, dy, t in [(-62, -14, "A ∩ H₁"), (58, -40, "A ∩ H₂"), (-72, 30, "A ∩ H₃"), (52, 16, "A ∩ H₄")]:
        s += testo(mx + dx, my + dy, t, VERDE, 15, math_=True)
    s += testo(x0 + w + 14, y0 - 14, "Ω", GRIGIO, 20, math_=True)
    return svg(470, 300, s)


def prob_bersagli():
    def bersaglio(cx, cy, colpi):
        anelli = [(150, "#e5e7eb"), (120, "#111827"), (92, "#0ea5e9"), (62, "#ef4444"), (34, "#f59e0b")]
        b = ""
        for r, col in anelli:
            b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="{GRIGIO}" stroke-width="1"/>'
        for x, y in colpi:
            X, Y, d = cx + x, cy + y, 7
            b += linea(X - d, Y - d, X + d, Y + d, "#6b7280", 3) + linea(X - d, Y + d, X + d, Y - d, "#6b7280", 3)
        return b
    s = bersaglio(170, 170, [(-48, -28), (-42, 0), (8, 30), (36, -50), (52, 20)])
    s += bersaglio(520, 170, [(-90, -132), (0, -78), (-104, 0), (104, 0), (128, 48), (0, 136)])
    return svg(690, 340, s)


def prob_albero():
    xs = [70, 150, 290, 450, 590]
    s = ""
    for i, t in enumerate(["1° lancio", "2° lancio", "3° lancio", "4° lancio"]):
        s += linea(xs[i], 40, xs[i], 760, ROSSO, 1, "4 4")
        s += testo(xs[i], 22, t, ROSSO, 14)
    # nodi: livello -> lista di (y, percorso)
    livelli = [[(400, "")]]
    passo = [180, 100, 52, 28]
    for l in range(4):
        nuovi = []
        for y, p in livelli[-1]:
            nuovi.append((y - passo[l], p + "T"))
            nuovi.append((y + passo[l], p + "C"))
        livelli.append(nuovi)
    evidenziati = {"TTTC": VIOLA, "TTCT": ROSA, "TCTT": "#a3a30b", "CTTT": BLU}
    # tratti evidenziati sotto, rami sopra
    for percorso, col in evidenziati.items():
        punti = [(xs[0], 400)]
        y = 400
        for l, c in enumerate(percorso):
            y = y - passo[l] if c == "T" else y + passo[l]
            punti.append((xs[l + 1], y))
        d = "M" + " L".join(f"{x},{y}" for x, y in punti)
        s += f'<path d="{d}" fill="none" stroke="{col}" stroke-width="11" stroke-opacity="0.55" stroke-linejoin="round"/>'
        s += testo(xs[4] + 14, punti[-1][1], "p · p · p · q", GRIGIO, 17, ancora="start", math_=True)
    for l in range(4):
        for y, p in livelli[l]:
            for yy, pp in livelli[l + 1]:
                if pp[:-1] == p:
                    s += linea(xs[l], y, xs[l + 1], yy, GRIGIO, 1.6)
                    col = VERDE if pp[-1] == "T" else ARANCIO
                    s += testo((xs[l] + xs[l + 1]) / 2 + 6, (y + yy) / 2 + (-10 if pp[-1] == "T" else 12),
                               pp[-1], col, 13)
    return svg(740, 780, s)


def gauss(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * PI)


def prob_normale(da, a, tick, larghezza=300, altezza=170, nome=None):
    """Curva normale standard con area ombreggiata tra da e a (±4 = infinito)."""
    mx, my = 16, 26
    xmin, xmax, ymax = -3.6, 3.6, 0.45
    sx = (larghezza - 2 * mx) / (xmax - xmin)
    sy = (altezza - my - 14) / ymax

    def P(x, y):
        return mx + (x - xmin) * sx, altezza - my - y * sy

    x0, y0 = P(0, 0)
    s = linea(mx - 6, y0, larghezza - mx + 6, y0, freccia=True)
    s += linea(x0, y0 + 4, x0, 10, freccia=True)
    a1, a2 = max(da, xmin), min(a, xmax)
    punti = [P(a1, 0)] + [P(a1 + (a2 - a1) * i / 120, gauss(a1 + (a2 - a1) * i / 120)) for i in range(121)] + [P(a2, 0)]
    s += '<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in punti) + f' Z" fill="{BLU}" fill-opacity="0.35"/>'
    curva = [P(xmin + (xmax - xmin) * i / 200, gauss(xmin + (xmax - xmin) * i / 200)) for i in range(201)]
    s += '<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in curva) + f'" fill="none" stroke="{ARANCIO}" stroke-width="2.4"/>'
    for v, t in tick:
        px, _ = P(v, 0)
        s += linea(px, y0 - 4, px, y0 + 4)
        s += linea(px, y0, px, P(v, gauss(v))[1], GRIGIO, 1.2, "3 3")
        s += testo(px, y0 + 15, t, dim=13)
    if nome:
        nome = nome.replace("<", "&lt;")
        s += testo(6, 12, nome, BLU, 14, ancora="start", math_=True)
    return svg(larghezza, altezza, s)


def genera_probabilita():
    inf = 4.5
    return {
        "probabilita-disintegrazione.svg": prob_disintegrazione(),
        "probabilita-bersagli.svg": prob_bersagli(),
        "probabilita-albero.svg": prob_albero(),
        "probabilita-phi.svg": prob_normale(-inf, 0.8, [(0.8, "x = z")], larghezza=460, altezza=230,
                                            nome="Area = Probabilità = Φ(z)"),
        "probabilita-normale-a.svg": prob_normale(-inf, 1, [(1, "1")], nome="p(Z < 1)"),
        "probabilita-normale-b.svg": prob_normale(0, 1.5, [(0, "0"), (1.5, "1,5")], nome="p(0 < Z < 1,5)"),
        "probabilita-normale-c.svg": prob_normale(0.75, inf, [(0.75, "0,75")], nome="p(Z > 0,75)"),
        "probabilita-normale-d.svg": prob_normale(-inf, -0.75, [(-0.75, "−0,75")], nome="p(Z < −0,75)"),
        "probabilita-normale-e.svg": prob_normale(-1, inf, [(-1, "−1")], nome="p(Z > −1)"),
        "probabilita-normale-f.svg": prob_normale(-1.75, -0.5, [(-1.75, "−1,75"), (-0.5, "−0,5")],
                                                  nome="p(−1,75 < Z < −0,5)"),
    }


# ============================================= FISICA 5SCI

BIANCO = "#c4c9d4"


def rett(x, y, w, h, bordo=GRIGIO, riemp="none", opacita=1, spessore=2):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{riemp}" fill-opacity="{opacita}" '
            f'stroke="{bordo}" stroke-width="{spessore}"/>')


def ellisse(cx, cy, rx, ry, colore=GRIGIO, spessore=2, tratteggio=None, riemp="none", opacita=1):
    tr = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{riemp}" fill-opacity="{opacita}" '
            f'stroke="{colore}" stroke-width="{spessore}"{tr}/>')


def percorso(d, colore=GRIGIO, spessore=2, tratteggio=None, freccia=False):
    tr = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    fr = f' marker-end="url(#f{colore[1:]})"' if freccia else ""
    return f'<path d="{d}" fill="none" stroke="{colore}" stroke-width="{spessore}"{tr}{fr}/>'


def punta(x, y, angolo_gradi, colore, lato=8):
    """Punta di freccia isolata in (x,y), orientata di angolo_gradi (0 = verso destra)."""
    a = math.radians(angolo_gradi)
    p1 = (x - lato * math.cos(a - 0.45), y - lato * math.sin(a - 0.45))
    p2 = (x - lato * math.cos(a + 0.45), y - lato * math.sin(a + 0.45))
    return (f'<path d="M{x:.1f},{y:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z" '
            f'fill="{colore}"/>')


def uscente(x, y, colore=VERDE, r=9):
    """Simbolo ⊙ (vettore uscente dal foglio)."""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{colore}" stroke-width="2"/>'
            + punto(x, y, colore, 2.5))


def ondina(x1, y1, x2, y2, colore=ROSSO, ampiezza=6, onde=6, freccia=True):
    """Linea ondulata (un fotone / un'onda) da (x1,y1) a (x2,y2)."""
    lung = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / lung, (y2 - y1) / lung
    nx, ny = -uy, ux
    punti = []
    for i in range(121):
        t = i / 120
        o = ampiezza * math.sin(2 * PI * onde * t) * (1 if t < 0.9 else (1 - t) / 0.1)
        punti.append((x1 + ux * lung * t + nx * o, y1 + uy * lung * t + ny * o))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punti)
    return percorso(d, colore, 2.2, freccia=freccia)


def carica(x, y, segno, colore):
    return (f'<circle cx="{x}" cy="{y}" r="8" fill="none" stroke="{colore}" stroke-width="2"/>'
            + testo(x, y + 1, segno, colore, 13, grassetto=True))


# ---------------------------------------- 0: ripasso campo magnetico

def f5_magnete_taglio():
    def magnete(x, w, y=30, h=46):
        return (rett(x, y, w, h, ROSSO, ROSSO, 0.85) + rett(x + w, y, w, h, BLU, BLU, 0.85)
                + testo(x + w / 2, y + h / 2, "N", "#fff", 18, grassetto=True)
                + testo(x + 1.5 * w, y + h / 2, "S", "#fff", 18, grassetto=True))
    s = magnete(30, 110) + linea(140, 16, 140, 92, BIANCO, 2, "5 4")
    s += linea(270, 53, 330, 53, GRIGIO, 2.5, freccia=True)
    s += magnete(350, 55) + magnete(480, 55)
    return svg(610, 106, s)


def f5_filo_campo():
    s = ellisse(160, 200, 120, 34, BIANCO, 1.6, "5 5")
    s += linea(160, 300, 160, 20, ARANCIO, 3, freccia=True) + testo(176, 50, "i", ARANCIO, 18, math_=True)
    px, py = 160 + 120 * math.cos(math.radians(60)), 200 + 34 * math.sin(math.radians(60))
    s += linea(160, 200, px, py, BIANCO, 1.5, "4 4") + testo((160 + px) / 2 + 6, (200 + py) / 2 - 12, "d", dim=17, math_=True)
    s += linea(px, py, px + 80, py - 14, VERDE, 3, freccia=True) + testo(px + 64, py + 16, "B⃗", VERDE, 18, math_=True)
    return svg(330, 320, s)


def f5_spira():
    s = linea(30, 170, 430, 170, BIANCO, 1.5, "5 5")
    s += ellisse(140, 170, 46, 125, ARANCIO, 3)
    s += linea(140, 170, 140, 45, BIANCO, 1.5, "4 4") + testo(154, 108, "R", dim=17, math_=True)
    s += punto(330, 170, BIANCO) + linea(330, 170, 400, 170, VERDE, 3, freccia=True)
    s += testo(372, 194, "B⃗", VERDE, 18, math_=True) + testo(236, 188, "r", dim=17, math_=True)
    s += punta(108, 78, 125, ARANCIO, 11) + testo(84, 60, "i", ARANCIO, 18, math_=True)
    return svg(450, 320, s)


def f5_solenoide():
    s = ""
    for k, h in [(1, 70), (2, 120)]:
        s += percorso(f"M330,{170 - 22 - 4 * k} C300,{170 - h} 200,{170 - h} 170,{170 - 22 - 4 * k}", VERDE, 1.6)
        s += percorso(f"M330,{170 + 22 + 4 * k} C300,{170 + h} 200,{170 + h} 170,{170 + 22 + 4 * k}", VERDE, 1.6)
        s += punta(250, 170 - 0.75 * h - 2.2 * k + 4, 0, VERDE, 9) + punta(250, 170 + 0.75 * h + 2.2 * k - 4, 0, VERDE, 9)
    for y in (152, 170, 188):
        s += linea(30, y, 470, y, VERDE, 1.6)
        for x in (80, 250, 420):
            s += punta(x, y, 180, VERDE, 9)
    s += rett(180, 136, 140, 68, BIANCO, "none", 1, 1.8)
    s += ellisse(180, 170, 12, 34, BIANCO, 1.8) + ellisse(320, 170, 12, 34, BIANCO, 1.8)
    return svg(500, 340, s)


def f5_due_fili():
    s = ellisse(160, 210, 130, 34, BIANCO, 1.5, "5 5")
    s += linea(160, 320, 160, 30, ARANCIO, 3, freccia=True) + testo(176, 60, pedice("i", "1"), ARANCIO, 17, math_=True)
    s += linea(290, 320, 290, 30, ARANCIO, 3, freccia=True) + testo(306, 60, pedice("i", "2"), ARANCIO, 17, math_=True)
    s += testo(160, 18, "filo 1", ARANCIO, 14) + testo(290, 18, "filo 2", ARANCIO, 14)
    s += linea(160, 210, 290, 222, BIANCO, 1.4, "4 4") + testo(222, 204, "d", dim=16, math_=True)
    s += linea(290, 222, 360, 212, VERDE, 3, freccia=True) + testo(352, 236, "B⃗", VERDE, 17, math_=True)
    s += linea(290, 170, 220, 170, ROSSO, 3, freccia=True) + testo(250, 152, "F⃗", ROSSO, 17, math_=True)
    return svg(420, 330, s)


def f5_circuitazione():
    s = ""
    for y in range(40, 221, 30):
        s += linea(20, y, 330, y, VERDE, 1.6) + punta(300, y, 0, VERDE, 9)
    s += (f'<ellipse cx="150" cy="130" rx="55" ry="95" transform="rotate(25 150 130)" fill="none" '
          f'stroke="{ARANCIO}" stroke-width="3"/>')
    s += testo(70, 40, "𝓛", ARANCIO, 22, math_=True)
    s += linea(196, 170, 176, 200, ROSSO, 3, freccia=True) + testo(206, 206, "Δℓ⃗", ROSSO, 16, math_=True)
    s += arco_angolo(196, 170, 18, -0.98, 0, BLU) + testo(226, 176, "θ", BLU, 16, math_=True)
    # destra: correnti concatenate e non
    s += ellisse(500, 200, 80, 26, BIANCO, 2) + ellisse(600, 110, 60, 22, BIANCO, 2)
    s += linea(500, 290, 500, 30, ARANCIO, 3, freccia=True) + testo(514, 52, "i", ARANCIO, 17, math_=True)
    s += testo(410, 200, pedice("𝓛", "1"), dim=18, math_=True) + testo(600, 74, pedice("𝓛", "2"), dim=18, math_=True)
    return svg(700, 300, s)


def f5_moto_circolare():
    s = f'<circle cx="150" cy="190" r="110" fill="none" stroke="{ROSSO}" stroke-width="2" stroke-dasharray="6 5"/>'
    s += linea(150, 190, 150, 80, BIANCO, 1.4, "4 4") + testo(164, 140, "R", dim=17, math_=True)
    s += punto(150, 190, BIANCO, 3)
    s += f'<circle cx="150" cy="80" r="11" fill="{BIANCO}" fill-opacity="0.35" stroke="{BIANCO}" stroke-width="2"/>'
    s += testo(126, 66, "q, m", dim=15)
    s += linea(161, 80, 240, 80, BIANCO, 3, freccia=True) + testo(232, 62, "v⃗", dim=17, math_=True)
    s += linea(150, 92, 150, 140, BLU, 3, freccia=True) + testo(172, 120, pedice("F⃗", "L"), BLU, 16, math_=True)
    s += uscente(300, 60) + testo(326, 60, "B⃗", VERDE, 18, math_=True)
    return svg(360, 320, s)


def f5_selettore():
    s = rett(60, 40, 340, 22, BIANCO) + testo(74, 51, "−", dim=18) + rett(60, 238, 340, 22, BIANCO) + testo(74, 249, "+", dim=18)
    s += linea(370, 236, 370, 66, ROSSO, 3, freccia=True) + testo(388, 150, "E⃗", ROSSO, 18, math_=True)
    s += carica(180, 150, "−", BIANCO)
    s += linea(190, 150, 260, 150, BIANCO, 2.5, freccia=True) + testo(250, 134, "v⃗", dim=16, math_=True)
    s += linea(180, 140, 180, 92, BLU, 3, freccia=True) + testo(156, 104, pedice("F", "L"), BLU, 16, math_=True)
    s += linea(180, 160, 180, 208, ARANCIO, 3, freccia=True) + testo(204, 200, pedice("F", "e"), ARANCIO, 16, math_=True)
    s += uscente(250, 96) + testo(272, 88, "B⃗", VERDE, 17, math_=True)
    return svg(440, 290, s)


# ------------------------------------------ 1: elettromagnetismo

def f5_barretta():
    s = rett(180, 60, 340, 140, ARANCIO, ARANCIO, 0.22, 0)
    s += linea(150, 60, 520, 60, ARANCIO, 3) + linea(150, 200, 520, 200, ARANCIO, 3) + linea(520, 60, 520, 200, ARANCIO, 3)
    s += rett(130, 40, 50, 180, BIANCO, "#1b1e26", 1, 2)
    for x, y in [(145, 56), (165, 56), (145, 74), (165, 74)]:
        s += carica(x, y, "−", BLU)
    for x, y in [(145, 186), (165, 186), (145, 204), (165, 204)]:
        s += carica(x, y, "+", ROSSO)
    s += linea(180, 130, 260, 130, BIANCO, 2.5, freccia=True) + testo(248, 114, "v⃗", dim=17, math_=True)
    s += uscente(70, 70) + testo(70, 42, "B⃗", VERDE, 17, math_=True)
    s += linea(555, 60, 555, 200, BIANCO, 1.5) + linea(548, 60, 562, 60, BIANCO, 1.5) + linea(548, 200, 562, 200, BIANCO, 1.5)
    s += testo(572, 130, "ℓ", dim=18, math_=True)
    s += punta(360, 60, 180, ARANCIO, 11) + punta(520, 130, -90, ARANCIO, 11) + punta(360, 200, 0, ARANCIO, 11)
    s += testo(360, 40, "i", ARANCIO, 16, math_=True)
    s += testo(360, 160, "superficie S che diminuisce", ARANCIO, 14)
    return svg(600, 240, s)


def f5_lenz():
    def pannello(dx, giusto):
        s = rett(dx + 125, 20, 50, 40, BLU, BLU, 0.85) + testo(dx + 150, 40, "S", "#fff", 16, grassetto=True)
        s += rett(dx + 125, 60, 50, 40, ROSSO, ROSSO, 0.85) + testo(dx + 150, 80, "N", "#fff", 16, grassetto=True)
        s += linea(dx + 200, 30, dx + 200, 92, ARANCIO, 2.5, freccia=True)
        s += testo(dx + 232, 40, "si avvicina", ARANCIO, 13, ancora="start")
        for x in (dx + 132, dx + 150, dx + 168):
            s += linea(x, 102, x, 290, VERDE, 2) + punta(x, 240, 90, VERDE, 9)
        s += ellisse(dx + 150, 205, 120, 30, BIANCO, 2.5)
        col = VIOLA if not giusto else ARANCIO
        for x in (dx + 60, dx + 240):
            if giusto:
                s += linea(x, 270, x, 140, col, 2.2, freccia=True)
            else:
                s += linea(x, 140, x, 270, col, 2.2, freccia=True)
        verso = 0 if giusto else 180
        s += punta(dx + 150, 235, verso, col, 12)
        s += testo(dx + 186, 254, pedice("i", "ind"), col, 15, math_=True)
        s += testo(dx + 280, 140, pedice("B⃗", "indotto"), col, 15, ancora="end", math_=True)
        s += testo(dx + 150, 312, "✗ rinforza la variazione" if not giusto else "✓ si oppone alla variazione", col, 14)
        return s
    return svg(640, 330, pannello(0, False) + pannello(330, True))


def f5_alternatore():
    return grafico(math.cos, -0.6, 4 * PI + 0.8, -1.35, 1.45, solido=(0, 4 * PI), colore=BLU,
                   tick_x=[(k * PI / 2, etichetta_multiplo_pi_mezzi(k), None) for k in range(1, 9)],
                   etichetta_x="t", etichetta_y="", altre=[(math.sin, ROSSO)],
                   nome="Φ (blu)   i (rosso)", nome_pos=(560, 24), larghezza=700)


def f5_rl(carica_):
    f = (lambda t: 1 - math.exp(-t)) if carica_ else (lambda t: math.exp(-t))
    return grafico(f, -0.5, 6, -0.2, 1.3, solido=(0, 6), colore=ROSSO, larghezza=420, altezza=220,
                   tick_y=[(1, "fem°/R" if carica_ else "I")], linee_y=((1, GRIGIO),) if carica_ else (),
                   etichetta_x="t", etichetta_y="i")


def f5_maxwell_condensatore():
    s = linea(60, 90, 160, 90, BIANCO, 2.5) + linea(300, 90, 400, 90, BIANCO, 2.5)
    s += linea(60, 90, 60, 270, BIANCO, 2.5) + linea(400, 90, 400, 270, BIANCO, 2.5)
    s += linea(60, 270, 222, 270, BIANCO, 2.5) + linea(238, 270, 400, 270, BIANCO, 2.5)
    s += linea(222, 250, 222, 290, BIANCO, 3) + linea(238, 258, 238, 282, BIANCO, 3)
    s += ellisse(170, 90, 14, 44, BLU, 2, riemp=BLU, opacita=0.6) + testo(170, 90, "− −", "#fff", 13)
    s += ellisse(230, 90, 14, 44, ROSSO, 2, riemp=ROSSO, opacita=0.6) + testo(230, 90, "+ +", "#fff", 13)
    s += ellisse(200, 90, 12, 40, BIANCO, 1.5, "4 4") + testo(200, 152, pedice("𝓛", "2"), dim=17, math_=True)
    s += ellisse(300, 90, 14, 44, ARANCIO, 2.5, riemp=ARANCIO, opacita=0.25) + testo(318, 36, pedice("𝓛", "1"), ARANCIO, 17, math_=True)
    return svg(460, 310, s)


def f5_onda_em():
    x0, y0 = 50, 150
    def P(x, y, z):
        return x0 + x + z * 0.55, y0 - y - z * 0.32
    s = linea(*P(0, 0, 0), *P(540, 0, 0), BIANCO, 1.6, freccia=True)
    s += linea(*P(0, 0, 0), *P(0, 110, 0), BIANCO, 1.2, freccia=True) + linea(*P(0, 0, 0), *P(0, 0, 160), BIANCO, 1.2, freccia=True)
    s += testo(*P(556, -10, 0), "x", dim=17, math_=True)
    pe, pb = [], []
    for i in range(301):
        x = 480 * i / 300
        v = math.sin(2 * PI * x / 240)
        pe.append(P(x, 80 * v, 0))
        pb.append(P(x, 0, 110 * v))
        if i % 12 == 0:
            s += linea(*P(x, 0, 0), *P(x, 80 * v, 0), BLU, 1, None) + linea(*P(x, 0, 0), *P(x, 0, 110 * v), ROSSO, 1, None)
    s += percorso("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pe), BLU, 2.6)
    s += percorso("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pb), ROSSO, 2.6)
    s += testo(*P(70, 100, 0), "E⃗", BLU, 18, math_=True) + testo(*P(30, 0, 140), "B⃗", ROSSO, 18, math_=True)
    return svg(680, 280, s)


def f5_malus():
    ox, oy = 150, 160
    a = math.radians(35)
    L = 150
    ex, ey = ox + L * math.cos(a), oy - L * math.sin(a)
    s = linea(30, oy, 480, oy, BIANCO, 1.5, "5 5") + testo(480, oy + 22, "asse di trasmissione del filtro", dim=13, ancora="end")
    s += linea(ox, oy, ex, oy, VERDE, 3, freccia=True) + testo((ox + ex) / 2, oy + 22, "E∥", VERDE, 17, math_=True)
    s += linea(ox, oy, ox, ey, BLU, 3, freccia=True) + testo(ox - 22, ey + 6, "E⊥", BLU, 17, math_=True)
    s += linea(ox, oy, ex, ey, ARANCIO, 3, freccia=True) + testo(ex + 14, ey - 6, "E⃗", ARANCIO, 18, math_=True)
    s += linea(ex, ey, ex, oy, BIANCO, 1.2, "3 3")
    s += arco_angolo(ox, oy, 40, 0, a) + testo(ox + 54, oy - 14, "α", ARANCIO, 17, math_=True)
    return svg(500, 200, s)


# ---------------------------------------------- 2: relatività

def f5_treno():
    s = linea(40, 210, 540, 210, BIANCO, 2, freccia=True) + linea(40, 210, 40, 20, BIANCO, 2, freccia=True)
    s += testo(552, 224, "x", dim=17, math_=True) + testo(56, 24, "y", dim=17, math_=True) + testo(22, 40, "S", dim=17, math_=True)
    s += rett(140, 80, 300, 100, BIANCO) + linea(140, 165, 440, 165, BIANCO, 1.5)
    for cx in (160, 182, 398, 420):
        s += f'<circle cx="{cx}" cy="190" r="11" fill="none" stroke="{BIANCO}" stroke-width="2"/>'
    s += linea(270, 210, 270, 110, ARANCIO, 2, freccia=True) + linea(270, 210, 360, 210, ARANCIO, 2.5, freccia=True)
    s += testo(250, 104, "S′", ARANCIO, 16, math_=True) + testo(366, 196, "x′", ARANCIO, 15, math_=True)
    s += f'<circle cx="390" cy="120" r="13" fill="{ROSSO}" fill-opacity="0.85"/>'
    s += linea(440, 110, 520, 110, VERDE, 2.5, freccia=True) + testo(504, 92, "v⃗", VERDE, 17, math_=True)
    return svg(580, 240, s)


def f5_dilatazione():
    def carrello(x, y=200, w=120):
        s = linea(x, y, x + w, y, ARANCIO, 3) + linea(x, y, x, y - 14, ARANCIO, 3) + linea(x + w, y, x + w, y - 14, ARANCIO, 3)
        s += (f'<circle cx="{x + 22}" cy="{y + 12}" r="11" fill="none" stroke="{ARANCIO}" stroke-width="2"/>'
              f'<circle cx="{x + w - 22}" cy="{y + 12}" r="11" fill="none" stroke="{ARANCIO}" stroke-width="2"/>')
        return s
    s = carrello(40) + rett(30, 40, 140, 16, BIANCO) + testo(100, 30, "specchio", dim=13)
    s += linea(96, 196, 96, 60, ROSSO, 2.5, freccia=True) + linea(108, 60, 108, 196, ROSSO, 2.5, freccia=True)
    s += testo(132, 130, "luce", ROSSO, 14) + testo(100, 250, "visto dal carrello", dim=14)
    s += linea(220, 20, 220, 260, BIANCO, 1, "3 5")
    xs = [260, 440, 620]
    for i, x in enumerate(xs):
        s += carrello(x, w=110) + rett(x - 5, 40, 120, 16, BIANCO)
        s += testo(x + 55, 236, ["A", "A′", "A″"][i], dim=15, math_=True) + testo(x + 55, 30, ["B", "B′", "B″"][i], dim=15, math_=True)
    s += linea(xs[0] + 55, 196, xs[1] + 55, 60, ROSSO, 2.5, freccia=True)
    s += linea(xs[1] + 55, 60, xs[2] + 55, 196, ROSSO, 2.5, freccia=True)
    s += testo(500, 268, "visto da fuori", dim=14)
    return svg(760, 280, s)


def f5_cono():
    cx, cy, L = 260, 220, 190
    s = (f'<path d="M{cx},{cy} L{cx - L},{cy - L} L{cx + L},{cy - L} Z" fill="{ARANCIO}" fill-opacity="0.25"/>'
         f'<path d="M{cx},{cy} L{cx - L},{cy + L} L{cx + L},{cy + L} Z" fill="{ARANCIO}" fill-opacity="0.25"/>'
         f'<path d="M{cx},{cy} L{cx - L},{cy - L} L{cx - L},{cy + L} Z" fill="{ROSSO}" fill-opacity="0.18"/>'
         f'<path d="M{cx},{cy} L{cx + L},{cy - L} L{cx + L},{cy + L} Z" fill="{ROSSO}" fill-opacity="0.18"/>')
    s += linea(cx - L - 10, cy, cx + L + 20, cy, BIANCO, 2, freccia=True) + linea(cx, cy + L, cx, cy - L - 20, BIANCO, 2, freccia=True)
    s += testo(cx + L + 30, cy + 16, "x", dim=17, math_=True) + testo(cx + 22, cy - L - 16, "ct", dim=17, math_=True)
    s += linea(cx - L, cy + L, cx + L, cy - L, ARANCIO, 2.5) + linea(cx - L, cy - L, cx + L, cy + L, ARANCIO, 2.5)
    s += testo(cx + L - 6, cy - L - 12, "ct = x", ARANCIO, 15, math_=True) + testo(cx - L + 6, cy - L - 12, "ct = −x", ARANCIO, 15, math_=True)
    s += testo(cx, cy - L + 30, "cono del futuro", ROSSO, 15) + testo(cx, cy + L - 20, "cono del passato", ROSSO, 15)
    s += testo(cx - 130, cy + 50, "impossibile", ROSSO, 15) + testo(cx + 130, cy + 50, "impossibile", ROSSO, 15)
    s += linea(cx, cy, cx + 50, cy - 110, VERDE, 2.5, freccia=True) + testo(cx + 68, cy - 120, "connesso", VERDE, 14, ancora="start")
    s += linea(cx, cy, cx + 110, cy - 30, VIOLA, 2.5, freccia=True) + testo(cx + 116, cy - 44, "non connesso", VIOLA, 14, ancora="start")
    s += punto(cx, cy, VERDE, 5) + testo(cx - 14, cy + 18, "presente", VERDE, 14, ancora="end")
    return svg(540, 440, s)


def f5_minkowski_assi():
    ox, oy, L, b = 50, 320, 300, 0.35
    s = linea(ox, oy, ox + L, oy, BIANCO, 2, freccia=True) + linea(ox, oy, ox, oy - L, BIANCO, 2, freccia=True)
    s += testo(ox + L + 12, oy + 14, "x", dim=17, math_=True) + testo(ox + 22, oy - L, "ct", dim=17, math_=True)
    s += linea(ox, oy, ox + L * 0.9, oy - L * 0.9, ARANCIO, 1.8, "6 5") + testo(ox + L * 0.9 + 4, oy - L * 0.9 - 10, "luce", ARANCIO, 14, ancora="start")
    s += linea(ox, oy, ox + L * b * 0.95, oy - L * 0.95, VERDE, 2.6, freccia=True)
    s += linea(ox, oy, ox + L * 0.95, oy - L * b * 0.95, VERDE, 2.6, freccia=True)
    s += testo(ox + L * b + 10, oy - L * 0.95, "ct′  (ct = x/β)", VERDE, 15, ancora="start", math_=True)
    s += testo(ox + L * 0.95, oy - L * b - 18, "x′  (ct = βx)", VERDE, 15, ancora="end", math_=True)
    s += testo(ox - 12, oy + 14, "O", dim=15, math_=True)
    return svg(400, 350, s)


# --------------------------------------- 3: crisi della fisica classica

def f5_spettro():
    regioni = [("raggi γ", 0, 130, "#6b7280"), ("raggi X", 130, 230, "#7c8594"), ("UV", 230, 290, "#8b93a1"),
               ("", 290, 330, None), ("IR", 330, 440, "#8b93a1"), ("onde radio", 440, 700, "#9aa3b2")]
    s = '<defs><linearGradient id="vis"><stop offset="0" stop-color="#7c3aed"/><stop offset=".25" stop-color="#2563eb"/><stop offset=".45" stop-color="#16a34a"/><stop offset=".62" stop-color="#eab308"/><stop offset=".8" stop-color="#f97316"/><stop offset="1" stop-color="#dc2626"/></linearGradient></defs>'
    for nome, a, b, col in regioni:
        x = 30 + a
        s += rett(x, 60, b - a, 44, GRIGIO, col or "url(#vis)", 0.75 if col else 1, 1.5)
        if nome:
            s += testo(x + (b - a) / 2, 82, nome, "#fff", 14, grassetto=True)
    s += testo(30 + 310, 120, "visibile", dim=13)
    s += linea(40, 30, 720, 30, BIANCO, 1.8, freccia=True) + testo(380, 18, "lunghezza d'onda λ crescente", dim=13)
    s += linea(720, 140, 40, 140, ARANCIO, 1.8, freccia=True) + testo(380, 156, "frequenza f crescente", ARANCIO, 13)
    return svg(760, 168, s)


def f5_cavita():
    def pannello(dx, emette):
        s = (f'<path d="M{dx + 245},{110} A100,100 0 1,0 {dx + 245},{190}" fill="none" stroke="{BIANCO}" '
             f'stroke-width="24"/>')
        pts = [(dx + 90, 80), (dx + 220, 120), (dx + 110, 210), (dx + 180, 70), (dx + 210, 200), (dx + 80, 150), (dx + 200, 100), (dx + 120, 90), (dx + 160, 220)]
        d = "M" + " L".join(f"{x},{y}" for x, y in pts)
        s += percorso(d, ROSSO, 1.4) + percorso("M" + " L".join(f"{x},{y + 10}" for x, y in reversed(pts)), ARANCIO, 1.4)
        if emette:
            s += linea(dx + 100, 145, dx + 330, 120, VERDE, 2.2, freccia=True) + linea(dx + 90, 160, dx + 330, 165, BLU, 2.2, freccia=True)
            s += testo(dx + 170, 270, "scaldato, emette radiazione non a caso", dim=13)
        else:
            s += linea(dx + 330, 120, dx + 130, 145, ROSSO, 2.2, freccia=True) + linea(dx + 330, 165, dx + 120, 150, ARANCIO, 2.2, freccia=True)
            s += testo(dx + 170, 270, "le onde entrano e restano intrappolate", dim=13)
        return s
    return svg(720, 290, pannello(0, False) + pannello(370, True))


def f5_fotoelettrico():
    s = rett(40, 170, 320, 30, ARANCIO, ARANCIO, 0.9) + testo(200, 216, "metallo", dim=13)
    s += ondina(70, 40, 190, 168, ROSSO, 5, 7) + testo(70, 28, "onda EM / fotone", ROSSO, 13, ancora="start")
    s += linea(192, 168, 320, 50, VERDE, 2.6, freccia=True) + testo(326, 40, "e⁻", VERDE, 17, ancora="start")
    return svg(400, 230, s)


def f5_compton():
    cx, cy = 200, 140
    s = linea(cx, cy, 420, cy, BIANCO, 1.4, "5 5")
    s += ondina(30, cy, cx - 12, cy, ROSSO, 5, 7) + testo(90, cy - 22, "f, λ", ROSSO, 16, math_=True)
    s += f'<circle cx="{cx}" cy="{cy}" r="11" fill="{VERDE}"/>' + testo(cx - 22, cy - 22, "e⁻", VERDE, 16)
    s += linea(cx, cy, cx + 110, cy - 90, VERDE, 2.6, freccia=True) + testo(cx + 122, cy - 98, "p⃗", VERDE, 17, math_=True, ancora="start")
    s += ondina(cx, cy + 12, cx + 70, cy + 140, ROSSO, 5, 6) + testo(cx + 90, cy + 140, "f′, λ′", ROSSO, 16, math_=True, ancora="start")
    s += arco_angolo(cx, cy, 36, -1.1, 0, ROSSO) + testo(cx + 52, cy + 26, "θ", ROSSO, 16, math_=True)
    return svg(440, 300, s)


# ------------------------------------- disegni aggiuntivi (circuiti, ecc.)

def solenoide_spire(x, y, w, h, n=9, colore=BIANCO):
    """Solenoide orizzontale: n spire (ellissi strette) tra x e x+w, centrato in y."""
    s = ""
    for k in range(n):
        cx = x + (k + 0.5) * w / n
        s += ellisse(cx, y, w / n * 0.75, h / 2, colore, 2)
    return s


def batteria(x, y, verticale=False, colore=BIANCO):
    """Simbolo del generatore: lineetta lunga (+) e corta (−) centrate in (x,y)."""
    if verticale:
        return (linea(x - 16, y - 4, x + 16, y - 4, colore, 2.5) + linea(x - 8, y + 4, x + 8, y + 4, colore, 4)
                + testo(x + 24, y - 8, "+", colore, 14) + testo(x + 24, y + 10, "−", colore, 14))
    return (linea(x - 4, y - 16, x - 4, y + 16, colore, 2.5) + linea(x + 4, y - 8, x + 4, y + 8, colore, 4)
            + testo(x - 12, y - 22, "+", colore, 14) + testo(x + 12, y - 22, "−", colore, 14))


def resistenza(x1, x2, y, colore=BIANCO, picchi=6):
    """Resistenza a zig-zag orizzontale tra x1 e x2."""
    passo = (x2 - x1) / (2 * picchi)
    d = f"M{x1},{y}"
    for k in range(2 * picchi):
        d += f" L{x1 + (k + 0.5) * passo:.1f},{y + (-7 if k % 2 == 0 else 7)}"
    d += f" L{x2},{y}"
    return percorso(d, colore, 2)


def resistenza_v(x, y1, y2, colore=BIANCO, picchi=6):
    passo = (y2 - y1) / (2 * picchi)
    d = f"M{x},{y1}"
    for k in range(2 * picchi):
        d += f" L{x + (-7 if k % 2 == 0 else 7)},{y1 + (k + 0.5) * passo:.1f}"
    d += f" L{x},{y2}"
    return percorso(d, colore, 2)


def amperometro(x, y, etichetta, colore=BIANCO, w=96, h=34):
    return rett(x - w / 2, y - h / 2, w, h, colore, "#1b1e26", 1, 2) + testo(x, y, etichetta, colore, 15, math_=True)


def circuito_rivelatore(x, y, etichetta="i = 0 A", colore=BIANCO, col_lab=BIANCO, frecce=False):
    """Primo circuito degli esperimenti di Faraday: amperometro in alto, solenoide in basso."""
    s = amperometro(x + 115, y, etichetta, colore)
    s += linea(x + 20, y, x + 67, y, colore, 2) + linea(x + 163, y, x + 210, y, colore, 2)
    s += linea(x + 20, y, x + 20, y + 110, colore, 2) + linea(x + 210, y, x + 210, y + 110, colore, 2)
    s += linea(x + 20, y + 110, x + 50, y + 110, colore, 2) + linea(x + 180, y + 110, x + 210, y + 110, colore, 2)
    s += solenoide_spire(x + 50, y + 110, 130, 54)
    if frecce:
        s += punta(x + 20, y + 60, 90, ARANCIO, 10) + punta(x + 210, y + 60, -90, ARANCIO, 10)
    return s


def magnete_orizzontale(x, y, w=110, h=30):
    return (rett(x, y - h / 2, w / 2, h, BLU, BLU, 0.85) + testo(x + w / 4, y, "N", "#fff", 14, grassetto=True)
            + rett(x + w / 2, y - h / 2, w / 2, h, ROSSO, ROSSO, 0.85) + testo(x + 3 * w / 4, y, "S", "#fff", 14, grassetto=True))


def linee_magnete(x, y, w=110):
    s = ""
    for h in (28, 52):
        s += percorso(f"M{x + w},{y} C{x + w + 10},{y - h} {x - 10},{y - h} {x},{y}", VERDE, 1.6)
        s += percorso(f"M{x + w},{y} C{x + w + 10},{y + h} {x - 10},{y + h} {x},{y}", VERDE, 1.6)
    return s


def omino(x, y, colore=BIANCO, opacita=1):
    """Omino stilizzato con i piedi in (x, y)."""
    return (f'<g opacity="{opacita}">'
            f'<circle cx="{x}" cy="{y - 58}" r="11" fill="none" stroke="{colore}" stroke-width="2"/>'
            + linea(x, y - 47, x, y - 22, colore, 2) + linea(x - 14, y - 38, x + 14, y - 38, colore, 2)
            + linea(x, y - 22, x - 10, y, colore, 2) + linea(x, y - 22, x + 10, y, colore, 2) + '</g>')


def specchio(cx, cy, lung, angolo, colore=BIANCO, spessore=12):
    return (f'<rect x="{cx - lung / 2}" y="{cy - spessore / 2}" width="{lung}" height="{spessore}" fill="none" '
            f'stroke="{colore}" stroke-width="2" transform="rotate({angolo} {cx} {cy})"/>')


def assi_piccoli(x, y, lx, ly, colore=BIANCO, ex="", ey="", spessore=2):
    s = linea(x, y, x + lx, y, colore, spessore, freccia=True) + linea(x, y, x, y - ly, colore, spessore, freccia=True)
    if ex:
        s += testo(x + lx + 12, y + 12, ex, colore, 15, math_=True)
    if ey:
        s += testo(x - 14, y - ly + 4, ey, colore, 15, math_=True)
    return s


def carrello(x, y, w=110, colore=ARANCIO):
    return (linea(x, y, x + w, y, colore, 3) + linea(x, y, x, y - 14, colore, 3) + linea(x + w, y, x + w, y - 14, colore, 3)
            + f'<circle cx="{x + 22}" cy="{y + 12}" r="11" fill="none" stroke="{colore}" stroke-width="2"/>'
            + f'<circle cx="{x + w - 22}" cy="{y + 12}" r="11" fill="none" stroke="{colore}" stroke-width="2"/>')


def vagone(x, y, w=210, h=100, colore=BIANCO, opacita=1):
    s = f'<g opacity="{opacita}">' + rett(x, y, w, h, colore)
    for cx in (x + 22, x + 46, x + w - 46, x + w - 22):
        s += f'<circle cx="{cx}" cy="{y + h + 12}" r="11" fill="none" stroke="{colore}" stroke-width="2"/>'
    return s + "</g>"


# ripasso

def f5_forza_filo():
    s = (f'<path d="M180,50 A110,110 0 0,0 180,270" fill="none" stroke="{BIANCO}" stroke-width="2.5"/>'
         f'<path d="M180,80 A80,80 0 0,0 180,240" fill="none" stroke="{BIANCO}" stroke-width="2.5"/>')
    s += rett(180, 50, 200, 30, ROSSO) + testo(280, 65, "N", BIANCO, 15) + rett(180, 240, 200, 30, BLU) + testo(280, 255, "S", BIANCO, 15)
    for x in range(200, 380, 28):
        s += linea(x, 84, x, 234, VERDE, 2, freccia=True)
    s += testo(398, 100, "B⃗", VERDE, 18, math_=True)
    s += percorso("M130,200 C130,160 140,160 160,160 L420,160 C440,160 450,160 450,200", ARANCIO, 2.5, "6 5")
    s += linea(160, 160, 420, 160, ARANCIO, 3) + linea(380, 140, 420, 140, ARANCIO, 2.5, freccia=True) + testo(432, 132, "i", ARANCIO, 17, math_=True)
    return svg(480, 300, s)


# elettromagnetismo: esperimenti di Faraday

def f5_faraday(n):
    if n == 1:
        s = circuito_rivelatore(10, 40) + magnete_orizzontale(280, 120) + linee_magnete(280, 120)
        s += testo(335, 190, "fermo", BIANCO, 14)
        s += circuito_rivelatore(440, 40, "i ≠ 0 A", ARANCIO, frecce=True) + magnete_orizzontale(710, 120) + linee_magnete(710, 120)
        s += linea(700, 100, 680, 100, ARANCIO, 2.5, freccia=True) + linea(822, 100, 842, 100, ARANCIO, 2.5, freccia=True)
        s += testo(765, 190, "in movimento", ARANCIO, 14)
        return svg(870, 210, s)

    def secondo(x, y, extra):
        t = batteria(x + 115, y) + linea(x + 20, y, x + 105, y, BIANCO, 2) + linea(x + 125, y, x + 210, y, BIANCO, 2)
        t += linea(x + 20, y, x + 20, y + 110, BIANCO, 2) + linea(x + 20, y + 110, x + 50, y + 110, BIANCO, 2)
        t += solenoide_spire(x + 50, y + 110, 130, 54) + linea(x + 180, y + 110, x + 210, y + 110, BIANCO, 2)
        if extra == "interruttore":
            t += linea(x + 210, y, x + 210, y + 40, BIANCO, 2) + linea(x + 210, y + 78, x + 210, y + 110, BIANCO, 2)
            t += linea(x + 210, y + 78, x + 230, y + 44, ROSSO, 2.5)
        elif extra == "resistenza":
            t += linea(x + 210, y, x + 210, y + 25, BIANCO, 2) + resistenza_v(x + 210, y + 25, y + 85) + linea(x + 210, y + 85, x + 210, y + 110, BIANCO, 2)
            t += linea(x + 190, y + 80, x + 232, y + 32, ROSSO, 1.8, freccia=True) + testo(x + 236, y + 56, pedice("R", "v"), BIANCO, 15, ancora="start", math_=True)
        else:
            t += linea(x + 210, y, x + 210, y + 110, BIANCO, 2)
        t += linea(x + 30, y + 110, x + 200, y + 110, VERDE, 1.8, freccia=True) + testo(x + 196, y + 132, "B⃗", VERDE, 15, math_=True)
        return t

    if n == 2:
        s = circuito_rivelatore(10, 40) + secondo(270, 40, "") + testo(385, 200, "fermo: i = 0 A nel primo", BIANCO, 13)
        s += circuito_rivelatore(560, 40, "i ≠ 0 A", ARANCIO, frecce=True) + secondo(820, 40, "")
        s += linea(808, 110, 788, 110, ARANCIO, 2.5, freccia=True) + linea(1042, 110, 1062, 110, ARANCIO, 2.5, freccia=True)
        s += testo(935, 200, "lo muovo: i ≠ 0 A nel primo", ARANCIO, 13)
        return svg(1080, 215, s)
    if n == 3:
        return svg(540, 200, circuito_rivelatore(10, 40) + secondo(280, 40, "interruttore"))
    return svg(560, 200, circuito_rivelatore(10, 40) + secondo(280, 40, "resistenza"))


def f5_conduttore():
    s = uscente(30, 70) + testo(30, 44, "B⃗", VERDE, 16, math_=True)
    s += rett(70, 40, 50, 180, BIANCO)
    for i, (dx, dy) in enumerate([(84, 60), (104, 82), (84, 104), (104, 126), (84, 150), (104, 172), (90, 200)]):
        s += carica(dx, dy, "+" if i % 2 == 0 else "−", ROSSO if i % 2 == 0 else BLU)
    s += testo(95, 244, "conduttore neutro", BIANCO, 13)
    s += uscente(250, 70) + testo(250, 44, "B⃗", VERDE, 16, math_=True)
    s += rett(290, 40, 50, 180, BIANCO)
    for x, y in [(305, 56), (325, 56), (305, 74), (325, 74)]:
        s += carica(x, y, "−", BLU)
    for x, y in [(305, 186), (325, 186), (305, 204), (325, 204)]:
        s += carica(x, y, "+", ROSSO)
    s += linea(340, 130, 410, 130, BIANCO, 2.5, freccia=True) + testo(398, 114, "v⃗", BIANCO, 16, math_=True)
    s += percorso("M440,50 C470,100 470,160 440,210", ARANCIO, 2.5, freccia=True) + testo(478, 130, "fem", ARANCIO, 15, ancora="start")
    s += testo(315, 244, "conduttore in moto", BIANCO, 13)
    return svg(530, 260, s)


def f5_barretta_stato(xr, etichetta):
    s = rett(xr + 50, 60, 520 - xr - 50, 140, ARANCIO, ARANCIO, 0.22, 0)
    s += linea(100, 60, 520, 60, ARANCIO, 3) + linea(100, 200, 520, 200, ARANCIO, 3) + linea(520, 60, 520, 200, ARANCIO, 3)
    s += rett(xr, 40, 50, 180, BIANCO, "#1b1e26", 1, 2)
    for x, y in [(xr + 15, 56), (xr + 35, 56), (xr + 15, 74), (xr + 35, 74)]:
        s += carica(x, y, "−", BLU)
    for x, y in [(xr + 15, 186), (xr + 35, 186), (xr + 15, 204), (xr + 35, 204)]:
        s += carica(x, y, "+", ROSSO)
    s += linea(xr + 50, 130, xr + 120, 130, BIANCO, 2.5, freccia=True) + testo(xr + 110, 114, "v⃗", BIANCO, 16, math_=True)
    s += uscente(40, 70) + testo(40, 42, "B⃗", VERDE, 16, math_=True)
    s += linea(555, 60, 555, 200, BIANCO, 1.5) + testo(572, 130, "ℓ", BIANCO, 17, math_=True)
    s += testo((xr + 50 + 520) / 2, 170, etichetta, ARANCIO, 15, math_=True)
    return svg(600, 240, s)


def f5_cariche_ritorno():
    s = uscente(40, 60) + testo(40, 34, "B⃗", VERDE, 16, math_=True)
    s += rett(90, 30, 50, 190, BIANCO)
    for x, y in [(105, 46), (125, 46), (105, 64), (125, 64)]:
        s += carica(x, y, "−", BLU)
    for x, y in [(105, 188), (125, 188), (105, 206), (125, 206)]:
        s += carica(x, y, "+", ROSSO)
    s += linea(140, 55, 360, 55, ARANCIO, 2.5) + linea(140, 196, 360, 196, ARANCIO, 2.5)
    s += carica(260, 55, "+", ROSSO) + linea(240, 40, 200, 40, ARANCIO, 2, freccia=True)
    s += carica(160, 120, "+", ROSSO) + linea(115, 90, 115, 150, ARANCIO, 2.5, freccia=True)
    s += carica(260, 196, "+", ROSSO) + linea(276, 212, 316, 212, ARANCIO, 2, freccia=True)
    return svg(380, 240, s)


def f5_piano_induzione():
    s = ""
    for k in range(9, 0, -1):
        s += ellisse(220, 250, 22 * k, 7 * k, "#c2410c", 2)
    s += ellisse(220, 250, 200, 62, BIANCO, 1.5)
    s += f'<path d="M120,70 L120,220 Q220,262 320,220 L320,70 Z" fill="#6b7280" fill-opacity="0.6" stroke="{BIANCO}" stroke-width="2"/>'
    s += ellisse(220, 70, 100, 26, BIANCO, 2, riemp="#2563eb", opacita=0.7)
    for x in (150, 185, 220, 255, 290):
        s += linea(x, 300, x, 150, VERDE, 2, freccia=True)
    s += testo(330, 170, "B⃗", VERDE, 17, math_=True, ancora="start")
    for x in (160, 220, 280):
        s += ellisse(x, 200, 18, 7, ROSSO, 2)
    s += testo(112, 192, "correnti indotte", ROSSO, 13, ancora="end")
    s += linea(400, 236, 470, 210, ARANCIO, 2.5, freccia=True) + linea(470, 250, 400, 270, ARANCIO, 2.5, freccia=True)
    s += testo(478, 210, "i", ARANCIO, 16, math_=True, ancora="start")
    return svg(520, 330, s)


def f5_alternatore_spira():
    def pannello(dx, alfa, etichetta):
        s = rett(dx + 10, 40, 22, 100, ROSSO, ROSSO, 0.85) + testo(dx + 21, 90, "N", "#fff", 13, grassetto=True)
        s += rett(dx + 168, 40, 22, 100, BLU, BLU, 0.85) + testo(dx + 179, 90, "S", "#fff", 13, grassetto=True)
        for y in (52, 72, 92, 112, 132):
            s += linea(dx + 36, y, dx + 164, y, VERDE, 1.6) + punta(dx + 120, y, 0, VERDE, 8)
        if alfa in (90, 270):
            s += rett(dx + 70, 48, 60, 84, BIANCO, "none", 1, 2.2)
        else:
            s += f'<path d="M{dx + 80},{132} L{dx + 80},{88} L{dx + 120},{48} L{dx + 120},{92} Z" fill="none" stroke="{BIANCO}" stroke-width="2.2"/>'
        s += linea(dx + 100, 132, dx + 100, 160, BIANCO, 2) + rett(dx + 40, 160, 120, 34, BIANCO)
        s += resistenza(dx + 75, dx + 125, 194)
        s += testo(dx + 100, 22, etichetta, ARANCIO, 15, math_=True)
        return s
    s = "".join(pannello(i * 210, a, f"α = {a}°") for i, a in enumerate([0, 90, 180, 270]))
    return svg(840, 215, s)


def f5_autoinduzione_circuiti():
    s = ""
    for dx, chiuso in [(20, False), (300, True)]:
        s += batteria(dx + 120, 40) + linea(dx + 20, 40, dx + 110, 40, BIANCO, 2) + linea(dx + 130, 40, dx + 220, 40, BIANCO, 2)
        s += linea(dx + 20, 40, dx + 20, 180, BIANCO, 2) + linea(dx + 220, 40, dx + 220, 180, BIANCO, 2)
        s += linea(dx + 20, 180, dx + 80, 180, BIANCO, 2) + linea(dx + 160, 180, dx + 220, 180, BIANCO, 2)
        if chiuso:
            s += linea(dx + 80, 180, dx + 160, 180, ROSSO, 2.5)
            s += punta(dx + 220, 110, 90, ROSSO, 11) + punta(dx + 20, 110, -90, ROSSO, 11) + testo(dx + 236, 100, "i", ROSSO, 16, math_=True)
            s += testo(dx + 120, 210, "chiuso: i circola", BIANCO, 13)
        else:
            s += linea(dx + 80, 180, dx + 150, 156, ROSSO, 2.5) + testo(dx + 120, 210, "aperto", BIANCO, 13)
    return svg(560, 225, s)


def f5_solenoide_generatore():
    s = ""
    for k in range(18):
        s += ellisse(90, 60 + k * 13, 40, 7, BIANCO, 1.8)
    s += linea(70, 300, 70, 30, VERDE, 2, freccia=True) + linea(110, 300, 110, 30, VERDE, 2, freccia=True)
    s += testo(56, 316, "B⃗", VERDE, 17, math_=True)
    s += linea(130, 50, 260, 50, BIANCO, 2) + linea(260, 50, 260, 150, BIANCO, 2) + batteria(260, 160, verticale=True)
    s += linea(260, 168, 260, 290, BIANCO, 2) + linea(130, 290, 260, 290, BIANCO, 2)
    s += punta(200, 50, 180, ARANCIO, 11) + punta(200, 290, 0, ARANCIO, 11)
    s += testo(200, 32, "i", ARANCIO, 16, math_=True) + testo(200, 312, "i", ARANCIO, 16, math_=True)
    return svg(320, 330, s)


def f5_circuito_rl():
    s = linea(60, 40, 120, 40, BIANCO, 2) + resistenza(120, 200, 40) + linea(200, 40, 260, 40, BIANCO, 2) + testo(160, 18, "R", BIANCO, 17, math_=True)
    s += linea(260, 40, 260, 70, BIANCO, 2)
    for k in range(8):
        s += ellisse(260, 78 + k * 12, 16, 6, BIANCO, 1.8)
    s += linea(260, 170, 260, 200, BIANCO, 2) + testo(290, 130, "L", BIANCO, 17, math_=True)
    s += linea(60, 200, 260, 200, BIANCO, 2) + linea(60, 40, 60, 110, BIANCO, 2) + batteria(60, 120, verticale=True)
    s += linea(60, 128, 60, 200, BIANCO, 2) + testo(30, 150, "fem°", BIANCO, 14)
    return svg(330, 225, s)


def f5_mutua():
    s = linea(40, 40, 90, 40, BIANCO, 2) + resistenza(90, 170, 40) + linea(170, 40, 220, 40, BIANCO, 2)
    s += linea(40, 40, 40, 110, BIANCO, 2) + batteria(40, 120, verticale=True) + linea(40, 128, 40, 180, BIANCO, 2)
    s += linea(40, 180, 220, 180, BIANCO, 2) + linea(220, 40, 220, 180, BIANCO, 2)
    s += punta(40, 160, 90, ARANCIO, 10) + testo(60, 205, pedice("i", "1"), ARANCIO, 15, math_=True)
    s += linea(280, 40, 330, 40, BIANCO, 2) + resistenza(330, 410, 40) + linea(410, 40, 460, 40, BIANCO, 2)
    s += linea(280, 40, 280, 180, BIANCO, 2) + linea(460, 40, 460, 180, BIANCO, 2)
    s += linea(280, 180, 322, 180, BIANCO, 2) + amperometro(370, 180, "AMP.") + linea(418, 180, 460, 180, BIANCO, 2)
    s += punta(460, 100, 90, ARANCIO, 10) + testo(478, 96, pedice("i", "2"), ARANCIO, 15, math_=True, ancora="start")
    return svg(520, 215, s)


def f5_e_indotto():
    def pannello(dx, aumenta):
        s = linea(dx + 160, 230, dx + 160, 20, VERDE, 2.5, freccia=True) + testo(dx + 176, 24, "B⃗", VERDE, 17, math_=True)
        s += ellisse(dx + 160, 110, 140, 46, ARANCIO, 2.5) + ellisse(dx + 160, 110, 80, 24, ARANCIO, 2.5)
        s += punta(dx + 160, 64, 0 if aumenta else 180, ARANCIO, 12) + testo(dx + 196, 52, "E⃗", ARANCIO, 16, math_=True)
        s += testo(dx + 110, 110, "ΔB⃗ ↑" if aumenta else "ΔB⃗ ↓", VERDE, 15, math_=True)
        if aumenta:
            s += linea(dx + 210, 70, dx + 210, 160, VIOLA, 2.5, freccia=True)
        else:
            s += linea(dx + 210, 160, dx + 210, 70, VIOLA, 2.5, freccia=True)
        s += testo(dx + 222, 180, "B generato da E,", VIOLA, 13, ancora="start")
        s += testo(dx + 222, 198, "si oppone a ΔB", VIOLA, 13, ancora="start")
        s += testo(dx + 110, 250, "B aumenta" if aumenta else "B diminuisce", VERDE, 15)
        return s
    return svg(720, 270, pannello(0, True) + pannello(370, False))


def f5_carica_oscillante():
    s = (f'<circle cx="80" cy="60" r="14" fill="none" stroke="{BIANCO}" stroke-width="2"/>'
         f'<circle cx="300" cy="60" r="14" fill="none" stroke="{BIANCO}" stroke-width="2" stroke-dasharray="4 3"/>')
    s += linea(100, 54, 280, 54, ARANCIO, 2.2, freccia=True) + linea(280, 66, 100, 66, ARANCIO, 2.2, freccia=True)
    s += testo(80, 96, "q", BIANCO, 16, math_=True)
    s += linea(80, 60, 420, 190, VERDE, 1.6, "5 4") + linea(300, 60, 420, 190, VERDE, 1.6, "5 4")
    s += linea(412, 182, 428, 198, VERDE, 2.5) + linea(412, 198, 428, 182, VERDE, 2.5)
    return svg(460, 220, s)


def f5_irradiamento():
    s = percorso("M40,90 L120,40 L250,40 L170,90 Z", BIANCO, 1.4, "4 4") + percorso("M40,210 L40,90 M170,90 L170,210 L40,210 M250,40 L250,160 L170,210", BIANCO, 1.4, "4 4")
    s += f'<path d="M100,90 L180,40 L180,160 L100,210 Z" fill="none" stroke="{BIANCO}" stroke-width="2.2"/>'
    s += testo(196, 40, "A", BIANCO, 16, math_=True)
    s += linea(140, 125, 140, 85, ROSSO, 2.5, freccia=True) + testo(152, 82, "E⃗", ROSSO, 15, math_=True, ancora="start")
    s += linea(140, 125, 108, 140, VERDE, 2.5, freccia=True) + testo(104, 158, "B⃗", VERDE, 15, math_=True)
    s += linea(440, 210, 150, 128, ARANCIO, 2.2, freccia=True) + punto(440, 210, ARANCIO, 5)
    return svg(470, 240, s)


# relatività

def f5_proiettile():
    s = rett(20, 60, 160, 20, BIANCO) + rett(20, 80, 160, 20, BIANCO) + rett(160, 50, 18, 12, BIANCO)
    s += percorso("M182,70 L236,52 L214,70 L256,78 L214,88 L236,104 L190,92", ROSSO, 2.2)
    s += percorso("M188,72 L222,60 L208,74 L236,78 L208,84 L222,96 L192,88", ARANCIO, 2)
    s += rett(380, 70, 16, 24, ARANCIO, "none", 1, 2.2) + percorso("M396,70 L440,70 Q470,82 440,94 L396,94", ARANCIO, 2.2)
    s += linea(390, 40, 470, 40, VERDE, 2.5, freccia=True) + testo(458, 24, "v⃗", VERDE, 16, math_=True)
    return svg(500, 120, s)


def f5_interferometro(perpendicolare):
    s = f'<circle cx="80" cy="260" r="46" fill="{ARANCIO}"/>' + testo(80, 262, "Sole", ROSSO, 14)
    s += linea(80, 214, 80, 30, BIANCO, 1.8, freccia=True) + linea(126, 260, 460, 260, BIANCO, 1.8, freccia=True)
    s += f'<circle cx="230" cy="150" r="18" fill="#2563eb"/><circle cx="226" cy="146" r="7" fill="#22c55e"/>' + testo(230, 184, "Terra", BIANCO, 12)
    s += linea(230, 132, 230, 50, BIANCO, 1.6, freccia=True) + linea(248, 150, 500, 150, BIANCO, 1.6, freccia=True)
    s += linea(330, 158, 330, 190, BIANCO, 2.2, freccia=True) + testo(346, 186, "v⃗", BIANCO, 15, math_=True, ancora="start")
    if not perpendicolare:
        s += specchio(380, 60, 110, 40) + testo(420, 46, "H", VERDE, 15)
        s += rett(330, 128, 90, 12, BIANCO) + testo(430, 134, "A", VERDE, 15, ancora="start")
        s += linea(368, 70, 368, 126, VERDE, 2.2, freccia=True)
        s += testo(470, 60, "AH = ℓ", BIANCO, 15, ancora="start", math_=True)
    else:
        s += specchio(310, 82, 110, 40) + testo(286, 100, "H", BIANCO, 15)
        s += rett(440, 30, 12, 110, BIANCO) + testo(466, 50, "B", BIANCO, 15, ancora="start")
        s += linea(320, 72, 436, 72, VERDE, 2.2, freccia=True) + testo(378, 58, "u⃗", VERDE, 15, math_=True)
        s += linea(320, 76, 436, 116, BLU, 2.2, freccia=True) + testo(374, 112, "c⃗", BLU, 15, math_=True)
        s += linea(446, 72, 446, 114, ROSSO, 2.2, freccia=True) + testo(462, 132, "v⃗", ROSSO, 15, math_=True, ancora="start")
        s += testo(500, 40, "HB = ℓ", BIANCO, 15, ancora="start", math_=True)
    return svg(580, 310, s)


def f5_simultaneita_laser():
    s = linea(60, 120, 520, 120, BIANCO, 2) + linea(60, 120, 60, 90, BIANCO, 2) + linea(520, 120, 520, 90, BIANCO, 2)
    s += rett(80, 82, 30, 12, BIANCO) + rett(470, 82, 30, 12, BIANCO)
    s += testo(95, 66, "laser", BIANCO, 12) + testo(485, 66, "laser", BIANCO, 12)
    s += linea(110, 88, 280, 88, ROSSO, 1.6, "4 3") + linea(470, 88, 300, 88, ROSSO, 1.6, "4 3")
    s += omino(290, 120)
    s += linea(95, 150, 290, 150, BIANCO, 1.4) + linea(290, 150, 485, 150, BIANCO, 1.4)
    for x in (95, 290, 485):
        s += linea(x, 144, x, 156, BIANCO, 1.4)
    s += testo(192, 168, "8 m", BIANCO, 14) + testo(388, 168, "8 m", BIANCO, 14)
    return svg(580, 180, s)


def f5_simultaneita_treno(moto):
    s = f'<circle cx="60" cy="200" r="26" fill="{ARANCIO}"/><circle cx="520" cy="200" r="26" fill="{ARANCIO}"/>'
    s += linea(40, 260, 540, 260, BIANCO, 1.4) + testo(170, 278, "10 m", BIANCO, 13) + testo(410, 278, "10 m", BIANCO, 13)
    s += omino(290, 250)
    s += ondina(86, 200, 270, 200, ARANCIO, 4, 9, False) + ondina(494, 200, 310, 200, ARANCIO, 4, 9, False)
    if not moto:
        s += vagone(185, 40) + omino(290, 140)
        s += ondina(80, 182, 270, 96, ARANCIO, 4, 9, False) + ondina(500, 182, 310, 96, ARANCIO, 4, 9, False)
    else:
        s += vagone(185, 40, opacita=0.35) + omino(290, 140, opacita=0.35)
        s += vagone(255, 40) + omino(360, 140)
        s += ondina(80, 182, 340, 96, ROSSO, 4, 10, False) + ondina(500, 182, 382, 96, ROSSO, 4, 6, False)
        s += linea(300, 20, 400, 20, VERDE, 2.5, freccia=True) + testo(352, 12, "v⃗", VERDE, 15, math_=True)
    return svg(580, 290, s)


def f5_contrazione_strada():
    s = linea(30, 100, 560, 100, BIANCO, 2) + carrello(60, 76, 90)
    s += linea(150, 70, 220, 70, VERDE, 2.5, freccia=True) + testo(206, 54, "v⃗", VERDE, 15, math_=True)
    s += linea(110, 94, 110, 106, BIANCO, 2) + linea(480, 94, 480, 106, BIANCO, 2)
    s += testo(110, 124, pedice("x", "1"), BIANCO, 15, math_=True) + testo(480, 124, pedice("x", "2"), BIANCO, 15, math_=True)
    s += percorso("M110,138 Q110,152 160,152 L280,152 Q295,152 295,166 Q295,152 310,152 L430,152 Q480,152 480,138", BIANCO, 1.8)
    s += testo(295, 186, "Δx", BIANCO, 16, math_=True)
    return svg(590, 200, s)


def f5_sistemi_v():
    s = assi_piccoli(30, 200, 170, 170, BIANCO) + testo(30, 18, "S", BIANCO, 15, math_=True)
    s += assi_piccoli(120, 130, 130, 110, BIANCO) + testo(120, 12, "S′", BIANCO, 15, math_=True)
    s += linea(120, 80, 200, 80, VERDE, 2.5, freccia=True) + testo(190, 64, "v⃗", VERDE, 15, math_=True)
    s += testo(290, 120, "=", BIANCO, 30)
    s += assi_piccoli(400, 160, 150, 150, BIANCO) + testo(384, 22, "S", BIANCO, 15, math_=True)
    s += assi_piccoli(510, 220, 150, 110, BIANCO) + testo(510, 104, "S′", BIANCO, 15, math_=True)
    s += linea(400, 150, 340, 150, VERDE, 2.5, freccia=True) + testo(348, 134, "−v⃗", VERDE, 15, math_=True)
    return svg(690, 240, s)


def f5_composizione(esempio):
    if not esempio:
        s = assi_piccoli(30, 200, 240, 180, BIANCO) + testo(30, 16, "S", BIANCO, 15, math_=True)
        s += assi_piccoli(70, 170, 170, 150, ARANCIO) + testo(78, 16, "S′", ARANCIO, 15, math_=True)
        s += linea(70, 60, 180, 60, VERDE, 2.5, freccia=True) + testo(170, 44, "v⃗", VERDE, 15, math_=True)
        s += punto(150, 110, BLU) + testo(142, 96, "P", BIANCO, 14, math_=True)
        s += linea(150, 110, 210, 110, BLU, 2.5, freccia=True) + testo(214, 96, "w⃗′", BLU, 15, math_=True)
        return svg(300, 230, s)
    s = assi_piccoli(30, 200, 200, 170, BIANCO) + assi_piccoli(110, 150, 150, 120, BIANCO)
    s += linea(110, 90, 50, 90, VERDE, 2.5, freccia=True) + testo(60, 74, "−v⃗", VERDE, 15, math_=True)
    s += punto(190, 60, BLU) + linea(190, 60, 260, 60, BLU, 2.5, freccia=True) + testo(250, 44, "w⃗", BLU, 15, math_=True)
    return svg(300, 230, s)


def f5_invariante():
    s = assi_piccoli(30, 230, 220, 200, BIANCO)
    k = 40
    s += linea(30, 230, 30 + 3 * k, 230 - 4 * k, ROSSO, 3, freccia=True) + testo(30 + 1.2 * k, 230 - 2.6 * k, "s⃗", ROSSO, 17, math_=True)
    s += linea(30 + 3 * k, 226, 30 + 3 * k, 234, BIANCO, 1.5) + linea(26, 230 - 4 * k, 34, 230 - 4 * k, BIANCO, 1.5)
    # sistema ruotato: asse x lungo la direzione (2,1)/√5
    ox, oy = 380, 230
    ux, uy = 2 / math.sqrt(5), 1 / math.sqrt(5)
    s += linea(ox, oy, ox + 230 * ux, oy - 230 * uy, BIANCO, 2, freccia=True)
    s += linea(ox, oy, ox - 200 * uy, oy - 200 * ux, BIANCO, 2, freccia=True)
    px, py = ox + 3 * k, oy - 4 * k
    s += linea(ox, oy, px, py, ROSSO, 3, freccia=True) + testo(ox + 0.9 * k - 16, oy - 2.2 * k, "s⃗", ROSSO, 17, math_=True)
    a = 3 * ux + 4 * uy
    fx, fy = ox + a * k * ux, oy - a * k * uy
    s += linea(px, py, fx, fy, BIANCO, 1.4, "4 3") + testo((px + fx) / 2 + 10, (py + fy) / 2, "a", BIANCO, 15, math_=True)
    b = -3 * uy + 4 * ux
    gx, gy = ox - b * k * uy, oy - b * k * ux
    s += linea(px, py, gx, gy, BIANCO, 1.4, "4 3") + testo((px + gx) / 2, (py + gy) / 2 - 12, "b", BIANCO, 15, math_=True)
    return svg(640, 250, s)


def f5_minkowski_base(ox=50, oy=290, L=260, b=0.35):
    s = assi_piccoli(ox, oy, L, L, BIANCO, "x", "ct")
    s += linea(ox, oy, ox + L * b * 0.95, oy - L * 0.95, VERDE, 2.4, freccia=True) + testo(ox + L * b + 6, oy - L * 0.95, "ct′", VERDE, 15, math_=True, ancora="start")
    s += linea(ox, oy, ox + L * 0.95, oy - L * b * 0.95, VERDE, 2.4, freccia=True) + testo(ox + L * 0.95, oy - L * b - 16, "x′", VERDE, 15, math_=True, ancora="end")
    s += testo(ox - 12, oy + 14, "O", BIANCO, 14, math_=True)
    return s


def f5_minkowski_eventi():
    ox, oy = 50, 230
    s = assi_piccoli(ox, oy, 280, 200, BIANCO, "x", "ct") + testo(ox - 12, oy + 14, "O", BIANCO, 14, math_=True)
    A, B, C = (110, 90), (240, 90), (240, 150)
    s += linea(ox, 90, 240, 90, ARANCIO, 1.4, "4 3") + linea(110, 90, 110, oy, ROSSO, 1.4, "4 3")
    s += linea(240, 90, 240, oy, ROSSO, 1.4, "4 3") + linea(ox, 150, 240, 150, VERDE, 1.4, "4 3")
    for (x, y), n in zip((A, B, C), "ABC"):
        s += punto(x, y, BIANCO, 4) + testo(x + 12, y - 12, n, BIANCO, 15, math_=True)
    return svg(360, 250, s)


def f5_minkowski_effetto(tipo):
    ox, oy, L, b = 50, 290, 260, 0.35
    s = f5_minkowski_base(ox, oy, L, b)
    P = (ox + 110, oy - 160)
    if tipo == "simultaneita":
        Q = (ox + 230, oy - 160)
        s += linea(ox, P[1], Q[0], Q[1], ROSSO, 1.4, "4 3")
        for (x, y), n, col in [(P, "P", ROSSO), (Q, "Q", VIOLA)]:
            s += linea(x, y, x, oy, col, 1.4, "4 3")
            # proiezione parallela all'asse x′ sull'asse ct′
            # intersezione della retta per (x,y) di pendenza b con l'asse ct′ (x = ox + b·(oy−y'))
            yy = (oy - y - b * (x - ox)) / (1 - b * b)
            ix, iy = ox + b * yy, oy - yy
            s += linea(x, y, ix, iy, BIANCO, 1.4, "4 3")
            s += punto(x, y, col, 4) + testo(x + 12, y - 12, n, col, 15, math_=True)
        return svg(360, 310, s)
    x, y = P
    s += linea(ox, y, x, y, ROSSO, 1.4, "4 3") + linea(x, y, x, oy, ROSSO, 1.4, "4 3") + punto(x, y, ROSSO, 4) + testo(x + 12, y - 12, "P", ROSSO, 15, math_=True)
    if tipo == "dilatazione":
        yy = (oy - y - b * (x - ox)) / (1 - b * b)
        ix, iy = ox + b * yy, oy - yy
        s += linea(x, y, ix, iy, VIOLA, 1.4, "4 3")
        s += linea(ox, oy, ox, y, ARANCIO, 4) + testo(ox - 14, (oy + y) / 2, pedice("Δt", "1"), ARANCIO, 14, math_=True, ancora="end")
        s += linea(ox, oy, ix, iy, BLU, 4) + testo(ix + 10, (oy + iy) / 2 + 30, pedice("Δt", "2"), BLU, 14, math_=True, ancora="start")
        s += testo(ox - 14, y, pedice("ct", "P"), ROSSO, 13, math_=True, ancora="end")
    else:
        # proiezione parallela all'asse ct′ sull'asse x′
        xx = ((x - ox) - b * (oy - y)) / (1 - b * b)
        jx, jy = ox + xx, oy - b * xx
        s += linea(x, y, jx, jy, VIOLA, 1.4, "4 3")
        s += linea(ox, oy, x, oy, ARANCIO, 4) + testo((ox + x) / 2, oy + 18, pedice("Δx", "1"), ARANCIO, 14, math_=True)
        s += linea(ox, oy, jx, jy, BLU, 4) + testo((ox + jx) / 2, (oy + jy) / 2 - 14, pedice("Δx", "2"), BLU, 14, math_=True)
    return svg(360, 310, s)


def f5_massa_energia(moto):
    if not moto:
        s = assi_piccoli(30, 60, 60, 50, BIANCO) + testo(20, 6, "S′", BIANCO, 14, math_=True, ancora="start")
        s += rett(140, 110, 110, 54, BIANCO) + testo(195, 137, "m", BIANCO, 17, math_=True)
        s += linea(195, 30, 195, 108, ROSSO, 2.2, freccia=True) + linea(195, 250, 195, 166, ROSSO, 2.2, freccia=True)
        s += testo(212, 30, "laser", ROSSO, 13, ancora="start") + testo(212, 250, "laser", ROSSO, 13, ancora="start")
        return svg(300, 270, s)
    s = linea(40, 30, 40, 250, BIANCO, 1.4, "4 3")
    s += rett(160, 112, 110, 54, BIANCO) + testo(215, 139, "m", BIANCO, 17, math_=True)
    s += linea(270, 139, 340, 139, BIANCO, 2.5, freccia=True) + testo(330, 122, "v⃗", BIANCO, 15, math_=True)
    s += linea(40, 30, 210, 110, ROSSO, 2.4, freccia=True) + linea(40, 250, 210, 168, ROSSO, 2.4, freccia=True)
    s += testo(100, 50, pedice("p⃗", "1"), ROSSO, 15, math_=True) + testo(100, 236, pedice("p⃗", "2"), ROSSO, 15, math_=True)
    # triangolo delle velocità
    s += linea(420, 60, 420, 200, BIANCO, 1.6) + linea(420, 200, 560, 200, BIANCO, 1.6) + linea(420, 60, 560, 200, BIANCO, 1.6)
    s += linea(420, 60, 500, 140, ROSSO, 2.5) + linea(420, 140, 500, 140, ROSSO, 1.4, "4 3")
    s += testo(470, 92, pedice("p", "1"), ROSSO, 14, math_=True) + testo(446, 154, pedice("p", "x"), ROSSO, 14, math_=True)
    s += testo(500, 222, "v", BIANCO, 15, math_=True) + testo(522, 120, "c", BIANCO, 15, math_=True)
    return svg(600, 270, s)


# crisi della fisica classica

def f5_particelle():
    s = ""
    for x, y in [(60, 90), (120, 50), (180, 90), (110, 120), (60, 170), (130, 190), (190, 160), (210, 220), (70, 230)]:
        s += f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="{BIANCO}" stroke-width="2"/>'
        s += linea(x - 26, y - 4, x - 20, y + 4, BIANCO, 1.5) + linea(x - 22, y - 6, x - 16, y + 2, BIANCO, 1.5)
        s += linea(x + 20, y - 18, x + 24, y - 10, BIANCO, 1.5)
    return svg(250, 260, s)


def f5_compton_schemi():
    def pannello(dx, reale):
        s = rett(dx + 170, 30, 26, 130, ARANCIO, ARANCIO, 0.9)
        s += ondina(dx + 20, 95, dx + 168, 95, ROSSO, 5, 8) + testo(dx + 80, 74, "λ", ROSSO, 16, math_=True)
        s += testo(dx + 60, 120, "raggi X", ROSSO, 12)
        s += linea(dx + 196, 95, dx + 360, 95, BIANCO, 1.4, "5 4")
        if reale:
            s += linea(dx + 198, 95, dx + 300, 30, VERDE, 2.4, freccia=True) + testo(dx + 312, 26, "e⁻", VERDE, 15, ancora="start")
            s += ondina(dx + 198, 100, dx + 270, 170, ROSSO, 4, 5) + testo(dx + 262, 186, "?", ROSSO, 16)
            s += arco_angolo(dx + 198, 95, 34, -0.78, 0, ROSSO) + testo(dx + 246, 116, "θ", ROSSO, 15, math_=True)
            s += testo(dx + 190, 210, "cosa si osserva in realtà", BIANCO, 13)
        else:
            s += ondina(dx + 198, 100, dx + 270, 170, ROSSO, 4, 5) + testo(dx + 282, 170, "λ", ROSSO, 16, math_=True, ancora="start")
            s += testo(dx + 190, 210, "teoria classica", BIANCO, 13)
        return s
    return svg(760, 225, pannello(0, False) + pannello(390, True))


def f5_compton_picchi():
    s = ""
    for i, (ang, sep) in enumerate([(0, 0), (45, 14), (90, 34), (135, 52)]):
        dx = 20 + i * 180
        s += linea(dx, 140, dx + 160, 140, BIANCO, 1.6)
        x1 = dx + 50
        x2 = x1 + sep
        pts = []
        for k in range(161):
            x = dx + k
            y = 0
            if sep == 0:
                y = 95 * math.exp(-((x - x1) / 9) ** 2)
            else:
                h1 = 95 - i * 18
                y = h1 * math.exp(-((x - x1) / 9) ** 2) + (40 + i * 22) * math.exp(-((x - x2) / 11) ** 2)
            pts.append((x, 140 - y))
        s += percorso("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), ARANCIO, 2.2)
        s += linea(x1, 30, x1, 140, BIANCO, 1.2, "3 3") + testo(x1, 156, "λ", BIANCO, 14, math_=True)
        if sep:
            s += linea(x2, 30, x2, 140, BIANCO, 1.2, "3 3") + testo(x2 + 4, 156, "λ′", BIANCO, 14, math_=True)
        s += testo(dx + 80, 18, f"θ = {ang}°", BIANCO, 14, math_=True)
    return svg(740, 170, s)


def genera_fisica5_aggiunte():
    return {
        "forza-filo.svg": f5_forza_filo(),
        "faraday-1.svg": f5_faraday(1), "faraday-2.svg": f5_faraday(2),
        "faraday-3.svg": f5_faraday(3), "faraday-4.svg": f5_faraday(4),
        "conduttore-moto.svg": f5_conduttore(),
        "barretta-iniziale.svg": f5_barretta_stato(110, pedice("Φ", "in") + "(B⃗) = B " + pedice("S", "in")),
        "barretta-finale.svg": f5_barretta_stato(300, pedice("Φ", "fin") + "(B⃗) = B " + pedice("S", "fin")),
        "cariche-ritorno.svg": f5_cariche_ritorno(),
        "piano-induzione.svg": f5_piano_induzione(),
        "alternatore-spira.svg": f5_alternatore_spira(),
        "autoinduzione-circuiti.svg": f5_autoinduzione_circuiti(),
        "solenoide-generatore.svg": f5_solenoide_generatore(),
        "circuito-rl.svg": f5_circuito_rl(),
        "mutua-induzione.svg": f5_mutua(),
        "e-indotto.svg": f5_e_indotto(),
        "carica-oscillante.svg": f5_carica_oscillante(),
        "irradiamento.svg": f5_irradiamento(),
        "proiettile.svg": f5_proiettile(),
        "interferometro-parallelo.svg": f5_interferometro(False),
        "interferometro-perpendicolare.svg": f5_interferometro(True),
        "simultaneita-laser.svg": f5_simultaneita_laser(),
        "simultaneita-fermo.svg": f5_simultaneita_treno(False),
        "simultaneita-moto.svg": f5_simultaneita_treno(True),
        "contrazione-strada.svg": f5_contrazione_strada(),
        "sistemi-v.svg": f5_sistemi_v(),
        "composizione-velocita.svg": f5_composizione(False),
        "composizione-esempio.svg": f5_composizione(True),
        "invariante-2d.svg": f5_invariante(),
        "minkowski-eventi.svg": f5_minkowski_eventi(),
        "minkowski-dilatazione.svg": f5_minkowski_effetto("dilatazione"),
        "minkowski-contrazione.svg": f5_minkowski_effetto("contrazione"),
        "minkowski-simultaneita.svg": f5_minkowski_effetto("simultaneita"),
        "massa-energia-riposo.svg": f5_massa_energia(False),
        "massa-energia-moto.svg": f5_massa_energia(True),
        "particelle-vibranti.svg": f5_particelle(),
        "compton-schemi.svg": f5_compton_schemi(),
        "compton-picchi.svg": f5_compton_picchi(),
    }


def genera_fisica5():
    return {
        "magnete-taglio.svg": f5_magnete_taglio(),
        "filo-campo.svg": f5_filo_campo(),
        "spira-campo.svg": f5_spira(),
        "solenoide-campo.svg": f5_solenoide(),
        "due-fili.svg": f5_due_fili(),
        "circuitazione.svg": f5_circuitazione(),
        "moto-circolare.svg": f5_moto_circolare(),
        "selettore-velocita.svg": f5_selettore(),
        "barretta-binari.svg": f5_barretta(),
        "lenz.svg": f5_lenz(),
        "alternatore-grafico.svg": f5_alternatore(),
        "rl-carica.svg": f5_rl(True),
        "rl-scarica.svg": f5_rl(False),
        "maxwell-condensatore.svg": f5_maxwell_condensatore(),
        "onda-em.svg": f5_onda_em(),
        "malus.svg": f5_malus(),
        "treno-galileo.svg": f5_treno(),
        "dilatazione-tempi.svg": f5_dilatazione(),
        "cono-di-luce.svg": f5_cono(),
        "minkowski-assi.svg": f5_minkowski_assi(),
        "spettro-em.svg": f5_spettro(),
        "corpo-nero-cavita.svg": f5_cavita(),
        "effetto-fotoelettrico.svg": f5_fotoelettrico(),
        "effetto-compton.svg": f5_compton(),
    }


def scrivi(cartella, figure):
    os.makedirs(cartella, exist_ok=True)
    for nome, contenuto in figure.items():
        with open(os.path.join(cartella, nome), "w", encoding="utf-8") as f:
            f.write(contenuto)
    print(f"{len(figure)} figure in {os.path.relpath(cartella)}")


if __name__ == "__main__":
    scrivi(DIR_MATE, genera_goniometria())
    scrivi(DIR_MATE, genera_probabilita())
    scrivi(DIR_FIS, genera_onde())
    scrivi(DIR_FIS, genera_fisica5())
    scrivi(DIR_FIS, genera_fisica5_aggiunte())
