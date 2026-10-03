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
