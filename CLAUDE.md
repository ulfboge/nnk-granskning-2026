# CLAUDE.md — nnk-granskning-2026

> Projektinstruktioner för Claude. Läs detta i sin helhet innan du arbetar i detta repo.

---

## 1. Vad detta repo är

**nnk-granskning-2026** är det **publika** arbetsdokument- och kontrollpanel-repot för
statusbedömningen av livsmiljötyper inom Natura 2000 i Södermanlands län (NNK — naturens
nuvarande kondition/tillstånd), del av naturrestaureringsuppdraget (NRR, ref. 2451-2026) vid
Länsstyrelsen i Södermanlands län, Naturskyddsenheten.

Repot publiceras som **GitHub Pages**: https://ulfboge.github.io/nnk-granskning-2026

Allt innehåll är fristående HTML **utan externa beroenden** — inga CDN:er, inga externa skript,
inga inloggningar. Det gör att sidorna fungerar bakom brandvägg/proxy och går att spara ned och
öppna lokalt.

## 2. Vad som medvetet INTE ligger här

Detta repo innehåller **bara material Länsstyrelsen själv har producerat**. Följande hör hemma i
det **privata** syskonrepot `natura-2000` (https://github.com/ulfboge/natura-2000) istället:

- Naturvårdsverkets underlag (handledning, kodlista, FAQ, statistikuttag, naturtypskarta `.lyrx`)
- Rådata och shapefiler (`data/`)
- Datapipeline och analysskript (`scripts/`)
- Origo-webbkarta och ArcGIS Pro-projekt
- Bedömningsdata, fältprotokoll, Ajourhålla-uttag, NV:s underlagsfiler

Skriv **aldrig** sådant material till detta repo. Sökvägar i dokumenten formaterade som
`natura-2000: docs/underlag/...` syftar på det andra (privata) repot.

Projektöversikten för hela naturrestaureringsuppdraget finns i det tredje syskonrepot,
`lansstyrelsen-nrr` (mappen `Länsstyrelsen/` lokalt).

## 3. Innehåll i detta repo

| Fil/mapp | Vad det är |
|----------|------------|
| `index.html` | Kontrollpanel — ingång till allt |
| `kontrollrum.html` | Gantt v34–v52, 58 uppgifter med avbockning, leveranser, milstolpar |
| `kunskapslage.html` | Kunskapsläge per Natura 2000-område |
| `docs/arbetsplan.md` (+ genererad `.html`) | Arbetsplan — kravnedbrytning, arbetspaket A–H |
| `docs/runbook.md` (+ `.html`) | Runbook — steg för steg genom alla 58 uppgifter |
| `docs/metodik.md` (+ `.html`) | Metodik förvaltarkunskap — arbetspaket H |
| `docs/typiska-arter.md` (+ `.html`) | Typiska/karakteristiska arter per naturtyp |
| `blanketter/blankett_forvaltarkunskap_nnk.xlsx` | Excelmall för insamling av förvaltarkunskap — genereras av `natura-2000/scripts/analysis/bygg_blankett.py`, kopieras hit som referensversion. **Den fil förvaltarna faktiskt fyller i ligger på G:-enheten** (`G:\5_Naturvard_miljoskydd\51_skydd_omr_arter_mm\511_skydd_omr_arter\NRF\blankett_forvaltarkunskap_nnk.xlsx`) — GitHub-kopian är alltså aldrig arbetskopian. |
| `bygg.py` | Genererar om `docs/*.html` från `docs/*.md` (körs efter varje ändring i Markdown-källorna) |
| `nnk_status.json` | Sparat avbockningsläge för kontrollrummet |

Markdown-källorna i `docs/` ligger kvar parallellt med den genererade HTML:en så att ändringar
går att diffa i Git — redigera alltid `.md`-filen, aldrig `.html`-filen direkt.

## 4. Bygga om HTML-sidorna

Efter varje ändring i en `docs/*.md`-fil:

```bash
python -m pip install markdown
python bygg.py
```

`bygg.py` använder samma designtokens (CSS-variabler för ljust/mörkt tema) för alla sidor så att
kontrollpanelen, kontrollrummet och dokumentsidorna ser ut som en enda produkt. Inga externa
CSS-ramverk eller typsnitt hämtas — allt är inline i den genererade HTML:en.

## 5. Relaterade repon

| Repo (lokal mapp) | Synlighet | Roll |
|---|---|---|
| `natura-2000` | Privat | Pipeline, rådata, NV-underlag, Origo/ArcGIS, NNK-analys |
| `Länsstyrelsen` (lansstyrelsen-nrr) | Publikt | Projektöversikt för hela NRR-uppdraget |
| `nnk-granskning-2026` (detta repo) | Publikt | Arbetsdokument + kontrollpanel för NNK-granskningen |

## 6. Status

Arbetsmaterial under pågående uppdrag. Siffror och bedömningar är preliminära tills NNK:s nya
tillståndsattribut är driftsatta (enligt Naturvårdsverket: slutet av september 2026).

## 7. Instruktioner för Claude

1. **Skriv alltid på svenska** (kod och tekniska termer på engelska undantagna).
2. **Lägg aldrig känsligt/internt material här** — se avsnitt 2. Är du osäker om något hör hemma
   i `natura-2000` istället, fråga innan du committar.
3. **Redigera `docs/*.md`, inte `docs/*.html`** — kör `bygg.py` efter varje ändring så att sidorna
   hålls i synk.
4. **Håll sidorna fristående** — inga CDN:er, inga externa skript/typsnitt, inga inloggningar.
   Nya funktioner ska fungera offline/bakom brandvägg precis som befintliga sidor.
5. **Kontrollera om filer redan finns** innan du skapar nya (undvik dubbletter av dokument/sidor).
6. **Synka mot syskonrepona** — ändringar som rör arbetsplan/runbook/uppgifter uppdateras ofta
   parallellt i `natura-2000/scripts/analysis/uppgifter.py` (kontrollrummets datakälla). Se efter
   om en ändring här också kräver en motsvarande ändring där.
7. **`blanketter/blankett_forvaltarkunskap_nnk.xlsx` är en referenskopia** — den senaste
   genererade versionen från `natura-2000`, inte den faktiska arbetskopian (se avsnitt 3). Länka
   eller beskriv den som referens, inte som "fyll i denna".
8. **`git push` fungerar inte via device_bash** (autentiseringsfel) — gör commits klara lokalt och
   låt Johan pusha själv, om inte annat är uppsatt.

---

*Skapad: 2026-08-27*
