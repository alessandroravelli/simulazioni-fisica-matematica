---
title: Relatività
description: Trasformazioni di Galileo, ipotesi dell'etere e Michelson-Morley, assiomi della relatività ristretta, simultaneità, dilatazione dei tempi, contrazione delle lunghezze, muoni, trasformazioni di Lorentz, composizione delle velocità, invariante relativistico, diagrammi di Minkowski, equivalenza massa-energia.
tags:
  - fisica
  - relatività
  - 5SCI
---
Nel 1905 Albert Einstein si rende conto che la fisica del tempo aveva prodotto una fortissima inconsistenza. La meccanica galileiana, su cui si basano tutti gli studi del moto fatti fino a quel tempo, non poteva essere d'accordo con l'elettromagnetismo formalizzato poco prima da James Clerk Maxwell (vedi [[Elettromagnetismo e Maxwell]]).

## Trasformazioni di Galileo

Consideriamo per semplicità un movimento in una sola direzione.

![Un vagone si muove con velocità v rispetto al sistema S; il sistema S′ è solidale con il vagone e contiene una palla](treno-galileo.svg)

In questa configurazione sappiamo che la carrozza del treno si sta muovendo con una velocità $v$ rispetto al sistema di riferimento $S$. Consideriamo la posizione della palla da basket nel sistema di riferimento $S$ e nel sistema di riferimento $S'$.

| | $t = 0$ | $t = 1\ \text{s}$ |
| --- | --- | --- |
| Posizione in $S$ (con $v = 5\ \text{m/s}$ in direzione $x$ positiva) | $(13, 4)$ | $(13 + 5, 4) = (18, 4)$ |
| Posizione in $S'$ | $(4, 4)$ | $(4, 4)$ … |

Quello che vediamo è che, dal momento che il treno si sposta, in uno dei due sistemi di riferimento le coordinate della palla da basket cambiano ogni secondo, mentre nell'altro sistema di riferimento, ovvero quello di chi sta sul treno, dove la palla è ferma, le coordinate sono sempre le stesse.

$$
\begin{cases}
x = x' + v \cdot \Delta t \\
y = y' \\
z = z' \\
t = t'
\end{cases}
$$

In questo caso consideriamo appunto soltanto il movimento sull'asse delle $x$. Questo significa che le coordinate $y$, $z$ e temporali sono condivise da entrambi i sistemi di riferimento.

La relatività di Galileo funziona perfettamente per tutta la meccanica classica e anche per le onde meccaniche, tra cui per esempio il suono.

$$
\text{Per un'onda meccanica:} \quad v^2 \propto \frac{k}{d} \qquad k := \text{compressibilità} \qquad d := \text{densità}
$$

Consideriamo un mezzo fermo, come può essere in prima approssimazione una massa d'aria in quiete. La velocità con cui un'onda meccanica si propaga all'interno del mezzo (in questo caso l'aria) è inversamente proporzionale alla densità dell'aria stessa ed è direttamente proporzionale alla capacità del materiale di comprimersi.

<span style="color:#f59e0b">La velocità di un'onda è legata a un mezzo.</span>

**In elettromagnetismo**

$$
v = \frac{1}{\sqrt{\varepsilon_0\,\mu_0}} \quad \text{ma nel vuoto non c'è mezzo}
$$

Se per il suono $v = 340\ \text{m/s}$ rispetto all'aria "ferma", $c = 2{,}9 \cdot 10^8\ \text{m/s}$ è rispetto a cosa?

## Ipotesi dell'etere

Esattamente come succede per le onde meccaniche, si è ipotizzata l'esistenza di un mezzo chiamato **etere**, rispetto a cui la luce ha la sua velocità. Quest'ipotesi però porta un'importantissima conseguenza: se effettivamente la luce si muove attraverso l'etere, questo significa che diversi osservatori in moto o in quiete dovrebbero osservare velocità della luce diverse, esattamente come succede per il suono con la relatività galileiana, di cui vediamo un esempio adesso.

![Una pistola spara un proiettile con velocità v](proiettile.svg)

Un proiettile viene sparato con velocità $\vec v$:

- per chi è fermo il proiettile ha velocità $+\vec v$;
- se corro nella stessa direzione del proiettile vedo $+\vec v - \vec v_c$;
- se corro nella direzione opposta vedo $+\vec v + \vec v_c$.

<span style="color:#f59e0b">Considero il Sole fermo nel sistema di riferimento dell'etere.</span> Per il Sole la luce ha velocità $c = 2{,}9 \cdot 10^8\ \text{m/s}$. E per noi sulla Terra?

### L'interferometro di Michelson e Morley

In laboratorio, sulla Terra che si muove con velocità $\vec v$ rispetto all'etere, un fascio di luce viene diviso in due da uno specchio semitrasparente $H$ e mandato su due bracci lunghi entrambi $\ell$.

**Braccio parallelo al moto** ($\overline{AH} = \ell$).

![Il Sole fermo nell'etere, la Terra che si muove con velocità v e il braccio dell'interferometro tra lo specchio H e lo specchio A, parallelo a v](interferometro-parallelo.svg)

Velocità osservata dalla Terra:

$$
H \to A: \ \vec c - \vec v \qquad A \to H: \ \vec c + \vec v
$$

Tempo di andata e ritorno:

$$
\Delta t_1 = \frac{\ell}{c - v} + \frac{\ell}{c + v} = \frac{c\ell + \ell v + \ell c - \ell v}{c^2 - v^2} = \frac{2\ell c}{c^2 - v^2} = \frac{2\ell}{c} \cdot \frac{1}{1 - \frac{v^2}{c^2}}
$$

**Braccio perpendicolare al moto** ($\overline{HB} = \ell$).

![Il braccio tra lo specchio H e lo specchio B, perpendicolare a v: nel laboratorio la luce va in orizzontale con velocità u, rispetto all'etere in diagonale con velocità c](interferometro-perpendicolare.svg)
 Quando osservo la luce nel laboratorio $\vec u$ è orizzontale ed è la velocità della luce rispetto alla Terra, $\vec v$ è la velocità della Terra rispetto all'etere e $\vec c$ è la velocità della luce rispetto all'etere.

$$
\vec u = \vec c - \vec v \quad\Longrightarrow\quad u = \sqrt{c^2 - v^2}
$$

Tempo di andata e ritorno:

$$
\Delta t_2 = \frac{2\ell}{u} = \frac{2\ell}{c} \cdot \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}
$$

$$
\Delta t_1 - \Delta t_2 = \frac{2\ell}{c}\left(\frac{1}{1 - \frac{v^2}{c^2}} - \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}\right)
$$

Se ruoto l'interferometro $\Delta t_1 - \Delta t_2$ cambia, e anche l'interferenza cambia.

$\longrightarrow$ <span style="color:#f59e0b">Michelson e Morley non osservano oscillazione: l'etere non esiste, $\vec v = 0$.</span>

Se la luce non è legata a un mezzo, $c$ è uguale ovunque?

## Assiomi della relatività ristretta

1. Le leggi e i principi della fisica hanno la stessa forma in tutti i sistemi di riferimento inerziali.
2. Il valore della velocità della luce nel vuoto è lo stesso in tutti i sistemi di riferimento inerziali, indipendentemente dal moto del sistema o da quello della sorgente che la emette.

## Eventi simultanei

Due eventi si dicono simultanei se i segnali luminosi da essi prodotti giungono nello stesso istante in un punto specifico equidistante dall'origine dei segnali. Per esempio, due laser a 8 m di distanza da un osservatore, da parti opposte, accesi nello stesso istante.

![Due laser a 8 m da un osservatore, da parti opposte](simultaneita-laser.svg)

**Cosa succede se mi muovo?** Due lampade sono a 10 m da un osservatore fermo a terra; sopra di lui passa un treno con un secondo osservatore.

**Tutto fermo $\rightarrow$ tutto simultaneo.**

![Treno fermo: i segnali delle due lampade arrivano insieme sia all'osservatore a terra sia a quello sul treno](simultaneita-fermo.svg)

**Il treno si muove verso destra con velocità $\vec v$.**

![Treno in moto: l'osservatore sul treno incontra prima la luce che arriva da destra](simultaneita-moto.svg)

L'osservatore che sta sul treno si muove in direzione della luce che arriva da destra. Questo significa che, al momento dell'accensione delle luci, lui incontrerà prima la luce che arriva da destra, verso cui si sta muovendo, e dopo quella che arriva da sinistra, da cui si allontana. Ciò significa che per uno dei due osservatori (quello fermo) i due eventi sono simultanei, mentre per l'osservatore in moto i due eventi non sono simultanei. Nella vita di tutti i giorni questa differenza non la vediamo perché la velocità della luce è altissima rispetto alle velocità a cui siamo abituati, e infatti se la velocità della luce fosse infinita tutti gli osservatori vedrebbero gli eventi simultanei. Quando però si ha a che fare con velocità molto elevate, la differenza di simultaneità è osservabile.

## Dilatazione dei tempi

Ora che è chiaro che due osservatori diversi hanno descrizioni diverse, introduciamo il primo effetto collaterale della relatività di Einstein, ovvero la dilatazione dei tempi. Quando abbiamo rivisto la relatività di Galileo avevamo imposto che le coordinate temporali dei due sistemi fossero sempre identiche: questo significa che due osservatori diversi misurano sempre gli stessi tempi. Nella relatività speciale la richiesta di avere la velocità della luce fissa per tutti fa sì che i tempi non siano più uguali per tutti.

![A sinistra la luce sale e scende in verticale nel carrello; a destra, vista da fuori, percorre un tragitto obliquo più lungo mentre il carrello avanza](dilatazione-tempi.svg)

**Sono sul carrello** e calcolo il tempo che ci mette la luce a rimbalzare sullo specchio:

$$
\Delta t = \frac{2\,\overline{AB}}{c} = \frac{2\ell}{c}
$$

**Sono fuori dal carrello**:

$$
\Delta t' = \frac{\overline{AB'}}{c} + \frac{\overline{B'A''}}{c} \qquad \text{se } \overline{AB'} = \overline{B'A''} \qquad \Delta t' = \frac{2\,\overline{AB'}}{c} \qquad \overline{AB'}^2 = \overline{AA'}^2 + \overline{A'B'}^2
$$

So che:

$$
\overline{AA''} = v\,\Delta t' \qquad \overline{AA'} = \frac{v\,\Delta t'}{2}
$$

$\overline{AB'}$ è percorso dalla luce in $\dfrac{\Delta t'}{2}$:

$$
\Longrightarrow\quad \left(c\,\frac{\Delta t'}{2}\right)^2 = \left(\frac{v\,\Delta t'}{2}\right)^2 + \left(\frac{c\,\Delta t}{2}\right)^2
$$

$$
\left(c^2 - v^2\right)\Delta t'^2 = c^2\,\Delta t^2 \quad\longrightarrow\quad \Delta t' = \frac{1}{\sqrt{1 - v^2/c^2}}\,\Delta t
$$

$$
\longrightarrow\quad \textcolor{#f59e0b}{\Delta t' = \frac{1}{\sqrt{1 - \beta^2}}\,\Delta t = \gamma\,\Delta t} \qquad \gamma := \text{fattore di Lorentz} \qquad \gamma \ge 1
$$

Quello che possiamo osservare dalla formula sulla dilatazione dei tempi è che la richiesta che la radice esista si traduce nel fatto che la velocità con cui il carrello si muove deve essere obbligatoriamente più piccola della velocità della luce, altrimenti violiamo le condizioni di esistenza.

$\Delta t$, misurato sul carrello e quindi solidale con la luce, è il **tempo proprio**.

## Contrazione delle lunghezze

Il secondo effetto collaterale della relatività ristretta è la contrazione delle lunghezze. Nella relatività galileiana due osservatori diversi erano d'accordo che una porzione di spazio avesse una lunghezza determinata. Nella relatività ristretta invece due osservatori diversi osservano porzioni di spazio di lunghezze diverse.

**Osservatore fuori dal carrello.** Un carrello con velocità $\vec v$ percorre il tratto di strada tra $x_1$ e $x_2$, lungo $\Delta x$.

![Un carrello in moto percorre il tratto di strada tra x1 e x2](contrazione-strada.svg)

 Se sono fuori dal carrello misuro $\Delta t'$ e $\Delta x$:

$$
\Longrightarrow\quad \Delta x = v \cdot \Delta t' = v\,\gamma\,\Delta t
$$

**Osservatore sul carrello**

$$
\Delta x' = v\,\Delta t \quad\longrightarrow\quad \Delta t = \frac{\Delta x'}{v}
$$

$$
\longrightarrow\quad \Delta x = v\,\gamma\,\frac{\Delta x'}{v} = \gamma\,\Delta x' \quad\Longrightarrow\quad \textcolor{#f59e0b}{\Delta x' = \frac{\Delta x}{\gamma}} \qquad \Delta x' < \Delta x
$$

Prima abbiamo visto che l'osservatore solidale con il sistema di riferimento che si muove (ovvero il carrello) misura un tempo inferiore a quello che misura l'osservatore fuori dal carrello. Allo stesso tempo, però, l'osservatore dentro il carrello misura uno spazio più corto.

- $\Delta t$ era proprio perché era misurato solidale con il carrello.
- $\Delta x$ è proprio perché è misurato solidale con la strada.

> [!warning] Attenzione
> La contrazione delle lunghezze avviene **solo** lungo la direzione di movimento.

## Test di conferma della relatività ristretta

Il mondo subatomico è composto da una selezione di particelle elementari; tra queste è presente il **muone**:

$$
\mu^- \xrightarrow{\ \tau\, =\, 2{,}2\ \mu\text{s}\ } e^- + \nu_\mu + \bar\nu_e
$$

Questa particella può essere prodotta da molte reazioni che avvengono sia nell'universo sia direttamente nell'atmosfera terrestre, e in particolare sappiamo che non è una particella stabile. Questo vuol dire che dovrà trasformarsi e decadere in qualcos'altro di stabile: quello che sappiamo è che la vita media del muone è di $2{,}2\ \mu\text{s}$.

Consideriamo $v = 0{,}9992\,c$ (il 99,92% di $c$), cioè $0{,}9992 \cdot 3 \cdot 10^8\ \text{m/s}$.

**Trascuriamo la relatività**

$$
\Delta x = v \cdot \Delta t = 0{,}9992\,c \cdot \tau = 659{,}5\ \text{m}
$$

Se non consideriamo la relatività, le particelle sarebbero in grado di percorrere circa 600 m prima di cessare di esistere; però sappiamo che l'atmosfera dove vengono prodotte queste particelle è spessa circa 10 km. Il fatto è che noi a terra, con i giusti rivelatori, riusciamo a osservare queste particelle. Come fanno ad arrivare a noi?

**Consideriamo la relatività**

$$
\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} = \frac{1}{\sqrt{1 - (0{,}9992)^2}} = 25
$$

Sul muone $\Delta t = \tau$; calcolo $\Delta t'$:

$$
\Delta t' = \gamma\,\Delta t = 25 \cdot 2{,}2\ \mu\text{s} = 55\ \mu\text{s}
$$

$$
\Delta x' = v \cdot \Delta t' = 0{,}9992 \cdot c \cdot 55\ \mu\text{s} = 16{,}5\ \text{km}
$$

Nel sistema di riferimento della Terra il muone percorre 16,5 km. Nel sistema del muone invece l'atmosfera è contratta:

$$
\Delta x' = 16{,}5\ \text{km} = \gamma\,\Delta x \quad\longrightarrow\quad \Delta x = \frac{16{,}5\ \text{km}}{25} = 660\ \text{m}
$$

## Trasformazioni di Lorentz

A questo punto abbiamo capito come le lunghezze e i tempi vengono modificati quando i due osservatori si trovano in condizioni diverse. Adesso però vorremmo trovare un modo per descrivere la posizione di un oggetto in movimento osservata da un osservatore oppure da un altro, esattamente come avevamo fatto con Galileo.

$$
\text{Galileo:} \quad
\begin{cases}
x = x' + v \cdot \Delta t \\
y = y' \\
z = z' \\
t = t'
\end{cases}
$$

Con le giuste considerazioni, se $S$ e $S'$ a $t = 0\ \text{s}$ sono nella stessa posizione ($x = x' = 0$, $y = y' = 0$, $z = z' = 0$ a $t = 0\ \text{s}$):

$$
\textcolor{#f59e0b}{
\begin{cases}
x' = \gamma\,(x - v t) \\
y' = y \\
z' = z \\
t' = \gamma\left(t - \beta\,\dfrac{x}{c}\right)
\end{cases}}
$$

se $\vec v$ è diretta nel verso positivo delle $x$ (se $\vec v$ cambia, cambio il segno).

Le trasformazioni opposte (conosco $x'$ e non conosco $x$) si ottengono scambiando gli apici e il segno di $\vec v$: vedere $S'$ che si allontana da $S$ con velocità $\vec v$ è come vedere $S$ che si allontana da $S'$ con velocità $-\vec v$.

![S′ che si muove con velocità v rispetto a S equivale a S che si muove con velocità −v rispetto a S′](sistemi-v.svg)

La relatività non predilige un sistema di riferimento inerziale rispetto all'altro.

> [!warning] Il limite di Galileo
> Se $v \ll c$, $\gamma \sim 1$ e ottengo Galileo.

Se uso Lorentz posso ricavare $\Delta t' = \gamma\,\Delta t$ e $\Delta x = \gamma\,\Delta x'$.

## Composizione delle velocità

Come le posizioni si compongono, lo fanno anche le velocità. Sia $\vec w'$ la velocità di un punto $P$ in $S'$ e $\vec w$ la velocità di $P$ in $S$.

![Il sistema S′ si muove con velocità v rispetto a S; il punto P ha velocità w′ in S′](composizione-velocita.svg)

$\vec w = \vec v + \vec w'$ secondo Galileo, che non tiene conto di $c$.

Supponiamo che $v = \frac{2}{3}c$ e $w' = \frac{2}{3}c$ $\rightarrow$ $w = \frac{4}{3}c > c$: **vietato dalla relatività**, Galileo non funziona.

$$
x' = w' t' \quad \text{legge oraria in } S' \quad x'(0) = 0 \qquad x = w t
$$

$$
x' = \gamma\,(x - v t) \qquad t' = \gamma\left(t - \frac{\beta}{c}\,x\right)
$$

$$
\longrightarrow\quad \cancel{\gamma}\,(x - v t) = w'\,\cancel{\gamma}\left(t - \frac{\beta}{c}\,x\right) \qquad w\cancel{t} - v\cancel{t} = w'\cancel{t} - \frac{v}{c^2}\, w\cancel{t}
$$

$$
\textcolor{#f59e0b}{w = \frac{w' + v}{1 + w'\,\frac{v}{c^2}}} \qquad \text{analogamente} \qquad w' = \frac{w - v}{1 - w\,\frac{v}{c^2}}
$$

- Se $v,\ w' \ll c$: $w'\,\dfrac{v}{c^2} \sim 0$ $\Rightarrow$ $w = w' + v$ (Galileo).
- Se $w' = c$: $w = \dfrac{c + v}{1 + v/c} = c$.

> [!example] Esempio
> $S'$ si muove con velocità $-\vec v$ (verso sinistra) e il punto con velocità $\vec w$ verso destra: $w = \frac{2}{3}c$, $v = \frac{2}{3}c$. Quanto vale $w'$?
>
> ![S′ si muove verso sinistra con velocità −v, il punto verso destra con velocità w](composizione-esempio.svg)
>
> $w' = \dfrac{w - v}{1 - w\frac{v}{c^2}}$ vale se $v$ e $w$ hanno lo stesso verso; altrimenti
>
> $$
> w' = \frac{w + v}{1 + w\frac{v}{c^2}} = \frac{\frac{2}{3}c + \frac{2}{3}c}{1 + \frac{4}{9}\,c^2/c^2} = \frac{4/3}{13/9}\,c = \frac{12}{13}\,c
> $$

## Invariante relativistico

In 2D possiamo calcolare la lunghezza di un segmento $\vec s$ di componenti $(3, 4)$:

$$
s = \sqrt{3^2 + 4^2} = \sqrt{25} = 5
$$

Ora teniamo fermo $\vec s$ e ruotiamo il nostro sistema di riferimento: le nuove componenti sono $a$ e $b$.

![A sinistra il vettore s di componenti 3 e 4; a destra lo stesso vettore in un sistema di riferimento ruotato, con componenti a e b](invariante-2d.svg)

$$
a = \sqrt{1 + 4} = \sqrt5 \qquad b = \sqrt{16 + 4} = \sqrt{20} \qquad s = \sqrt{5 + 20} = 5
$$

Non importa come ruoto o sposto il mio sistema di riferimento, ma $\vec s$ avrà sempre lo stesso modulo $\longrightarrow$ <span style="color:#f59e0b">invariante</span>.

In 3D è uguale. E in relatività? Abbiamo 4 coordinate $(t, x, y, z)$ che definiscono un **evento**.

**Considero la luce.** Percorre uno spazio

$$
s^2 = x^2 + y^2 + z^2 = c^2\Delta t^2
$$

$$
(\Delta\sigma)^2 = c^2\Delta t^2 - s^2 = c^2\Delta t^2 - x^2 - y^2 - z^2
$$

Per un raggio di luce $(\Delta\sigma)^2 = 0$, ma per oggetti più lenti no. Vediamo cosa succede a $(\Delta\sigma)^2$ se cambio sistema di riferimento. Calcoliamo $(\Delta\sigma)^2$ tra $(0, 0, 0, 0)$ e $(t, x, y, z)$:

$$
(\Delta\sigma)^2 = (ct)^2 - x^2 - y^2 - z^2
$$

Cambio sistema di riferimento con Lorentz ($x' = \gamma(x - vt)$, $t' = \gamma(t - \beta\frac{x}{c})$): $(0, 0, 0, 0) \to (0, 0, 0, 0)$ e $(t, x, y, z) \to (t', x', y', z')$.

$$
\begin{aligned}
(\Delta\sigma')^2 &= (ct')^2 - (x')^2 - (y')^2 - (z')^2 \\
&= c^2\gamma^2\left(t - \beta\frac{x}{c}\right)^2 - \gamma^2\,(x - vt)^2 - y^2 - z^2 \\
&= \gamma^2\left[c^2t^2 + \beta^2x^2 - \cancel{2txv} - x^2 - v^2t^2 + \cancel{2xvt}\right] - y^2 - z^2 \\
&= \gamma^2\left[c^2t^2\left(1 - \beta^2\right) - x^2\left(1 - \beta^2\right)\right] - y^2 - z^2 \\
&= \frac{\cancel{1 - \beta^2}}{\cancel{1 - \beta^2}}\left[c^2t^2 - x^2\right] - y^2 - z^2 = (ct)^2 - s^2 = (\Delta\sigma)^2
\end{aligned}
$$

$$
(\Delta\sigma)^2 = (\Delta\sigma')^2 \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{invariante}}
$$

## Spaziotempo di Minkowski

Lo spazio quadridimensionale in cui l'intervallo invariante $\Delta\sigma$ tra due eventi è dato dall'equazione

$$
(\Delta\sigma)^2 = (c\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2
$$

è chiamato **spaziotempo di Minkowski**.

### Segno di $(\Delta\sigma)^2$

- $(\Delta\sigma)^2 = 0$. Abbiamo visto per la luce $(c\Delta t)^2 - s^2 = 0$. Considero solo le $x$: $(c\Delta t)^2 - x^2 = 0$ $\rightarrow$ $c\Delta t = \pm x$, **intervallo di tipo luce**. <span style="color:#f59e0b">Solo la luce può percorrerlo!</span>
- $(\Delta\sigma)^2 > 0$: $(c\Delta t)^2 - s^2 > 0$ $\rightarrow$ $(c\Delta t)^2 > s^2$. Ci ho messo più tempo della luce a percorrere $s$ $\rightarrow$ sono più lento. <span style="color:#f59e0b">Tutti quelli più lenti di $c$ possono percorrerlo.</span>
- $(\Delta\sigma)^2 < 0$: $(c\Delta t)^2 - s^2 < 0$ $\rightarrow$ $(c\Delta t)^2 < s^2$. Ci ho messo meno tempo della luce $\rightarrow$ sono più veloce: **impossibile**. <span style="color:#f59e0b">Nessuno può percorrere questa distanza.</span>

> [!note] Osservazione
> Se $(\Delta\sigma)^2 \ge 0$ l'intervallo può essere percorso, quindi i 2 eventi separati da $(\Delta\sigma)^2$ possono comunicare $\rightarrow$ **causalmente connessi**.
>
> Se $(\Delta\sigma)^2 < 0$ i due eventi non possono comunicare in nessun modo $\rightarrow$ **causalmente non connessi**.

## Diagrammi di Minkowski

Per poter disegnare, consideriamo per semplicità uno spostamento solo sull'asse delle $x$. A questo punto possiamo disegnare un piano cartesiano particolare, con $x$ in orizzontale e $ct$ in verticale. Ogni sistema di riferimento rappresenta un osservatore; vediamo come si relazionano tra loro due eventi.

![Tre eventi nel diagramma di Minkowski: A e B alla stessa altezza, B e C sulla stessa verticale](minkowski-eventi.svg)

Per esempio, se gli eventi $A$ e $B$ hanno la stessa $ct$ e gli eventi $B$ e $C$ la stessa $x$: $A$ e $B$ sono simultanei nel sistema di riferimento di $O$, mentre $B$ e $C$ avvengono nello stesso posto a tempi diversi.

### La luce nel diagramma

$$
\text{Luce:} \quad ct = \pm x \quad\longrightarrow\quad \text{retta}
$$

![Diagramma di Minkowski con il cono di luce: cono del futuro e del passato, regioni impossibili ai lati, un evento connesso e uno non connesso](cono-di-luce.svg)

<span style="color:#ef4444">Se parto dal presente non posso andare nelle regioni rosse.</span>

Un punto che si muove soddisfa $x = v \cdot t = \beta ct$:

$$
\longrightarrow\quad ct = \frac{x}{\beta} \qquad \beta \in [0, 1] \qquad \frac{1}{\beta} > 1 \quad \text{retta più pendente della bisettrice}
$$

### 2 sistemi di riferimento inerziali in un diagramma di Minkowski

Due sistemi che a $t = 0$ coincidono, e $S'$ ha velocità $\vec v$ rispetto a $S$.

![Assi ct e x del sistema S e assi ct′ e x′ del sistema S′, inclinati simmetricamente rispetto alla bisettrice della luce](minkowski-assi.svg)

$x' = 0$ è l'asse $ct'$ del diagramma verde:

$$
x' = \gamma\,(x - vt) \qquad x = vt = \beta ct \quad\rightarrow\quad ct = \frac{1}{\beta}\,x
$$

L'equazione dell'asse $ct'$ in $S$ è $ct = \dfrac{1}{\beta}\,x$.

$ct' = 0$ è l'asse $x'$: analogamente $ct = \beta x$.

### Gli effetti relativistici nel diagramma

**Dilatazione dei tempi**

![Proiezione dell'evento P sull'asse ct e sull'asse ct′](minkowski-dilatazione.svg)

$\Delta t_2$ è il tempo proprio; dal grafico vediamo $\Delta t_2 < \Delta t_1$, con $\Delta t_1 = \gamma\,\Delta t_2$.

**Contrazione delle distanze**

![Proiezione dell'evento P sull'asse x e sull'asse x′](minkowski-contrazione.svg)

$\Delta x_1$ è lo spazio proprio; dal grafico $\Delta x_2 < \Delta x_1$, con $\Delta x_2 = \dfrac{1}{\gamma}\,\Delta x_1$.

**Simultaneità**

![Due eventi P e Q alla stessa altezza in S, proiettati sull'asse ct′](minkowski-simultaneita.svg)

$t_P = t_Q$ $\rightarrow$ i 2 eventi sono simultanei per $O$; $t'_P \neq t'_Q$ $\rightarrow$ per $O'$ i 2 eventi non sono simultanei.

## Equivalenza massa-energia

Abbiamo visto nel capitolo delle [[Elettromagnetismo e Maxwell#Quantità di moto|onde elettromagnetiche]] che un'onda elettromagnetica è in grado di trasportare energia e quantità di moto. In particolare abbiamo visto che la quantità di moto che porta con sé è:

$$
p = \frac{\mathcal E}{c} \qquad \mathcal E := \text{energia}
$$

**Considero un sistema di riferimento a riposo con un corpo di massa $m$** ($v'_i = 0$). Due laser, uno sopra e uno sotto, colpiscono il corpo con un lampo ciascuno:

![Un corpo di massa m fermo, colpito da due lampi laser opposti](massa-energia-riposo.svg)

$$
\text{energia di un lampo: } \frac{\mathcal E'}{2} \qquad \text{quantità di moto: } \frac{\mathcal E'}{2c}
$$

$$
\mathcal E'_{tot} = \frac{\mathcal E'}{2} + \frac{\mathcal E'}{2} = \mathcal E' \qquad p'_{tot} = p_1 - p_2 = 0 \quad\rightarrow\quad v'_2 = 0 \ \text{fermo}
$$

**Considero un sistema di riferimento esterno in cui $S'$ si muove con velocità $\vec v$.** Emetto i lampi quando il corpo passa: visti da qui arrivano obliqui.

![Il corpo in moto con velocità v: i lampi arrivano obliqui; a destra il triangolo tra quantità di moto e velocità](massa-energia-moto.svg)

$$
p_1 = \frac{\mathcal E}{2c} \qquad p_x = \ ? \qquad p_y = \ ?
$$

$$
\vec p_{y_1} + \vec p_{y_2} = 0 \ \text{(sono opposti!)} \qquad \vec p_{x_1} + \vec p_{x_2} = 2\,\vec p_x
$$

Per similitudine tra il triangolo delle quantità di moto e quello delle velocità:

$$
p_1 : p_x = c : v \qquad p_x = p_1\,\frac{v}{c} = \frac{\mathcal E v}{2c^2} \qquad 2p_x = \frac{\mathcal E v}{c^2}
$$

**Come cambia $p$?**

$$
p_i = m v \qquad p_f = m v + \frac{\mathcal E v}{c^2}
$$

Se $S$ e $S'$ devono osservare la stessa fisica, se $m$ non accelera in $S'$ non lo può fare in $S$.

$$
\longrightarrow\quad \Delta p = m\,\Delta v \quad \text{non può funzionare perché } \Delta v \Rightarrow \text{accelerazione}
$$

$$
\longrightarrow\quad \Delta p = \Delta m\, v \quad\Longrightarrow\quad p_f = p_i + \Delta p = (m + \Delta m)\, v = m v + \frac{\mathcal E v}{c^2}
$$

$$
\longrightarrow\quad \Delta m = \frac{\mathcal E}{c^2} \quad\longrightarrow\quad \textcolor{#f59e0b}{\mathcal E = \Delta m\, c^2}
$$

Un corpo che assorbe o cede energia cambia massa.

$$
\mathcal E_0 = m_0\, c^2 \quad \text{energia a riposo}
$$

## Dinamica relativistica

Considero un corpo in moto $\rightarrow$ $\mathcal E = \mathcal E_0 + K$, con $\mathcal E_0 = m_0 c^2$ e $K :=$ energia cinetica relativistica.

$$
\longrightarrow\quad \textcolor{#f59e0b}{\text{energia relativistica:} \quad \mathcal E = \gamma\, m_0\, c^2}
$$

- Se il corpo è fermo: $v = 0$ $\rightarrow$ $\gamma = 1$ $\rightarrow$ $\mathcal E = m_0 c^2$.
- Se $v \to c$: $\mathcal E = \displaystyle\lim_{v \to c} \gamma\, m_0 c^2 = \lim_{v \to c} \frac{1}{\sqrt{1 - v^2/c^2}}\, m_0 c^2 = \infty$.

Se riprendo $\mathcal E = \mathcal E_0 + K = \gamma\, m_0 c^2$:

$$
\longrightarrow\quad K = (\gamma - 1)\, m_0\, c^2
$$

**Energia totale relativistica**

$$
\mathcal E^2 = m_0^2\, c^4 + p^2\, c^2
$$

Per la luce $m_0 = 0$ e ottengo $\rightarrow$ $\mathcal E = pc$ $\rightarrow$ $p = \dfrac{\mathcal E}{c}$, come abbiamo visto prima.

> [!info] Collegamenti
> L'energia e la quantità di moto dei fotoni tornano nella [[Crisi della fisica classica]].
