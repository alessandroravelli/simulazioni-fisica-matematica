// Se la pagina è mostrata dentro un'altra (iframe in una nota), segnala
// la cosa al CSS: l'intestazione con "Torna all'elenco" viene nascosta.
if (window.self !== window.top) document.documentElement.classList.add("incorporato");
