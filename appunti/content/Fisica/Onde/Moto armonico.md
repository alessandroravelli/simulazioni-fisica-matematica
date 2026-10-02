---
title: Moto armonico
description: Il moto armonico semplice come proiezione di un moto circolare uniforme.
tags:
  - fisica
  - oscillazioni
---
Un punto si muove di **moto armonico semplice** quando oscilla avanti e indietro attorno a una posizione di equilibrio con legge sinusoidale. Il modo più intuitivo per vederlo è come **proiezione di un moto circolare uniforme**: un punto ruota con velocità angolare costante $\omega$ su una circonferenza di raggio $A$, e la sua ombra sul diametro orizzontale si muove di moto armonico.

## Legge oraria

$$x(t) = A\cos(\omega t + \varphi_0)$$

- $A$ è l'**ampiezza** (lo spostamento massimo dall'equilibrio);
- $\omega$ è la **pulsazione**, legata al periodo e alla frequenza da $\omega = \dfrac{2\pi}{T} = 2\pi f$;
- $\varphi_0$ è la **fase iniziale**, che dice dove si trova il punto all'istante $t = 0$.

## Velocità e accelerazione

Derivando la posizione rispetto al tempo:

$$v(t) = -A\omega\sin(\omega t + \varphi_0) \qquad a(t) = -A\omega^2\cos(\omega t + \varphi_0) = -\omega^2 x(t)$$

L'ultima uguaglianza è quella che **definisce** il moto armonico: l'accelerazione è sempre proporzionale allo spostamento e diretta verso la posizione di equilibrio. Per questo una massa attaccata a una molla ($F = -kx$) oscilla di moto armonico con $\omega = \sqrt{k/m}$.

> [!tip] Fasi
> La velocità è sfasata di un quarto di periodo rispetto alla posizione (è massima quando il punto passa per l'equilibrio), l'accelerazione è in opposizione di fase (è massima, verso il centro, quando lo spostamento è massimo).

## Collegamenti

Il moto armonico è il mattone delle onde: in un'[[Onde meccaniche|onda meccanica]] armonica ogni punto del mezzo oscilla proprio di moto armonico, e l'[[Onda progressiva|onda progressiva]] si ottiene mettendo in fila tanti oscillatori armonici sfasati tra loro.

## Simulazione

[Apri la simulazione a schermo intero ↗](https://simulazioni-fisica-matematica.alessandro-ravelli00.workers.dev/esperimenti/fisica/moto-armonico/)

<iframe src="https://simulazioni-fisica-matematica.alessandro-ravelli00.workers.dev/esperimenti/fisica/moto-armonico/" width="100%" height="760" style="border: 1px solid var(--lightgray); border-radius: 8px;"></iframe>
