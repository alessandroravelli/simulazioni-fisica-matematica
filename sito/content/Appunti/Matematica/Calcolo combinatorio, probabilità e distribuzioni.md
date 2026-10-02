---
title: Calcolo combinatorio, probabilità e distribuzioni
description: Disposizioni, permutazioni e combinazioni; probabilità, probabilità condizionata, teorema di disintegrazione e formula di Bayes; distribuzioni di probabilità, media, varianza, binomiale, Poisson e normale.
tags:
  - matematica
  - probabilità
  - statistica
  - 5SCI
---
## Calcolo combinatorio

È una parte della matematica che si preoccupa di descrivere come è possibile ordinare e raggruppare gli elementi di un insieme.

Risponde alle domande:

1. Quante sono le possibili combinazioni del lotto?
2. Quante sono le targhe automobilistiche possibili?
3. Quante possibili confezioni di 10 caramelle posso preparare con tre gusti di caramelle diversi?
4. …

### Principio fondamentale del calcolo combinatorio

Se un oggetto è individuato da $n$ scelte in cui abbiamo $k_i$ possibilità per ogni scelta il numero totale di possibilità è:

$$
k_1 \cdot k_2 \cdot \ldots \cdot k_n
$$

#### Targhe

$$
\underbrace{\textcolor{#f59e0b}{A}}_{22}\,\underbrace{\textcolor{#f59e0b}{A}}_{22}\;\underbrace{\textcolor{#ef4444}{0}}_{10}\,\underbrace{\textcolor{#ef4444}{0}}_{10}\,\underbrace{\textcolor{#ef4444}{0}}_{10}\;\underbrace{\textcolor{#f59e0b}{A}}_{22}\,\underbrace{\textcolor{#f59e0b}{A}}_{22}
$$

- $\textcolor{#f59e0b}{22}$ possibili lettere (no I, O, U, Q)
- $\textcolor{#ef4444}{10}$ possibili numeri (0, 1, …, 9)

$$
22 \cdot 22 \cdot 10 \cdot 10 \cdot 10 \cdot 22 \cdot 22 = 234\,256\,000 \text{ possibilità}
$$

Se volessi studiare quante targhe servono per far cambiare solo la lettera a sinistra basta considerare il fatto che uno dei caratteri delle targhe è fissato, ovvero quello di cui voglio contare quanti mi servono per farlo cambiare e poi basta contare il numero di possibili targhe con tutti gli altri caratteri che possono cambiare.

$$
\textcolor{#ef4444}{\boxed{A}}A\,000\,AA \longrightarrow \textcolor{#ef4444}{\boxed{B}}A\,000\,AA
$$

<span style="color:#ef4444">il cambio A → B è fissato, tutti gli altri cambiano</span>

$$
1 \cdot 22 \cdot 10^3 \cdot 22^2 = 10\,648\,000 \text{ auto}
$$

### Disposizioni

Ho $n$ oggetti e voglio prenderne $k$ ($n \ge k$) e mi interessa l'ordine con cui li prendo: quante possibilità ho?

> [!example] Esempio
> Ho 3 oggetti e ne voglio prendere 2.
>
> $$A\ B\ C \longrightarrow \begin{matrix} AB & AC & BC \\ BA & CA & CB \end{matrix} \qquad 6 \text{ possibilità}$$

**Come lo ricavo?**
Ho 3 oggetti e ne devo prendere 2: prendo il primo e posso scegliere uno tra tutti e 3, prendo il secondo e posso scegliere uno tra quelli che rimangono ovvero $3 - 1 = 2$.

$$
\longrightarrow\quad 3 \cdot 2 = 6
$$

$$
\textcolor{#f59e0b}{\text{Disposizione:}} \quad D_{n,k} = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot (n-k+1)
$$

### Permutazioni

Consideriamo il caso in cui stiamo studiando delle disposizioni in cui decidiamo di disporre tutti gli oggetti possibili.

Questo caso rappresenta la condizione in cui semplicemente ci chiediamo in quanti modi diversi possiamo ordinare tutti gli oggetti di un insieme. Quest'operazione è definita come permutazione dove semplicemente in un insieme si scambiano di posizione i suoi elementi.

$$
P_n = D_{n,n} = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot \underbrace{(n-n+1)}_{1} = n!
$$

$$
\textcolor{#f59e0b}{\text{Fattoriale}} \qquad n! = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 1
$$

$$
3! = 3 \cdot 2 \cdot 1 = 6
$$

> [!example] Esempio
> Un mazzo di 52 carte ha $P_{52} = 52! \approx 8 \cdot 10^{67}$ diverse permutazioni.

### Disposizioni con ripetizione

Ho $n$ oggetti da disporre in $k$ posti ma ogni volta posso ripescare l'oggetto: ho 10 oggetti (numeri $0 \to 9$) e ne devo posizionare in 4 posizioni. Scelgo il primo e ho 10 possibilità, rimetto l'oggetto nell'insieme, scelgo il secondo e ho 10 possibilità…

$$
10 \cdot 10 \cdot 10 \cdot 10 = 10^4
$$

> [!example] Esempio: lucchetto a combinazione
> 10 cifre, 4 posizioni $\longrightarrow 10^4$

$$
D^*_{n,k} = n^k
$$

### Permutazioni con ripetizione

Se gli $n$ oggetti non sono tutti diversi tra loro, ad esempio nella parola **CASSA**, ci sono delle permutazioni in $n!$ che sono uguali tra loro:

$$
C A_1 S_1 S_2 A_2 = C A_2 S_1 S_2 A_1 = C A_1 S_2 S_1 A_2 = \ldots
$$

Dati $n$ oggetti diversi e un gruppo $k$ il cui primo elemento è ripetuto $a_1$ volte, il secondo ripetuto $a_2$ volte… $\longrightarrow a_1 + a_2 + \ldots + a_k = n$

Le permutazioni possibili sono:

$$
\frac{n!}{a_1!\, a_2!\, \ldots\, a_k!}
$$

### Combinazioni semplici

Sono simili alle disposizioni in cui ho un insieme di $n$ elementi in cui ne prendo solo $k$ ma in questo caso **non mi interessa l'ordine**.

Per capire come calcolare le combinazioni è sufficiente calcolare la disposizione associata e poi dividere per tutte le permutazioni possibili degli elementi che ho preso dal momento che siccome non mi interessa l'ordine tutte queste permutazioni sono identiche.

$$
C_{n,k} = \frac{D_{n,k}}{k!} = \binom{n}{k} = \frac{n!}{k!\,(n-k)!}
$$

### Combinazioni con ripetizione

Considero il caso in cui ho $n$ oggetti e voglio creare dei gruppi di $k$ elementi, di questi gruppi non mi interessa l'ordine e posso anche ripetere la tipologia di elementi.

Un esempio può essere chiedersi quanti possibili sacchetti di 10 caramelle si possono fare se si hanno a disposizione caramelle di tre gusti: mela, limone, fragola.

$$
\star\star\star\;\textcolor{#f59e0b}{\Big|}\;\star\star\;\textcolor{#f59e0b}{\Big|}\;\star\star\star\star\star \qquad (\overset{M}{3}, \overset{L}{2}, \overset{F}{5})
$$

$$
\textcolor{#f59e0b}{\Big|}\;\star\star\star\star\;\textcolor{#f59e0b}{\Big|}\;\star\star\star\star\star\star \qquad (0, 4, 6)
$$

In queste possibilità ho sempre scelto 10 caramelle in due configurazioni diverse. Le sbarrette sono aggiunte per separare la tipologia di caramelle e sono fondamentali per capire che le combinazioni con ripetizione non sono altro che delle permutazioni con ripetizioni di tutti gli oggetti più le sbarrette per separarli.

$$
10 \text{ oggetti (caramelle)} + 2 \text{ separatori} = 12!
$$

Dal momento che nelle configurazioni le caramelle sono tutte uguali, ma cambiano il gusto in base alla posizione rispetto ai separatori avremo una permutazione con ripetizione dove ripetiamo 10 volte le caramelle e due volte i separatori.

$$
\frac{12!}{10!\; 2!} = \binom{12}{10}
$$

$$
C^*_{n,k} = \binom{\textcolor{#f59e0b}{n + k - 1}}{\textcolor{#ef4444}{k}}
$$

- $\textcolor{#f59e0b}{n + k - 1}$: tra quanti oggetti posso scegliere
- $\textcolor{#ef4444}{k}$: quanti elementi prendo

## Probabilità

Il verificarsi di un evento è descritto dalla probabilità dell'evento $E$ come il rapporto tra tutti i casi favorevoli $k$ che soddisfano $E$ fratto tutti i casi possibili.

$$
p(E) = \frac{k}{n} \quad\longrightarrow\quad 0 \le p(E) \le 1 \qquad
\begin{cases}
p(E) = 0 & \text{evento impossibile} \\
p(E) = 1 & \text{evento certo}
\end{cases}
$$

Lo studio del calcolo combinatorio ci viene in aiuto molto spesso, quando dobbiamo andare a capire qual è il numero di casi favorevoli e soprattutto qual è il numero di casi possibili.

### Operazioni tra eventi

È possibile che nel calcolo della probabilità di un evento ci venga richiesto di studiare quale sia la probabilità che succeda un evento A o la probabilità che succeda un evento B.

> [!example] Esempio: pescare una carta di fiori o di quadri
> $$p(\text{fiori}) = \frac{13}{52} = \frac{1}{4} \qquad p(\text{quadri}) = \frac{13}{52} = \frac{1}{4}$$
>
> $$p(\text{tot}) = \frac{1}{4} + \frac{1}{4}$$
>
> Questo caso funziona perché non c'è intersezione tra i due eventi. Questo significa che non c'è nessun elemento che sia contemporaneamente una carta di fiori e una carta di quadri.

> [!example] Esempio: pescare una carta rossa o pescare una figura
> $$p(\text{rosso}) = \frac{26}{52} = \frac{1}{2} \qquad p(\text{figura}) = \frac{12}{52}$$
>
> C'è intersezione perché ci sono 6 figure rosse $\longrightarrow$ l'intersezione tra i 2 è $\frac{6}{52}$.
>
> $$\begin{aligned} p(\text{tot}) &= p(\text{rosso}) + p(\text{figura}) - p(\text{intersezione}) \\ &= \frac{1}{2} + \frac{12}{52} - \frac{6}{52} = \frac{13}{26} + \frac{6}{26} - \frac{3}{26} = \frac{16}{26} = \frac{8}{13} \end{aligned}$$

$$
\longrightarrow\quad \textcolor{#f59e0b}{p(A \cup B) = p(A) + p(B) - p(A \cap B)}
$$

#### Evento contrario

Se $p(A)$ è la probabilità che A succeda allora $1 - p(A) = p(\overline{A})$ è la probabilità che non succeda.

## Probabilità composta e condizionata

Quello che ci chiediamo adesso è come si fa a studiare la probabilità di un evento chiedendo anche che ne succeda oppure che ne sia successo un altro.

### Probabilità condizionata

Se so che B è successo e voglio studiare la probabilità che succeda A:

$$
p(A \mid B) = \frac{\text{numero di elementi di } A \cap B}{\text{numero di elementi di } B}
$$

Formalmente significa che quando B succede tra tutte le possibilità che avevamo all'inizio ora abbiamo a disposizione soltanto più quelli che soddisfano B perché abbiamo richiesto che l'evento B sia già successo. A questo punto, se vogliamo studiare qual è la probabilità che succeda l'evento A ci dobbiamo chiedere quanti siano gli elementi che verificano l'evento A e che stiano anche dentro quelli che verificano B. La probabilità quindi si studia come il numero di eventi che verificano sia A che B fratto tutti gli elementi possibili, che in questo caso sono ristretti a solo quelli di B.

$$
\longrightarrow\quad p(A \mid B) = \frac{p(A \cap B)}{p(B)}
$$

Se voglio che succedano sia A che B è sufficiente calcolare $p(A \cap B)$ direttamente dalla definizione di probabilità oppure, se conosco $p(A \mid B)$:

$$
\longrightarrow\quad p(A \cap B) = p(A \mid B)\, p(B)
$$

> [!example] Esempio
> - Probabilità di pescare l'asso di cuori: $p(\text{asso}) = \frac{1}{52} \approx 1{,}9\%$
> - Probabilità di A♥ se ho pescato una carta rossa:
>   $$p(\text{asso} \mid \text{rosso}) = \frac{p(\text{asso} \cap \text{rosso})}{p(\text{rosso})} = \frac{2/52}{26/52} = \frac{2}{26} = \frac{1}{13} \approx 7{,}7\%$$
> - Probabilità di pescare rosso se ho pescato un asso:
>   $$p(\text{rosso} \mid \text{asso}) = \frac{p(\text{rosso} \cap \text{asso})}{p(\text{asso})} = \frac{2/52}{4/52} = \frac{2}{4} = 50\%$$

### Proprietà della probabilità condizionata

$A$, $B$, $H$ 3 eventi con $p(A),\ p(H),\ p(B) \neq 0$:

$$
p(\overline{A} \mid H) = 1 - p(A \mid H)
$$

$$
p(A \cup B \mid H) = p(A \mid H) + p(B \mid H) - p(A \cap B \mid H)
$$

### Eventi indipendenti

Due eventi si dicono indipendenti se l'accadere di uno non influisce sull'accadere dell'altro.

Per definizione di 2 eventi indipendenti:

$$
p(A \mid B) = p(A) \qquad p(B \mid A) = p(B)
$$

Siccome:

$$
p(A \mid B) = \frac{p(A \cap B)}{p(B)} \quad\longrightarrow\quad p(A) = \frac{p(A \cap B)}{p(B)} \quad\longrightarrow\quad \textcolor{#f59e0b}{p(A \cap B) = p(A) \cdot p(B)}
$$

Se due eventi sono indipendenti, allora la probabilità che succedano entrambi contemporaneamente è semplicemente data dal prodotto tra le loro singole probabilità. Questa formula viene spesso utilizzata per verificare se effettivamente due eventi sono o meno indipendenti: è sufficiente calcolare le singole probabilità dell'evento A e dell'evento B e vedere se il loro prodotto è uguale alla probabilità dell'intersezione.

> [!example] Esempio: lancio 2 dadi diversi, probabilità che esca 5 e 2
> $$p(5) = \frac{1}{6} \qquad p(2) = \frac{1}{6}$$
>
> Come calcolo tutte le possibilità di 2 dadi?
> - Mi interessa l'ordine? Sì, perché i dadi sono diversi.
> - Ripetizioni? Sì, posso avere lo stesso numero.
>
> $$D^*_{6,2} = 6^2 = 36$$
>
> $$\left.\begin{aligned} p(A \cap B) &= \frac{1}{36} \\ p(A) \cdot p(B) &= \frac{1}{6} \cdot \frac{1}{6} \end{aligned}\right\} \quad \frac{1}{36} = \frac{1}{36}$$
>
> Gli eventi sono indipendenti.

## Teorema di disintegrazione

![Spazio campionario diviso nella partizione H1, H2, H3, H4 e l'evento A che la attraversa](probabilita-disintegrazione.svg)

Consideriamo lo spazio in cui conteniamo tutti gli eventi di uno spazio campionario. Per esempio quando prendiamo i numeri che possono essere estratti da un dado a 6 facce possiamo creare delle partizioni dello spazio: $H_1, H_2, \ldots, H_N$.

La partizione deve essere tale per cui la somma di tutti i sottoinsiemi restituisce proprio lo spazio campionario. Vediamo qualche esempio.

$$
\Omega = \{1, 2, 3, 4, 5, 6\}
$$

| Partizione        |                   |                                         |
| ----------------- | ----------------- | --------------------------------------- |
| $H_1 = 2, 4, 6$   | numeri pari       |                                         |
| $H_2 = 1, 3$      | divisori di 3     | <span style="color:#22c55e">va bene</span> |
| $H_3 = 5$         | numero 5          |                                         |

$$
H_1 \cup H_2 \cup H_3 = \Omega
$$

| Partizione        |                   |
| ----------------- | ----------------- |
| $H_1 = 2, 4, 6$   | numeri pari       |
| $H_2 = 3, 6$      | multipli di 3     |
| $H_3 = 1, 5$      | divisori di 5     |

$$
H_1 \cup H_2 \cup H_3 = 2, 4, \textcolor{#ef4444}{\text{\textcircled{6}}}, 3, \textcolor{#ef4444}{\text{\textcircled{6}}}, 1, 5
$$

In questo caso se unisco tutto prendo due volte il numero sei quindi non va bene.

Le partizioni di un insieme possono essere definite in tantissimi modi diversi. L'importante però è che si verifichi sempre che l'unione di tutti gli elementi della partizione restituisca proprio l'insieme iniziale.

**Teorema di disintegrazione**

$$
\longrightarrow\quad p(A) = p(A \mid H_1) \cdot p(H_1) + p(A \mid H_2) \cdot p(H_2) + \ldots
$$

> [!example] Esempio (dal libro di testo): applicazione del teorema di disintegrazione
> Un esperto di cavalli stima che il purosangue Furia vinca con probabilità 10% se il tempo è asciutto e 25% se piove; le previsioni danno tempo asciutto con probabilità 30%. Qual è la probabilità che Furia vinca?
>
> Chiamiamo $A$ l'evento "il giorno della gara è asciutto" (quindi $\overline{A}$ = "piove") e $V$ l'evento "Furia vince":
>
> $$p(V \mid A) = 0{,}1 \qquad p(V \mid \overline{A}) = 0{,}25 \qquad p(A) = 0{,}3$$
>
> $A$ e $\overline{A}$ formano una partizione (uno è il complementare dell'altro), quindi:
>
> $$\begin{aligned} p(V) &= p(V \mid A)\, p(A) + p(V \mid \overline{A})\, p(\overline{A}) \\ &= 0{,}1 \cdot 0{,}3 + 0{,}25 \cdot (1 - 0{,}3) = 0{,}205 = 20{,}5\% \end{aligned}$$

## Formula di Bayes

$$
\textcolor{#f59e0b}{p(B \mid A) = \frac{p(A \mid B)\, p(B)}{p(A)}}
$$

Molto spesso $p(A)$ si calcola con la disintegrazione.

> [!example] Esempio (dal libro di testo): controllo qualità
> Una fabbrica ha due linee di produzione di sacchetti di carta: la prima produce 500 pezzi al giorno, di cui in media il 2% difettosi; la seconda 300 pezzi al giorno, di cui in media l'1% difettosi. Si controlla un sacchetto a caso e risulta difettoso: qual è la probabilità che venga dalla prima linea?
>
> Eventi: $L_1$ = "viene dalla linea 1", $L_2$ = "viene dalla linea 2", $D$ = "è difettoso".
>
> $$p(L_1) = \frac{500}{800} = \frac{5}{8} \qquad p(L_2) = \frac{300}{800} = \frac{3}{8} \qquad p(D \mid L_1) = 0{,}02 \qquad p(D \mid L_2) = 0{,}01$$
>
> Per la formula di Bayes $p(L_1 \mid D) = \dfrac{p(D \mid L_1)\, p(L_1)}{p(D)}$; manca $p(D)$, che si trova con la disintegrazione:
>
> $$p(D) = p(D \mid L_1)\, p(L_1) + p(D \mid L_2)\, p(L_2) = 0{,}02 \cdot \frac{5}{8} + 0{,}01 \cdot \frac{3}{8} = \frac{13}{800}$$
>
> $$p(L_1 \mid D) = \frac{0{,}02 \cdot \frac{5}{8}}{\frac{13}{800}} = \frac{10}{13}$$

## Distribuzioni di probabilità

Le distribuzioni di probabilità sono degli oggetti matematici che ci restituiscono la probabilità che un evento accada in funzione dell'evento stesso. Nel caso più semplice, prendiamo per esempio il lancio di due monete.

**Vogliamo la probabilità di "testa"**

$$
TT \qquad TC \qquad CT \qquad CC
$$

| $x$     | casi        | probabilità   |
| ------- | ----------- | ------------- |
| $x = 0$ | CC (no testa) | $\frac{1}{4}$ |
| $x = 1$ | TC, CT      | $\frac{1}{2}$ |
| $x = 2$ | TT          | $\frac{1}{4}$ |

$$
\longrightarrow\quad f(x) =
\begin{cases}
\frac{1}{4} & x = 0 \ \lor\ x = 2 \\[2pt]
\frac{1}{2} & x = 1 \\[2pt]
0 & \forall x \in \mathbb{R} - \{0, 1, 2\}
\end{cases}
$$

Quando si ha a che fare con una distribuzione di probabilità è molto utile andare a definire alcuni parametri che ci permettono di capire cosa ci aspettiamo da questa distribuzione di probabilità.

### Media

$$
\mu = E[x] = \sum_{i=1}^{N} x_i\, p_i
$$

La media, come sappiamo bene, ci restituisce un'informazione su un valore rappresentativo della nostra distribuzione dicendoci indicativamente su che valore si colloca.

> [!example] Esempio: media dei voti
> $$7 \quad 7 \quad 8 \quad 6 \quad 9 \quad 8 \quad 8$$
>
> Fino ad ora la media si calcolava così:
>
> $$\frac{7 + 7 + 8 + 6 + 9 + 8 + 8}{7}$$
>
> Calcoliamola come distribuzione:
>
> $$p(7) = \frac{2}{7} \quad \text{(prob. che } x \text{ sia 7 tra tutti i voti)} \qquad p(8) = \frac{3}{7} \qquad p(6) = \frac{1}{7} \qquad p(9) = \frac{1}{7}$$
>
> $$\mu = 7 \cdot \frac{2}{7} + 8 \cdot \frac{3}{7} + 6 \cdot \frac{1}{7} + 9 \cdot \frac{1}{7} = \frac{2 \cdot 7 + 3 \cdot 8 + 6 \cdot 1 + 9 \cdot 1}{7} = \frac{7 + 7 + 8 + 8 + 8 + 6 + 9}{7}$$
>
> Uguale a prima!

La media però non basta per descrivere completamente la nostra distribuzione. Infatti è possibile avere due distribuzioni diverse che abbiano la stessa media e però si comportino in maniera completamente diversa.

![Due bersagli: a sinistra i tiri sono vicini al centro, a destra sono sparsi](probabilita-bersagli.svg)

Entrambi questi bersagli hanno la media della posizione dei tiri esattamente nel centro, il disco giallo (fidatevi oppure fate la media delle posizioni sulle $x$ e poi separatamente fate la media delle posizioni sulle $y$ usando un sistema di coordinate cartesiano, mettendo nel centro lo zero e considerando ogni cambio di colore come una distanza pari a uno). Quello che però si può vedere subito è che nel bersaglio di sinistra le misure sono molto più concentrate vicino al valore medio, ovvero il centro, mentre nel bersaglio di destra le misure sono sparse. Quindi è necessario definire qualcosa che ci dica quanto sono disperse le misure attorno al valore medio.

### Varianza e deviazione standard

Proviamo a vedere se è possibile definire questo parametro sfruttando la distanza che ha ogni valore rispetto alla media:

$$
\begin{aligned}
\sum_{i=1}^{N} \big(x_i - E[x]\big) \cdot p_i &= \sum_{i=1}^{N} x_i\, p_i - \sum_{i=1}^{N} E[x]\, p_i \\
&= E[x] - E[x] \underbrace{\sum_{i=1}^{N} p_i}_{\text{la somma delle prob è sempre } 1} = E[x] - E[x] = 0
\end{aligned}
$$

Con questo metodo non otteniamo nulla di utile, perché sistematicamente otteniamo zero in ogni caso. Vediamolo praticamente con l'esempio di prima.

$$
7 \quad 7 \quad 8 \quad 6 \quad 9 \quad 8 \quad 8
$$

$$
\mu = 7 \cdot \frac{2}{7} + 8 \cdot \frac{3}{7} + 6 \cdot \frac{1}{7} + 9 \cdot \frac{1}{7} = 7{,}5714
$$

$$
\begin{aligned}
&(7 - 7{,}5714) \cdot \tfrac{2}{7} + (8 - 7{,}5714) \cdot \tfrac{3}{7} + (6 - 7{,}5714) \cdot \tfrac{1}{7} + (9 - 7{,}5714) \cdot \tfrac{1}{7} \\
&= -0{,}1636 + 0{,}1837 - 0{,}2245 + 0{,}2041 = -0{,}0003 \approx 0
\end{aligned}
$$

Quello che osserviamo è che nei vari termini le distanze sono pesate con segni positivi e negativi. A noi però interessa in generale quanto sono distanti dalla media e non tanto se si trovano da una parte o dall'altra, quindi possiamo provare a pensare di calcolare il quadrato della distanza in modo tale che sia positivo.

$$
\sum_{i=1}^{N} \big(x_i - E[x]\big)^2 p_i = \sigma^2 = V(x) \quad\longrightarrow\quad \textcolor{#f59e0b}{\text{varianza di } x}
$$

$$
\sigma = \sqrt{\sigma^2} \quad := \quad \textcolor{#f59e0b}{\text{deviazione standard}}
$$

In questo contesto la deviazione standard non è più nulla come succedeva prima, ma è un numero che ci dice indicativamente quanto sono disperse le misure attorno alla media.

### A cosa servono?

Quando facciamo un esperimento e raccogliamo una serie di dati, come per esempio il periodo di un pendolo, la media ci dice qual è il valore più rappresentativo di tutti i dati che abbiamo scelto mentre la deviazione standard ci dà un'indicazione su quanto tutte le nostre misure erano vicine alla media. Chiaramente con una misura molto precisa la deviazione standard sarà molto piccola perché tutte le misure sono molto vicine tra di loro, diversamente con una misura poco precisa la deviazione standard sarà molto grande, pure eventualmente mantenendo lo stesso valor medio.

## Distribuzione binomiale

> [!info] Collegamenti
> Prova la distribuzione binomiale dal vivo nella simulazione [[Distribuzione binomiale]]: un singolo esperimento animato e l'istogramma di molte ripetizioni confrontato con la formula qui sotto.

Quando in un esperimento abbiamo soltanto due possibili esiti, successo e insuccesso, possiamo sfruttare l'esperimento di Bernoulli che ci permette di determinare quante volte abbiamo successo se facciamo un certo numero di prove.

| Probabilità successo   | $0 \le p \le 1$ |
| ---------------------- | --------------- |
| Probabilità insuccesso | $q = 1 - p$     |
| Numero di successi     | $x$             |

Immaginiamo di lanciare una moneta, dove sappiamo che la probabilità di ottenere testa (quello che noi consideriamo il successo) è la metà delle volte. Quello che vogliamo chiederci adesso è qual è la probabilità di ottenere 3 volte testa se lancio la moneta 4 volte.

**Consideriamo una moneta truccata:** $p(T) = 0{,}65 \qquad q = 0{,}35$

![Albero dei 4 lanci: i quattro percorsi con tre teste e una croce danno ciascuno p·p·p·q](probabilita-albero.svg)

L'esito di un lancio della moneta è completamente indipendente dal lancio precedente o dal lancio successivo, quindi vuol dire che ad ogni lancio moltiplichiamo la probabilità che ci interessa per quella precedente e così via. Vediamo che per ottenere tre volte testa su quattro lanci abbiamo più possibilità.

Vediamo che ci sono quattro diversi percorsi che soddisfano la nostra richiesta: siccome vanno bene tutti e quattro possiamo sommarli assieme per ottenere:

$$
4\, p^3 q^1
$$

In generale:

$$
\textcolor{#f59e0b}{p(x = k) = \binom{n}{k} p^k\, q^{n-k}}
$$

<span style="color:#f59e0b">Il coefficiente binomiale c'è perché la scelta di p e q è una combinazione.</span>

$$
p(x = 3) = \binom{4}{3} p^3 q^{4-3} = \frac{4!}{3!\,1!}\, p^3 q = 4\, p^3 q
$$

### Binomiale: media e varianza

$$
E[x] = np \qquad V[x] = npq
$$

> [!example] Esempio (dal libro di testo): test a risposta multipla
> Paolo deve rispondere a 5 quesiti a risposta multipla, ognuno con 4 risposte di cui una sola esatta; il test è superato con almeno 3 risposte corrette. Del tutto impreparato, Paolo risponde a caso.
> a. Qual è la probabilità che superi il test?
> b. Quante risposte esatte può aspettarsi di dare in media?
>
> Ogni risposta è una prova di Bernoulli con $p = \frac{1}{4}$, e i 5 quesiti formano 5 prove: il numero $X$ di risposte esatte è una variabile binomiale con $n = 5$, $p = \frac{1}{4}$.
>
> a. $p(X \ge 3) = p(X = 3) + p(X = 4) + p(X = 5)$ (eventi incompatibili):
>
> $$p(X = 3) = \binom{5}{3}\left(\frac{1}{4}\right)^3\left(\frac{3}{4}\right)^2 = 10 \cdot \frac{1}{64} \cdot \frac{9}{16} = \frac{45}{512} \approx 0{,}088 = 8{,}8\%$$
>
> $$p(X = 4) = \binom{5}{4}\left(\frac{1}{4}\right)^4\left(\frac{3}{4}\right)^1 = 5 \cdot \frac{1}{256} \cdot \frac{3}{4} = \frac{15}{1024} \approx 0{,}015 = 1{,}5\%$$
>
> $$p(X = 5) = \binom{5}{5}\left(\frac{1}{4}\right)^5\left(\frac{3}{4}\right)^0 = \frac{1}{1024} \approx 0{,}001 = 0{,}1\%$$
>
> In tutto circa $8{,}8\% + 1{,}5\% + 0{,}1\% = 10{,}4\%$ (decisamente bassa!).
>
> b. $E(X) = n \cdot p = 5 \cdot \frac{1}{4} = 1{,}25$

## Poisson

> [!info] Collegamenti
> Nella simulazione [[Distribuzione di Poisson]] vedi la binomiale con $p = \lambda/n$ avvicinarsi alla Poisson al crescere di $n$: è proprio il limite calcolato qui sotto.

Formalmente è una distribuzione del tutto identica a quella binomiale, ma funziona in particolare quando il numero di prove è molto grande e la probabilità di successo è molto piccola.

$$
P = \binom{n}{k} p^k q^{n-k} = \binom{n}{k} p^k (1 - p)^{n-k}
$$

$$
\lambda = E[x] = np \quad\longrightarrow\quad p = \frac{\lambda}{n}
$$

$$
P = \binom{n}{k} \cdot \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k}
$$

Se $n \to \infty$, $p \to 0$ per $\lambda$ fissato:

$$
\lim_{n \to +\infty} \frac{n!}{k!\,(n-k)!} \cdot \frac{\lambda^k}{n^k} \left(1 - \frac{\lambda}{n}\right)^{n} \cdot \left(1 - \frac{\lambda}{n}\right)^{-k}
$$

$$
= \lim_{n \to +\infty} \underbrace{\frac{n \cdot (n-1) \cdot \ldots \cdot (n-k+1)}{n^k}}_{\textcolor{#22c55e}{\to\, 1}} \cdot \frac{\lambda^k}{k!} \underbrace{\left(1 - \frac{\lambda}{n}\right)^{n}}_{\textcolor{#22c55e}{e^{-\lambda}}} \cdot \underbrace{\left(1 - \cancel{\frac{\lambda}{n}}\right)^{-k}}_{\textcolor{#22c55e}{\to\, 1}}
$$

$$
= \frac{\lambda^k}{k!}\, e^{-\lambda} \simeq P(x = k)
$$

$$
E[x] = \lambda \qquad V[x] = \lambda
$$

## Distribuzione normale

> [!info] Collegamenti
> Nella simulazione [[Distribuzione normale]] scegli $\mu$, $\sigma$ e un intervallo e vedi l'area sotto la curva, cioè la probabilità, calcolarsi dal vivo.

Diversamente da quello che abbiamo visto per le altre distribuzioni, quella normale è una distribuzione continua. In precedenza ci chiedevamo il numero di successi quando facevamo $n$ tentativi, questo significa che lavoravamo sempre con numeri interi; è possibile però che esistano delle distribuzioni che non si limitano ai numeri interi ma appunto vengono dette continue.

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

$$
E[x] = \mu \qquad V[x] = \sigma^2
$$

Questa distribuzione ha un massimo in $x = \mu$, è simmetrica rispetto a $x = \mu$ e presenta un asintoto orizzontale che è proprio rappresentato dall'asse $x$.

$$
\textcolor{#f59e0b}{\text{forma standard:}} \quad f(x) = \frac{1}{\sqrt{2\pi}}\, e^{-x^2/2} \qquad (\mu = 0,\ \sigma = 1)
$$

$f(x)$ da sola non mi dà la probabilità di trovare $x$, ma l'area sotto $f(x)$ sì $\longrightarrow$ **integrali**. Vedremo che non abbiamo modo di calcolare l'integrale di $f(x)$ esplicitamente.

### Probabilità con f(x) standard

Ci sono delle tabelle che restituiscono la probabilità che $x < z$ e i valori descrivono la funzione $\Phi(x)$.

**Funzione Φ(x):** mi dà l'area da $-\infty$ a $x = z$.

![Curva normale standard con l'area colorata da meno infinito fino a z, che è la probabilità Φ(z)](probabilita-phi.svg)

$$
\text{Area} = \text{Probabilità} = \Phi(x = z)
$$

> [!note]- Tavola di Φ(z) (clicca per aprirla)
> Riga = prima cifra decimale di $z$, colonna = seconda cifra. Esempio: $\Phi(1{,}24)$ è alla riga **1,2**, colonna **0,04**: $0{,}89251$.
>
> | z | 0,00 | 0,01 | 0,02 | 0,03 | 0,04 | 0,05 | 0,06 | 0,07 | 0,08 | 0,09 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | **0,0** | 0,50000 | 0,50399 | 0,50798 | 0,51197 | 0,51595 | 0,51994 | 0,52392 | 0,52790 | 0,53188 | 0,53586 |
> | **0,1** | 0,53983 | 0,54380 | 0,54776 | 0,55172 | 0,55567 | 0,55962 | 0,56356 | 0,56749 | 0,57142 | 0,57535 |
> | **0,2** | 0,57926 | 0,58317 | 0,58706 | 0,59095 | 0,59483 | 0,59871 | 0,60257 | 0,60642 | 0,61026 | 0,61409 |
> | **0,3** | 0,61791 | 0,62172 | 0,62552 | 0,62930 | 0,63307 | 0,63683 | 0,64058 | 0,64431 | 0,64803 | 0,65173 |
> | **0,4** | 0,65542 | 0,65910 | 0,66276 | 0,66640 | 0,67003 | 0,67364 | 0,67724 | 0,68082 | 0,68439 | 0,68793 |
> | **0,5** | 0,69146 | 0,69497 | 0,69847 | 0,70194 | 0,70540 | 0,70884 | 0,71226 | 0,71566 | 0,71904 | 0,72240 |
> | **0,6** | 0,72575 | 0,72907 | 0,73237 | 0,73565 | 0,73891 | 0,74215 | 0,74537 | 0,74857 | 0,75175 | 0,75490 |
> | **0,7** | 0,75804 | 0,76115 | 0,76424 | 0,76730 | 0,77035 | 0,77337 | 0,77637 | 0,77935 | 0,78230 | 0,78524 |
> | **0,8** | 0,78814 | 0,79103 | 0,79389 | 0,79673 | 0,79955 | 0,80234 | 0,80511 | 0,80785 | 0,81057 | 0,81327 |
> | **0,9** | 0,81594 | 0,81859 | 0,82121 | 0,82381 | 0,82639 | 0,82894 | 0,83147 | 0,83398 | 0,83646 | 0,83891 |
> | **1,0** | 0,84134 | 0,84375 | 0,84614 | 0,84849 | 0,85083 | 0,85314 | 0,85543 | 0,85769 | 0,85993 | 0,86214 |
> | **1,1** | 0,86433 | 0,86650 | 0,86864 | 0,87076 | 0,87286 | 0,87493 | 0,87698 | 0,87900 | 0,88100 | 0,88298 |
> | **1,2** | 0,88493 | 0,88686 | 0,88877 | 0,89065 | 0,89251 | 0,89435 | 0,89617 | 0,89796 | 0,89973 | 0,90147 |
> | **1,3** | 0,90320 | 0,90490 | 0,90658 | 0,90824 | 0,90988 | 0,91149 | 0,91309 | 0,91466 | 0,91621 | 0,91774 |
> | **1,4** | 0,91924 | 0,92073 | 0,92220 | 0,92364 | 0,92507 | 0,92647 | 0,92785 | 0,92922 | 0,93056 | 0,93189 |
> | **1,5** | 0,93319 | 0,93448 | 0,93574 | 0,93699 | 0,93822 | 0,93943 | 0,94062 | 0,94179 | 0,94295 | 0,94408 |
> | **1,6** | 0,94520 | 0,94630 | 0,94738 | 0,94845 | 0,94950 | 0,95053 | 0,95154 | 0,95254 | 0,95352 | 0,95449 |
> | **1,7** | 0,95543 | 0,95637 | 0,95728 | 0,95818 | 0,95907 | 0,95994 | 0,96080 | 0,96164 | 0,96246 | 0,96327 |
> | **1,8** | 0,96407 | 0,96485 | 0,96562 | 0,96638 | 0,96712 | 0,96784 | 0,96856 | 0,96926 | 0,96995 | 0,97062 |
> | **1,9** | 0,97128 | 0,97193 | 0,97257 | 0,97320 | 0,97381 | 0,97441 | 0,97500 | 0,97558 | 0,97615 | 0,97670 |
> | **2,0** | 0,97725 | 0,97778 | 0,97831 | 0,97882 | 0,97932 | 0,97982 | 0,98030 | 0,98077 | 0,98124 | 0,98169 |
> | **2,1** | 0,98214 | 0,98257 | 0,98300 | 0,98341 | 0,98382 | 0,98422 | 0,98461 | 0,98500 | 0,98537 | 0,98574 |
> | **2,2** | 0,98610 | 0,98645 | 0,98679 | 0,98713 | 0,98745 | 0,98778 | 0,98809 | 0,98840 | 0,98870 | 0,98899 |
> | **2,3** | 0,98928 | 0,98956 | 0,98983 | 0,99010 | 0,99036 | 0,99061 | 0,99086 | 0,99111 | 0,99134 | 0,99158 |
> | **2,4** | 0,99180 | 0,99202 | 0,99224 | 0,99245 | 0,99266 | 0,99286 | 0,99305 | 0,99324 | 0,99343 | 0,99361 |
> | **2,5** | 0,99379 | 0,99396 | 0,99413 | 0,99430 | 0,99446 | 0,99461 | 0,99477 | 0,99492 | 0,99506 | 0,99520 |
> | **2,6** | 0,99534 | 0,99547 | 0,99560 | 0,99573 | 0,99585 | 0,99598 | 0,99609 | 0,99621 | 0,99632 | 0,99643 |
> | **2,7** | 0,99653 | 0,99664 | 0,99674 | 0,99683 | 0,99693 | 0,99702 | 0,99711 | 0,99720 | 0,99728 | 0,99736 |
> | **2,8** | 0,99744 | 0,99752 | 0,99760 | 0,99767 | 0,99774 | 0,99781 | 0,99788 | 0,99795 | 0,99801 | 0,99807 |
> | **2,9** | 0,99813 | 0,99819 | 0,99825 | 0,99831 | 0,99836 | 0,99841 | 0,99846 | 0,99851 | 0,99856 | 0,99861 |
> | **3,0** | 0,99865 | 0,99869 | 0,99874 | 0,99878 | 0,99882 | 0,99886 | 0,99889 | 0,99893 | 0,99896 | 0,99900 |
> | **3,1** | 0,99903 | 0,99906 | 0,99910 | 0,99913 | 0,99916 | 0,99918 | 0,99921 | 0,99924 | 0,99926 | 0,99929 |
> | **3,2** | 0,99931 | 0,99934 | 0,99936 | 0,99938 | 0,99940 | 0,99942 | 0,99944 | 0,99946 | 0,99948 | 0,99950 |
> | **3,3** | 0,99952 | 0,99953 | 0,99955 | 0,99957 | 0,99958 | 0,99960 | 0,99961 | 0,99962 | 0,99964 | 0,99965 |
> | **3,4** | 0,99966 | 0,99968 | 0,99969 | 0,99970 | 0,99971 | 0,99972 | 0,99973 | 0,99974 | 0,99975 | 0,99976 |
> | **3,5** | 0,99977 | 0,99978 | 0,99978 | 0,99979 | 0,99980 | 0,99981 | 0,99981 | 0,99982 | 0,99983 | 0,99983 |
> | **3,6** | 0,99984 | 0,99985 | 0,99985 | 0,99986 | 0,99986 | 0,99987 | 0,99987 | 0,99988 | 0,99988 | 0,99989 |
> | **3,7** | 0,99989 | 0,99990 | 0,99990 | 0,99990 | 0,99991 | 0,99991 | 0,99992 | 0,99992 | 0,99992 | 0,99992 |
> | **3,8** | 0,99993 | 0,99993 | 0,99993 | 0,99994 | 0,99994 | 0,99994 | 0,99994 | 0,99995 | 0,99995 | 0,99995 |
> | **3,9** | 0,99995 | 0,99995 | 0,99996 | 0,99996 | 0,99996 | 0,99996 | 0,99996 | 0,99996 | 0,99997 | 0,99997 |

> [!example] Esempi di calcolo con la tavola
> | a. | b. | c. |
> | --- | --- | --- |
> | ![p(Z < 1)](probabilita-normale-a.svg) | ![p(0 < Z < 1,5)](probabilita-normale-b.svg) | ![p(Z > 0,75)](probabilita-normale-c.svg) |
> | $p(Z < 1) = \Phi(1) = 0{,}84134$ | $p(0 < Z < 1{,}5) = \Phi(1{,}5) - \Phi(0) = 0{,}93319 - 0{,}5 = 0{,}43319$ | $p(Z > 0{,}75) = 1 - \Phi(0{,}75) = 1 - 0{,}77337 = 0{,}22663$ (complementare) |
> | **d.** | **e.** | **f.** |
> | ![p(Z < −0,75)](probabilita-normale-d.svg) | ![p(Z > −1)](probabilita-normale-e.svg) | ![p(−1,75 < Z < −0,5)](probabilita-normale-f.svg) |
> | $p(Z < -0{,}75) = p(Z > 0{,}75) = 1 - \Phi(0{,}75) = 0{,}22663$ (simmetria) | $p(Z > -1) = p(Z < 1) = \Phi(1) = 0{,}84134$ (simmetria) | $p(-1{,}75 < Z < -0{,}5) = p(0{,}5 < Z < 1{,}75) = \Phi(1{,}75) - \Phi(0{,}5) = 0{,}95994 - 0{,}69146 = 0{,}26848$ (simmetria) |

### Probabilità con f(x) non standard

Se

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(x - \mu)^2 / 2\sigma^2}
$$

posso lo stesso usare $\Phi$, ma non uso più $x$ bensì $\dfrac{x - \mu}{\sigma}$:

$$
\Phi\!\left(\frac{X - \mu}{\sigma}\right) \text{ mi restituisce la probabilità che } x \le X
$$

### Intervalli rilevanti

$\longrightarrow$ intervallo $[\mu - \sigma,\ \mu + \sigma]$:

$$
[-\infty,\ \mu + \sigma] = \Phi\!\left(\frac{\mu + \sigma - \mu}{\sigma}\right) = \Phi(1)
$$

$$
[-\infty,\ \mu - \sigma] = \Phi\!\left(\frac{\mu - \sigma - \mu}{\sigma}\right) = \Phi(-1)
$$

$$
[\mu - \sigma,\ \mu + \sigma] = \Phi(1) - \Phi(-1) = \Phi(1) - \big(1 - \Phi(1)\big) = 2\Phi(1) - 1 = 0{,}68
$$

$\longrightarrow$ intervallo $[\mu - 2\sigma,\ \mu + 2\sigma] = 2\Phi(2) - 1 = 0{,}955$

$\longrightarrow$ intervallo $[\mu - 3\sigma,\ \mu + 3\sigma] = 2\Phi(3) - 1 = 0{,}997$
