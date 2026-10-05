---
title: Equazioni goniometriche
description: Come si risolvono le equazioni goniometriche elementari in seno, coseno e tangente, quelle con argomento diverso da x, di secondo grado, lineari e omogenee in seno e coseno.
tags:
  - matematica
  - goniometria
  - 4SCI
---
Come si risolvono le equazioni goniometriche elementari e avanzate.

> [!info] Collegamenti
> Servono le funzioni goniometriche, i valori notevoli e gli archi associati visti in [[Goniometria]]. Il passo successivo sono le [[Disequazioni goniometriche]].

## Equazioni elementari

Abbiamo visto che $\sin(x)$ e $\cos(x)$ rappresentano rispettivamente le ordinate e le ascisse di un punto appartenente a una circonferenza unitaria (segmento verticale e segmento orizzontale).

### sin(x) = m

![Circonferenza goniometrica: il punto P sulla retta y = m, il segmento rosso verticale è sin α](eqgonio-sin-punto.svg)

Fissato il punto $P$ io posso individuare l'ordinata (altezza) a cui si trova e questa corrisponde esattamente al seno dell'angolo che unisce il centro della circonferenza e $P$.

> [!warning] Attenzione
> Se io non conosco $P$ ma conosco solo il seno (quindi l'altezza) può esserci più di un punto che va bene.

![La retta y = m incontra la circonferenza in due punti: P all'angolo α e Q all'angolo π − α](eqgonio-sin-due-punti.svg)

In questo caso ho esattamente 2 punti che hanno la stessa $y = m$, quindi entrambi sono soluzione di $\sin(x) = m$. Se ricordate gli archi associati, $\sin(x) = \sin(\pi - x)$, che è proprio il nostro caso: infatti $Q$ si trova a un angolo $\pi - \alpha$ mentre $P$ si trova a un angolo $\alpha$ e le loro altezze (i seni) sono identiche.

#### 3 casi possibili

**$m > 1$**

![La retta y = m passa sopra la circonferenza](eqgonio-sin-m-maggiore.svg)

Se traccio la retta orizzontale $y = m$ non interseco mai la circonferenza e quindi non esiste nessun angolo $x$ tale per cui $\sin(x) = m$: **impossibile**.

**$-1 \le m \le 1$**

![La retta y = m taglia la circonferenza agli angoli α e π − α](eqgonio-sin-m-intermedio.svg)

Ho due soluzioni possibili, una in $\alpha$ e l'altra in $\pi - \alpha$, quindi scriverò:

$$
x = \alpha + \textcolor{#22c55e}{2k\pi} \quad \vee \quad x = \pi - \alpha + \textcolor{#22c55e}{2k\pi}
$$

Perché mettiamo $2k\pi$? Perché abbiamo visto che la funzione seno è periodica con periodo $2\pi$: mettendo solo una soluzione perderemmo tutte le sue copie.

**$m < -1$**

![La retta y = m passa sotto la circonferenza](eqgonio-sin-m-minore.svg)

Se traccio la retta orizzontale $y = m$ non interseco mai la circonferenza e quindi non esiste nessun angolo $x$ tale per cui $\sin(x) = m$: **impossibile**.

#### Come trovo l'angolo α da mettere nella soluzione?

Se il valore di $m$ che otteniamo è uno di quei valori speciali per le funzioni periodiche, sappiamo direttamente l'angolo. I valori speciali sono

$$
\pm\frac{1}{2} \qquad \pm\frac{\sqrt{2}}{2} \qquad \pm\frac{\sqrt{3}}{2} \qquad \pm 1 \qquad 0
$$

Per esempio:

$$
\begin{aligned}
\sin(\,?\,) = \tfrac{1}{2} &\longrightarrow \tfrac{\pi}{6} \quad (30^\circ) \\
\sin(\,?\,) = \tfrac{\sqrt{2}}{2} &\longrightarrow \tfrac{\pi}{4} \quad (45^\circ) \\
\sin(\,?\,) = \tfrac{\sqrt{3}}{2} &\longrightarrow \tfrac{\pi}{3} \quad (60^\circ) \\
\sin(\,?\,) = 1 &\longrightarrow \tfrac{\pi}{2} \quad (90^\circ)
\end{aligned}
$$

**Se ho il segno −?** Se $m$ fosse un valore negativo non c'è da preoccuparsi: l'angolo di riferimento è lo stesso del $+$, ma sarà messo da qualche altra parte.

![Retta m = 1/2: angolo di 30° sopra l'asse x](eqgonio-sin-30.svg)

$$
\sin\left(\frac{\pi}{6}\right) = \frac{1}{2} \;\checkmark
$$

![Retta m = −1/2: angolo di 30° sotto l'asse x](eqgonio-sin-meno-30.svg)

$$
\sin\left(-\frac{\pi}{6}\right) = -\frac{1}{2} \;\checkmark
$$


In questo caso con $m = -1/2$ avrò sempre a che fare con un angolo da $30^\circ$. Prima disegno la retta $y = m$, poi individuo dove si trova l'angolo di $30^\circ$ che mi aspetto.

#### Se il valore di m non è uno dei valori speciali?

Se $m$ non è uno dei valori speciali allora sarà sufficiente usare la calcolatrice e calcolare $\arcsin(m)$ (sulla calcolatrice è scritto come $\sin^{-1}$): questo mi darà l'angolo relativo. Il resto del procedimento è uguale.

$$
m = \frac{2}{3} \longrightarrow \arcsin\left(\frac{2}{3}\right) = 41{,}8^\circ
$$

![Retta m = 2/3: le soluzioni sono 41,8° e 180° − 41,8°](eqgonio-sin-arcsin.svg)

### cos(x) = m

Come abbiamo visto con $\sin(x) = m$, ora vediamo le equazioni elementari con $\cos(x)$. Dato un punto $P$, il coseno rappresenta l'ascissa del punto $P$ (la coordinata $x$).

![Circonferenza goniometrica: il segmento blu orizzontale è cos α, l'ascissa di P](eqgonio-cos-punto.svg)

Anche in questo caso, se conosco il punto $P$ vedo subito che l'ascissa del punto $P$ è il $\cos(\alpha)$.

> [!warning] Attenzione
> Se però conosco solo il valore di $\cos(x) = m$ individuo due punti che soddisfano la condizione $\cos(x) = m$.

![La retta verticale x = m incontra la circonferenza in P (angolo α) e in Q (angolo −α)](eqgonio-cos-due-punti.svg)

Ricordando le relazioni degli archi associati sappiamo che $\cos(\alpha) = \cos(-\alpha)$: infatti i due angoli che portano ad avere lo stesso coseno sono proprio $\alpha$ e $-\alpha$, cioè $2\pi - \alpha$. Le soluzioni dell'equazione sono:

$$
x = \alpha + \textcolor{#22c55e}{2k\pi} \quad \vee \quad x = 2\pi - \alpha + \textcolor{#22c55e}{2k\pi}
$$

Il motivo del $2k\pi$ è lo stesso che abbiamo visto per le equazioni con il seno. In questo caso abbiamo $\alpha$ e $-\alpha$ come soluzioni.

#### 3 casi possibili

**$m > 1$**

![La retta verticale x = m passa a destra della circonferenza](eqgonio-cos-m-maggiore.svg)

Se traccio la retta verticale $x = m$ non interseco mai la circonferenza e quindi non esiste nessun angolo $x$ tale per cui $\cos(x) = m$: **impossibile**.

**$-1 \le m \le 1$**

![La retta x = m taglia la circonferenza agli angoli α e −α](eqgonio-cos-m-intermedio.svg)

Ho due soluzioni possibili, una in $\alpha$ e l'altra in $-\alpha$ (cioè $2\pi - \alpha$), quindi scriverò:

$$
x = \alpha + \textcolor{#22c55e}{2k\pi} \quad \vee \quad x = 2\pi - \alpha + \textcolor{#22c55e}{2k\pi}
$$

Perché mettiamo $2k\pi$? Perché anche la funzione coseno è periodica con periodo $2\pi$: mettendo solo una soluzione perderemmo tutte le sue copie.

**$m < -1$**

![La retta verticale x = m passa a sinistra della circonferenza](eqgonio-cos-m-minore.svg)

Se traccio la retta verticale $x = m$ non interseco mai la circonferenza e quindi non esiste nessun angolo $x$ tale per cui $\cos(x) = m$: **impossibile**.

> [!tip] Il metodo per trovare α è lo stesso del seno
> Valori speciali → angolo noto; altrimenti $\alpha = \arccos(m)$ con la calcolatrice ($\cos^{-1}$).

### tan(x) = m

Quando abbiamo a che fare con seno e coseno il valore di $m$ deve essere limitato tra $-1$ e $1$; per la tangente invece possiamo avere qualunque valore.

![La tangente di α è il segmento verde sulla retta tangente alla circonferenza in (1, 0)](eqgonio-tan-punto.svg)

Conoscendo il punto $P$ e il suo angolo $\alpha$, la tangente dell'angolo è il segmento verde, che può essere nella direzione positiva o negativa e può assumere qualunque valore.

Anche in questo caso osserviamo il valore numerico della tangente e proviamo a vedere se è uno di quelli speciali, come

$$
0 \qquad \pm\sqrt{3} \qquad \pm 1 \qquad \pm\frac{\sqrt{3}}{3}
$$

Se non è uno di questi valori facciamo come per seno e coseno: sulla calcolatrice calcoliamo $\arctan(m) = \alpha$ e abbiamo la soluzione.

#### Come risolviamo l'equazione?

![La retta per l'origine e per il valore m = tan α incontra la circonferenza in P (angolo α) e Q (angolo π + α)](eqgonio-tan-due-punti.svg)

Traccio la retta che passa per il valore della tangente $= m$ e per il centro della circonferenza. Questa retta incontrerà sempre la circonferenza in 2 punti: uno dei due è $\alpha$, l'altro è $\pi + \alpha$. Quello che possiamo osservare è che la tangente, diversamente da seno e coseno, è periodica in un intervallo $\pi$ piuttosto che $2\pi$.

![Grafico di tan(x): si ripete uguale ogni π](eqgonio-tan-grafico.svg)

La tangente è **periodica in $\pi$**:

$$
x = \alpha + 2k\pi \quad \vee \quad x = \pi + \alpha + 2k\pi
$$

e queste soluzioni si uniscono in

$$
x = \alpha + k\pi
$$

## Equazioni elementari con argomento diverso da x

Se nell'argomento di seno, coseno o tangente non c'è $x$ ma un suo multiplo (es. $2x$, $\frac{1}{2}x$, …) risolviamo normalmente l'equazione ottenendo la soluzione, per esempio:

$$
\frac{2x}{\textcolor{#ef4444}{2}} = \frac{\alpha}{\textcolor{#ef4444}{2}} + \frac{2k\pi}{\textcolor{#ef4444}{2}} \quad \vee \quad \frac{2x}{\textcolor{#ef4444}{2}} = \frac{2\pi}{\textcolor{#ef4444}{2}} - \frac{\alpha}{\textcolor{#ef4444}{2}} + \frac{2k\pi}{\textcolor{#ef4444}{2}}
$$

$$
\longrightarrow\quad x = \frac{\alpha}{2} + k\pi \quad \vee \quad x = \pi - \frac{\alpha}{2} + k\pi
$$

Scrivo la soluzione con il multiplo di $x = \dots$ e poi divido o moltiplico in modo da ottenere $x = \dots$

## Equazioni riconducibili a equazioni elementari

### Equazioni di 2° grado solo in sin, cos o tan

Consideriamo delle equazioni che abbiano **solo** coseno, solo seno o solo tangente al loro interno, fino al massimo della seconda potenza.

$$
2\cos^2 x - \cos x - 1 = 0
$$

$$
\cos x = t \quad\longrightarrow\quad 2t^2 - t - 1 = 0
$$

$$
t_{1,2} = \frac{1 \pm \sqrt{1 + 8}}{4} = \begin{cases} -\dfrac{1}{2} \\[4pt] 1 \end{cases}
$$

$$
t = 1 \quad \vee \quad t = -\frac{1}{2}
\qquad\longrightarrow\qquad
\cos x = 1 \quad \vee \quad \cos x = -\frac{1}{2}
$$

A questo punto ho ottenuto due equazioni separate che devono essere risolte separatamente. Per seno e tangente si risolve in maniera analoga con la sostituzione $\sin(x) = t$ oppure $\tan(x) = t$.

### Equazioni riconducibili a elementari tramite sin²x + cos²x = 1

$$
3\sin^2 x + 2\cos^2 x - 2 = \sin x
$$

So che $\sin^2 x + \cos^2 x = 1$:

$$
\begin{aligned}
\sin^2 x + 2\sin^2 x + 2\cos^2 x - 2 &= \sin x \\
\sin^2 x + 2\cdot\underbrace{\left(\sin^2 x + \cos^2 x\right)}_{=\,1} - 2 &= \sin x \\
\sin^2 x + \cancel{2} - \cancel{2} &= \sin x
\end{aligned}
\qquad\longrightarrow\qquad \sin^2 x - \sin x = 0
$$

## Equazioni lineari in sin e cos

Sono equazioni in cui sono presenti sia seno che coseno allo stesso momento, ed entrambi alla prima potenza.

### a sin x + b cos x = 0

Osservo che posso dividere entrambi i membri per $\cos(x)$, in modo da ottenere $\tan(x)$ da una parte, mentre dall'altra parte ottengo $b$.

$$
a\,\frac{\sin x}{\textcolor{#ef4444}{\cos x}} + b\,\frac{\cos x}{\textcolor{#ef4444}{\cos x}} = \frac{0}{\textcolor{#ef4444}{\cos x}}
\qquad\longrightarrow\qquad a\tan x + b = 0
$$

> [!warning] Attenzione
> Quando dividiamo per $\cos(x)$ **dobbiamo** modificare le C.E. Se normalmente $\cos x$ e $\sin x$ non hanno problemi, quando metto $\cos x$ al denominatore devo chiedere:
>
> $$
> \text{C.E.}\quad \cos x \neq 0 \qquad x \neq \frac{\pi}{2} + k\pi
> $$
>
> Dopo aver imposto le C.E. risolvo l'equazione e alla fine confronto il risultato con le C.E. per vedere se è accettabile. **Importantissimo** verificare poi a parte se $\cos x = 0$ sia o no soluzione (basta sostituire): dobbiamo farlo perché nelle C.E. lo abbiamo escluso.

### a sin x + b cos x + c = 0

Qui ho anche $c$, quindi dividere per $\cos x$ non mi conviene, perché rimarrei con $c/\cos(x)$.

$\longrightarrow$ **Metodo grafico**: chiamo $Y = \sin x$ e $X = \cos x$ e metto a sistema l'equazione con la relazione fondamentale.

$$
\begin{cases} a\sin x + b\cos x + c = 0 \\ \sin^2 x + \cos^2 x = 1 \end{cases}
\qquad\longrightarrow\qquad
\begin{cases} aY + bX + c = 0 \\ Y^2 + X^2 = 1 \end{cases}
$$

La prima è una retta, la seconda la circonferenza goniometrica: le soluzioni sono gli angoli dei punti in cui la retta taglia la circonferenza.

![La retta aY + bX + c = 0 taglia la circonferenza nei punti agli angoli α e β](eqgonio-lineare.svg)

$$
x = \alpha + 2k\pi \quad \vee \quad x = \beta + 2k\pi
$$

## Equazioni omogenee di 2° grado in sin e cos

Prima abbiamo visto equazioni di secondo grado dove compariva una sola tipologia di funzione periodica: o solo seno, o solo coseno, o solo tangente. In questo caso consideriamo equazioni di secondo grado che abbiano un mix di funzioni trigonometriche:

$$
a\sin^2 x + b\sin x\cos x + c\cos^2 x = 0
$$

- Se manca $c$, raccolgo $\sin x$:

  $$
  a\sin^2 x + b\sin x\cos x = 0 \quad\longrightarrow\quad \sin x\,(a\sin x + b\cos x) = 0
  $$

  $$
  \sin x = 0 \quad \vee \quad a\sin x + b\cos x = 0
  $$

- Se manca $a$, raccolgo $\cos x$:

  $$
  b\sin x\cos x + c\cos^2 x = 0 \quad\longrightarrow\quad \cos x\,(b\sin x + c\cos x) = 0
  $$

  $$
  \cos x = 0 \quad \vee \quad b\sin x + c\cos x = 0
  $$

- Se ci sono tutti e tre i termini, divido per $\cos^2 x$ e ottengo un'equazione di secondo grado in $\tan x$:

  $$
  a\,\frac{\sin^2 x}{\textcolor{#ef4444}{\cos^2 x}} + b\,\frac{\sin x\cos x}{\textcolor{#ef4444}{\cos^2 x}} + c\,\frac{\cos^2 x}{\textcolor{#ef4444}{\cos^2 x}} = \frac{0}{\textcolor{#ef4444}{\cos^2 x}}
  \quad\longrightarrow\quad a\tan^2 x + b\tan x + c = 0
  $$

> [!warning] Attenzione
> Anche qui vanno fatte le C.E. e poi bisogna verificare se $\cos^2 x = 0$ è soluzione, esattamente come nel caso precedente.

## Equazioni complete di 2° grado

$$
a\sin^2 x + b\sin x\cos x + c\cos^2 x + d = 0
$$

Uso

$$
d = d\cdot 1 = d\left(\cos^2 x + \sin^2 x\right) = d\cos^2 x + d\sin^2 x
$$

$$
\textcolor{#f59e0b}{a\sin^2 x} + b\sin x\cos x + \textcolor{#ef4444}{c\cos^2 x} + \textcolor{#ef4444}{d\cos^2 x} + \textcolor{#f59e0b}{d\sin^2 x} = 0
$$

$$
(a + d)\sin^2 x + b\sin x\cos x + (c + d)\cos^2 x = 0
$$

Questa la risolvo come un'equazione omogenea di secondo grado, con i metodi visti sopra.
