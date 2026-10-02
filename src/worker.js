export default {
  async fetch(request, env) {
    const ruolo = verificaAuth(request.headers.get("Authorization"), env);

    if (!ruolo) {
      return new Response("Accesso riservato.", {
        status: 401,
        headers: {
          "WWW-Authenticate": 'Basic realm="Simulazioni interattive", charset="UTF-8"',
        },
      });
    }

    // Il docente riceve pagine diverse (col pulsante "Modifica", vedi
    // sotto): niente risposte "304 non modificato" basate sulla copia in
    // cache del browser, che potrebbe essere quella senza pulsante.
    let richiesta = request;
    if (ruolo === "docente") {
      const intestazioni = new Headers(request.headers);
      intestazioni.delete("If-None-Match");
      intestazioni.delete("If-Modified-Since");
      richiesta = new Request(request, { headers: intestazioni });
    }

    const risposta = await env.ASSETS.fetch(richiesta);
    const finale = new Response(risposta.body, risposta);
    finale.headers.append("Set-Cookie", `ruolo=${ruolo}; Path=/; SameSite=Lax`);

    // Solo per il docente: nelle pagine generate da Quartz (non nelle
    // simulazioni) aggiunge il pulsante "Modifica", che apre la nota
    // nell'editor web di GitHub. È solo una scorciatoia: salvare le
    // modifiche richiede comunque l'accesso in scrittura al repository.
    const tipo = finale.headers.get("Content-Type") || "";
    const percorso = new URL(request.url).pathname;
    if (ruolo === "docente" && tipo.includes("text/html") && !percorso.startsWith("/esperimenti/")) {
      finale.headers.delete("ETag");
      finale.headers.set("Cache-Control", "private, no-cache");
      return new HTMLRewriter()
        .on("body", {
          element(el) {
            el.append('<script src="/assets/js/modifica.js" defer></script>', { html: true });
          },
        })
        .transform(finale);
    }
    return finale;
  },
};

// Elenco dei ruoli con accesso al sito. Ogni ruolo ha una coppia
// username/password salvata come secret Cloudflare (mai nel codice).
// Per aggiungere un nuovo ruolo: aggiungere una riga qui con un nome a
// scelta, fare il deploy, poi impostare i due secret corrispondenti
// (vedi GESTIONE-UTENTI.txt nella root del repository).
const RUOLI = [
  { nome: "docente", chiaveUsername: "USERNAME_MASTER", chiavePassword: "PASSWORD_MASTER" },
  { nome: "studente", chiaveUsername: "USERNAME_STUDENTI", chiavePassword: "PASSWORD_STUDENTI" },
  { nome: "camilla", chiaveUsername: "USERNAME_CAMILLA", chiavePassword: "PASSWORD_CAMILLA" },
  { nome: "federico", chiaveUsername: "USERNAME_FEDERICO", chiavePassword: "PASSWORD_FEDERICO" },
];

function verificaAuth(header, env) {
  if (!header || !header.startsWith("Basic ")) return null;

  const decoded = atob(header.slice(6));
  const separatore = decoded.indexOf(":");
  const username = separatore === -1 ? "" : decoded.slice(0, separatore);
  const password = separatore === -1 ? decoded : decoded.slice(separatore + 1);

  for (const ruolo of RUOLI) {
    const usernameAtteso = env[ruolo.chiaveUsername];
    const passwordAttesa = env[ruolo.chiavePassword];
    if (usernameAtteso && passwordAttesa && username === usernameAtteso && password === passwordAttesa) {
      return ruolo.nome;
    }
  }
  return null;
}
