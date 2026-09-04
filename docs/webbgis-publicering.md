# Publicera NNK-granskningslagret som WebbGIS — LstD NNK Granskning

**Version 1.0 · 2026-09-01 · Handläggare NRR, Naturskyddsenheten** · Manual för uppgifterna **A2.7** (publicera granskningslagret i portalen) och **A2.8** (skapa webbGIS). Skriven för att kunna följas på jobbdatorn utan annat stöd än detta dokument.

> **Målbild.** Ett internt WebbGIS i GK Standardmall — motsvarigheten till Stockholms *KartLitS*-webbGIS med lagret `LstAB NNK granskning` som NV:s lathund (2026-07-10) använder som exempel — där granskaren infoklickar på en NNK-polygon, klickar *Redigera*, fyller i rullistorna *Livsmiljötyp/Utbredning/Tillstånd, behov av justering*, *Vad ska kontrolleras*, *Metod för kontroll*, *Granskat* och kommentarer, och sparar med *Uppdatera*. Runt omkring: NV:s naturtypskarta, Natura 2000-gränser med länk till bevarandeplan, ängs- och betesmarksinventeringen (TUVA), ortofoto (färg/IR, årsvis), ekonomiska kartan och jordbruksblock.

Källor som manualen bygger på (alla i `natura-2000: docs/`): NV:s *Manual NNK mall för granskning* (steg 4–5), *Lathund granskning WebbGIS-KartLitS 2026-07-10* (hur slutprodukten ser ut och används), *GK Konfigurator och standardmall — Manual för producenter v.13 (2026-08-20)*, *Namnsättnings- och taggningsprincip … v2.0 (2026-04-22)*, *FO GK Riktlinjer för en stabil GIS-miljö*, Södermanlands egen *LstD GIS LOGG Publicering DriftadeGeodata* (checklista) samt GIS-funktionens användarstöd för ArcGIS Pro/portalerna.

---

## 0. Översikt och tidsåtgång

| Del | Vad | Var | Ungefärlig tid |
|---|---|---|---|
| 1 | Förbered geodatabasen: domäner (rullistor), fälttyper, alias, GlobalID, editor tracking | ArcGIS Pro, Python-fönstret | 20 min |
| 2 | Förbered kartan: lagerordning, fältsynlighet, symbol, popup, lagernamn | ArcGIS Pro | 20 min |
| 3 | Publicera som driftat lager: *Share → Web Layer* | ArcGIS Pro → intern geodataportal | 20 min + uppladdning |
| 4 | Efterarbete på item: namn, taggar, redigeringsinställningar, delning, GDK, logg | Geodataportalen (webb) | 30 min |
| 5 | Bygg WebMap: granskningslagret + referenslager, popup, formulär | Geodataportalen → Map Viewer | 45 min |
| 6 | Bygg appen i GK Konfigurator: objekt, lagerlista, widgetar, filter | Konfiguratorn (webb) | 45 min |
| 7 | Testa, döp om, dela länken, informera granskarna | Portalen + Teams/mejl | 30 min |

Räkna med en halv arbetsdag om behörigheterna är på plats, annars mer (se 0.1). Delarna kan göras i separata pass — spara efter varje del.

### 0.1 Förutsättningar (kolla FÖRST, allt annat stannar annars)

1. **Inloggad i den interna geodataportalen från ArcGIS Pro**: `https://lst-geoportal.lansstyrelsen.se/arcgis/` ska vara *Active Portal* och du ska vara *Signed in* (uppe till höger i Pro; välj *Automatisk inloggning* i rutan som dyker upp). Saknas portalen: *Project → Settings → Portals → Add Portal*. Från Pro 3.5.1 licensieras Pro dessutom mot portalen — är du inloggad så är det redan löst.
2. **Publiceringsrätt i portalen** (rollen *Publisher* eller motsvarande). Testa: i Catalog → Portal → *My Content* ska du kunna skapa en mapp (*New folder*). Kan du inte det → beställ via GIS-funktionen (`gis.sodermanland@lansstyrelsen.se`) och/eller LIAM.
3. **Medlem i gruppen `GK Standardmall – Producenter`** (intern portal) — krävs för att logga in i Konfiguratorn. Kontrollera under Portal → *Groups*. Saknas → mejla `fo.gk.team.applikation@lansstyrelsen.se` (enligt GK-manualen) med kopia till GIS-funktionen.
4. **Filerna på jobbdatorn** (från zip:en i `natura-2000/deliveries/nnk_granskning_sodermanland_20260901.zip`, hämtad från github.com): `NNK_Sodermanland_granskning.gdb`, mappen `lyrx/` och skriptet `forbered_gdb_for_publicering.py`. Dessutom KartLits-mallens gdb `KartLits_NNK_granskning.gdb` (A2.3 — behövs för domänerna i del 1). Lägg allt på en **lokal** disk, t.ex. `C:\GIS\NNK\` (inte på G:, som är långsam och ibland låser gdb-filer).
5. **Vilken portal?** Manualen utgår från den **interna** portalen och den interna Konfiguratorn — granskarna är kollegor på Länsstyrelsen, precis som i Stockholms exempel. Extern portal blir aktuell först om förvaltare utanför Länsstyrelsen ska redigera direkt (då gäller dessutom striktare regler för export och personuppgifter, se GK-manualen s.16 och 61). Bestäm inte själv om det blir aktuellt — stäm av med GIS-funktionen.

### 0.2 Namn som ska användas (bestämda enligt namnprincipen v2.0)

| Vad | Namn | Kommentar |
|---|---|---|
| Tjänstenamn vid publicering (*Name* i Share As Web Layer), NNK-lagren | `LstD_NNK_Granskning` | 19 tecken; max 40 för driftat lager. Inga åäö/mellanslag/bindestreck. Går INTE att ändra efteråt. |
| Tjänstenamn vid publicering, referenslagret | `LstD_Skyddade_Omraden` | separat tjänst, ej redigerbar |
| Item-titel (alias) i portalen, driftat lager | `LstD NNK Granskning – Driftat` | sätts på itemsidan efter publicering |
| Item-titel, referenslager | `LstD Skyddade områden (N2000 och naturreservat) – Driftat` | |
| WebMap | `LstD NNK Granskning – WebMap` | |
| Appen (WebbGIS, huvudprodukt) | `LstD NNK Granskning – WebbGIS` | |
| Tagg (identisk på ALLA items ovan) | `LstD NNK Granskning WebbGIS` | huvudproduktens namn utan tankstreck |
| Appens URL-sökväg i Konfiguratorn | `lstd_nnk_granskning` | gemener, länsprefix, unik i hela miljön |
| Visningsrubrik i appen | *NNK-granskning Södermanland* (underrubrik: *Natura 2000 — livsmiljötyper, utbredning och tillstånd*) | fritext, ändrar inte item-titeln |
| Domäner i gdb:n | `LstD_NNK_yta`, `LstD_NNK_tillstand` … | prefix enligt NV-manualens steg 3 |

---

## Del 1 · Förbered geodatabasen i ArcGIS Pro

**Varför:** Vår gdb byggdes utanför ArcGIS (Python/GDAL) för att kringgå Append-buggen. Den har rätt fält och data, men **saknar de 13 kodlistedomänerna** från KartLits-mallen. Det är domänerna som ger rullistorna i WebbGIS-formuläret (*Inget behov av justering / Ändring till annan livsmiljötyp / …*). Dessutom är några kodfält av typen Double (ska vara Long), NV:s textfält `globalid` krockar med Esris GlobalID, och vi vill ha spårning av vem som granskat vad.

Allt detta gör skriptet `forbered_gdb_for_publicering.py` (bilaga A) i ett svep. Gör så här:

1. **Ta en kopia av gdb:n först** (Utforskaren: kopiera mappen `NNK_Sodermanland_granskning.gdb` → `NNK_Sodermanland_granskning_ORIGINAL.gdb`). Skriptet ändrar schemat på plats.
2. Öppna ArcGIS Pro med ett tomt projekt (eller ditt NNK-projekt). **Ta bort NNK-lagren ur kartan** om de ligger där — Pro låser annars gdb:n och stegen misslyckas med "lock"-fel.
3. Öppna skriptet i Anteckningar (behövs oftast inte). `VAR_GDB` (vår gdb) hittas automatiskt via lagren i det aktiva Pro-projektet - lägg bara till lagren i en karta först (steg 1 ovan). `MALL_GDB` (KartLits-mallens gdb) hittas automatiskt via mappen `KartLits_mall/` som ligger bredvid skriptet i leveranszippen - fungerar oavsett om du bara laddat ner/packat upp zippen eller har hela natura-2000-repot klonat. Rätta `_RESERV_VAR_GDB`/`_RESERV_MALL_GDB` under `KONFIGURATION` bara om automatiken inte hittar rätt gdb (skriptet skriver ut en tydlig varning då). Spara.
4. *View → Python Window*. Klistra in HELA skriptet (Ctrl+A, Ctrl+C i Anteckningar → Ctrl+V i Python-fönstret) och tryck Enter. Alternativt: *Analysis → Python → Python Window*, högerklicka → *Load Code* → välj filen → Enter.
5. Läs utskriften. Förväntat: `1.` (några rader "Double → Long" på ytlagret), `2.` 13 domäner skapade (`NV_NNK_yta → LstD_NNK_yta (230 koder)` osv.), `3.`/`4.` "klart" × 3, `5.` GlobalID tillagt × 4, `6.` aktiverat × 3, `KLART`.
6. **Kontroll i Catalog:** högerklicka gdb:n → *Domains* — 13 domäner med prefix `LstD_`. Högerklicka `NNK_naturaobjekt_yta` → *Design → Fields*: kolumnen *Domain* ska vara ifylld för `naturtyp`, `granskat`, `tillstand`, `justering`, `utbredning`, `kontroll1–3`, `metod`, `livsmiljötyp1–3`, `malnaturtyp1–3` m.fl.; kolumnen *Alias* ska visa svenska namn; det ska finnas ett `GlobalID`-fält och fälten `lst_skapad_av/lst_skapad/lst_andrad_av/lst_andrad`.

**Om skriptet stannar** — vanligaste orsaker:

| Fel | Orsak | Lösning |
|---|---|---|
| `ERROR 000464: Cannot get exclusive schema lock` | gdb:n används av kartan/Catalog | ta bort lagren ur kartan, stäng Catalog-förhandsgranskning, kör igen (skriptet fortsätter där det slutade) |
| `ERROR 000800`/domännamn ogiltigt | ogiltiga tecken | kontrollera att `PREFIX = "LstD_"` inte ändrats till något med mellanslag |
| `Domain type does not match field type` | ett kodfält är fortfarande Double/Text | kör om skriptet (steg 1 konverterar); om fältet är Text: säg till, då krävs manuell fix |
| `AlterField` misslyckas på `livsmiljötyp1` | fältnamn med ö | ignorera — aliaset sätts istället i lagrets Fields-vy i del 2 |

**Utan skript (manuell reservväg, ~1 h):** *Data Management → Domains → Domain To Table* på mallens gdb (en tabell per domän) → *Table To Domain* mot vår gdb med namn `LstD_…` → *Assign Domain To Field* per fält enligt tabellen `FALT_DOMAN` i skriptet → *Add Global IDs* → *Enable Editor Tracking* (ange nya fältnamn, *Add fields* ikryssat, UTC). Byt först namn på `globalid` → `nv_globalid` via *Alter Field*.

---

## Del 2 · Förbered kartan i ArcGIS Pro

1. Ny karta (*Insert → New Map*), koordinatsystem SWEREF 99 TM (EPSG:3006) — sätts automatiskt av första lagret.
2. Lägg till de fyra lyrx-filerna från `lyrx/` (dra in från Catalog). Om de pekar fel: högerklicka lagret → *Properties → Source → Set Data Source* → peka på `NNK_Sodermanland_granskning.gdb` (en gång per lager). Lagren ska rita ut: alla NNK-objekt röda (*granskat = Nej*).
3. **Fältsynlighet — viktigast i denna del.** Högerklicka `NNK_naturaobjekt_yta` → *Data → Fields*. Slå PÅ *Visible* för **alla granskningsfält**: `granskat`, `justering`, `utbredning`, `livsmiljötyp1–3`, `kommentar_livsmil_utbred`, `tillstand`, `procent_gott`, `procent_ej_gott`, `procent_osaker`, `kommentar_tillstand`, `kontroll1–3`, `kommentar_kontroll`, `metod`, `Kommentar_metod` samt `lst_andrad_av`, `lst_andrad`. (Leveransens lyrx döljer flera av dem som standard för att hålla popupen kort — men **fält som är avstängda i lagret följer inte med i den publicerade tjänsten**, och då saknas de i WebbGIS-formuläret.) Behåll gärna avstängt: `nv_globalid`, `created_user/date`, `last_edited_user/date`, `habitat_priority_*`, `habitat_period_*`, `shape_Length/Area`. Spara (Ctrl+S i Fields-vyn). Upprepa för linje- och punktlagret.
4. **Alias:** i samma Fields-vy syns nu domänernas och aliasens effekt. Vill du ändra ordalydelse gör du det här (lagrets alias vinner över gdb:ns vid publicering).
5. **Symbol:** behåll mallens *Unique Values* på `granskat` (grön Ja / röd Nej / gul Påbörjat). Den följer med till webblagret. Kontrollera att "Övriga värden" (*Show all other values*) är på, annars försvinner objekt med okänd kod.
6. **Popup:** kommer redan färdig med lyrx-filen (steg 2) — byggd av `bygg_nnk_lyrx.py` med sex rubriksatta sektioner (*Identifiering och skydd* · *Naturtyp (NNK-data)* · *Granskning 1: Avvikelse och korrigeringsförslag* · *2: Tillstånd* · *3: Vad ska kontrolleras och metod* · *4: Granskat och kommentarer*) — tekniskt flera `CIMTableMediaInfo`-poster i `mediaInfos`, inte `Configure Pop-ups`-dialogens enda fältlista. **Bygg inte om den här.** Högerklicka → *Pop-ups* bara för att KONTROLLERA att sektionerna syns grupperade — rör ingenting. Ser popupen ogrupperad ut trots att lyrx-filen är den senaste: Pro cachar en tidigare öppnad popup-konfiguration per lager — ta bort lagret ur kartan och lägg till lyrx-filen på nytt (samma fix som för en felaktig dataConnection, se steg 2). Popupen följer med till webblagret som standardpopup och ärvs sedan automatiskt av WebMap:en i Map Viewer, del 5 — den ska INTE byggas om där heller.
7. **Display field:** *Properties → Display → Display field* = `omrade_namn` (ger begripliga träfflistor i webbGIS).
8. **Lagernamn i Contents** (det som blir undernamn i tjänsten): döp om till `NNK ytor (granskning)`, `NNK linjer (granskning)`, `NNK punkter (granskning)` och `Skyddade områden (N2000 och naturreservat)`. Undernamn får ha åäö och mellanslag — det är bara tjänstens *Name* som är begränsat.
9. **Ordning i Contents:** punkter överst, linjer, ytor, referenslagret underst (eller överst med genomskinlig fyllning som i leveransen — båda fungerar, WebbGIS-användaren kan ändå styra ritordning).
10. **Visningsintervall:** sätt gärna *Out beyond 1:250 000* på ytlagret (15 800 polygoner, varav stora vattenobjekt — utan gräns blir länsöversikten seg i webben). Referenslagret utan gräns.
11. **Överväg urval före publicering** (NV-manualens OBS i steg 4): "vill du sålla bort vissa koder eller bara behålla objekt som överlappar N2000?". Rekommendation för 2026: publicera **allt** (även *Ingen matchning* och naturreservatsobjekt) — granskningen 2026 avgränsas ändå till N2000 via filter i appen (del 6, steg 5), och vi slipper publicera om när avgränsningen ändras. Marina objekt (naturtyp 1000-serien) ska enligt FAQ 16/29 inte granskas i NNK 2026 — även dessa hanteras med filter, inte genom att ta bort dem.
12. Spara projektet (t.ex. `C:\GIS\NNK\LstD_NNK_Granskning_publicering.aprx`) — det behövs igen vid nästa Ajourhålla-uttag.

---

## Del 3 · Publicera som driftat lager (Share → Web Layer)

Publicera **två** gånger: först NNK-lagren (tre lager i en tjänst), sedan referenslagret (egen tjänst, så att det kan vara oredigerbart och delas bredare).

**Tjänst 1 — NNK-lagren**

1. Markera de tre NNK-lagren i Contents (Ctrl-klick). Fliken *Share → Web Layer → Publish Web Layer* (välj *Selected layers* om Pro frågar).
2. Fliken **General**:
   - *Name*: `LstD_NNK_Granskning` (exakt så; namnet är låst efter publicering).
   - *Summary*: "Granskningskopia av NNK Ajourhålla för Södermanlands län (uttag 2026-08-26), attribuerad med områdesnamn, skyddskategori och län. Granskningsfält enligt KartLitS-mallen. Ansvarig: Naturskyddsenheten/NRR."
   - *Tags*: `LstD NNK Granskning WebbGIS` (huvudtaggen) + `NNK`, `Natura 2000`, `naturrestaurering`.
   - *Layer Type*: **Feature** (inte Map Image — riktlinje 1: map image layers får inte publiceras till hosted).
   - *Location → Folder*: skapa/välj mappen `LstD NNK` i My Content.
   - *Share with*: **bara** gruppen `GK Standardmall – Producenter` och/eller en egen grupp för granskarna (riktlinje 3: dela restriktivt; INTE *Organization*). Se del 4 för slutlig delning.
3. Fliken **Configuration** → klicka på pennan vid *Feature*:
   - *Operations*: kryssa **Enable editing** och *Add, update and delete features* → begränsa i del 4 till *Update attributes only*. (Du kan sätta det direkt här om ditt Pro visar valet "Update attributes only".)
   - *Enable Sync* — **av** (behövs inte, och sync utlöser fler analyskrav).
   - *Export data* — **av**.
   - *Properties*: **Attachments AV** (riktlinje 2: driftade lager utan bilagor).
   - *Time zone* (om dialogen visar "Date fields time zone"): välj *W. Europe Standard Time (Stockholm)* — NV:s datumfält är i svensk tid.
4. Klicka **Analyze**. Vanliga meddelanden:
   - *24011 Unique numeric IDs are not assigned* — högerklicka meddelandet → *Assign unique IDs automatically* (eller *Map Properties → General → Allow assignment of unique numeric IDs*). Motsvarar loggens "Unique Ids aktiverat på kartan".
   - *00230/00231 Layer's data source should have GlobalID / editor tracking* — löst av del 1.
   - *00068 Layer draws at all scale ranges* — varning, hanterad av steg 2.10.
   - Röda fel (❌) måste åtgärdas; gula varningar går att publicera trots.
5. **Publish**. 15 800 polygoner tar några minuter. Klicka *Manage the web layer* i klarmeddelandet → itemsidan öppnas i portalen (lämna fliken öppen inför del 4).

**Tjänst 2 — referenslagret**

Samma sak för `Skyddade_omraden`: *Name* `LstD_Skyddade_Omraden`, samma taggar, **Enable editing AV**, *Export data* kan vara på (data är öppna NV-data). Summary: "Natura 2000-siter (SCI/SPA) och naturreservat/nationalparker i och runt Södermanland, från Naturvårdsverkets Naturvårdsregistret 2026-09. Referenslager för NNK-granskningen."

**Kontroll:** i Catalog → Portal → My Content → mappen `LstD NNK` ska det finnas två *Feature Layer (hosted)*-items. Högerklicka → *Add To Current Map*, kolla i *Properties → Source* att källan är `https://lst-hostedgeodata.lansstyrelsen.se/arcgis/rest/services/Hosted/LstD_NNK_Granskning/FeatureServer` (så vet du att kartan nu läser från portalen, inte lokala filen).

---

## Del 4 · Efterarbete på items i Geodataportalen (webbläsaren)

Öppna `https://lst-geoportal.lansstyrelsen.se/arcgis/` → *Content* → mappen `LstD NNK`. För **varje** av de två items:

1. **Titel** (Overview → penna vid titeln): `LstD NNK Granskning – Driftat` resp. `LstD Skyddade områden (N2000 och naturreservat) – Driftat`. (Titeln är ett alias; tjänstnamnet i URL:en förblir `LstD_NNK_Granskning`.)
2. **Taggar**: kontrollera att `LstD NNK Granskning WebbGIS` finns; lägg till om Pro tappade den.
3. **Beskrivning**: kort text om innehållet, ansvarig (NRR-handläggare, Naturskyddsenheten), datum för uttaget, samt — när metadataposten finns (steg 7) — länken till den. Ange också: "Redigering: endast attribut. Ta INTE bort objekt."
4. **Settings-fliken, NNK-tjänsten** (avsnittet *Feature layer (hosted)*):
   - *Editing*: **Enable editing** ✔.
   - *What kind of editing is allowed?*: **Update** ✔ (Add ✘, Delete ✘). Under Update: **Attributes only** (om alternativet finns i er portalversion 11.5 — annars *Attributes and geometry* och instruera granskarna att inte flytta gränser).
   - *Track edits*: **Keep track of who created and last updated features** ✔ (använder fälten från del 1 steg 6). *Editors can only see/edit their own features* ✘.
   - *Export data*: ✘. *Sync*: ✘.
   - *Layer optimization / Indexes*: ingen ändring.
   Spara.
5. **Settings-fliken, referenstjänsten**: *Enable editing* ✘, *Export data* ✔ (frivilligt).
6. **Delning** (*Share*): dela med den grupp granskarna ingår i. Finns ingen lämplig grupp: skapa gruppen `LstD NNK Granskning` (Groups → Create group; *Who can view*: endast medlemmar; *Who can contribute*: gruppägare/medlemmar) och bjud in granskarna med länsstyrelsekontot. Dela **båda** items + (senare) WebMap + app med samma grupp. Producenter-gruppen behövs bara för Konfiguratorn. *Everyone/Organization*: nej.
7. **Metadatapost i Geodatakatalogen (GDK)** — principen kräver en post för huvudprodukten (appen), skapa den när appen finns (del 7). Titel = `LstD NNK Granskning – WebbGIS`; lägg in taggens portal-URL (klicka på taggen i portalen och kopiera adressen) som *Onlinekälla* med protokoll *ESRI Portal*; lägg sedan metadatapostens URL i appens/lagrets *Beskrivning*. Frågor om GDK → GIS-funktionen.
8. **Logga i `LstD_GIS_LOGG_Publicering_DriftadeGeodata`** (GIS-funktionens SharePoint; kopia i `natura-2000: docs/D_GIS_manualer/Portalerna/`): ny rad per driftat lager med ansvarig GIS-are, informationsförvaltare, chef informerad, syfte, publiceringsdatum, REST-länk, delning. Kolumnerna i loggen är exakt de kontroller som gjorts i del 1–4 — bocka av.

---

## Del 5 · Bygg WebMap i Map Viewer

Konfiguratorn läser lager **bara via WebMaps** (GK-manualen s.14). WebMap:en är också där popup, formulär och referenslager konfigureras.

1. Portalen → *Map* (Map Viewer, inte Classic). *Add → Browse layers → My Content* → lägg till `LstD NNK Granskning – Driftat` (alla tre undernivåer följer med som grupp) och `LstD Skyddade områden … – Driftat`.
2. **Referenslager** — sök i *Browse layers → My Organization* (eller *Groups → Södermanland – Karttjänster* och de nationella grupperna) på följande och lägg till dem som finns. Skriv ned exakta item-namn i loggen — de behövs igen i Konfiguratorn:
   - "Naturtypskartan" / "NNK" — NV:s naturtypskarta med naturtypsfärger (*NV Naturtypskartan NNK* i Stockholms app).
   - "Natura 2000" — områdesgränser med bevarandeplanlänk (*NV Natura2000 områden*; fältet `BEVPLAN`).
   - "Ängs- och betesmark" / "TUVA" — inventeringen med TUVA-länk.
   - "Ortofoto" — Lantmäteriets ortofoto färg (årsvis) och IR (*LM Ortofoto* / *LM Historiska ortofoton – WMS*).
   - "Ekonomiska kartan" (50-talet), "Jordbruksblock" (senaste år), "Naturreservat"/"Skyddad natur", "Fastighetskarta".
   Nationella karttjänster som redan finns i portalen behöver **inte** kopieras in i vår WebMap — de kan istället läggas till direkt i Konfiguratorns lagerlista från sina egna WebMaps (del 6, steg 4). Lägg in i vår WebMap endast det som saknas i portalen. Saknas NV:s Natura 2000-lager helt: *Add → Layer from URL* → `https://geodata.naturvardsverket.se/naturvardsregistret/wfs` (WFS, öppna data) — undantagsfall, kräver att URL:en är nåbar från jobbnätet.
3. **Ordning** (uppifrån): NNK punkter, NNK linjer, Skyddade områden (kontur), NNK ytor, NV naturtypskarta (släckt vid start), Natura 2000-gränser, ängs- och betesmark (släckt), ortofoton (släckta), bakgrund. Slå på *Visible* bara för NNK-lagren, skyddade områden och N2000-gränser vid start.
4. **Symbol**: kommer från Pro. Vill du ha kontur i stället för fyllning på NNK-ytorna (så naturtypskartan syns igenom): *Styles → Types (unique symbols)* på `granskat`, tjock kontur grön/röd/gul, fyllning 70 % genomskinlig.
5. **Popup** per NNK-lager (*Pop-ups*): **redan klar — ärvs automatiskt** från lagrets publicerade popup (del 2 steg 6), med samma sex rubriksatta sektioner som i Pro, inklusive granskningsstegen 1–4 som lässtöd. (Det är alltså MEDVETET att granskningsfälten syns i popupen och inte bara i formuläret — en tidigare version av den här manualen sa motsatsen, "håll granskningsfälten ur popupen"; det stämmer inte längre.) Kontrollera bara: öppna *Pop-ups* på ytlagret → sektionerna ska synas grupperade, med rubrik `{omrade_namn}` överst — bekräftat att detta stämmer 2026-09-04. Gör INGEN ny fältlista. Ser popupen i stället ogrupperad ut (platt fältlista utan rubriker): lagret lades troligen till i WebMap:en innan popup-uppdateringen i Pro — ta bort och lägg till lagret på nytt från portalen (samma cache-orsak som del 2 steg 6). Lägg sist till (manuellt, en gång) ett *Text*-element sist i listan: "Redigera via knappen Redigera → välj lager LstD NNK Granskning → klicka på objektet." Slå på *Pop-ups* även på referenslagren (N2000: så att bevarandeplanlänken syns).
6. **Formulär (smart form)** — det som gör att formuläret ser ut som Stockholms: markera NNK-ytlagret → *Forms → Configure*. Dra in fälten i denna ordning och gruppera (*Group*-element):
   - **Grupp "1. Avvikelse och korrigeringsförslag"** (bytte namn 2026-09-03 för att spegla samma
     ombenämning som Pro-popupens grupper, se README.md i leveransmappen): Livsmiljötyp, behov av
     justering · Utbredning, behov av justering · Livsmiljötyp 1 · Livsmiljötyp 2 · Livsmiljötyp 3 ·
     Kommentar – livsmiljötyp och utbredning.
     *Gruppbeskrivning:* "Fyll i bara vid fel klassificering — förslag på rätt typ (max 3, prioritetsordning). OBS: igenväxning pga utebliven skötsel ändrar INTE livsmiljötypen (sätt i stället Tillstånd = Icke gott). Inte samma sak som utvecklingsmark."
     Lägg dessutom till ett **Info-element** överst i gruppen, för utförligare bakgrund och citat:
     "Igenväxning på grund av utebliven skötsel är den vanligaste och allvarligaste fällan i
     granskningen. Ändra INTE livsmiljötypen av det skälet — sätt i stället Tillstånd = Icke gott.

     Lathunden ('Vad kan vi ändra på?'): 'Behåll dock livsmiljötypen om en faktisk förändring
     beror på brist på nödvändiga bevarandeåtgärder – det är inte en giltig anledning att ändra,
     snarare har länen skyldighet att vidta nödvändiga bevarandeåtgärder. Ytan är då förmodligen
     i Icke gott tillstånd.'

     Utvecklingsmark (framtida potential) är en annan sak än en korrigering av nuvarande typ —
     förutsätter Naturtypsstatus = Utvecklingsmark och att nuvarande Naturtyp INTE redan är en
     livsmiljötyp.

     Utpekade livsmiljötyper (grund för N2000-områdets urval) har särskilt skydd — kolla
     bevarandeplanen (fältet BEVPLAN i N2000-lagret) innan du föreslår ändring; ändra bara vid
     uppenbart fel eller faktisk förändring (FAQ 19)."
   - **Grupp "2. Tillstånd"**: Tillstånd, behov av justering · Gott tillstånd (%) · Ej gott tillstånd (%) · Osäker (%) · Kommentar – Tillstånd.
     *Gruppbeskrivning:* "Bedöm gott/icke gott/okänt tillstånd (struktur, funktion, typiska arter).
     Blandat inom ytan: ange andel gott/ej gott/osäker i procent (summa 100). Osäker? Välj
     Okänt/Icke gott — gissa inte."
   - **Grupp "3. Vad ska kontrolleras och hur"**: Vad ska kontrolleras 1–3 · Kommentar – Vad ska kontrolleras · Metod för kontroll · Kommentar – Metod.
     *Gruppbeskrivning:* "Framåtsyftande: vad bör kontrolleras/inventeras inför 2027, och med
     vilken metod. Beskriv INTE hur du kom fram till dagens bedömning här — det hör hemma som
     kommentar under Avvikelse/Tillstånd."
   - **Grupp "4. Klart?"**: Granskat.
     *Gruppbeskrivning:* "Sätt Ja när ytan är färdiggranskad och fälten ovan är ifyllda. Påbörjat =
     delresultat, inte klart än. Nej är standardläget för ogranskade objekt."
   - **Beskrivning per fält** — sätt enligt lathundens text (klicka på fältet i formuläret → Beskrivning):
     - **Livsmiljötyp, behov av justering:** Ändra bara vid fel klassificering eller faktisk förändring — inte vid igenväxning pga utebliven skötsel (sätt då Tillstånd = Icke gott i stället).
     - **Utbredning, behov av justering:** Ändra bara om gränsen är fel och avvikelsen är minst lika stor som minsta karteringsenhet.
     - **Livsmiljötyp 1:** Förstahandsförslag på rätt livsmiljötyp, vid fel klassificering.
     - **Livsmiljötyp 2:** Andrahandsförslag, om osäker mellan flera typer.
     - **Livsmiljötyp 3:** Tredjehandsförslag, om osäker mellan flera typer.
     - **Kommentar – livsmiljötyp och utbredning:** Grund för bedömningen (skötselplan, bevarandeplan, fältbesök …) och när kunskapen är ifrån.
     - **Tillstånd, behov av justering:** Gott = bra skick. Icke gott = igenvuxen/behöver restaurering, även vid utebliven skötsel. Okänt = kan inte bedömas — ange skälet i kommentaren.
     - **Gott tillstånd (%):** Andel av ytan i gott tillstånd om blandat. Summan av de tre procentfälten ska bli 100.
     - **Ej gott tillstånd (%):** Andel av ytan i icke gott tillstånd om blandat. Summan av de tre procentfälten ska bli 100.
     - **Osäker (%):** Andel av ytan där tillståndet är osäkert. Summan av de tre procentfälten ska bli 100.
     - **Kommentar – Tillstånd:** Grund för bedömningen. Vid osäkerhet: dokumentera vad ni inte vet i stället för att gissa.
     - **Vad ska kontrolleras 1–3:** Vad som bör kontrolleras/inventeras inför 2027: typiska arter, strukturer, hävd, funktioner, morfologi eller annan negativ påverkan.
     - **Kommentar – Vad ska kontrolleras:** Motivera varför just detta bör kontrolleras.
     - **Metod för kontroll:** Framåtsyftande — vilken metod BÖR användas 2027 (fältbesök, fältinventering, skrivbord, annan), inte hur du gjort hittills.
     - **Kommentar – Metod:** Kompletterande info om vald metod, t.ex. varför fältinventering behövs.
     - **Granskat:** Ja = färdiggranskad, fälten ovan ifyllda. Påbörjat = delresultat. Nej = standardläge för ogranskade objekt.
   - Lämna NV:s ursprungsfält (naturtyp, naturtypsstatus, kommentar …) UTANFÖR formuläret eller som *read-only* — det är bara mallens granskningsfält som ska ändras (lathunden: "Vad kan vi ändra på?"). Villkorlig synlighet är möjlig (Arcade-uttryck, t.ex. procentfälten bara när `tillstand == 3`) men inte nödvändig i första versionen.
   Gör samma sak för linje- och punktlagret (kopiera formulär går inte — det är 3 + 5 + 6 + 1 fält per lager, går fort).
7. **Kartans utgångsläge**: zooma till Södermanlands län. *Map properties → Item details*.
8. **Spara**: *Save as* → titel `LstD NNK Granskning – WebMap`, tagg `LstD NNK Granskning WebbGIS`, mapp `LstD NNK`, sammanfattning. **Dela** WebMap:en med samma grupp som lagren (annars kan Konfiguratorn/appen inte visa lagerlistan för granskarna — GK-manualen s.34).

---

## Del 6 · Bygg appen i GK Konfigurator

Intern Konfigurator: `https://lst-webbgis-konfigurator.lansstyrelsen.se/` (logga in med portalkontot; kräver Producenter-gruppen). Arbetsflödet är GK-manualens 10 steg (s.6). Alla ändringar kräver **Spara** (knappen längst till vänster i varje flik).

1. **Appar → Skapa**. Mall: *GK Standardmall* (intern), **senaste version**. Titel: `LstD NNK Granskning – WebbGIS`. Spara → ett item skapas i portalen.
2. **Fliken Objekt**: *Uppdatera mall automatiskt* PÅ (rekommenderat). *Sökväg*: `lstd_nnk_granskning` (validering visar om upptagen). Fyll i Sammanfattning/Beskrivning/Taggar (`LstD NNK Granskning WebbGIS`) — de skrivs till portal-itemet. *Katalog*: Natur/Naturvård om valet finns.
3. **Fliken Allmänt**: hoppa över (ingen konfiguration).
4. **Fliken Lagerlista**:
   - *Datakällor → Lägg till*: sök `LstD NNK Granskning` → markera vår WebMap → Lägg till. Sök därefter fram de nationella WebMaps som motsvarar referensunderlagen från del 5 steg 2 (sök på "Naturtypskarta", "Natura 2000", "Ängs- och betesmark", "Ortofoto", "Historiska ortofoton", "Ekonomiska kartan", "Jordbruksblock", "Naturvårdsverket"). Markera en–två WebMaps i taget (prestanda).
   - *Urval av datakällor*: bocka i vår WebMap → den dyker upp under *Tillgängliga lager*.
   - *Använda lager*: skapa grupper (knappen *Ny grupp*) med denna struktur och dra in lagren:
     1. **Granskning** — `LstD NNK Granskning` (hela tjänsten som grupp: punkter, linjer, ytor) + `Skyddade områden`. Tända vid start. Gruppinställning: *Tillåt tänd alla* ✔, fet titel.
     2. **Naturvårdsverket** — Naturtypskartan NNK (släckt), Natura 2000-områden (tänt), naturreservat/skyddad natur (släckt).
     3. **Jordbruk och hävd** — ängs- och betesmarksinventeringen (TUVA-länk), jordbruksblock.
     4. **Ortofoto och historiska kartor** — ortofoto färg (årsvis), ortofoto IR, ekonomiska kartan 50-tal. För *LM Historiska ortofoton – WMS*: avaktivera lagren "Ortofoto YYYY" och behåll "YYYY ortofoton, 1 m, sv_v" (känd utskriftsbugg, GK-manualen s.50).
     5. **Fastighet och administrativt** — fastighetskarta, kommun/länsgräns.
   - Lagerinställningar (fäll ut gruppen, ikonerna per lager):
     - **Sökbart** (förstoringsglaset) på NNK ytor: sökfält `omrade_namn` och `n2000_sitecode`; på Skyddade områden: `omrade_namn`, `sitecode`. Då hittar granskaren sitt område i *Sök i kartan*.
     - **Redigeringsinställningar** (pennan) på NNK ytor/linjer/punkter: *Gör tjänsten redigerbar* ✔ → tillåt *Uppdatera attribut* ✔, *Lägg till* ✘, *Ta bort* ✘, *Geometri* ✘ (om valen finns), *Fältkalkylator i attributtabellen* ✘ (skydd mot massändring av misstag). **OBS:** den här vägen (inte bara widgeten) krävs för att formulären från del 5 steg 6 ska slå igenom (GK-manualen s.27 och 47).
     - Popup på: alla utom rena bakgrundslager.
   - *Bakgrunder*: välj en ljus bakgrund (t.ex. LM Topografisk webbkarta nedtonad) som start.
   - *Kartans utgångsläge*: aktivera, zooma till Södermanland, Spara.
   - **Exportera lagerlistan** (knappen *Export* överst) → spara JSON-filen i `natura-2000: deliveries/nnk_granskning_sodermanland_20260901/` — backup om en WebMap försvinner ("Etikett kan inte hittas i WebMap", s.28).
5. **Fliken Filter** (ger granskaren snabbknappar; ersätter urvalet vi INTE gjorde i del 2 steg 11). *Nytt filter* → *Gruppfilter*, datakälla NNK ytor + linjer + punkter:
   - "Bara Natura 2000" — `skyddskategori` *innehåller* `Natura 2000` — **aktivt vid start** (lathunden: granskningen avgränsas till N2000-områden).
   - "Ej granskade" — `granskat` = 2.
   - "Påbörjade" — `granskat` = 3.
   - "Dölj marint (naturtyp 1000-serien)" — enkelt filter på ytlagret: `naturtyp < 1000 OR naturtyp >= 2000` (FAQ 16/29: marint ska inte in i NNK 2026).
   - "Mitt område" — enkelt filter, `omrade_namn`, *Fråga efter värde* ✔ (granskaren skriver in namnet).
   Kombinera filtren med **OCH**. Aktiverande verktyg: *Nollställ alla* och *Stäng av alla* ✔.
6. **Fliken Widgetar** — aktivera (✔) följande, resten av (≈ Stockholms app + attributtabell):
   - *Meny och inloggning*: **Inloggning krävs** ✔ (WebMap:en är inte publik, och redigering kräver inloggad användare med redigeringsroll). Logotyp: länets, via HTTPS-URL på `\\lansstyrelsen.se\lst_kartor\dokument\Sodermanland\…` (fråga GIS-funktionen efter befintlig logo-URL) eller lämna standard. Rubrik/underrubrik enligt tabell 0.2. Länksamling: knapp **"Lathund granskning"** → länk till NV:s lathund (Samverkansytan) eller till `https://ulfboge.github.io/nnk-granskning-2026/docs/runbook.html`; knapp **"Kodlista/attributbeskrivning"**; knapp **"Granskningslogg (G:)"** kan inte länkas (filsökväg), skriv sökvägen i välkomsttexten i stället. *Sidofält utfällt vid start* ✔ med *Lagerlista* öppen.
   - *Information*: statisk välkomstruta ✔: rubrik "NNK-granskning Södermanland 2026", text: syfte (var har vi kunskap/var saknas — plan för 2027), vem (Naturskyddsenheten/NRR), hur (Redigera → välj lager → klicka polygon → fyll i → Uppdatera; *Ta bort* raderar objektet — klicka *Behåll geoobjektet* om du råkar trycka), var loggen ligger (`G:\5_Naturvard_miljoskydd\51_skydd_omr_arter_mm\511_skydd_omr_arter\NRF\granskningslogg_mall.xlsx`), kontakt (din mejl).
   - *Lagerlista* ✔ (sidofält; *Automatisk popup* ✔; dölj inget), *Attributtabell* ✔ (paginering 50 rader, filtrera på kartutbredning ✔ — bra att kunna sortera på `granskat`), *Redigera* ✔ (sidofält; *Inkludera alltid alla redigerbara lager* ✘ — vi styr per lager i Lagerlistan), *Sök i kartan* ✔ (geografisk avgränsning: län Södermanland; plats/fastighet/adress + våra söklager), *Välj i kartan* ✔, *Rita och mät* ✔, *Bokmärken* ✔, *Dela karta* ✔, *Skala* ✔, *Visa koordinater* ✔, *Visa teckenförklaring* ✔, *Utskrift* ✔ (standardlayouter, A3 liggande), *Filter* ✔ (sidofält), *Export* ✔ men bara Excel, endast från Attributtabell (för att exportera granskningsläget till loggen), *Popupfunktioner* ✔, *Högerklick-meny* ✔, *Artsök* ✔ (FO Natur — artfynd från Artportalen, nyttigt för typiska arter), *Ärendekontroll* ✘, *Lägg till data* ✔ (fil + portal; granskaren kan dra in egna shapefiler), *Höjdprofil* ✘, MarkGIS/Små avlopp ✘.
7. **Fliken Förhandsgranska** → kolla lagerlista, filter, formulär. Tillbaka till *Objekt → Starta* för att öppna appen i egen flik.

---

## Del 7 · Test, namn, delning och överlämning

1. **Redigeringstest** (gör det själv innan någon annan får länken): öppna appen → *Logga in → Automatisk inloggning* → zooma till ett välkänt område → *Redigera* → *Välj lager att redigera: NNK ytor (granskning)* → *Redigera geoobjekt* → klicka på en polygon → formuläret ska visa grupperna 1–4 med **rullistor** (om du ser tomma textrutor i stället saknas domänerna — tillbaka till del 1) → sätt *Granskat = Påbörjat*, skriv testkommentar → **Uppdatera**. Polygonen ska bli gul direkt. Öppna attributtabellen → `Granskad av` ska visa ditt konto och `Granskad datum` nu. Återställ till *Nej* och tom kommentar.
2. **Negativt test**: kontrollera att *Ta bort* antingen saknas eller stoppas (vi stängde av Delete i del 4/6). Kontrollera att NV:s ursprungsfält inte går att ändra i formuläret.
3. **Kollega-test**: be en kollega i granskargruppen (utan Producenter-roll) öppna länken, logga in och göra samma sak. Kan hen inte redigera → hen har bara *visningsroll* i portalen (GK-manualen s.34); GIS-funktionen höjer rollen till *Editor/User*.
4. **Itemnamn i portalen**: leta upp appens item (*Content → LstD NNK*) → titel `LstD NNK Granskning – WebbGIS`, tagg, beskrivning med GDK-länk. Dela med granskargruppen (samma som lagren + WebMap). Kontrollera att alla fyra items (2 driftade, WebMap, WebbGIS) har taggen — klicka på taggen: alla fyra ska listas.
5. **GDK-metadatapost** (del 4 steg 7) och **LstD-loggen**: fyll i kolumnerna "Fältkarta/WebbGIS" (Lagt till i webbGIS, Kontrollerat funktion, länk till webbGISet).
6. **Överlämning**: mejla/Teams:a granskarna appens länk (`https://lst-webbgis.lansstyrelsen.se/lstd_nnk_granskning/` — kopiera den exakta adressen från *Starta*), NV:s lathund, och instruktionen om granskningsloggen på G:. Boka en 30-minuters genomgång. Bocka av A2.7/A2.8 i kontrollrummet.
7. **Kommunicera** till Naturskyddsenheten/GIS-funktionen att `LstD NNK Granskning` finns, så att ingen publicerar en parallell kopia.

---

## Del 8 · Felsökning och drift

| Symptom | Trolig orsak | Åtgärd |
|---|---|---|
| Formuläret i WebbGIS visar fritextfält, inga rullistor | domäner saknas i tjänsten | del 1; publicera om (Share → *Overwrite Web Layer* från samma projekt) |
| Granskningsfält saknas i formuläret/popupen | fältet var dolt i Pro-lagret vid publicering | slå på *Visible* (del 2 steg 3), *Overwrite Web Layer* |
| Popupen i Map Viewer syns som platt fältlista utan rubriker, inte sex sektioner | lagret tillagt i WebMap:en innan popup-uppdateringen — Portalen cachar precis som Pro | ta bort lagret ur WebMap:en, lägg till det på nytt från portalen (del 5 steg 5) |
| "Du har inte behörighet att redigera" | visningsroll i portalen, eller redigering av på itemet/lagret | del 4 steg 4, del 6 steg 4; roll via GIS-funktionen |
| Lagerlistan tom / "Etikett kan inte hittas i WebMap" | WebMap inte delad med användaren, eller borttagen | dela WebMap med gruppen; GK-manualen s.28 (importera exporterad lagerlista) |
| Appen kräver inloggning men lagren syns inte | driftat lager ej delat med gruppen | dela itemet (del 4 steg 6) |
| Segt vid länsöversikt | ytlagret ritas i alla skalor | visningsintervall (del 2 steg 10) eller i Map Viewer *Visibility range* |
| Fel färg/inga objekt | renderer utan "övriga värden"; `granskat` null | i Map Viewer: *Styles → other values* ✔; i data: `granskat=2` som default (redan satt i leveransen) |
| Tjänstnamnet blev fel | *Name* kan inte ändras | ta bort itemet, publicera om med rätt namn (gör det innan WebMap/app byggs) |
| Nytt Ajourhålla-uttag (t.ex. efter NV:s nya attribut i slutet av sept. 2026) | ny data, samma schema | kör om pipeline + del 1, sedan *Overwrite Web Layer* — **OBS: skriver över granskarnas ifyllda fält**. Exportera först attributtabellen (Excel) och slå ihop, eller vänta med överskrivning tills granskningen är klar. Om schemat ändras: ny tjänst + ny version av WebMap. |
| Konfiguratorn nere | driftsättning (fredagar 10.30–12, se driftinfo) | vänta; appen fungerar under tiden |
| Frågor | | GK Konfigurator/portal: `giampaolo.cocca@lansstyrelsen.se` (NV-manualen), `fo.gk.team.applikation@lansstyrelsen.se` (GK), GIS-funktionen `gis.sodermanland@lansstyrelsen.se`; NNK-data: `Sandra.Wennberg@naturvardsverket.se` |

---

## Bilaga A · Skriptet `forbered_gdb_for_publicering.py`

Ligger i `natura-2000: deliveries/nnk_granskning_sodermanland_20260901/forbered_gdb_for_publicering.py` (och i zip:en). Kopia här så att det går att kopiera från webbsidan:

```python
# -*- coding: utf-8 -*-
"""Förbereder NNK_Sodermanland_granskning.gdb för publicering (domäner, typer,
alias, GlobalID, editor tracking, metadata). Körs i ArcGIS Pro:s Python-fönster."""
import os
import arcpy
from arcpy import metadata as md

def _hitta_mall_gdb():
    """Mallens gdb följer med i leveranszippen (KartLits_mall/ bredvid det här
    skriptet) - funkar utan git/klonat repo. Provar även repo-relativt
    (docs/underlag/handledning/...) om hela natura-2000 är klonat, sen
    reservsökvägen."""
    kandidater = []
    try:
        har = os.path.dirname(os.path.abspath(__file__))
        kandidater.append(os.path.normpath(os.path.join(
            har, "KartLits_mall", "KartLits_NNK_granskning.gdb")))
        kandidater.append(os.path.normpath(os.path.join(
            har, "..", "..", "docs", "underlag", "handledning",
            "KartLits_NNK_GIS_mall", "KartLits_NNK_granskning.gdb")))
    except NameError:
        pass
    kandidater.append(_RESERV_MALL_GDB)
    for k in kandidater:
        if arcpy.Exists(k):
            return k
    return None

_RESERV_MALL_GDB = r"C:\GIS\NNK\KartLits_NNK_GIS_mall\KartLits_NNK_granskning.gdb"
MALL_GDB = _hitta_mall_gdb() or _RESERV_MALL_GDB
PREFIX = "LstD_"
GOR_GLOBALID = True
GOR_EDITOR_TRACKING = True
GOR_METADATA = True

NNK_LAGER = {"NNK_naturaobjekt_yta": "NV_NNK_yta",
             "NNK_naturaobjekt_lin": "NV_NNK_linje",
             "NNK_naturaobjekt_pkt": "NV_NNK_punkt"}

def _hitta_gdb_fran_projektlager(kandidatnamn):
    """Hittar gdb-sökvägen via ett lager i AKTIVA Pro-projektet vars namn finns
    i kandidatnamn (lyr.connectionProperties['connection_info']['database']).
    Returnerar None om inget/flera projekt-gdb:er hittas."""
    try:
        aprx = arcpy.mp.ArcGISProject("CURRENT")
    except OSError:
        return None
    hittade = set()
    for karta in aprx.listMaps():
        for lyr in karta.listLayers():
            if lyr.name not in kandidatnamn or not lyr.supports("DATASOURCE"):
                continue
            try:
                cp = lyr.connectionProperties
            except Exception:
                continue
            if not cp or cp.get("workspace_factory") != "File Geodatabase":
                continue
            gdb = (cp.get("connection_info") or {}).get("database")
            if gdb:
                hittade.add(gdb)
    return hittade.pop() if len(hittade) == 1 else None

_RESERV_VAR_GDB = r"C:\GIS\NNK\nnk_granskning_sodermanland_20260901\NNK_Sodermanland_granskning.gdb"
VAR_GDB = _hitta_gdb_fran_projektlager(set(NNK_LAGER) | {"Skyddade_omraden"}) or _RESERV_VAR_GDB

_BEHOVDA_DOMANER = (set(FALT_DOMAN.values()) - {"NATURTYP", "LST_NNK_tillstand"}) | set(NNK_LAGER.values())

FALT_DOMAN = {
    "naturtyp": "NATURTYP", "livsmiljötyp1": "NATURTYP", "livsmiljötyp2": "NATURTYP",
    "livsmiljötyp3": "NATURTYP", "malnaturtyp1": "NATURTYP", "malnaturtyp2": "NATURTYP",
    "malnaturtyp3": "NATURTYP", "komplex": "NV_NNK_Komplex",
    "naturtypsstatus": "NV_NNK_Naturtypsstatus", "karteringsstatus": "NV_NNK_Karteringsstatus",
    "forandringsorsak": "NV_NNK_Förändringsorsak", "ursprung": "NV_NNK_Ursprung",
    "tillstand": "LST_NNK_tillstand", "justering": "LST_NNK_justering",
    "utbredning": "LST_NNK_utbredning", "kontroll1": "LST_NNK_kontroll",
    "kontroll2": "LST_NNK_kontroll", "kontroll3": "LST_NNK_kontroll",
    "metod": "LST_NNK_metod", "granskat": "LST_NNK_granskad",
}

# Tillagt 2026-09-03: mallens egen domän för `tillstand` visade sig omatchad mot både
# blanketten och NV:s FAQ ("gott, inte gott eller okänt tillstånd") - kopieras inte,
# byggs som egen domän i steg 2b i stället. Se README.md/naturtyp_koder.TILLSTAND_TEXT.
EXKLUDERA_MALLDOMANER = {"LST_NNK_tillstand"}
TILLSTAND_KORRIGERAD_DOMAN = {1: "Gott", 2: "Icke gott", 3: "Okänt – kan ej bedöma",
                               4: "Blandat – se andelar"}

ALIAS = {
    "omrade_namn": "Områdesnamn", "skyddskategori": "Skyddskategori",
    "lan": "Län (skyddat område)", "n2000_sitecode": "Natura 2000-kod (SE-nummer)",
    "n2000_namn": "Natura 2000-namn", "n2000_typ": "Natura 2000-typ (SCI/SPA)",
    "n2000_lan": "Län (N2000-siten)", "naturreservat_namn": "Naturreservat-namn",
    "naturreservat_nvrid": "Naturreservat-ID (NVRID)", "naturreservat_lan": "Län (naturreservatet)",
    "naturtyp": "Naturtyp (livsmiljötyp)", "naturtyp_text": "Naturtyp (klartext)",
    "naturtypsstatus": "Naturtypsstatus (tillstånd)", "naturtypsstatus_text": "Naturtypsstatus (klartext)",
    "karteringsstatus": "Karteringsstatus", "karteringsstatus_text": "Karteringsstatus (klartext)",
    "malnaturtyp1": "Målnaturtyp 1", "malnaturtyp2": "Målnaturtyp 2", "malnaturtyp3": "Målnaturtyp 3",
    "malnaturtyp1_text": "Målnaturtyp 1 (klartext)", "malnaturtyp2_text": "Målnaturtyp 2 (klartext)",
    "malnaturtyp3_text": "Målnaturtyp 3 (klartext)", "kommentar": "Kommentar (NNK)",
    "nnk_kommentar": "NNK-kommentar", "granskat": "Granskat",
    "justering": "Livsmiljötyp, behov av justering", "utbredning": "Utbredning, behov av justering",
    "livsmiljötyp1": "Livsmiljötyp 1", "livsmiljötyp2": "Livsmiljötyp 2", "livsmiljötyp3": "Livsmiljötyp 3",
    "kommentar_livsmil_utbred": "Kommentar - livsmiljötyp och utbredning",
    "tillstand": "Tillstånd",  # rättat 2026-09-03, se ovan
    "procent_gott": "Gott tillstånd (%)",
    "procent_ej_gott": "Ej gott tillstånd (%)", "procent_osaker": "Osäker (%)",
    "kommentar_tillstand": "Kommentar - Tillstånd", "kontroll1": "Vad ska kontrolleras 1",
    "kontroll2": "Vad ska kontrolleras 2", "kontroll3": "Vad ska kontrolleras 3",
    "kommentar_kontroll": "Kommentar - Vad ska kontrolleras", "metod": "Metod för kontroll",
    "Kommentar_metod": "Kommentar - Metod", "forandringsorsak": "Förändringsorsak",
    "ursprung": "Ursprung", "komplex": "Komplex", "faltinventerare": "Fältinventerare",
    "egen_bet": "Egen beteckning",
    # _text-fälten tillagda 2026-09-03 (sätts redan i lyrx:en, listade här för fullständighet)
    "livsmiljötyp1_text": "Livsmiljötyp 1, förslag (klartext)",
    "livsmiljötyp2_text": "Livsmiljötyp 2, förslag (klartext)",
    "livsmiljötyp3_text": "Livsmiljötyp 3, förslag (klartext)",
    "komplex_text": "Komplex (klartext)", "tillstand_text": "Tillstånd (klartext)",
    "justering_text": "Livsmiljötyp, justering (klartext)",
    "utbredning_text": "Utbredning, justering (klartext)",
    "kontroll1_text": "Vad ska kontrolleras 1 (klartext)",
    "kontroll2_text": "Vad ska kontrolleras 2 (klartext)",
    "kontroll3_text": "Vad ska kontrolleras 3 (klartext)",
    "metod_text": "Metod för kontroll (klartext)", "granskat_text": "Granskat (klartext)",
    "forandringsorsak_text": "Förändringsorsak (klartext)", "ursprung_text": "Ursprung (klartext)",
}

# Item-metadata per lager (steg 7) - källa/begränsning gemensam för alla fyra, se README.md
# för de fullständiga beskrivningstexterna (kondenserat här för läsbarhet).
_KALLA = ("Länsstyrelsen Södermanland (bearbetning/granskning); Naturvårdsverket, "
          "NNK Ajourhålla (källdata, uttag 2026-08-26)")
_BEGRANSNING = ("Preliminärt internt granskningsunderlag under NNK 2026 - INTE Naturvårdsverkets "
                 "officiella NNK-data. Se README.md i leveransmappen för fullständig dokumentation.")
_TAGGAR_NNK = ("NNK, Nationell naturtypskartering, Natura 2000, naturtyper, livsmiljötyper, "
               "granskning, Södermanland, Länsstyrelsen, LstD")

METADATA = {
    "NNK_naturaobjekt_yta": {
        "title": "NNK-granskningslager Södermanland – ytor",
        "summary": "NNK-ytor för Södermanlands län, attribuerade med områdesnamn, skyddskategori "
                    "och länstillhörighet, för länsstyrelsens desktopgranskning inom NNK 2026.",
        "description": "Underlag för Länsstyrelsen Södermanlands granskning av NNK 2026, kopplat "
                        "mot Natura 2000 och naturreservat/nationalpark. Innehåller mallens "
                        "NNK-attribut (med klartextfält) samt granskningsfält för avvikelse/"
                        "korrigeringsförslag, tillstånd och kontrollbehov. Länsuttaget är oklippt "
                        "vid länsgränsen. Se README.md för fullständig beskrivning.",
        "tags": _TAGGAR_NNK,
    },
    "NNK_naturaobjekt_lin": {
        "title": "NNK-granskningslager Södermanland – linjer",
        "summary": "NNK-linjer för Södermanlands län, attribuerade med områdesnamn, "
                    "skyddskategori och länstillhörighet, för länsstyrelsens desktopgranskning.",
        "description": "Samma underlag/attributschema som ytlagret (NNK_naturaobjekt_yta), men "
                        "för NNK-objekt karterade som linjer. malnaturtyp1-3 finns inte på detta "
                        "lager. Se ytlagrets metadata för fullständig beskrivning.",
        "tags": _TAGGAR_NNK,
    },
    "NNK_naturaobjekt_pkt": {
        "title": "NNK-granskningslager Södermanland – punkter",
        "summary": "NNK-punkter för Södermanlands län, attribuerade med områdesnamn, "
                    "skyddskategori och länstillhörighet, för länsstyrelsens desktopgranskning.",
        "description": "Samma underlag/attributschema som ytlagret (NNK_naturaobjekt_yta), men "
                        "för NNK-objekt karterade som punkter. malnaturtyp1-3 finns inte på detta "
                        "lager. Se ytlagrets metadata för fullständig beskrivning.",
        "tags": _TAGGAR_NNK,
    },
    "Skyddade_omraden": {
        "title": "Skyddade områden Södermanland (referenslager, NNK-granskning)",
        "summary": "Referenslager: Natura 2000-siter (SCI/SPA) och naturreservat/nationalpark i "
                    "och kring Södermanlands län, till stöd för NNK-granskningen.",
        "description": "Kontur per skyddskategori som NNK-lagrens skyddskategori/områdesnamn/"
                        "sitecode-fält är matchade mot. Hämtat från NV:s N2000-källa och "
                        "Naturvårdsregistret-WFS, utvidgat till angränsande län. Genomskinlig "
                        "fyllning så NNK-lagrens granskningsfärger syns igenom.",
        "tags": "Natura 2000, naturreservat, nationalpark, skyddade områden, Södermanland, "
                "Länsstyrelsen, LstD, NNK",
    },
}


def nytt_domannamn(gammalt):
    n = gammalt
    for p in ("NV_", "LST_"):
        if n.startswith(p):
            n = n[len(p):]
    n = (n.replace("å", "a").replace("ä", "a").replace("ö", "o")
          .replace("Å", "A").replace("Ä", "A").replace("Ö", "O"))
    return PREFIX + n


def falt(tabell):
    return {f.name: f for f in arcpy.ListFields(tabell)}


def double_till_long(tabell, faltnamn):
    tmp = faltnamn + "_tmp"
    arcpy.management.AddField(tabell, tmp, "LONG")
    arcpy.management.CalculateField(
        tabell, tmp, "None if !{0}! is None else int(round(!{0}!))".format(faltnamn), "PYTHON3")
    arcpy.management.DeleteField(tabell, faltnamn)
    arcpy.management.AlterField(tabell, tmp, faltnamn, faltnamn)
    print("    {}: Double -> Long".format(faltnamn))


print("1. Fälttyper...")
for lager in NNK_LAGER:
    tab = VAR_GDB + "\\" + lager
    f = falt(tab)
    for namn in FALT_DOMAN:
        if namn in f and f[namn].type == "Double":
            double_till_long(tab, namn)

print("2. Domäner...")
befintliga = {d.name for d in arcpy.da.ListDomains(VAR_GDB)}
karta = {}
for d in arcpy.da.ListDomains(MALL_GDB):
    nytt = nytt_domannamn(d.name)
    karta[d.name] = nytt
    if d.name in EXKLUDERA_MALLDOMANER:
        continue  # se EXKLUDERA_MALLDOMANER ovan - tillstand får en egen, korrigerad domän i steg 2b
    if nytt in befintliga:
        print("    {} finns redan".format(nytt)); continue
    if d.domainType != "CodedValue":
        continue
    arcpy.management.CreateDomain(VAR_GDB, nytt, d.description or nytt, d.type.upper(), "CODED")
    for kod, text in d.codedValues.items():
        arcpy.management.AddCodedValueToDomain(VAR_GDB, nytt, kod, text)
    print("    {} -> {} ({} koder)".format(d.name, nytt, len(d.codedValues)))

print("2b. Rättad tillstand-domän (blankettens fyra värden)...")
nytt_tillstand = nytt_domannamn("LST_NNK_tillstand")
if nytt_tillstand not in befintliga:
    arcpy.management.CreateDomain(VAR_GDB, nytt_tillstand,
        "Tillstånd (blankett_forvaltarkunskap_nnk.xlsx)", "LONG", "CODED")
    for kod, text in TILLSTAND_KORRIGERAD_DOMAN.items():
        arcpy.management.AddCodedValueToDomain(VAR_GDB, nytt_tillstand, kod, text)
    print("    {} skapad ({} koder)".format(nytt_tillstand, len(TILLSTAND_KORRIGERAD_DOMAN)))

print("3. Kopplar domäner...")
for lager, naturtypsdoman in NNK_LAGER.items():
    tab = VAR_GDB + "\\" + lager
    f = falt(tab)
    for namn, doman in FALT_DOMAN.items():
        if namn not in f:
            continue
        if doman == "NATURTYP":
            doman = naturtypsdoman
        if f[namn].domain != karta[doman]:
            arcpy.management.AssignDomainToField(tab, namn, karta[doman])
    print("    {} klart".format(lager))

print("4. Alias...")
for lager in NNK_LAGER:
    tab = VAR_GDB + "\\" + lager
    f = falt(tab)
    for namn, alias in ALIAS.items():
        if namn in f and f[namn].aliasName != alias:
            arcpy.management.AlterField(tab, namn, new_field_alias=alias)

if GOR_GLOBALID:
    print("5. GlobalID...")
    for lager in list(NNK_LAGER) + ["Skyddade_omraden"]:
        tab = VAR_GDB + "\\" + lager
        f = falt(tab)
        if "globalid" in f and f["globalid"].type != "GlobalID":
            arcpy.management.AlterField(tab, "globalid", "nv_globalid", "NV GlobalID (ursprunglig)")
        if not any(x.type == "GlobalID" for x in arcpy.ListFields(tab)):
            arcpy.management.AddGlobalIDs(tab)
            print("    {}: GlobalID tillagt".format(lager))

if GOR_EDITOR_TRACKING:
    print("6. Editor tracking...")
    for lager in NNK_LAGER:
        tab = VAR_GDB + "\\" + lager
        if "lst_andrad" in falt(tab):
            continue
        arcpy.management.EnableEditorTracking(
            tab, "lst_skapad_av", "lst_skapad", "lst_andrad_av", "lst_andrad", "ADD_FIELDS", "UTC")
        arcpy.management.AlterField(tab, "lst_andrad_av", new_field_alias="Granskad av (senast ändrad av)")
        arcpy.management.AlterField(tab, "lst_andrad", new_field_alias="Granskad datum (senast ändrad)")
        print("    {}: aktiverat".format(lager))

if GOR_METADATA:
    print("7. Metadata...")
    for lager, poster in METADATA.items():
        tab = VAR_GDB + "\\" + lager
        item_md = md.Metadata(tab)
        if item_md.isReadOnly:
            print("    {}: skrivskyddad - hoppade över".format(lager)); continue
        item_md.title = poster["title"]
        item_md.summary = poster["summary"]
        item_md.description = poster["description"]
        item_md.tags = poster["tags"]
        item_md.credits = _KALLA
        item_md.accessConstraints = _BEGRANSNING
        item_md.save()
        print("    {}: metadata satt".format(lager))

print("KLART. Ladda om lagren i ArcGIS Pro innan Share As Web Layer.")
```

## Bilaga B · Domänerna som kopieras (ur KartLits-mallen)

| Domän (nytt namn) | Fält | Koder |
|---|---|---|
| `LstD_NNK_granskad` | granskat | 1 Ja · 2 Nej · 3 Påbörjat |
| `LstD_NNK_justering` | justering | 1 Inget behov av justering · 2 Ändring till annan livsmiljötyp · 3 Ändring till utvecklingsmark · 4 Osäker – kan ej bedöma om livsmiljö eller inte · 5 Obestämd – kan ej bedöma vilken livsmiljö |
| `LstD_NNK_utbredning` | utbredning | 1 Inget behov av justering · 2 Yttergränser, kvalitetsförbättring · 3 Yttergränser, ändrad utbredning · 4 Behov av att dela upp ytan, flera LMT |
| `LstD_NNK_kontroll` | kontroll1–3 | 1 Typiska och karakteristiska arter · 2 Strukturer · 3 Hävd · 4 Funktioner (hydrologi, störningar) · 5 Morfologi (jordart, formationer) · 6 Annan negativ påverkan |
| `LstD_NNK_metod` | metod | 1 Fältbesök · 2 Fältinventering (standardiserad metodik) · 3 Skrivbord / granska mot andra underlag · 4 Annan metod |
| `LstD_NNK_yta` / `_linje` / `_punkt` | naturtyp, livsmiljötyp1–3, malnaturtyp1–3 | NV:s naturtypskoder (230 / 24 / 15 koder) |
| `LstD_NNK_Naturtypsstatus`, `_Karteringsstatus`, `_Komplex`, `_Forandringsorsak`, `_Ursprung` | resp. NV-fält | NV:s kodlistor (visas som klartext i popup) |

**`LstD_NNK_tillstand` — rättad 2026-09-03, byggs INTE längre genom att kopiera mallen.**
KartLits-mallens egen domän för fältet `tillstand` innehöll "1 Inget behov av justering · 2 Okänt
(kan ej bedöma) · 3 Annat tillstånd" — en kopplingsbugg i själva NV-mallen (innehållet hörde
snarare hemma vid `justering`/`utbredning`; matchade varken blanketten eller NV:s egen FAQ-text
"gott, inte gott eller okänt tillstånd", FAQ fråga 30). `forbered_gdb_for_publicering.py` bygger
i stället domänen direkt (steg 2b) med blankettens egna fyra värden:

| Domän (nytt namn) | Fält | Koder |
|---|---|---|
| `LstD_NNK_tillstand` | tillstand | 1 Gott · 2 Icke gott · 3 Okänt – kan ej bedöma · 4 Blandat – se andelar |

Samma fyra värden ligger även i det redan färdiga, read-only klartextfältet `tillstand_text` i
gdb:n (`scripts/analysis/naturtyp_koder.py`, `TILLSTAND_TEXT`) — domänen ovan används bara för
själva redigeringsrullistan vid publicering.

## Bilaga C · Checklista (speglar LstD GIS LOGG)

- [ ] Kopia av gdb tagen · skript kört utan fel · 13 domäner · alias · GlobalID · editor tracking
- [ ] Alla granskningsfält synliga i lagret · symbol på `granskat` · popup · display field · visningsintervall
- [ ] `LstD_NNK_Granskning` publicerad: Feature, kopiera all data, editing på, sync av, export av, bilagor av, tidszon
- [ ] `LstD_Skyddade_Omraden` publicerad: editing av
- [ ] Items: titel `– Driftat`, tagg, beskrivning, Update attributes only, track edits, delat med granskargrupp (ej organisation)
- [ ] WebMap: lager + referenslager, popup, formulär (grupp 1–4), utgångsläge, sparad `– WebMap`, delad
- [ ] Konfigurator: app `– WebbGIS`, sökväg, lagerlista (5 grupper), sök- och redigeringsinställningar per lager, filter (N2000 aktivt), widgetar, välkomstruta, lagerlista exporterad (JSON)
- [ ] Test: rullistor i formuläret · Uppdatera fungerar · Granskad av/datum fylls · Ta bort går inte · kollega kan redigera
- [ ] GDK-metadatapost · LstD-logg ifylld · länk utskickad · A2.7/A2.8 avbockade i kontrollrummet
