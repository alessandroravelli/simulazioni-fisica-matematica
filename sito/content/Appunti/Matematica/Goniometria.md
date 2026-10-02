---
title: Goniometria
description: Funzioni goniometriche, relazione fondamentale, radianti, archi associati, grafici, formule di addizione, duplicazione e bisezione, funzioni lineari in seno e coseno.
tags:
  - matematica
  - goniometria
  - 4SCI
---
Le funzioni goniometriche sono fondamentali per poter rappresentare dei comportamenti periodici della realtà che ci circonda e soprattutto hanno infinite applicazioni nella geometria e nello studio dei triangoli.

> [!info] Collegamenti
> Il fenomeno periodico per eccellenza sono le onde: in fisica seno e coseno descrivono il moto armonico, vedi [[Onde suono e luce]].

## Funzioni goniometriche

*Libro di testo, pag. 122*

Consideriamo una circonferenza con raggio pari a 1. Prendiamo ora un punto P che si trova sulla circonferenza. Le funzioni trigonometriche ci permettono di trovare le coordinate di questo punto sapendo solo un angolo.

![Circonferenza goniometrica con il punto P e le sue coordinate x_P e y_P](goniometria-circonferenza.svg)

Sapendo che le coordinate del punto sono $(0{,}8\,;\ 0{,}6)$ so che obbligatoriamente $x = 0{,}8$ e $y = 0{,}6$.

![Triangolo rettangolo con ipotenusa 1 e cateti x_P e y_P](goniometria-triangolo.svg)

Se cambio l'angolo automaticamente cambieranno anche i valori dei due cateti $x$ e $y$ del triangolo. Per conoscere questi valori ci vengono in aiuto le funzioni trigonometriche.

$$
\textcolor{#ef4444}{y_P = 1 \cdot \sin(\alpha)} \qquad \textcolor{#3b82f6}{x_P = 1 \cdot \cos(\alpha)}
$$

### Tangente

In aggiunta a queste funzioni c'è anche la tangente che rappresenta la lunghezza del segmento verde in figura che parte dall'asse $x$ e incontra il prolungamento del raggio passante per P.

![Circonferenza goniometrica con seno, coseno e tangente di alfa](goniometria-tangente.svg)

$$
\textcolor{#22c55e}{\tan(\alpha)} = \frac{\textcolor{#ef4444}{\sin(\alpha)}}{\textcolor{#3b82f6}{\cos(\alpha)}}
$$

## Valori delle funzioni trigonometriche

Le funzioni trigonometriche sin e cos abbiamo visto che rappresentano le coordinate del punto P sulla circonferenza di raggio 1. Siccome i valori massimi di $x$ e $y$ nella circonferenza sono 1 e i minimi sono $-1$ allora anche queste funzioni saranno **limitate** ai valori tra 1 e $-1$.

![Diametri della circonferenza: x e y variano tra -1 e 1](goniometria-limiti.svg)

$$
\textcolor{#f59e0b}{-1 \le y \le 1} \quad\longrightarrow\quad -1 \le \sin(\alpha) \le 1
$$

$$
\textcolor{#22c55e}{-1 \le x \le 1} \quad\longrightarrow\quad -1 \le \cos(\alpha) \le 1
$$

### Valori notevoli

Ci sono alcuni angoli che portano le funzioni trigonometriche a dei valori speciali da ricordare.

| Misura dell'angolo        | Seno                  | Coseno                | Tangente              |
| ------------------------- | --------------------- | --------------------- | --------------------- |
| $0° = 0$                  | $0$                   | $1$                   | $0$                   |
| $30° = \dfrac{\pi}{6}$     | $\dfrac{1}{2}$        | $\dfrac{\sqrt3}{2}$   | $\dfrac{\sqrt3}{3}$   |
| $45° = \dfrac{\pi}{4}$     | $\dfrac{\sqrt2}{2}$   | $\dfrac{\sqrt2}{2}$   | $1$                   |
| $60° = \dfrac{\pi}{3}$     | $\dfrac{\sqrt3}{2}$   | $\dfrac{1}{2}$        | $\sqrt3$              |
| $90° = \dfrac{\pi}{2}$     | $1$                   | $0$                   | non definita          |
| $180° = \pi$              | $0$                   | $-1$                  | $0$                   |
| $270° = \dfrac{3\pi}{2}$   | $-1$                  | $0$                   | non definita          |

![Valori di seno, coseno e tangente per l'angolo di 0 gradi](goniometria-angolo-0.svg) ![Valori di seno, coseno e tangente per l'angolo di 30 gradi](goniometria-angolo-30.svg)

> [!todo] Compito
> Fare il grafico per gli altri angoli.

## Relazione fondamentale della trigonometria

Consideriamo il triangolo con cui abbiamo definito le funzioni sin e cos.

![Triangolo rettangolo con ipotenusa 1 e cateti x_P e y_P](goniometria-triangolo.svg)

$$
\textcolor{#ef4444}{y_P = 1 \cdot \sin(\alpha)} \qquad \textcolor{#3b82f6}{x_P = 1 \cdot \cos(\alpha)}
$$

È un triangolo rettangolo quindi posso applicare il teorema di Pitagora.

$$
1^2 = \textcolor{#3b82f6}{x_P^2} + \textcolor{#ef4444}{y_P^2} \quad\longrightarrow\quad 1^2 = 1^2 \cdot \textcolor{#3b82f6}{\cos^2(\alpha)} + 1^2 \cdot \textcolor{#ef4444}{\sin^2(\alpha)}
$$

$$
\longrightarrow\quad 1 = \cos^2(\alpha) + \sin^2(\alpha)
$$

Questa relazione è valida sempre per ogni angolo. E sono particolarmente importanti le formule inverse che permettono di trovare cos sapendo sin e viceversa.

## Radianti e gradi d'arco

Ci sono due modi importanti con cui si possono rappresentare gli angoli in matematica e fisica. I gradi d'arco (Deg sulla calcolatrice) e i radianti (Rad sulla calcolatrice).

| Gradi d'arco | $0° \longrightarrow 360°$ |
| ------------ | ------------------------- |
| Radianti     | $0 \longrightarrow 2\pi$  |

Come convertire i 2 valori?

$$
\text{RAD} : \pi = \text{DEG} : 180
$$

## Archi associati

Ci sono alcune relazioni tra gli angoli che ci permettono di osservare come sin e cos di angoli diversi abbiano lo stesso valore.

$$
\sin(30°) = \frac{1}{2} \qquad \sin(150°) = \frac{1}{2}
$$

![Angoli alfa, pi meno alfa, pi più alfa e 2pi meno alfa](goniometria-archi-associati.svg)

Posso collegare più angoli usando $\alpha$ e $\pi$ o $2\pi$.

![Angoli supplementari: stesso seno, coseno opposto](goniometria-supplementari.svg)

$$
\sin(\alpha) = \sin(\pi - \alpha) \qquad \cos(\pi - \alpha) = -\cos\alpha
$$

### Angoli che differiscono per un angolo giro

![Angolo 2pi più alfa: stesso seno e coseno di alfa](goniometria-angolo-giro.svg)

$$
\sin(2\pi + \alpha) = \sin\alpha \qquad \cos(2\pi + \alpha) = \cos(\alpha)
$$

$\sin(\alpha)$ e $\cos(\alpha)$ sono funzioni periodiche con periodo $2\pi$.

|                                              | Seno                                        | Coseno                                       | Tangente                                                |
| -------------------------------------------- | ------------------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| **Angoli opposti**                           | $\sin(-\alpha) = -\sin\alpha$               | $\cos(-\alpha) = \cos\alpha$                 | $\tan(-\alpha) = -\tan\alpha$                           |
| **Angoli complementari**                     | $\sin(\frac{\pi}{2} - \alpha) = \cos\alpha$ | $\cos(\frac{\pi}{2} - \alpha) = \sin\alpha$  | $\tan(\frac{\pi}{2} - \alpha) = \frac{1}{\tan\alpha}$   |
| **Angoli supplementari**                     | $\sin(\pi - \alpha) = \sin\alpha$           | $\cos(\pi - \alpha) = -\cos\alpha$           | $\tan(\pi - \alpha) = -\tan\alpha$                      |
| **Angoli che differiscono di un angolo piatto** | $\sin(\pi + \alpha) = -\sin\alpha$       | $\cos(\pi + \alpha) = -\cos\alpha$           | $\tan(\pi + \alpha) = \tan\alpha$                       |
| **Angoli che differiscono per un angolo giro**  | $\sin(2\pi + \alpha) = \sin(\alpha)$     | $\cos(2\pi + \alpha) = \cos(\alpha)$         | $\tan(2\pi + \alpha) = \tan\alpha$                      |

*Lezione del 16/09/2026*

## Grafici delle funzioni

![Grafico di sin(x)](goniometria-grafico-sin.svg)

![Grafico di cos(x)](goniometria-grafico-cos.svg)

![Grafico di tan(x) con asintoti verticali](goniometria-grafico-tan.svg)

## Formule di addizione e sottrazione

Sappiamo calcolare singolarmente il seno e il coseno di angoli singoli utilizzando per esempio i valori notevoli. Ma come calcoliamo il sin o il cos di una somma tra angoli?

$$
\sin(45°) = \frac{\sqrt2}{2} \qquad \sin(30°) = \frac{1}{2}
$$

$$
\sin(75°) = \ ?
$$

$$
\sin(75°) = \sin(45° + 30°) = \ ?
$$

$$
\textcolor{#f59e0b}{\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta}
$$

$$
\textcolor{#f59e0b}{\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta}
$$

$$
\begin{aligned}
\sin(75°) &= \sin(45°)\cos(30°) + \cos(45°)\sin(30°) \\
&= \frac{\sqrt2}{2} \cdot \frac{\sqrt3}{2} + \frac{\sqrt2}{2} \cdot \frac{1}{2} = \frac{\sqrt6}{4} + \frac{\sqrt2}{4} = \frac{1}{4}\left(\sqrt6 + \sqrt2\right)
\end{aligned}
$$

> [!warning] Attenzione
> Quando si lavora con sin e cos non si scrive mai il risultato con la virgola.

$$
\tan(\alpha \pm \beta) = \frac{\sin(\alpha \pm \beta)}{\cos(\alpha \pm \beta)} = \frac{\sin\alpha\cos\beta \pm \cos\alpha\sin\beta}{\cos\alpha\cos\beta \mp \sin\alpha\sin\beta}
$$

$$
= \frac{\dfrac{\sin\alpha\,\cancel{\cos\beta}}{\cos\alpha\,\cancel{\cos\beta}} \pm \dfrac{\cancel{\cos\alpha}\,\sin\beta}{\cancel{\cos\alpha}\,\cos\beta}}{1 \mp \dfrac{\sin\alpha\sin\beta}{\cos\alpha\cos\beta}} = \frac{\tan(\alpha) \pm \tan(\beta)}{1 \mp \tan(\alpha)\tan(\beta)}
$$

## Formule di duplicazione

$$
\sin(2\alpha) = \ ? \qquad \cos(2\alpha) = \ ?
$$

$$
\sin(2\alpha) = \sin(\alpha + \alpha) = \sin\alpha\cos\alpha + \cos\alpha\sin\alpha = 2\sin\alpha\cos\alpha
$$

$$
\longrightarrow\quad \textcolor{#f59e0b}{\sin 2\alpha = 2\sin\alpha\cos\alpha}
$$

$$
\cos(2\alpha) = \cos\alpha\cos\alpha - \sin\alpha\sin\alpha = \cos^2\alpha - \sin^2\alpha
$$

$$
\longrightarrow\quad \textcolor{#f59e0b}{\cos(2\alpha) = \cos^2\alpha - \sin^2\alpha}
$$

$$
\tan(2\alpha) = \frac{2\tan\alpha}{1 - \tan^2\alpha}
$$

*Lezione del 17/09/2026*

## Formule di bisezione

So che

$$
\cos(\alpha) = \cos^2\frac{\alpha}{2} - \sin^2\frac{\alpha}{2} \qquad \text{e} \qquad \cos^2\frac{\alpha}{2} + \sin^2\frac{\alpha}{2} = 1
$$

$$
\longrightarrow\quad \cos(\alpha) = 1 - 2\sin^2\frac{\alpha}{2}
$$

$$
\sin^2\frac{\alpha}{2} = \frac{1 - \cos(\alpha)}{2} \quad\longrightarrow\quad \sin\frac{\alpha}{2} = \pm\sqrt{\frac{1 - \cos(\alpha)}{2}}
$$

$$
\longrightarrow\quad \cos(\alpha) = 2\cos^2\frac{\alpha}{2} - 1
$$

$$
\cos^2\frac{\alpha}{2} = \frac{1 + \cos(\alpha)}{2} \quad\longrightarrow\quad \cos\frac{\alpha}{2} = \pm\sqrt{\frac{1 + \cos(\alpha)}{2}}
$$

$$
\textcolor{#f59e0b}{\sin\frac{\alpha}{2} = \pm\sqrt{\frac{1 - \cos\alpha}{2}}} \qquad \textcolor{#f59e0b}{\cos\frac{\alpha}{2} = \pm\sqrt{\frac{1 + \cos\alpha}{2}}}
$$

> [!example] Esempio (dal libro di testo): utilizzo delle formule di bisezione
> Sapendo che $\cos\alpha = -\frac{7}{8}$ e che $\pi < \alpha < \frac{3\pi}{2}$, calcoliamo le funzioni goniometriche di $\frac{\alpha}{2}$.
>
> Da $\pi < \alpha < \frac{3\pi}{2}$ segue $\frac{\pi}{2} < \frac{\alpha}{2} < \frac{3\pi}{4}$: l'angolo $\frac{\alpha}{2}$ sta nel secondo quadrante, dove il seno è positivo e il coseno negativo. Quindi nella formula del seno scegliamo il segno **più**, in quella del coseno il segno **meno**:
>
> $$\sin\frac{\alpha}{2} = +\sqrt{\frac{1 - \left(-\frac{7}{8}\right)}{2}} = +\sqrt{\frac{15}{16}} = +\frac{\sqrt{15}}{4}$$
>
> $$\cos\frac{\alpha}{2} = -\sqrt{\frac{1 + \left(-\frac{7}{8}\right)}{2}} = -\sqrt{\frac{1}{16}} = -\frac{1}{4}$$
>
> Dalla definizione di tangente:
>
> $$\tan\frac{\alpha}{2} = \frac{\sin\frac{\alpha}{2}}{\cos\frac{\alpha}{2}} = \frac{\frac{\sqrt{15}}{4}}{-\frac{1}{4}} = -\sqrt{15}$$

## Funzioni lineari in seno e coseno

> [!info] Collegamenti
> I parametri $A$, $\omega$ e $\varphi$ sono gli stessi di un'onda armonica in fisica (ampiezza, pulsazione e fase): vedi [[Onde suono e luce#Onde armoniche|onde armoniche]]. Puoi cambiarli dal vivo nella simulazione [[Moto armonico e onde meccaniche]].

### Parte 1

Come traccio il grafico di

$$
y(x) = A\sin(\omega x + \varphi) + B
$$

Conoscendo i 4 parametri $A$, $B$, $\omega$, $\varphi$ si può disegnare completamente la funzione periodica.

![Grafico di y = sin x](goniometria-sin-base.svg)

#### Modifico B → alzo la funzione o la abbasso

![Grafico di y = sin x - 1](goniometria-sin-meno-1.svg)

![Grafico di y = sin x + 1](goniometria-sin-piu-1.svg)

#### Modifico A → aumento l'altezza dell'onda

Se $A = 1$ al massimo $A\sin(90°) = 1 \cdot 1 = 1$.

![Grafico di y = 2 sin x](goniometria-2sin.svg)

#### Modifico φ → sfasamento dell'onda

$\varphi < 0$ mi sposto a dx, $\varphi > 0$ a sx.

![Grafico di y = sin(x - pi/2)](goniometria-sin-x-meno-pi2.svg)

![Grafico di y = sin(x + pi/2)](goniometria-sin-x-piu-pi2.svg)

↳ questo è $\cos(x)$.

#### Modifico ω → cambio il periodo

Il periodo di una funzione trigonometrica $y = \sin(kx)$ oppure $y = \cos(kx)$ è dato da $\frac{2\pi}{k}$.

$y = \sin(x)$: $\omega = 1$, $T = 2\pi$

![Grafico di y = sin x](goniometria-sin-base.svg)

$y = \sin(2x)$: $\omega = 2$, $T = \frac{2\pi}{2} = \pi$

![Grafico di y = sin(2x)](goniometria-sin-2x.svg)

$y = \sin\left(\frac{x}{2}\right)$: $\omega = \frac{1}{2}$, $T = \dfrac{2\pi}{1/2} = 4\pi$

![Grafico di y = sin(x/2)](goniometria-sin-x-mezzi.svg)

### Parte 2

Quando mi capita di avere una funzione del tipo $y = a\sin x + b\cos x + c$ è possibile ricondurla ad una funzione più semplice scritta come un singolo sin.

$$
y = a\sin x + b\cos x + c \quad\longrightarrow\quad y = \sqrt{a^2 + b^2}\,\sin(x + \varphi) + c \qquad a, b \neq 0
$$

$$
\sin\varphi = \frac{b}{\sqrt{a^2 + b^2}} \qquad \cos\varphi = \frac{a}{\sqrt{a^2 + b^2}}
$$

> [!example] Esempio
> $$y = \underbrace{\sqrt3}_{a}\,\sin x + \underbrace{1}_{b}\,\cos x \underbrace{-\,1}_{c}$$
>
> $$y = \sqrt{3 + 1} \cdot \sin(x + \varphi) - 1$$
>
> $$\varphi \longrightarrow \sin\varphi = \frac{1}{2} \qquad \cos\varphi = \frac{\sqrt3}{2} \qquad \varphi = \frac{\pi}{6}$$
>
> $$\longrightarrow\quad y = 2\sin\left(x + \frac{\pi}{6}\right) - 1$$

![Grafico di y = 2 sin(x + pi/6) - 1](goniometria-esempio-2sin.svg)
