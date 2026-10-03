---
title: Onde suono e luce
description: Moto armonico (legge oraria, periodo, velocità, accelerazione, energia) e moto ondulatorio.
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


![sovrapposizione-impulsi](sovrapposizione-impulsi.svg)