# Runbook NNK/NRF 2026 — steg för steg

*Länsstyrelsen i Södermanlands län · Naturskyddsenheten · ref. 2451-2026*

**Datum:** 2026-10-09 (D5.2 utgår: ingen konsult för fältbedömning hösten 2026, beslut Johan — för sent på året; all fältkontroll, även R7-pilotens, görs i eget fältarbete 2027). 2026-10-08 (D2.5 VISS-koppling för R7C tillagd och preciserad; D2.6 Skogsstyrelsens register och D2.7 bedömningsförslag per yta tillagda; körordningen ÅTERSTÄLL före Overwrite rättad i D2.4). 2026-09-29 (D2.4 hävdanalys mot jordbruksskiften tillagd; avsnitt C omgjort till tabeller: översiktstabell per arbetspaket, objekttabeller per batch, hanteringstabell i C2.1; C7.1 Tullgarn södra utredd). 2026-09-25 (en källa: runbook och kontrollrum genereras nu direkt ur uppgifter.py till båda repona; D5.1 fältprotokoll och D5.2 villkorat konsultuppdrag tillagda; A2.3 och H5.1: nya fält i granskningslagret). 2026-09-11: A2.5–A2.8 och H2.2 uppdaterade, länsuttaget ur Ajourhålla hämtat och granskningslagret publicerat  
**Omfattning:** 68 uppgifter i 7 arbetspaket, 324 konkreta steg  
**Hör ihop med:** [Arbetsplan](arbetsplan.html) (varför) · [Kontrollrum](../kontrollrum.html) (överblick och avbockning) · [Bedömningsguide](../bedomningsguide.html) (ett område steg för steg) · [Filterguide](filterguide.html) · [Metodik](metodik.html) (förvaltardialogen och R7)

---

## Så används dokumentet

Arbetsplanen säger *varför* och *när*. Det här dokumentet säger *hur*. Varje uppgift har ett id som matchar kontrollrummet och arbetsplanen, och stegen är skrivna för att gå att följa rakt av.

Uppgifter markerade **[Johan]** (projektledare/handläggare), **[Karin]** eller **[Båda]** följer rollfördelningen i arbetsplanens avsnitt 6.1. Där texten nämner *Johans dator* eller det privata natura-2000-repot gäller steget bara Johan — andra kan hoppa över det.

---

## A. Etablering och förutsättningar

*v34–v36 · 17 uppgifter*

| Uppgift | Vecka | Ansvar | Förutsätter | Bidrar till |
|---|---|---|---|---|
| [A1.1 · Beställ och verifiera systembehörigheter](#a11-bestall-och-verifiera-systembehorigheter) | v34–v35 | Johan | – | – |
| [A1.2 · Verifiera att NNK-utcheckning fungerar mot ett testobjekt](#a12-verifiera-att-nnk-utcheckning-fungerar-mot-ett-testobjekt) | v35 | Johan | A1.1 | – |
| [A1.3 · Åtkomst till samverkansytan för Livsmiljötyper](#a13-atkomst-till-samverkansytan-for-livsmiljotyper) | v34 | Johan | – | – |
| [A2.1 · Läs handledningen och lathunden](#a21-las-handledningen-och-lathunden) | v34 | Båda | – | – |
| [A2.2 · Gå igenom kodlistan](#a22-ga-igenom-kodlistan) | v35 | Johan | A1.3 | – |
| [A2.3 · Installera KartLitS GIS-mall och testa den](#a23-installera-kartlits-gis-mall-och-testa-den) | v35 | Johan | A1.2 | – |
| [A2.4 · Hämta fastställda vägledningar — kontrollera status](#a24-hamta-faststallda-vagledningar-kontrollera-status) | v36 | Johan | – | – |
| [A2.5 · Begär datauttag för D-län](#a25-begar-datauttag-for-d-lan) | v35 | Johan | – | – |
| [A2.6 · Kopiera in uttaget i mallen](#a26-kopiera-in-uttaget-i-mallen) | v37 | Johan | A2.3, A2.5 | – |
| [A2.7 · Publicera granskningslagret i portalen](#a27-publicera-granskningslagret-i-portalen) | v37 | Johan | A2.6 | – |
| [A2.8 · Skapa webbGIS från de publicerade lagren](#a28-skapa-webbgis-fran-de-publicerade-lagren) | v37 | Johan | A2.7 | – |
| [A3.1 · Avstämning med chef](#a31-avstamning-med-chef) | v35 | Johan | – | – |
| [A3.2 · Kartlägg förvaltaransvaret på Naturvårdsenheten](#a32-kartlagg-forvaltaransvaret-pa-naturvardsenheten) | v36 | Johan | – | – |
| [A3.3 · Rollfördelning med Karin](#a33-rollfordelning-med-karin) | v35 | Båda | – | – |
| [A3.4 · Anmäl er till KartLitS arbetsgrupper](#a34-anmal-er-till-kartlits-arbetsgrupper) | v36 | Johan | A1.3 | – |
| [A4.1 · Skapa arbetsstruktur för dokumentation](#a41-skapa-arbetsstruktur-for-dokumentation) | v36 | Johan | – | – |
| [A4.2 · Etablera rutin för NNK-uttag](#a42-etablera-rutin-for-nnk-uttag) | v36 | Johan | A1.2 | – |

### A1.1 · Beställ och verifiera systembehörigheter

**v34–v35** · **[Johan]**

1. Skicka en samlad beställning till IT/behörighetsansvarig. Lista exakt: ArcGIS Pro med NNK-tillägget, NNK Ajourhålla (läs OCH skriv — läsrättighet räcker inte), ArcGIS Enterprise-portalen, KartLitS WebbGIS, SkötselDOS, Artportalen (rapportörskonto), samverkansytan för Livsmiljötyper.
2. Ange i beställningen att det gäller regeringsuppdraget NRF, ref. 2451-2026 — det brukar korta handläggningstiden.
3. Notera datum för varje beställning i granskningsloggen. Behörighet är den enskilt vanligaste förseningsorsaken i planen.
4. Medan du väntar: allt i arbetspaket A2 och H2.1 går att göra utan behörigheter, liksom att läsa bevarandeplaner.

### A1.2 · Verifiera att NNK-utcheckning fungerar mot ett testobjekt

**v35** · **[Johan]** · förutsätter A1.1

1. Öppna ArcGIS Pro. Skapa ett nytt projekt: `NNK_D_2026`. Sätt kartans koordinatsystem till SWEREF 99 TM (EPSG:3006) — Map Properties → Coordinate Systems → sök 3006.
2. Anslut till NNK Ajourhålla enligt manualen på VIC Natur (vicnatur.naturvardsverket.se/nnk). Insert → Connections → Database, eller den anslutningsfil IT tillhandahåller.
3. Titta på inspelningen av hur man praktiskt uppdaterar i NNK på VIC Natur (samma sida) innan du checkar ut testobjektet. (Möte 12 aug: båda behöver den.)
4. Välj ett litet testobjekt — förslag: SE0220012 Nävsjöskogen, 5,0 ha, 1 polygon. Minimal risk om något går fel.
5. Checka ut området. Kontrollera att du får ut geometri OCH attribut, och att fälten KOMMENTAR, NNK_KOMMEN och REDIGERARE finns (de saknas i den publika versionen).
6. Gör INGEN ändring. Checka in igen direkt och verifiera att det går utan fel.
7. Notera i granskningsloggen: fungerar utcheckning ja/nej, vilken version av tillägget, eventuella felmeddelanden.

### A1.3 · Åtkomst till samverkansytan för Livsmiljötyper

**v34** · **[Johan]**

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

**v35** · **[Johan]** · förutsätter A1.3

1. Öppna `natura-2000: docs/underlag/handledning/Kodlista_NNK_20260703.xlsx` — den ger kodstruktur och undergrupper, men saknar en egen kategorikolumn.
2. Öppna i stället `natura-2000: docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx`, fliken *KODLISTA_NNK*. Filtrera kolumn H *Kategori 2026* på Gräsmark, Skog och Våtmark — det är de kategorier D-läns arbete gäller. Marina och limniska koder kan du hoppa över i år.
3. Notera undertyperna för de koder som dominerar i länet: 9010 taiga, 9070/9071/9072 trädklädd betesmark, 8230/8231/8232 hällmarkstorräng, 6270 silikatgräsmark, 1630/1631 strandäng. Undertypen syns som olika KOD-nummer inom samma familj (kolumn A) kombinerat med kolumn C *Namn, undergrupp* — kolumn B *Namn* är samma för hela familjen och skiljer inte typerna åt (9070/9071/9072 har alla `Namn` = "Trädklädd betesmark", men 9071 har `Namn, undergrupp` = "Ekhagar" och 9072 = "Ädellövskogsdominerade").
4. Lär dig skillnaden mellan de tre flaggkategorierna: *Naturanaturtyp* (livsmiljötyp), *Obestämd naturanaturtyp* (vet att det är livsmiljötyp, inte vilken) och *Osäker natura/icke-natura* (vet inte om det är livsmiljötyp alls). De kräver helt olika åtgärder. Kategorierna finns i kolumn E *Natura / icke-natura KOD* (värde 1–4) med klartext i kolumn F *Natura/ickenatura Namn*. Filen har en kolumn G till med exakt samma rubriktext (en brist i källfilen) — den innehåller bara en nyare parallell terminologi (Livsmiljötyp-varianterna) för samma fyra värden, inte en annan indelning. Värde 4, *Icke-naturanaturtyp*, är en fjärde kategori som medvetet INTE räknas som en av de tre flaggorna — den är entydig och kräver ingen bedömning.
5. Urvalet finns redan i `natura-2000: docs/nnk/nnk_kodurval_dlan.csv` (41 koder): kolumnen NATURTYPKO i `natura-2000: data/nnk/nnk_yta_med_sitecode.csv` (det faktiska NNK-uttaget för länet), filtrerat till kolumn E = 1 (Naturanaturtyp/livsmiljötyp, se steg 4) och Kategori 2026 = Gräsmark/Skog/Våtmark (se steg 2). Kolumnerna KOD, Namn, Namn_undergrupp, Kategori_2026 samt antal polygoner och areal per kod i länet — uppdatera filen om ett nytt uttag ändrar bilden.

### A2.3 · Installera KartLitS GIS-mall och testa den

**v35** · **[Johan]** · förutsätter A1.2

1. Packa upp `natura-2000: docs/underlag/handledning/KartLits_NNK_GIS_mall_v_2.zip` till en lokal projektmapp.
2. Mallen innehåller `KartLits_NNK_granskning.gdb` med tre tomma lager i SWEREF 99 TM: NNK_naturaobjekt_yta, _lin och _pkt. Plus tre .lyrx-filer med färdig symbologi.
3. Lägg till lagren i ArcGIS Pro-projektet och applicera .lyrx-filerna: högerklick på lagret → Symbology → Import from Layer File.
4. Granska attributtabellen för NNK_naturaobjekt_yta. Fälten du kommer använda: `tillstand`, `procent_gott`, `procent_ej_gott`, `procent_osaker`, `justering`, `utbredning`, `livsmiljötyp1–3`, `malnaturtyp1–3`, `kontroll1–3`, `metod`, `granskat`, `faltinventerare`, `egen_bet`, `habitat_period_lastdata_start`/`_end`, `forandringsorsak_forslag` samt fyra kommentarsfält. Länets eget publicerade lager (`LstD NNK Granskning`) har dessutom skrivskyddade stödfält som pipelinen fyller i: `prio` (P1–P4), `bevarandeplan_ar`, `area_ha` och `naturtyp_kod_text`. De finns inte i den tomma KartLitS-mallen. Se [Attributbeskrivning](attributbeskrivning.html), del C.
5. Testa att lägga till en dummy-post och fylla i fälten, så att du känner igen dem i WebbGIS-gränssnittet. Radera den sedan.

### A2.4 · Hämta fastställda vägledningar — kontrollera status

**v36** · **[Johan]** · klar 2026-10-02

**Läge 2026-10-02:** vägledningarna för alla 45 livsmiljötyper som finns i länets NNK är nedladdade till `natura-2000: docs/underlag/natura2000/naturtyper/`, plus gemensamma texter och tolkningsdokument i undermappen `gemensamt/`. Öppna dem via [Vägledningar per livsmiljötyp](vagledningar.html) (länkar direkt till NV:s och HaV:s PDF:er, med NNK-koder och datum per typ). Lokal översikt: `natura-2000: docs/underlag/natura2000/naturtyper/Status_vagledningar_A2.4.md`. Alla är fastställda, ingen är på remiss. Använd den senaste fastställda versionen för typen, oavsett ålder. Akvatiska typer (11xx, 31xx–32xx) kommer från Havs- och vattenmyndigheten, övriga från Naturvårdsverket.

1. Gå till Naturvårdsverkets sida *Natura 2000 i Sverige* → vägledningar för naturtyper.
2. Ladda hem vägledningarna för de livsmiljötyper som finns i D-län. Prioritera 9010, 9070, 8230, 6270, 6410, 1630, 7110, 7140, 7230, 9080, 9190.
3. Kontrollera för varje: är den FASTSTÄLLD eller på REMISS? FAQ fråga 10 säger att en remissversion inte ska användas som grund för bedömning.
4. Notera i granskningsloggen vilka typer som saknar fastställd vägledning. De blockeras och ska med i planen för 2027 (uppgift F1.1) som ett eget stycke.
5. Kom ihåg: nu gällande vägledningar är från 2026 för akvatiska livsmiljötyper samt taiga (9010) och örtrik skog med gran (9050), men från 2011–2012 för övriga terrestra typer.

### A2.5 · Begär datauttag för D-län

**v35** · **[Johan]** · brådskande — svarstid från NV okänd

1. Mejla `Sandra.Wennberg@naturvardsverket.se` och begär ett uttag ur NNK-Ajourhålla för Södermanlands län (punkter, linjer, ytor), enligt `Manual NNK mall för granskning.pdf` steg 1.
2. Du får instruktioner via mejl för att ladda ner en zipfil med geodatabasen för uttaget.
3. Spara ner zipfilen, extrahera geodatabasen och öppna filerna i ArcGIS Pro. Kontrollera att allt ser rimligt ut (jämför gärna mot exemplet för Stockholm i manualen).
4. Detta är en extern beroende som annars blockerar A2.6–A2.8 och i förlängningen allt WebbGIS-baserat granskningsarbete — skicka mejlet så tidigt som möjligt, gärna samtidigt som A2.3.
5. **Läge 2026-08-26:** uttaget mottaget och sparat (`Lansuttag_NNK_Sodermanland_20260826`, se `natura-2000: data/raw/backups/`). Inte längre blockerande.

### A2.6 · Kopiera in uttaget i mallen

**v37** · **[Johan]** · förutsätter A2.3, A2.5

1. Öppna ArcGIS Pro-projektet med både mallen (A2.3) och datauttaget (A2.5) tillagda.
2. Öppna verktyget **Append** (under Tools/Geoprocessing).
3. Under *Target Dataset*, ange mallens lager för punkter, linjer eller ytor (ett i taget). Under *Input Dataset*, ange motsvarande lager ur uttaget.
4. Under *Field Matching Type*, välj **Use the field map to reconcile field differences**. Klicka Run.
5. Spara editeringarna när alla tre lager (punkt/linje/yta) är klara.
6. Döp om domänerna i geodatabasen med prefixet `LstD` inför publiceringen, enligt manualens rekommendation.
7. **Läge 2026-09-01:** Append-steget kringgicks — granskningslagret byggdes i stället med skript (`natura-2000: deliveries/nnk_granskning_sodermanland_20260901/`, se README där). Domänerna läggs på med `forbered_gdb_for_publicering.py` — steg 1–6 ovan gäller alltså bara om Append-vägen används. Se [Publicera WebbGIS](webbgis-publicering.html), del 1.

### A2.7 · Publicera granskningslagret i portalen

**v37** · **[Johan]** · förutsätter A2.6

1. Ta bort de rena uttagsfilerna från projektet (de som bara användes som källa till Append) så att bara de ifyllda mallagren återstår.
2. Byt namn på de lager som ska publiceras som hostade lager — använd länskoden som prefix, t.ex. `LstD NNK Granskning`.
3. Ta ställning till om vissa koder ska sållas bort, eller om bara objekt som överlappar ett Natura 2000-område ska behållas, innan publicering.
4. Klicka **Share → Web Layer** i ArcGIS Pro och publicera till Länsstyrelsens interna eller externa ArcGIS Enterprise-portal (avstäm vilken med IT/GIS-funktionen — nätverksrestriktionerna på Länsstyrelsens datorer kan påverka vilken som går att nå från fältet).
5. **Detaljerad instruktion:** [Publicera WebbGIS](webbgis-publicering.html), del 2–4 (förberedelser i Pro, Share As Web Layer, efterarbete på item i portalen). Tjänstenamn: `LstD_NNK_Granskning` och `LstD_Skyddade_Omraden`.
6. **Läge 2026-09-01:** publicerat i Länsstyrelsens interna ArcGIS Enterprise-portal. Metadataposten i Geodatakatalogen (informationsklassning, åtkomst- och användningsrestriktioner) stäms fortfarande av med GIS-avdelningen, ej klar per 2026-09-11.

### A2.8 · Skapa webbGIS från de publicerade lagren

**v37** · **[Johan]** · förutsätter A2.7

1. Följ Länsstyrelsernas interna vägledning *Generellt kartstöd* för hur man bygger ett webbGIS från publicerade lager (länken finns i manualen, på Länsstyrelsernas intranät).
2. Lägg till `LstD NNK Granskning` och relevanta referenslager (t.ex. *NV Naturtypskartan NNK*, *NV Natura2000 områden*) i webbGIS-appen.
3. Testa redigering mot ett enskilt objekt innan du meddelar kollegan att lagret är klart att använda (jämför med rutinen i A2.3, punkt 5).
4. Vid frågor eller problem: `giampaolo.cocca@lansstyrelsen.se`.
5. **Detaljerad instruktion:** [Publicera WebbGIS](webbgis-publicering.html), del 5–7 (WebMap i Map Viewer, GK Konfigurator, test och överlämning).
6. **Läge:** webbGIS-appen skapad via GK Konfigurator.

### A3.1 · Avstämning med chef

**v35** · **[Johan]**

1. Boka 60 min med Ing-Marie, ordinarie EC naturskydd. Stefan Henriksson har slutat.
2. Ta med: `kunskapslage.html` (öppna i webbläsare — nyckeltalen finns överst) och arbetsplanens avsnitt 0.
3. Punkter att få beslut om: (1) att 2026 är ett kartläggningsår, inte ett produktionsår; (2) att marina miljöer medvetet lämnas; (3) tidsbudget 107 dagar handläggare + 61 dagar Karin; (4) att Karins 50 % faktiskt är skyddad tid; (5) vilka EC och AC som ska sitta i styrgruppen (beslut 12 aug).
4. Fråga specifikt vad som förväntas i årsredovisningen för 2026 och när texten ska vara inne.
5. Dokumentera besluten i granskningsloggen — särskilt bortvalen. De är det du kommer behöva försvara.

### A3.2 · Kartlägg förvaltaransvaret på Naturvårdsenheten

**v36** · **[Johan]**

**Uppdaterat 2026-08-26:** en sammanställd lista fanns redan (länsstyrelsens förvaltarlista, uttag 2026-05-27) — kolumn I *Förvaltare* i blanketten är nu automatiskt ifylld för 186 av 197 sitecodes, se H1.1 och `natura-2000: data/forvaltare/README.md`.

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

**v36** · **[Johan]** · förutsätter A1.3

1. Maila `kartlitsN2000@naturvardsverket.se`. Anmäl er till arbetsgrupperna för skog, gräsmark och våtmark.
2. Passa på att i samma mail ställa frågorna i arbetsplanens avsnitt 10 — särskilt om storobjekten och om generaliseringar. Svaren styr hela hösten, så ju tidigare desto bättre.
3. Notera att arbetsgrupperna för akvatiska miljöer och fjäll startar hösten 2026 — de är inte relevanta för D-län i år.
4. Spara svaren i `natura-2000: docs/nnk/` — de är underlag till planen för 2027.

### A4.1 · Skapa arbetsstruktur för dokumentation

**v36** · **[Johan]**

1. Mapparna `natura-2000: docs/faltprotokoll/` och `natura-2000: data/uttag/` finns redan. Granskningsloggen förs i stället i `G:\5_Naturvard_miljoskydd\51_skydd_omr_arter_mm\511_skydd_omr_arter\NRF\granskningslogg_mall.xlsx`, fliken *Objektgranskning* — en rad per objekt: sitecode, namn, datum, vem, vad som granskats, vad som ändrats, vad som återstår, osäkerheter. (Ersatte 2026-08-21 den tidigare docs/nnk/granskningslogg.md i natura-2000 — svår att nå och skriva i från Länsstyrelsens datorer. Ligger på G:-enheten, alltså utanför Git — committas aldrig.)
2. Fältdokumentation: en fil per fältdag i `natura-2000: docs/faltprotokoll/`. Fältarbetet är flyttat till 2027 (beslut 2026-08-25) — mappen står färdig men väntas inte fyllas på under 2026.
3. NNK-uttag: spara i `natura-2000: data/uttag/` med datum i filnamnet så före/efter-jämförelser går att göra. Hela mappen är gitignorad utom README.md — filerna committas inte, de är bara lokala arbetskopior.
4. Under 2026 finns ingen daglig commit-rutin kopplad till granskningsarbetet — resultatet av skrivbordsgranskningen (C1.1) hamnar i KartLitS WebbGIS-mallen och i granskningsloggen på G:-enheten, inte i något repo. Committa som vanligt när du faktiskt ändrar filer i natura-2000 eller nnk-granskning-2026 (dokument, analysskript, kodurval m.m.).
5. Kontrollera att `natura-2000: data/uttag/` (hela mappen, inte bara *.gpkg) och `natura-2000: data/nnk/*.gpkg` ligger i `.gitignore` — stora geodatafiler hör inte hemma i Git.
6. Diarieföring (beslut 5 aug): öppna ärenden allteftersom förfrågningar kommer in, och stäng dem när svaret är diariefört. Stäm av rutinen med diariet.

### A4.2 · Etablera rutin för NNK-uttag

**v36** · **[Johan]** · förutsätter A1.2

1. Dokumentera exakt hur du gör uttaget, så att det går att upprepa identiskt i v45: vilket lager, vilka fält, vilket filter, vilket format.
2. Uttaget ska innehålla minst: NOID, NATURTYP, NATURTYPKO, NATURTYPSS, KARTERINGS, FORANDRING, URSPRUNG, KOMMENTAR, NNK_KOMMEN, REDIGERARE, REDIGERATA, REDIGERATG, SKAPATDATU, MALNATUR1–3, samt de nya tillstånds- och dateringsfälten när de driftsatts.
3. Exportera som shapefile eller GPKG till `natura-2000: data/uttag/nnk_YYYYMMDD.gpkg`.
4. Kör `python natura-2000: scripts/analysis/koppla_omraden.py` mot uttaget för att få SITECODE på varje yta. Sätt miljövariabeln NNK_SHP till uttagets sökväg först.
5. Kör `python natura-2000: scripts/analysis/nnk_kunskapslage.py` för att uppdatera nollmätningen.

---

## C. Skrivbordsgranskning av utbredning

*v35–v46 · 7 uppgifter*

| Uppgift | Vecka | Ansvar | Förutsätter | Bidrar till |
|---|---|---|---|---|
| [C1.1 · Etablera granskningsrutinen](#c11-etablera-granskningsrutinen) | v35 | Johan | A2.1, A2.3 | – |
| [C2.1 · Batch S — storobjekten Skärgårdsreservaten och Nynäs](#c21-batch-s-storobjekten-skargardsreservaten-och-nynas) | v41–v46 | Johan | C1.1, A3.4 | L-C |
| [C3.1 · Batch A — kust och skärgård](#c31-batch-a-kust-och-skargard) | v38–v42 | Båda | C1.1 | L-C |
| [C4.1 · Batch B — ängs- och hagmark inland](#c41-batch-b-angs-och-hagmark-inland) | v35–v38 | Karin | C1.1 | L-C |
| [C5.1 · Batch C — våtmark och vattendrag](#c51-batch-c-vatmark-och-vattendrag) | v42–v44 | Karin | C1.1 | L-C |
| [C6.1 · Batch D — skog och ädellöv](#c61-batch-d-skog-och-adellov) | v43–v46 | Karin | C1.1 | L-C |
| [C7.1 · Okarterade ytor och länssöverskridande objekt](#c71-okarterade-ytor-och-lanssoverskridande-objekt) | v44 | Johan | C1.1 | L-C |

### C1.1 · Etablera granskningsrutinen

**v35** · **[Johan]** · förutsätter A2.1, A2.3

**Död ved är ett krav för 9010 och 9050 (2026-10-02):** enligt NV:s vägledningar 2026-02-19 ska en förekomst uppfylla samtliga klassningskrav, bland annat död ved. Det går inte att fastställa vid skrivbordet, så 9010 (inkl. 9006, 9008, 9009), 9050 och 9830 kan bli *icke fullgod* eller *till fält*, aldrig *fullgod*. Se R7B i [metodiken](metodik.html).

**Vägledningar:** senaste fastställda vägledning för varje livsmiljötyp i länet nås via [Vägledningar per livsmiljötyp](vagledningar.html), lokala kopior i `natura-2000: docs/underlag/natura2000/naturtyper/`. Bedöm alltid mot den, oavsett om den är från 2011–2012 eller 2026.

**Nytt 2026-09-29 — stöd för steg (5):** fynd av typiska arter i Artportalen finns sammanställda per yta, se [typiska arter](typiska-arter.html) (avsnittet *Fynd i Artportalen per yta*). Fälten `typarter_antal`, `typarter` och `typarter_senaste_ar` i granskningslagret, och Excelfilen `natura-2000: data/outputs/typiska_arter_artportalen.xlsx`. Skriptet `python natura-2000: scripts/analysis/artportalen_typiska_arter.py` körs av Johan (projektledaren) på hans egen dator, där det privata natura-2000-repot finns — ingen annan behöver köra det.

1. För en rad per objekt i granskningsloggen (`.../NRF/granskningslogg_mall.xlsx`, fliken *Objektgranskning*). Skriv eller välj SITECODE så fylls område, batch, prio, uppgift, förvaltare, utpekade typer och antal ytor i automatiskt (sedan 2026-10-06; mallen byggs av Johan med `python natura-2000: scripts/analysis/bygg_granskningslogg.py`). Rutinen steg för steg, med Floden som exempel, finns i [Bedömningsguiden](../bedomningsguide.html).
2. Rutinen per objekt, åtta steg: (1) öppna objektet i KartLitS WebbGIS och i ArcGIS Pro mot NNK; (2) läs bevarandeplanen — vilka livsmiljötyper är utpekade, vilka är prioriterade bevarandevärden, vilka bevarandemål finns; (3) jämför bevarandeplanens typer mot vad NNK visar, notera differenser; (4) kontrollera mot aktuellt ortofoto och IR-ortofoto — syns uppenbara förändringar sedan 2012?; (5) kontrollera mot TUVA, VMI, VISS och Artportalen; (6) bedöm per yta: stämmer utbredningen — OK / justera / kontrolleras i fält / osäker; (7) notera i WebbGIS-mallen; (8) justera geometri i NNK endast där det påverkar arealen meningsfullt.
3. Minsta karteringsenhet, från handledningen tabell 9: 0,25 ha generellt, 1 ha skog icke-natura och öppen myr, 0,5 ha skog natura, 2 ha ovan trädgränsen. Minsta karteringsbredd 10 m.
4. Lägg större vikt vid gränsen mellan livsmiljötyp och icke-livsmiljötyp än vid gränser mellan olika livsmiljötyper — de senare är gradvisa och svåra att avgränsa exakt.
5. Testa rutinen på ett litet objekt först och tidsätt den. Tidsåtgången är indata till volymuppskattningen i F1.2.

### C2.1 · Batch S — storobjekten Skärgårdsreservaten och Nynäs

**v41–v46** · **[Johan]** · förutsätter C1.1, A3.4 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

**Objekt**

| Sitecode | Område | Terrester (ha) | Hävdberoende (ha) | Sällsynt (ha) | Sällsynta koder | Polygoner | Fältkontrollerade |
|---|---|---:|---:|---:|---|---:|---:|
| SE0220129 | Skärgårdsreservaten | 1 341,5 | 501,3 | 69,3 | 1220, 1620, 4030, 5133, 6210, 6230 | 2915 | 198 |
| SE0220126 | Nynäs | 521,8 | 168,7 | 23,9 | 1640, 4030, 6110, 6210, 6230, 8231 | 1433 | 30 |
| **Summa** | **2 objekt** | **1 863,3** | **670,0** | **93,2** |  | **4348** | **228** |

**Hantering**

| Urval | Vilka ytor | Hur | Filter i webbGIS |
|---|---|---|---|
| Marint — lämnas | `1000` och `11xx` (~390 polygoner i Skärgårdsreservaten) | Rörs inte 2026 (FAQ f.16) | Dölj marint |
| Individuellt | Terrestra ytor > 5 ha (bara ~30 st), alla hävdberoende, alla sällsynta livsmiljötyper, alla Åtgärdas-ytor (91 i Skärgårdsreservaten) | Granskningsrutinen C1.1 per yta | Batch S + *Större än 5 ha* / *Hävdberoende* / *Sällsynt livsmiljötyp* / *Åtgärdas* (ett i taget) |
| Gruppvis | Små hällmarks-, skogs- och skärytor med samma kod och samma bedömningsgrund: `9010`, `8230`/`8231`, `1621` | Sätt attribut i grupp + EN gemensam kommentar | Batch S + naturtyp = 9010, 8230, 8231 eller 1621 och `area_ha` ≤ 5 |
| Återanvänd | Redan fältkontrollerade: 198 i Skärgårdsreservaten, 30 i Nynäs | Läs in befintlig kunskap — gör inte om den | Batch S + *Fältkontrollerade* |

1. Yta för yta på det terrestra är inte realistiskt i de två storobjekten (se tabellen *Objekt*). Dela i stället upp ytorna enligt tabellen *Hantering* och arbeta rad för rad.
2. Stratifiera i ArcGIS Pro: symbolisera på `naturtyp` och sortera attributtabellen på `area_ha` fallande. Samma urval går att göra med filter i webbGIS-appen, se kolumnen *Filter i webbGIS* och filtertabellen i [webbGIS-publicering](webbgis-publicering.html) (Del 6, steg 5).
3. Gruppvis hantering: selektera med Select By Attributes, sätt attributen i grupp och skriv EN gemensam kommentar som anger att det är en generalisering och på vilken grund.
4. Invänta svar från KartLitS (A3.4) på om metoden accepteras innan du kör hela vägen. Fråga 1 i arbetsplanens avsnitt 10.

### C3.1 · Batch A — kust och skärgård

**v38–v42** · **[Båda]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

**Objekt**

| Sitecode | Område | Terrester (ha) | Hävdberoende (ha) | Sällsynt (ha) | Sällsynta koder | Polygoner | Fältkontrollerade |
|---|---|---:|---:|---:|---|---:|---:|
| SE0220439 | Askö | 346,0 | 218,3 | 6,9 | 1220, 1640, 2181, 8231, 9006 | 506 | 48 |
| SE0220020 | Strandstuviken | 268,4 | 155,6 | 15,5 | 1220, 1640, 8231, 8232, 9006, 9190 | 255 | 40 |
| SE0220034 | Tullgarn södra | 327,1 | 90,6 | 24,4 | 1620, 6110, 6210 | 254 | 38 |
| SE0220231 | Rågö | 174,3 | 72,4 | 4,5 | 8220, 8231, 9006, 9072 | 371 | 15 |
| SE0220218 | Stendörren | 167,8 | 69,7 | 0,0 | – | 277 | 11 |
| SE0220077 | Ridö-Sundbyholmsarkipelagen södra | 408,9 | 84,5 | 14,8 | 9110, 9190 | 195 | 12 |
| **Summa** | **6 objekt** | **1 692,5** | **691,1** | **66,1** |  | **1858** | **164** |

1. Kör granskningsrutinen C1.1 per objekt i tabellen. Totalt 1 692 ha terrester livsmiljötyp, varav 691 ha hävdberoende.
2. Särskilt att titta på: 1630 strandängar — hävdas de fortfarande? Strandstuviken har 15 Åtgärdas-ytor av typen 1630 och Rågö har 4.
3. Marina ytor inom objekten: rör dem inte. FAQ fråga 16.
4. Tullgarn södra: de 299 ha som står som okarterade ligger i den del av objektet som är utanför länsgränsen — se C7.1.

### C4.1 · Batch B — ängs- och hagmark inland

**v35–v38** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

**Objekt**

| Sitecode | Område | Terrester (ha) | Hävdberoende (ha) | Sällsynt (ha) | Sällsynta koder | Polygoner | Fältkontrollerade |
|---|---|---:|---:|---:|---|---:|---:|
| SE0220110 | Skåraviken | 94,9 | 94,9 | 0,0 | – | 43 | 0 |
| SE0220017 | Svanviken-Lindbacke | 73,6 | 73,6 | 5,0 | 5130 | 30 | 1 |
| SE0220063 | Sparreholms ekhagar | 83,3 | 83,3 | 0,0 | – | 25 | 0 |
| SE0220118 | Labro ängar | 52,4 | 52,4 | 0,0 | – | 22 | 0 |
| SE0220182 | Segersön | 96,7 | 44,0 | 0,0 | – | 65 | 0 |
| SE0220150 | Tåkenön | 85,8 | 38,1 | 0,0 | – | 50 | 2 |
| SE0220085 | Gripsholms Hjorthage | 36,6 | 36,6 | 0,0 | – | 7 | 0 |
| SE0220363 | Lindön | 57,4 | 31,4 | 0,0 | – | 27 | 0 |
| SE0220115 | Marsviken-Marsäng | 42,8 | 42,8 | 0,4 | 6230 | 26 | 2 |
| SE0220206 | Floden | 31,1 | 31,1 | 0,0 | – | 13 | 0 |
| SE0220088 | Herröknanäs | 33,4 | 28,8 | 0,0 | – | 13 | 0 |
| SE0220603 | Jungfruvassen | 52,0 | 34,4 | 0,0 | – | 12 | 4 |
| SE0220344 | Lövön | 35,4 | 25,7 | 0,0 | – | 20 | 0 |
| SE0220309 | Brebol | 24,4 | 24,4 | 0,0 | – | 42 | 0 |
| SE0220435 | Gesta | 21,8 | 21,8 | 0,0 | – | 22 | 0 |
| SE0220228 | Ånhammarsnäset | 28,8 | 20,4 | 0,5 | 6430 | 30 | 0 |
| **Summa** | **16 objekt** | **850,4** | **683,7** | **5,9** |  | **447** | **9** |

1. Denna batch går FÖRST, medvetet: objekten är små och snabba (851 ha terrester, 684 ha hävdberoende, bara 447 polygoner), vilket kalibrerar rutinen och tidsuppskattningen innan de tunga batcharna.
2. Tidsätt varje objekt och notera i loggen. Siffran används i F1.2.
3. TUVA är det viktigaste sidounderlaget här — nästan allt är ängs- och betesmark.
4. Milstolpe M2 i v38: batchen klar och rutinen kalibrerad.

### C5.1 · Batch C — våtmark och vattendrag

**v42–v44** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

**Objekt**

| Sitecode | Område | Terrester (ha) | Hävdberoende (ha) | Sällsynt (ha) | Sällsynta koder | Polygoner | Fältkontrollerade |
|---|---|---:|---:|---:|---|---:|---:|
| SE0220176 | Tovhulta stormosse | 47,0 | 0,0 | 47,0 | 7110 | 8 | 0 |
| SE0220137 | Bråtamossen | 25,8 | 0,0 | 14,9 | 7230 | 10 | 0 |
| SE0220103 | Pilgöljan | 8,4 | 0,1 | 7,6 | 7230, 7231 | 9 | 0 |
| SE0220021 | Sjösakärren | 20,9 | 2,2 | 5,7 | 7230 | 16 | 1 |
| SE0220106 | Fjällmossen norra | 230,5 | 0,4 | 7,4 | 9006 | 144 | 109 |
| SE0220304 | Kilaån-Vretaån | 45,9 | 6,2 | 44,9 | 3260, 9750 | 214 | 41 |
| **Summa** | **6 objekt** | **378,5** | **8,9** | **127,5** |  | **401** | **151** |

1. Kör granskningsrutinen C1.1 per objekt i tabellen. Totalt 378 ha terrester, varav 128 ha sällsynta typer.
2. Sällsynta typer här: 7110 högmossar (47 ha i länet), 7230 rikkärr (34 ha), 7231 rikkärr undertyp (4 ha), 3260 vattendrag (44 ha), 9750 svämskog (2,7 ha).
3. Limniska ytor: ange livsmiljötyp i befintliga ytor och linjer där förekomsten är känd, men justera INTE ytterkanter eller vattendragsgeometri. FAQ fråga 16.
4. VMI är sidounderlaget för våtmarkerna, VISS för vattendragen.
5. Fjällmossen norra har 109 fältkontrollerade polygoner — återanvänd.

### C6.1 · Batch D — skog och ädellöv

**v43–v46** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

**Objekt**

| Sitecode | Område | Terrester (ha) | Hävdberoende (ha) | Sällsynt (ha) | Sällsynta koder | Polygoner | Fältkontrollerade |
|---|---|---:|---:|---:|---|---:|---:|
| SE0220602 | Vilsta | 248,2 | 12,3 | 7,9 | 9006, 9072 | 146 | 8 |
| SE0220343 | Askholmen | 54,9 | 20,2 | 18,0 | 9072, 9190 | 41 | 14 |
| SE0220503 | Fjellskäfte | 15,0 | 0,0 | 15,0 | 9060 | 10 | 0 |
| SE0220217 | Tore Grav | 10,2 | 0,0 | 10,2 | 9060 | 1 | 0 |
| SE0220130 | Lotsängsbacken | 13,8 | 0,0 | 8,3 | 9180 | 8 | 0 |
| SE0220211 | Ekorneberg | 8,5 | 8,5 | 6,6 | 6230 | 11 | 0 |
| SE0220234 | Persö | 8,0 | 5,8 | 5,8 | 6280 | 20 | 0 |
| SE0220348 | Tynnelsö Djurgård | 21,2 | 8,2 | 8,2 | 9072 | 19 | 1 |
| SE0220507 | Lundäng | 7,5 | 1,1 | 6,4 | 4030 | 4 | 0 |
| SE0220438 | Åsa gravfält | 6,2 | 1,0 | 5,2 | 4030 | 4 | 0 |
| **Summa** | **10 objekt** | **393,5** | **57,1** | **91,6** |  | **264** | **23** |

1. Kör granskningsrutinen C1.1 per objekt i tabellen. Totalt 393 ha terrester, 92 ha sällsynta typer.
2. Sällsynta typer: 9060 åsbarrskog (29 ha), 9072 ädellövdominerad betesmark (29 ha), 9180 ädellövskog i branter (10 ha), 4030 torra hedar (16 ha), 9110 bokskog (6 ha), 6280 alvar (6 ha).
3. För 9010 taiga: kontrollera hällmarker i anslutning — handledningen 3.1 påpekar att grundkarteringen avgränsat taiga främst inom produktiv skog, så angränsande hällmarker kan behöva justeras.
4. Kontrollera avverkningsanmälningar via Skogsstyrelsen för objekt med skogsmark — det är den vanligaste faktiska förändringen.
5. Vilsta har 6 Åtgärdas-ytor.

### C7.1 · Okarterade ytor och länssöverskridande objekt

**v44** · **[Johan]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

**Objekt**

| Objekt | Okarterat | Vad det är | Åtgärd |
|---|---|---|---|
| SE0220303 Båven | 4 845 ha av 6 200 ha | Sjöytan | Lägg INGEN tid på ytterkanterna (FAQ f.16 och 29). Ange livsmiljötyp i befintliga ytor om förekomsten är känd. Dokumentera i loggen att det är medvetet nedprioriterat. |
| SE0220034 Tullgarn södra | 299 ha av 2 014 ha | Kontrollerat 2026-09-29: NNK täcker hela den del av objektet som ligger inom länet (1 690 ha) — det finns inga hål där. Objektet är 2 014 ha enligt den rikstäckande SCI-gränsen; resten (324 ha) ligger utanför länsgränsen och är därför bortklippt ur länsuttaget och ur lagret Skyddade områden. De 299 ha okarterat ligger i den delen. | Eftersom D-län är rapporterande län räknas delen utanför länsgränsen ändå hit. Lägg den rikstäckande SCI-gränsen (`natura-2000: data/raw/SCI_Rikstackande.zip`) över ortofoto och avgör om ytan är land eller vatten. Land: felanmäl som karteringsgap. Vatten: samma som Båven. Stäm av med Stockholms län enligt punkt 4. |
| SE0220077 Ridö-Sundbyholmsarkipelagen södra | – | Gränsar mot Västmanlands län | Samma avstämning som för Tullgarn södra. |

1. Gå igenom objekten i tabellen. Notera resultatet i loggen — båda posterna ska med i kunskapslägesrapporten (E2.1).
2. Är ett hål inom länet terrestert är det ett faktiskt karteringsgap. Felanmäl till `NNK-kartering@metria.se` med sitecode, en skärmbild och en kort beskrivning. Är det vatten gäller samma sak som för Båven.
3. Länssöverskridande objekt: arealer utanför länsgräns tillfaller **rapporterande län** enligt NV:s NNK-statistik (fliken *Beskrivning*). Det är samma sak som förklarar 0,2 %-avvikelsen i arbetsplanens bilaga 3.
4. Kontakta NNK/NRF-handläggaren på det andra länet och kom överens om vem som bedömer vilken del. Vet du inte vem: maila `kartlitsN2000@naturvardsverket.se`. Det är inte Metrias sak — `NNK-kartering@metria.se` är bara för karteringsgap.
5. Dokumentera vilket län som är rapporterande och hur ni delar arbetet. (Åtgärd från möte 20 aug.)

---

## D. Tillståndsbedömning i NNK

*v40–v50 · 15 uppgifter*

| Uppgift | Vecka | Ansvar | Förutsätter | Bidrar till |
|---|---|---|---|---|
| [D1.1 · Bevaka driftsättningen av de nya NNK-attributen](#d11-bevaka-driftsattningen-av-de-nya-nnk-attributen) | v39–v40 | Johan | – | – |
| [D1.2 · Gå igenom den nya attributlistan](#d12-ga-igenom-den-nya-attributlistan) | v40 | Båda | D1.1 | – |
| [D1.3 · Delta i NV:s utbildning](#d13-delta-i-nvs-utbildning) | v40–v41 | Båda | D1.1 | – |
| [D2.1 · Registrera tillstånd där kunskapen redan finns](#d21-registrera-tillstand-dar-kunskapen-redan-finns) | v41–v48 | Båda | D1.2 | L-D |
| [D2.2 · Dokumentera grunden för varje bedömning](#d22-dokumentera-grunden-for-varje-bedomning) | v41–v48 | Båda | – | L-D |
| [D2.3 · Registrera aktivt även oförändrat tillstånd](#d23-registrera-aktivt-aven-oforandrat-tillstand) | v41–v48 | Båda | – | L-D |
| [D2.4 · Hävdanalys mot jordbruksskiften (underlag för R7A, årligen)](#d24-havdanalys-mot-jordbruksskiften-underlag-for-r7a-arligen) | v40–v41 | Johan | – | – |
| [D2.5 · VISS-koppling för sjöar och vattendrag (underlag för R7C)](#d25-viss-koppling-for-sjoar-och-vattendrag-underlag-for-r7c) | v41–v42 | Johan | – | – |
| [D2.6 · Skogsstyrelsens register: avverkning, anmälan och skydd (underlag för R7B)](#d26-skogsstyrelsens-register-avverkning-anmalan-och-skydd-underlag-for-r7b) | v41 | Johan | – | – |
| [D2.7 · Bedömningsförslag per yta enligt R7 (Excel och popup)](#d27-bedomningsforslag-per-yta-enligt-r7-excel-och-popup) | v41–v42 | Johan | D2.4, D2.6 | – |
| [D4.1 · Notera avvikelser mot bevarandeplan och beslut](#d41-notera-avvikelser-mot-bevarandeplan-och-beslut) | v41–v48 | Johan | – | – |
| [D4.2 · Lista objekt där beslut hindrar nödvändig skötsel](#d42-lista-objekt-dar-beslut-hindrar-nodvandig-skotsel) | v48 | Johan | D4.1 | – |
| [D4.3 · Peka ut utvecklingsmark och ange målnaturtyper](#d43-peka-ut-utvecklingsmark-och-ange-malnaturtyper) | v45–v50 | Johan | D1.2 | L-D |
| [D5.1 · Fältprotokoll för tillståndsbedömning](#d51-faltprotokoll-for-tillstandsbedomning) | v40–v42 | Johan | D1.2 | – |
| [D5.2 · Konsultuppdrag för fältbedömning hösten 2026 (utgår)](#d52-konsultuppdrag-for-faltbedomning-hosten-2026-utgar) | v41–v43 | Johan | D5.1 | – |

### D1.1 · Bevaka driftsättningen av de nya NNK-attributen

**v39–v40** · **[Johan]**

1. FAQ fråga 30: nya attribut för tillståndsbedömning införs sommaren 2026, driftsättning planerad till slutet av september.
2. Maila `kartlitsN2000@naturvardsverket.se` i v39 och be om bekräftat datum samt när utbildning ges.
3. Kontrollera i ArcGIS Pro när attributen dykt upp: checka ut testobjektet igen och titta efter fälten för tillstånd i procent.
4. Blir det försenat: fyll v40–v43 med arbetspaket C i stället. Ingen tid går förlorad, bedömningarna dokumenteras i fältprotokoll och granskningslager under tiden.

### D1.2 · Gå igenom den nya attributlistan

**v40** · **[Båda]** · förutsätter D1.1

1. Läs igenom vad som ändrats. Två saker är viktiga: fältnamnen byter från *natura-naturtyp* till *livsmiljötyp*, och tillstånd anges nu som procentuell andel av ytan.
2. Konsekvensen av procentandelen: du behöver INTE längre dela upp en yta för att ange olika tillstånd. Det sparar mycket geometriarbete.
3. Namnbytet sker automatiskt — det du redan lagt in påverkas inte.
4. Uppdatera granskningsrutinen med de nya fälten. Fältprotokollet hanteras i D5.1.

### D1.3 · Delta i NV:s utbildning

**v40–v41** · **[Båda]** · förutsätter D1.1

1. Anmäl båda till utbildningen så snart datum finns.
2. Ta med konkreta frågor från arbetet: storobjektsmetoden, generaliseringar, hur procentandelarna ska tolkas för mosaikartade ytor.
3. Anteckna och lägg i `natura-2000: docs/nnk/`. Notera särskilt allt som avviker från handledningen från juli.

### D2.1 · Registrera tillstånd där kunskapen redan finns

**v41–v48** · **[Båda]** · förutsätter D1.2 · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

**Död ved är ett krav för 9010 och 9050 (2026-10-02):** enligt NV:s vägledningar 2026-02-19 ska en förekomst uppfylla samtliga klassningskrav, bland annat död ved. Det går inte att fastställa vid skrivbordet, så 9010 (inkl. 9006, 9008, 9009), 9050 och 9830 kan bli *icke fullgod* eller *till fält*, aldrig *fullgod*. Se R7B i [metodiken](metodik.html).

**Vägledningar:** bedöm mot den senaste fastställda vägledningen för typen, se [Vägledningar per livsmiljötyp](vagledningar.html) (alla 45 typer i länet, med NNK-koder och datum).

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

### D2.4 · Hävdanalys mot jordbruksskiften (underlag för R7A, årligen)

**v40–v41** · **[Johan]**

1. Hämta Jordbruksverkets årslager av jordbruksskiften (WFS `inspire:arslager_skifte`) för alla år från 2015 till senaste året, klippt på bbox runt länet. Spara som `natura-2000: data/skiften/jordbruksskiften_<år>.gpkg` — se `natura-2000: data/skiften/README.md` (BBOX i CQL kräver `'EPSG:3006'` som sista argument, annars 0 träffar).
2. Lägg till det nya året i grödkodslistan `natura-2000: data/grodkoder/grodkoder_<år>.csv` (BETE = 52, 53, 55, 61, 89, 90, 95; VALL = 49, 50) och utöka `SKIFTEN` i `natura-2000: scripts/analysis/nnk_havd.py`.
3. Bygg om `natura-2000: data/nnk/nnk_join.gpkg` med `python natura-2000: scripts/analysis/bygg_nnk_join.py` om ett nytt NNK-uttag finns, och kör sedan `python natura-2000: scripts/analysis/nnk_havd.py` (knappt en minut). Görs av Johan på hans egen dator, där det privata natura-2000-repot finns.
4. Resultat: `natura-2000: data/resultat/n2000_statusforslag.xlsx` (översikt och urval av pilotens 30 fältkontroller) och `natura-2000: data/analysis/havd_for_granskning.csv`. Johan kopierar CSV:n till sin projektmapp på Länsstyrelsens dator, `C:\Lst\ArcGISProData\Projects\NNK_NRF\Bearbetning\`.
5. Johan publicerar fälten från sin arbetsdator: `jobbdator_BACKUP_granskning.py` → `jobbdator_koppla_nnk_skyddskategori.py` → `forbered_gdb_for_publicering.py` → `jobbdator_ATERSTALL_granskning.py` (först torrkörning, sedan `--skarp`) → `jobbdator_bygg_nnk_lyrx_KORRIGERAD_V3.py` → Overwrite. Återställningen ska alltid köras före Overwrite, annars publiceras lagret utan granskarnas värden. Hoppa aldrig över backupen när granskningen har startat.
6. Lägg in filtren *Hävd enligt skiften* och *Vall senaste året* i Konfiguratorn och popupavsnittet *Hävd enligt jordbruksskiften*, se [webbGIS-publicering](webbgis-publicering.html) (Del 6, steg 5) och [popup-uttryck](popup-arcade-uttryck.html) (avsnitt 8).
7. Så används fältet i bedömningen: [metodik](metodik.html), R7A. Upprepa varje år när Jordbruksverket publicerat årets skiften.

### D2.5 · VISS-koppling för sjöar och vattendrag (underlag för R7C)

**v41–v42** · **[Johan]**

1. Mål: att granskningslagrets popup visar VISS ekologisk status för ytor med sjö- och vattendragstyper (3110, 3130, 3150, 3160, 3260), och vilken kvalitetsfaktor som sätter statusen, så att R7C kan bedömas utan att öppna VISS. Exempel Floden (WA99934431): måttlig, styrd av totalfosfor (otillfredsställande, övergödning), biologi ej klassad, hydromorfologi god → icke fullgod.
2. Hämta VISS vattenförekomster för sjöar (ytor) och vattendrag (linjer) med gällande ekologisk status (geometri), statusklassningen per kvalitetsfaktor med tillförlitlighet, miljöproblemen per vattenförekomst (övergödning, fysisk påverkan, försurning m.m.) och statusen per avrinningsområde (VARO). Källor: VISS export/nedladdning och Geodatakatalogen (*VM VISS Statusklassningar sjöar/vattendrag*, *… avrinningsområden VARO*, ATOM). Notera vilken förvaltningscykel klassningen tillhör. Spara under `natura-2000: data/viss/`. Görs av Johan på hans egen dator, där det privata natura-2000-repot finns; VISS gick inte att nå från molnmiljön 2026-10-08.
3. Skriv `natura-2000: scripts/analysis/nnk_viss.py` på samma sätt som `nnk_tuva.py`. Sjöar (31xx): koppla till den vattenförekomst ytan överlappar mest (samma tröskel, ≥ 1 % eller ≥ 0,25 ha). Vattendrag (3260): VISS-vattendragen är linjer, så areaöverlapp fungerar inte. Koppla i stället den vattenförekomst som har längst sträcka inom ytan buffrad 25 m, och ange sträckan i meter.
4. Fält: `viss_id`, `viss_namn`, `viss_ekostatus`, `viss_risk`, `viss_styrande` (faktorn/faktorerna som sätter statusen, t.ex. "Totalfosfor: otillfredsställande (övergödning)"), `viss_miljoproblem`, `viss_biologi_klassad` (Ja/Nej, så att en status som bara bygger på kemi syns), `viss_tillforlitlighet` (för statusklassningen), `viss_klassning_ar` (år eller cykel, så att åldersgränserna kan tillämpas som för TUVA), `viss_hydromorf` (sämsta hydromorfologiska klass) och `viss_aro_status` (avrinningsområdets status, indicier för sjöar som inte är egna vattenförekomster). Utdata `natura-2000: data/resultat/viss_for_granskning.csv` med nyckel `nv_globalid`, inga datumfält.
5. Föreslaget utfall enligt R7C: god/hög och hydromorfologi god → kandidat till *fullgod*. Måttlig eller sämre där den styrande faktorn är avgörande för typen (näring för 3150/3160, försurning för 3110/3130, hydromorfologi för 3260) → *icke fullgod*. Låg tillförlitlighet, enbart expertbedömning, enbart fisk, eller ingen egen vattenförekomst → *till fält* (avrinningsområdets status skrivs då som indicier i kommentaren).
6. Koppla in fälten i `jobbdator_koppla_nnk_skyddskategori.py` och kör kedjan BACKUP → koppla → forbered → ÅTERSTÄLL → lyrx V3 → Overwrite (se D2.4).
7. Lägg till rader i popupsektion 2b *Bedömning vid skrivbordet (R7)* för R7C, se [popup-uttryck](popup-arcade-uttryck.html), och låt *Vad gäller* föreslå utfallet enligt R7C i [metodiken](metodik.html). Lagret *Vatten (VISS)* finns redan i webbGIS:ets lagerlista sedan 2026-10-08. Samma fält läses av R7-förslagsskriptet (se förslaget om automatiska bedömningsförslag 2026-10-08).

### D2.6 · Skogsstyrelsens register: avverkning, anmälan och skydd (underlag för R7B)

**v41** · **[Johan]**

1. Mål: att R7B kan pröva *avverkning efter karteringen* och *fri utveckling säkerställd* för alla ytor, inte bara via laserdata (som slutar 2020/2023). Klart 2026-10-08.
2. Kör `python natura-2000: scripts/analysis/nnk_skogsregister.py` (ca 6 minuter första gången). Skriptet hämtar Skogsstyrelsens utförda avverkningar, avverkningsanmälningar, biotopskydd och naturvårdsavtal för länet ur Geodataportalens öppna tjänster till `natura-2000: data/skogsstyrelsen/` (gitignorerad, ca 680 MB) och kopplar dem till NNK-ytorna. `--hamta` hämtar om allt; gör det inför varje ny granskningsomgång, eftersom anmälningarna ändras löpande.
3. Tröskel: en avverkning eller anmälan räknas om den täcker minst 0,1 ha eller 10 % av ytan (som kalibreringen i `nnk_laser.py`); skydd om det täcker minst 50 %. Fält: `skr_utford_ar/typ/ha/antal`, `skr_anmald_ar/typ/ha/antal`, `skr_skydd`, `skr_skydd_ar`. Utdata `natura-2000: data/analysis/skogsregister_for_granskning.csv`.
4. Resultat 2026-10-08: 109 av 2 918 skogsytor har utförd avverkning på ytan (de flesta 2021–2025), 14 en aktuell anmälan och 21 biotopskydd eller naturvårdsavtal.
5. Fälten publiceras tillsammans med R7-förslaget, se D2.7.

### D2.7 · Bedömningsförslag per yta enligt R7 (Excel och popup)

**v41–v42** · **[Johan]** · förutsätter D2.4, D2.6

1. Mål: att varje yta som R7 gäller för har ett förslag till utfall, säkerhet, motiv, förslag till formulärets fält och en lista över manuella kontroller med lager och år, så att granskningen kan göras yta för yta och summeras per område. Beslut 2026-10-08: alla grupper, både popup och Excel.
2. Kör `python natura-2000: scripts/analysis/bygg_r7_forslag.py` på din egen dator efter underlagsskripten (hävd, TUVA, SkötselDOS, laser, floraväkteri, D2.6 och, när den finns, VISS i D2.5). Saknas ett underlag blir de ytor som behöver det *till fält* med en hänvisning i kontrollistan. Kör om skriptet när ett underlag uppdaterats.
3. Utdata: `natura-2000: data/resultat/r7_forslag_AAAAMMDD.xlsx` (Läs mig, Områdessök, Per område, en flik per batch och Data) och `natura-2000: data/analysis/r7_forslag_for_granskning.csv` med tre popupfält: `r7f_utfall`, `r7f_motiv`, `r7f_kontrollera`. Excel-filen innehåller interna bedömningsdata och ska inte på den publika webbsidan.
4. Områdessök: skriv SITECODE eller en del av namnet i den gula cellen. Fyra tabeller bredvid varandra: ytorna, underlaget, förslaget till formuläret och vad som ska kontrolleras. Fungerar i Excel och LibreOffice utan dynamiska matriser.
5. Publicera fälten: kopiera `skogsregister_for_granskning.csv` och `r7_forslag_for_granskning.csv` till `C:\Lst\ArcGISProData\Projects\NNK_NRF\Bearbetning\` (eller bygg om jobbdatorpaketet med `bygg_jobbdator_paket.py`) och kör kedjan BACKUP → koppla → forbered → ÅTERSTÄLL → lyrx V3 → Overwrite (se D2.4).
6. Lägg in de nya raderna i popupsektion 2b, se [popup-uttryck](popup-arcade-uttryck.html). Förslaget visas skrivskyddat; formulärfälten fyller granskaren i själv.
7. Hur förslaget används: [metodik](metodik.html), avsnittet *Förslag per yta*, och [bedömningsguiden](../bedomningsguide.html), som går yta för yta och summerar per område.
8. Pilot: förslagen för batch B prövas i samma fältkontroll av 30 ytor som R7-regeln. Notera i granskningsloggen när du ändrar ett förslag och varför; det är underlaget för att justera reglerna.

### D4.1 · Notera avvikelser mot bevarandeplan och beslut

**v41–v48** · **[Johan]**

1. FAQ fråga 24: när det du dokumenterar i NNK avviker från fastställd bevarandeplan eller reservatsbeslut ska länsstyrelsen göra en notering om avvikelsen.
2. För en enkel lista i granskningsloggen: objekt, livsmiljötyp, vad bevarandeplanen säger, vad NNK nu visar, och varför.
3. Bedömningen av vilka faktiska åtgärder som ska vidtas ingår INTE i KartLitS — men noteringen ska finnas.
4. Bevarandeplanen når du via WebbGIS-lagret *NV Natura2000 områden*, raden BEVPLAN i attributtabellen. Länken finns även i `natura-2000: data/nnk/nnk_yta_med_sitecode.csv`.

### D4.2 · Lista objekt där beslut hindrar nödvändig skötsel

**v48** · **[Johan]** · förutsätter D4.1

1. FAQ fråga 24 sista stycket: kommer ni fram till att nuvarande beslut eller skötselplan hindrar nödvändig skötsel för att upprätthålla livsmiljötyp i gott tillstånd, ska en notering om revideringsbehov göras.
2. Sammanställ dessa fall i ett eget avsnitt i granskningsloggen.
3. Detta blir ett eget stycke i planen till NV och ett underlag till Naturvårdsenhetens revideringsplanering.
4. Stäm av med förvaltarna innan du skriver — de känner besluten.

### D4.3 · Peka ut utvecklingsmark och ange målnaturtyper

**v45–v50** · **[Johan]** · förutsätter D1.2 · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

1. Idag har bara 87 polygoner i hela länet en angiven målnaturtyp. FAQ fråga 23 säger att ytor med bevarandemål om utökad areal BÖR pekas ut som utvecklingsmark.
2. Gå igenom bevarandeplanerna för P1-objekten: finns mål om att utöka arealen av någon livsmiljötyp? Finns mål om återskapande eller restaurering i reservatsbesluten?
3. Formella krav: naturtypsstatus sätts till 3 Utvecklingsmark, NATURTYP måste vara en icke-natura-kod, och MALNATUR1–3 anger vad ytan ska bli. Upp till tre målnaturtyper.
4. Prioritera ytor med påtaglig utvecklingspotential — de är enligt FAQ fråga 23 normalt högre prioriterade för skydds- och skötselresurser än ytor med ringa potential.
5. Arronderingsmark och mark som på längre sikt skulle kunna restaureras sätts som icke-natura-typ, inte utvecklingsmark.
6. Förvaltarna vet i regel mycket väl vilka ytor som är på väg åt rätt håll — ta frågan i H3.2.

### D5.1 · Fältprotokoll för tillståndsbedömning

**v40–v42** · **[Johan]** · förutsätter D1.2

1. Utgå från utkastet `natura-2000: docs/nnk/parameterlista_tillstand_livsmiljotyper_utkast.xlsx` (54 parametrar i XLSForm-struktur). Flikarna *LST-målindikatorer* och *Luckor* visar hur uppföljningsplanernas 181 målindikatorer täcks.
2. Stäm av mot NNK:s nya tillståndsattribut från D1.2. Den samlade bedömningen (G10) ska använda exakt NNK:s klasser och procentandelar.
3. Ta ställning till luckorna: graninslag i 9010, 9080 och 9070, föryngring av tall och löv, död ved i 9070 och områdesspecifika rödlistade arter. Kör om `natura-2000: scripts/analysis/koppla_malindikatorer_parameterlista.py` efter ändringar.
4. Stäm av den orange kolumnen (indikation gott tillstånd) mot NV:s vägledningar, för 9010 och 9050 mot de reviderade versionerna från februari 2026.
5. För 9010 och 9050: död ved ska finnas som obligatorisk fråga i protokollet, eftersom den avgör om ytan är typen (mängd död ved äldre än ett år, och för 9010 även kvalitet: grov ved, förrötade lågor, flera nedbrytningsstadier, senvuxen eller brandpåverkad ved). Se R7B i [metodiken](metodik.html).
6. Bestäm leveransformat: fältdata i ett eget hostat lager eller en egen tabell, aldrig i granskningslagret (Overwrite raderar fältdatan). Koppla på NNK:s objekt-ID, inte GlobalID.
7. Protokollet används i eget fältarbete 2027 (inget konsultuppdrag 2026, se D5.2). Insamlingen görs i Field Maps med Smart Form mot ett eget lager, se `natura-2000: docs/nnk/faltformular_tillstand_smartform.md`.

### D5.2 · Konsultuppdrag för fältbedömning hösten 2026 (utgår)

**v41–v43** · **[Johan]** · förutsätter D5.1 · utgår 2026-10-09

**Beslut 2026-10-09 (Johan):** ingen konsult för fältbedömning hösten 2026, det är för sent på året. All fältkontroll görs i eget fältarbete 2027.

1. Inget att göra 2026. Uppgiften står kvar så att numreringen och tidigare hänvisningar stämmer.
2. Ytor med utfallet *Till fält* i R7-förslagen (D2.7) och *kontrolleras i fält* i granskningsloggen samlas som underlag till fältplaneringen 2027 (F1.2).
3. R7-pilotens 30 fältkontroller görs i eget fältarbete 2027. Till dess används R7 bara som förslag i granskningslagret.
4. Om konsult blir aktuellt för säsongen 2027 tas det upp i F1.2 (volymuppskattning och insatsbehov).

---

## E. Sammanställning av kunskapsläget

*v45–v50 · 7 uppgifter*

| Uppgift | Vecka | Ansvar | Förutsätter | Bidrar till |
|---|---|---|---|---|
| [E1.1 · Nytt NNK-uttag för före/efter-jämförelse](#e11-nytt-nnk-uttag-for-foreefter-jamforelse) | v45 | Karin | A4.2 | L-E |
| [E1.2 · Statistik per Natura 2000-område](#e12-statistik-per-natura-2000-omrade) | v46 | Karin | E1.1 | L-E |
| [E1.3 · Statistik per livsmiljötyp för hela länet](#e13-statistik-per-livsmiljotyp-for-hela-lanet) | v46 | Karin | E1.1 | L-E |
| [E2.1 · Kvantifiera kunskapsluckorna per objekt](#e21-kvantifiera-kunskapsluckorna-per-objekt) | v47 | Johan | E1.2 | L-E |
| [E2.2 · Redovisa vilka livsmiljötyper per objekt som är osäkra](#e22-redovisa-vilka-livsmiljotyper-per-objekt-som-ar-osakra) | v47 | Johan | E2.1 | L-E |
| [E2.3 · Kvalitetsbrister på systemnivå](#e23-kvalitetsbrister-pa-systemniva) | v47 | Johan | E1.1 | L-E |
| [E3.1 · Fyll i KartLitS WebbGIS-mallen för granskade objekt](#e31-fyll-i-kartlits-webbgis-mallen-for-granskade-objekt) | v38–v48 | Karin | C1.1 | L-C |

### E1.1 · Nytt NNK-uttag för före/efter-jämförelse

**v45** · **[Karin]** · förutsätter A4.2 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Kör uttagsrutinen från A4.2 igen, exakt samma struktur som januariuttaget.
2. Spara som `natura-2000: data/uttag/nnk_20261110.gpkg`.
3. Kör `python natura-2000: scripts/analysis/koppla_omraden.py` — sätt NNK_SHP till det nya uttaget.
4. Kör `python natura-2000: scripts/analysis/nnk_kunskapslage.py` och jämför mot nollmätningen. Nyckeltalet: andel polygoner med bedömd status ska ha rört sig från 8 %.
5. Spara utskriften i granskningsloggen — det är den mätbara progressen.

### E1.2 · Statistik per Natura 2000-område

**v46** · **[Karin]** · förutsätter E1.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Ta fram areal per livsmiljötyp × tillståndsklass per objekt ur det nya uttaget.
2. Använd `natura-2000: data/nnk/nnk_yta_med_sitecode.csv` som grund — den har redan SITECODE på varje yta.
3. Pivotera i Python eller Excel: rader = sitecode × naturtypskod, kolumner = tillståndsklass, värden = hektar.
4. Detta är kärnan i vad FAQ fråga 6 efterfrågar för 2026.

### E1.3 · Statistik per livsmiljötyp för hela länet

**v46** · **[Karin]** · förutsätter E1.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Aggregera samma data till länsnivå: areal per livsmiljötyp × tillståndsklass.
2. Jämför mot nollmätningen i `kunskapslage.html` avsnitt 2.
3. Lyft fram de hävdberoende typerna separat — de är uppdragets prioritet.

### E2.1 · Kvantifiera kunskapsluckorna per objekt

**v47** · **[Johan]** · förutsätter E1.2 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Per objekt: areal i okänt tillstånd, areal osäker naturtyp, areal obestämd naturtyp, areal utvecklingsmark, areal okarterat.
2. Detta är den exakta redovisning FAQ fråga 6 kräver av 2026.
3. Ta med Båven (4 845 ha okarterat) och Tullgarn södra (299 ha) med motivering till varför de inte åtgärdats.

### E2.2 · Redovisa vilka livsmiljötyper per objekt som är osäkra

**v47** · **[Johan]** · förutsätter E2.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Explicit krav i FAQ fråga 6: ni ska kunna säga vilka livsmiljötyper i vilket område som omfattas av osäkerhet.
2. Producera en tabell: sitecode × livsmiljötyp × typ av osäkerhet (utbredning / tillstånd / båda) × areal.
3. Sortera så att de hävdberoende och sällsynta typerna hamnar överst.

### E2.3 · Kvalitetsbrister på systemnivå

**v47** · **[Johan]** · förutsätter E1.1 · bidrar till *Kunskapslägesrapport D-län per 2026-12-31*

1. Sammanställ: andel polygoner med BIDOS-ursprung, åldersfördelning på karteringen, saknade attribut, gränskvalitet, topologifel.
2. Nollmätningen: 96 % BIDOS inom N2000, 81 % skapade 2012, endast 7,5 % någonsin fältbesökta.
3. Detta är inte kritik av länet — det är ett resultat som ska in i planen för 2027 som ett insatsbehov, och en del av det ligger hos Metria.
4. Systematiska fel i grundkarteringen anmäls till `NNK-kartering@metria.se`.

### E3.1 · Fyll i KartLitS WebbGIS-mallen för granskade objekt

**v38–v48** · **[Karin]** · förutsätter C1.1 · bidrar till *Granskningslogg för 40 P1-objekt + lista över ytor som kräver fältkontroll 2027*

1. Öppna KartLitS WebbGIS, logga in med Automatisk inloggning.
2. Zooma till objektet. Se till att lagret *LstD NNK Granskning* är aktivt. Tänd även *NV Naturtypskartan NNK* så färger och mönster syns.
3. Klicka Redigera → välj lager *LstD NNK Granskning* → pilen under Redigera geoobjekt → infoklicka på polygonen.
4. Fyll i: Livsmiljötyp behov av justering, Utbredning behov av justering, Livsmiljötyp 1–3, Kommentar livsmiljötyp och utbredning, Tillstånd behov av justering, procentandelarna, Kommentar tillstånd, Vad ska kontrolleras 1–3, Metod för kontroll, och sist Granskat = Ja eller Påbörjat.
5. Spara med *Uppdatera* längst ner. Klicka ALDRIG *Ta bort* — det raderar hela geoobjektet. Vill du avbryta: bakåtpilen vid Redigera geoobjekt → Ignorera redigeringar.
6. Enligt FAQ fråga 9.1 är det detta lager som blir underlaget till planen för 2027.

---

## F. Plan för 2027

*v46–v52 · 6 uppgifter*

| Uppgift | Vecka | Ansvar | Förutsätter | Bidrar till |
|---|---|---|---|---|
| [F1.1 · Vilka insatser krävs och vem gör det](#f11-vilka-insatser-kravs-och-vem-gor-det) | v46–v49 | Johan | E2.1 | L-F1 |
| [F1.2 · Volymuppskattning för 2027](#f12-volymuppskattning-for-2027) | v47–v48 | Johan | C4.1, E2.1 | L-F1 |
| [F2.1 · Er prioritering för 2027](#f21-er-prioritering-for-2027) | v48–v49 | Johan | F1.2 | L-F1 |
| [F2.2 · Antaganden och generaliseringar](#f22-antaganden-och-generaliseringar) | v48–v49 | Johan | H3.2 | L-F1 |
| [F3.1 · Vad ni gör själva och vad ni behöver hjälp med](#f31-vad-ni-gor-sjalva-och-vad-ni-behover-hjalp-med) | v49 | Johan | F1.1 | L-F1 |
| [F4.1 · Underlag till årsredovisningen 2026](#f41-underlag-till-arsredovisningen-2026) | v50–v52 | Johan | E2.1, F2.1 | L-F2 |

### F1.1 · Vilka insatser krävs och vem gör det

**v46–v49** · **[Johan]** · förutsätter E2.1 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Dela upp insatsbehovet i fem kategorier: eget fältarbete, eget skrivbordsarbete, Metria, NV:s arbetsgrupper, konsult.
2. Metria har enligt FAQ fråga 26 INTE uppdrag att göra om tidigare karteringar, kartera med högre detaljering utifrån länsspecifika underlag, eller fältkontrollera. Räkna inte med det.
3. Marina och limniska miljöer läggs uttryckligen på HaV och de nationella karteringarna.
4. Ta med de livsmiljötyper som saknar fastställd vägledning (från A2.4) som ett eget stycke — de är blockerade av NV, inte av er.

### F1.2 · Volymuppskattning för 2027

**v47–v48** · **[Johan]** · förutsätter C4.1, E2.1 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Räkna antal objekt, hektar och fältdagar per livsmiljötypsgrupp.
2. Kalibrera mot faktisk tidsåtgång i batch B — därför ligger den batchen först i planen. Ta tiden per objekt ur granskningsloggen.
3. Underlag: 197 objekt totalt, varav 40 P1 klara 2026. Kvar: 43 P2, 108 P3, 6 P4 (P4 kräver ingen insats).
4. Räkna separat för naturreservat utanför N2000: 24 914 ha, varav bara 8 % karterat som livsmiljötyp. Underlag från G1.3.

### F2.1 · Er prioritering för 2027

**v48–v49** · **[Johan]** · förutsätter F1.2 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Ange ordningsföljd med motivering per livsmiljötypsgrupp, enligt FAQ fråga 11: hävdberoende först, därefter liten utbredning, förekomster med risk för försämring, och förekomster där åtgärder gjorts eller planeras.
2. Var konkret om vad ni behöver veta, inte bara var. "Vi behöver veta om hävden i 6270 upprätthålls" är mer användbart än "vi behöver besöka fler gräsmarker".
3. Koppla till de kvarvarande P2- och P3-objekten.

### F2.2 · Antaganden och generaliseringar

**v48–v49** · **[Johan]** · förutsätter H3.2 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Detta är den fråga som ger störst avlastning om NV accepterar förslagen. Lägg mest tid här.
2. Konkreta förslag att pröva: kan hävdstatus i TUVA användas som proxy för tillstånd i 6270 och 6510? Kan 8230 hällmarkstorräng antas oförändrad utan fältbesök, givet att den är svårpåverkad? Kan 9010 taiga i objekt utan avverkningsanmälan antas oförändrad? Kan betesmark med aktivt jordbruksstöd och pågående hävd antas vara i gott tillstånd?
3. Varje generalisering behöver: vad den innebär, vilket underlag den vilar på, hur många hektar den skulle avlasta, och vilken risk den medför.
4. Förvaltarnas svar från H3.2 är det som gör förslagen trovärdiga — utan dem är de gissningar.
5. Skicka gärna in förslagen till KartLitS redan innan planen är klar. Ett tidigt ja är värt mycket mer än ett sent.

### F3.1 · Vad ni gör själva och vad ni behöver hjälp med

**v49** · **[Johan]** · förutsätter F1.1 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Dra gränsen tydligt. Marina och limniska miljöer lämnas explicit.
2. Ange vad som kräver resurstillskott för att klaras till 2027, och vad som klaras inom befintlig bemanning.
3. Ta med storobjekten som ett eget stycke — de är länets största enskilda utmaning.

### F4.1 · Underlag till årsredovisningen 2026

**v50–v52** · **[Johan]** · förutsätter E2.1, F2.1 · bidrar till *Underlag till årsredovisningen 2026*

1. Regeringsuppdraget efterfrågar två tal: antal områden bedömda och antal områden med plan.
2. Skriv kort — årsredovisningstext är sällan mer än ett stycke per uppdrag.
3. Bifoga kunskapslägesrapporten som underlag om det efterfrågas.
4. Stäm av med chef i god tid före inlämningsdatumet (fråga efter det i A3.1).

---

## G. Naturreservat och nationalpark

*v42–v52 · 4 uppgifter*

| Uppgift | Vecka | Ansvar | Förutsätter | Bidrar till |
|---|---|---|---|---|
| [G1.1 · Gå igenom flik 3 i NNK-statistiken](#g11-ga-igenom-flik-3-i-nnk-statistiken) | v42–v44 | Karin | – | L-G |
| [G1.2 · Screening av hävdberoende och sällsynta typer i reservaten](#g12-screening-av-havdberoende-och-sallsynta-typer-i-reservaten) | v46 | Karin | G1.1 | L-G |
| [G1.3 · Grov volymuppskattning för naturreservaten](#g13-grov-volymuppskattning-for-naturreservaten) | v48 | Karin | G1.2 | L-G |
| [G2.1 · Ta med NR/NP i planen till Naturvårdsverket](#g21-ta-med-nrnp-i-planen-till-naturvardsverket) | v50 | Johan | G1.3, F1.2 | L-F1 |

### G1.1 · Gå igenom flik 3 i NNK-statistiken

**v42–v44** · **[Karin]** · bidrar till *Screening av naturreservat med volymuppskattning för 2027*

1. Öppna `natura-2000: docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx`, fliken *3. NP_NR_exkl_överlapp*.
2. Filtrera på Län = D. Sortera på kolumnen *Area NVR utanför N2000* fallande.
3. Notera vilka reservat som har stor areal utanför N2000-överlappet — de är det egentliga arbetet 2027.
4. Läge idag: 24 914 ha NR/NP utanför N2000-överlapp, varav bara 4 103 ha (8 %) karterat som livsmiljötyp. Betydligt sämre kunskapsläge än inom N2000.
5. Läs reservatsbesluten för de största: vilka prioriterade bevarandevärden anges i syftet? Det styr prioriteringen på samma sätt som utpekade livsmiljötyper gör inom N2000.

### G1.2 · Screening av hävdberoende och sällsynta typer i reservaten

**v46** · **[Karin]** · förutsätter G1.1 · bidrar till *Screening av naturreservat med volymuppskattning för 2027*

**Beslut 2026-09-29 — Artportalen-fynd för naturreservaten tas 2027.** Hämtningen av fynd och typiska arter per yta (`natura-2000: scripts/analysis/artportalen_typiska_arter.py`) kördes 2026 bara för de 197 Natura 2000-områdena. Naturreservat och nationalpark utanför N2000 hämtas 2027, när tillståndsbedömningen för NR/NP ska göras (FAQ fråga 6). Skriptet behöver då kompletteras så att det kan välja reservat (lagret Skyddade områden, NVRID) i stället för sitecode.

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

**v50** · **[Johan]** · förutsätter G1.3, F1.2 · bidrar till *Plan för 2027 enligt FAQ fråga 9*

1. Skriv ett eget avsnitt i planen om naturreservat och nationalpark.
2. Poängtera deadline: NR/NP ska enligt FAQ fråga 6 vara klara 2027, inte 2028. Det är lätt att missa.
3. Ange vad som är gjort (screening) och vad som återstår (allt annat).

---

## H. Förvaltardialog

*v35–v48 · 12 uppgifter*

| Uppgift | Vecka | Ansvar | Förutsätter | Bidrar till |
|---|---|---|---|---|
| [H1.1 · Kartlägg vem som förvaltar vilka objekt](#h11-kartlagg-vem-som-forvaltar-vilka-objekt) | v35–v36 | Karin | – | L-H1 |
| [H1.2 · Förankra upplägget med Naturvårdsenhetens chef](#h12-forankra-upplagget-med-naturvardsenhetens-chef) | v36 | Johan | – | – |
| [H2.1 · Gå igenom de 141 Åtgärdas-ytorna](#h21-ga-igenom-de-141-atgardas-ytorna) | v37 | Johan | – | – |
| [H2.2 · Kontrollera KOMMENTAR i NNK Ajourhålla](#h22-kontrollera-kommentar-i-nnk-ajourhalla) | v37 | Johan | A1.2 | – |
| [H2.3 · Kör områdeskopplingen mot NVR-lagret](#h23-kor-omradeskopplingen-mot-nvr-lagret) | v43 | Karin | – | – |
| [H3.1 · Boka förvaltarsamtalen](#h31-boka-forvaltarsamtalen) | v37 | Karin | H1.1, H1.2 | – |
| [H3.2 · Genomför förvaltarsamtalen](#h32-genomfor-forvaltarsamtalen) | v38–v44 | Båda | H3.1, H2.1 | L-H2 |
| [H4.1 · Eftersök odokumenterade underlag](#h41-eftersok-odokumenterade-underlag) | v38–v46 | Karin | H3.2 | – |
| [H4.2 · Registrera funna underlag i datakälleregistret](#h42-registrera-funna-underlag-i-datakalleregistret) | v38–v48 | Karin | H4.1 | – |
| [H5.1 · För in förvaltarkunskapen i granskningslagret](#h51-for-in-forvaltarkunskapen-i-granskningslagret) | v38–v46 | Båda | H3.2 | L-H2 |
| [H5.2 · Registrera i NNK efter avstämning](#h52-registrera-i-nnk-efter-avstamning) | v41–v48 | Johan | H5.1, D1.2 | L-D |
| [H5.3 · Skicka avstämning tillbaka till förvaltaren](#h53-skicka-avstamning-tillbaka-till-forvaltaren) | v38–v48 | Johan | H5.1 | – |

### H1.1 · Kartlägg vem som förvaltar vilka objekt

**v35–v36** · **[Karin]** · bidrar till *Förvaltarkarta: vem förvaltar vilka objekt*

**Uppdaterat 2026-08-26:** kolumn I *Förvaltare* i `blanketter/blankett_forvaltarkunskap_nnk.xlsx` fylls nu i automatiskt av `natura-2000: scripts/analysis/bygg_blankett.py`, kopplat via `natura-2000: scripts/analysis/koppla_forvaltare.py` mot länsstyrelsens förvaltarlista (uttag 2026-05-27). 186 av 197 sitecodes fick en träff vid körningen 2026-08-26.

1. Öppna `blanketter/blankett_forvaltarkunskap_nnk.xlsx`, fliken Blankett, kolumn I — redan ifylld för de flesta objekt. Ett "(?)" efter namnet betyder osäker namn-matchning.
2. Kontrollera de 5 lågsäkra matchningarna listade i `natura-2000: data/forvaltare/README.md` — särskilt SE0220330 Tolamossen/Torsmossen.
3. Lös de 11 sitecodes utan automatisk träff manuellt (samma README). **SE0220129 Skärgårdsreservaten kräver särskild uppmärksamhet** — objektet består av många enskilt namngivna öar med minst tre olika förvaltare (Paul, Sari, Kristoffer i källistan), inte en enda kontaktperson.
4. Prioritera de sju objekten med Åtgärdas-ytor och de 40 P1-objekten om något ändå saknas. Resten kan vänta.
5. Blanketten går redan att filtrera per förvaltare (kolumn I) och skicka ut i delar.
6. Publicerad 2026-08-27 på GitHub (`blanketter/blankett_forvaltarkunskap_nnk.xlsx`) — den är bara senaste genererade referensversionen, inte en delad levande fil. Arbetskopian som förvaltarna faktiskt fyller i ska ligga på `G:\5_Naturvard_miljoskydd\51_skydd_omr_arter_mm\511_skydd_omr_arter\NRF\blankett_forvaltarkunskap_nnk.xlsx` (samma mapp som granskningslogg_mall.xlsx, se A3.3) — läggs dit av Johan.

### H1.2 · Förankra upplägget med Naturvårdsenhetens chef

**v36** · **[Johan]**

1. Boka 30 min. Det är deras personals tid du ber om — förankra innan du kontaktar förvaltarna.
2. Ta med: `docs/metodik.md` avsnitt 1 (citaten som visar att NV godkänner lokalkännedom) och Åtgärdas-fliken i blanketten.
3. Var konkret om vad du ber om: ca 60 minuter per förvaltare, plus tid att fylla i en blankett.
4. Erbjud något tillbaka: den kunskap som förs in i NNK blir ett bättre underlag för deras egen skötselplanering, och åtgärdsbehov förs vidare till SkötselDOS.
5. På sikt: be om en kort informationspunkt på Naturvårdsenhetens enhetsmöte så att förvaltarna vet att NNK-granskningen pågår (beslut 20 aug).

### H2.1 · Gå igenom de 141 Åtgärdas-ytorna

**v37** · **[Johan]**

1. Öppna `blanketter/blankett_forvaltarkunskap_nnk.xlsx`, fliken Åtgärdas-ytor. 30 rader, per objekt och livsmiljötyp.
2. Fördelning: Skärgårdsreservaten 91 ytor, Strandstuviken 25, Marvikarna 7, Vilsta 6, Rågö 5, Storhultet 4, Tovhulta stormosse 3. Samtliga inom Natura 2000.
3. Bakgrunden: koden är enligt den publika produktbeskrivningen en äldre kod från basinventeringen som betydde att kompletterande uppgifter behövdes för att bestämma naturtypen. 139 av 141 kommer från BIDOS och redigerades 2007–2008.
4. Öppna dem i ArcGIS Pro för att se var de ligger: Select By Attributes på NNK-lagret, `KARTERINGS LIKE '5%'`. Zooma till urvalet.
5. Detta blir öppningsfrågan i förvaltarsamtalen: *"basinventeringen kunde inte bestämma naturtypen här — vet du vad det är?"*

### H2.2 · Kontrollera KOMMENTAR i NNK Ajourhålla

**v37** · **[Johan]** · förutsätter A1.2

1. Detta är en KÄLLKRITISK kontroll som måste göras innan slutsatser dras om kunskapsläget.
2. Bakgrund: i den publika NNK är KOMMENTAR, NNK_KOMMEN och REDIGERARE tomma i samtliga 14 830 polygoner — men handledningen 1.3 säger att den publika versionen strippar kommentarer och användaruppgifter. Fälten kan alltså vara ifyllda i Ajourhålla.
3. **Genväg sedan 2026-08-26:** länsuttaget `Lansuttag_NNK_Sodermanland_20260826` har `kommentar`/`nnk_kommentar` ifyllda för alla ytor i länet redan — det kan gå snabbare att fråga i det direkt (`natura-2000: data/raw/backups/`) än att checka ut objekt för objekt enligt punkt 4–6 nedan.
4. Checka ut ett av de sju Åtgärdas-objekten i ArcGIS Pro, förslagsvis SE0220020 Strandstuviken (25 ytor, hanterbart).
5. Öppna attributtabellen och titta på KOMMENTAR och NNK_KOMMEN för ytorna med KARTERINGS = 5.
6. Gör samma kontroll för några av de 277 ytorna med fältdata men ej bedömd status.
7. Notera resultatet i granskningsloggen. Står grunden redan där är en stor del av arbetet redan gjort — då ska det bara läsas in och tillståndet registreras.
8. Checka in utan ändringar.

### H2.3 · Kör områdeskopplingen mot NVR-lagret

**v43** · **[Karin]**

1. 5 221 NNK-ytor ligger utanför Natura 2000 — de finns i naturreservat och nationalpark och saknar områdesidentitet.
2. Öppna `natura-2000: scripts/analysis/koppla_omraden.py`. Kopiera funktionen `hamta_sci` till en variant som hämtar NVR-lagret från Naturvårdsregistret i stället, och byt fältnamnet SITE_CODE mot NVRID.
3. NVR-nedladdningen finns på `geodata.naturvardsverket.se/nedladdning/naturvardsregistret/`. `natura-2000: data/sources_sodermanland.csv` har mönstret för URL:erna.
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

1. FÖRE, ca 30 min per objekt: ta fram objektet i WebbGIS med lagren *LstD NNK Granskning* och *NV Naturtypskartan NNK* tända. Läs bevarandeplanen. Filtrera blanketten. Markera rader med karteringsstatus 3, 4 eller 5 — de har en historia.
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

**Uppdaterat 2026-08-26:** `natura-2000: docs/underlag/NRF_2026_underlag.zip` — en export av `G:\5_Naturvard_miljoskydd\` (~9 400 filer, 20 GB: skötselplaner, LIFE-projekt (CoastBenefit, Life Taiga, RestoRED, MIA, RIWUS, GrazedWoods), uppföljningsrapporter, en marin inventering 2016–17 för skärgårdsöarna, bevarandeplan-utkast) täcker det mesta av punkt 2–4 nedan redan.

**Djupgranskning klar 2026-08-26** (samma dag, "ett steg i taget"): de 38 site-specifika uppföljningsplanerna (målindikatorer per naturtyp) är inkopplade i Blanketten (ny kolumn K) och en ny geo-fil `natura-2000: data/analysis/nnk_med_uppfoljningsplan_2026.gpkg`. LIFE-projekten och den limniska vattendragskartläggningen 2022 är genomgångna — se `natura-2000: data/analysis/README.md` för detaljer per delprojekt. Viktigast: **LIFE GrazedWoods (Tynnelsö) har själva flaggat att de behöver NNK-statusklassning som en del av sitt projekt** — värt att lyfta med projektledningen för samordning innan NNK-arbetet och LIFE GW körs parallellt utan kontakt.

**Metodlärdom, viktig för punkt 3 nedan:** en ren sitecode-/N2000-namnsökning i arkivet missar underlag som ligger under ett naturreservats EGNA namn när reservatet bara delvis täcker ett N2000-område. Bekräftat geografiskt (inte bara namnmatchning) via en ny hämtning från Naturvårdsverkets Naturvårdsregistret-WFS: 121 av 195 naturreservat i länet överlappar Natura 2000, se `natura-2000: data/analysis/naturreservat_n2000_overlapp.csv`. Använd den listan som ett extra sökregister när du letar i enhetsmappar (punkt 3) — sök på reservatets namn, inte bara sitecoden eller N2000-områdets namn.

1. Börja med Per Flodin — han sitter på skötselhistorik, artkunskap och tidigare åtgärder. Gör detta ändå, arkivet ersätter inte samtalet.
2. Se `natura-2000: data/analysis/nrf_2026_underlag_per_sitecode.csv` för vad som redan finns per objekt innan du letar på egen hand.
3. Sök på enhetsmappar, i diariet, och i SkötselDOS för det som inte redan låg i G:\5_Naturvard_miljoskydd. Fråga även dem som slutat, om det går.
4. Prioritera underlag som rör de 277 ytorna med fältdata men ej bedömd status — där finns det med största sannolikhet ett protokoll någonstans.
5. Skanna in det som bara finns på papper.

### H4.2 · Registrera funna underlag i datakälleregistret

**v38–v48** · **[Karin]** · förutsätter H4.1

**Uppdaterat 2026-08-26:** för `NRF_2026_underlag.zip` är detta redan gjort automatiskt — `natura-2000: scripts/analysis/katalogisera_nrf_underlag.py` indexerade 3 697 av 9 422 filer (39 %) mot 199 sitecodes utan att öppna innehållet, se `natura-2000: data/analysis/nrf_2026_underlag_katalog.csv` (fil-nivå) och `..._per_sitecode.csv` (sitecode-nivå). `natura-2000: data/sources_sodermanland.csv` har en sammanfattningsrad som pekar dit — det är en bulkarkiv-post, inte en per-dokument-rad, eftersom den filens kolumner är gjorda för nedladdningsbara GIS-lager.

1. Lägg in varje YTTERLIGARE funnet underlag (Per Flodin-samtalet, papper som skannas in) i `natura-2000: data/sources_sodermanland.csv` med samma kolumnstruktur som finns där.
2. Ange: vad det är, vilket objekt eller vilka objekt det gäller, årtal, var det ligger, och om det är digitalt eller papper.
3. Registret är i sig en leverans — det svarar på FAQ fråga 4 om vad bedömningarna vilar på.

### H5.1 · För in förvaltarkunskapen i granskningslagret

**v38–v46** · **[Båda]** · förutsätter H3.2 · bidrar till *Ifyllda blanketter från förvaltarsamtalen*

1. Samma vecka som samtalet. Följ stegen i E3.1 för WebbGIS-redigeringen.
2. Sätt `faltinventerare` = förvaltarens namn, inte ditt.
3. Sätt `habitat_period_lastdata_end` = det årtal förvaltaren angav.
4. Sätt `forandringsorsak_forslag` (Förändringsorsak, förslag) = 3 Komplettering i nästan alla fall. 2 Faktisk förändring bara vid en verklig, daterad förändring. Samma val förs sedan in i NNK i H5.2 steg 4.
5. Skriv `Kommentar_metod` i klartext: *"Uppgift från NN, förvaltare, samtal 2026-09-24. Bygger på hens fältbesök hösten 2024 samt skötselplan 2019."*
6. Fältmappningen finns i blankettens flik *Fältmappning* — den visar vilken blankettkolumn som hamnar i vilket fält.

### H5.2 · Registrera i NNK efter avstämning

**v41–v48** · **[Johan]** · förutsätter H5.1, D1.2 · bidrar till *Tillstånd registrerat i NNK där kunskap finns; resten dokumenterat som okänt*

1. Först efter att du bedömt att underlaget räcker. Granskningslagret är förslagsnivå; NNK är skarpt.
2. Tillståndsfälten först efter driftsättningen i v40.
3. Karteringsstatus: 2 Granskad vid skrivbordet för förvaltarkunskap och dokument. 3 Besökt i fält om förvaltaren faktiskt varit där nyligen. 4 Inventerad i fält endast vid standardiserad metodik.
4. Förändringsorsak: 3 Komplettering i nästan alla fall — kunskapen fanns, den var bara inte registrerad.
5. Kör toolboxen och checka in per objekt.

### H5.3 · Skicka avstämning tillbaka till förvaltaren

**v38–v48** · **[Johan]** · förutsätter H5.1

1. Skicka en kort sammanfattning av vad du fört in, per objekt.
2. Förvaltaren ska känna igen sin egen uppgift. Gör de inte det har något gått fel i översättningen.
3. Detta är också det som gör att de svarar nästa gång du frågar.

---

## Filterguide för webbGIS

Filterguiden har en egen sida: [Filterguide för webbGIS](filterguide.html) — en flik per grupp av livsmiljötyper med de filter som ger något för just den gruppen, arbetsgång och hur träffen läses. Samma guide finns också längst ned i kontrollrummet.

**Grupper och batcher är två olika indelningar.** *Batch* (S, A, B, C, D) är arbetsordningen per Natura 2000-område — vilket objekt du tar när. *Grupp* (Hävd, Skog, Våtmark, Stabila) avgör vilken bedömningsregel i metodiken (R7A–R7D) som gäller för en enskild yta. Ett och samma objekt innehåller därför ytor från flera grupper. Tabellen visar antal ytor med Natura-naturtyp i varje batch (uttag 2026-08-26):

| Batch | Objekt | Uppgift | Hävd | Skog | Våtmark | Stabila | Marint (lämnas) |
|---|---|---|---:|---:|---:|---:|---:|
| S | Storobjekten | C2.1 | 567 | 799 | 23 | 924 | 364 |
| A | Kust och skärgård | C3.1 | 311 | 370 | 36 | 395 | 177 |
| B | Ängs- och hagmark inland | C4.1 | 147 | 55 | 18 | 16 | 1 |
| C | Våtmark och vattendrag | C5.1 | 7 | 115 | 43 | 0 | 0 |
| D | Skog och ädellöv | C6.1 | 33 | 90 | 4 | 0 | 4 |

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
| Eget fältarbete flyttas till 2027 | Arbetspaket B genomförs inte 2026 — fokus är skrivbordsgranskning och förvaltarsamtal utifrån befintlig kunskap. Inget konsultuppdrag hösten 2026 heller (D5.2 utgår): för sent på året | Beslut Johan 2026-08-25, konsultfrågan avgjord 2026-10-09 |

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

*Runbook v1.6 · genererad ur `natura-2000: scripts/analysis/uppgifter.py` med `bygg_kontrollrum.py` — redigera där, inte i den här filen*