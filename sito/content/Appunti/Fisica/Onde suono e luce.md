---
title: Onde suono e luce
description: Moto armonico, moto ondulatorio, interferenza e il suono (velocità, eco, caratteristiche, note musicali, decibel e scala logaritmica, battimenti, effetto Doppler).
tags:
  - fisica
  - onde
  - 4SCI
---
Nello studio della [[Goniometria|goniometria]] abbiamo visto come le funzioni seno e coseno ci permettono di rappresentare dei fenomeni periodici. Il fenomeno periodico per eccellenza è quello delle onde che viene descritto in fisica dal moto armonico.

## Moto armonico

![Vettore r sulla circonferenza e sua proiezione r cos phi sull'asse x](onde-proiezione.svg)

$$
x = r\cos\varphi \quad\longrightarrow\quad \text{è la legge oraria del moto armonico}
$$

Se $\varphi$ dipende dal tempo?

$$
\varphi = \omega t + \varphi_0 \quad\longrightarrow\quad x = r\cos(\omega t + \varphi_0)
$$

Qui vediamo che la legge oraria del moto armonico è semplicemente un coseno che può avere ampiezza dipendente da $r$, periodo dipendente da $\omega$ ed eventualmente può avere una traslazione.

> [!info] Collegamenti
> Guarda il punto che ruota e la sua proiezione diventare il grafico di $x(t)$ nella simulazione [[Moto armonico e onde meccaniche]].

### Terminologia

| Simbolo     | Significato                     | Unità di misura |
| ----------- | ------------------------------- | --------------- |
| $r$         | Ampiezza oscillazione           | $[\text{m}]$    |
| $\omega$    | Pulsazione / frequenza angolare | $[\text{rad/s}]$ |
| $\varphi_0$ | Fase iniziale o traslazione     | $[\text{rad}]$  |

Già visto chiaramente seno e coseno, non sono due funzioni indipendenti, ma una è generata dalla traslazione dell'altra. Questo significa che tutta la trattazione può essere rifatta in maniera identica con il seno.

$$
x = r\cos(\omega t + \varphi_0) = r\sin\left(\omega t + \varphi_0 + \frac{\pi}{2}\right) = r\sin(\omega t + \varphi_0')
$$

> [!info] Collegamenti
> Lo sfasamento di $\frac{\pi}{2}$ tra seno e coseno è quello visto in [[Goniometria#Modifico φ → sfasamento dell'onda|goniometria]].

### Periodo

Se ho $x = r\cos(\omega t + \varphi_0)$ il tempo che impiego a percorrere un'oscillazione completa è

$$
T = \frac{2\pi}{\omega} \quad\longrightarrow\quad \text{frequenza} \;\Rightarrow\; f = \frac{1}{T}
$$

### Velocità

In questo caso vogliamo studiare come varia la velocità della proiezione del punto sull'asse delle x. In pratica vogliamo vedere come varia la lunghezza del segmento $\textbf{\textcolor{RoyalBlue}{BLU}}$

![Velocità tangenziale e sua componente lungo l'asse x](onde-velocita.svg)
> [!info] 
>  Ricordiamo la formula della velocità tangenziale vista nello studio del moto circolare: 
>  
> $$
> \longrightarrow\quad v = \omega r
> $$


Sfruttando le proprietà della [[trigonometria ]] si ottiene la velocità sull'asse $x$:

$$
v = -\omega r\sin\varphi = -\omega r\sin(\omega t + \varphi_0)
$$

$x$ è descritto da cos e $v$ da sin $\;\longrightarrow\;$ sono sfasati di $\frac{\pi}{2}$!

### Accelerazione

![Accelerazione centripeta e sua componente lungo l'asse x](onde-accelerazione.svg)
>[!info]
>Ricordiamo la formula dell' [[accelerazione centripeta]] :
>$$
>\longrightarrow\quad a_c = \omega^2 r
>$$


Sfruttando le proprietà della [[trigonometria ]] si ottiene l'accelerazione sull'asse $x$:

$$
a = -\omega^2 r\cos\varphi = -\omega^2 r\cos(\omega t + \varphi_0)
$$

$$
a(t) = -\omega^2 x(t) \quad\longrightarrow\quad \omega = \sqrt{-\frac{a(t)}{x(t)}}
$$

### Energia di un moto armonico

**Cinetica**

$$
E_k = \frac{1}{2} m v^2 = \frac{1}{2} m\omega^2 A^2 \sin^2(\omega t + \varphi_0)
$$

**Potenziale**

In questo caso, ricordiamo che un sistema formato da una molla e da un oggetto ad essa collegato si muovono di moto armonico, quindi utilizziamo l'energia potenziale elastica.

$$
U = \frac{1}{2} m\omega^2 x^2 = \frac{1}{2} m\omega^2 A^2 \cos^2(\omega t + \varphi_0)
$$

**Totale**

$$
E = E_k + U = \frac{1}{2} m\omega^2 A^2
$$

Come vediamo l'energia totale di un corpo che si muove di moto armonico è direttamente proporzionale all'ampiezza di oscillazione dell'onda stessa al quadrato. Quindi, quanto più grande l'ampiezza dell'onda tanto più porta energia.

## Moto ondulatorio

> [!example] Simulazioni
> Le onde trasversali e longitudinali si vedono propagare nella seconda parte di [[Moto armonico e onde meccaniche]]; per un'onda che dipende insieme da spazio e tempo c'è [[Onda progressiva in 3D]].

Un'onda è una perturbazione che si propaga trasportando energia e quantità di moto, ma non materia.

| Onde trasversali                                   | Onde longitudinali                                     |
| -------------------------------------------------- | ------------------------------------------------------ |
| oscillazione avviene $\perp$ al verso di propagazione | oscillazione $\parallel$ al verso di propagazione  |

### Fronte d'onda

È un luogo di punti in cui la grandezza variabile descritta dall'onda rimane costante nel tempo.

### Onde armoniche

Fenomeno periodico + semplice che ha la forma di una delle funzioni viste in [[goniometria]].

![Onda armonica y = A cos(omega t + phi0) tra -A e A](onde-onda-armonica-cos.svg)

Vediamo subito che un onda armonica è caratterizzata da delle grandezze fondamentali: l'ampiezza A, ovvero la distanza tra il punto più alto dell'onda e lo zero e la lunghezza d'onda $\lambda$ che ci dice qual è la distanza che intercorre tra due picchi o due valli dell'onda

### Velocità di propagazione

Un'onda si propaga nello spazio ad una determinata velocità che è strettamente legata alle caratteristiche dell'onda, viste poco sopra in [[#Moto ondulatorio]]. In particolare, dal momento che la velocità è definita come spazio fratto tempo possiamo sfruttare due caratteristiche di un moto armonico legate allo spazio e al tempo: 
$$
\text{lunghezza d'onda}\rightarrow\lambda \: [m] \: \qquad \text{frequenza} \rightarrow T \: [s]
$$
La velocità con cui si propaga un'onda, quindi si può andare a definire in questa maniera:
$$
v = \frac{\lambda}{T}
$$

In maniera pratica rappresenta il fatto che l'onda percorre uno spazio pari alla sua lunghezza d'onda nel tempo in cui completa l'oscillazione.

<span style="color:#ef4444"> La velocità di propagazione però dipende dal materiale in cui l'onda si propaga</span>

Se fino ad ora abbiamo visto che la velocità è determinata dalle caratteristiche dell'onda, è vero anche che questa velocità si può ricavare direttamente dalle proprietà del materiale in cui questa si propaga. Siccome un'onda interagisce col materiale che attraversa è ragionevole pensare che le proprietà di questo materiale determinino, quanto veloce l'onda stessa può attraversarlo. 
In particolare, la velocità dipende dalle forze di tensione generata all'interno del materiale e dalla densità lineare dell'oggetto. 
$$
v = \sqrt{\dfrac{F_T}{d_L}}
$$
 >[!warning]
 > per quello che dobbiamo studiare, noi non è importante che ricordiate questa formula, ma semplicemente comprendiate che la velocità di un'onda dipende dalle caratteristiche ondulatoria che però derivano completamente dalle proprietà del materiale in cui l'onda si propaga.
 > 


### Funzione d'onda Armonica

Fino ad ora abbiamo parlato di [[#Moto armonico]] e abbiamo sempre descritto l'oscillazione solo tramite una variabile temporale: il tempo $t$. 
Le onde si propagano sia nello spazio e nel tempo, quindi è necessario utilizzare una funzione d'onda che sia più completa e comprenda anche un'informazione sullo spazio. 

In una corda che oscilla un punto generico di ascissa $x$  inizierà ad oscillare dall'istante $t = x/v$ in cui l'onda lo raggiungerà perciò la funzione d'onda completa ha l'aspetto di una funzione goniometrica traslata: 
$$
y(x,t)=A \cos\left[\omega\left(t-\frac{x}{v}\right)+\varphi_0\right]
$$
Se ricordiamo la definizione di $\omega$ vista nello studio del [[#Periodo]]  e gli archi associati della [[Goniometria]] possiamo scrivere: 

$$
y(x,t) = A \cos\left[\frac{2 \pi}{\lambda}\left(x-vt\right)+\varphi_0\right]  = A \cos\left[\frac{2 \pi}{\lambda}x- \frac{2 \pi}{T}t+\varphi_0\right]
$$

>[!warning]
>Queste diverse formulazioni della funzione d'onda armonica sono esattamente equivalenti e vengono utilizzate in funzione della richiesta del problema in cui può essere più utile conoscere alcuni dati piuttosto di altri.


## Interferenza Costruttiva e Distruttiva

> [!example] Simulazione
> Interferenza costruttiva e distruttiva, e i massimi e minimi tra due altoparlanti: [[Interferenza tra onde]].

### Principio di sovrapposizione

Due o più onde che si propagano nello spazio e nel tempo possono sovrapporsi in uno o più punti. La perturbazione totale provocata è data dalla <font color="#f59e0b">SOMMA</font> delle singole perturbazioni.

> [!tip] Principio di sovrapposizione
> Se due o più onde si propagano nello stesso mezzo, in ogni punto la perturbazione totale è la somma delle perturbazioni che ciascuna onda produrrebbe da sola.

>[!warning]
>Come facciamo a sommare delle funzioni generiche tipo:
>$$
>y_1(x,t) = A \cos{\omega(t-\frac{x}{v})} \quad \text{ e } \quad y_2(x,t) = A \cos{\omega(t-\frac{x}{v})}
>$$
>In generale si usa prostaferesi che però noi non vediamo!

![sovrapposizione-impulsi](sovrapposizione-impulsi.svg)

Due impulsi che si incontrano su una corda: se gli spostamenti sono uguali e nello stesso verso, nel punto di incontro lo spostamento è **doppio**; se sono uguali e opposti, lo spostamento è **nullo**. Dopo l'incontro ciascuna onda prosegue invariata, come se l'altra non ci fosse mai stata.

### Interferenza costruttiva e distruttiva

Quando due o più onde si sovrappongono si ha **interferenza**:

- è **costruttiva** se la perturbazione risultante è **maggiore** di quella delle singole onde;
- è **distruttiva** se la perturbazione risultante è **minore**.

Per due onde periodiche conta come oscillano in un punto fissato:

- sono **in fase** se in quel punto raggiungono insieme i massimi (e insieme i minimi);
- sono **in opposizione di fase** se quando una è al massimo l'altra è al minimo.

Due onde che oscillano in fase generano uno spostamento doppio nel punto in cui si incontrano. Due onde che oscillano in opposizione di fase generano uno spostamento nullo nel punto in cui si incontrano.

![Due onde in fase di ampiezze A1 e A2: la somma ha ampiezza A1 + A2](interferenza-in-fase.svg)

**In fase** $\longrightarrow$ massima interferenza costruttiva: l'onda risultante ha ampiezza $A_1 + A_2$.

![Due onde in opposizione di fase di ampiezze A1 e A2: la somma ha ampiezza |A1 − A2|](interferenza-opposizione.svg)

**In opposizione di fase** $\longrightarrow$ massima interferenza distruttiva: l'onda risultante ha ampiezza $|A_1 - A_2|$.

Se le due onde hanno la stessa ampiezza $A$, nel primo caso l'onda risultante ha ampiezza $2A$, nel secondo ampiezza $0$: le due onde si cancellano completamente.

> [!note]
> Se le due onde non sono né in fase né in opposizione di fase, l'interferenza è **in parte costruttiva o in parte distruttiva**, a seconda di quanto sono sfasate.

### Sorgenti coerenti

Per osservare un'interferenza stabile servono sorgenti che oscillano "d'accordo" tra loro.

> [!tip] Sorgenti coerenti
> Due sorgenti sono **coerenti** se oscillano con la stessa frequenza e con una **differenza di fase costante nel tempo**: raggiungono insieme i loro massimi (sorgenti in fase), oppure una li raggiunge sempre con lo stesso ritardo rispetto all'altra.

Esempi: due punte che oscillano insieme sulla superficie dell'acqua, oppure due altoparlanti collegati allo stesso amplificatore. Le onde circolari prodotte dalle due punte formano una **figura di interferenza** stabile: ci sono linee lungo le quali l'acqua è molto agitata (i massimi delle due onde arrivano sempre insieme: interferenza costruttiva) e linee lungo le quali è quasi ferma (a un massimo dell'una corrisponde un minimo dell'altra: interferenza distruttiva).

### Condizioni per l'interferenza costruttiva e distruttiva

Consideriamo due sorgenti $S_1$ e $S_2$ **in fase**, che emettono onde con la stessa lunghezza d'onda $\lambda$ e la stessa ampiezza. Che cosa succede in un punto dipende solo dalla **differenza tra le distanze** del punto dalle due sorgenti.

![Il punto P dista 4λ da S1 e 3λ da S2: le onde arrivano in fase](interferenza-cammini-costruttiva.svg)

Il punto $P$ dista $4\lambda$ da $S_1$ e $3\lambda$ da $S_2$. Le distanze differiscono di $\lambda$: lungo i due cammini "stanno" un numero intero di lunghezze d'onda, quindi le due onde arrivano in $P$ **in fase** e l'interferenza in $P$ è **costruttiva**.

![Il punto Q dista 4λ da S1 e 7λ/2 da S2: le onde arrivano in opposizione di fase](interferenza-cammini-distruttiva.svg)

Il punto $Q$ dista $4\lambda$ da $S_1$ e $\frac{7}{2}\lambda$ da $S_2$. Le distanze differiscono di $\frac{\lambda}{2}$: le due onde arrivano in $Q$ **in opposizione di fase**, il massimo dell'una insieme al minimo dell'altra, e l'interferenza in $Q$ è **distruttiva**.

In generale, per due sorgenti che oscillano in fase:

> [!success] Interferenza costruttiva
> Si ha nei punti $P$ in cui la differenza delle distanze dalle sorgenti è un **multiplo intero** della lunghezza d'onda:
> $$
> \overline{S_1P} - \overline{S_2P} = k\lambda \qquad k = 0, \pm 1, \pm 2, \dots
> $$

> [!failure] Interferenza distruttiva
> Si ha nei punti $Q$ in cui la differenza delle distanze dalle sorgenti è un **multiplo dispari di mezza** lunghezza d'onda:
> $$
> \overline{S_1Q} - \overline{S_2Q} = (2k+1)\frac{\lambda}{2} \qquad k = 0, \pm 1, \pm 2, \dots
> $$

Queste condizioni valgono anche per onde che si propagano nello spazio tridimensionale, per esempio le onde sonore.

> [!warning] Sorgenti in opposizione di fase
> Se le due sorgenti oscillano **in opposizione di fase** (per esempio due altoparlanti con i fili invertiti), partono già sfasate di mezza lunghezza d'onda e le due condizioni si **scambiano**:
> - $\Delta d = k\lambda$ $\longrightarrow$ interferenza **distruttiva**;
> - $\Delta d = (2k+1)\dfrac{\lambda}{2}$ $\longrightarrow$ interferenza **costruttiva**.

## Il suono

### Produzione e propagazione

Ogni suono nasce da un **corpo che vibra**: le membrane e i piatti di una batteria, le corde di una chitarra, le corde vocali nella laringe, la membrana di un altoparlante.

Pensiamo a una lamina che oscilla avanti e indietro nell'aria. Quando si sposta verso destra spinge l'aria davanti a sé (la **comprime**) e lascia dietro di sé aria meno densa (la **rarefà**); quando torna indietro succede il contrario. Le zone di compressione e di rarefazione si trasmettono agli strati d'aria via via più lontani: ogni volumetto d'aria oscilla avanti e indietro **lungo la stessa direzione** in cui l'onda si propaga, senza spostarsi complessivamente.

> [!tip] Il suono è un'onda meccanica longitudinale di pressione
> - **meccanica**: per propagarsi ha bisogno di un mezzo materiale (aria, acqua, solidi). Nel **vuoto il suono non si propaga**: un campanello che suona sotto una campana di vetro si sente sempre meno man mano che si aspira l'aria;
> - **longitudinale**: le particelle del mezzo oscillano parallelamente alla direzione di propagazione;
> - **di pressione**: quello che si propaga è un'alternanza di compressioni (pressione più alta) e rarefazioni (pressione più bassa) del mezzo.

![Strato d'aria con compressioni e rarefazioni; sotto, la variazione di pressione e lo spostamento dei volumetti d'aria lungo la direzione di propagazione](suono-compressioni.svg)

Un'onda sonora si può descrivere in due modi equivalenti:

- con la **variazione di pressione**: è massima nelle compressioni e minima nelle rarefazioni;
- con lo **spostamento dei volumetti d'aria**: è nullo proprio nelle compressioni e nelle rarefazioni, dove l'aria arriva da entrambi i lati (o se ne va da entrambi i lati).

Le due curve sono due funzioni armoniche **sfasate di $\frac{\pi}{2}$**: dove una ha un massimo o un minimo, l'altra passa per lo zero.

> [!info] Collegamenti
> Un'onda longitudinale in movimento, con le sue compressioni e rarefazioni, si vede nella seconda parte della simulazione [[Moto armonico e onde meccaniche]].

Quando un'onda sonora arriva all'orecchio mette in vibrazione il **timpano**, una sottile membrana; le vibrazioni passano agli **ossicini** e poi al liquido della **coclea**, dove vengono trasformate in segnali nervosi che il nervo acustico porta al cervello. Un microfono funziona in modo simile: il suono fa vibrare una membrana e il suo movimento diventa un segnale elettrico. L'altoparlante fa il percorso inverso.

### La velocità del suono

La velocità del suono dipende dal **mezzo** in cui si propaga, in particolare da quanto è **comprimibile** (elastico) e da quanto è **denso**:

- a parità di densità, il suono è più veloce nel mezzo **meno comprimibile**;
- a parità di comprimibilità, è più veloce nel mezzo **meno denso** (che ha meno inerzia).

Per questo nei solidi e nei liquidi il suono è in genere molto più veloce che nei gas. Nei gas la velocità dipende soprattutto dalla **temperatura**. In aria secca:

$$
v \approx 332\ \text{m/s} \ \text{a}\ 0\,^\circ\text{C} \qquad\qquad v \approx 340\ \text{m/s} \ \text{a}\ 20\,^\circ\text{C}
$$

![Velocità del suono a 20 °C in diversi mezzi, in m/s: aria 340, elio 965, acqua 1482, gomma vulcanizzata 60, piombo 1230, bronzo 3150, nichel 4970, ferro 5130](suono-velocita.svg)

> [!example] Tuoni e fulmini
> La luce viaggia a circa $300\,000\ \text{km/s}$: su distanze terrestri arriva praticamente subito. Il suono invece percorre circa $340\ \text{m}$ ogni secondo. Se tra il lampo e il tuono passano $3\ \text{s}$, il temporale è a circa $3 \cdot 340\ \text{m} \approx 1\ \text{km}$.

### L'eco

Come tutte le onde, anche il suono si **riflette** quando incontra il confine del mezzo in cui si propaga, per esempio una parete. La riflessione di un'onda sonora produce l'**eco**.

![Una persona a distanza d da una parete: l'onda emessa raggiunge la parete e torna indietro come onda riflessa](suono-eco.svg)

La voce va fino alla parete e torna indietro: percorre $2d$. Alla velocità $v$ impiega il tempo

$$
\Delta t = \frac{2d}{v}
$$

Per esempio, con $d = 20\ \text{m}$:

$$
\Delta t = \frac{2 \cdot 20\ \text{m}}{340\ \text{m/s}} \approx 0{,}12\ \text{s}
$$

L'orecchio distingue due suoni solo se arrivano a distanza di almeno $0{,}1\ \text{s}$ l'uno dall'altro: in questo tempo il suono percorre $34\ \text{m}$, quindi per sentire l'eco della propria voce bisogna stare ad almeno $17\ \text{m}$ dalla parete.

> [!info] Applicazioni
> Sullo stesso principio funzionano l'**ecografia** (onde sonore ad alta frequenza riflesse dagli organi interni ricostruiscono un'immagine del corpo) e il **sonar** delle navi (dal ritardo dell'eco si ricava la profondità del fondale).

### Le caratteristiche del suono

Un **rumore** è un'onda sonora **non periodica**, che varia in modo irregolare; un **suono** propriamente detto è un'onda sonora **periodica**.

![A sinistra un rumore, onda irregolare non periodica; a destra un suono, onda che si ripete uguale](suono-rumore-suono.svg)

Ogni suono ha tre caratteristiche, ciascuna legata a una grandezza dell'onda:

| Caratteristica | | Grandezza dell'onda |
| :---: | :---: | :---: |
| **Altezza**: suono acuto o grave | $\longrightarrow$ | **frequenza** $f$ |
| **Intensità**: suono forte o debole | $\longrightarrow$ | **ampiezza** (e quindi energia trasportata) |
| **Timbro**: "voce" dello strumento | $\longrightarrow$ | **forma dell'onda** |

**Altezza $\longrightarrow$ frequenza.** Più la frequenza è alta, più il suono è acuto.

![Due onde: quella grave ha frequenza bassa, quella acuta frequenza alta](suono-altezza.svg)

**Intensità $\longrightarrow$ ampiezza.** Un'onda di ampiezza maggiore produce compressioni e rarefazioni più marcate, trasporta più energia e il suono si sente più forte.

![Due onde con la stessa frequenza: quella debole ha ampiezza piccola, quella forte ampiezza grande](suono-intensita.svg)

**Timbro $\longrightarrow$ forma dell'onda.** La stessa nota (stessa frequenza) suonata da strumenti diversi ha forme d'onda diverse: è per questo che distinguiamo un violino da un pianoforte.

![Stessa nota con forme diverse: il diapason dà un'onda sinusoidale pura, uno strumento un'onda periodica più complessa](suono-timbro.svg)

**Limiti di udibilità.** L'orecchio umano percepisce suoni con frequenza compresa tra circa $20\ \text{Hz}$ e $20\,000\ \text{Hz}$. Le onde sonore con frequenza minore di $20\ \text{Hz}$ sono **infrasuoni**, quelle con frequenza maggiore di $20\,000\ \text{Hz}$ sono **ultrasuoni**: alcuni animali li sentono.

![Intervalli di frequenze udibili, in scala logaritmica: uomo da 20 a 20 000 Hz, cane da 65 a 45 000 Hz, pipistrello da 11 a 120 000 Hz](suono-udibilita.svg)

### Le note musicali

Ogni **nota** è un suono con una precisa frequenza. Quello che conta in musica non è la differenza tra le frequenze, ma il loro **rapporto**:

> [!tip] Intervallo e ottava
> - l'**intervallo** tra due note è il **rapporto** tra le loro frequenze;
> - un'**ottava** è l'intervallo di valore $2$: un *do* ha frequenza doppia del *do* precedente (e lo stesso vale per ogni altra nota).

Sulla tastiera di un pianoforte, partendo dal *la* a $440\ \text{Hz}$, nella **scala naturale** le note consecutive hanno questi rapporti:

![Un'ottava di pianoforte da do 264 Hz a do 528 Hz: tra i tasti bianchi vicini i rapporti sono 9/8, 10/9, 16/15, 9/8, 10/9, 9/8, 16/15; il do in alto ha frequenza doppia di quello in basso](suono-pianoforte.svg)

I rapporti tra note vicine **non sono tutti uguali**: quelli grandi ($\frac{9}{8}$ e $\frac{10}{9}$) sono **toni**, quelli piccoli ($\frac{16}{15}$, tra *mi* e *fa* e tra *si* e *do*, dove infatti non c'è il tasto nero) sono **semitoni**. Un'ottava contiene 5 toni e 2 semitoni, cioè 12 semitoni: sono i 12 tasti, bianchi e neri, di un'ottava.

La **scala temperata**, usata per accordare i pianoforti, divide l'ottava in 12 semitoni **tutti uguali**. Le frequenze cambiano pochissimo rispetto alla scala naturale, ma così un brano si può suonare partendo da qualunque nota senza che "stoni".

### Percepiamo in scala logaritmica

I nostri sensi non misurano gli stimoli in modo lineare. Se l'intensità di un suono raddoppia non lo sentiamo "forte il doppio": la sensazione cresce molto meno. Vale in buona approssimazione la **legge di Weber-Fechner**:

> [!tip] Legge di Weber-Fechner
> La sensazione è proporzionale al **logaritmo** dello stimolo: quello che percepiamo non è la variazione assoluta di uno stimolo, ma la sua **variazione relativa** (di quante volte è aumentato).

Lo stesso succede con la luce (la vista), con il peso degli oggetti, perfino con i numeri grandi: la differenza tra 1 e 2 ci sembra enorme, quella tra 1001 e 1002 trascurabile.

![Sensazione in funzione dell'intensità su scala lineare: la curva sale molto all'inizio e poi si appiattisce](suono-percezione-lineare.svg)

Se mettiamo l'intensità su un asse **logaritmico**, in cui ogni tacca vale 10 volte la precedente, la stessa curva diventa una **retta**: a ogni moltiplicazione per 10 dell'intensità corrisponde lo stesso "gradino" di sensazione.

![Sensazione in funzione dell'intensità su scala logaritmica, da 10^-12 a 1 W/m²: la curva diventa una retta](suono-percezione-log.svg)

**Vantaggi.**
- Possiamo sentire suoni di intensità **enormemente diverse**: dalla soglia di udibilità ($10^{-12}\ \text{W/m}^2$) alla soglia del dolore ($10\ \text{W/m}^2$) ci sono **13 ordini di grandezza**. Con una risposta lineare dovremmo scegliere: o sentiamo un bisbiglio, o sopportiamo un concerto.
- Siamo molto sensibili ai **piccoli cambiamenti relativi**: un suono che aumenta del 25% lo notiamo sia in una stanza silenziosa sia in mezzo al traffico.

**Svantaggi.**
- A intensità alte **sottovalutiamo gli aumenti**: passare da $80$ a $90\ \text{dB}$ ci sembra "un po' più forte", ma l'energia che colpisce il timpano è diventata **10 volte** maggiore. È per questo che il volume alto è pericoloso: il danno all'udito arriva prima che il suono ci sembri insopportabile.
- Non sappiamo stimare le differenze assolute: aggiungere la stessa potenza sonora si sente moltissimo in una stanza silenziosa e quasi per niente a un concerto.

> [!warning] Perché l'intensità sonora si misura con un logaritmo
> 1. Gli **intervalli di valori** sono enormi ($10^{-12}$–$10\ \text{W/m}^2$): con il logaritmo diventano numeri comodi, da $0$ a circa $130$.
> 2. Una scala logaritmica **somiglia a quello che sentiamo**: passi uguali sulla scala corrispondono a passi (circa) uguali di sensazione.

### Livello di intensità sonora e decibel

Si definisce allora il **livello di intensità sonora** $L_s$, misurato in **decibel** ($\text{dB}$):

$$
L_s = 10 \log_{10} \frac{I}{I_0} \qquad\qquad I_0 = 10^{-12}\ \text{W/m}^2
$$

dove $I$ è l'intensità dell'onda che arriva all'orecchio e $I_0$ è la minima intensità percepibile. $L_s$ è un numero puro.

Grazie alle proprietà dei logaritmi:

- per $I = I_0$ si ha $L_s = 10\log_{10} 1 = 0\ \text{dB}$: è la **soglia di udibilità**;
- se l'intensità **raddoppia**, il livello aumenta di circa $3\ \text{dB}$:

$$
L_{s,1} = 10 \log_{10} \frac{2I}{I_0} = 10\log_{10} 2 + 10 \log_{10} \frac{I}{I_0} \approx 3{,}01\ \text{dB} + L_s
$$

- se l'intensità diventa **10 volte** più grande, il livello aumenta di $10\ \text{dB}$; 100 volte, di $20\ \text{dB}$, e così via.

![Scala dei decibel da 0 a 180 dB con le intensità corrispondenti, da 10^-12 a 10^6 W/m²: soglia di udibilità 0, bisbiglio 30, conversazione 60, traffico 75, rischio per esposizioni prolungate 85, discoteca 100, soglia del dolore 130, aereo in decollo 140](suono-decibel.svg)

Il valore di $130\ \text{dB}$ è la **soglia del dolore**. In generale bisogna evitare di esporsi a lungo a livelli superiori a $85\ \text{dB}$, che possono danneggiare l'udito in modo permanente.

> [!example] Esempio
> Il fischietto di un allenatore arriva all'orecchio di un'atleta con intensità $I = 3{,}47 \times 10^{-3}\ \text{W/m}^2$. Il livello di intensità sonora è
> $$
> L_s = 10 \log_{10} \frac{3{,}47 \times 10^{-3}\ \text{W/m}^2}{10^{-12}\ \text{W/m}^2} = 10 \log_{10}\left(3{,}47 \times 10^{9}\right) \approx 10 \cdot 9{,}54 = 95{,}4\ \text{dB}
> $$

### I battimenti

Quando si sovrappongono due suoni con frequenze $f_1$ e $f_2$ **molto vicine**, le due onde passano periodicamente dall'essere in fase (interferenza costruttiva) all'essere in opposizione di fase (interferenza distruttiva). Si sente un suono di frequenza intermedia il cui volume **cresce e cala** regolarmente: sono i **battimenti**.

![Due onde di frequenze vicine f1 e f2 e la loro somma, la cui ampiezza aumenta e diminuisce periodicamente](suono-battimenti.svg)

La frequenza con cui il volume oscilla è la differenza tra le due frequenze:

$$
f_b = |f_1 - f_2|
$$

> [!info]
> I musicisti usano i battimenti per **accordare** gli strumenti: suonano la stessa nota insieme a un riferimento e regolano la corda finché i battimenti rallentano e spariscono, cioè finché $f_1 = f_2$.

### L'effetto Doppler

Il suono della sirena di un'ambulanza è più acuto quando si avvicina e più grave quando si allontana.

> [!tip] Effetto Doppler
> La frequenza rilevata da un ricevitore dipende dal **moto della sorgente** e dal **moto del ricevitore** rispetto al mezzo in cui l'onda si propaga.

Vale per tutte le onde: sull'effetto Doppler si basano, per esempio, i sensori che aprono le porte automatiche e l'**ecodoppler**, che misura la velocità del sangue nei vasi. Per il suono descriviamo tutto nel sistema di riferimento **dell'aria**: $v$ è la velocità del suono, $f$ la frequenza emessa dalla sorgente, $f'$ quella rilevata.

#### Sorgente ferma e ricevitore in movimento

I fronti di compressione sono distanti $\lambda$ l'uno dall'altro. Se il ricevitore va **verso** la sorgente con velocità $v_r$, li incontra con velocità relativa $v + v_r$, quindi ne incontra uno ogni

$$
\Delta t = \frac{\lambda}{v + v_r} \quad\longrightarrow\quad f' = \frac{1}{\Delta t} = \frac{v + v_r}{\lambda} = \frac{v + v_r}{v}\,f
$$

Se si allontana cambia solo il segno. In generale:

$$
f' = \frac{v \pm v_r}{v}\,f \qquad \begin{cases} + & \text{ricevitore che si avvicina} \;\Rightarrow\; f' > f \\ - & \text{ricevitore che si allontana} \;\Rightarrow\; f' < f \end{cases}
$$

#### Sorgente in movimento e ricevitore fermo

Se è la sorgente a muoversi con velocità $v_s$, i fronti sono sfere che si allargano con velocità $v$ ma hanno i centri che si spostano insieme alla sorgente: **davanti** alla sorgente si addensano, **dietro** si diradano.

![Sorgente che si muove verso destra: i fronti d'onda circolari sono ravvicinati davanti (suono più acuto) e distanziati dietro (suono più grave)](suono-doppler.svg)

In un periodo $T = \frac{1}{f}$ un fronte percorre $\frac{v}{f}$, ma intanto la sorgente avanza di $\frac{v_s}{f}$ prima di emettere il fronte successivo. Davanti alla sorgente la lunghezza d'onda diventa

$$
\lambda' = \frac{v}{f} - \frac{v_s}{f} = \frac{v - v_s}{f} \quad\longrightarrow\quad f' = \frac{v}{\lambda'} = \frac{v}{v - v_s}\,f
$$

In generale:

$$
f' = \frac{v}{v \mp v_s}\,f \qquad \begin{cases} - & \text{sorgente che si avvicina} \;\Rightarrow\; f' > f \\ + & \text{sorgente che si allontana} \;\Rightarrow\; f' < f \end{cases}
$$

> [!warning]
> Le due formule sono **diverse**: l'effetto non dipende solo dalla velocità relativa tra sorgente e ricevitore, ma da **chi** si muove rispetto all'aria.

#### Sorgente e ricevitore entrambi in movimento

Mettendo insieme i due casi:

$$
f' = \frac{v \pm v_r}{v \mp v_s}\,f
$$

con i segni superiori quando ricevitore e sorgente si muovono **uno verso l'altro**. Qui i segni da soli non bastano a dire se $f'$ è maggiore o minore di $f$: dipende da quale dei due effetti prevale.

> [!example] Esempio: suono riflesso da un furgone
> Un altoparlante fermo emette un suono di $f = 740\ \text{Hz}$; un furgone si allontana a $v_F = 83\ \text{km/h} \approx 23\ \text{m/s}$ e riflette il suono verso un microfono vicino all'altoparlante.
> 1. Il furgone è un **ricevitore che si allontana**: $f' = \dfrac{v - v_F}{v}\,f$.
> 2. Il retro del furgone rimanda indietro il suono: ora è una **sorgente che si allontana**: $f_M = \dfrac{v}{v + v_F}\,f'$.
>
> $$
> f_M = \frac{v - v_F}{v + v_F}\,f = \frac{(340 - 23)\ \text{m/s}}{(340 + 23)\ \text{m/s}} \cdot 740\ \text{Hz} \approx 646\ \text{Hz}
> $$
> Il suono riflesso è più grave di quello emesso.

#### Una sorgente più veloce dell'onda

Più la sorgente è veloce, più i fronti davanti a lei sono ravvicinati. Se $v_s = v$ la formula perde significato (il denominatore si annulla): i fronti si accumulano uno sull'altro e formano una barriera di aria compressa, l'**onda d'urto**, che viaggia insieme alla sorgente. Se $v_s > v$ l'onda d'urto prende la forma di un **cono** con la sorgente nel vertice.

![Sorgente più veloce del suono: i fronti circolari emessi restano indietro e il loro inviluppo è un cono, l'onda d'urto](suono-onda-urto.svg)

Quando un aereo supera la velocità del suono, l'onda d'urto arriva fino a terra e si sente come un forte boato, il **bang supersonico**. La scia a forma di V di una nave che va più veloce delle onde sull'acqua è lo stesso fenomeno.
