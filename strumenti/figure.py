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
    colori = [GRIGIO, BLU, ROSSO, VERDE, ARANCIO, VIOLA, ROSA, TEAL]
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
            asintoti=(), linee_y=(), etichetta_x="x", etichetta_y="y"):
    """Grafico di f: tratto pieno nell'intervallo `solido`, tratteggiato fuori."""
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

    # campionamento della curva, spezzata vicino agli asintoti
    n = 900
    tratti = []
    corrente = []
    stato = None
    for i in range(n + 1):
        x = xmin + (xmax - xmin) * i / n
        vicino_asintoto = any(abs(x - a) < 0.03 for a in asintoti)
        y = None if vicino_asintoto else f(x)
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

    clip = f'<clipPath id="area"><rect x="0" y="{my - 14}" width="{larghezza}" height="{altezza - 2 * my + 28}"/></clipPath>'
    curve = ""
    for pieno, punti in tratti:
        if len(punti) < 2:
            continue
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in punti)
        tr = "" if pieno else ' stroke-dasharray="5 5"'
        curve += (f'<path d="{d}" fill="none" stroke="{colore}" stroke-width="{2.6 if pieno else 1.6}"'
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


def scrivi(cartella, figure):
    os.makedirs(cartella, exist_ok=True)
    for nome, contenuto in figure.items():
        with open(os.path.join(cartella, nome), "w", encoding="utf-8") as f:
            f.write(contenuto)
    print(f"{len(figure)} figure in {os.path.relpath(cartella)}")


if __name__ == "__main__":
    scrivi(DIR_MATE, genera_goniometria())
    scrivi(DIR_FIS, genera_onde())
