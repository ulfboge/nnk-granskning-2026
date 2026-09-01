# Runbook NNK/NRF 2026 — steg för steg

## Länsstyrelsen i Södermanlands län · Naturskyddsenheten · ref. 2451-2026

**Datum:** 2026-08-21  
**Omfattning:** 58 uppgifter i sju arbetspaket, 266 konkreta steg  
**Hör ihop med:** `docs/arbetsplan.md` (varför) · `kontrollrum.html` (överblick och avbockning) · `docs/metodik.md` (förvaltardialogen)

---

## Så används dokumentet

Arbetsplanen säger *varför* och *när*. Det här dokumentet säger *hur*. Varje uppgift har ett id som matchar kontrollrummet och arbetsplanen, och stegen är skrivna för att gå att följa rakt av.

Uppgifter markerade **[Handläggare]**, **[Karin]** eller **[Båda]** följer rollfördelningen i arbetsplanens avsnitt 6.1.

---

## A. Etablering och förutsättningar

*v34–v36 · 13 uppgifter*

### A1.1 · Beställ och verifiera systembehörigheter

**v34–v35** · **[Handläggare]**

1. Skicka en samlad beställning till IT/behörighetsansvarig. Lista exakt: ArcGIS Pro med NNK-tillägget, NNK Ajourhålla (läs OCH skriv — läsrättighet räcker inte), ArcGIS Enterprise-portalen, KartLitS WebbGIS, SkötselDOS, Artportalen (rapportörskonto), samverkansytan för Livsmiljötyper.
2. Ange i beställningen att det gäller regeringsuppdraget NRF, ref. 2451-2026 — det brukar korta handläggningstiden.
3. Notera datum för varje beställning i granskningsloggen. Behörighet är den enskilt vanligaste förseningsorsaken i planen.
4. Medan du väntar: allt i arbetspaket A2 och H2.1 går att göra utan behörigheter, liksom att läsa bevarandeplaner.

### A1.2 · Verifiera att NNK-utcheckning fungerar mot ett testobjekt

**v35** · **[Handläggare]** · förutsätter A1.1

1. Öppna ArcGIS Pro. Skapa ett nytt projekt: `NNK_D_2026`. Sätt kartans koordinatsystem till SWEREF 99 TM (EPSG:3006) — Map Properties → Coordinate Systems → sök 3006.
2. Anslut till NNK Ajourhålla enligt manualen på VIC Natur (vicnatur.naturvardsverket.se/nnk). Insert → Connections → Database, eller den anslutningsfil IT tillhandahåller.
3. Titta på inspelningen av hur man praktiskt uppdaterar i NNK på VIC Natur (samma sida) innan du checkar ut testobjektet. (Möte 12 aug: båda behöver den.)
4. Välj ett litet testobjekt — förslag: SE0220012 Nävsjöskogen, 5,0 ha, 1 polygon. Minimal risk om något går fel.
5. Checka ut området. Kontrollera att du får ut geometri OCH attribut, och att fälten KOMMENTAR, NNK_KOMMEN och REDIGERARE finns (de saknas i den publika versionen).
6. Gör INGEN ändring. Checka in igen direkt och verifiera att det går utan fel.
7. Notera i granskningsloggen: fungerar utcheckning ja/nej, vilken version av tillägget, eventuella felmeddelanden.

### A1.3 · Åtkomst till samverkansytan för Livsmiljötyper

**v34** · **[Handläggare]**

1. Begär åtkomst till Naturvårdsverkets samverkansyta för Livsmiljötyper.
2. Ladda hem allt under Dokument: manualer från basinventeringen och uppföljningen, handledningen för länsstyrelsernas granskning inklusive checklista, kodlistan.
3. Bokmärk menyn längst till vänster — där ligger länken till NNK-manualerna på VIC Natur.
4. Spara ned i `natura-2000: docs/underlag/` och notera nedladdningsdatum. Dokumenten uppdateras löpande under projektet.

### A2.1 · Läs handledningen och lathunden

**v34** · **[Båda]**

1. Läs `natura-2000: docs/underlag/handledning/Handledning NNK 20260703.pdf`, 26 sidor. Prioritera avsnitt 2.3 (checklistan), 3.2 (minsta karteringsenhet), 5 (attributen) och bilaga 1 (fältlistan).
2. Läs `natura-2000: docs/underlag/handledning/Lathud_granskning_WebbGIS_KartLitS_20260714.pdf`, 9 sidor. Avsnittet *Vad kan vi ändra på?* är det viktigaste i hela uppdraget.
3. Läs `docs/metodik.md` avsnitt 5 — de sex beslutsreglerna.
4. Skriv ut checklistan på sidan 9 i handledningen och ha den framme vid varje granskning.

### A2.2 · Gå igenom kodlistan

**v35** · **[Handläggare]** · förutsätter A1.3

1. Öppna `natura-2000: docs/underlag/handledning/Kodlista_NNK_20260703.xlsx` — den ger kodstruktur och undergrupper, men saknar en egen kategorikolumn.
2. Öppna i stället `natura-2000: docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx`, fliken *KODLISTA_NNK*. Filtrera kolumn H *Kategori 2026* på Gräsmark, Skog och Våtmark — det är de kategorier D-läns arbete gäller. Marina och limniska koder kan du hoppa över i år.
3. Notera undertyperna för de koder som dominerar i länet: 9010 taiga, 9070/9071/9072 trädklädd betesmark, 8230/8231/8232 hällmarkstorräng, 6270 silikatgräsmark, 1630/1631 strandäng. Undertypen syns som olika KOD-nummer inom samma familj (kolumn A) kombinerat med kolumn C *Namn, undergrupp* — kolumn B *Namn* är samma för hela familjen och skiljer inte typerna åt (9070/9071/9072 har alla `Namn` = "Trädklädd betesmark", men 9071 har `Namn, undergrupp` = "Ekhagar" och 9072 = "Ädellövskogsdominerade").
4. Lär dig skillnaden mellan de tre flaggkategorierna: *Naturanaturtyp* (livsmiljötyp), *Obestämd naturanaturtyp* (vet att det är livsmiljötyp, inte vilken) och *Osäker natura/icke-natura* (vet inte om det är livsmiljötyp alls). De kräver helt olika åtgärder. Kategorierna finns i kolumn E *Natura / icke-natura KOD* (värde 1–4) med klartext i kolumn F *Natura/ickenatura Namn*. Filen har en kolumn G till med exakt samma rubriktext (en brist i källfilen) — den innehåller bara en nyare parallell terminologi (Livsmiljötyp-varianterna) för samma fyra värden, inte en annan indelning. Värde 4, *Icke-naturanaturtyp*, är en fjärde kategori som medvetet INTE räknas som en av de tre flaggorna — den är entydig och kräver ingen bedömning.
5. Urvalet finns redan i `natura-2000: docs/nnk/nnk_kodurval_dlan.csv` (41 koder): kolumnen NATURTYPKO i `natura-2000: data/nnk/nnk_yta_med_sitecode.csv` (det faktiska NNK-uttaget för länet), filtrerat till kolumn E = 1 (Naturanaturtyp/livsmiljötyp, se steg 4) och Kategori 2026 = Gräsmark/Skog/Våtmark (se steg 2). Kolumnerna KOD, Namn, Namn_undergrupp, Kategori_2026 samt antal polygoner och areal per kod i länet — uppdatera filen om ett nytt uttag ändrar bilden.

### A2.3 · Installera KartLitS GIS-mall och testa den

**v35** · **[Handläggare]** · förutsätter A1.2

1. Packa upp `natura-2000: docs/underlag/handledning/KartLits_NNK_GIS_mall_v_2.zip` till en lokal projektmapp.
2. Mallen innehåller `KartLits_NNK_granskning.gdb` med tre tomma lager i SWEREF 99 TM: NNK_naturaobjekt_yta, _lin och _pkt. Plus tre .lyrx-filer med färdig symbologi.
3. Lägg till lagren i ArcGIS Pro-projektet och applicera .lyrx-filerna: högerklick på lagret → Symbology → Import from Layer File.
4. Granska attributtabellen för NNK_naturaobjekt_yta. Fälten du kommer använda: `tillstand`, `procent_gott`, `procent_ej_gott`, `procent_osaker`, `justering`, `utbredning`, `livsmiljötyp1–3`, `malnaturtyp1–3`, `kontroll1–3`, `metod`, `granskat`, `faltinventerare`, `egen_bet`, `habitat_period_lastdata_start`/`_end` samt fyra kommentarsfält.
5. Testa att lägga till en dummy-post och fylla i fälten, så att du känner igen dem i WebbGIS-gränssnittet. Radera den sedan.

### A2.4 · Hämta fastställda vägledningar — kontrollera status

**v36** · **[Handläggare]**

1. Gå till Naturvårdsverkets sida *Natura 2000 i Sverige* → vägledningar för naturtyper.
2. Ladda hem vägledningarna för de livsmiljötyper som finns i D-län. Prioritera 9010, 9070, 8230, 6270, 6410, 1630, 7110, 7140, 7230, 9080, 9190.
3. Kontrollera för varje: är den FASTSTÄLLD eller på REMISS? FAQ fråga 10 säger att en remissversion inte ska användas som grund för bedömning.
4. Notera i granskningsloggen vilka typer som saknar fastställd vägledning. De blockeras och ska med i planen för 2027 (uppgift F1.1) som ett eget stycke.
5. Kom ihåg: nu gällande vägledningar är från 2026 för akvatiska livsmiljötyper samt taiga (9010) och örtrik skog med gran (9050), men från 2011–2012 för övriga terrestra typer.

### A2.5 · Begär datauttag för D-län

**v35** · **[Handläggare]** · brådskande — svarstid från NV okänd

1. Mejla `Sandra.Wennberg@naturvardsverket.se` och begär ett uttag ur NNK-Ajourhålla för Södermanlands län (punkter, linjer, ytor), enligt `Manual NNK mall för granskning.pdf` steg 1.
2. Du får instruktioner via mejl för att ladda ner en zipfil med geodatabasen för uttaget.
3. Spara ner zipfilen, extrahera geodatabasen och öppna filerna i ArcGIS Pro. Kontrollera att allt ser rimligt ut (jämför gärna mot exemplet för Stockholm i manualen).
4. Detta är en extern beroende som blockerar A2.6–A2.8 och i förlängningen allt WebbGIS-baserat granskningsarbete — skicka mejlet så tidigt som möjligt, gärna samtidigt som A2.3.

### A2.6 · Kopiera in uttaget i mallen

**v37** · **[Handläggare]** · förutsätter A2.3, A2.5

1. Öppna ArcGIS Pro-projektet med både mallen (A2.3) och datauttaget (A2.5) tillagda.
2. Öppna verktyget **Append** (under Tools/Geoprocessing).
3. Under *Target Dataset*, ange mallens lager för punkter, linjer eller ytor (ett i taget). Under *Input Dataset*, ange motsvarande lager ur uttaget.
4. Under *Field Matching Type*, välj **Use the field map to reconcile field differences**. Klicka Run.
5. Spara editeringarna när alla tre lager (punkt/linje/yta) är klara.
6. Döp om domänerna i geodatabasen med prefixet `LstD` inför publiceringen, enligt manualens rekommendation.
7. **Läge 2026-09-01:** Append-steget kringgicks — granskningslagret byggdes i stället med skript (`natura-2000: deliveries/nnk_granskning_sodermanland_20260901/`, se README där). Domänerna läggs på med `forbered_gdb_for_publicering.py` — steg 1–6 ovan gäller alltså bara om Append-vägen används. Se [Publicera WebbGIS](webbgis-publicering.html), del 1.

### A2.7 · Publicera granskningslagret i portalen

**v37** · **[Handläggare]** · förutsätter A2.6

1. Ta bort de rena uttagsfilerna från projektet (de som bara användes som källa till Append) så att bara de ifyllda mallagren återstår.
2. Byt namn på de lager som ska publiceras som hostade lager — använd länskoden som prefix, t.ex. `LstD NNK granskning`.
3. Ta ställning till om vissa koder ska sållas bort, eller om bara objekt som överlappar ett Natura 2000-område ska behållas, innan publicering.
4. Klicka **Share → Web Layer** i ArcGIS Pro och publicera till Länsstyrelsens interna eller externa ArcGIS Enterprise-portal (avstäm vilken med IT/GIS-funktionen — jobbdatorns nätverksrestriktioner kan påverka vilken som går att nå från fältet).
5. **Detaljerad instruktion:** [Publicera WebbGIS](webbgis-publicering.html), del 2–4 (förberedelser i Pro, Share As Web Layer, efterarbete på item i portalen). Tjänstenamn: `LstD_NNK_Granskning` och `LstD_Skyddade_Omraden`.

### A2.8 · Skapa webbGIS från de publicerade lagren

**v37** · **[Handläggare]** · förutsätter A2.7

1. Följ Länsstyrelsernas interna vägledning *Generellt kartstöd* för hur man bygger ett webbGIS från publicerade lager (länken finns i manualen, på Länsstyrelsernas intranät).
2. Lägg till `LstD NNK granskning` och relevanta referenslager (t.ex. *NV Naturtypskartan NNK*, *NV Natura2000 områden*) i webbGIS-appen.
3. Testa redigering mot ett enskilt objekt innan du meddelar kollegan att lagret är klart att använda (jämför med rutinen i A2.3, punkt 5).
4. Vid frågor eller problem: `giampaolo.cocca@lansstyrelsen.se`.
5. **Detaljerad instruktion:** [Publicera WebbGIS](webbgis-publicering.html), del 5–7 (WebMap i Map Viewer, GK Konfigurator, test och överlämning).

### A3.1 · Avstämning med chef

**v35** · **[Handläggare]**

1. Boka 60 min med Ing-Marie, ordinarie EC naturskydd. Stefan Henriksson har slutat.
2. Ta med: `kunskapslage.html` (öppna i webbläsare — nyckeltalen finns överst) och arbetsplanens avsnitt 0.
3. Punkter att få beslut om: (1) att 2026 är ett kartläggningsår, inte ett produktionsår; (2) att marina miljöer medvetet lämnas; (3) tidsbudget 107 dagar handläggare + 61 dagar Karin; (4) att Karins 50 % faktiskt är skyddad tid; (5) vilka EC och AC som ska sitta i styrgruppen (beslut 12 aug).
4. Fråga specifikt vad som förväntas i årsredovisningen för 2026 och när texten ska vara inne.
5. Dokumentera besluten i granskningsloggen — särskilt bortvalen. De är det du kommer behöva försvara.

### A3.2 · Kartlägg förvaltaransvaret på Naturvårdsenheten

**v36** · **[Handläggare]**

**Uppdaterat 2026-08-26:** en sammanställd lista fanns redan (länsstyrelsens förvaltarlista, uttag
2026-05-27) — kolumn I *Förvaltare* i blanketten är nu automatiskt ifylld för 186 av 197 sitecodes,
se H1.1 och `natura-2000: data/forvaltare/README.md`.

1. Be Naturvårdsenheten bekräfta eller komplettera den automatiska kopplingen, snarare än att börja om från grunden.
2. Per Flodin är första rådgivare för skötselhistorik och tidigare åtgärder — fråga honom innan du jagar dokument på egen hand.
3. Prioritera att få de sju objekten med Åtgärdas-ytor täckta: SE0220129 Skärgårdsreservaten (obs: flera förvaltare, se H1.1), SE0220020 Strandstuviken, SE0220174 Marvikarna, SE0220602 Vilsta, SE0220231 Rågö, SE0220337 Storhultet, SE0220176 Tovhulta stormosse.
4. Detta är samma sak som H1.1 — gör dem i ett svep.

### A3.3 · Rollfördelning med Karin

**v35** · **[Båda]**

1. Gå igenom arbetsplanens avsnitt 6.1 tillsammans.
2. Karin tar: batch B, C och D i skrivbordsgranskningen, dataunderlag och uttag, förvaltarbokningar, eftersök av dokument, screening av naturreservat.
3. Du tar: metodik, all NNK-redigering, bedömningarna, storobjekten, planen till NV.
4. Sätt en fast veckoavstämning, 30 min måndagar. Granskningsloggen ligger (beslutat 2026-08-21) som `granskningslogg_mall.xlsx` på `G:\5_Naturvard_miljoskydd\51_skydd_omr_arter_mm\511_skydd_omr_arter\NRF\` — se A4.1.
5. Viktigt: lägg Karins arbete på avgränsade batchar som går att pausa — 50 % tid blir i praktiken ofta mindre.

### A3.4 · Anmäl er till KartLitS arbetsgrupper

**v36** · **[Handläggare]** · förutsätter A1.3

1. Maila `kartlitsN2000@naturvardsverket.se`. Anmäl er till arbetsgrupperna för skog, gräsmark och våtmark.
2. Passa på att i samma mail ställa frågorna i arbetsplanens avsnitt 10 — särskilt om storobjekten och om generaliseringar. Svaren styr hela hösten, så ju tidigare desto bättre.
3. Notera att arbetsgrupperna för akvatiska miljöer och fjäll startar hösten 2026 — de är inte relevanta för D-län i år.
4. Spara svaren i `docs/nnk/` — de är underlag till planen för 2027.

### A4.1 · Skapa arbetsstruktur för dokumentation

**v36** · **[Handläggare]**

1. Mapparna `natura-2000: docs/faltprotokoll/` och `natura-2000: data/uttag/` finns redan. Granskningsloggen förs i stället i `G:\5_Naturvard_miljoskydd\51_skydd_omr_arter_mm\511_skydd_omr_arter\NRF\granskningslogg_mall.xlsx`, fliken *Objektgranskning* — en rad per objekt: sitecode, namn, datum, vem, vad som granskats, vad som ändrats, vad som återstår, osäkerheter. (Ersatte 2026-08-21 den tidigare docs/nnk/granskningslogg.md i natura-2000 — svår att nå och skriva i från jobbdatorn. Ligger på G:-enheten, alltså utanför Git — committas aldrig.)
2. Fältdokumentation: en fil per fältdag i `natura-2000: docs/faltprotokoll/`. Fältarbetet är flyttat till 2027 (beslut 2026-08-25) — mappen står färdig men väntas inte fyllas på under 2026.
3. NNK-uttag: spara i `natura-2000: data/uttag/` med datum i filnamnet så före/efter-jämförelser går att göra. Hela mappen är gitignorad utom README.md — filerna committas inte, de är bara lokala arbetskopior.
4. Under 2026 finns ingen daglig commit-rutin kopplad till granskningsarbetet — resultatet av skrivbordsgranskningen (C1.1) hamnar i KartLitS WebbGIS-mallen och i granskningsloggen på G:-enheten, inte i något repo. Committa som vanligt när du faktiskt ändrar filer i natura-2000 eller här (dokument, analysskript, kodurval m.m.).
5. Kontrollera att `natura-2000: data/uttag/` (hela mappen, inte bara *.gpkg) och `natura-2000: data/nnk/*.gpkg` ligger i `.gitignore` — stora geodatafiler hör inte hemma i Git.
6. Diarieföring (beslut 5 aug): öppna ärenden allteftersom förfrågningar kommer in, och stäng dem när svaret är diariefört. Stäm av rutinen med diariet.

### A4.2 · Etablera rutin för NNK-uttag

**v36** · **[Handläggare]** · förutsätter A1.2

1. Dokumentera exakt hur du gör uttaget, så att det går att upprepa identiskt i v45: vilket lager, vilka fält, vilket filter, vilket format.
2. Uttaget ska innehålla minst: NOID, NATURTYP, NATURTYPKO, NATURTYPSS, KARTERINGS, FORANDRING, URSPRUNG, KOMMENTAR, NNK_KOMMEN, REDIGERARE, REDIGERATA, REDIGERATG, SKAPATDATU, MALNATUR1–3, samt de nya tillstånds- och dateringsfälten när de driftsatts.
3. Exportera som shapefile eller GPKG till `data/uttag/nnk_YYYYMMDD.gpkg`.
4. Kör `python natura-2000: scripts/analysis/koppla_omraden.py` mot uttaget för att få SITECODE på varje yta. Sätt miljövariabeln NNK_SHP till uttagets sökväg först.
5. Kör `python natura-2000: scripts/analysis/nnk_kunskapslage.py` för att uppdatera nollmätningen.

---

## C. Skrivbordsgranskning av utbredning

*v35–v46 · 7 uppgifter*

### C1.1 · Etablera granskningsrutinen

**v35** · **[Handläggare]** · förutsätter A2.1, A2.3

1. Skriv ned rutinen som en mall du kopierar per objekt i granskningsloggen (`.../NRF/granskningslogg_mall.xlsx`, fliken *Objektgranskning*).
2. Rutinen per objekt, åtta steg: (1) öppna objektet i KartLitS WebbGIS och i ArcGIS Pro mot NNK; (2) läs bevarandeplanen — vilka livsmiljötyper är utpekade, vilka är prioriterade bevarandevärden, vilka bevarandemål finns; (3) jämför bevarandeplanens typer mot vad NNK visar, notera differenser; (4) kontrollera mot aktuellt ortofoto och IR-ortofoto — syns uppenbara förändringar sedan 2012?; (5) kontrollera mot TUVA, VMI, VISS och Artportalen; (6) bedöm per yta: stämmer utbredningen — OK / justera / kontrolleras i fält / osäker; (7) notera i WebbGIS-mallen; (8) justera geometri i NNK endast där det påverkar arealen meningsfullt.
3. Minsta karteringsenhet, från handledningen tabell 9: 0,25 ha generellt, 1 ha skog icke-natura och öppen myr, 0,5 ha skog natura, 2 ha ovan trädgränsen. Minsta karteringsbredd 10 m.
4. Lägg större vikt vid gränsen mellan livsmiljötyp och icke-livsmiljötyp än vid gränser mellan olika livsmiljötyper — de senare är gradvisa och svåra att avgränsa exakt.
5. Testa rutinen på ett litet objekt först och tidsätt den. Tidsåtgången är indata till volymuppskattningen i F1.2.

### C2.1 · Batch S — storobjekten Skärgårdsreservaten och Nynäs

**v41–v46** · **[Handläggare]** · förutsätter C1.1, A3.4 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. SE0220129 Skärgårdsreservaten har 2 915 polygoner totalt, men merparten av arealen är marin och lämnas enligt FAQ f.16 (~390 marina polygoner / `1000` och `11xx`). Kvar på land: ca 2 500 polygoner (ca 1 800 ha), varav bara ~30 är ≥ 5 ha. SE0220126 Nynäs har 1 433 polygoner, nästan samtliga terrestra. Yta för yta på det terrestra är inte realistiskt.
2. Stratifiera det terrestra i ArcGIS Pro: filtrera bort marina koder, symbolisera på NATURTYPKO och sortera attributtabellen på Shape_Area fallande.
3. Hantera individuellt: alla terrestra ytor över 5 ha, alla hävdberoende ytor, alla sällsynta livsmiljötyper, alla Åtgärdas-ytor (91 i Skärgårdsreservaten).
4. Hantera gruppvis: små hällmarks-, skogs- och skärytor (`9010`, `8230`/`8231`, `1621`) med samma kod och samma bedömningsgrund. Selektera med Select By Attributes, sätt attributen i grupp, och skriv EN gemensam kommentar som anger att det är en generalisering och på vilken grund.
5. Skärgårdsreservaten har redan 198 fältkontrollerade polygoner. Filtrera fram dem (KARTERINGS 3 eller 4) och återanvänd kunskapen — gör inte om den.
6. Invänta svar från KartLitS (A3.4) på om metoden accepteras innan du kör hela vägen. Fråga 1 i arbetsplanens avsnitt 10.

### C3.1 · Batch A — kust och skärgård

**v38–v42** · **[Båda]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. Sex objekt: SE0220439 Askö, SE0220020 Strandstuviken, SE0220034 Tullgarn södra, SE0220231 Rågö, SE0220218 Stendörren, SE0220077 Ridö-Sundbyholmsarkipelagen södra. 1 692 ha terrester livsmiljötyp, varav 691 ha hävdberoende.
2. Kör granskningsrutinen C1.1 per objekt.
3. Särskilt att titta på: 1630 strandängar — hävdas de fortfarande? Strandstuviken har 15 Åtgärdas-ytor av typen 1630 och Rågö har 4.
4. Marina ytor inom objekten: rör dem inte. FAQ fråga 16.
5. Tullgarn södra har 299 ha okarterat — se C7.1.

### C4.1 · Batch B — ängs- och hagmark inland

**v35–v38** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. 16 objekt: SE0220110 Skåraviken, SE0220017 Svanviken-Lindbacke, SE0220063 Sparreholms ekhagar, SE0220118 Labro ängar, SE0220182 Segersön, SE0220150 Tåkenön, SE0220085 Gripsholms Hjorthage, SE0220363 Lindön, SE0220115 Marsviken-Marsäng, SE0220206 Floden, SE0220088 Herröknanäs, SE0220603 Jungfruvassen, SE0220344 Lövön, SE0220309 Brebol, SE0220435 Gesta, SE0220228 Ånhammarsnäset. 851 ha terrester, 684 ha hävdberoende, bara 447 polygoner.
2. Denna batch går FÖRST, medvetet: objekten är små och snabba, vilket kalibrerar rutinen och tidsuppskattningen innan de tunga batcharna.
3. Tidsätt varje objekt och notera i loggen. Siffran används i F1.2.
4. TUVA är det viktigaste sidounderlaget här — nästan allt är ängs- och betesmark.
5. Milstolpe M2 i v38: batchen klar och rutinen kalibrerad.

### C5.1 · Batch C — våtmark och vattendrag

**v42–v44** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. Sex objekt: SE0220176 Tovhulta stormosse, SE0220137 Bråtamossen, SE0220103 Pilgöljan, SE0220021 Sjösakärren, SE0220106 Fjällmossen norra, SE0220304 Kilaån-Vretaån. 378 ha terrester, varav 128 ha sällsynta typer.
2. Sällsynta typer här: 7110 högmossar (47 ha i länet), 7230 rikkärr (34 ha), 7231 rikkärr undertyp (4 ha), 3260 vattendrag (44 ha), 9750 svämskog (2,7 ha).
3. Limniska ytor: ange livsmiljötyp i befintliga ytor och linjer där förekomsten är känd, men justera INTE ytterkanter eller vattendragsgeometri. FAQ fråga 16.
4. VMI är sidounderlaget för våtmarkerna, VISS för vattendragen.
5. Fjällmossen norra har 109 fältkontrollerade polygoner — återanvänd.

### C6.1 · Batch D — skog och ädellöv

**v43–v46** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. Tio objekt: SE0220602 Vilsta, SE0220343 Askholmen, SE0220503 Fjellskäfte, SE0220217 Tore Grav, SE0220130 Lotsängsbacken, SE0220211 Ekorneberg, SE0220234 Persö, SE0220348 Tynnelsö Djurgård, SE0220507 Lundäng, SE0220438 Åsa gravfält. 393 ha terrester, 92 ha sällsynta typer.
2. Sällsynta typer: 9060 åsbarrskog (29 ha), 9072 ädellövdominerad betesmark (29 ha), 9180 ädellövskog i branter (10 ha), 4030 torra hedar (16 ha), 9110 bokskog (6 ha), 6280 alvar (6 ha).
3. För 9010 taiga: kontrollera hällmarker i anslutning — handledningen 3.1 påpekar att grundkarteringen avgränsat taiga främst inom produktiv skog, så angränsande hällmarker kan behöva justeras.
4. Kontrollera avverkningsanmälningar via Skogsstyrelsen för objekt med skogsmark — det är den vanligaste faktiska förändringen.
5. Vilsta har 6 Åtgärdas-ytor.

### C7.1 · Okarterade ytor och länssöverskridande objekt

**v44** · **[Handläggare]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. SE0220303 Båven: 4 845 ha okarterat av 6 200 ha. Det är sjöytan. Lägg INGEN tid på ytterkanterna — FAQ fråga 16 och 29. Ange livsmiljötyp i befintliga ytor om förekomsten är känd. Dokumentera i loggen att det är medvetet nedprioriterat, med hänvisning till FAQ.
2. SE0220034 Tullgarn södra: 299 ha okarterat av 2 014 ha. Kontrollera i ArcGIS Pro vad ytan består av — lägg NNK-lagret över objektsgränsen och titta på hålen.
3. Är hålet terrestert är det ett faktiskt karteringsgap. Felanmäl till `NNK-kartering@metria.se` med sitecode, en skärmbild och en kort beskrivning.
4. Är det vatten gäller samma sak som för Båven.
5. Notera resultatet i loggen — båda posterna ska med i kunskapslägesrapporten (E2.1).
6. Länssöverskridande objekt: arealer utanför länsgräns tillfaller **rapporterande län** enligt NV:s NNK-statistik (fliken *Beskrivning*). Det är samma sak som förklarar 0,2 %-avvikelsen i arbetsplanens bilaga 3. I D-län är Tullgarn södra (SE0220034, mot Stockholms län) det tydligaste fallet; Ridö-Sundbyholmsarkipelagen södra (SE0220077) gränsar mot Västmanland.
7. Kontakta NNK/NRF-handläggaren på det andra länet och kom överens om vem som bedömer vilken del. Vet du inte vem: maila `kartlitsN2000@naturvardsverket.se`. Det är inte Metrias sak — `NNK-kartering@metria.se` är bara för karteringsgap.
8. Dokumentera vilket län som är rapporterande och hur ni delar arbetet. (Åtgärd från möte 20 aug.)

---

## D. Tillståndsbedömning i NNK

*v40–v50 · 9 uppgifter*

### D1.1 · Bevaka driftsättningen av de nya NNK-attributen

**v39–v40** · **[Handläggare]**

1. FAQ fråga 30: nya attribut för tillståndsbedömning införs sommaren 2026, driftsättning planerad till slutet av september.
2. Maila `kartlitsN2000@naturvardsverket.se` i v39 och be om bekräftat datum samt när utbildning ges.
3. Kontrollera i ArcGIS Pro när attributen dykt upp: checka ut testobjektet igen och titta efter fälten för tillstånd i procent.
4. Blir det försenat: fyll v40–v43 med arbetspaket C i stället. Ingen tid går förlorad, bedömningarna dokumenteras i fältprotokoll och granskningslager under tiden.

### D1.2 · Gå igenom den nya attributlistan

**v40** · **[Båda]** · förutsätter D1.1

1. Läs igenom vad som ändrats. Två saker är viktiga: fältnamnen byter från *natura-naturtyp* till *livsmiljötyp*, och tillstånd anges nu som procentuell andel av ytan.
2. Konsekvensen av procentandelen: du behöver INTE längre dela upp en yta för att ange olika tillstånd. Det sparar mycket geometriarbete.
3. Namnbytet sker automatiskt — det du redan lagt in påverkas inte.
4. Uppdatera granskningsrutinen och fältprotokollmallen med de nya fälten.

### D1.3 · Delta i NV:s utbildning

**v40–v41** · **[Båda]** · förutsätter D1.1

1. Anmäl båda till utbildningen så snart datum finns.
2. Ta med konkreta frågor från arbetet: storobjektsmetoden, generaliseringar, hur procentandelarna ska tolkas för mosaikartade ytor.
3. Anteckna och lägg i `docs/nnk/`. Notera särskilt allt som avviker från handledningen från juli.

### D2.1 · Registrera tillstånd där kunskapen redan finns

**v41–v48** · **[Båda]** · förutsätter D1.2 · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

1. Börja med de 277 ytorna som har karteringsstatus 3 eller 4 (fältdata) men naturtypsstatus 5 (ej bedömd). Det är hela uppdragets snabbaste vinst — kunskapen finns, den registrerades aldrig.
2. Hitta dem: i ArcGIS Pro, Select By Attributes på NNK-lagret: `KARTERINGS IN ('3 - Besökt i fält','4 - Inventerad i fält') AND NATURTYPSS LIKE '5%'`.
3. Leta upp underlaget bakom varje: uppföljningsprotokoll, ÄoB-blankett, basinventeringsprotokoll. Karin söker parallellt i H4.1.
4. Ta därefter de 482 fullgoda och 336 icke fullgoda — kontrollera att bedömningen fortfarande är rimlig och komplettera med procentandelar och datering.
5. Checka ut objektet i ArcGIS Pro, sätt attributen, kör toolboxen, checka in. Arbeta objekt för objekt, inte spritt — utcheckning är områdesbaserad.

### D2.2 · Dokumentera grunden för varje bedömning

**v41–v48** · **[Båda]** · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

1. Varje redigerad yta ska ha KOMMENTAR ifylld. Formatet: vad bedömningen bygger på, vem som gjort den, och när.
2. Exempel: *"Tillstånd bedömt utifrån uppföljning 2023-06 (protokoll i SkötselDOS) samt uppgift från NN, förvaltare, 2026-09-24. Hävd pågår men otillräcklig i södra delen."*
3. Fyll även Slutdatum senaste inventering (`habitat_period_lastdata_end`) — det är enda sättet att besvara FAQ fråga 4:s krav på aktualitet.
4. Utan detta är bedömningen inte spårbar, och kan inte redovisas i kunskapslägesrapporten.

### D2.3 · Registrera aktivt även oförändrat tillstånd

**v41–v48** · **[Båda]** · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

1. Är tillståndet oförändrat sedan tidigare bedömning — registrera det ändå, med grund och datum. FAQ fråga 9: "oförändrat" är också ett svar.
2. Skillnaden mellan *ej bedömd* och *bedömd som oförändrad* är hela poängen med årets uppdrag.
3. Sätt karteringsstatus 2 om grunden är befintlig kunskap, och uppdatera slutdatum till dagens datum.

### D4.1 · Notera avvikelser mot bevarandeplan och beslut

**v41–v48** · **[Handläggare]**

1. FAQ fråga 24: när det du dokumenterar i NNK avviker från fastställd bevarandeplan eller reservatsbeslut ska länsstyrelsen göra en notering om avvikelsen.
2. För en enkel lista i granskningsloggen: objekt, livsmiljötyp, vad bevarandeplanen säger, vad NNK nu visar, och varför.
3. Bedömningen av vilka faktiska åtgärder som ska vidtas ingår INTE i KartLitS — men noteringen ska finnas.
4. Bevarandeplanen når du via WebbGIS-lagret *NV Natura2000 områden*, raden BEVPLAN i attributtabellen. Länken finns även i `data/nnk/nnk_yta_med_sitecode.csv`.

### D4.2 · Lista objekt där beslut hindrar nödvändig skötsel

**v48** · **[Handläggare]** · förutsätter D4.1

1. FAQ fråga 24 sista stycket: kommer ni fram till att nuvarande beslut eller skötselplan hindrar nödvändig skötsel för att upprätthålla livsmiljötyp i gott tillstånd, ska en notering om revideringsbehov göras.
2. Sammanställ dessa fall i ett eget avsnitt i granskningsloggen.
3. Detta blir ett eget stycke i planen till NV och ett underlag till Naturvårdsenhetens revideringsplanering.
4. Stäm av med förvaltarna innan du skriver — de känner besluten.

### D4.3 · Peka ut utvecklingsmark och ange målnaturtyper

**v45–v50** · **[Handläggare]** · förutsätter D1.2 · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

1. Idag har bara 87 polygoner i hela länet en angiven målnaturtyp. FAQ fråga 23 säger att ytor med bevarandemål om utökad areal BÖR pekas ut som utvecklingsmark.
2. Gå igenom bevarandeplanerna för P1-objekten: finns mål om att utöka arealen av någon livsmiljötyp? Finns mål om återskapande eller restaurering i reservatsbesluten?
3. Formella krav: naturtypsstatus sätts till 3 Utvecklingsmark, NATURTYP måste vara en icke-natura-kod, och MALNATUR1–3 anger vad ytan ska bli. Upp till tre målnaturtyper.
4. Prioritera ytor med påtaglig utvecklingspotential — de är enligt FAQ fråga 23 normalt högre prioriterade för skydds- och skötselresurser än ytor med ringa potential.
5. Arronderingsmark och mark som på längre sikt skulle kunna restaureras sätts som icke-natura-typ, inte utvecklingsmark.
6. Förvaltarna vet i regel mycket väl vilka ytor som är på väg åt rätt håll — ta frågan i H3.2.

---

## E. Sammanställning av kunskapsläget

*v45–v50 · 7 uppgifter*

### E1.1 · Nytt NNK-uttag för före/efter-jämförelse

**v45** · **[Karin]** · förutsätter A4.2 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Kör uttagsrutinen från A4.2 igen, exakt samma struktur som januariuttaget.
2. Spara som `data/uttag/nnk_20261110.gpkg`.
3. Kör `python natura-2000: scripts/analysis/koppla_omraden.py` — sätt NNK_SHP till det nya uttaget.
4. Kör `python natura-2000: scripts/analysis/nnk_kunskapslage.py` och jämför mot nollmätningen. Nyckeltalet: andel polygoner med bedömd status ska ha rört sig från 8 %.
5. Spara utskriften i granskningsloggen — det är den mätbara progressen.

### E1.2 · Statistik per Natura 2000-område

**v46** · **[Karin]** · förutsätter E1.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Ta fram areal per livsmiljötyp × tillståndsklass per objekt ur det nya uttaget.
2. Använd `data/nnk/nnk_yta_med_sitecode.csv` som grund — den har redan SITECODE på varje yta.
3. Pivotera i Python eller Excel: rader = sitecode × naturtypskod, kolumner = tillståndsklass, värden = hektar.
4. Detta är kärnan i vad FAQ fråga 6 efterfrågar för 2026.

### E1.3 · Statistik per livsmiljötyp för hela länet

**v46** · **[Karin]** · förutsätter E1.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Aggregera samma data till länsnivå: areal per livsmiljötyp × tillståndsklass.
2. Jämför mot nollmätningen i `kunskapslage.html` avsnitt 2.
3. Lyft fram de hävdberoende typerna separat — de är uppdragets prioritet.

### E2.1 · Kvantifiera kunskapsluckorna per objekt

**v47** · **[Handläggare]** · förutsätter E1.2 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Per objekt: areal i okänt tillstånd, areal osäker naturtyp, areal obestämd naturtyp, areal utvecklingsmark, areal okarterat.
2. Detta är den exakta redovisning FAQ fråga 6 kräver av 2026.
3. Ta med Båven (4 845 ha okarterat) och Tullgarn södra (299 ha) med motivering till varför de inte åtgärdats.

### E2.2 · Redovisa vilka livsmiljötyper per objekt som är osäkra

**v47** · **[Handläggare]** · förutsätter E2.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Explicit krav i FAQ fråga 6: ni ska kunna säga vilka livsmiljötyper i vilket område som omfattas av osäkerhet.
2. Producera en tabell: sitecode × livsmiljötyp × typ av osäkerhet (utbredning / tillstånd / båda) × areal.
3. Sortera så att de hävdberoende och sällsynta typerna hamnar överst.

### E2.3 · Kvalitetsbrister på systemnivå

**v47** · **[Handläggare]** · förutsätter E1.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Sammanställ: andel polygoner med BIDOS-ursprung, åldersfördelning på karteringen, saknade attribut, gränskvalitet, topologifel.
2. Nollmätningen: 96 % BIDOS inom N2000, 81 % skapade 2012, endast 7,5 % någonsin fältbesökta.
3. Detta är inte kritik av länet — det är ett resultat som ska in i planen för 2027 som ett insatsbehov, och en del av det ligger hos Metria.
4. Systematiska fel i grundkarteringen anmäls till `NNK-kartering@metria.se`.

### E3.1 · Fyll i KartLitS WebbGIS-mallen för granskade objekt

**v38–v48** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. Öppna KartLitS WebbGIS, logga in med Automatisk inloggning.
2. Zooma till objektet. Se till att lagret *LstD NNK granskning* är aktivt. Tänd även *NV Naturtypskartan NNK* så färger och mönster syns.
3. Klicka Redigera → välj lager *LstD NNK granskning* → pilen under Redigera geoobjekt → infoklicka på polygonen.
4. Fyll i: Livsmiljötyp behov av justering, Utbredning behov av justering, Livsmiljötyp 1–3, Kommentar livsmiljötyp och utbredning, Tillstånd behov av justering, procentandelarna, Kommentar tillstånd, Vad ska kontrolleras 1–3, Metod för kontroll, och sist Granskat = Ja eller Påbörjat.
5. Spara med *Uppdatera* längst ner. Klicka ALDRIG *Ta bort* — det raderar hela geoobjektet. Vill du avbryta: bakåtpilen vid Redigera geoobjekt → Ignorera redigeringar.
6. Enligt FAQ fråga 9.1 är det detta lager som blir underlaget till planen för 2027.

---

## F. Plan för 2027

*v46–v52 · 6 uppgifter*

### F1.1 · Vilka insatser krävs och vem gör det

**v46–v49** · **[Handläggare]** · förutsätter E2.1 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Dela upp insatsbehovet i fem kategorier: eget fältarbete, eget skrivbordsarbete, Metria, NV:s arbetsgrupper, konsult.
2. Metria har enligt FAQ fråga 26 INTE uppdrag att göra om tidigare karteringar, kartera med högre detaljering utifrån länsspecifika underlag, eller fältkontrollera. Räkna inte med det.
3. Marina och limniska miljöer läggs uttryckligen på HaV och de nationella karteringarna.
4. Ta med de livsmiljötyper som saknar fastställd vägledning (från A2.4) som ett eget stycke — de är blockerade av NV, inte av er.

### F1.2 · Volymuppskattning för 2027

**v47–v48** · **[Handläggare]** · förutsätter C4.1, E2.1 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Räkna antal objekt, hektar och fältdagar per livsmiljötypsgrupp.
2. Kalibrera mot faktisk tidsåtgång i batch B — därför ligger den batchen först i planen. Ta tiden per objekt ur granskningsloggen.
3. Underlag: 197 objekt totalt, varav 40 P1 klara 2026. Kvar: 43 P2, 108 P3, 6 P4 (P4 kräver ingen insats).
4. Räkna separat för naturreservat utanför N2000: 24 914 ha, varav bara 8 % karterat som livsmiljötyp. Underlag från G1.3.

### F2.1 · Er prioritering för 2027

**v48–v49** · **[Handläggare]** · förutsätter F1.2 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Ange ordningsföljd med motivering per livsmiljötypsgrupp, enligt FAQ fråga 11: hävdberoende först, därefter liten utbredning, förekomster med risk för försämring, och förekomster där åtgärder gjorts eller planeras.
2. Var konkret om vad ni behöver veta, inte bara var. "Vi behöver veta om hävden i 6270 upprätthålls" är mer användbart än "vi behöver besöka fler gräsmarker".
3. Koppla till de kvarvarande P2- och P3-objekten.

### F2.2 · Antaganden och generaliseringar

**v48–v49** · **[Handläggare]** · förutsätter H3.2 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Detta är den fråga som ger störst avlastning om NV accepterar förslagen. Lägg mest tid här.
2. Konkreta förslag att pröva: kan hävdstatus i TUVA användas som proxy för tillstånd i 6270 och 6510? Kan 8230 hällmarkstorräng antas oförändrad utan fältbesök, givet att den är svårpåverkad? Kan 9010 taiga i objekt utan avverkningsanmälan antas oförändrad? Kan betesmark med aktivt jordbruksstöd och pågående hävd antas vara i gott tillstånd?
3. Varje generalisering behöver: vad den innebär, vilket underlag den vilar på, hur många hektar den skulle avlasta, och vilken risk den medför.
4. Förvaltarnas svar från H3.2 är det som gör förslagen trovärdiga — utan dem är de gissningar.
5. Skicka gärna in förslagen till KartLitS redan innan planen är klar. Ett tidigt ja är värt mycket mer än ett sent.

### F3.1 · Vad ni gör själva och vad ni behöver hjälp med

**v49** · **[Handläggare]** · förutsätter F1.1 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Dra gränsen tydligt. Marina och limniska miljöer lämnas explicit.
2. Ange vad som kräver resurstillskott för att klaras till 2027, och vad som klaras inom befintlig bemanning.
3. Ta med storobjekten som ett eget stycke — de är länets största enskilda utmaning.

### F4.1 · Underlag till årsredovisningen 2026

**v50–v52** · **[Handläggare]** · förutsätter E2.1, F2.1 · bidrar till *Underlag till årsredovisningen 2026*

1. Regeringsuppdraget efterfrågar två tal: antal områden bedömda och antal områden med plan.
2. Skriv kort — årsredovisningstext är sällan mer än ett stycke per uppdrag.
3. Bifoga kunskapslägesrapporten som underlag om det efterfrågas.
4. Stäm av med chef i god tid före inlämningsdatumet (fråga efter det i A3.1).

---

## G. Naturreservat och nationalpark

*v42–v52 · 4 uppgifter*

### G1.1 · Gå igenom flik 3 i NNK-statistiken

**v42–v44** · **[Karin]** · bidrar till *Screening av naturreservat med volymuppskattning för 2027*

1. Öppna `natura-2000: docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx`, fliken *3. NP_NR_exkl_överlapp*.
2. Filtrera på Län = D. Sortera på kolumnen *Area NVR utanför N2000* fallande.
3. Notera vilka reservat som har stor areal utanför N2000-överlappet — de är det egentliga arbetet 2027.
4. Läge idag: 24 914 ha NR/NP utanför N2000-överlapp, varav bara 4 103 ha (8 %) karterat som livsmiljötyp. Betydligt sämre kunskapsläge än inom N2000.
5. Läs reservatsbesluten för de största: vilka prioriterade bevarandevärden anges i syftet? Det styr prioriteringen på samma sätt som utpekade livsmiljötyper gör inom N2000.

### G1.2 · Screening av hävdberoende och sällsynta typer i reservaten

**v46** · **[Karin]** · förutsätter G1.1 · bidrar till *Screening av naturreservat med volymuppskattning för 2027*

1. Använd samma prioriteringsgrunder som för N2000: hävdberoende marker och sällsynta livsmiljötyper först.
2. Kolumnerna längst till höger i flik 3 ger areal per naturtypskod per reservat — samma struktur som flik 2.
3. Producera en enkel topplista: de 20 reservat som har mest hävdberoende eller sällsynt areal utanför N2000.
4. Gör INTE mer än screening i år. Poängen är att 2027 inte ska börja med en överraskning.

### G1.3 · Grov volymuppskattning för naturreservaten

**v48** · **[Karin]** · förutsätter G1.2 · bidrar till *Screening av naturreservat med volymuppskattning för 2027*

1. Räkna antal reservat, hektar och uppskattade fältdagar, med samma tidsantaganden som i F1.2.
2. Notera vilka som redan har aktuella skötselplaner eller uppföljningar — de går snabbare.
3. Lämna över till F1.2 och G2.1.

### G2.1 · Ta med NR/NP i planen till Naturvårdsverket

**v50** · **[Handläggare]** · förutsätter G1.3, F1.2 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Skriv ett eget avsnitt i planen om naturreservat och nationalpark.
2. Poängtera deadline: NR/NP ska enligt FAQ fråga 6 vara klara 2027, inte 2028. Det är lätt att missa.
3. Ange vad som är gjort (screening) och vad som återstår (allt annat).

---

## H. Förvaltardialog

*v35–v48 · 12 uppgifter*

### H1.1 · Kartlägg vem som förvaltar vilka objekt

**v35–v36** · **[Karin]** · bidrar till *Förvaltarkarta: vem förvaltar vilka objekt*

**Uppdaterat 2026-08-26:** kolumn I *Förvaltare* i `blanketter/blankett_forvaltarkunskap_nnk.xlsx`
fylls nu i automatiskt av `natura-2000: scripts/analysis/bygg_blankett.py`, kopplat via
`natura-2000: scripts/analysis/koppla_forvaltare.py` mot länsstyrelsens förvaltarlista
(uttag 2026-05-27). 186 av 197 sitecodes fick en träff vid körningen 2026-08-26.

1. Öppna `blanketter/blankett_forvaltarkunskap_nnk.xlsx`, fliken Blankett, kolumn I — redan ifylld för de flesta objekt. Ett "(?)" efter namnet betyder osäker namn-matchning.
2. Kontrollera de 5 lågsäkra matchningarna listade i `natura-2000: data/forvaltare/README.md` — särskilt SE0220330 Tolamossen/Torsmossen.
3. Lös de 11 sitecodes utan automatisk träff manuellt (samma README). **SE0220129 Skärgårdsreservaten kräver särskild uppmärksamhet** — objektet består av många enskilt namngivna öar med minst tre olika förvaltare (Paul, Sari, Kristoffer i källistan), inte en enda kontaktperson.
4. Prioritera de sju objekten med Åtgärdas-ytor och de 40 P1-objekten om något ändå saknas. Resten kan vänta.
5. Blanketten går redan att filtrera per förvaltare (kolumn I) och skicka ut i delar.
6. Publicerad 2026-08-27 på GitHub (`blanketter/blankett_forvaltarkunskap_nnk.xlsx`) — den är bara senaste genererade referensversionen, inte en delad levande fil. Arbetskopian som förvaltarna faktiskt fyller i ska ligga på `G:\5_Naturvard_miljoskydd\51_skydd_omr_arter_mm\511_skydd_omr_arter\NRF\blankett_forvaltarkunskap_nnk.xlsx` (samma mapp som granskningslogg_mall.xlsx, se A3.3) — läggs dit av Johan.

### H1.2 · Förankra upplägget med Naturvårdsenhetens chef

**v36** · **[Handläggare]**

1. Boka 30 min. Det är deras personals tid du ber om — förankra innan du kontaktar förvaltarna.
2. Ta med: `docs/metodik.md` avsnitt 1 (citaten som visar att NV godkänner lokalkännedom) och Åtgärdas-fliken i blanketten.
3. Var konkret om vad du ber om: ca 60 minuter per förvaltare, plus tid att fylla i en blankett.
4. Erbjud något tillbaka: den kunskap som förs in i NNK blir ett bättre underlag för deras egen skötselplanering, och åtgärdsbehov förs vidare till SkötselDOS.
5. På sikt: be om en kort informationspunkt på Naturvårdsenhetens enhetsmöte så att förvaltarna vet att NNK-granskningen pågår (beslut 20 aug).

### H2.1 · Gå igenom de 141 Åtgärdas-ytorna

**v37** · **[Handläggare]**

1. Öppna `blanketter/blankett_forvaltarkunskap_nnk.xlsx`, fliken Åtgärdas-ytor. 30 rader, per objekt och livsmiljötyp.
2. Fördelning: Skärgårdsreservaten 91 ytor, Strandstuviken 25, Marvikarna 7, Vilsta 6, Rågö 5, Storhultet 4, Tovhulta stormosse 3. Samtliga inom Natura 2000.
3. Bakgrunden: koden är enligt den publika produktbeskrivningen en äldre kod från basinventeringen som betydde att kompletterande uppgifter behövdes för att bestämma naturtypen. 139 av 141 kommer från BIDOS och redigerades 2007–2008.
4. Öppna dem i ArcGIS Pro för att se var de ligger: Select By Attributes på NNK-lagret, `KARTERINGS LIKE '5%'`. Zooma till urvalet.
5. Detta blir öppningsfrågan i förvaltarsamtalen: *"basinventeringen kunde inte bestämma naturtypen här — vet du vad det är?"*

### H2.2 · Kontrollera KOMMENTAR i NNK Ajourhålla

**v37** · **[Handläggare]** · förutsätter A1.2

1. Detta är en KÄLLKRITISK kontroll som måste göras innan slutsatser dras om kunskapsläget.
2. Bakgrund: i den publika NNK är KOMMENTAR, NNK_KOMMEN och REDIGERARE tomma i samtliga 14 830 polygoner — men handledningen 1.3 säger att den publika versionen strippar kommentarer och användaruppgifter. Fälten kan alltså vara ifyllda i Ajourhålla.
3. Checka ut ett av de sju Åtgärdas-objekten i ArcGIS Pro, förslagsvis SE0220020 Strandstuviken (25 ytor, hanterbart).
4. Öppna attributtabellen och titta på KOMMENTAR och NNK_KOMMEN för ytorna med KARTERINGS = 5.
5. Gör samma kontroll för några av de 277 ytorna med fältdata men ej bedömd status.
6. Notera resultatet i granskningsloggen. Står grunden redan där är en stor del av arbetet redan gjort — då ska det bara läsas in och tillståndet registreras.
7. Checka in utan ändringar.

### H2.3 · Kör områdeskopplingen mot NVR-lagret

**v43** · **[Karin]**

1. 5 221 NNK-ytor ligger utanför Natura 2000 — de finns i naturreservat och nationalpark och saknar områdesidentitet.
2. Öppna `natura-2000: scripts/analysis/koppla_omraden.py`. Kopiera funktionen `hamta_sci` till en variant som hämtar NVR-lagret från Naturvårdsregistret i stället, och byt fältnamnet SITE_CODE mot NVRID.
3. NVR-nedladdningen finns på `geodata.naturvardsverket.se/nedladdning/naturvardsregistret/`. `data/sources_sodermanland.csv` har mönstret för URL:erna.
4. Kör och kontrollera att antalet reservat stämmer mot flik 3 i statistikuttaget.
5. Resultatet behövs för arbetspaket G och för naturreservatsspåret 2027.

### H3.1 · Boka förvaltarsamtalen

**v37** · **[Karin]** · förutsätter H1.1, H1.2

1. Ca 60 minuter per förvaltare, flera objekt per möte. Fysiskt möte med karta framme är bättre än Teams.
2. Skicka med i kallelsen: den filtrerade blanketten för deras objekt, plus en rad om vad mötet handlar om.
3. Be dem titta igenom Åtgärdas-raderna i förväg — det är den fråga som kräver mest eftertanke.
4. Boka in samtalen mellan v38 och v44 så att svaren hinner påverka fältplaneringen.

### H3.2 · Genomför förvaltarsamtalen

**v38–v44** · **[Båda]** · förutsätter H3.1, H2.1 · bidrar till *Ifyllda blanketter från förvaltarsamtalen*

1. FÖRE, ca 30 min per objekt: ta fram objektet i WebbGIS med lagren *LstD NNK granskning* och *NV Naturtypskartan NNK* tända. Läs bevarandeplanen. Filtrera blanketten. Markera rader med karteringsstatus 3, 4 eller 5 — de har en historia.
2. UNDER, punkt 1: börja med Åtgärdas-ytorna. Konkret, och den erkänner att kunskapen finns hos dem.
3. UNDER, punkt 2: gå igenom hävdberoende marker objekt för objekt — hävdas den, av vem, hur länge till, vad är trenden.
4. UNDER, punkt 3: fråga efter dokument du inte känner till — uppföljningsprotokoll, ÄoB-blanketter, konsultrapporter, gamla skötselplansbilagor, foton. Det ligger ofta på en enhetsmapp ingen letat i.
5. UNDER, punkt 4: fråga specifikt om utvecklingsmark — vilka ytor är på väg att bli livsmiljötyp, vilka har ni restaurerat.
6. UNDER, punkt 5: fråga om gränser bara där det rör större arealer. Under minsta karteringsenhet är det inte värt tiden.
7. UNDER, punkt 6: avsluta med vad som borde kontrolleras i fält, och vilka objekt som kan lämnas som de är.
8. REGEL R1 att bevaka hela tiden: när förvaltaren säger "det är ingen äng längre" — beror det på utebliven skötsel står livsmiljötypen kvar, i icke gott tillstånd.
9. EFTER: för in i granskningslagret samma vecka. Minnesbilder av andras minnesbilder blir snabbt oanvändbara.

### H4.1 · Eftersök odokumenterade underlag

**v38–v46** · **[Karin]** · förutsätter H3.2

**Uppdaterat 2026-08-26:** `natura-2000: docs/underlag/NRF_2026_underlag.zip` — en export av
`G:\5_Naturvard_miljoskydd\` (~9 400 filer, 20 GB: skötselplaner, LIFE-projekt (CoastBenefit,
Life Taiga, RestoRED, MIA, RIWUS, GrazedWoods), uppföljningsrapporter, en marin inventering
2016–17 för skärgårdsöarna, bevarandeplan-utkast) täcker det mesta av punkt 2–4 nedan redan.

**Djupgranskning klar 2026-08-26** (samma dag, "ett steg i taget"): de 38 site-specifika
uppföljningsplanerna (målindikatorer per naturtyp) är inkopplade i Blanketten (ny kolumn K)
och en ny geo-fil `natura-2000: data/analysis/nnk_med_uppfoljningsplan_2026.gpkg`. LIFE-projekten
och den limniska vattendragskartläggningen 2022 är genomgångna — se
`natura-2000: data/analysis/README.md` för detaljer per delprojekt. Viktigast: **LIFE
GrazedWoods (Tynnelsö) har själva flaggat att de behöver NNK-statusklassning som en del av sitt
projekt** — värt att lyfta med projektledningen för samordning innan NNK-arbetet och LIFE GW körs
parallellt utan kontakt.

**Metodlärdom, viktig för punkt 3 nedan:** en ren sitecode-/N2000-namnsökning i arkivet missar
underlag som ligger under ett naturreservats EGNA namn när reservatet bara delvis täcker ett
N2000-område. Bekräftat geografiskt (inte bara namnmatchning) via en ny hämtning från
Naturvårdsverkets Naturvårdsregistret-WFS: 121 av 195 naturreservat i länet överlappar Natura
2000, se `natura-2000: data/analysis/naturreservat_n2000_overlapp.csv`. Använd den listan som
ett extra sökregister när du letar i enhetsmappar (punkt 3) — sök på reservatets namn, inte bara
sitecoden eller N2000-områdets namn.

1. Börja med Per Flodin — han sitter på skötselhistorik, artkunskap och tidigare åtgärder. Gör detta ändå, arkivet ersätter inte samtalet.
2. ~~Leta systematiskt efter...~~ — se `natura-2000: data/analysis/nrf_2026_underlag_per_sitecode.csv` för vad som redan finns per objekt innan du letar på egen hand.
3. Sök på enhetsmappar, i diariet, och i SkötselDOS för det som inte redan låg i G:\5_Naturvard_miljoskydd. Fråga även dem som slutat, om det går.
4. Prioritera underlag som rör de 277 ytorna med fältdata men ej bedömd status — där finns det med största sannolikhet ett protokoll någonstans.
5. Skanna in det som bara finns på papper.

### H4.2 · Registrera funna underlag i datakälleregistret

**v38–v48** · **[Karin]** · förutsätter H4.1

**Uppdaterat 2026-08-26:** för `NRF_2026_underlag.zip` är detta redan gjort automatiskt —
`natura-2000: scripts/analysis/katalogisera_nrf_underlag.py` indexerade 3 697 av 9 422 filer
(39 %) mot 199 sitecodes utan att öppna innehållet, se `data/analysis/nrf_2026_underlag_katalog.csv`
(fil-nivå) och `..._per_sitecode.csv` (sitecode-nivå). `data/sources_sodermanland.csv` har en
sammanfattningsrad som pekar dit — det är en bulkarkiv-post, inte en per-dokument-rad, eftersom
den filens kolumner är gjorda för nedladdningsbara GIS-lager.

1. Lägg in varje YTTERLIGARE funnet underlag (Per Flodin-samtalet, papper som skannas in) i `data/sources_sodermanland.csv` med samma kolumnstruktur som finns där.
2. Ange: vad det är, vilket objekt eller vilka objekt det gäller, årtal, var det ligger, och om det är digitalt eller papper.
3. Registret är i sig en leverans — det svarar på FAQ fråga 4 om vad bedömningarna vilar på.

### H5.1 · För in förvaltarkunskapen i granskningslagret

**v38–v46** · **[Båda]** · förutsätter H3.2 · bidrar till *Ifyllda blanketter från förvaltarsamtalen*

1. Samma vecka som samtalet. Följ stegen i E3.1 för WebbGIS-redigeringen.
2. Sätt `faltinventerare` = förvaltarens namn, inte ditt.
3. Sätt `habitat_period_lastdata_end` = det årtal förvaltaren angav.
4. Skriv `Kommentar_metod` i klartext: *"Uppgift från NN, förvaltare, samtal 2026-09-24. Bygger på hens fältbesök hösten 2024 samt skötselplan 2019."*
5. Fältmappningen finns i blankettens flik *Fältmappning* — den visar vilken blankettkolumn som hamnar i vilket fält.

### H5.2 · Registrera i NNK efter avstämning

**v41–v48** · **[Handläggare]** · förutsätter H5.1, D1.2 · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

1. Först efter att du bedömt att underlaget räcker. Granskningslagret är förslagsnivå; NNK är skarpt.
2. Tillståndsfälten först efter driftsättningen i v40.
3. Karteringsstatus: 2 Granskad vid skrivbordet för förvaltarkunskap och dokument. 3 Besökt i fält om förvaltaren faktiskt varit där nyligen. 4 Inventerad i fält endast vid standardiserad metodik.
4. Förändringsorsak: 3 Komplettering i nästan alla fall — kunskapen fanns, den var bara inte registrerad.
5. Kör toolboxen och checka in per objekt.

### H5.3 · Skicka avstämning tillbaka till förvaltaren

**v38–v48** · **[Handläggare]** · förutsätter H5.1

1. Skicka en kort sammanfattning av vad du fört in, per objekt.
2. Förvaltaren ska känna igen sin egen uppgift. Gör de inte det har något gått fel i översättningen.
3. Detta är också det som gör att de svarar nästa gång du frågar.

---

## Checklista före incheckning i NNK

Gäller varje gång ett område checkas in. Från handledningen avsnitt 2.3 och 3.3.

- [ ] Kör toolboxen i ArcGIS Pro på det utcheckade området — databasreglerna kontrolleras där, inte vid incheckningen.
- [ ] Alla obligatoriska attribut ifyllda med godkända värden. Undantag: fritextfälten och de beräknade fälten.
- [ ] Inga överlapp mellan ytor. Inga glapp eller tomrum. Linjer och ytor korsar inte sig själva.
- [ ] Topologifel, prioritering enligt handledningen 3.3: undvik nya fel, prioritera överlapp, åtgärda hål större än 0,25 ha och remsor bredare än 10 m, strunta i mindre.
- [ ] FORANDRING satt på allt du ändrat — 3 Komplettering, 1 Rättning, eller 2 Faktisk förändring.
- [ ] KARTERINGS uppdaterad så att den speglar underlaget, inte din ansträngning.
- [ ] Slutdatum senaste inventering ifyllt.
- [ ] KOMMENTAR ifylld med grund och källa.
- [ ] Systematiska fel i grundkarteringen anmälda till NNK-kartering@metria.se.

---

## Vad som medvetet inte görs 2026

| Avgränsning | Innebörd | Stöd |
|---|---|---|
| Marina livsmiljötyper läggs inte in i NNK | 16 912 ha osäker marin areal lämnas orörd | FAQ f.16 |
| Limniska ytterkanter justeras inte | Livsmiljötyp anges i befintliga ytor där förekomsten är känd | FAQ f.16 |
| Båvens 4 845 ha okarterat åtgärdas inte | Limniskt objekt, nationell kartering pågår | FAQ f.16, f.29 |
| Grottor, branter, sandstäpp, inlandssandmarker | Nationella karteringsunderlag räcker | FAQ f.16 |
| Obetydliga livsmiljötyper inom N2000 | Endast areal redovisas, ingen tillståndsbedömning | FAQ f.15 |
| Standard Data Form / N2000-databasen uppdateras inte | Uppgifterna hämtas automatiskt ur NNK | FAQ f.17 |
| Tillståndsbedömningar med osäkert underlag görs inte | Behåll tidigare bedömning eller ange okänt, dokumentera osäkerheten | FAQ f.22 |
| Uppdateringar under minsta karteringsenhet görs inte | 0,25 ha generellt, 1 ha skog och våtmark, 0,5 ha ädellöv | FAQ f.12 |
| Tidigare signifikansbedömningar görs inte om | Endast nytillkomna livsmiljötyper bedöms | FAQ f.15 |
| Naturreservat utanför N2000 får screening, inte genomgång | Deadline är 2027 | FAQ f.6 |
| Fältkontroll flyttas till 2027 | Arbetspaket B genomförs inte 2026 — fokus är skrivbordsgranskning och förvaltarsamtal utifrån befintlig kunskap | Beslut Johan 2026-08-25 |

---

## Milstolpar

| # | Vecka | Datum | Milstolpe |
|---|---|---|---|
| M1 | v36 | 2026-09-04 | Arbetsplats, behörigheter och metodik på plats |
| M2 | v38 | 2026-09-18 | Batch B granskad — rutinen kalibrerad |
| M3 | v40 | 2026-10-02 | Nya NNK-attribut driftsatta, utbildning genomförd |
| M4 | v44 | 2026-10-30 | Förvaltardialogen genomförd, kunskapen registrerad |
| M5 | v46 | 2026-11-13 | Samtliga 40 P1-objekt skrivbordsgranskade |
| M6 | v50 | 2026-12-11 | Kunskapslägesrapport D-län klar |
| M7 | v52 | 2026-12-23 | Plan för 2027 levererad till NV |

---

## Leveranser

| # | Leverans | Paket | Klart | Mottagare |
|---|---|---|---|---|
| L-A | Fungerande arbetsplats och dokumenterad rollfördelning | A | v36 | Internt |
| L-H1 | Förvaltarkarta: vem förvaltar vilka objekt | H | v36 | Internt |
| L-H2 | Ifyllda blanketter från förvaltarsamtalen | H | v44 | Underlag till C, D och F |
| L-C | Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027 | C | v46 | KartLitS WebbGIS |
| L-D | Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt | D | v48 | NNK Ajourhålla |
| L-G | Screening av naturreservat med volymuppskattning för 2027 | G | v48 | Underlag till F |
| L-E | Kunskapslägesrapport D-län per 2026-12-31 | E | v50 | Naturvårdsverket, internt |
| L-F1 | Plan för 2027 enligt FAQ fråga 9 | F | v52 | Naturvårdsverket |
| L-F2 | Underlag till årsredovisningen 2026 | F | v52 | Länsledningen |

---

*Runbook v1.2 · 2026-08-25 · fältarbete (arbetspaket B) flyttat till 2027 — se `docs/arbetsplan.md` avsnitt 8 · ursprungligen genererad ur `natura-2000: scripts/analysis/uppgifter.py` med `bygg_kontrollrum.py`, denna ändring gjord direkt i `nnk-granskning-2026`*