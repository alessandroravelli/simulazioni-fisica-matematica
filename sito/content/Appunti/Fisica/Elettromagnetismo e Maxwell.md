---
title: Elettromagnetismo e Maxwell
description: Esperimenti di Faraday, legge di Faraday-Neumann-Lenz, applicazioni, autoinduzione e circuito RL, mutua induzione, equazioni di Maxwell, onde elettromagnetiche, irradianza, pressione di radiazione e legge di Malus.
tags:
  - fisica
  - elettromagnetismo
  - onde
  - 5SCI
---
Ricordiamo che, come abbiamo già visto nel [[Ripasso campo magnetico e moto nei campi magnetici|ripasso sul campo magnetico]], quando un filo è percorso da corrente, questo genera un campo magnetico. Quello che vediamo adesso sono degli esperimenti proposti da Faraday, che scoprì in maniera empirica che il legame tra corrente e campo magnetico è molto più profondo di quanto pensiamo per ora.

## 4 esperimenti di Faraday

In tutti e quattro c'è un circuito con un solenoide, senza generatore, collegato a un amperometro che inizialmente segna $i = 0\ \text{A}$.

1. **Magnete.** Con il magnete fermo e il circuito senza generatore $i = 0\ \text{A}$. <span style="color:#f59e0b">Muovo il magnete e leggo $i \neq 0\ \text{A}$.</span>
2. **Secondo circuito.** Un secondo circuito con generatore è un filo percorso da corrente $\Rightarrow$ genera $\vec B$. Se è fermo $i = 0\ \text{A}$ nel primo. <span style="color:#f59e0b">Muovo il circuito e ottengo $i \neq 0\ \text{A}$.</span>
3. **Interruttore.** Quando chiudo l'interruttore $i \neq 0\ \text{A}$ nel secondo circuito $\Rightarrow$ $\vec B$ cambia e $i \neq 0\ \text{A}$ nel primo.
4. **Resistenza variabile.** Se nel secondo circuito ho una resistenza variabile $R_v$ $\Rightarrow$ $i_{eq} = \dfrac{\Delta V}{R_{eq}}$ cambia $\Rightarrow$ $\vec B$ cambia $\Rightarrow$ $i \neq 0\ \text{A}$ nel primo.

$$
\longrightarrow\quad \textcolor{#f59e0b}{\text{se in un circuito immerso in } \vec B \text{ il campo cambia si genera una corrente indotta}}
$$

> [!info] Collegamenti
> Prova tu a muovere il magnete vicino alla spira nella simulazione [[Induzione elettromagnetica]]: la corrente compare solo mentre il flusso cambia.

### Perché nasce la corrente

In un conduttore neutro le cariche positive e negative sono mescolate. Se il conduttore si muove con velocità $\vec v$ in un campo $\vec B$ (uscente), le cariche si spostano: le negative da una parte, le positive dall'altra, e ai capi del conduttore nasce una fem. Le cariche si spostano a causa di

$$
\vec F = q\,\vec v \times \vec B
$$

Consideriamo una sbarretta che scorre su due binari chiusi da un lato, in un campo $\vec B$ uscente.

![Sbarretta conduttrice che scorre su due binari: la superficie del circuito diminuisce mentre la sbarretta avanza](barretta-binari.svg)

$$
\Phi_{in}(\vec B) = B\,S_{in}\cos\theta = B\,S_{in} \qquad \Phi_{fin}(\vec B) = B\,S_{fin}\cos\theta = B\,S_{fin}
$$

Di quanto cambia $\Phi$?

$$
\Delta\Phi = \Phi_{fin} - \Phi_{in} = B\,(S_{fin} - S_{in}) = B\,\ell\,\underbrace{(x_{fin} - x_{in})}_{<\,0} = B\,\ell\,(-v\,\Delta t)
$$

$$
\longrightarrow\quad \frac{\Delta\Phi}{\Delta t} = -B\,\ell\,v
$$

**Cosa succede alle cariche quando tornano alla sbarretta carica?** La carica $\oplus$ subisce lavoro quando viene riportata al polo $+$:

$$
W_{-\to+} = \vec F_L \cdot \vec\ell = F_L\,\ell\cos 180^\circ = e\,v\,B\,\ell
$$

$$
\text{fem} = \frac{W_{-\to+}}{e} = \frac{\cancel{e}\,v\,B\,\ell}{\cancel{e}} = v\,B\,\ell
$$

> [!note] Segno della fem
> La fem è simile a $\Delta V$ ma è definita con $\dfrac{W}{q}$, quindi con un segno opposto.

$$
\longrightarrow\quad \text{fem} = -\frac{\Delta\Phi(\vec B)}{\Delta t} \quad\xrightarrow{\ \text{Ohm}\ }\quad i = -\frac{\Delta\Phi(\vec B)}{\Delta t \cdot R}
$$

Abbiamo utilizzato la definizione di potenziale elettrico tramite il lavoro e abbiamo ottenuto la formulazione del valore della corrente indotta.

$$
\textcolor{#f59e0b}{\text{Legge di Faraday-Neumann:}} \quad \text{fem} = -\frac{\Delta\Phi(\vec B)}{\Delta t}
$$

## In che verso circola la corrente?

Abbiamo capito che quando un campo magnetico varia, e il flusso di questo campo magnetico attraverso un circuito o una spira di conseguenza cambia, allora si genera automaticamente una corrente indotta. La corrente in un circuito però può viaggiare in due direzioni e qui dobbiamo capire in che direzione viaggia la corrente indotta. Vediamo due casi:

![Un magnete si avvicina a una spira: a sinistra il campo indotto rinforzerebbe la variazione, a destra si oppone](lenz.svg)

**Primo caso.** Supponiamo che la corrente indotta abbia un verso orario: così facendo il campo generato dalla corrente indotta all'interno della spira alimenta ancora di più la variazione di campo magnetico, perché la prima variazione di campo magnetico data dal magnete genera una corrente che aumenta la variazione di campo magnetico, che a sua volta alimenta la corrente. Questo processo non è fisicamente accettabile perché la corrente aumenterebbe all'infinito.

**Secondo caso.** La corrente gira invece in senso antiorario: in questo modo il flusso generato dalla spira si oppone al flusso entrante del magnete. La corrente indotta funziona quindi un po' come un freno: la stessa corrente genera un flusso uguale e opposto a quello che l'ha generata. Fisicamente questo è accettabile perché pone un limite al nostro sistema.

### Legge di Lenz

$$
\text{in} \quad \text{fem} = -\frac{\Delta\Phi(\vec B)}{\Delta t} \qquad \text{oppure in} \quad i = -\frac{1}{R}\,\frac{\Delta\Phi(\vec B)}{\Delta t}
$$

il "$-$" è un contributo di Lenz ed è una legge di conservazione dell'energia: ci indica che **$i_{\text{indotta}}$ scorre sempre in modo da opporsi alla variazione esterna di flusso!**

## Applicazioni

### Piano a induzione

L'avvolgimento che sta sotto la pentola, percorso dalla corrente alternata degli impianti casalinghi, genera a sua volta un campo magnetico alternato. Siccome il campo varia costantemente, nella pentola si creano costantemente delle correnti che devono bilanciare la variazione di flusso. Queste correnti, per effetto Joule, scaldano la padella.

### Alternatore

Questo strumento permette di caricare la batteria dell'automobile quando si viaggia, oppure per esempio permette di tenere accese le luci delle biciclette mentre avanzano. Ha anche moltissime applicazioni nelle auto elettriche per quanto riguarda il recupero di energia.

Una spira ruota tra i poli N e S di un magnete. Quando l'angolo $\alpha$ tra la spira e le linee di campo passa da $0^\circ$ a $90^\circ$, $180^\circ$, $270^\circ$, $360^\circ$, il flusso attraverso la spira oscilla come un coseno e la corrente indotta come un seno:

![Durante la rotazione il flusso Φ segue un coseno e la corrente indotta i un seno, sfasati di un quarto di giro](alternatore-grafico.svg)

Il meccanismo con cui l'alternatore funziona prevede che ci sia un agente esterno che faccia muovere la spira, come per esempio la ruota di una bicicletta che avanza oppure l'albero motore di un'auto a combustione interna, e questa rotazione meccanica viene trasformata in corrente alternata. Similmente si può creare un motore elettrico generando corrente alternata per far sì che una spira ruoti, e questa, una volta collegata a un albero di trasmissione, genera il moto.

> [!info] Collegamenti
> Φ e $i$ sono sfasati di $\frac{\pi}{2}$ come seno e coseno in [[Goniometria#Funzioni lineari in seno e coseno|goniometria]], e come posizione e velocità nel [[Onde suono e luce#Moto armonico|moto armonico]].

## Autoinduzione

A causa della legge di Faraday-Neumann-Lenz, quando chiudiamo l'interruttore di un circuito e inizia a circolare della corrente, questa non può crescere istantaneamente al valore che ci aspettiamo, ma è forzata a crescere più lentamente.

1. Chiudo l'interruttore e $i$ circola
2. $i$ variabile $\Rightarrow$ $\vec B$ variabile
3. Flusso variabile $\Rightarrow$ $i$ indotta
4. $\vec B$ indotto che si oppone a $\vec B$ variabile

$$
\Longrightarrow\quad \textcolor{#f59e0b}{\text{la corrente cresce più lentamente}}
$$

![La corrente dopo la chiusura dell'interruttore cresce gradualmente fino al valore fem°/R](rl-carica.svg)

### Autoinduzione e solenoide

Consideriamo un solenoide collegato a un generatore.

$$
B = \mu_0\, n\, i = \mu_0\,\frac{N}{\ell}\, i \qquad \Phi_{tot} = B \cdot S \cdot N \cdot \cos 0^\circ \qquad \Phi_{spira} = B \cdot S \cdot \cos 0^\circ
$$

$$
\Phi_{tot} = \mu_0\,\frac{N}{\ell}\, i\, N\, S = \mu_0\,\frac{N^2}{\ell}\, S \cdot i = L \cdot i
$$

$$
\longrightarrow\quad \textcolor{#f59e0b}{\Phi_{tot} = L \cdot i}
$$

La corrente in un circuito genera $\vec B$, che produce $\Phi_{tot}(\vec B)$ attraverso il circuito stesso pari a $L \cdot i$.

$L :=$ **induttanza** (coefficiente di autoinduzione), $\quad [L] = \text{H} :=$ Henry

## Circuito RL

Un circuito in cui sono presenti **resistenze** e **induttanze** (solenoidi), alimentato da un generatore di forza elettromotrice $\text{fem}^\circ$.

$$
\Phi(B) = L \cdot i \qquad \frac{\Delta\Phi}{\Delta t} = L\,\frac{\Delta i}{\Delta t} \quad\longrightarrow\quad -\text{fem} = L\,\frac{\Delta i}{\Delta t}
$$

$$
\text{fem} = -L\,\frac{\Delta i}{\Delta t} \qquad \text{caduta di potenziale ai capi di } L
$$

Uso Kirchhoff:

$$
\text{fem}^\circ - R\,i - L\,\frac{\Delta i}{\Delta t} = 0
$$

Con il calcolo infinitesimale:

$$
\text{fem}^\circ - R\,i - L\,\frac{di}{dt} = 0 \quad\longrightarrow\quad \frac{di}{dt} + \frac{R}{L}\, i - \frac{\text{fem}^\circ}{L} = 0
$$

È un'equazione differenziale lineare del primo ordine: con la formula risolutiva

$$
i(t) = e^{-\frac{R}{L}t}\left[\int e^{\frac{R}{L}t} \cdot \frac{\text{fem}^\circ}{L}\, dt + c\right] = e^{-\frac{R}{L}t}\left[\frac{\text{fem}^\circ}{L} \cdot \frac{L}{R}\, e^{\frac{R}{L}t} + c\right] = \frac{\text{fem}^\circ}{R} + c\, e^{-\frac{R}{L}t}
$$

$$
i(0) = 0\ \text{A} \quad\Longrightarrow\quad \frac{\text{fem}^\circ}{R} + c = 0 \quad\longrightarrow\quad c = -\frac{\text{fem}^\circ}{R}
$$

$$
\Longrightarrow\quad i(t) = \frac{\text{fem}^\circ}{R}\left(1 - e^{-\frac{R}{L}t}\right) \qquad \lim_{t \to +\infty} i(t) = \frac{\text{fem}^\circ}{R}
$$

$$
\tau = \frac{L}{R} := \text{tempo caratteristico} \qquad [\tau] = \text{s}
$$

> [!info] Collegamenti
> Puoi controllare la soluzione disegnandola con la simulazione [[Equazioni differenziali del primo ordine]].

### RL senza generatore

$$
-R\,i - L\,\frac{di}{dt} = 0 \quad\longrightarrow\quad i(t) = I\, e^{-\frac{R}{L}t}
$$

![Senza generatore la corrente cala esponenzialmente a partire dal valore iniziale I](rl-scarica.svg)

## Mutua induzione

Due circuiti vicini: il primo con un generatore, il secondo con un amperometro.

Se $i_1$ varia $\Rightarrow$ $B_1$ varia $\Rightarrow$ $\Phi_2(B_1)$ varia $\Rightarrow$ genero $i_2$ $\Rightarrow$ genero $\text{fem}^{1\to2}$

$$
\Phi_2(B_1) = M\, i_1
$$

$$
\text{fem}^{1\to2} = -\frac{\Delta\Phi_2}{\Delta t} = -M\,\frac{\Delta i_1}{\Delta t} \qquad \text{fem}^{2\to1} = -M\,\frac{\Delta i_2}{\Delta t}
$$

## Energia e densità di energia di B

Similmente a quanto succede per il campo elettrico e il lavoro per caricare un condensatore:

$$
W_L = \frac{1}{2}\, L\, i^2 \quad := \text{lavoro per portare la corrente da 0 a } I \text{ in } L
$$

Densità di energia:

$$
w_L = \frac{W_L}{\underbrace{S \cdot \ell}_{\text{volume}}} = \frac{1}{2}\, L\, i^2\,\frac{1}{S\ell} = \frac{1}{2}\,\mu_0\,\frac{N^2 S}{\ell}\, i^2\,\frac{1}{S\ell} = \frac{1}{2\mu_0}\, B^2
$$

<span style="color:#f59e0b">Ricordo per il solenoide: $B = \mu_0\,\dfrac{N}{\ell}\, i$.</span>

## Equazioni di Maxwell

Per il momento conosciamo tre equazioni che riguardano elettrostatica e magnetismo, da cui si possono derivare i principali risultati che abbiamo visto. Le equazioni di Maxwell però sono quattro e di conseguenza ci serve definire una quarta equazione.

**Equazioni di Maxwell statiche** (i campi non variano):

$$
1)\ \ \Phi_\Sigma(\vec E) = \frac{Q_{tot}}{\varepsilon_0} \qquad 2)\ \ ? \qquad 3)\ \ \Phi_\Sigma(\vec B) = 0 \qquad 4)\ \ \Gamma_{\mathcal L}(\vec B) = \mu_0\, i_{\mathcal L}
$$

### 2ª legge di Maxwell

Come con $\vec B$, calcolo la circuitazione:

$$
\Gamma_{\mathcal L}(\vec E) = \sum_{i=1}^{n} \vec E_i \cdot \Delta\vec\ell_i = \sum \frac{\vec F_i}{\Delta q} \cdot \Delta\vec\ell_i = \sum \frac{W_i}{\Delta q} = -\sum \Delta V_i = \text{fem}^\circ
$$

Immagino $n = 3$ e $\mathcal L$ chiuso:

$$
= -\sum_{i=1}^{3} \left(V_{i+1} - V_i\right) = -\left(\cancel{V_2} - \cancel{V_1} + \cancel{V_3} - \cancel{V_2} + \cancel{V_1} - \cancel{V_3}\right) = 0 = \text{fem}^\circ
$$

$\Gamma_{\mathcal L}(\vec E) = 0\ \text{V}$: in condizioni statiche la circuitazione in un percorso chiuso è **nulla**.

<span style="color:#f59e0b">Se $\vec B$ varia però possiamo generare una corrente indotta:</span>

$$
\text{fem} = -\frac{\Delta\Phi}{\Delta t} \qquad \Gamma_{\mathcal L}(\vec E) = \text{fem} \quad\longrightarrow\quad \Gamma_{\mathcal L}(\vec E) = -\frac{\Delta\Phi}{\Delta t}
$$

Se $\Gamma(\vec E) \neq 0$ sto generando campo elettrico.

$$
\textcolor{#f59e0b}{\text{posso generare } \vec E \text{ con cariche elettriche e con } \vec B \text{ variabile}}
$$

In analogia con la legge di Lenz, il campo elettrico indotto generato dalla variazione di campo magnetico si dovrà opporre alla variazione dello stesso campo magnetico: se $\vec B$ aumenta, le linee di $\vec E$ indotto girano in modo che il campo magnetico da esso generato si opponga a $\Delta\vec B$; se $\vec B$ diminuisce, girano nel verso opposto.

Ora abbiamo visto tutte e quattro le equazioni di Maxwell, ma soltanto per la seconda abbiamo visto il caso in cui i campi cambiano nel tempo.

$$
1)\ \ \Phi_\Sigma(\vec E) = \frac{Q_{tot}}{\varepsilon_0} \qquad 3)\ \ \Phi_\Sigma(\vec B) = 0
$$

Queste due equazioni non cambiano quando consideriamo campi variabili, dal momento che si affidano alla presenza o meno di cariche, che inevitabilmente rimangono quello che sono.

### 4ª legge di Maxwell

Per $\vec E$ abbiamo visto:

$$
\text{statico: } \Gamma_{\mathcal L}(\vec E) = 0 \quad\longrightarrow\quad \text{dinamico: } \Gamma_{\mathcal L}(\vec E) = -\frac{\Delta\Phi(\vec B)}{\Delta t}
$$

Per $\vec B$ abbiamo:

$$
\text{statico: } \Gamma_{\mathcal L}(\vec B) = \mu_0\, i_{\mathcal L} \quad\longrightarrow\quad \text{dinamico: } \Gamma_{\mathcal L}(\vec B) = \ ?
$$

Consideriamo un circuito di questo tipo, con un condensatore:

![Circuito con un condensatore: la linea L1 abbraccia il filo, la linea L2 passa tra le armature](maxwell-condensatore.svg)

$$
\Gamma_{\mathcal L_1}(\vec B) = \mu_0\, i \qquad \Gamma_{\mathcal L_2}(\vec B) = 0
$$

Non va bene: $\Gamma_{\mathcal L}(\vec B)$ è una proprietà del circuito e non posso avere 2 valori diversi.

<span style="color:#f59e0b">Maxwell, per similitudine a $\Gamma_{\mathcal L}(\vec E)$, aggiunge:</span>

$$
\Gamma_{\mathcal L}(\vec B) = \mu_0\left[i_{\mathcal L} + \varepsilon_0\,\frac{\Delta\Phi(\vec E)}{\Delta t}\right]
$$

Se $\vec E$ è statico $\Rightarrow$ $\Gamma_{\mathcal L}(\vec B) = \mu_0\, i_{\mathcal L}$ **ok!**

Se $\vec E$ è variabile:

$$
\varepsilon_0\,\frac{\Delta\left(Q_{tot}/\varepsilon_0\right)}{\Delta t} = \cancel{\varepsilon_0} \cdot \frac{1}{\cancel{\varepsilon_0}} \cdot \frac{\Delta Q}{\Delta t} = i_s \quad := \text{corrente di spostamento}
$$

$$
\Gamma_{\mathcal L}(\vec B) = \mu_0\left[i + i_s\right] \qquad i_s = i
$$

Con $\vec E$ variabile: se sono in $\mathcal L_1$ $\rightarrow$ $i_s = 0$; se sono in $\mathcal L_2$ $\rightarrow$ $i = 0$.

$\longrightarrow$ <span style="color:#f59e0b">Non importa dove mi trovo: $\Gamma_{\mathcal L}(\vec B)$ ha lo stesso valore $\forall\,\mathcal L$.</span>

- Se $\vec E$ aumenta, $\vec B$ segue il verso di $i$ concorde con $\vec E$.
- Se $\vec E$ diminuisce, $\vec B$ segue il verso di $i$ discorde ad $\vec E$.

### Equazioni di Maxwell complete

**Forma compatta**

$$
\begin{aligned}
&1)\ \ \Phi_\Sigma(\vec E) = \frac{Q_{tot}}{\varepsilon_0} \\
&2)\ \ \Gamma_{\mathcal L}(\vec E) = -\frac{d\Phi(\vec B)}{dt} \\
&3)\ \ \Phi_\Sigma(\vec B) = 0 \\
&4)\ \ \Gamma_{\mathcal L}(\vec B) = \mu_0\left[i_{\mathcal L} + \varepsilon_0\,\frac{d\Phi(\vec E)}{dt}\right]
\end{aligned}
$$

**Forma integrale**

$$
1)\ \ \oint_\Sigma \vec E \cdot d\vec S = \frac{Q_{tot}}{\varepsilon_0} \qquad 2)\ \ \oint_{\partial\Sigma} \vec E \cdot d\vec\ell = -\frac{d\Phi(\vec B)}{dt}
$$

$$
3)\ \ \oint_\Sigma \vec B \cdot d\vec S = 0 \qquad 4)\ \ \oint_{\partial\Sigma} \vec B \cdot d\vec\ell = \mu_0\left[i_{\mathcal L} + \varepsilon_0\,\frac{d\Phi(\vec E)}{dt}\right]
$$

Se $Q_{tot} = \displaystyle\int \rho\, dV$ e $\Phi(\vec B) = \displaystyle\int \vec B \cdot d\vec S$:

**Forma differenziale**

$$
1)\ \ \nabla \cdot \vec E = \rho \qquad 2)\ \ \nabla \times \vec E = -\partial_t \vec B \qquad 3)\ \ \nabla \cdot \vec B = 0 \qquad 4)\ \ \nabla \times \vec B = \vec J + \partial_t \vec E
$$

> [!note] Unità di misura
> Le forme differenziali qui sopra sono scritte in unità in cui $\varepsilon_0 = \mu_0 = c = 1$. Nel Sistema Internazionale diventano $\nabla \cdot \vec E = \dfrac{\rho}{\varepsilon_0}$ e $\nabla \times \vec B = \mu_0 \vec J + \mu_0\varepsilon_0\,\partial_t \vec E$.

> [!abstract]- Per chi vuole andare oltre
> Introducendo i potenziali: $\vec B = \nabla \times \vec A$ ed $\vec E = -\nabla\phi$ (nel caso statico).
>
> Al campo elettromagnetico si associa la quantità
> $$-\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \qquad \text{dove} \qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

## Onde elettromagnetiche

Considero una carica $q$ che oscilla tra 2 punti. Cosa succede ad $\vec E$ e $\vec B$ in un punto fisso dello spazio?

$$
\vec E = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r^2} \quad\longrightarrow\quad \text{varia con la distanza}
$$

$\vec B$ dipende da $i$, che cambia di continuo perché la carica si muove avanti e indietro.

$$
\textcolor{#f59e0b}{\vec E \text{ variabile genera } \vec B \text{ variabile, che genera } \vec E \text{ variabile} \ldots}
$$

<span style="color:#f59e0b">Origine di un'onda elettromagnetica che si propaga nel vuoto.</span>

Velocità di un'onda nel vuoto:

$$
c = \frac{1}{\sqrt{\varepsilon_0\,\mu_0}} = 2{,}9 \cdot 10^8\ \frac{\text{m}}{\text{s}}
$$

In un mezzo:

$$
v = \frac{1}{\sqrt{\varepsilon\,\mu}} = \frac{1}{\sqrt{\varepsilon_r\,\mu_r}} \cdot c = \frac{c}{n} \quad\Longrightarrow\quad n = \sqrt{\varepsilon_r\,\mu_r}
$$

### Proprietà delle onde elettromagnetiche

Dalle equazioni di Maxwell deduciamo che $\vec E \perp \vec B$ ed entrambi sono perpendicolari alla direzione di propagazione. In ogni punto dell'onda ci sono sia $\vec E$ che $\vec B$.

![Onda elettromagnetica: il campo E oscilla in un piano, il campo B nel piano perpendicolare, entrambi perpendicolari alla propagazione](onda-em.svg)

In particolare i valori di $E$ e $B$ in un'onda EM sono legati da $E = cB$.

> [!info] Collegamenti
> Come ogni onda armonica, anche l'onda elettromagnetica si descrive con una [[Onda progressiva in 3D|funzione di spazio e tempo]]; per le onde in generale vedi [[Onde suono e luce]].

### Energia di un'onda

$$
\left.\begin{aligned} w_E &= \frac{1}{2}\,\varepsilon_0\, E^2 \\ w_B &= \frac{1}{2\mu_0}\, B^2 \end{aligned}\right\} \quad \text{densità energetiche di } \vec E \text{ e } \vec B
$$

$$
w = w_E + w_B = \frac{1}{2}\left(\varepsilon_0 E^2 + \frac{1}{\mu_0} B^2\right) = \frac{1}{2}\,\varepsilon_0\left(E^2 + c^2 B^2\right) = \varepsilon_0\, E^2 \quad \textcolor{#f59e0b}{\text{densità energetica di un'onda EM}}
$$

Le onde oscillano: se si considerano $E$ e $B$ variabili si ottiene

$$
\overline{w} = \frac{1}{2}\,\varepsilon_0\, E^2 \quad \text{densità energetica media} \qquad [\overline{w}] = \frac{\text{energia}}{\text{volume}}
$$

### Irradiamento

Sappiamo che l'irradiamento è definito da

$$
E_R = \frac{\mathcal E}{\Delta t \cdot A}
$$

L'onda si propaga con velocità $c$ e in $\Delta t$ copre un volume $c\,\Delta t\, A$.

$$
\longrightarrow\quad \text{l'energia totale è } \mathcal E = c\,\Delta t\, A\,\overline{w}
$$

$$
\Longrightarrow\quad E_R = \frac{c\,\Delta t\, A\,\overline{w}}{\Delta t\, A} = c\,\overline{w} = \frac{1}{2}\, c\,\varepsilon_0\, E^2
$$

### Quantità di moto

$\vec E$ e $\vec B$ permettono di far muovere una carica $q$ e quindi è possibile trasmettere quantità di moto secondo:

$$
\Delta p = \frac{\mathcal E}{c}
$$

$$
F = \frac{\Delta p}{\Delta t} \quad \text{per il teorema dell'impulso} \quad\longrightarrow\quad F = \frac{\mathcal E}{c\,\Delta t}
$$

$$
P_R = \frac{F}{A} = \frac{\mathcal E}{c\,\Delta t\, A} = \frac{E_R}{c} \quad := \textcolor{#f59e0b}{\text{pressione di radiazione}}
$$

> [!info] Collegamenti
> Che la luce trasporti quantità di moto $p = \mathcal E / c$ si ritrova nella [[Relatività#Equivalenza massa-energia|equivalenza massa-energia]] e nell'[[Crisi della fisica classica#Effetto Compton|effetto Compton]].

## Polarizzazione

Vedi la simulazione [[Polarizzazione della luce]].

### Legge di Malus

La fisica ci permette di determinare cosa succede all'intensità, e di conseguenza all'irradianza, di un'onda elettromagnetica quando attraversa un filtro polarizzatore. In generale un fascio di luce naturale, e quindi non polarizzato, ha il campo elettrico (e di conseguenza quello magnetico) che oscilla in maniera disordinata e casuale. Quando prendiamo un'onda elettromagnetica non polarizzata e la facciamo passare attraverso un filtro polarizzatore lineare, ovvero che seleziona soltanto una singola direzione, l'irradianza varia in questa maniera:

$$
E_R^{\text{lin.}} = \frac{E_R^{\text{non pol.}}}{2}
$$

Ora ci si può chiedere che cosa succede nel caso in cui prendiamo un'onda già polarizzata linearmente e la facciamo passare attraverso un secondo filtro polarizzatore, che ha un angolo di inclinazione $\alpha$ rispetto alla direzione iniziale.

![Il campo E forma un angolo α con l'asse di trasmissione del filtro: passa solo la componente parallela](malus.svg)

$$
E_\parallel = E\cos\alpha \quad\Longrightarrow\quad E_{R_\alpha} = \frac{1}{2}\, c\,\varepsilon_0\, E_\parallel^2 = \frac{1}{2}\, c\,\varepsilon_0\, E^2\cos^2\alpha
$$

$$
\textcolor{#f59e0b}{E_{R_\alpha} = E_R\cos^2\alpha}
$$
