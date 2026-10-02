# Attributbeskrivning / kodlista — LstD NNK Granskning

## Länsstyrelsen i Södermanlands län · Naturskyddsenheten · NNK 2026

**Version:** 1.5 · 2026-10-02 (samlingsfälten `tuva_negativ` och `fv_forsamring` för webbGIS-filtren). 1.4 · 2026-10-01 (SkötselDOS- och uppföljningsfälten i Del C). 1.3 · 2026-09-30 (laser- och dikesfälten i Del C). 1.2 · 2026-09-30 (TUVA-fälten i Del C). 1.1 · 2026-09-25 (ny Del C: datering och länets stödfält)  
**Hör ihop med:** `docs/webbgis-publicering.html` (Del 6, knappen "Kodlista/attributbeskrivning")  
**Källor:** blankett_forvaltarkunskap_nnk.xlsx (Kodlistor-fliken), KartLits-mallens ArcGIS-domäner, Beskrivning_NNK_koder.pdf (NV PM NV-08177-15), Handledning NNK 20260703.pdf

Slå upp vad ett granskningsfält eller en kod betyder utan att lämna webbGIS:et. Del A är fälten du själv fyller i. Del B är NV:s egna, skrivskyddade källfält som visas i popupen. Del C är dateringsfälten och de stödfält som länets egen pipeline lägger till.

---

## Del A · Granskningsfälten (det du fyller i)

### Grupp 1 · Livsmiljötyp och utbredning

**Livsmiljötyp, behov av justering**  
Ändra bara vid fel klassificering eller faktisk förändring — inte vid igenväxning pga utebliven skötsel (sätt då Tillstånd = Icke gott i stället).

| Kod | Klartext |
|---|---|
| 1 | Inget behov av justering |
| 2 | Ändring till annan livsmiljötyp |
| 3 | Ändring till utvecklingsmark |
| 4 | Osäker – kan ej bedöma om livsmiljötyp eller inte |
| 5 | Obestämd – kan ej bedöma vilken livsmiljötyp |

**Utbredning, behov av justering**  
Ändra bara om gränsen är fel och avvikelsen är minst lika stor som minsta karteringsenhet.

| Kod | Klartext |
|---|---|
| 1 | Inget behov av justering |
| 2 | Yttergränser, kvalitetsförbättring |
| 3 | Yttergränser, ändrad utbredning |
| 4 | Behov av att dela upp ytan, flera livsmiljötyper |

**Livsmiljötyp 1**  
Förstahandsförslag på rätt livsmiljötyp, vid fel klassificering. Koderna är samma kodutrymme som NV:s naturtypskoder — se tabellen längre ned.

**Livsmiljötyp 2**  
Andrahandsförslag, om osäker mellan flera typer.

**Livsmiljötyp 3**  
Tredjehandsförslag, om osäker mellan flera typer.

**Förändringsorsak, förslag** *(tillagd 2026-09-22)*  
Granskarens eget förslag till varför bedömningen ändras — fylls i även när du vid skrivbordsgranskning bekräftar att objektets "ej bedömda" status faktiskt stämmer. Skild från det skrivskyddade käll­fältet Förändringsorsak i Del B, som visar NV:s NUVARANDE registrerade värde. Samma tre koder, samma domän (NV_NNK_Förändringsorsak) — se Del B nedan för kodlistan. Nästan alltid kod 3 Komplettering (R2-regeln, se `metodik.html` avsnitt 5): kunskapen fanns, den var bara inte registrerad. Kod 2 Faktisk förändring bara vid en verklig, daterad förändring på marken.

**Kommentar – livsmiljötyp och utbredning**  
Grund för bedömningen (skötselplan, bevarandeplan, fältbesök …) och när kunskapen är ifrån.

### Grupp 2 · Tillstånd

**Tillstånd, behov av justering**  
Gott = bra skick. Icke gott = igenvuxen/behöver restaurering, även vid utebliven skötsel. Okänt = kan inte bedömas — ange skälet i kommentaren. Blandat = ange andelar i procentfälten (ska bli 100 %).

| Kod | Klartext |
|---|---|
| 1 | Gott |
| 2 | Icke gott |
| 3 | Okänt – kan ej bedöma |
| 4 | Blandat – se andelar |

**Gott tillstånd (%)**  
Andel av ytan i gott tillstånd om blandat. Summan av de tre procentfälten ska bli 100.

**Ej gott tillstånd (%)**  
Andel av ytan i icke gott tillstånd om blandat. Summan av de tre procentfälten ska bli 100.

**Osäker (%)**  
Andel av ytan där tillståndet är osäkert. Summan av de tre procentfälten ska bli 100.

**Kommentar – Tillstånd**  
Grund för bedömningen. Vid osäkerhet: dokumentera vad ni inte vet i stället för att gissa.

### Grupp 3 · Vad ska kontrolleras och hur

**Vad ska kontrolleras 1–3**  
Vad som bör kontrolleras/inventeras inför 2027: typiska arter, strukturer, hävd, funktioner, morfologi eller annan negativ påverkan.

| Kod | Klartext |
|---|---|
| 1 | Typiska och karakteristiska arter |
| 2 | Strukturer |
| 3 | Hävd |
| 4 | Funktioner (hydrologi, störningar) |
| 5 | Morfologi (jordart, formationer) |
| 6 | Annan negativ påverkan |

**Kommentar – Vad ska kontrolleras**  
Motivera varför just detta bör kontrolleras.

**Metod för kontroll**  
Framåtsyftande — vilken metod BÖR användas 2027 (fältbesök, fältinventering, skrivbord, annan), inte hur du gjort hittills.

| Kod | Klartext |
|---|---|
| 1 | Fältbesök |
| 2 | Fältinventering (standardiserad metodik) |
| 3 | Skrivbord / Granska mot andra underlag |
| 4 | Annan metod |

**Kommentar – Metod**  
Kompletterande info om vald metod, t.ex. varför fältinventering behövs.

### Grupp 4 · Klart?

**Granskat**  
Ja = färdiggranskad, fälten ovan ifyllda. Påbörjat = delresultat. Nej = standardläge för ogranskade objekt.

| Kod | Klartext |
|---|---|
| 1 | Ja |
| 2 | Nej |
| 3 | Påbörjat |

---

## Del B · NV:s ursprungsfält (skrivskyddade källfält)

Lämna dessa orörda — det är bara mallens granskningsfält i Del A som ska ändras (lathunden: "Vad kan vi ändra på?").

### Naturtyp / Livsmiljötyp 1–3 / Malnaturtyp 1–3
NV:s egen kod för livsmiljötyp/naturtyp (Beskrivning_NNK_koder.pdf, NV PM NV-08177-15). Samma kodutrymme används i granskningsfälten Livsmiljötyp 1–3 när ni föreslår en annan typ.

*(247 koder — sök i webbläsaren med Ctrl+F, eller använd sökrutan på HTML-sidan.)*

| Kod | Klartext |
|---|---|
| 0 | Ospecificerad kod (0) |
| 109 | Dike/uträtat vattendrag |
| 120 | Alpina vattendrag, < 3 m |
| 121 | Alpina vattendrag, 3-6 m |
| 122 | Alpina vattendrag, vattenfall < 3 m |
| 123 | Alpina vattendrag, vattenfall 3-6 m |
| 124 | Alpina vattendrag, fors < 3 m |
| 125 | Alpina vattendrag, fors 3-6 m |
| 126 | Mindre vattendrag, < 3 m |
| 127 | Mindre vattendrag, 3-6 m |
| 128 | Mindre vattendrag, vattenfall < 3 m |
| 129 | Mindre vattendrag, vattenfall 3-6 m |
| 130 | Mindre vattendrag, fors < 3 m |
| 131 | Mindre vattendrag, fors 3-6 m |
| 132 | Mindre vattendrag, sten- och blockrika partier < 3m |
| 133 | Mindre vattendrag, sten- och blockrika partier 3-6 m |
| 134 | Mindre vattendrag, sten- och blockrika forssträckor < 3 m |
| 135 | Mindre vattendrag, sten- och blockrika forssträckor 3-6 m |
| 1000 | Marint vatten |
| 1110 | Sublittorala sandbankar |
| 1117 | Sublittorala sandbankar - Med dominans av ålgräs/marina |
| 1118 | Sublittorala sandbankar - Med dominans av makroalgsvegetation |
| 1119 | Sublittorala sandbankar - Fri från vegetation |
| 1130 | Estuarier |
| 1137 | Estuarier - Med dominans av ålgräs/marina kärlväxter |
| 1138 | Estuarier - Med dominans av makroalgsvegetation |
| 1139 | Estuarier - Fri från vegetation |
| 1140 | Blottade ler- och sandbottnar |
| 1147 | Blottade ler- och sandbottnar - Med dominans av ålgräs/marina |
| 1150 | Laguner |
| 1152 | Laguner - Lagunartade vikar |
| 1153 | Laguner - Flada på landhöjningskust |
| 1154 | Laguner - Glo eller gloflada på landhöjningskust |
| 1157 | Laguner - Med dominans av ålgräs/marina kärlväxter |
| 1158 | Laguner - Med dominans av makroalgsvegetation |
| 1160 | Vikar och sund |
| 1167 | Vikar och sund - Med dominans av ålgräs/marina kärlväxter |
| 1168 | Vikar och sund - Med dominans av makroalgsvegetation |
| 1169 | Vikar och sund - Fri från vegetation |
| 1170 | Rev |
| 1171 | Rev - Biogent rev, mussel eller ostronbank |
| 1172 | Rev - Biogent rev, korallogent (ögonkorall) |
| 1173 | Rev - Biogent rev, krusta (kalkalgskrusta/märlbäddsbotten) |
| 1174 | Rev - Geogent rev 0-30 meter (berg/blocksubstrat) |
| 1175 | Rev - Geogent rev > 30 meter (berg/blocksubstrat) |
| 1177 | Rev - Med dominans av ålgräs/marina kärlväxter |
| 1178 | Rev - Med dominans av makroalgsvegetation |
| 1180 | Submarina strukturer orsakade av utläckande gas |
| 1181 | Submarina strukturer orsakade av utläckande gas - Bubbelrev |
| 1182 | Submarina strukturer orsakade av utläckande gas - |
| 1210 | Driftvallar |
| 1220 | Sten- och grusvallar |
| 1230 | Havsklippor |
| 1231 | Havsklippor - Kalkrika klippor |
| 1232 | Havsklippor - Silikatrika klippor |
| 1310 | Glasörtsstränder |
| 1330 | Salta strandängar |
| 1610 | Åsöar i Östersjön |
| 1620 | Skär i Östersjön (endast komplexkod) |
| 1621 | Skär i Östersjön - Terrester del |
| 1630 | Strandängar vid Östersjön |
| 1631 | Strandängar vid Östersjön - Ishyvlade |
| 1640 | Sandstränder vid Östersjön |
| 1650 | Smala vikar i Östersjön |
| 1820 | Obestämd sten-/sandstrand i Östersjön (1220/1640) |
| 1830 | Osäkra ler- eller sandsediment/ blottade bottnar |
| 1950 | Icke-natura strand |
| 2100 | Öppna kustdyner vid Atlant- och Östersjökusten |
| 2110 | Fördyner |
| 2120 | Vita dyner |
| 2130 | Grå dyner |
| 2140 | Risdyner |
| 2170 | Sandvidedyner |
| 2180 | Trädklädda dyner |
| 2181 | Trädklädda dyner - Torr dynskog |
| 2182 | Trädklädda dyner - Dynsumpskog |
| 2190 | Dynvåtmark |
| 2300 | Obestämd sanddominerad mark i inlandet (2320/2330) |
| 2320 | Rissandhedar |
| 2330 | Grässandhedar |
| 2920 | Sanddominerad, icke-natura naturtyp |
| 3000 | Vatten |
| 3100 | Sjö |
| 3110 | Näringsfattiga slättsjöar |
| 3130 | Ävjestrandsjöar |
| 3140 | Kransalgsjöar |
| 3150 | Naturligt näringsrika sjöar |
| 3160 | Myrsjöar |
| 3200 | Vattendrag |
| 3210 | Större vattendrag |
| 3211 | Större vattendrag - Vattenfall |
| 3212 | Större vattendrag - Forssträckor |
| 3213 | Större vattendrag – Sten- och blockrika partier |
| 3214 | Större vattendrag – Sten- och blockrika forssträckor |
| 3220 | Alpina vattendrag |
| 3221 | Alpina vattendrag - Vattenfall |
| 3222 | Alpina vattendrag - Forssträckor |
| 3260 | Mindre vattendrag |
| 3261 | Mindre vattendrag - Flytbladstyp |
| 3262 | Mindre vattendrag - Fontinalistyp |
| 3263 | Mindre vattendrag - Vattenfall |
| 3264 | Mindre vattendrag - Forssträckor |
| 3265 | Mindre vattendrag – Sten- och blockrika partier |
| 3266 | Mindre vattendrag – Sten- och blockrika forssträckor |
| 3268 | Ospecificerad kod (3268) |
| 3900 | Icke-natura sjö |
| 3920 | Icke-natura sjö, småvatten i odlingslandskapet |
| 3942 | Icke-natura sjö, oliogotrof sprickdalssjö |
| 3960 | Icke-natura vattendrag - Alpint |
| 3999 | Icke-natura vattendrag - Ej alpint |
| 4000 | Rishedar, gräshedar och videbuskmarker |
| 4010 | Fukthedar |
| 4030 | Torra hedar |
| 4060 | Alpina hedar |
| 4080 | Alpina videbuskmarker |
| 4810 | Obestämd torr-frisk hed/gräsmark nedanför trädgränsen |
| 4811 | Obestämd fuktig-blöt hed/gräsmark/myrmark nedanför trädgränsen |
| 4812 | Obestämd torr-frisk hed/gräsmark ovanför trädgränsen |
| 4813 | Obestämd fuktig-blöt hed/gräsmark/myrmark ovan trädgränsen |
| 4880 | Obestämd videbuskmark/högörtäng ovanför trädgränsen (4060/6430) |
| 5130 | Enbuskmarker |
| 5131 | Enbuskmarker - Enbuskmark på hed |
| 5132 | Enbuskmarker - Enbuskmark på kalkgräsmark |
| 5133 | Enbuskmarker - Naturlig enbuskmark vid kust |
| 6000 | Gräsmarker, substratdominerade gräsmarker och alluviala gräsmarker |
| 6110 | Basiska berghällar |
| 6120 | Sandstäpp |
| 6150 | Alpina silikatgräsmarker |
| 6170 | Alpina kalkgräsmarker |
| 6210 | Kalkgräsmarker |
| 6211 | Kalkgräsmarker - Viktiga orkidélokaler |
| 6230 | Stagg-gräsmarker |
| 6270 | Silikatgräsmarker |
| 6280 | Alvar |
| 6283 | Prekambriska kalkhällmarker |
| 6410 | Fuktängar |
| 6411 | Fuktängar - Kalkfuktäng |
| 6412 | Fuktängar – Fuktäng på surare jordar |
| 6413 | Fuktängar - Ishyvlade |
| 6430 | Högörtängar |
| 6450 | Svämängar |
| 6451 | Svämängar - Ishyvlade |
| 6510 | Slåtterängar i låglandet |
| 6520 | Höglänta slåtterängar |
| 6530 | Lövängar |
| 6830 | Obestämd naturlig högörts-/ översvämnings-/ alluvial äng |
| 6910 | Öppen kultiverad gräsmark |
| 6911 | Öppen kultiverad betesmark |
| 6912 | Öppen kultiverad slåtteräng |
| 6913 | Trädbärande kultiverad betesmark |
| 6914 | Trädbärande kultiverad slåtteräng |
| 6917 | Betad skog |
| 6918 | Trädbärande kultiverad gräsmark |
| 6930 | Åker |
| 6960 | Öppen icke-naturanaturtyp |
| 6999 | Exploaterad mark |
| 7000 | Osäker våtmark |
| 7110 | Högmossar |
| 7111 | Högmossar - Öppna mosseplan |
| 7120 | Skadade högmossar |
| 7130 | Terrängtäckande mossar |
| 7140 | Öppna mossar och kärr |
| 7141 | Öppna mossar och kärr - Svagt välvda mossar |
| 7142 | Öppna mossar och kärr - Kärr och gungflyn |
| 7143 | Öppna mossar och kärr - Hävdade svagt välvda mossar, kärr och |
| 7160 | Källor och källkärr |
| 7210 | Agkärr |
| 7220 | Kalktuffkällor |
| 7230 | Rikkärr |
| 7231 | Rikkärr - Trädklädda och videbevuxna (krontäckning 30-100 %) |
| 7232 | Rikkärr - Öppna hävdade (krontäckning 0-30 %) |
| 7233 | Rikkärr - Öppna (krontäckning 0-30%) |
| 7240 | Alpina översilningskärr |
| 7310 | Aapamyrar |
| 7320 | Palsmyrar |
| 7810 | Obestämd källa/källkärr (7160/7220) |
| 7820 | Obestämd öppet rikkärr/annan öppen myr (7232/7233/7140) |
| 7830 | Obestämd öppen myr, naturanaturtyp |
| 7930 | Torvtäkt |
| 7999 | Våtmark, icke-naturanaturtyp |
| 8000 | Osäker substratmark |
| 8110 | Silikatrasmarker |
| 8120 | Kalkrasmarker |
| 8210 | Kalkbranter |
| 8220 | Silikatbranter |
| 8230 | Hällmarkstorräng |
| 8231 | Hällmarkstorräng - Hällmarkstorrängstyp |
| 8232 | Hällmarkstorräng - Ej hävdberoende typ |
| 8240 | Karsthällmarker |
| 8310 | Grottor |
| 8330 | Havsgrottor, helt eller delvis under vattenytan |
| 8340 | Glaciärer |
| 8810 | Obestämd silikat/basisk rasmark (8110/8120) |
| 8820 | Obestämd silikat/kalkrik klippvegetation (8210/8220) |
| 8840 | Obestämd hällmark basisk/silikat (6110/8230) |
| 8900 | Öppna substratmarker, icke-naturanaturtyp |
| 8920 | Gles hällmarkstallskog, <30% krontäckning |
| 8949 | Blekemark |
| 9000 | Skog |
| 9005 | Taiga - Kalkbarrskog |
| 9006 | Taiga - Sumpskog |
| 9008 | Taiga - Kalmark/glest beskogad mark med mycket död ved efter |
| 9009 | Taiga - Naturliga successionsstadier efter störning |
| 9010 | Taiga |
| 9020 | Nordlig ädellövskog |
| 9030 | Landhöjningsskog |
| 9040 | Fjällbjörkskog |
| 9050 | Näringsrik granskog |
| 9060 | Åsbarrskog |
| 9061 | Åsbarrskog - Örtrik talltyp |
| 9062 | Åsbarrskog - Örtrik grantyp |
| 9070 | Trädklädd betesmark |
| 9071 | Trädklädda betesmarker - Ekhagar |
| 9072 | Trädklädda betesmarker - Ädellövskogdominerade |
| 9080 | Lövsumpskog |
| 9110 | Näringsfattig bokskog |
| 9130 | Näringsrik bokskog |
| 9160 | Näringsrik ekskog |
| 9161 | Näringsrik ekskog - Ek-avenbokskog |
| 9162 | Näringsrik ekskog - Ek-hassellund |
| 9170 | Torr ekskog |
| 9180 | Ädellövskog i branter |
| 9190 | Näringsfattig ekskog |
| 9740 | Skogbevuxen myr (91D0) |
| 9750 | Svämlövskog (91E0) |
| 9760 | Svämädellövskog (91F0) |
| 9801 | Osäker lövskog |
| 9810 | Osäker Taiga/ickenatura skog |
| 9820 | Obestämd ädellövskog (9020/9850/9860) |
| 9830 | Obestämd näringsrik granskog/västlig taiga (9050/9010) |
| 9840 | Obestämd svämskog (9750/9760) |
| 9841 | Obestämd lövsumpskog/ skogbevuxen myr (9080/9740) |
| 9842 | Obestämd lövsumpskog/ skogbevuxen myr/ trädklädda rikkärr |
| 9843 | Obestämd skogbevuxen myr/ Taiga (9740/9010) |
| 9850 | Obestämd bokskog (9110/9130) |
| 9860 | Obestämd ekskog (9160/9190) |
| 9870 | Osäker skogbevuxen myr – icke naturanaturtyp |
| 9900 | Ickenatura-skog |
| 9903 | Icke-natura-skog, barrskog |
| 9905 | Icke-natura-skog, blandskog (lövblandad barrskog) |
| 9906 | Icke-natura-skog, triviallövskog |
| 9907 | Icke-natura-skog, ädellövskogar |
| 9908 | Icke-natura-skog, triviallövskog med ädellövinslag |
| 9909 | Icke-natura-skog, kalkbarrskog |
| 9915 | Icke-natura-skog, sandbarrskog |
| 9925 | Icke-natura-skog, fuktig/blöt mark |
| 9940 | Icke-natura-skog, gles fjällbarrskog |

### Naturtypsstatus
NV:s status för naturtypsbedömningen (Handledning NNK, tabell 6).

| Kod | Klartext |
|---|---|
| 1 | Fullgod Natura-naturtyp |
| 2 | Icke fullgod Natura-naturtyp |
| 3 | Utvecklingsmark, icke Natura-naturtyp |
| 4 | Övrigt, icke Natura-naturtyp |
| 5 | Ej bedömd status |

### Karteringsstatus
Hur senaste karteringen gjordes (Handledning NNK, tabell 7).

| Kod | Klartext |
|---|---|
| 1 | Ej granskad |
| 2 | Granskad vid skrivbordet |
| 3 | Besökt i fält |
| 4 | Inventerad i fält |
| 5 | Åtgärdas |

### Komplex
NV:s kod för sammansatta naturtyper (komplexkoder) — förekommer bara för dessa sex kombinationer.

| Kod | Klartext |
|---|---|
| 1130 | Estuarier |
| 1160 | Vikar och sund (1110, 1140, 1170, 1610, 1620) |
| 1610 | Åsöar i Östersjön – förekommer endast som komplexkod |
| 1620 | Skär i Östersjön – förekommer endast som komplexkod |
| 7110 | Högmossar |
| 7310 | Aapamyrar |

### Förändringsorsak
NV:s kod för varför en tidigare bedömning ändrats.

| Kod | Klartext |
|---|---|
| 1 | Rättning av felaktig kartering |
| 2 | Faktisk förändring av bevarandestatus/naturtypsareal |
| 3 | Komplettering |

### Ursprung
NV:s kod för varifrån uppgiften ursprungligen kommer.

| Kod | Klartext |
|---|---|
| 1 | BIDOS |
| 2 | NNK |
| 3 | BIDOS Sammanslagning |
| 4 | BIDOS + NNK |

---

## Del C · Datering och länets stödfält

Visas i popupens avsnitt *Naturtyp (NNK-data)* eller som filtrerbara kolumner. Dateringsfälten kommer från NNK Ajourhålla. Övriga fält räknas fram av länets egen pipeline (`jobbdator_koppla_nnk_skyddskategori.py` → `forbered_gdb_for_publicering.py`) varje gång lagret byggs om. Lämna dem orörda.

### Startdatum / Slutdatum senaste inventering
`habitat_period_lastdata_start` / `habitat_period_lastdata_end` · datum, visas som årtal i popupen  
Slutdatum är när naturtypen senast bedömdes, startdatum gången före. Vid en faktisk förändring ska datumen avgränsa perioden då förändringen skedde (Handledningen, bilaga 1). Fälten är nya och tomma för nästan alla ytor. **Uppdatera framför allt slutdatum när du granskar** — det är det enda sättet att besvara FAQ fråga 4 om hur aktuell bedömningen är. Motsvarar blankettens *År för senaste bedömning*.

### Bevarandeplan, fastställd (år)
`bevarandeplan_ar` · heltal · skrivskyddat  
Året då bevarandeplanen för Natura 2000-området fastställdes, hämtat ur `bevarandeplan_platser.csv`. Tomt om det inte finns någon bevarandeplan i underlaget. Visar hur gammal bevarandeplanens bedömning är — kontrollera alltid om den fortfarande stämmer.

### Prioklass NNK (P1-P4)
`prio` · text · skrivskyddat · filtrerbart i webbGIS  
Objektets prioritetsklass för granskningen, enligt arbetsplanen avsnitt 5.2. Hämtas ur `nnk_prioklass.csv`.

| Kod | Kriterium | Insats 2026 |
|---|---|---|
| P1 | ≥ 20 ha hävdberoende eller ≥ 5 ha sällsynt livsmiljötyp (40 objekt) | Full skrivbordsgranskning |
| P2 | ≥ 20 ha terrester livsmiljötyp eller ≥ 5 ha osäker/obestämd (43 objekt) | Skrivbordsgranskning om tid finns, annars 2027 |
| P3 | Övriga objekt med terrester livsmiljötyp (108 objekt) | 2027 |
| P4 | Ingen terrester livsmiljötyp — rent limniska/marina (6 objekt) | Ingen insats, medvetet nedprioriterat |

### Batch (S/A/B/C/D)
`batch` · text · skrivskyddat · filtrerbart i webbGIS  
Vilken granskningsbatch objektet tillhör enligt arbetsplanens bilaga 2. Bara de 40 P1-objekten har en batch, övriga är tomma. Hämtas ur kolumnen `batch` i `nnk_prioklass.csv`.

| Kod | Batch | Uppgift |
|---|---|---|
| S | Storobjekt (Skärgårdsreservaten, Nynäs) | C2.1 |
| A | Kust och skärgård | C3.1 |
| B | Ängs- och hagmark inland | C4.1 |
| C | Våtmark och vattendrag | C5.1 |
| D | Skog och ädellöv | C6.1 |

### Hävdberoende livsmiljötyp
`havdberoende` · text Ja/Nej · skrivskyddat · filtrerbart i webbGIS  
Ja om ytans naturtyp är hävdberoende enligt arbetsplanens bilaga 3: 1630, 1631, 5130, 5133, 6110, 6210, 6230, 6270, 6280, 6410, 6412, 6430, 6510, 6520, 8230, 8231, 8232, 9070, 9071, 9072.

### Sällsynt livsmiljötyp i länet
`sallsynt` · text Ja/Nej · skrivskyddat · filtrerbart i webbGIS  
Ja om ytans naturtyp har mindre än 50 ha total karterad areal inom länets Natura 2000-områden (marina koder undantagna), enligt NNK-statistiken 2026-01-20: 1220, 1620, 1640, 2181, 3260, 4030, 5130, 5133, 6110, 6210, 6230, 6280, 6430, 7110, 7230, 7231, 8210, 8220, 8231, 8232, 9006, 9060, 9072, 9110, 9162, 9180, 9190, 9750. Listan räknas om med `nnk_kunskapslage.py` när ett nytt statistikuttag kommer.

### Typiska arter i Artportalen
`typarter_antal` · heltal · `typarter` · text · `typarter_senaste_ar` · heltal · skrivskyddade · filtrerbara i webbGIS  
Hur många av ytans **typiska arter** (T-arter för naturtypen i [typiska arter](typiska-arter.html)) som har fynd i Artportalen inom ytan, vilka de är och året för det senaste fyndet. Räknas fram av `artportalen_typiska_arter.py` (standard: fynd från 2010, koordinatnoggrannhet ≤ 100 m, P1-objekten). **0** = ytan söktes men inga fynd. **Tomt** = ytan söktes inte, eller naturtypen saknar artlista. Fynd talar för gott tillstånd, men inga fynd betyder oftast bara att ingen har letat. Skyddsklassade fynd ingår inte.

### TUVA — ängs- och betesmarksinventeringen
Tio fält, alla skrivskyddade och bara i ytlagret. Hämtas ur `tuva_for_granskning.csv` (`nnk_tuva.py`, TUVA-uttag 2026-08-21, senaste inventering per objekt). Ytan kopplas till det TUVA-objekt som täcker mest av den, med samma tröskel som för sitecode: minst 1 % av ytan eller 0,25 ha. Tomt = ingen träff. Används i R7A tillsammans med hävdfälten från skiftena, se [metodiken](metodik.html) avsnitt 5. Visas i popupens avsnitt *Hävd enligt jordbruksskiften och TUVA*.

| Fält | Typ | Innehåll |
|---|---|---|
| `tuva_objekt_id` | text | TUVA:s fält-ID, t.ex. "42B-QEP". Objektrapport: `https://etjanst.sjv.se/tuvaut/?f=&id=<fält-ID>` |
| `tuva_andel_overlapp` | heltal | Hur stor del av NNK-ytan (%) som täcks av TUVA-objektet |
| `tuva_antal_objekt` | heltal | Antal TUVA-objekt som överlappar ytan över tröskeln. Fler än 1: kontrollera de andra i TUVA |
| `tuva_inv_ar` | heltal | År för senaste inventeringen. Äldre än 15 år räknas inte som aktuellt underlag (R7A) |
| `tuva_havdstatus` | text | Dominerande hävdklass med andel: *Välhävdad*, *Svagt hävdad* eller *Ingen hävd* (lika andelar ger den sämre). *Ohävdad (restaurerbar)* = markslag Restaurerbar, *Ej aktuell* = objektet är inte längre ängs- eller betesmark |
| `tuva_havdregim` | text | Markslag: *Bete*, *Slåtter (äng)*, *Restaurerbar* eller *Ej aktuell*, med hävdform om den är angiven (möjlig äng, skogsbete, fäbodbete) |
| `tuva_igenvaxning` | text | *Igenväxt (ej aktuell)*, *Restaurerbar*, eller igenväxningens andel av busk- och trädskiktet: *Tydlig* (≥ 30 %), *Viss* (1–29 %), *Ingen*. *Ej angiven* för de flesta objekt från 2000-talets första inventering, som saknar fältet |
| `tuva_naturtyp` | text | Natura-naturtyper i hela TUVA-objektet med areal, störst först, t.ex. "6270 (3,98 ha), 6410 (0,15 ha)" |
| `tuva_paverkan` | text | Produktionshöjande åtgärder (gödsling m.m.) med andel av objektet, tillskottsutfodring, upplag, täkt. *Ingen angiven* om inget är noterat |
| `tuva_negativ` | text | *Ja* om TUVA har en negativ notering: dominerande hävdklass *Ingen hävd*, *Ohävdad (restaurerbar)* eller *Ej aktuell*, eller igenväxning *Tydlig*/*Igenväxt*. Annars *Nej*. Finns för att webbGIS-filtret *TUVA ohävdad/igenväxande* ska bli ett enda villkor. Tillagt 2026-10-02 |

### SkötselDOS — utförd hävd och uppföljning
Sju fält, alla skrivskyddade och bara i ytlagret. Hämtas ur `skotseldos_for_granskning.csv` (`nnk_skotseldos.py`, Metrias SkötselDOS-uttag 2026-10-01). Tomt = ingen träff. Används i R7A, se [metodiken](metodik.html) avsnitt 5. Visas i popupens avsnitt *Hävd enligt jordbruksskiften och TUVA*.

| Fält | Typ | Innehåll |
|---|---|---|
| `skdos_havd_typ` | text | *Bete*, *Slåtter* eller *Bete och slåtter*: utförda åtgärder (löpande skötsel/drift, status Genomförd, Avslutad eller Påbörjad) som överlappar ytan med minst 1 % eller 0,25 ha. Åtgärder som ritats på hela reservatet (≥ 200 ha) och transporter, stängsel och liknande räknas inte. 486 ytor |
| `skdos_havd_senaste_ar` | heltal | Senaste året med bete eller slåtter. SkötselDOS har inget datumfält, så året tas ur åtgärdens namn ("Bete Lindön 2017"). Tomt om inget år står i namnet (125 av ytorna) |
| `skdos_havd_antal_ar` | heltal | Antal olika år med bete eller slåtter |
| `uppf_punkter_bedomda` | heltal | Antal uppföljningspunkter (målindikatorer för naturtyper) inom ytan med bedömd måluppfyllelse. 101 ytor |
| `uppf_andel_bra` | heltal | Andel av punkterna (%) med måluppfyllelse *Bra* |
| `uppf_antal_dalig` | heltal | Antal punkter med måluppfyllelse *Dålig*. 17 ytor har minst en |
| `uppf_senaste_ar` | heltal | År för den senaste bedömda punkten (2015–2022) |

### Floraväkteri (Artportalen)
Tio fält, alla skrivskyddade, heltal utom `fv_arter` och `fv_forsamring`, och bara i ytlagret. Hämtas ur `floravakteri_for_granskning.csv` (`nnk_floravakteri.py`, hämtat 2026-10-01 ur SLU:s publika SOS-tjänst). Underlaget är Floraväktarnas rapporter i Artportalen (projekten *Floraväkteri Sverige* och *Arkiv Floraväktarlokaler*): återkommande besök på lokaler för rödlistade arter och arter i habitatdirektivet. En rapport räknas till ytan om punkten ligger inom den och koordinatnoggrannheten är högst 100 m. Skyddsklassade fynd ingår inte — enligt Länsstyrelsens floraväktarsamordning gäller det bara guckusko, vars enda lokal ligger utanför N2000 och naturreservat. Kommentarerna (Artportalens fält *Kommentar*) är publika och ingår, vilket `fv_anm_havd` bygger på. Tomt = ingen rapport. 290 ytor inom Natura 2000 har minst en rapport. Visas i popupens avsnitt *Floraväkteri (Artportalen)*.

| Fält | Typ | Innehåll |
|---|---|---|
| `fv_antal_arter` | heltal | Antal arter med floraväktarrapport i ytan |
| `fv_antal_rapporter` | heltal | Antal rapporter, alla år |
| `fv_senaste_ar` | heltal | År för den senaste rapporten |
| `fv_hotade_arter` | heltal | Antal arter i kategori CR, EN eller VU |
| `fv_bilaga2_arter` | heltal | Antal arter i habitatdirektivets bilaga 2 |
| `fv_ej_aterfunna` | heltal | Antal arter där senaste rapporten är *ej återfunnen* |
| `fv_minskande` | heltal | Antal arter där senaste räknade antal är under hälften av det första (samma enhet, minst två räknade besök) |
| `fv_anm_havd` | heltal | Antal rapporter vars kommentar nämner igenväxning, upphört bete, sly o.d. Enkel textsökning, läs kommentaren innan du drar slutsatser |
| `fv_arter` | text | Arterna med rödlistekategori, hotade först, t.ex. "finnögontröst (EN); sen fältgentiana (VU); …". Avkortad till 250 tecken |
| `fv_forsamring` | text | *Ja* om `fv_ej_aterfunna`, `fv_minskande` eller `fv_anm_havd` är större än 0, annars *Nej*. Finns för att webbGIS-filtret *Floraväkteri: försämring* ska bli ett enda villkor. Tillagt 2026-10-02 |

### Laserdata och diken
Elva fält, alla skrivskyddade, heltal utom de två textfälten, och bara i ytlagret. Hämtas ur `laser_for_granskning.csv` (`nnk_laser.py`). Laserfälten kommer från Skogsstyrelsens Skogliga grunddata, 10 m-raster skattade ur laserskanning: första nationella skanningen (Södermanland 2010–2012) och Laserdata Skog (2020, på några ställen 2023). Bara pixlar som ligger helt inom ytan räknas. Laserfälten finns för skogstyperna (R7 grupp B, inklusive 9740 och 9750), dikesfälten för skogstyperna och myrarna 7110–7231. Tomt = ytan ingår inte, eller är för liten (färre än tre hela pixlar). Används i R7B och R7C, se [metodiken](metodik.html) avsnitt 5. Visas i popupens avsnitt *Skog (laserdata)*.

| Fält | Typ | Innehåll |
|---|---|---|
| `laser_hojd_medel` | heltal | Grundytevägd medelhöjd, medel för ytan, senaste skanningen (dm, 185 = 18,5 m) |
| `laser_volym_medel` | heltal | Virkesvolym, senaste skanningen (m³sk/ha) |
| `laser_grundyta_medel` | heltal | Grundyta, senaste skanningen (m²/ha) |
| `laser_diameter_medel` | heltal | Grundytevägd medeldiameter, senaste skanningen (cm) |
| `laser_skanning_ar` | heltal | År för senaste skanningen. Förändringar efter det året syns inte i laserfälten |
| `laser_hojdforandring_medel` | heltal | Medelhöjden i senaste skanningen minus den äldsta (dm). Negativt = sänkning. Normal tillväxt ger några dm till 1–2 m |
| `laser_andel_sankt` | heltal | Andel av ytan (%) där höjden sjunkit mer än 5 m mellan skanningarna |
| `laser_forandring_period` | text | Skanningsåren som jämförs, t.ex. "2010-2020" |
| `laser_flagga` | text | *Möjlig avverkning* (minst 10 % av ytan eller 0,1 ha sänkt mer än 5 m), *Möjlig gallring* (grundytan minskat minst 3 m²/ha och 15 %, höjden inte sänkt), *Osäker (lövat/olövat)* (lövskogstyp där den äldsta skanningen var i lövat läge) eller tomt. Trösklarna är förslag |
| `diken_m_inom` | heltal | Meter dike inom ytan enligt Skogsstyrelsens AI-karterade diken (NV:s vektorversion). Alla dikestyper, även vägdiken |
| `diken_m_50m` | heltal | Meter dike i en 50 m bred zon runt ytan (utanför ytan) |

### Areal (ha)
`area_ha` · decimaltal, 2 decimaler · skrivskyddat · bara ytlagret  
Polygonens areal i hektar. Bra för att jämföra mot arealen i bevarandeplanen.

### Naturtyp (kod + klartext)
`naturtyp_kod_text` · text · skrivskyddat  
NV:s naturtypskod och namn i samma fält, t.ex. "9010 - Taiga". Själva koden (`naturtyp`) finns som egen kolumn att filtrera på.
