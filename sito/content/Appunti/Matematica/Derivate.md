---
title: Derivate
description: Retta tangente e velocità istantanea, definizione di derivata, derivate delle funzioni elementari, algebra delle derivate, funzioni composte e inverse, punti di non derivabilità, retta tangente e normale.
tags:
  - matematica
  - analisi
  - 5SCI
---
> [!info] Collegamenti
> La derivata è uno strumento che ritrovi ovunque in fisica: velocità e accelerazione del [[Onde suono e luce#Moto armonico|moto armonico]] (provale nella simulazione [[Moto armonico e onde meccaniche]]) e la legge di Faraday-Neumann in [[Elettromagnetismo e Maxwell]]. Serve anche per risolvere le [[Equazioni differenziali del primo ordine]].

## Derivate e retta tangente

All'inizio dello studio dell'analisi matematica abbiamo visto come uno dei problemi che fino ad ora non potevano essere risolti era legato allo studio della retta tangente in un punto a una funzione.

![Grafico di y = sin(x) con la retta y = mx + q tangente in un punto](derivate-tangente-seno.svg)

Il metodo che si utilizzava in geometria analitica per vedere se una retta è tangente in questa occasione non può più funzionare, perché otteniamo un sistema di questo tipo:

$$
\begin{cases} y = \sin x \\ y = mx + q \end{cases} \qquad \text{come lo risolvo?}
$$

Soprattutto quando trattavamo polinomi di solito avevamo un'equazione di secondo grado e imponevamo di avere una sola soluzione, e questo ci garantiva che la retta sarebbe stata tangente. In questo caso non abbiamo modo di capire se la retta è tangente o secante, quindi dobbiamo trovare un'altra via.

Supponiamo di voler trovare la retta tangente al grafico del seno nel punto $P$. Noi sappiamo scrivere l'equazione del fascio di rette proprio del punto:

$$
y - y_0 = m \cdot (x - x_0) \quad\longrightarrow\quad m \text{ può prendere qualunque valore}
$$

![La retta per i punti P e Q della curva, la retta tangente in P e i cateti h e f(x0 + h) − f(x0)](derivate-secante.svg)

Il coefficiente angolare di una retta è $m = \dfrac{\Delta y}{\Delta x}$, quindi per la retta che passa per $P$ e $Q$:

$$
m_{PQ} = \frac{f(x_0 + h) - f(x_0)}{h}
$$

Che cosa succede in questo caso se io prendo il limite per $h$ che tende a zero? Graficamente vediamo che se $h$ tende a zero allora il punto $P$ e il punto $Q$ tendono a sovrapporsi, e proprio nel momento in cui si sovrappongono la retta generica diventa la retta tangente.

$$
m_{tg} = \lim_{h \to 0} m_{PQ} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$

### Velocità istantanea come retta tangente

Ci ricordiamo dallo studio della fisica che, nel momento in cui vogliamo calcolare la velocità di un oggetto, possiamo fare il calcolo dello spazio percorso fratto il tempo impiegato. Questo calcolo però ci restituisce la velocità media dell'oggetto e non quella istantanea. Se applichiamo il concetto appena visto per trovare la retta tangente, vediamo che calcoliamo esattamente la velocità istantanea.

$$
v_{\text{media}} = \frac{\Delta s}{\Delta t} = \frac{s(t_0 + \Delta t) - s(t_0)}{\Delta t}
$$

$$
v_{\text{istantanea}}(t) = \lim_{h \to 0} \frac{s(t + h) - s(t)}{h}
$$

Formalmente il calcolo è molto simile, però in quello della velocità istantanea noi stiamo calcolando lo spazio percorso in una frazione di tempo piccolissima, che si può quindi approssimare a un istante solo, e perciò in questa maniera calcoliamo la velocità istantanea proprio grazie all'operazione di limite. In particolare, quindi, adesso scopriamo che la velocità di un oggetto risulta essere rappresentata dal coefficiente angolare della retta tangente alla funzione che descrive lo spostamento.

## Definizione di derivata

> [!tip] Definizione
> Una funzione $f(x)$ definita $\forall x \in I_\delta(x_0)$ è **derivabile in $x_0$** se
> $$
> \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} \quad \text{esiste ed è finito}
> $$
> Questo limite è la **derivata prima di $f$ in $x_0$**, e si indica con $f'(x_0)$.

$$
\frac{df}{dx}(x_0) = f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$

$f'(x_0)$ è la <span style="color:#ef4444">pendenza della retta tangente a $f$ in $x_0$</span>.

### Derivabilità di una funzione

La derivata di una funzione è essa stessa una funzione definita in un intervallo. Per questo motivo, quando si studia la derivata, è necessario capire se anch'essa è continua e se ha dei punti singolari. Il metodo è sempre lo stesso: la derivata in un punto esiste se la derivata destra e la derivata sinistra di quel punto sono finite e uguali.

$$
\left.
\begin{aligned}
f'_+(x_0) &= \lim_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h} \\[6pt]
f'_-(x_0) &= \lim_{h \to 0^-} \frac{f(x_0 + h) - f(x_0)}{h}
\end{aligned}
\right\}
\qquad f'_+(x_0) = f'_-(x_0) \;\longrightarrow\; f'(x_0) \text{ esiste}
$$

### Proprietà delle funzioni derivabili

> [!tip]
> Se una $f$ è derivabile in $x_0$ allora è anche continua in $x_0$.

### Interpretazione della derivata

Come abbiamo visto, la derivata di una funzione in un punto rappresenta il coefficiente angolare della retta tangente alla funzione proprio in quel punto. Questa osservazione ci permette di intendere la derivata come un oggetto che determina **quanto rapidamente una quantità cresce**.

Consideriamo l'esempio di prima con la velocità: questa può essere rappresentata come la derivata della funzione che determina lo spazio percorso. In questo caso, più lo spazio percorso varia rapidamente più la velocità sarà alta: significa che un valore della derivata molto alto è strettamente collegato a un incremento molto rapido della funzione non derivata. Lo stesso succede quando la derivata assume un valore negativo molto grande in valore assoluto: questo vuol dire una variazione molto rapida della quantità non derivata, chiaramente in questo caso si intende una diminuzione.

Geometricamente questo è legato al fatto che il coefficiente angolare di una retta ne determina la pendenza, e tanto più il coefficiente angolare è un numero grande tanto più la retta ha una pendenza elevata.

In fisica, ogni volta che si vuole considerare la rapidità con cui varia una grandezza, si utilizzano le derivate. Basti pensare appunto alla velocità, che rappresenta la rapidità con cui lo spazio cambia, oppure all'accelerazione, che rappresenta la rapidità con cui la velocità cambia. Allo stesso modo ci sono tantissime altre grandezze fisiche che sono interpretate come rapidità di variazione di un'altra grandezza.

## Derivate di funzioni elementari

Fortunatamente, quando bisogna calcolare una derivata, non è necessario calcolare il limite del rapporto incrementale ogni volta: ci sono delle regole, che vanno dimostrate, che ci permettono di calcolare più rapidamente le derivate.

### Costante

$f(x) = c \quad \forall x \in \mathbb{R}$

$$
f'(x) = \lim_{h \to 0} \frac{c - c}{h} = \lim_{h \to 0} \frac{0}{h} = 0
$$

### Monomio di 1° grado

$f(x) = x \quad \forall x \in \mathbb{R}$

$$
f'(x) = \lim_{h \to 0} \frac{(x + h) - x}{h} = \lim_{h \to 0} \frac{x + h - x}{h} = \lim_{h \to 0} \frac{h}{h} = 1 \quad\longrightarrow\quad \text{costante}
$$

### Potenza

$f(x) = x^n \quad \forall x \in \mathbb{R}$

Ricordo che:

$$
(a + b)^2 = a^2 + 2ab + b^2 = \binom{2}{0} a^2 + \binom{2}{1} ab + \binom{2}{2} b^2
$$

$\dbinom{n}{k}$ rappresenta tutte le [[Calcolo combinatorio, probabilità e distribuzioni#Combinazioni semplici|combinazioni]] non ordinate in cui da $n$ elementi ne prendo $k$.

In $(a + b)^2$ ho 2 fattori disponibili, $(a + b) \cdot (a + b)$, e mi chiedo in quanti modi posso combinarli se voglio:

$$
\begin{aligned}
k = 2 &\longrightarrow 2 \text{ volte } b \quad (\text{quindi zero volte } a) \\
k = 1 &\longrightarrow 1 \text{ volta } b \quad (\text{quindi 1 volta } a) \\
k = 0 &\longrightarrow 0 \text{ volte } b \quad (\text{quindi 2 volte } a)
\end{aligned}
$$

$$
\underbrace{\binom{2}{0} a^2}_{\substack{2 \text{ volte } a \\ 0 \text{ volte } b}} + \underbrace{\binom{2}{1} ab}_{\substack{1 \text{ volta } a \\ 1 \text{ volta } b}} + \underbrace{\binom{2}{2} b^2}_{2 \text{ volte } b}
$$

$$
(a + b)^3 = \binom{3}{0} a^3 + \binom{3}{1} a^2 b + \binom{3}{2} a b^2 + \binom{3}{3} b^3 = a^3 + 3a^2 b + 3ab^2 + b^3
$$

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$

Allora:

$$
\lim_{h \to 0} \frac{(x + h)^n - x^n}{h} = \lim_{h \to 0} \frac{\left( \sum_{k=0}^{n} \binom{n}{k} x^{n-k} h^k \right) - x^n}{h} = \lim_{h \to 0} \frac{\sum_{k=1}^{n} \binom{n}{k} x^{n-k} h^k}{h}
$$

$$
= \lim_{h \to 0} \left[ n x^{n-1} \frac{\textcolor{#22c55e}{\cancel{h}}}{\textcolor{#22c55e}{\cancel{h}}} + \underbrace{\binom{n}{2} \frac{x^{n-2} h^2}{h} + \dots}_{\textcolor{#ef4444}{\text{tutti nulli}}} \right] = n \cdot x^{n-1} = f'(x)
$$

$$
\Longrightarrow \quad \text{se } f(x) = x^n \quad\longrightarrow\quad f'(x) = n \cdot x^{n-1}
$$

> [!note]
> La dimostrazione con il binomio vale per $n$ naturale, ma la regola resta vera per qualunque esponente reale $n \neq 0$ (con $x > 0$).

### Esponenziale

$f(x) = a^x \quad a \neq 1,\ a > 0,\ \forall x \in \mathbb{R}$

$$
\lim_{h \to 0} \frac{a^{x+h} - a^x}{h} = \lim_{h \to 0} \frac{a^x \cdot (a^h - 1)}{h} = a^x \cdot \underbrace{\lim_{h \to 0} \frac{a^h - 1}{h}}_{\textcolor{#ef4444}{\text{limite notevole}}} = a^x \cdot \ln a
$$

$$
f'(x) = a^x \ln a
$$

$$
\text{se } a = e \quad\longrightarrow\quad f(x) = e^x \qquad f'(x) = e^x
$$

### Logaritmo

$f(x) = \log_a x \quad a > 0,\ a \neq 1,\ \forall x > 0$

$$
f'(x) = \lim_{h \to 0} \frac{\log_a(x + h) - \log_a(x)}{h} = \lim_{h \to 0} \frac{\log_a\left(1 + \frac{h}{x}\right) + \textcolor{#ef4444}{\cancel{\log_a x}} - \textcolor{#ef4444}{\cancel{\log_a x}}}{h}
$$

Con la sostituzione $t = \dfrac{h}{x}$:

$$
= \lim_{h \to 0} \frac{\log_a\left(1 + \frac{h}{x}\right)}{h} = \lim_{t \to 0} \frac{\log_a(1 + t)}{t\,x} = \frac{1}{x \ln a}
$$

$$
\text{se } a = e \quad\longrightarrow\quad f(x) = \ln(x) \qquad f'(x) = \frac{1}{x}
$$

### Seno e coseno

$\forall x \in \mathbb{R}$. Usiamo le [[Goniometria#Formule di addizione e sottrazione|formule di addizione]]:

$$
f'(x) = \lim_{h \to 0} \frac{\sin(x + h) - \sin(x)}{h} = \lim_{h \to 0} \frac{(\sin x \cos h + \cos x \sin h) - \sin x}{h}
$$

$$
= \lim_{h \to 0} \cos x \cdot \underbrace{\frac{\sin h}{h}}_{\textcolor{#ef4444}{= 1}} + \lim_{h \to 0} \frac{\sin x \cos h - \sin x}{h} = \cos x + \lim_{h \to 0} \frac{\sin x}{h} \cdot (\cos h - 1)
$$

Per $h \to 0$ si ha $\cos h \approx 1 - \dfrac{h^2}{2}$:

$$
= \cos x + \lim_{h \to 0} \frac{\sin x}{h} \left( \textcolor{#ef4444}{\cancel{1}} - \frac{h^2}{2} - \textcolor{#ef4444}{\cancel{1}} \right) = \cos x - \underbrace{\lim_{h \to 0} \sin x \cdot \frac{h}{2}}_{\textcolor{#ef4444}{= 0}} = \cos x
$$

$$
f(x) = \sin x \quad\longrightarrow\quad f'(x) = \cos x
$$

$$
f(x) = \cos x \quad\longrightarrow\quad f'(x) = -\sin x
$$

## Algebra delle derivate

### Linearità

$$
\frac{d}{dx} \left[ f(x) + g(x) \right] = \frac{d}{dx} f(x) + \frac{d}{dx} g(x) = f'(x) + g'(x)
$$

$$
\frac{d}{dx} \left[ a f(x) \right] = a \frac{d}{dx} f(x) = a f'(x)
$$

### Prodotto di funzioni

$$
\frac{d}{dx} \left[ f(x)\, g(x) \right] = \lim_{h \to 0} \frac{f(x + h)\, g(x + h) - f(x)\, g(x)}{h}
$$

Aggiungo e tolgo <span style="color:#22c55e">lo stesso termine</span>:

$$
= \lim_{h \to 0} \frac{f(x + h)\, g(x + h) \textcolor{#22c55e}{- f(x)\, g(x + h)} - f(x)\, g(x) \textcolor{#22c55e}{+ g(x + h)\, f(x)}}{h}
$$

$$
= \lim_{h \to 0} \left[ \frac{f(x + h) - f(x)}{h} \cdot g(x + h) + \frac{g(x + h) - g(x)}{h} \cdot f(x) \right]
$$

$$
= \underbrace{\lim_{h \to 0} \frac{f(x + h) - f(x)}{h}}_{\textcolor{#ef4444}{f'(x)}} \cdot \underbrace{\lim_{h \to 0} g(x + h)}_{\textcolor{#22c55e}{g(x)}} + \underbrace{\lim_{h \to 0} \frac{g(x + h) - g(x)}{h}}_{\textcolor{#ef4444}{g'(x)}} \cdot f(x)
$$

$$
= f'(x)\, g(x) + g'(x)\, f(x)
$$

### Quoziente

$$
\frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \; ?
$$

Considero

$$
f(x) = \frac{f(x)}{g(x)} \cdot g(x) \qquad g(x) \neq 0 \quad \forall x \in D_g
$$

$$
\frac{d}{dx} \left[ f(x) \right] = \frac{d}{dx} \left[ \frac{f}{g} \cdot g \right] = \frac{d}{dx} \left[ \frac{f}{g} \right] g + \frac{f}{g} \cdot \frac{d}{dx} g
$$

$$
f' = \left[ \frac{f}{g} \right]' g + \frac{f}{g} \cdot g' \quad\longrightarrow\quad \left[ \frac{f}{g} \right]' = \frac{f'\, g - f\, g'}{g^2}
$$

### Reciproco

$$
\frac{d}{dx} \left[ \frac{1}{f(x)} \right] = \frac{0 \cdot f(x) - f'(x)}{f^2(x)} = -\frac{f'(x)}{f^2(x)}
$$

### Funzione composta

Consideriamo $g(x) = e^x$ e $f(x) = 2x + 1$:

$$
g(f(x)) = e^{2x + 1}
$$

Come calcolo $\dfrac{d}{dx}\, g(f(x))$?

$$
\frac{d}{dx}\, g(f(x)) = g'(f(x)) \cdot f'(x)
$$

$$
\longrightarrow\quad \frac{d}{dx}\, e^{2x + 1} = \underbrace{e^{2x + 1}}_{\textcolor{#ef4444}{g'}} \cdot \underbrace{(2)}_{\textcolor{#ef4444}{f'}}
$$

$$
\frac{d}{dx} \left( x^2 + 3x \right)^4 = 4 \cdot \left( x^2 + 3x \right)^3 \cdot (2x + 3)
$$

### Funzione inversa

$$
y = f(x) \quad\longrightarrow\quad g(y) = x
$$

Sostituisco $y$ in $g(y)$:

$$
g(f(x)) = x
$$

$$
\frac{d}{dx} \left[ g(f(x)) \right] = \frac{d}{dx}\, x
$$

$$
g'(y) \cdot f'(x) = 1 \quad\longrightarrow\quad g'(y) = \frac{1}{f'(x)}
$$

### Funzioni goniometriche inverse

**Arcoseno.** Consideriamo $\arcsin(x) = y$, cioè $\sin(y) = x$.

$$
\frac{d}{dx} \left[ \arcsin(x) \right] = \frac{1}{\frac{d}{dy} \sin(y)} = \frac{1}{\cos y}
$$

$$
\frac{d}{dx} \arcsin(x) = \frac{1}{\textcolor{#ef4444}{+}\sqrt{1 - \sin^2 y}} = \frac{1}{\sqrt{1 - x^2}}
$$

<span style="color:#ef4444">L'arcoseno ha valori in $\left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$, dove il coseno non è negativo: quindi scelgo sempre il $+$.</span>

**Arcocoseno.** Considero $\arccos(x) = y$, cioè $\cos(y) = x$.

$$
\frac{d}{dx} \left[ \arccos(x) \right] = \frac{1}{\frac{d}{dy} \cos(y)} = -\frac{1}{\sin(y)} = -\frac{1}{+\sqrt{1 - x^2}}
$$

Anche qui scelgo il $+$: l'arcocoseno ha valori in $[0, \pi]$, dove il seno non è negativo.

**Arcotangente.** Considero $\arctan(x) = y$, cioè $\tan(y) = x$.

$$
\frac{d}{dy} \tan(y) = \frac{d}{dy} \left[ \frac{\sin y}{\cos y} \right] = \frac{\cos^2 y + \sin^2 y}{\cos^2 y} = \frac{1}{\cos^2 y}
$$

$$
\frac{d}{dx} \left[ \arctan(x) \right] = \frac{1}{\frac{d}{dy} \tan(y)} = \cos^2 y
$$

Come scrivo $\cos^2 y$ in termini di $\tan(y) = x$?

$$
\tan^2 + 1 = \frac{\sin^2}{\cos^2} + 1 = \frac{\sin^2 + \cos^2}{\cos^2} = \frac{1}{\cos^2} \quad\longrightarrow\quad \cos^2 = \frac{1}{1 + \tan^2}
$$

$$
\frac{d}{dx} \left[ \arctan(x) \right] = \frac{1}{1 + x^2}
$$

**Arcocotangente.** Considero $\text{arccot}(x) = y$, cioè $\cot(y) = x$.

$$
\frac{d}{dx} \left[ \text{arccot}(x) \right] = \frac{1}{\frac{d}{dy} \cot(y)} = -\frac{1}{1 + x^2}
$$

## Derivabilità

Una funzione si dice derivabile in un intervallo se la derivata esiste in ogni punto di quell'intervallo. Dobbiamo quindi capire come studiare la derivata: abbiamo già visto in precedenza che la derivata è essa stessa una funzione classica, perciò i meccanismi con cui studiamo la sua continuità sono gli stessi che utilizzavamo con le funzioni la prima volta che le abbiamo viste.

> [!tip] Criterio pratico
> **Prima** controllo che $f(x)$ sia continua in $x_0$: se non lo è, $f$ non è derivabile in $x_0$ e mi fermo qui.
>
> **Poi** guardo se $f'$ è continua in $x_0$: se
> $$
> \lim_{x \to x_0^-} f'(x) = \lim_{x \to x_0^+} f'(x) = l \qquad l \in \mathbb{R} \ \text{(finito)}
> $$
> allora $f$ è derivabile in $x_0$ e $f'(x_0) = l$.

Come si studia la derivabilità di una funzione:

1. controllo che la funzione sia continua (di norma lo abbiamo già fatto studiando la funzione);
2. una volta calcolata la derivata della funzione originale, studio il suo dominio;
3. una volta riconosciuto il suo dominio, studio i limiti destro e sinistro della derivata nei punti estremi del dominio o, eventualmente, se la funzione è definita a tratti, studio i limiti destro e sinistro nel punto in cui le due funzioni si incollano;
4. i valori che ottengo come risultato dei limiti mi dicono se la funzione derivata è continua o meno e di conseguenza se la funzione è derivabile.

> [!warning] Attenzione
> Il fatto che una funzione sia continua non garantisce il fatto che sia derivabile. Viceversa, però, se una funzione è derivabile allora è garantita la sua continuità.

## Punti di non derivabilità

### Punto angoloso

Se il limite destro e sinistro della derivata in un punto hanno valori diversi, allora significa che la derivata non è continua e in quel punto la funzione originale presenta un punto angoloso.

![Grafico della derivata: vale 2 a sinistra di x = 2 e 1 a destra](derivate-angoloso-derivata.svg)

$$
\lim_{x \to 2^-} f'(x) = 2 \qquad \lim_{x \to 2^+} f'(x) = 1 \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{discontinuità di tipo salto in } x = 2}
$$

![Grafico della funzione: due rette che si incontrano in (2, 3/2) con pendenze diverse](derivate-angoloso-funzione.svg)

$$
\lim_{x \to 2^-} f(x) = \frac{3}{2} \qquad \lim_{x \to 2^+} f(x) = \frac{3}{2} \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{continua con punto angoloso in } x = 2}
$$

### Cuspide

Se il limite destro e il limite sinistro della derivata in un punto sono alternati, uno che tende a più infinito e l'altro a meno infinito o viceversa, otteniamo una cuspide. Geometricamente, quando la derivata ha un limite infinito significa che la pendenza della funzione originale cresce all'infinito e diventa verticale. Questo significa che nella cuspide la funzione arriverà a creare una punta, perché sia da destra che da sinistra in quel punto la sua crescita sarà talmente alta da renderla verticale. Ricordiamo che, dal momento che la derivata rappresenta il coefficiente angolare della retta tangente, il lato che tende a più infinito rappresenterà una funzione che cresce verticalmente, mentre il lato che tende a meno infinito rappresenterà una funzione che decresce verticalmente.

![Grafico della derivata: tende a più infinito per x che tende a 0 da sinistra e a meno infinito da destra](derivate-cuspide-derivata.svg)

$$
\lim_{x \to 0^-} f'(x) = +\infty \qquad \lim_{x \to 0^+} f'(x) = -\infty \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{discontinuità di tipo asintoto verticale in } x = 0}
$$

![Grafico della funzione: una punta verso l'alto in (0, 2) con tangente verticale](derivate-cuspide-funzione.svg)

$$
\lim_{x \to 0^-} f(x) = 2 \qquad \lim_{x \to 0^+} f(x) = 2 \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{funzione continua con cuspide in } x = 0}
$$

### Flesso a tangente verticale

In questo caso, se la derivata a destra e a sinistra di un punto assume per entrambi il valore di più infinito o di meno infinito, quello che otteniamo è un flesso a tangente verticale. Significa che la funzione ha un punto in cui cresce verticalmente, seguendo i ragionamenti geometrici che abbiamo visto per la cuspide.

![Grafico della derivata: tende a più infinito da entrambi i lati di x = 0](derivate-flesso-derivata.svg)

$$
\lim_{x \to 0^-} f'(x) = +\infty \qquad \lim_{x \to 0^+} f'(x) = +\infty \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{discontinuità di tipo asintoto verticale in } x = 0}
$$

![Grafico della funzione: sempre crescente, in (0, 2) ha tangente verticale](derivate-flesso-funzione.svg)

$$
\lim_{x \to 0^-} f(x) = 2 \qquad \lim_{x \to 0^+} f(x) = 2 \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{funzione continua con flesso a tangente verticale in } x = 0}
$$

## Retta tangente e normale

Come abbiamo già detto, la derivata ci permette di trovare la retta tangente a una curva in un dato punto. Vediamo adesso nel dettaglio come descrivere questa retta.

Se $f$ è definita e continua in $x_0$ e lo è anche $f'$:

$$
y - f(x_0) = f'(x_0)\,(x - x_0) \quad \text{è la retta tangente}
$$

mentre, se $f'(x_0) \neq 0$,

$$
y - f(x_0) = -\frac{1}{f'(x_0)}\,(x - x_0) \quad \text{è la retta normale}
$$

> [!tip] Curve tangenti
> Due curve $f$ e $g$ sono tangenti in $x_0$ se:
> $$
> f(x_0) = g(x_0) \quad \text{e} \quad f'(x_0) = g'(x_0)
> $$
> perché le rette tangenti a $f$ e $g$ in $x_0$ sono **identiche**.
