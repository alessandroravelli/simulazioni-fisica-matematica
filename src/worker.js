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

function verificaAuth(header, env) {
  if (!header || !header.startsWith("Basic ")) return null;

  const decoded = atob(header.slice(6));
  const separatore = decoded.indexOf(":");
  const password = separatore === -1 ? decoded : decoded.slice(separatore + 1);

  if (env.PASSWORD_MASTER && password === env.PASSWORD_MASTER) return "docente";
  if (env.PASSWORD_STUDENTI && password === env.PASSWORD_STUDENTI) return "studente";
  return null;
}
