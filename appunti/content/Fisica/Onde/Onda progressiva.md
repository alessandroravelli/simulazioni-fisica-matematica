---
title: Onda progressiva
description: La funzione d'onda y(x,t) di un'onda armonica che si propaga lungo x.
tags:
  - fisica
  - onde
---
Un'onda armonica che si propaga lungo l'asse $x$ con velocità $v$ è descritta da una funzione di **due** variabili, la posizione e il tempo:

$$y(x,t) = A\sin\!\left(\omega\left(t - \frac{x}{v}\right) + \varphi_0\right)$$

Il termine $x/v$ è il **ritardo** con cui l'oscillazione della sorgente (in $x = 0$) arriva alla posizione $x$: ogni punto ripete la stessa storia della sorgente, solo più tardi.

Introducendo il **numero d'onda** $k = \dfrac{\omega}{v} = \dfrac{2\pi}{\lambda}$ la stessa formula si scrive

$$y(x,t) = A\sin(\omega t - kx + \varphi_0)$$

## Due modi di leggerla

- **Fissando la posizione** $x$ e lasciando scorrere il tempo, si ottiene l'oscillazione di un singolo punto del mezzo: un [[Moto armonico|moto armonico]] di periodo $T = 2\pi/\omega$.
- **Fissando il tempo** $t$ e guardando tutte le posizioni, si ottiene una "fotografia" dell'onda: una sinusoide nello spazio di periodo $\lambda$.

Sono le due sezioni della superficie $y(x,t)$ che la simulazione evidenzia, e che legano tra loro le grandezze viste nelle [[Onde meccaniche]].

## Onde in più dimensioni

Una sorgente puntiforme nello spazio genera un'**onda sferica**: la fase dipende dalla distanza $r$ dalla sorgente, e l'ampiezza diminuisce come $1/r$ perché la stessa energia si distribuisce su superfici sempre più grandi.

$$y(r,t) = \frac{A}{r}\sin\!\left(\omega\left(t - \frac{r}{v}\right)\right)$$

La luce è un'onda progressiva di questo tipo, ma elettromagnetica e trasversale: vedi [[Polarizzazione della luce]].

## Simulazione

[Apri la simulazione a schermo intero ↗](https://simulazioni-fisica-matematica.alessandro-ravelli00.workers.dev/esperimenti/fisica/onda-progressiva-3d/)

<iframe src="https://simulazioni-fisica-matematica.alessandro-ravelli00.workers.dev/esperimenti/fisica/onda-progressiva-3d/" width="100%" height="760" style="border: 1px solid var(--lightgray); border-radius: 8px;"></iframe>
