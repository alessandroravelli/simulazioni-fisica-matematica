// Adatta le note scritte in Obsidian a come le legge Quartz.
// Gira da solo prima di ogni build (vedi wrangler.jsonc); si può lanciare anche a mano:
//   node strumenti/sistema-markdown.mjs sito/content
//
// 1. Formule su una riga sola  "$$ v = \lambda/T $$"  (Obsidian le centra, Quartz no)
//    diventano blocchi su tre righe:
//      $$
//      v = \lambda/T
//      $$
//    Funziona anche dentro i callout ("> $$ ... $$").
// 2. Immagini SVG incorporate con "![[file.svg]]" (sul sito non si vedono)
//    diventano "![file](file.svg)".

import fs from "node:fs"
import path from "node:path"

const cartella = process.argv[2] ?? "sito/content"

const FORMULA_SU_UNA_RIGA = /^(\s*(?:>\s*)*)\$\$(?!\$)(.*?[^$\s].*?)\$\$\s*$/
const SVG_OBSIDIAN = /!\[\[([^\]|#]+?\.svg)(?:\|([^\]]*))?\]\]/g

function sistema(testo) {
  let inCodice = false
  let inFormula = false
  return testo
    .split("\n")
    .map((riga) => {
      const pulita = riga.replace(/^\s*(?:>\s*)*/, "")
      if (/^(```|~~~)/.test(pulita)) inCodice = !inCodice
      if (inCodice) return riga
      if (pulita.trim() === "$$") {
        inFormula = !inFormula
        return riga
      }
      if (inFormula) return riga

      const f = riga.match(FORMULA_SU_UNA_RIGA)
      if (f && !f[2].includes("$$")) {
        const prefisso = f[1]
        return `${prefisso}$$\n${prefisso}${f[2].trim()}\n${prefisso}$$`
      }
      return riga.replace(SVG_OBSIDIAN, (_, file, alt) => {
        const nome = path.basename(file)
        const descrizione = (alt ?? nome.replace(/\.svg$/, "")).trim()
        const url = nome.includes(" ") ? `<${nome}>` : nome
        return `![${descrizione}](${url})`
      })
    })
    .join("\n")
}

function* fileMarkdown(dir) {
  for (const voce of fs.readdirSync(dir, { withFileTypes: true })) {
    if (voce.name.startsWith(".")) continue
    const p = path.join(dir, voce.name)
    if (voce.isDirectory()) yield* fileMarkdown(p)
    else if (voce.name.endsWith(".md")) yield p
  }
}

let modificati = 0
for (const file of fileMarkdown(cartella)) {
  const prima = fs.readFileSync(file, "utf8")
  const dopo = sistema(prima)
  if (dopo !== prima) {
    fs.writeFileSync(file, dopo)
    modificati++
    console.log(`sistemato: ${path.relative(cartella, file)}`)
  }
}
console.log(`sistema-markdown: ${modificati} file modificati`)
