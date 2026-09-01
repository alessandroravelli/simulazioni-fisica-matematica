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

    const risposta = await env.ASSETS.fetch(request);
    const finale = new Response(risposta.body, risposta);
    finale.headers.append("Set-Cookie", `ruolo=${ruolo}; Path=/; SameSite=Lax`);
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
