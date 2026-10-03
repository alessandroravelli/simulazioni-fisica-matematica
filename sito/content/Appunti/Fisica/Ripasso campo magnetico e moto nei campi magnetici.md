---
title: Ripasso campo magnetico e moto nei campi magnetici
description: Magneti, proprietà di B, forza su un filo, Biot-Savart, spira e solenoide, forza tra due fili, Gauss e circuitazione per B, forza di Lorentz, moto circolare, selettore di velocità.
tags:
  - fisica
  - elettromagnetismo
  - 5SCI
---
## Magneti e campo magnetico B

Sono oggetti dotati di 2 poli: **Nord** e **Sud**. Emettono un campo magnetico e i poli **non possono essere divisi**: se li taglio ottengo 2 magneti uguali, ciascuno con il suo N e il suo S.

![Un magnete tagliato a metà diventa due magneti, ognuno con polo nord e polo sud](magnete-taglio.svg)

### Proprietà di B

| Similitudini con $\vec E$                                                                       | Differenze con $\vec E$                                                     |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Poli uguali si respingono, poli diversi si attraggono                                           | Non esiste la carica singola come per $\vec E$, ma ci sono sempre coppie NS |
| Il campo esce da N (come dalle cariche $+$ per $\vec E$) ed entra in S (come nelle cariche $-$) | Non ci possono essere linee di campo aperte come per $\vec E$               |
| Una carica $q>0$ segue $\vec E$; un magnete si allinea al $\vec B$ esterno (bussola)            | $\vec E$ è generato da cariche ferme, $\vec B$ da cariche in moto           |
| Si rappresenta con linee di campo                                                               |                                                                             |

## Forza magnetica su un filo

Un filo percorso da corrente immerso in un campo magnetico subisce una forza:

$$
\vec F = i\,\vec\ell \times \vec B
$$

- $\vec\ell$: lunghezza del filo (vettoriale)
- $i$: corrente elettrica
- $\vec B$: campo magnetico

<span style="color:#f59e0b">Con la regola della mano destra capisco il verso di $\vec F$.</span>

Questa formula è importante perché è il primo modo con il quale possiamo calcolare il campo magnetico. La corrente e la forza sappiamo misurarle in generale e usando la formula inversa riusciamo a capire quanto è intenso il campo magnetico.

$$
\text{Se } \theta = \frac{\pi}{2}: \quad F = i\ell B \sin\frac{\pi}{2} \quad\longrightarrow\quad B = \frac{F}{i\ell} \qquad [B] = \frac{\text{N}}{\text{A}\cdot\text{m}} = \text{T}
$$

## Campo magnetico generato da un filo percorso da corrente

Abbiamo accennato prima che il campo magnetico viene generato da cariche in movimento. Un esempio di carica in movimento è la corrente che scorre dentro un filo. Un filo percorso da corrente fa sì che un magnete esterno si allinei con il campo magnetico generato dal filo.

Il campo magnetico avvolge il filo ed è tangente in ogni punto alle circonferenze che avvolgono il filo. Il verso in cui ruota il campo magnetico attorno al filo si ottiene sempre con la mano destra, con il pollice in direzione della corrente e il campo magnetico che ruota nella direzione in cui la mano si chiude.

![Filo verticale percorso da corrente i: il campo B è tangente alle circonferenze attorno al filo](filo-campo.svg)

$$
\textcolor{#f59e0b}{\text{Legge di Biot-Savart:}} \quad B = \frac{\mu_0}{2\pi}\,\frac{i}{d}
$$

dove $\mu_0$ è la permeabilità magnetica del vuoto: $\mu_0 = 4\pi \cdot 10^{-7}\ \frac{\text{T}\cdot\text{m}}{\text{A}}$.

Se sono in un mezzo uso $\mu = \mu_r\,\mu_0$, dove $\mu_r$ è la costante relativa (adimensionale).

<span style="color:#f59e0b">Ricordiamo che $\vec B$ è un vettore e diversi $\vec B$ in un punto si sommano come si sommano i vettori.</span>

In generale Biot-Savart è:

$$
\Delta\vec B = \frac{\mu_0\, i}{4\pi}\,\frac{\Delta\vec\ell \times \vec r}{r^3}
$$

## Campo magnetico di una spira

Una spira semplicemente è un filo di forma circolare percorso da corrente, e di conseguenza genera un campo magnetico. Usando la regola della mano destra vediamo che il campo magnetico in ogni punto sull'asse della spira è diretto esattamente nella stessa direzione dell'asse.

![Spira di raggio R e campo B in un punto dell'asse a distanza r](spira-campo.svg)

$$
\text{Sull'asse:} \quad B = \frac{\mu_0\, i\, R^2}{2\left(R^2 + r^2\right)^{3/2}} \qquad \text{Se } r = 0 \;\longrightarrow\; B = \frac{\mu_0\, i}{2R}
$$

## Campo magnetico di un solenoide

Il solenoide è un oggetto costituito da tante spire di filo conduttore, una collegata alla successiva, in cui l'effetto della singola spira viene cumulato a quello delle altre.

$$
n := \text{passo del solenoide} = \frac{N}{\ell} \qquad N := \text{numero di spire} \qquad \ell := \text{lunghezza del solenoide} \qquad [n] = \frac{1}{\text{m}}
$$

> [!example] Esempio
> $n = 50\ \frac{\text{spire}}{\text{m}}$, solenoide $\ell = 1{,}5\ \text{m}$ $\;\longrightarrow\; N = n \cdot \ell = 75$ spire

$$
\longrightarrow\quad \textcolor{#f59e0b}{\text{Campo magnetico:}} \quad B = \mu_0\, n\, i
$$

Internamente il campo magnetico è costante e uniforme in ogni punto e assume il valore visto nella formula sopra. Esternamente il campo magnetico non sarebbe nullo ma è molto più debole. Se il solenoide che consideriamo è molto più lungo di quanto sia largo possiamo considerare il campo esterno nullo.

![Linee del campo magnetico di un solenoide: fitte e parallele dentro, rade fuori](solenoide-campo.svg)

## Forza tra due fili

Abbiamo visto che un filo percorso da corrente genera un campo magnetico e sappiamo allo stesso momento che un filo percorso da corrente all'interno di un campo magnetico subisce una forza: questo ci permette di dimostrare che due fili percorsi da corrente possono attrarsi o respingersi.

Il filo 1, percorso da corrente, genera $\vec B$; il filo 2 subisce il $\vec B$ del filo 1 e sente $\vec F$.

![Due fili paralleli con correnti concordi: il campo del filo 1 attrae il filo 2](due-fili.svg)

$$
B = \frac{\mu_0}{2\pi}\,\frac{i_1}{d} \quad \text{generato dal filo 1}
$$

$$
\vec F = i_2\,\vec\ell \times \vec B \quad\longrightarrow\quad F = i_2\,\ell\,\frac{\mu_0}{2\pi}\,\frac{i_1}{d} = \frac{\mu_0}{2\pi}\,\frac{i_1\, i_2}{d}\,\ell
$$

- Se $i_1$ e $i_2$ hanno lo stesso verso: $F$ **attrattiva**
- Se $i_1$ e $i_2$ hanno versi opposti: $F$ **repulsiva**

## Teorema di Gauss per B

Ricordiamo che $\Phi_\Sigma(\vec E) \propto Q_{tot}$.

$\longrightarrow$ <span style="color:#f59e0b">Il campo magnetico ha $Q_{tot} = 0$ sempre! Non esiste carica magnetica singola (coppie NS).</span>

$$
\longrightarrow\quad \Phi_\Sigma(\vec B) = 0
$$

## Circuitazione di B

La circuitazione è la quantità fisica che tiene conto del valore di una grandezza lungo un percorso e ne somma tutti i contributi.

$$
\Gamma_{\mathcal L}(\vec B) = \sum_{i=1}^{n} \vec B_i \cdot \Delta\vec\ell_i = \sum_{i=1}^{n} B_i\,\Delta\ell_i \cos\theta_i \qquad \text{(prodotto scalare)}
$$

![A sinistra la circuitazione lungo una linea chiusa in un campo uniforme; a destra una linea che abbraccia un filo e una che non lo abbraccia](circuitazione.svg)

Quello che scopriamo è che $\Gamma$ è non nulla solo se $\mathcal L$ è attraversata da una corrente: per una linea $\mathcal L_1$ concatenata con la corrente $\Gamma_{\mathcal L_1} = \mu_0\, i_{\mathcal L}$, per una linea $\mathcal L_2$ che non la abbraccia $\Gamma_{\mathcal L_2} = 0$.

<span style="color:#f59e0b">Solo le correnti concatenate contribuiscono a $\Gamma$.</span>

## Moto in campi elettrici e magnetici

Ricordiamo che un filo percorso da corrente immerso in un $\vec B$ sente $\vec F = i\,\vec\ell \times \vec B$. La corrente $i$ è generata da cariche che si muovono, le cariche hanno velocità $\vec v$:

$$
\Longrightarrow\quad \vec F = q\,\vec v \times \vec B \quad := \textcolor{#f59e0b}{\text{forza di Lorentz}}
$$

$$
\vec F \perp \vec v \text{ sempre} \quad\Longrightarrow\quad W = \vec F \cdot \vec s = F\,s\cos\frac{\pi}{2} = 0
$$

<span style="color:#f59e0b">La forza di Lorentz non genera lavoro.</span>

> [!info] Collegamenti
> Le correnti indotte da un magnete in movimento, conseguenza di queste forze sulle cariche, si vedono nella simulazione [[Induzione elettromagnetica]].

### Moto circolare

Una carica $q$ di massa $m$ entra con velocità $\vec v$ perpendicolare a un campo $\vec B$ uscente. Se $F_L = F_{centr}$ $\Rightarrow$ moto circolare:

![Carica in moto in un campo B uscente: la forza di Lorentz la fa girare su una circonferenza di raggio R](moto-circolare.svg)

$$
\begin{cases}
F_L = q v B \sin\frac{\pi}{2} \\[2pt]
F_{centr} = m\,\dfrac{v^2}{R}
\end{cases}
\qquad
m\frac{v^{\cancel{2}}}{R} = q\cancel{v}B \quad\longrightarrow\quad R = \frac{m v}{q B} \quad \text{raggio della circonferenza che percorre la carica}
$$

### Selettore di velocità

Considero un'area in cui sono presenti sia campo elettrico che campo magnetico, orientati correttamente. Questi generano due forze su una particella carica che si annullano a vicenda, facendo sì che la particella percorra un percorso rettilineo. Le uniche particelle che soddisfano questa condizione però sono quelle che hanno una velocità ben definita e fissata.

![Selettore di velocità: tra due piastre cariche, forza elettrica e forza di Lorentz su una carica negativa si bilanciano](selettore-velocita.svg)

$$
\vec F_e = -q\,\vec E \qquad \vec F_L = -q\,\vec v \times \vec B
$$

$$
F_e = F_L \;\longrightarrow\; \text{particella indisturbata} \quad\Longrightarrow\quad \cancel{q}E = \cancel{q}vB \;\longrightarrow\; v = \frac{E}{B}
$$

Tra tutte le particelle che entrano nel selettore di velocità solo e solamente quelle che hanno una velocità pari al rapporto tra campo elettrico e campo magnetico che abbiamo generato noi passeranno indisturbate, tutte le altre invece verranno deflesse.

> [!info] Collegamenti
> Il discorso prosegue con l'induzione elettromagnetica e le equazioni di Maxwell: [[Elettromagnetismo e Maxwell]].
