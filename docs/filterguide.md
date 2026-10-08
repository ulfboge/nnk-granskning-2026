# Filterguide för webbGIS

*LstD NNK Granskning · Länsstyrelsen i Södermanlands län · NNK 2026*

Vilka filter i webbGIS-appen som hjälper dig att hitta kandidater till *fullgod*, *icke fullgod* eller *till fält* — en flik per grupp av livsmiljötyper. Välj fliken för den grupp ytan tillhör. Gruppen står i popupen under *Naturtyp (NNK-data)*, raden *Bedömningsgrupp (R7)*.

**Grundurvalet ska alltid vara på:** *Natura 2000-typ*, *Marina objekt* och *Dölj icke-Natura-livsmiljötyper*. Filtren kombineras med OCH. Vill du ha ELLER, slå på dem ett i taget.

| Tecken | Betyder |
|---|---|
| **på** | Slå alltid på för gruppen |
| ● huvudfilter | Ger kandidater till fullgod eller icke fullgod |
| ○ komplement | Stöder bedömningen eller styr arbetsordningen |
| siffra | Antal ytor inom N2000 i gruppen som filtret träffar (uttag 2026-08-26) |

**Grupper och batcher är två olika indelningar.** *Batch* (S, A, B, C, D) är arbetsordningen per Natura 2000-område — vilket objekt du tar när. *Grupp* (Hävd, Skog, Våtmark, Stabila) avgör vilken bedömningsregel i metodiken (R7A–R7D) som gäller för en enskild yta. Ett och samma objekt innehåller därför ytor från flera grupper. Tabellen visar antal ytor med Natura-naturtyp i varje batch (uttag 2026-08-26):

| Batch | Objekt | Uppgift | Hävd | Skog | Våtmark | Stabila | Marint (lämnas) |
|---|---|---|---:|---:|---:|---:|---:|
| S | Storobjekten | C2.1 | 567 | 799 | 23 | 924 | 364 |
| A | Kust och skärgård | C3.1 | 311 | 370 | 36 | 395 | 177 |
| B | Ängs- och hagmark inland | C4.1 | 147 | 55 | 18 | 16 | 1 |
| C | Våtmark och vattendrag | C5.1 | 7 | 115 | 43 | 0 | 0 |
| D | Skog och ädellöv | C6.1 | 33 | 90 | 4 | 0 | 4 |

## Hävd

**Hävd** — hävdberoende gräsmarker, strandängar och trädklädd betesmark. Bedöms enligt **R7A** i [metodiken](metodik.html). 1 375 ytor inom N2000.

*Typer:* 1630, 4030, 5130, 5133, 6110, 6210, 6230, 6270, 6280, 6410, 6430, 6510, 8231, 9070, 9071, 9072

### Arbetsgång

1. Slå på **Hävdberoende**.
2. Lägg till ett skiftesfilter i taget: **Ja** → kandidater till fullgod, **Nej** → kandidater till icke fullgod, **Delvis**/**Oklart** → behöver mer underlag.
3. För Delvis, Oklart och Nej: slå på **SkötselDOS: bete/slåtter** — bete utan stöd syns bara där.
4. **TUVA-träff** visar vilka som har TUVA-underlag. **TUVA ohävdad/igenväxande** och **Uppföljning: dålig** ger kandidater till icke fullgod.
5. 6430 längs vattendrag är ofta inte hävdberoende → *till fält*. Laserfälten finns inte för 9070.

### Filter som ger något för gruppen

| Filter | Roll | Ytor | Så läser du träffen |
|---|---|---:|---|
| **Hävdberoende**<br>`havdberoende = 'Ja'` | **på** |  | Motsvarar gruppen Hävd. Slå alltid på när du bedömer hävdtyper, annars drar hävdfiltren med sig skog och myr. |
| **Hävd enligt skiften: Ja**<br>`havd_skiften = 'Ja'` | ● | 158 | Bete eller slåtter varje år sedan 2015 (eller sedan typen sattes) → kandidat *fullgod*. Kontrollera orto. |
| **Hävd enligt skiften: Delvis**<br>`havd_skiften = 'Delvis'` | ● | 607 | Hävd vissa år. Se popupen för saknade år — saknas bara 2015 är det troligen brist i skiftesdata. Behöver oftast TUVA eller SkötselDOS. |
| **Hävd enligt skiften: Nej**<br>`havd_skiften = 'Nej'` | ● | 369 | Träffar skiften men aldrig bete/slåtter → kandidat *icke fullgod* på hävdberoende ytor. På skog och myr betyder Nej oftast bara att ytan gränsar mot åker — använd inte där. |
| **Hävd enligt skiften: Oklart**<br>`havd_skiften = 'Oklart'` | ○ | 241 | Inga skiften alls. Bete utan stöd syns inte — gå vidare med SkötselDOS och TUVA. |
| **Vall senaste året**<br>`havd_varning_vall = 'Ja'` | ○ | 2 | Varning för 6270, 6410 och 6510. Bara 2 hävdberoende ytor inom N2000 — kontrollera dem, men det är inget urvalsfilter. |
| **SkötselDOS: bete/slåtter**<br>`skdos_havd_typ IS NOT NULL` | ● | 122 | Utförd bete/slåtter i Länsstyrelsens skötselsystem — fångar bete som inte syns i skiftena. Kontrollera att åtgärden ligger på ytan och inte bara i reservatet. På skog kan det tyda på skogsbete (pröva om 9070 är rätt typ), på myr på slåtter av rikkärr (7230). |
| **TUVA-träff**<br>`tuva_antal_objekt IS NOT NULL` | ● | 980 | Ytan överlappar ett TUVA-objekt — underlag för både typ och hävd. TUVA äldre än 15 år räcker inte. Träff på skog eller strand: pröva om typen stämmer. |
| **TUVA ohävdad/igenväxande**<br>`tuva_negativ = 'Ja'` | ● | 133 | Ingen hävd, ohävdad/restaurerbar eller tydlig igenväxning → kandidat *icke fullgod*. På skogsytor kan det betyda att en betesmark vuxit igen. Kontrollera inventeringsåret. |
| **SKS: utförd avverkning**<br>`skr_utford_ar IS NOT NULL` | ○ | 34 | Skogsstyrelsens satellitdetekterade avverkningar på minst 0,1 ha eller 10 % av ytan (tillagt 2026-10-08). Efter karteringen → kandidat *icke fullgod*. Kontrollera året mot karteringen och ingreppet i orto. På hävdytor (9070) kan det vara röjning i betesmark. |
| **Förslag: låg säkerhet**<br>`r7f_utfall LIKE '%säkerhet låg%'` | ● | 342 | Ytor där underlagen säger emot varandra eller är svaga (tillagt 2026-10-08). Ta dem med störst omsorg — förslaget är minst pålitligt där. |
| **Förslag: typ ej styrkt**<br>`r7f_utfall LIKE 'Typ ej styrkt%'` | ○ | 346 | Inget underlag nyare än karteringen stöder typen. Pröva typen i IR-ortot; stöds den inte: Karteringsstatus 5 Åtgärdas. Motivet visar vad tillståndet blir om typen godtas. |
| **Förslag: fullgod eller icke fullgod**<br>`r7f_utfall LIKE '%ullgod%'` | ● | 508 | Ytor där förslaget har ett utfall att pröva mot villkoret (oftast ortot). Snabbast att gå igenom först. |
| **Typiska arter i Artportalen**<br>`typarter_antal IS NOT NULL` | ○ |  | Fynd sedan 2010, noggrannhet ≤ 100 m. Stöder att typen är rimlig — förutsättningen för alla R7-grupper. Inga fynd betyder inte att arten saknas. |
| **Uppföljning: dålig**<br>`uppf_antal_dalig > 0` | ● | 12 | Uppföljningspunkt med måluppfyllelse Dålig (2015–2022) → kandidat *icke fullgod*. Nästan bara hävdberoende ytor. |

## Skog

**Skog** — barrskog, lövskog, ädellöv och sumpskog. Bedöms enligt **R7B** i [metodiken](metodik.html). 1 944 ytor inom N2000.

*Typer:* 2181, 9006, 9008, 9009, 9010, 9020, 9030, 9050, 9060, 9080, 9110, 9160, 9162, 9180, 9190, 9740, 9750

### Arbetsgång

1. **9010 och 9050** (inkl. 9006, 9008, 9009, 9830) blir aldrig *fullgod* vid skrivbordet — död ved är ett klassningskrav. Filtren ger bara kandidater till icke fullgod; övriga blir *till fält*.
2. **Laser: möjlig avverkning** → kandidater till icke fullgod. Kontrollera orto och avverkningsinformationen.
3. **Laser: möjlig gallring** → svagare signal, kontrollera orto.
4. För sumpskog (9080), 9740 och 9750: **Diken inom ytan**.
5. Ytor utan laserflagga och utan diken är kandidater till fullgod (utom 9010/9050) — kolla ändå avverkningar efter 2020.
6. Skiftesfiltren säger inget här. **TUVA-träff** eller **SkötselDOS** på skog: pröva om typen egentligen är trädklädd betesmark (9070).
7. **SKS: utförd avverkning** täcker tiden efter laserskanningen — avverkning efter karteringen → kandidat till icke fullgod.

### Filter som ger något för gruppen

| Filter | Roll | Ytor | Så läser du träffen |
|---|---|---:|---|
| **SkötselDOS: bete/slåtter**<br>`skdos_havd_typ IS NOT NULL` | ○ | 77 | Utförd bete/slåtter i Länsstyrelsens skötselsystem — fångar bete som inte syns i skiftena. Kontrollera att åtgärden ligger på ytan och inte bara i reservatet. På skog kan det tyda på skogsbete (pröva om 9070 är rätt typ), på myr på slåtter av rikkärr (7230). |
| **TUVA-träff**<br>`tuva_antal_objekt IS NOT NULL` | ○ | 104 | Ytan överlappar ett TUVA-objekt — underlag för både typ och hävd. TUVA äldre än 15 år räcker inte. Träff på skog eller strand: pröva om typen stämmer. |
| **TUVA ohävdad/igenväxande**<br>`tuva_negativ = 'Ja'` | ○ | 57 | Ingen hävd, ohävdad/restaurerbar eller tydlig igenväxning → kandidat *icke fullgod*. På skogsytor kan det betyda att en betesmark vuxit igen. Kontrollera inventeringsåret. |
| **Laser: möjlig avverkning**<br>`laser_flagga = 'Möjlig avverkning'` | ● | 37 | Höjden sjönk mer än 5 m mellan skanningarna 2010–12 och 2020 → kandidat *icke fullgod*. Kontrollera orto och Skogsstyrelsens avverkningsinformation — kan vara storm eller granbarkborre. Laserfälten finns bara för gruppen Skog. |
| **Laser: möjlig gallring**<br>`laser_flagga = 'Möjlig gallring'` | ○ | 106 | Grundytan minskade, höjden oförändrad. Svagare signal — kontrollera i orto. |
| **Diken inom ytan**<br>`diken_m_inom > 0` | ● | 440 | Skogsstyrelsens AI-karterade diken. Väger tyngst för sumpskog (9080), 9740, 9750 och myrarna 7110–7231 → kandidat *icke fullgod*. Kontrollera i terrängskuggningen och markfuktighetskartan. |
| **SKS: utförd avverkning**<br>`skr_utford_ar IS NOT NULL` | ● | 38 | Skogsstyrelsens satellitdetekterade avverkningar på minst 0,1 ha eller 10 % av ytan (tillagt 2026-10-08). Efter karteringen → kandidat *icke fullgod*. Kontrollera året mot karteringen och ingreppet i orto. På hävdytor (9070) kan det vara röjning i betesmark. |
| **SKS: avverkningsanmälan**<br>`skr_anmald_ar IS NOT NULL` | ○ | 3 | Aktuell anmälan på ytan. Säger att avverkning får ske, inte att den skett — kontrollera i *SKS Avverkningsinformation* och orto. |
| **Förslag: låg säkerhet**<br>`r7f_utfall LIKE '%säkerhet låg%'` | ● | 154 | Ytor där underlagen säger emot varandra eller är svaga (tillagt 2026-10-08). Ta dem med störst omsorg — förslaget är minst pålitligt där. |
| **Förslag: typ ej styrkt**<br>`r7f_utfall LIKE 'Typ ej styrkt%'` | ● | 981 | Inget underlag nyare än karteringen stöder typen. Pröva typen i IR-ortot; stöds den inte: Karteringsstatus 5 Åtgärdas. Motivet visar vad tillståndet blir om typen godtas. |
| **Förslag: fullgod eller icke fullgod**<br>`r7f_utfall LIKE '%ullgod%'` | ● | 207 | Ytor där förslaget har ett utfall att pröva mot villkoret (oftast ortot). Snabbast att gå igenom först. |
| **Typiska arter i Artportalen**<br>`typarter_antal IS NOT NULL` | ○ |  | Fynd sedan 2010, noggrannhet ≤ 100 m. Stöder att typen är rimlig — förutsättningen för alla R7-grupper. Inga fynd betyder inte att arten saknas. |
| **Uppföljning: dålig**<br>`uppf_antal_dalig > 0` | ○ | 1 | Uppföljningspunkt med måluppfyllelse Dålig (2015–2022) → kandidat *icke fullgod*. Nästan bara hävdberoende ytor. |

## Våtmark

**Våtmark** — myr, kärr, sjöar och vattendrag. Bedöms enligt **R7C** i [metodiken](metodik.html). 344 ytor inom N2000.

*Typer:* 3110, 3130, 3150, 3160, 3260, 7110, 7111, 7140, 7141, 7142, 7230, 7231

### Arbetsgång

1. Myrar (7110–7231): **Diken inom ytan** → kandidater till icke fullgod. Kontrollera terrängskuggning och markfuktighetskarta.
2. Rikkärr (7230): **SkötselDOS: bete/slåtter** visar var hävd ingår i skötseln.
3. Sjöar och vattendrag (3110–3260): VISS-fälten fylls när D2.5 är körd. Tills dess: slå upp statusen i gruppen *Vatten (VISS)*.
4. **Typiska arter i Artportalen** stöder att typen är rätt.

### Filter som ger något för gruppen

| Filter | Roll | Ytor | Så läser du träffen |
|---|---|---:|---|
| **SkötselDOS: bete/slåtter**<br>`skdos_havd_typ IS NOT NULL` | ○ | 42 | Utförd bete/slåtter i Länsstyrelsens skötselsystem — fångar bete som inte syns i skiftena. Kontrollera att åtgärden ligger på ytan och inte bara i reservatet. På skog kan det tyda på skogsbete (pröva om 9070 är rätt typ), på myr på slåtter av rikkärr (7230). |
| **Diken inom ytan**<br>`diken_m_inom > 0` | ● | 25 | Skogsstyrelsens AI-karterade diken. Väger tyngst för sumpskog (9080), 9740, 9750 och myrarna 7110–7231 → kandidat *icke fullgod*. Kontrollera i terrängskuggningen och markfuktighetskartan. |
| **Förslag: låg säkerhet**<br>`r7f_utfall LIKE '%säkerhet låg%'` | ● | 154 | Ytor där underlagen säger emot varandra eller är svaga (tillagt 2026-10-08). Ta dem med störst omsorg — förslaget är minst pålitligt där. |
| **Förslag: typ ej styrkt**<br>`r7f_utfall LIKE 'Typ ej styrkt%'` | ○ | 122 | Inget underlag nyare än karteringen stöder typen. Pröva typen i IR-ortot; stöds den inte: Karteringsstatus 5 Åtgärdas. Motivet visar vad tillståndet blir om typen godtas. |
| **Förslag: fullgod eller icke fullgod**<br>`r7f_utfall LIKE '%ullgod%'` | ● | 109 | Ytor där förslaget har ett utfall att pröva mot villkoret (oftast ortot). Snabbast att gå igenom först. |
| **Typiska arter i Artportalen**<br>`typarter_antal IS NOT NULL` | ○ |  | Fynd sedan 2010, noggrannhet ≤ 100 m. Stöder att typen är rimlig — förutsättningen för alla R7-grupper. Inga fynd betyder inte att arten saknas. |

## Stabila

**Stabila** — strand, klippa, skär och häll utan hävdberoende. Bedöms enligt **R7D** i [metodiken](metodik.html). 1 549 ytor inom N2000.

*Typer:* 1220, 1230, 1232, 1620, 1621, 1640, 8210, 8220, 8230, 8232

### Arbetsgång

1. Få filter ger tillståndssignal — typerna är stabila och regeln (R7D) bygger mest på att typen är rimlig och att ortot inte visar ingrepp.
2. **Typiska arter i Artportalen** och **Större än 5 ha** för de ytor som granskas en och en.
3. **TUVA-träff** eller **Hävd enligt skiften: Delvis** på strand eller häll: pröva om ytan egentligen är strandäng (1630) eller annan hävdberoende typ.
4. Kusten granskas i **Batch A**.

### Filter som ger något för gruppen

| Filter | Roll | Ytor | Så läser du träffen |
|---|---|---:|---|
| **Hävd enligt skiften: Delvis**<br>`havd_skiften = 'Delvis'` | ○ | 83 | Hävd vissa år. Se popupen för saknade år — saknas bara 2015 är det troligen brist i skiftesdata. Behöver oftast TUVA eller SkötselDOS. |
| **TUVA-träff**<br>`tuva_antal_objekt IS NOT NULL` | ○ | 132 | Ytan överlappar ett TUVA-objekt — underlag för både typ och hävd. TUVA äldre än 15 år räcker inte. Träff på skog eller strand: pröva om typen stämmer. |
| **TUVA ohävdad/igenväxande**<br>`tuva_negativ = 'Ja'` | ○ | 27 | Ingen hävd, ohävdad/restaurerbar eller tydlig igenväxning → kandidat *icke fullgod*. På skogsytor kan det betyda att en betesmark vuxit igen. Kontrollera inventeringsåret. |
| **Förslag: låg säkerhet**<br>`r7f_utfall LIKE '%säkerhet låg%'` | ○ | 57 | Ytor där underlagen säger emot varandra eller är svaga (tillagt 2026-10-08). Ta dem med störst omsorg — förslaget är minst pålitligt där. |
| **Förslag: typ ej styrkt**<br>`r7f_utfall LIKE 'Typ ej styrkt%'` | ● | 1309 | Inget underlag nyare än karteringen stöder typen. Pröva typen i IR-ortot; stöds den inte: Karteringsstatus 5 Åtgärdas. Motivet visar vad tillståndet blir om typen godtas. |
| **Förslag: fullgod eller icke fullgod**<br>`r7f_utfall LIKE '%ullgod%'` | ● | 216 | Ytor där förslaget har ett utfall att pröva mot villkoret (oftast ortot). Snabbast att gå igenom först. |
| **Typiska arter i Artportalen**<br>`typarter_antal IS NOT NULL` | ○ |  | Fynd sedan 2010, noggrannhet ≤ 100 m. Stöder att typen är rimlig — förutsättningen för alla R7-grupper. Inga fynd betyder inte att arten saknas. |

## Urval och arbetsordning

Filter som inte säger något om tillståndet men styr vilka ytor du ser och i vilken ordning. Gäller alla grupper.

| Filter | Villkor | Så används det |
|---|---|---|
| **Natura 2000-typ** | `n2000_typ` = SCI eller SCI+SPA | Aktivt vid start. Avgränsar till Natura 2000-områden av typen SCI eller SCI+SPA. |
| **Marina objekt** | `naturtyp NOT IN (1000, 1110 … 1174)` | Aktivt vid start. Döljer de marina typerna. Strandängar (1630), skär (1620), alvar (1640) och driftvallar (1220) ligger kvar. |
| **Dölj icke-Natura-livsmiljötyper** | `naturtyp NOT IN (1950, 2920 …)` | Slå på vid statusgranskning — R7 gäller bara Natura-naturtyper. |
| **Osäker/obestämd naturtyp** | `naturtyp IN (2300, 4810 … 9870)` | Eget spår, inte statusbedömning: typen måste bestämmas först (E2.1, P2-kriteriet). Använd utan gruppfiltren och utan *Dölj icke-Natura*. |
| **Prio P1–P4** | `prio = 'P1'` osv. | Arbetsordning enligt arbetsplanen 5.2. Säger inget om tillståndet. |
| **Batch S / A / B / C / D** | `batch = 'S'` osv. | Bara de 40 P1-objekten. Batcharna är arbetsordning per *objekt* och är inte samma sak som R7-grupperna, som gäller per *yta*. Batch B (ängs- och hagmark) består mest av hävdtyper, C mest av våtmark, D mest av skog, A är kusten (strandängar hör till Hävd, skär och stränder till Stabila) och S storobjekten (blandat). |
| **Ej granskade / Granskning påbörjad** | `granskat = 2` / `3` | Arbetsläge. Kombinera med gruppens filter för att se vad som återstår. |
| **Större än 5 ha** | `area_ha > 5` | C2.1: ytor som granskas en och en i storobjekten. |
| **Sällsynt livsmiljötyp** | `sallsynt = 'Ja'` | Under 50 ha i länets N2000 (28 koder). Varje yta väger tungt för länets andel — ta dem tidigt. |

## Alla filter

Översikt: vilka filter som ger något för vilken grupp. Detaljerna står under respektive flik.

| Filter | Hävd | Skog | Våtmark | Stabila |
|---|:---:|:---:|:---:|:---:|
| Natura 2000-typ | på | på | på | på |
| Marina objekt | på | på | på | på |
| Dölj icke-Natura-livsmiljötyper | på | på | på | på |
| Osäker/obestämd naturtyp | – | – | – | – |
| Prio P1–P4 | ○ | ○ | ○ | ○ |
| Batch S / A / B / C / D | ○ | ○ | ○ | ○ |
| Ej granskade / Granskning påbörjad | ○ | ○ | ○ | ○ |
| Större än 5 ha | ○ | ○ | ○ | ○ |
| Sällsynt livsmiljötyp | ○ | ○ | ○ | ○ |
| Hävdberoende | på | – | – | – |
| Hävd enligt skiften: Ja | ● 158 | – | – | – |
| Hävd enligt skiften: Delvis | ● 607 | – | – | ○ 83 |
| Hävd enligt skiften: Nej | ● 369 | – | – | – |
| Hävd enligt skiften: Oklart | ○ 241 | – | – | – |
| Vall senaste året | ○ 2 | – | – | – |
| SkötselDOS: bete/slåtter | ● 122 | ○ 77 | ○ 42 | – |
| TUVA-träff | ● 980 | ○ 104 | – | ○ 132 |
| TUVA ohävdad/igenväxande | ● 133 | ○ 57 | – | ○ 27 |
| Laser: möjlig avverkning | – | ● 37 | – | – |
| Laser: möjlig gallring | – | ○ 106 | – | – |
| Diken inom ytan | – | ● 440 | ● 25 | – |
| SKS: utförd avverkning | ○ 34 | ● 38 | – | – |
| SKS: avverkningsanmälan | – | ○ 3 | – | – |
| Förslag: låg säkerhet | ● 342 | ● 154 | ● 154 | ○ 57 |
| Förslag: typ ej styrkt | ○ 346 | ● 981 | ○ 122 | ● 1309 |
| Förslag: fullgod eller icke fullgod | ● 508 | ● 207 | ● 109 | ● 216 |
| Typiska arter i Artportalen | ○ | ○ | ○ | ○ |
| Uppföljning: dålig | ● 12 | ○ 1 | – | – |

---

*Genererad ur `natura-2000: scripts/analysis/uppgifter.py` med `bygg_kontrollrum.py` — redigera där, inte i den här filen*