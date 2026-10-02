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

![Velocità tangenziale e sua componente lungo l'asse x](onde-velocita.svg)

Velocità tangenziale:

$$
\longrightarrow\quad v = \omega r
$$

Velocità sull'asse $x$:

$$
v = -\omega r\sin\varphi = -\omega r\sin(\omega t + \varphi_0)
$$

$x$ è descritto da cos e $v$ da sin $\;\longrightarrow\;$ sono sfasati di $\frac{\pi}{2}$!

### Accelerazione

![Accelerazione centripeta e sua componente lungo l'asse x](onde-accelerazione.svg)

Accelerazione centripeta:

$$
\longrightarrow\quad a_c = \omega^2 r
$$

Accelerazione sull'asse $x$:

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

Fenomeno periodico + semplice che ha la forma di un sin.

![Onda armonica y = A sin(omega t + phi0) tra -A e A](onde-onda-armonica.svg)

$$
y = A\sin(\omega t + \varphi_0)
$$
