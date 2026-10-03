---
title: Crisi della fisica classica
description: Radiazione termica, corpo nero, legge di Wien, Rayleigh-Jeans e catastrofe ultravioletta, quanti, effetto fotoelettrico, dualismo onda-particella, legge di Planck, effetto Compton.
tags:
  - fisica
  - fisica moderna
  - 5SCI
---
## Corpo a una temperatura T ≠ 0 K

![Particelle della materia che vibrano](particelle-vibranti.svg)

**Temperatura = vibrazione.** La materia è composta da particelle cariche che generano $\vec E$; il loro movimento genera campi variabili, $\vec E$ e $\vec B$ variabili $\Rightarrow$ **onde EM** (vedi [[Elettromagnetismo e Maxwell#Onde elettromagnetiche|onde elettromagnetiche]]).

$$
\longrightarrow\quad \textcolor{#f59e0b}{\text{calore e onde EM sono legati}}
$$

### Radiazione infrarossa

![Spettro elettromagnetico: dai raggi gamma alle onde radio; tra ultravioletto e infrarosso la piccola banda del visibile](spettro-em.svg)

La classica emissione di calore è nell'infrarosso; temperature altissime portano il colore rosso (il visibile confina con l'infrarosso dalla parte del rosso).

Pensiamo ai dischi dei freni delle auto. Quando un'auto frena normalmente, il disco si scalda, e lo possiamo verificare avvicinando una mano al disco e sentendo il calore. Come abbiamo visto, questo calore è strettamente legato alle onde elettromagnetiche generate dall'oscillazione delle particelle. Quando la temperatura aumenta, l'oscillazione delle particelle è più rapida, il che significa che ha una frequenza maggiore: questo aumento di frequenza corrisponde a una temperatura più alta e in particolare genera onde elettromagnetiche anch'esse con frequenza più alta. Se guardiamo lo spettro elettromagnetico, quello che vediamo è che aumentando la frequenza a partire dall'infrarosso troviamo subito dopo la luce visibile. Questo spiega il motivo per cui, nelle auto ad alte prestazioni, frenate ripetute fanno sì che il disco del freno inizi a brillare di rosso.

## Qual è il modello che mi dice come un corpo emette onde EM a una certa T?

L'emissione dipende da $T$, dalla composizione del corpo e dalla sua forma. Ora vogliamo studiare **solo** $T$.

### Corpo nero

Considero un oggetto che sia in grado di assorbire qualunque onda EM e sia poi in grado di emetterla.

![Una cavità con un piccolo foro: le onde che entrano restano intrappolate e vengono assorbite; una volta scaldata, la cavità emette radiazione](corpo-nero-cavita.svg)

- Le onde vengono intrappolate e vengono assorbite $\Rightarrow$ la **temperatura sale**!
- Una volta scaldato, il corpo emette radiazione **non a caso**!

Posso scaldare il corpo come voglio, ma le onde che emetterà non sono casuali!

## Spettro di emissione di corpo nero

Apertura del corpo nero di area $S$:

$$
R(\lambda, T) = \frac{P(T, \lambda)}{S\,\Delta\lambda} \qquad P := \text{potenza} \qquad R := \text{radianza} \qquad [R] = \frac{\text{W}}{\text{m}^3}
$$

Quello che si osserva sperimentalmente sono degli spettri di radianza che si spostano al variare della temperatura del corpo che consideriamo. In maniera empirica si può osservare che la posizione dei massimi delle curve segue il disegno di un'iperbole.

> [!example] Simulazione
> Cambia la temperatura nella simulazione [[Radiazione di corpo nero]] e guarda il massimo scorrere lungo la legge di Wien; puoi anche confrontare la curva vera con quella di Rayleigh-Jeans.

<iframe class="simulazione" src="/esperimenti/fisica/corpo-nero/" title="Radiazione di corpo nero" loading="lazy"></iframe>

### Legge di Wien

Empiricamente si è trovata la relazione

$$
\lambda_{max} = \frac{2{,}9 \cdot 10^{-3}\ \text{m}\cdot\text{K}}{T}
$$

Se $T$ aumenta, $\lambda_{max}$ diminuisce.

### Fine '800: fisica classica + Maxwell

Si ottiene la radianza spiegabile dall'oscillazione delle particelle: **Rayleigh-Jeans**

$$
R^{RJ}(\lambda, T) = \frac{2\pi c\, k_B\, T}{\lambda^4}
$$

La questione veramente importante di questa formula è che dipende inversamente dalla lunghezza d'onda. Se studiamo il limite per la lunghezza d'onda che tende a zero, quello che otteniamo è un asintoto verticale, che però è completamente incompatibile con gli spettri ottenuti sperimentalmente. Infatti questa legge porta a una divergenza di energia quando andiamo a studiare lunghezze d'onda molto piccole. Questa scoperta viene chiamata **catastrofe ultravioletta**.

$$
R^{RJ}(\lambda, T) \propto \frac{1}{\lambda^4} \quad\Longrightarrow\quad \lim_{\lambda \to 0} \frac{1}{\lambda^4} = \infty \quad\longrightarrow\quad \text{incompatibile con le osservazioni}
$$

## Quanti

È proprio in questo momento che nasce il concetto di fisica quantistica. Vedremo adesso che il fisico Max Planck risolse il problema della catastrofe ultravioletta semplicemente supponendo che le onde elettromagnetiche, ovvero la luce, non potessero scambiarsi energia in maniera arbitraria, ma potessero farlo solo in **quanti**. Un quanto si definisce come l'unità indivisibile di una grandezza.

### Luce: onda o particella?

| Onda | Particella (fotone) |
| --- | --- |
| L'intensità dipende dall'ampiezza dell'onda alla seconda: $I \propto A^2$ | L'energia dipende da altre caratteristiche della particella |
| $\rightarrow$ onde del mare | La velocità è fissata, $c = 3 \cdot 10^8\ \text{m/s}$: cos'altro? |

## Effetto fotoelettrico

Consideriamo un'onda EM. Sappiamo che l'irradianza

$$
E_R = \frac{1}{2}\,\varepsilon_0\, c\, E_0^2
$$

dipende dall'(ampiezza)² dell'onda.

![Un'onda elettromagnetica colpisce un metallo e ne fa uscire un elettrone](effetto-fotoelettrico.svg)

Nel 1905 Einstein pubblica un articolo sull'effetto fotoelettrico. Si scopre che un'onda EM che incide su un metallo può scalzare un $e^-$, come se fosse un urto!

<span style="color:#f59e0b">Potremmo pensare che se $E_0 \uparrow$ $\Rightarrow$ $E_R \uparrow$ $\Rightarrow$ la velocità dell'$e^-$ in uscita debba aumentare</span> $\longrightarrow$ <span style="color:#ef4444">**No!**</span>

Einstein scopre solo che se $E_0 \uparrow$ aumenta il numero di $e^-$, ma non la loro velocità.

**Come funziona allora?** Si scopre che cambiando la frequenza $f$ e tenendo fisso $E_R$, il numero di $e^-$ rimane uguale ma la velocità cambia.

$$
\longrightarrow\quad \textcolor{#f59e0b}{\text{l'energia di un fotone dipende da } f!}
$$

L'energia del fotone la scriviamo così:

$$
\textcolor{#f59e0b}{E = h f} \qquad h = 6{,}62 \cdot 10^{-34}\ \text{J}\cdot\text{s} \quad \text{costante di Planck}
$$

<span style="color:#f59e0b">Un'onda EM è formata da tanti fotoni, tutti di energia $E = hf$.</span>

### Consideriamo un caso specifico

Un $e^-$ ha bisogno di energia $W_e$ per essere rimosso: a che frequenza corrisponde?

$$
E = h f_e = W_e \quad\longrightarrow\quad f_e = \frac{W_e}{h}
$$

- Se $f \ge f_e$: **estraggo**
- Se $f < f_e$: **non estraggo**

Considero $f_0 > f_e$:

$$
E = h f_0 = h f + h f_e = \underbrace{h f}_{\text{energia cinetica con cui esce l'}e^-} + W_e
$$

$$
E_k = h f_0 - W_e = h\,(f_0 - f_e) = \frac{1}{2}\, m v^2 \qquad v = \sqrt{\frac{2h}{m}\,(f_0 - f_e)}
$$

### Quindi la luce è onda o particella?

Tutte e due: ecco come si conciliano le 2 visioni. Considero

$$
\frac{\text{numero di fotoni}}{\text{secondi} \cdot \text{m}^2} = \frac{E_R}{hf}
$$

L'irradianza di Maxwell mi dice che un'onda porta $\dfrac{\text{W}}{\text{m}^2} = \dfrac{\text{J/s}}{\text{m}^2} = \dfrac{\text{J}}{\text{s}\,\text{m}^2}$; io so che 1 fotone ha $E = hf$ in J.

$$
\Phi = \frac{E_R}{hf} \qquad \text{se } E_0 \uparrow \Rightarrow E_R \uparrow \Rightarrow \Phi \uparrow
$$

$\Longrightarrow$ se $E_0$ aumenta ho più fotoni, ma non sono più energetici.

- $E_R$ mi dice l'energia dell'onda (tanti fotoni).
- $E = hf$ mi dice l'energia di 1 fotone.

<span style="color:#f59e0b">Tanti fotoni poco energetici e pochi fotoni molto energetici possono dare la stessa $E_R$.</span>

## Torniamo al corpo nero

$E = hf$: come ci mette tutto a posto? Se lo scambio di energia dipende dal passaggio di 1 fotone $hf$, con $f\lambda = c$:

$$
\longrightarrow\quad \textcolor{#f59e0b}{R^{BB}(\lambda, T) = \frac{2\pi c^2}{\lambda^5}\,\frac{h}{e^{hc/k_B T\lambda} - 1}}
$$

Con la sostituzione $\dfrac{hc}{k_B T\lambda} = x$:

$$
\lim_{\lambda \to +\infty} \frac{1}{\lambda^5}\,\frac{1}{e^{hc/k_B T\lambda} - 1} = \left(\frac{k_B T}{hc}\right)^5 \lim_{x \to 0} \frac{x^5}{e^x - 1} = \left(\frac{k_B T}{hc}\right)^5 \lim_{x \to 0} \frac{x^{\cancel{5}\,4}}{\cancel{x}} = 0
$$

$$
\lim_{\lambda \to 0} \frac{1}{\lambda^5}\,\frac{1}{e^{hc/k_B T\lambda} - 1} = \left(\frac{k_B T}{hc}\right)^5 \lim_{x \to \infty} \frac{x^5}{e^x - 1} = 0
$$

<span style="color:#f59e0b">Entrambi i limiti esistono e sono finiti.</span>

Abbiamo risolto il problema che avevamo riscontrato all'inizio con la teoria classica. Adesso la radianza del corpo nero, sia per lunghezze d'onda molto piccole sia per lunghezze d'onda molto grandi, risulta limitata ed è fisicamente accettabile.

## Effetto Compton

I fisici di inizio Novecento ritenevano impossibile che la luce fosse fatta di particelle, sostenendo che fosse solo e solamente un'onda. L'effetto fotoelettrico scoperto da Einstein non convince la comunità scientifica fino a quando, nel 1923, si scoprì l'effetto Compton, che prende il nome dal fisico che lo descrisse per la prima volta.

**Consideriamo raggi X su un bersaglio.**

![A sinistra la teoria classica: il raggio X esce con la stessa lunghezza d'onda; a destra ciò che si osserva: esce anche un elettrone e il raggio deviato di θ ha lunghezza d'onda diversa](compton-schemi.svg)

- **Teoria classica:** il raggio X attraversa il materiale e ne esce eventualmente deviato, con la stessa lunghezza d'onda $\lambda$.
- **Cosa si osserva in realtà?** Compton studia la lunghezza d'onda dei raggi X in uscita a diversi angoli $\theta$. Si vede che oltre ai raggi X con lunghezza d'onda $\lambda$ ci sono anche raggi X con lunghezza d'onda $\lambda'$, tanto più diversa da $\lambda$ quanto più grande è l'angolo. Come mai?

![Schema delle misure di Compton: a 0° un solo picco in λ, ad angoli maggiori compare un secondo picco in λ′ sempre più lontano](compton-picchi.svg)

![Un fotone urta un elettrone: l'elettrone parte con quantità di moto p, il fotone esce deviato di un angolo θ con frequenza minore](effetto-compton.svg)

Consideriamo $\theta = 90^\circ$ $\rightarrow$ se i fotoni sono particelle allora posso creare un **urto elastico**: il fotone cede un po' di energia all'$e^-$ e lo strappa via.

<span style="color:#f59e0b">Se scrivo la conservazione della quantità di moto trovo:</span>

$$
\Delta\lambda = \frac{h}{m_e c}\,(1 - \cos\theta)
$$

Se i fotoni $\lambda'$ sono legati agli $e^-$ emessi, quelli $\lambda$ cosa sono?

$\rightarrow$ Sono fotoni che hanno provato a portare via $e^-$ più legati e non ci sono riusciti, e vengono deviati secondo la teoria classica.

$$
\text{Se } \theta = 90^\circ \quad\longrightarrow\quad \Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c} = 2{,}42 \cdot 10^{-12}\ \text{m}
$$

> [!info] Collegamenti
> Il fotone ha quantità di moto $p = E/c$ anche se non ha massa: lo si ricava dall'energia relativistica in [[Relatività#Dinamica relativistica|Relatività]].
