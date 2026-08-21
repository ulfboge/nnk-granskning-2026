# NNK-granskning 2026 — Södermanlands län

Arbetsdokument och kontrollpanel för statusbedömning av livsmiljötyper inom Natura 2000.
Länsstyrelsen i Södermanlands län · Naturskyddsenheten · ref. 2451-2026

## Öppna kontrollpanelen

🌐 **https://ulfboge.github.io/nnk-granskning-2026**

Allt är fristående HTML utan externa beroenden — inga CDN:er, inga skript utifrån, inga inloggningar.
Det gör att sidorna fungerar bakom brandvägg och proxy, och att de går att spara ned och öppna lokalt.

## Innehåll

| Fil | Vad det är |
|-----|------------|
| [`index.html`](index.html) | Kontrollpanel — ingång till allt |
| [`kontrollrum.html`](kontrollrum.html) | Gantt v34–v52, 68 uppgifter med avbockning, leveranser, milstolpar |
| [`kunskapslage.html`](kunskapslage.html) | Kunskapsläge per Natura 2000-område |
| [`docs/arbetsplan.md`](docs/arbetsplan.md) | Arbetsplan v1.3 — kravnedbrytning, arbetspaket A–H |
| [`docs/runbook.md`](docs/runbook.md) | Runbook — steg för steg genom alla 68 uppgifter |
| [`docs/metodik.md`](docs/metodik.md) | Metodik förvaltarkunskap — arbetspaket H |
| [`docs/typiska-arter.md`](docs/typiska-arter.md) | Typiska/karakteristiska arter per naturtyp — stöd för fältet "Vad ska kontrolleras" |
| [`blanketter/`](blanketter/) | Excelmall för insamling av förvaltarkunskap |

Markdownfilerna finns även som HTML under `docs/*.html` — det är de som kontrollpanelen länkar till.
Källan i Markdown ligger kvar så att ändringar går att diffa i Git.

## Vad som medvetet ligger någon annanstans

Detta repo innehåller **bara material vi själva har producerat**. Följande ligger i det privata
syskonrepot [`natura-2000`](https://github.com/ulfboge/natura-2000):

- Naturvårdsverkets underlag — handledning, kodlista, FAQ, statistikuttag, naturtypskartan (`.lyrx`)
- Rådata och shapefiler (`data/`)
- Datapipeline och analysskript (`scripts/`)
- Origo-webbkarta och ArcGIS Pro-projekt

Sökvägar som `natura-2000: docs/underlag/...` i dokumenten syftar på det repot.

Projektöversikten för naturrestaureringsuppdraget i stort finns i
[`lansstyrelsen-nrr`](https://github.com/ulfboge/lansstyrelsen-nrr).

## Bygga om HTML-versionerna

När en `.md`-fil ändras genereras motsvarande `.html` om med:

```bash
python -m pip install markdown
python bygg.py
```

## Status

Arbetsmaterial under pågående uppdrag. Siffror och bedömningar är preliminära
tills NNK:s nya tillståndsattribut är driftsatta (enligt NV: slutet av september 2026).
