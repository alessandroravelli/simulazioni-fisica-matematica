---
title: Disequazioni goniometriche
description: Disequazioni goniometriche elementari con il metodo grafico e con la circonferenza goniometrica, con sostituzione, di secondo grado, fratte e prodotto, lineari e di secondo grado in seno e coseno.
tags:
  - matematica
  - goniometria
  - 4SCI
---
Le disequazioni goniometriche richiedono di trovare per quali valori una funzione goniometrica è $<$, $>$ o $=$ di un numero. Per esempio:

$$
\sin x > m \qquad \cos x < m \qquad \tan(x) \ge m \qquad m \in \mathbb{R}
$$

> [!info] Collegamenti
> Prima di queste servono le [[Equazioni goniometriche]]: le soluzioni dell'equazione sono i "limiti" della disequazione. I grafici di seno, coseno e tangente sono in [[Goniometria#Grafici delle funzioni]].

Ci sono due modi per risolvere le disequazioni.

## Metodo grafico

Consideriamo $\sin x > \frac{1}{2}$. Lo vediamo dal punto di vista grafico:

1. devo prima di tutto individuare il periodo della funzione $\longrightarrow T = 2\pi$;
2. devo capire se $\frac{1}{2}$ si riferisce a qualche angolo notevole;
3. identifico l'intervallo che risolve la mia disequazione.

![Grafico di sin x tra 0 e 2π con la retta y = 1/2: la curva sta sopra la retta solo tra π/6 e 5π/6](disgonio-sin-grafico.svg)

Mi fermo a $2\pi$ perché tutte le soluzioni che trovo dopo sono uguali e ripetute.

Devo capire quali sono i "limiti" della mia disequazione. Il seno per quali angoli vale $\frac{1}{2}$?

$$
\sin\left(\frac{\pi}{6}\right) = \frac{1}{2} \qquad \underbrace{\sin\left(\pi - \frac{\pi}{6}\right)}_{\text{archi associati}} = \sin\left(\frac{5}{6}\pi\right) = \frac{1}{2}
$$

$\sin(x) > \frac{1}{2}$ solo in questo intervallo:

$$
\longrightarrow\quad \frac{\pi}{6} + 2k\pi < x < \frac{5}{6}\pi + 2k\pi
$$

## Metodo della circonferenza goniometrica

![Circonferenza goniometrica: l'arco evidenziato sopra la retta y = 1/2 va da π/6 a 5π/6](disgonio-sin-circonferenza.svg)

Anche in questo caso ci chiediamo quando è che $\sin x = \frac{1}{2}$ e troviamo i due angoli $\frac{\pi}{6}$ e $\frac{5\pi}{6}$. A questo punto vediamo che la parte di circonferenza che sta sopra la linea che rappresenta $\frac{1}{2}$ è proprio la soluzione.

Il limite di questo metodo sta nel fatto che è applicabile facilmente solo quando il periodo delle funzioni è minore o uguale a $2\pi$.

> [!example] Esempio: $\sin x > -\dfrac{\sqrt{3}}{2}$
> Per quali angoli ho $-\frac{\sqrt{3}}{2}$? $\frac{\sqrt{3}}{2}$ e il seno sono legati all'angolo $\frac{\pi}{3}$.
>
> ![La retta y = −√3/2 taglia la circonferenza agli angoli 4π/3 e 5π/3](disgonio-esempio-circonferenza.svg)
>
> ![Grafico di sin x con la retta y = −√3/2: le intersezioni sono in 4π/3 e 5π/3](disgonio-esempio-grafico.svg)
>
> ![Arco evidenziato: tutta la circonferenza tranne la parte sotto la retta, tra 4π/3 e 5π/3](disgonio-esempio-circonferenza-sol.svg)
>
> ![Grafico di sin x: evidenziati gli intervalli da 0 a 4π/3 e da 5π/3 a 2π](disgonio-esempio-grafico-sol.svg)
>
>
> Individuo subito gli intervalli in cui la mia disequazione è verificata.

> [!warning] Attenzione
> Quando scriviamo le soluzioni di una disequazione partiamo sempre, per convenzione, da $0$ e arriviamo a $2\pi$. Il metodo con il grafico ci aiuta perché parte sempre da $0$; quello con la circonferenza no.

$$
0 + 2k\pi < x < \frac{4}{3}\pi + 2k\pi \quad \vee \quad \frac{5}{3}\pi + 2k\pi < x < 2\pi + 2k\pi
$$

È accettabile anche usare angoli negativi per scrivere tutto in un'unica soluzione:

$$
-\frac{\pi}{3} + 2k\pi < x < \frac{4}{3}\pi + 2k\pi
$$

## Disequazioni elementari con cos x

$$
\cos x > \frac{\sqrt{2}}{2}
$$

![La retta verticale x = √2/2: l'arco evidenziato a destra va da −π/4 a π/4](disgonio-cos-circonferenza.svg)

![Grafico di cos x con la retta y = √2/2: evidenziati gli intervalli da 0 a π/4 e da 7π/4 a 2π](disgonio-cos-grafico.svg)


$\cos$ e $\frac{\sqrt{2}}{2}$ sono legati a $\frac{\pi}{4}$ $\longrightarrow$ ho sempre 2 angoli:

$$
\frac{\pi}{4} \qquad\text{e}\qquad 2\pi - \frac{\pi}{4} = \frac{7}{4}\pi
$$

Scelgo gli intervalli in cui $\cos(x) > \frac{\sqrt{2}}{2}$:

$$
0 + 2k\pi \le x < \frac{\pi}{4} + 2k\pi \quad \vee \quad \frac{7}{4}\pi + 2k\pi < x < 2\pi + 2k\pi
$$

## Disequazioni con tan(x)

Per questi esercizi è consigliato usare **solo** il metodo con il grafico, perché quello con la circonferenza goniometrica può essere fuorviante.

$$
\tan(x) \ge \sqrt{3}
$$

Il periodo della tangente è $\pi$ $\longrightarrow$ quindi posso studiare la soluzione tra $0$ e $\pi$. $\sqrt{3}$ e $\tan(x)$ sono legati all'angolo $\frac{\pi}{3}$.

![Grafico di tan x tra 0 e π con la retta y = √3: evidenziato il tratto da π/3 fino all'asintoto in π/2](disgonio-tan.svg)

$$
\frac{\pi}{3} + k\pi \;\textcolor{#22c55e}{\le}\; x \;\textcolor{#ef4444}{<}\; \frac{\pi}{2} + k\pi
$$

- $\textcolor{#22c55e}{\le}$: metto $\le$ perché ho $\tan(x) \ge \sqrt{3}$;
- $\textcolor{#ef4444}{<}$: solo $<$ perché $\tan(x)$ non esiste in $\frac{\pi}{2}$.

## Disequazioni goniometriche con sostituzione

In maniera esattamente analoga alle equazioni, quando in una disequazione l'argomento delle funzioni goniometriche non è $x$ ma un suo multiplo, possiamo risolvere prima normalmente la disequazione e poi, nell'ultimo passaggio, trovare $x$.

$$
\cos 4x \le \frac{1}{2}
$$

> [!danger] Errore gravissimo!
> $$
> \frac{\cos 4x}{4} \le \frac{1}{2\cdot 4} \quad\longrightarrow\quad \cos x \le \frac{1}{8}
> $$

Abbiamo a disposizione un metodo utile che chiede di sostituire $4x = t$ e risolvere normalmente, per poi dividere la soluzione e trovare $x$.

$$
4x = t \qquad \cos(t) \le \frac{1}{2} \qquad \cos \text{ e } \frac{1}{2}\,? \longrightarrow \frac{\pi}{3}
$$

![Circonferenza: la retta t = 1/2, l'arco evidenziato va da π/3 a 5π/3 passando per π](disgonio-cos-4x.svg)

$$
\frac{\pi}{3} + 2k\pi \le t \le \frac{5}{3}\pi + 2k\pi
$$

$$
\frac{\frac{\pi}{3} + 2k\pi}{\textcolor{#22c55e}{4}} \le \frac{4x}{\textcolor{#22c55e}{4}} \le \frac{\frac{5}{3}\pi + 2k\pi}{\textcolor{#22c55e}{4}}
\qquad\longrightarrow\qquad
\frac{\pi}{12} + \frac{k\pi}{2} \le x \le \frac{5}{12}\pi + \frac{k\pi}{2}
$$

## Disequazioni riconducibili a 2° grado semplice

Il meccanismo di risoluzione è analogo a quello visto per le equazioni: cerchiamo una sostituzione che porti a scrivere una disequazione di secondo grado nell'incognita $t$, che sappiamo risolvere.

$$
\cos^2 x - \sin^2 x - \cos x + 1 \le 0
$$

Voglio scrivere tutto per avere solo $\cos(x)$:

$$
\sin^2 x + \cos^2 x = 1 \quad\longrightarrow\quad -\sin^2 x = \cos^2 x - 1
$$

$$
2\cos^2 x - \cos x \le 0 \qquad \boxed{\cos x = t} \;\; \textcolor{#22c55e}{\text{sostituzione}}
$$

$$
2t^2 - t \le 0 \quad\longrightarrow\quad \text{disequazione classica}
$$

$$
t_{1,2} = \frac{1 \pm \sqrt{1}}{4} = \begin{cases} \dfrac{1}{2} \\[4pt] 0 \end{cases}
$$

Siccome ho $\le$ $\longrightarrow$ **valori interni**:

$$
0 \le t \le \frac{1}{2} \quad\longrightarrow\quad 0 \le \cos x \le \frac{1}{2}
$$

A questo punto ho ottenuto una relazione sul coseno di $x$ che racchiude due disequazioni che devono essere soddisfatte contemporaneamente.

$$
\begin{cases}
\textcolor{#ef4444}{\cos x \ge 0} \;\longrightarrow\; 0 + 2k\pi \le x \le \dfrac{\pi}{2} + 2k\pi \;\;\vee\;\; \dfrac{3}{2}\pi + 2k\pi \le x \le 2\pi + 2k\pi \\[10pt]
\textcolor{#3b82f6}{\cos x \le \tfrac{1}{2}} \;\longrightarrow\; \dfrac{\pi}{3} + 2k\pi \le x \le \dfrac{5}{3}\pi + 2k\pi
\end{cases}
$$

A questo punto devo unire le due soluzioni in modo che siano verificate entrambe allo stesso momento.

![Schema del sistema: cos x ≥ 0 in [0, π/2] e [3π/2, 2π], cos x ≤ 1/2 in [π/3, 5π/3]; la soluzione comune è [π/3, π/2] e [3π/2, 5π/3]](disgonio-sistema.svg)

$$
\frac{\pi}{3} + 2k\pi \le x \le \frac{\pi}{2} + 2k\pi \quad \vee \quad \frac{3}{2}\pi + 2k\pi \le x \le \frac{5}{3}\pi + 2k\pi
$$

## Disequazioni frazionarie e prodotto

Quando si ha a che fare con disequazioni fratte o prodotto è fondamentale calcolare per prima cosa i periodi delle funzioni in ogni parte del prodotto o della frazione. Questo perché la disequazione poi andrà risolta nell'intervallo ottenuto facendo il m.c.m. tra i due periodi.

$$
\frac{\sin 2x}{2\cos x - \sqrt{3}} \le 0
$$

$$
\left.
\begin{aligned}
\sin 2x &\longrightarrow \text{periodo } T = \frac{2\pi}{2} = \pi \\
\cos x &\longrightarrow \text{periodo } T = 2\pi
\end{aligned}
\right\}\;\text{m.c.m. tra 1 e 2} \longrightarrow 2
\qquad\qquad T_{\text{tot}} = 2\pi
$$

**Separo numeratore e denominatore.**

*Numeratore*

$$
\sin 2x \ge 0 \qquad 2x = t \qquad \sin t \ge 0
$$

$$
0 + 2k\pi \le t \le \pi + 2k\pi
$$

$$
\frac{0 + 2k\pi}{\textcolor{#ef4444}{2}} \le \frac{2x}{\textcolor{#ef4444}{2}} \le \frac{\pi + 2k\pi}{\textcolor{#ef4444}{2}}
\quad\longrightarrow\quad 0 + k\pi \le x \le \frac{\pi}{2} + k\pi
$$

*Denominatore*

$$
2\cos x - \sqrt{3} > 0 \qquad \cos x > \frac{\sqrt{3}}{2}
$$

$$
0 + 2k\pi < x < \frac{\pi}{6} + 2k\pi \quad \vee \quad \frac{11}{6}\pi + 2k\pi < x < 2\pi + 2k\pi
$$

> [!warning] Attenzione
> La soluzione del numeratore è periodica in $k\pi$, mentre quella del denominatore lo è in $2k\pi$. È fondamentale che quando facciamo il grafico del segno mettiamo tutte le soluzioni nello stesso periodo.

$0 + k\pi \le x \le \frac{\pi}{2} + k\pi$ **va raddoppiata** per arrivare a $2\pi$:

![Da 0 a 2π il numeratore è positivo in [0, π/2] e in [π, 3π/2], negativo altrove](disgonio-raddoppio.svg)

$$
0 + 2k\pi \le x \le \frac{\pi}{2} + 2k\pi \quad \vee \quad \pi + 2k\pi \le x \le \frac{3}{2}\pi + 2k\pi
$$

**Segno:**

![Grafico del segno di N e D tra 0 e 2π; la frazione è negativa tra π/6 e π/2, tra π e 3π/2 e tra 11π/6 e 2π](disgonio-segno.svg)

$$
\frac{\pi}{6} + 2k\pi < x \le \frac{\pi}{2} + 2k\pi \;\;\vee\;\; \pi + 2k\pi \le x \le \frac{3}{2}\pi + 2k\pi \;\;\vee\;\; \frac{11}{6}\pi + 2k\pi < x \le 2\pi + 2k\pi
$$

In maniera del tutto analoga si risolvono le disequazioni prodotto, scomponendo nello studio dei due fattori separatamente.

## Disequazioni lineari in sin e cos

La logica con cui si risolvono è la stessa delle equazioni lineari in seno e coseno: si procede con la sostituzione $Y = \sin x$ e $X = \cos x$ e si risolve il sistema.

$$
\sin x + \cos x \ge -1
\qquad\longrightarrow\qquad
\begin{cases} Y + X \ge -1 \\ X^2 + Y^2 = 1 \end{cases}
$$

Trovo le intersezioni tra circonferenza e retta:

$$
\begin{cases} Y + X = -1 \\ X^2 + Y^2 = 1 \end{cases}
\qquad\longrightarrow\qquad (-1,\ 0) \qquad (0,\ -1)
$$

Quali sono gli angoli tali per cui:

$$
(-1,\ 0) \;\longrightarrow\; \cos\alpha = -1,\ \sin\alpha = 0 \;\longrightarrow\; \alpha = \pi
\qquad\qquad
(0,\ -1) \;\longrightarrow\; \cos\beta = 0,\ \sin\beta = -1 \;\longrightarrow\; \beta = \frac{3}{2}\pi
$$

La condizione chiede $X + Y \ge -1$, cioè la parte di piano sopra la retta:

![Circonferenza goniometrica e retta X + Y = −1: è evidenziata la parte sopra la retta, l'arco da 3π/2 a π passando per 0 e π/2](disgonio-lineare.svg)

Prendo tutti gli angoli nella parte evidenziata:

$$
0 + 2k\pi \le x \le \pi + 2k\pi \quad \vee \quad \frac{3}{2}\pi + 2k\pi \le x \le 2\pi + 2k\pi
$$

## Disequazioni di 2° grado in sin e cos

Quando abbiamo a che fare con una disequazione di secondo grado in seno e coseno dobbiamo prima di tutto essere sicuri di poterla scrivere in questa forma:

$$
a\sin^2 x + b\sin x\cos x + c\cos^2 x \ge 0
$$

Se ci fosse un $+d$ lo dovremmo scomporre con la relazione fondamentale della trigonometria:

$$
d = d\cdot\left(\sin^2 x + \cos^2 x\right)
$$

Una volta scritta nella forma corretta possiamo ricondurci a una disequazione in $\tan(x)$ dividendo ogni membro per $\cos^2(x)$:

$$
a\,\frac{\sin^2 x}{\cos^2 x} + b\,\frac{\sin x\cos x}{\cos^2 x} + c\,\frac{\cos^2 x}{\cos^2 x} \ge 0
\qquad\longrightarrow\qquad a\tan^2(x) + b\tan(x) + c \ge 0
$$

> [!warning] Attenzione
> Normalmente possiamo dividere una disequazione, senza dover girare il segno, solo per un numero positivo. Per questo motivo dividiamo per $\cos^2(x)$, che è sempre positivo o al massimo nullo.

> [!warning] Attenzione
> Quando dividiamo per $\cos^2(x)$ stiamo introducendo delle C.E. Quindi prima di dividere dobbiamo vedere se $\cos^2(x) = 0$ è soluzione da solo, poi facciamo le C.E. ed eventualmente alla fine scartiamo i valori che non vanno bene.

$$
\sin^2 x + \left(1 - \sqrt{3}\right)\sin x\cos x - \sqrt{3}\cos^2 x \ge 0
$$

Voglio dividere per $\cos^2 x$, ma prima verifico se $\cos^2 x = 0$ è soluzione:

$$
\sin^2 x + \left(1 - \sqrt{3}\right)\cdot\sin x\cdot 0 - \sqrt{3}\cdot 0 \ge 0
\qquad\longrightarrow\qquad \sin^2 x \ge 0
$$

$\cos^2 x = 0$ in $x = \frac{\pi}{2} + k\pi$, quindi verifico se

$$
\sin^2\left(\frac{\pi}{2}\right) \ge 0 \qquad 1 \ge 0 \;\checkmark\; \text{sì}
$$

$$
\Longrightarrow\quad \textcolor{#22c55e}{x = \frac{\pi}{2} + k\pi \text{ è soluzione}}
$$

Continuiamo con il resto:

$$
\tan^2(x) + \left(1 - \sqrt{3}\right)\tan(x) - \sqrt{3} \ge 0
$$

$$
\longrightarrow\quad -\frac{\pi}{2} + k\pi < x \le -\frac{\pi}{4} + k\pi \quad \vee \quad \frac{\pi}{3} + k\pi \le x < \frac{\pi}{2} + k\pi
$$

La soluzione $x = \frac{\pi}{2} + k\pi$ aggiunge un pezzo:

$$
-\frac{\pi}{2} + k\pi \;\textcolor{#22c55e}{\le}\; x \le -\frac{\pi}{4} + k\pi \quad \vee \quad \frac{\pi}{3} + k\pi \le x \;\textcolor{#22c55e}{\le}\; \frac{\pi}{2} + k\pi
$$
