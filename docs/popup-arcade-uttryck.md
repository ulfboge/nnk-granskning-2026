# Popup-uttryck (Arcade) — LstD NNK Granskning

## Länsstyrelsen i Södermanlands län · Naturskyddsenheten · NNK 2026

**Version:** 1.8 · 2026-10-08 (sektion 2b: Skogsstyrelsens register, VISS och R7-förslaget). 1.7 · 2026-10-08 (sektion 2b: tydligare text för statusens ålder när inventeringsdatum saknas). 1.6 · 2026-10-06 (ny sektion 2b Bedömning vid skrivbordet: R7-grupp, statusens ålder och underlag nyare än statusen). 1.5 · 2026-10-01 (sektion 8 utökad med SkötselDOS och uppföljning). 1.4 · 2026-09-30 (ny sektion 9 Skog (laserdata) med diken). 1.3 · 2026-09-30 (sektion 8 utökad med TUVA). 1.2 · 2026-09-29 (sektion 7 Typiska arter och sektion 8 Hävd enligt jordbruksskiften tillagda)
**Hör ihop med:** `docs/webbgis-publicering.html` (Del 2 steg 6, Del 5 steg 5)
**Status:** Detta är den faktiska, levande popup-konfigurationen i Map Viewer/Konfiguratorn — inte det som `bygg_nnk_lyrx.py` genererar.

---

## Bakgrund

Popupen för NNK-ytlagret beskrevs ursprungligen (Del 2 steg 6, Del 5 steg 5) som att den byggs en gång av `bygg_nnk_lyrx.py` (sex `CIMTableMediaInfo`-sektioner i `mediaInfos`) och sedan ärvs oförändrad hela vägen till WebMap och Konfigurator. Det stämmer inte längre.

Samtliga sex popup-sektioner har (per 2026-09-22) ersatts med handskrivna **Arcade-popuputtryck** direkt i Map Viewers popup-konfiguration för NNK-ytlagret, ett `type: "fields"`-uttryck per grupp. Anledningen är att en vanlig fältlista i Map Viewer inte kan dölja rader som saknar värde per objekt — det kan ett Arcade-uttryck. Varje uttryck bygger sin egen `fieldInfos`/`attributes`-lista dynamiskt och visar "Ingen information registrerad i denna del." om alla fält i gruppen är tomma.

**Det här är den enda versionshanterade kopian av koden.** Den lever annars bara inne i portalens popup-konfiguration (per-lager, i WebMap:en), inte i något lyrx eller skript. Om popupen någon gång nollställs (t.ex. genom att ta bort och lägga till lagret på nytt i WebMap:en — se varningen i Del 5 steg 5) är det här filen att kopiera tillbaka ifrån, uttryck för uttryck.

**Kända avvikelser mot den ursprungliga `bygg_nnk_lyrx.py`-designen**, upptäckta när koden nedan dokumenterades:

- ~~**Granskning 4** saknade `nnk_kommentar`, `faltinventerare`, `egen_bet`~~ — åtgärdat 2026-09-22, alla fem fälten är nu med (se avsnitt 6 nedan).
- **Area (ha)** ligger i gruppen *Naturtyp (NNK-data)*, inte i *Identifiering och skydd* där `bygg_nnk_lyrx.py`s `NEW_FIELDS`-ordning ursprungligen placerade den.
- **Fältnamnet för metod-kommentaren** skrivs `kommentar_metod` (gemener) i Arcade-uttrycket för Granskning 3, medan övrig dokumentation (`webbgis-publicering.md`, `metodik.md`) genomgående skriver `Kommentar_metod` (stort K). Arcades fältuppslagning är skiftlägesokänslig så det är sannolikt ofarligt, men värt att göra konsekvent i dokumentationen.
- **Grupp 1–3** slår upp klartext direkt med `DomainName($feature, "fältnamn")` på kodfälten (`livsmiljötyp1–3`, `justering`, `utbredning`, `tillstand`, `kontroll1–3`, `metod`), inte via de förberäknade `_text`-fälten som `bygg_nnk_lyrx.py` annars bygger. Fungerar likvärdigt, men det betyder att de förberäknade `_text`-fälten för just dessa fält inte används av popupen (de kan fortfarande vara användbara i attributtabellen/exporter).
- **Startdatum/Slutdatum senaste inventering** (`habitat_period_lastdata_start`/`_end`) tillagda i *Naturtyp (NNK-data)* 2026-09-22, på Johans önskemål — årtalet för naturtypsbedömningen saknades helt i popupen innan dess. **Kräver en publiceringsförberedelse som inte är gjord än:** fältsynlighet för `habitat_period_*` måste slås PA i `NNK_naturaobjekt_yta`/`lin`/`pkt` (Del 2 steg 3 nedan säger idag att de ska hållas AVSTÄNGDA) och läget republiceras (Share As Web Layer → Overwrite) innan fälten dyker upp i tjänsten — annars visar Arcade-uttrycket ingenting för dessa två rader, även om koden är på plats. Se även punkt 6 i kvarvarande_punkter_20260922.md.
- **Bevarandeplan, fastställd (år)** (`bevarandeplan_ar`) tillagt i *Naturtyp (NNK-data)* 2026-09-22, på Johans önskemål — visar vilket år den senaste bevarandeplanen för N2000-siten fastställdes (tomt för siter utan bevarandeplan). Fältet är nytt och sätts av `jobbdator_koppla_nnk_skyddskategori.py` (kräver att `data/analysis/bevarandeplan_platser.csv` kopieras till Johans arbetsdator, se README/kvarvarande_punkter_20260922.md) — **hela pipelinen måste köras om** (koppla_nnk_skyddskategori → forbered_gdb_for_publicering → bygg_nnk_lyrx → republicera) innan fältet finns i tjänsten.

- **Typiska arter (Artportalen)** — ny sektion 7, tillagd 2026-09-29. Visar fälten `typarter_antal`, `typarter` och `typarter_senaste_ar`, som sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `typiska_arter_per_yta.csv` (framräknad av `natura-2000: scripts/analysis/artportalen_typiska_arter.py`). Uttrycket kontrollerar med `HasKey` att fälten finns, men klistra ändå in det först efter Overwrite (se OBS nedan).
- **Hävd enligt jordbruksskiften** — ny sektion 8, tillagd 2026-09-29. Visar fälten `havd_skiften`, `havd_obrutet_sedan`, `havd_ar_utan_bete`, `havd_andel_bete_senaste`, `havd_varning_vall` och `havd_period`, som sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `havd_for_granskning.csv` (framräknad av `natura-2000: scripts/analysis/nnk_havd.py`). Sektionen visas bara för hävdberoende typer och för ytor där skiftesdata visar hävd — på övriga ytor säger värdet lite. Samma `HasKey`-skydd som sektion 7.
- **SkötselDOS och uppföljning i sektion 8** — tillagt 2026-10-01. Fälten `skdos_havd_senaste_ar`, `skdos_havd_antal_ar`, `skdos_havd_typ`, `uppf_punkter_bedomda`, `uppf_andel_bra`, `uppf_antal_dalig` och `uppf_senaste_ar` sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `skotseldos_for_granskning.csv` (framräknad av `natura-2000: scripts/analysis/nnk_skotseldos.py` ur Metrias SkötselDOS-uttag). Sektionen visas nu också för ytor med SkötselDOS-hävd eller uppföljningspunkter. Klistra in efter Overwrite (se OBS nedan).
- **TUVA i sektion 8** — tillagt 2026-09-30. Fälten `tuva_objekt_id`, `tuva_andel_overlapp`, `tuva_antal_objekt`, `tuva_inv_ar`, `tuva_havdstatus`, `tuva_havdregim`, `tuva_igenvaxning`, `tuva_naturtyp` och `tuva_paverkan` sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `tuva_for_granskning.csv` (framräknad av `natura-2000: scripts/analysis/nnk_tuva.py`). Sektionen visas nu också för alla ytor med TUVA-träff, oavsett naturtyp och skiftesvärde. Inventeringsåret visas med ålder, och TUVA äldre än 15 år markeras. Klistra in efter Overwrite (se OBS nedan).
- **Skog (laserdata)** — ny sektion 9, tillagd 2026-09-30. Visar fälten `laser_hojd_medel`, `laser_volym_medel`, `laser_grundyta_medel`, `laser_diameter_medel`, `laser_skanning_ar`, `laser_hojdforandring_medel`, `laser_andel_sankt`, `laser_forandring_period`, `laser_flagga`, `diken_m_inom` och `diken_m_50m`, som sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `laser_for_granskning.csv` (framräknad av `natura-2000: scripts/analysis/nnk_laser.py`). Visas för skogstyperna i gruppen Skog (inklusive 9740 och 9750) och, med bara dikesraderna och titeln *Diken (laserdata)*, för myrarna i gruppen Våtmark (7110–7231). Skanningsår och förändringsperiod står i klartext. Klistra in efter Overwrite (se OBS nedan).

- **Floraväkteri (Artportalen)** — ny sektion 10, tillagd 2026-10-01. Visar fälten `fv_antal_arter`, `fv_antal_rapporter`, `fv_senaste_ar`, `fv_hotade_arter`, `fv_bilaga2_arter`, `fv_ej_aterfunna`, `fv_minskande`, `fv_anm_havd` och `fv_arter`, som sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `floravakteri_for_granskning.csv` (framräknad av `natura-2000: scripts/analysis/nnk_floravakteri.py` ur SLU:s publika SOS-WFS, Artportalen-projekten Floraväkteri Sverige och Arkiv Floraväktarlokaler). Skyddsklassade fynd ingår inte. Visas bara för ytor med minst en floraväktarrapport. Klistra in efter Overwrite (se OBS nedan).

> **OBS (2026-10-01): klistra in uttrycken först efter Share As Web Layer → Overwrite.** `HasKey` skyddar bara när uttrycket körs. Map Viewers Arcade-redigerare kontrollerar dessutom att alla `$feature.fält` finns i lagret, och saknas fälten i tjänsten går det att trycka *Kör* men inte *Klar*. Samma sak om fälten finns men är dolda (Visible av i Pro före publiceringen).
---

## 1. Identifiering och skydd

```js
// Identifiering och skydd
// Grundläggande identifiering visas alltid.
// Skydds-ID visas endast när värde finns.

var infos = [];
var attrs = {};

// --- Alltid synliga ---

Push(infos, {
    fieldName: "omrade_varde",
    label: "Område"
});
attrs["omrade_varde"] = $feature.omrade_namn;

Push(infos, {
    fieldName: "skyddskategori_varde",
    label: "Skyddskategori"
});
attrs["skyddskategori_varde"] = $feature.skyddskategori;

Push(infos, {
    fieldName: "lan_varde",
    label: "Län (skyddat område)"
});
attrs["lan_varde"] = $feature.lan;

// --- Visas endast när värde finns ---

if (!IsEmpty($feature.n2000_sitecode)) {
    Push(infos, {
        fieldName: "n2000_sitecode_varde",
        label: "Natura 2000-kod (SE-nummer)"
    });
    attrs["n2000_sitecode_varde"] = $feature.n2000_sitecode;
}

if (!IsEmpty($feature.n2000_typ)) {
    Push(infos, {
        fieldName: "n2000_typ_varde",
        label: "Natura 2000-typ (SCI/SPA)"
    });
    attrs["n2000_typ_varde"] = $feature.n2000_typ;
}

if (!IsEmpty($feature.naturreservat_nvrid)) {
    Push(infos, {
        fieldName: "nvrid_varde",
        label: "Naturreservat-ID (NVRID)"
    });
    attrs["nvrid_varde"] = $feature.naturreservat_nvrid;
}

return {
    type: "fields",
    title: "Identifiering och skydd",
    fieldInfos: infos,
    attributes: attrs
};
```

## 2. Naturtyp (NNK-data)

```js
// Naturtyp (NNK-data)
// Visar endast fält som innehåller ett värde.

var infos = [];
var attrs = {};

// Naturtyp – kod + klartext
if (!IsEmpty($feature.naturtyp_kod_text)) {
    Push(infos, {
        fieldName: "naturtyp_varde",
        label: "Naturtyp"
    });
    attrs["naturtyp_varde"] = $feature.naturtyp_kod_text;
}

// Naturtypsstatus
if (!IsEmpty($feature.naturtypsstatus_text)) {
    Push(infos, {
        fieldName: "naturtypsstatus_varde",
        label: "Naturtypsstatus"
    });
    attrs["naturtypsstatus_varde"] = $feature.naturtypsstatus_text;
}

// Area
if (!IsEmpty($feature.area_ha)) {
    Push(infos, {
        fieldName: "area_varde",
        label: "Area (ha)"
    });
    attrs["area_varde"] = Round($feature.area_ha, 2);
}

// Karteringsstatus
if (!IsEmpty($feature.karteringsstatus_text)) {
    Push(infos, {
        fieldName: "karteringsstatus_varde",
        label: "Karteringsstatus"
    });
    attrs["karteringsstatus_varde"] = $feature.karteringsstatus_text;
}

// Startdatum senaste inventering av naturtypen
// OBS (2026-09-22): kräver att fältsynlighet för habitat_period_* slås PA i
// NNK_naturaobjekt_yta/lin/pkt (Data > Fields i Pro) och läget republiceras
// (Share As Web Layer > Overwrite) - just nu står webbgis-publicering.md steg 3
// att dessa ska hållas AVSTÄNGDA, så fälten finns inte i den publicerade
// tjänsten än. Formatering antar Date-fält (TypeOf-koll gör den ofarlig även
// om fältet visar sig vara Text/Short istället).
if (!IsEmpty($feature.habitat_period_lastdata_start)) {
    Push(infos, {
        fieldName: "habitat_period_lastdata_start_varde",
        label: "Startdatum senaste inventering"
    });
    attrs["habitat_period_lastdata_start_varde"] = IIf(
        TypeOf($feature.habitat_period_lastdata_start) == "Date",
        Text($feature.habitat_period_lastdata_start, "YYYY"),
        Text($feature.habitat_period_lastdata_start)
    );
}

// Slutdatum senaste inventering av naturtypen
if (!IsEmpty($feature.habitat_period_lastdata_end)) {
    Push(infos, {
        fieldName: "habitat_period_lastdata_end_varde",
        label: "Slutdatum senaste inventering"
    });
    attrs["habitat_period_lastdata_end_varde"] = IIf(
        TypeOf($feature.habitat_period_lastdata_end) == "Date",
        Text($feature.habitat_period_lastdata_end, "YYYY"),
        Text($feature.habitat_period_lastdata_end)
    );
}

// Bevarandeplanens fastställelseår - vilket år den senaste bevarandeplanen
// för N2000-siten fastställdes (bara sitecoder med en bevarandeplan har ett
// värde här). Tillagt 2026-09-22 på Johans önskemål ("så att det är klart
// från vilket år det senast fanns bedömning"). Rent heltalsfält (Long), inte
// Date - Text() räcker, ingen TypeOf/Date-formatering behövs.
if (!IsEmpty($feature.bevarandeplan_ar)) {
    Push(infos, {
        fieldName: "bevarandeplan_ar_varde",
        label: "Bevarandeplan, fastställd (år)"
    });
    attrs["bevarandeplan_ar_varde"] = Text($feature.bevarandeplan_ar);
}

// Målnaturtyp 1
if (!IsEmpty($feature.malnaturtyp1_text)) {
    Push(infos, {
        fieldName: "malnaturtyp1_varde",
        label: "Målnaturtyp 1"
    });
    attrs["malnaturtyp1_varde"] = $feature.malnaturtyp1_text;
}

// Målnaturtyp 2
if (!IsEmpty($feature.malnaturtyp2_text)) {
    Push(infos, {
        fieldName: "malnaturtyp2_varde",
        label: "Målnaturtyp 2"
    });
    attrs["malnaturtyp2_varde"] = $feature.malnaturtyp2_text;
}

// Målnaturtyp 3
if (!IsEmpty($feature.malnaturtyp3_text)) {
    Push(infos, {
        fieldName: "malnaturtyp3_varde",
        label: "Målnaturtyp 3"
    });
    attrs["malnaturtyp3_varde"] = $feature.malnaturtyp3_text;
}

// Komplex
if (!IsEmpty($feature.komplex_text)) {
    Push(infos, {
        fieldName: "komplex_varde",
        label: "Komplex"
    });
    attrs["komplex_varde"] = $feature.komplex_text;
}

// Ursprung
if (!IsEmpty($feature.ursprung_text)) {
    Push(infos, {
        fieldName: "ursprung_varde",
        label: "Ursprung"
    });
    attrs["ursprung_varde"] = $feature.ursprung_text;
}

// Förändringsorsak
if (!IsEmpty($feature.forandringsorsak_text)) {
    Push(infos, {
        fieldName: "forandringsorsak_varde",
        label: "Förändringsorsak"
    });
    attrs["forandringsorsak_varde"] = $feature.forandringsorsak_text;
}

// Om hela sektionen saknar information
if (Count(infos) == 0) {
    return {
        type: "fields",
        title: "Naturtyp (NNK-data)",
        fieldInfos: [{
            fieldName: "tom_info",
            label: "Information"
        }],
        attributes: {
            tom_info: "Ingen information registrerad i denna del."
        }
    };
}

return {
    type: "fields",
    title: "Naturtyp (NNK-data)",
    fieldInfos: infos,
    attributes: attrs
};
```

## 2b. Bedömning vid skrivbordet (R7)

Ny sektion 2026-10-06. Lägg den direkt efter *Naturtyp (NNK-data)*. Den samlar det du behöver för att avgöra om status kan sättas eller omprövas vid skrivbordet, så att du inte behöver gå till attributtabellen:

- **Bedömningsgrupp (R7)** — vilken delregel i metodiken som gäller (Hävd, Skog, Våtmark, Stabila). Räknas fram ur naturtypskoden.
- **Statusens ålder** — slutdatum senaste inventering om det finns, annars året då NNK-objektet senast redigerades och om statusen kommer från basinventeringen (BIDOS). Redigeringsåret är bara en övre gräns: ändringen kan ha gällt vilket attribut som helst, så statusen kan vara äldre.
- **Vad gäller** — *bedöm* (Ej bedömd status), *ompröva* (status finns redan, se R7-omprövning i metodiken) eller *ingår inte*.
- **Underlag** — skiften, TUVA, SkötselDOS, uppföljning, laser och typiska arter med år, och om de är nyare eller äldre än statusen. Bara underlag nyare än statusen kan bekräfta eller ändra den.

**Tillägg 2026-10-08:** sektionen visar också Skogsstyrelsens register (utförd avverkning, avverkningsanmälan, biotopskydd/naturvårdsavtal), VISS-status när den är kopplad, och sist R7-förslaget i tre rader: **Förslag (R7)** (utfall, säkerhet och villkor), **Motiv** (underlagen med år och eventuella motsägelser) och **Kontrollera** (manuella kontroller med lager inom hakparentes). Fälten kommer från `skogsregister_for_granskning.csv`, `viss_for_granskning.csv` och `r7_forslag_for_granskning.csv` och måste vara synliga i Pro före Overwrite (de står i `EXTRA_VISIBLE_FIELDS` i lyrx-skriptet). Klistra in hela uttrycket nedan igen i Map Viewer; det ersätter det gamla. Förslaget är skrivskyddat — formulärfälten fylls i av granskaren.

Uttrycket läser fälten dynamiskt med `Expects($feature, "*")`, så det går att klistra in och spara även om något fält saknas i tjänsten — raden visas då bara inte. **Statusens ålder läses ur heltalsfältet `nnk_andrad_ar`**, som `forbered_gdb_for_publicering.py` (steg 1d) räknar fram ur NV:s `last_edited_date`. NV:s fält går inte att publicera: det är *Date, Time and Timezone Offset* och ger fel 00403 (konstaterat 2026-10-06). Låt `last_edited_date` vara avstängt och se till att `nnk_andrad_ar` är synligt före Overwrite. Tills fältet finns visar raden bara BIDOS-ursprunget.

```js
// Bedömning vid skrivbordet (R7) — tillagd 2026-10-06
// Grupp, statusens ålder och vilka underlag som är nyare än statusen.
// Fälten läses dynamiskt: saknas ett fält i tjänsten hoppas raden över.
Expects($feature, "*");

function F(n) {
    if (HasKey($feature, n)) { return $feature[n]; }
    return null;
}
function Ar(v) {
    if (IsEmpty(v)) { return null; }
    if (TypeOf(v) == "Date") { return Year(v); }
    var n = Number(Left(Text(v), 4));
    if (IsNan(n)) { return null; }
    return n;
}

var kod = Text(F("naturtyp"));
var hav = ["1630","4030","5130","5133","6110","6210","6230","6270","6280","6410","6430","6510","8231","9070","9071","9072"];
var sko = ["2181","9006","9008","9009","9010","9020","9030","9050","9060","9080","9110","9160","9162","9180","9190","9740","9750"];
var vat = ["3110","3130","3150","3160","3260","7110","7111","7140","7141","7142","7230","7231"];
var sta = ["1220","1230","1232","1620","1621","1640","8210","8220","8230","8232"];
var dodved = ["9006","9008","9009","9010","9050","9830"];

var grupp = When(
    Includes(hav, kod), "Hävd (R7A)",
    Includes(sko, kod), "Skog (R7B)",
    Includes(vat, kod), "Våtmark (R7C)",
    Includes(sta, kod), "Stabila (R7D)",
    null);

// Statusens ålder
var status = DefaultValue(F("naturtypsstatus_text"), "");
var urs = DefaultValue(F("ursprung_text"), "");
var bidos = Find("BIDOS", urs) > -1;
var slut = Ar(F("habitat_period_lastdata_end"));
var red = Ar(F("nnk_andrad_ar"));   // år ur NV:s last_edited_date, se forbered_gdb steg 1d
if (IsEmpty(red)) { red = Ar(F("last_edited_date")); }
var statusAr = IIf(IsEmpty(slut), red, slut);

var alder = "Okänt år";
if (!IsEmpty(slut)) {
    alder = "Bedömd " + slut + " (slutdatum senaste inventering)";
} else if (!IsEmpty(red)) {
    alder = "Okänt år. NNK-objektet senast redigerat " + red + " (inte nödvändigtvis statusen)" + IIf(bidos, ", ursprung BIDOS (basinventeringen)", "");
} else if (bidos) {
    alder = "Okänt år. Ursprung BIDOS (basinventeringen), ofta 15–20 år gammal";
}

// Vad gäller
var ejBedomd = Find("Ej bedömd", status) > -1;
var harStatus = Find("ullgod", status) > -1;   // Fullgod / Icke fullgod
var vad = "";
if (IsEmpty(grupp)) {
    vad = "Ingår inte i R7 (marin, obestämd eller icke-Natura-naturtyp).";
} else if (ejBedomd) {
    vad = "Ej bedömd status: bedöm enligt " + grupp + ".";
} else if (harStatus) {
    vad = "Har status: ompröva (R7-omprövning). Statusen räknas inte som belägg — bara underlag nyare än "
        + IIf(IsEmpty(statusAr), "statusen", Text(statusAr)) + " kan bekräfta eller ändra den.";
} else {
    vad = "R7 gäller inte för den här statusen.";
}
if (Includes(dodved, kod)) {
    vad += " 9010/9050 kan inte bli fullgod vid skrivbordet (död ved).";
}

function Jmf(y) {
    if (IsEmpty(y) || IsEmpty(statusAr)) { return ""; }
    if (y > statusAr) { return " · nyare än statusen"; }
    return " · inte nyare än statusen";
}

var infos = [];
var attrs = {};
function Rad(id, etikett, varde) {
    if (IsEmpty(varde) || varde == "") { return; }
    Push(infos, { fieldName: id, label: etikett });
    attrs[id] = varde;
}

Rad("r7_grupp", "Bedömningsgrupp (R7)", grupp);
Rad("r7_alder", "Statusens ålder", alder);
Rad("r7_vad", "Vad gäller", vad);

// Underlag med år
var nu = Year(Now());
var sk = F("havd_skiften");
if (!IsEmpty(sk)) {
    var saknas = F("havd_ar_utan_bete");
    Rad("r7_skiften", "Hävd enligt skiften (2015–2025)",
        sk + IIf(IsEmpty(saknas), "", " — år utan bete/slåtter: " + saknas) + Jmf(2025));
}
var tAr = Ar(F("tuva_inv_ar"));
if (!IsEmpty(tAr)) {
    var tAlder = nu - tAr;
    var tNot = When(tAlder > 15, " · äldre än 15 år, räknas inte som aktuellt",
                    tAlder > 10, " · 11–15 år, räcker inte för fullgod", "");
    Rad("r7_tuva", "TUVA", tAr + " · " + DefaultValue(F("tuva_havdstatus"), "hävd ej angiven") + tNot + Jmf(tAr));
}
var sAr = Ar(F("skdos_havd_senaste_ar"));
var sTyp = F("skdos_havd_typ");
if (!IsEmpty(sTyp)) {
    Rad("r7_skdos", "SkötselDOS", sTyp + IIf(IsEmpty(sAr), " (år saknas)", " senast " + sAr) + Jmf(sAr));
}
var uAr = Ar(F("uppf_senaste_ar"));
if (!IsEmpty(uAr)) {
    Rad("r7_uppf", "Uppföljning", uAr + " · " + DefaultValue(F("uppf_antal_dalig"), 0) + " punkter Dålig" + Jmf(uAr));
}
var lAr = Ar(F("laser_skanning_ar"));
if (!IsEmpty(lAr)) {
    Rad("r7_laser", "Laserdata", lAr + IIf(IsEmpty(F("laser_flagga")), " · ingen flagga", " · " + F("laser_flagga")) + Jmf(lAr));
}
var dik = F("diken_m_inom");
if (!IsEmpty(dik) && dik > 0 && grupp != "Hävd (R7A)") {
    Rad("r7_diken", "Diken inom ytan", Round(dik) + " m");
}
// Skogsstyrelsens register (2026-10-08)
var avAr = Ar(F("skr_utford_ar"));
if (!IsEmpty(avAr)) {
    Rad("r7_sksavv", "SKS utförd avverkning", avAr + " · " + DefaultValue(F("skr_utford_typ"), "") + Jmf(avAr));
}
var anAr = Ar(F("skr_anmald_ar"));
if (!IsEmpty(anAr)) {
    Rad("r7_sksanm", "SKS avverkningsanmälan", anAr + " · " + DefaultValue(F("skr_anmald_typ"), "") + " (inte nödvändigtvis utförd)");
}
Rad("r7_skydd", "Biotopskydd/naturvårdsavtal", F("skr_skydd"));
// VISS (D2.5, tomt tills kopplingen körts)
var vs = F("viss_ekostatus");
if (!IsEmpty(vs)) {
    Rad("r7_viss", "VISS ekologisk status", vs + IIf(IsEmpty(F("viss_styrande")), "", " — styrs av " + F("viss_styrande"))
        + IIf(IsEmpty(F("viss_hydromorf")), "", " · hydromorfologi " + F("viss_hydromorf")));
}
var aAr = Ar(F("typarter_senaste_ar"));
if (!IsEmpty(aAr)) {
    Rad("r7_arter", "Typiska arter", F("typarter_antal") + " arter, senast " + aAr + Jmf(aAr));
}

// R7-förslaget (2026-10-08): utfall, motiv och kontroller ur bygg_r7_forslag.py
Rad("r7_f_utfall", "Förslag (R7)", F("r7f_utfall"));
Rad("r7_f_motiv", "Motiv", F("r7f_motiv"));
Rad("r7_f_kontroll", "Kontrollera", F("r7f_kontrollera"));

if (Count(infos) == 0) {
    return { type: "fields", title: "Bedömning vid skrivbordet (R7)",
             fieldInfos: [{ fieldName: "tom", label: "Information" }],
             attributes: { tom: "Ingen information." } };
}
return { type: "fields", title: "Bedömning vid skrivbordet (R7)", fieldInfos: infos, attributes: attrs };
```

## 3. Granskning 1 — Avvikelse och korrigeringsförslag

**Utökad 2026-09-22:** nytt block för `forandringsorsak_forslag` ("Förändringsorsak, förslag") — granskarens EGNA förslagskod, inte det skrivskyddade källfältet `forandringsorsak` som redan syns i gruppen *Naturtyp (NNK-data)*. Kräver att fältet finns i tjänsten (gdb-kedjan → republicering, se `webbgis-publicering.html` Del 5 steg 6) innan den här versionen kan klistras in. Placerat sist i "vad"-delen, direkt före kommentaren — gruppen läses nu "vad" (föreslagen typ/justering) följt av "varför" (förändringsorsak + fritextkommentar).

```js
// Granskning 1 – Avvikelse och korrigeringsförslag
// Visar endast fält som innehåller ett värde.

var infos = [];
var attrs = {};

if (!IsEmpty($feature.livsmiljötyp1)) {
    Push(infos, {
        fieldName: "livsmiljo1_varde",
        label: "Förslag livsmiljötyp 1"
    });
    attrs["livsmiljo1_varde"] = DomainName($feature, "livsmiljötyp1");
}

if (!IsEmpty($feature.livsmiljötyp2)) {
    Push(infos, {
        fieldName: "livsmiljo2_varde",
        label: "Förslag livsmiljötyp 2"
    });
    attrs["livsmiljo2_varde"] = DomainName($feature, "livsmiljötyp2");
}

if (!IsEmpty($feature.livsmiljötyp3)) {
    Push(infos, {
        fieldName: "livsmiljo3_varde",
        label: "Förslag livsmiljötyp 3"
    });
    attrs["livsmiljo3_varde"] = DomainName($feature, "livsmiljötyp3");
}

if (!IsEmpty($feature.justering)) {
    Push(infos, {
        fieldName: "justering_varde",
        label: "Behöver livsmiljötypen justeras?"
    });
    attrs["justering_varde"] = DomainName($feature, "justering");
}

if (!IsEmpty($feature.utbredning)) {
    Push(infos, {
        fieldName: "utbredning_varde",
        label: "Behöver utbredningen justeras?"
    });
    attrs["utbredning_varde"] = DomainName($feature, "utbredning");
}

// Förändringsorsak, förslag (nytt 2026-09-22)
if (!IsEmpty($feature.forandringsorsak_forslag)) {
    Push(infos, {
        fieldName: "forandringsorsak_forslag_varde",
        label: "Förändringsorsak, förslag"
    });
    attrs["forandringsorsak_forslag_varde"] = DomainName($feature, "forandringsorsak_forslag");
}

if (!IsEmpty($feature.kommentar_livsmil_utbred)) {
    Push(infos, {
        fieldName: "kommentar_varde",
        label: "Kommentar"
    });
    attrs["kommentar_varde"] = $feature.kommentar_livsmil_utbred;
}

if (Count(infos) == 0) {
    return {
        type: "fields",
        title: "Granskning 1: Avvikelse och korrigeringsförslag",
        fieldInfos: [{
            fieldName: "tom_info",
            label: "Information"
        }],
        attributes: {
            tom_info: "Ingen information registrerad i denna del."
        }
    };
}

return {
    type: "fields",
    title: "Granskning 1: Avvikelse och korrigeringsförslag",
    fieldInfos: infos,
    attributes: attrs
};
```

## 4. Granskning 2 — Tillstånd

```js
// Granskning 2 – Tillstånd
// Visar endast fält som innehåller ett värde.

var infos = [];
var attrs = {};

if (!IsEmpty($feature.tillstand)) {
    Push(infos, {
        fieldName: "tillstand_varde",
        label: "Tillstånd"
    });
    attrs["tillstand_varde"] = DomainName($feature, "tillstand");
}

if (!IsEmpty($feature.procent_gott)) {
    Push(infos, {
        fieldName: "procent_gott_varde",
        label: "Gott tillstånd (%)"
    });
    attrs["procent_gott_varde"] = $feature.procent_gott;
}

if (!IsEmpty($feature.procent_ej_gott)) {
    Push(infos, {
        fieldName: "procent_ej_gott_varde",
        label: "Ej gott tillstånd (%)"
    });
    attrs["procent_ej_gott_varde"] = $feature.procent_ej_gott;
}

if (!IsEmpty($feature.procent_osaker)) {
    Push(infos, {
        fieldName: "procent_osaker_varde",
        label: "Osäkert tillstånd (%)"
    });
    attrs["procent_osaker_varde"] = $feature.procent_osaker;
}

if (!IsEmpty($feature.kommentar_tillstand)) {
    Push(infos, {
        fieldName: "kommentar_varde",
        label: "Kommentar"
    });
    attrs["kommentar_varde"] = $feature.kommentar_tillstand;
}

if (Count(infos) == 0) {
    return {
        type: "fields",
        title: "Granskning 2: Tillstånd",
        fieldInfos: [{
            fieldName: "tom_info",
            label: "Information"
        }],
        attributes: {
            tom_info: "Ingen information registrerad i denna del."
        }
    };
}

return {
    type: "fields",
    title: "Granskning 2: Tillstånd",
    fieldInfos: infos,
    attributes: attrs
};
```

## 5. Granskning 3 — Kontroll och metod

```js
// Granskning 3 – Kontroll och metod
// Visar endast fält som innehåller ett värde.

var infos = [];
var attrs = {};

if (!IsEmpty($feature.kontroll1)) {
    Push(infos, {
        fieldName: "kontroll1_varde",
        label: "Vad ska kontrolleras 1"
    });
    attrs["kontroll1_varde"] = DomainName($feature, "kontroll1");
}

if (!IsEmpty($feature.kontroll2)) {
    Push(infos, {
        fieldName: "kontroll2_varde",
        label: "Vad ska kontrolleras 2"
    });
    attrs["kontroll2_varde"] = DomainName($feature, "kontroll2");
}

if (!IsEmpty($feature.kontroll3)) {
    Push(infos, {
        fieldName: "kontroll3_varde",
        label: "Vad ska kontrolleras 3"
    });
    attrs["kontroll3_varde"] = DomainName($feature, "kontroll3");
}

if (!IsEmpty($feature.kommentar_kontroll)) {
    Push(infos, {
        fieldName: "kommentar_kontroll_varde",
        label: "Kommentar – kontrollbehov"
    });
    attrs["kommentar_kontroll_varde"] = $feature.kommentar_kontroll;
}

if (!IsEmpty($feature.metod)) {
    Push(infos, {
        fieldName: "metod_varde",
        label: "Metod för kontroll"
    });
    attrs["metod_varde"] = DomainName($feature, "metod");
}

if (!IsEmpty($feature.kommentar_metod)) {
    Push(infos, {
        fieldName: "kommentar_metod_varde",
        label: "Kommentar – metod"
    });
    attrs["kommentar_metod_varde"] = $feature.kommentar_metod;
}

if (Count(infos) == 0) {
    return {
        type: "fields",
        title: "Granskning 3: Kontroll och metod",
        fieldInfos: [{
            fieldName: "tom_info",
            label: "Information"
        }],
        attributes: {
            tom_info: "Ingen information registrerad i denna del."
        }
    };
}

return {
    type: "fields",
    title: "Granskning 3: Kontroll och metod",
    fieldInfos: infos,
    attributes: attrs
};
```

## 6. Granskning 4 — Granskat och kommentarer

**Åtgärdat 2026-09-22:** kopplar nu in samtliga fem fält (`granskat`, `kommentar`, `nnk_kommentar`, `faltinventerare`, `egen_bet`) — matchar gruppens ursprungliga fältlista i `bygg_nnk_lyrx.py`.

```js
// Granskning 4
// Visar endast fält som faktiskt innehåller ett värde.

var infos = [];
var attrs = {};

// Granskat?
if (!IsEmpty($feature.granskat)) {
    Push(infos, {
        fieldName: "granskat_varde",
        label: "Granskat?"
    });
    attrs["granskat_varde"] = DomainName($feature, "granskat");
}

// Kommentar
if (!IsEmpty($feature.kommentar)) {
    Push(infos, {
        fieldName: "kommentar_varde",
        label: "Kommentar"
    });
    attrs["kommentar_varde"] = $feature.kommentar;
}

// NNK-kommentar
if (!IsEmpty($feature.nnk_kommentar)) {
    Push(infos, {
        fieldName: "nnk_kommentar_varde",
        label: "NNK-kommentar"
    });
    attrs["nnk_kommentar_varde"] = $feature.nnk_kommentar;
}

// Fältinventerare
if (!IsEmpty($feature.faltinventerare)) {
    Push(infos, {
        fieldName: "faltinventerare_varde",
        label: "Fältinventerare"
    });
    attrs["faltinventerare_varde"] = $feature.faltinventerare;
}

// Egen beteckning
if (!IsEmpty($feature.egen_bet)) {
    Push(infos, {
        fieldName: "egen_bet_varde",
        label: "Egen beteckning"
    });
    attrs["egen_bet_varde"] = $feature.egen_bet;
}

// Om alla fält är tomma
if (Count(infos) == 0) {
    return {
        type: "fields",
        title: "Granskning 4: Granskat och kommentarer",
        fieldInfos: [{
            fieldName: "tom_info",
            label: "Information"
        }],
        attributes: {
            tom_info: "Ingen information registrerad i denna del."
        }
    };
}

return {
    type: "fields",
    title: "Granskning 4: Granskat och kommentarer",
    fieldInfos: infos,
    attributes: attrs
};
```

## 7. Typiska arter (Artportalen)

Nytt uttryck (Map Viewer → NNK-ytlagret → *Configure pop-ups* → *Add content* → *Arcade*). Placera det direkt efter *Naturtyp (NNK-data)*. Texten om tidsperiod och noggrannhet gäller skriptets standardinställningar (fynd från 2010, koordinatnoggrannhet ≤ 100 m) — ändra den om skriptet körs med andra värden.

```js
// Typiska arter (Artportalen)
// Fynd av naturtypens typiska arter inom ytan, enligt artportalen_typiska_arter.py.
// typarter_antal: tomt = ytan söktes inte eller naturtypen saknar artlista,
//                 0 = söktes men inga fynd, > 0 = antal olika typiska arter med fynd.

var titel = "Typiska arter (Artportalen)";
var underlag = "Fynd från 2010, koordinatnoggrannhet ≤ 100 m. Skyddsklassade fynd ingår inte.";

// rader = lista med [etikett, värde] - en lista (inte en dictionary) så att ordningen håller
function svar(rader) {
    var infos = [];
    var attrs = {};
    for (var i in rader) {
        var namn = "rad_" + Text(i);
        Push(infos, { fieldName: namn, label: rader[i][0] });
        attrs[namn] = rader[i][1];
    }
    return { type: "fields", title: titel, fieldInfos: infos, attributes: attrs };
}

// Fälten finns inte förrän tjänsten republicerats med de nya fälten
if (!HasKey($feature, "typarter_antal")) {
    return svar([["Information", "Underlaget är inte inläst i lagret än."]]);
}

var antal = $feature.typarter_antal;

if (IsEmpty(antal)) {
    return svar([["Information", "Ingen artlista för ytans naturtyp, eller ytan ingick inte i sökningen."]]);
}

if (antal == 0) {
    return svar([
        ["Typiska arter", "Inga fynd"],
        ["Att tänka på", "Inga fynd betyder oftast att ingen har letat — inte att arterna saknas."],
        ["Underlag", underlag]
    ]);
}

var rader = [["Antal typiska arter med fynd", Text(antal)]];
if (HasKey($feature, "typarter") && !IsEmpty($feature.typarter)) {
    Push(rader, ["Arter", $feature.typarter]);
}
if (HasKey($feature, "typarter_senaste_ar") && !IsEmpty($feature.typarter_senaste_ar)) {
    Push(rader, ["Senaste fynd (år)", Text($feature.typarter_senaste_ar)]);
}
Push(rader, ["Underlag", underlag]);
return svar(rader);
```

## 8. Hävd enligt jordbruksskiften och TUVA

Nytt uttryck, placera det efter *Typiska arter (Artportalen)*. Underlag för R7A i `metodik.md`. Titeln i popupen är fortfarande *Hävd enligt jordbruksskiften* när ytan saknar TUVA-träff. Uppdaterat 2026-09-30 med TUVA-raderna och 2026-10-01 med SkötselDOS och uppföljning (titeln får då tillägget *, SkötselDOS*).

```js
// Hävd enligt jordbruksskiften och TUVA
// Skiften: Jordbruksverkets årslager av jordbruksskiften, framräknat av nnk_havd.py.
//   Ett år räknas som hävdat när minst 50 % av ytan ligger på bete- eller slåtterskifte.
// TUVA: Jordbruksverkets ängs- och betesmarksinventering, senaste inventering per objekt,
//   kopplat av nnk_tuva.py (störst överlapp, >= 1 % av ytan eller >= 0,25 ha).
// SkötselDOS: Metrias uttag 2026-10-01, utförda bete-/slåtteråtgärder och
//   uppföljningspunkter (målindikatorer), kopplat av nnk_skotseldos.py.
// Visas för hävdberoende typer, för ytor där skiftena visar hävd och för alla ytor med
// TUVA-träff, SkötselDOS-hävd eller uppföljningspunkter.

// rader = lista med [etikett, värde] - en lista så att ordningen håller
function svar(titel, rader) {
    var infos = [];
    var attrs = {};
    for (var i in rader) {
        var namn = "rad_" + Text(i);
        Push(infos, { fieldName: namn, label: rader[i][0] });
        attrs[namn] = rader[i][1];
    }
    return { type: "fields", title: titel, fieldInfos: infos, attributes: attrs };
}

var harSkiften = HasKey($feature, "havd_skiften");
var harTuvaFalt = HasKey($feature, "tuva_objekt_id");

// Fälten finns inte förrän tjänsten republicerats med de nya fälten
if (!harSkiften && !harTuvaFalt) {
    return svar("Hävd enligt jordbruksskiften", [["Information", "Underlaget är inte inläst i lagret än."]]);
}

// Inte IIf här: Arcade utvärderar båda grenarna, och fältet kan saknas
var v = null;
if (harSkiften) {
    v = $feature.havd_skiften;
}
var tuva = harTuvaFalt && !IsEmpty($feature.tuva_objekt_id);
var havdberoende = HasKey($feature, "havdberoende") && $feature.havdberoende == "Ja";
var skdos = HasKey($feature, "skdos_havd_typ") && !IsEmpty($feature.skdos_havd_typ);
var uppf = HasKey($feature, "uppf_punkter_bedomda") && !IsEmpty($feature.uppf_punkter_bedomda);
var titel = IIf(tuva, "Hävd enligt jordbruksskiften och TUVA", "Hävd enligt jordbruksskiften");
if (skdos || uppf) {
    titel += ", SkötselDOS";
}

if (IsEmpty(v) && !tuva && !skdos && !uppf) {
    return svar(titel, [["Information", "Ytan ingick inte i hävdanalysen (bara ytlagret analyseras)."]]);
}
// På övriga typer säger Nej/Oklart lite - visa ingenting, om inte ytan har TUVA-träff
if (!havdberoende && !tuva && !skdos && !uppf && (v == "Nej" || v == "Oklart")) {
    return svar(titel, [["Information", "Inte relevant för ytans naturtyp."]]);
}

var rader = [];

// ---- Skiften ----
// Alla havd_-fält publiceras tillsammans, så de finns om havd_skiften finns
if (!IsEmpty(v)) {
    var period = DefaultValue($feature.havd_period, "");
    var forklaring = Decode(v,
        "Ja", "Bete eller slåtter varje år från typens startår eller första dataåret.",
        "Delvis", "Hävd vissa år, men inte obrutet.",
        "Nej", "Ytan träffar skiften men aldrig bete eller slåtter.",
        "Oklart", "Ingen skiftesträff. Bete utan stöd syns inte i skiftesdata.",
        "");
    Push(rader, ["Hävd enligt skiften", v + IIf(period == "", "", " (" + period + ")")]);
    Push(rader, ["Förklaring", forklaring]);

    if (!IsEmpty($feature.havd_obrutet_sedan)) {
        Push(rader, ["Obruten hävd sedan", Text($feature.havd_obrutet_sedan)]);
    }
    if (v == "Delvis" && !IsEmpty($feature.havd_ar_utan_bete)) {
        Push(rader, ["År utan bete/slåtter", $feature.havd_ar_utan_bete]);
        if ($feature.havd_ar_utan_bete == "2015") {
            Push(rader, ["Att tänka på", "Bara 2015 saknas. Skiftesdata 2015 är ofullständiga, så det är troligen inget verkligt uppehåll."]);
        }
    }
    if (!IsEmpty($feature.havd_andel_bete_senaste)) {
        Push(rader, ["Andel bete/slåtter senaste året", Text($feature.havd_andel_bete_senaste) + " %"]);
    }
    if ($feature.havd_varning_vall == "Ja") {
        Push(rader, ["Varning", "Minst halva ytan låg på vall (åkermark) senaste året."]);
    }
}

// ---- TUVA ----
// Alla tuva_-fält publiceras tillsammans, så de finns om tuva_objekt_id finns
if (tuva) {
    var obj = $feature.tuva_objekt_id;
    if (!IsEmpty($feature.tuva_andel_overlapp)) {
        obj += " (täcker " + Text($feature.tuva_andel_overlapp) + " % av ytan)";
    }
    if (!IsEmpty($feature.tuva_antal_objekt) && $feature.tuva_antal_objekt > 1) {
        obj += ", ytan överlappar " + Text($feature.tuva_antal_objekt) + " TUVA-objekt, här visas det största";
    }
    Push(rader, ["TUVA-objekt", obj]);

    var ar = $feature.tuva_inv_ar;
    if (!IsEmpty(ar)) {
        var alder = Year(Now()) - ar;
        var arText = "Inventerad " + Text(ar) + " (" + Text(alder) + " år sedan)";
        if (alder > 15) {
            arText += ". Äldre än 15 år, räknas inte som aktuellt underlag (R7A)";
        }
        Push(rader, ["TUVA, inventeringsår", arText]);
    }
    if (!IsEmpty($feature.tuva_havdstatus)) {
        Push(rader, ["TUVA, hävdstatus", $feature.tuva_havdstatus]);
    }
    if (!IsEmpty($feature.tuva_havdregim)) {
        Push(rader, ["TUVA, markslag/hävdregim", $feature.tuva_havdregim]);
    }
    if (!IsEmpty($feature.tuva_igenvaxning) && $feature.tuva_igenvaxning != "Ej angiven") {
        Push(rader, ["TUVA, igenväxning", $feature.tuva_igenvaxning]);
    }
    if (!IsEmpty($feature.tuva_naturtyp)) {
        Push(rader, ["TUVA, naturtyper i objektet", $feature.tuva_naturtyp]);
    }
    if (!IsEmpty($feature.tuva_paverkan) && $feature.tuva_paverkan != "Ingen angiven") {
        Push(rader, ["TUVA, påverkan", $feature.tuva_paverkan]);
    }
    Push(rader, ["Öppna i TUVA", "https://etjanst.sjv.se/tuvaut/?f=&id=" + $feature.tuva_objekt_id]);
}

// ---- SkötselDOS: utförd bete/slåtter ----
if (skdos) {
    var sk = $feature.skdos_havd_typ;
    if (!IsEmpty($feature.skdos_havd_senaste_ar)) {
        sk += ", senast " + Text($feature.skdos_havd_senaste_ar);
        if (!IsEmpty($feature.skdos_havd_antal_ar) && $feature.skdos_havd_antal_ar > 1) {
            sk += " (" + Text($feature.skdos_havd_antal_ar) + " olika år)";
        }
    } else {
        sk += ", år saknas i åtgärdens namn";
    }
    Push(rader, ["SkötselDOS, utförd hävd", sk]);
    if (v == "Nej" || v == "Oklart") {
        Push(rader, ["Att tänka på", "Skiftena visar ingen hävd men SkötselDOS gör det. Bete utan stöd syns inte i skiftena. Kontrollera åtgärden i SkötselDOS."]);
    }
}

// ---- Uppföljning av naturtyper (målindikatorer) ----
if (uppf) {
    var up = Text($feature.uppf_punkter_bedomda) + " bedömda punkter, " +
             Text($feature.uppf_andel_bra) + " % Bra";
    if (!IsEmpty($feature.uppf_antal_dalig) && $feature.uppf_antal_dalig > 0) {
        up += ", " + Text($feature.uppf_antal_dalig) + " Dålig";
    }
    if (!IsEmpty($feature.uppf_senaste_ar)) {
        up += " (senast " + Text($feature.uppf_senaste_ar) + ")";
    }
    Push(rader, ["Uppföljning, målindikatorer", up]);
}
return svar(titel, rader);
```

---

## 9. Skog (laserdata)

Nytt uttryck, placera det efter *Hävd enligt jordbruksskiften och TUVA*. Underlag för R7B och R7C i `metodik.md`. Visas för skogstyperna (gruppen Skog, inklusive 9740 skogbevuxen myr och 9750 svämlövskog). För myrarna 7110–7231 visas bara dikesraderna, med titeln *Diken (laserdata)*. Övriga typer får en kort rad om att sektionen inte gäller.

```js
// Skog (laserdata)
// Laser: Skogsstyrelsens Skogliga grunddata, omdrev 1 (2010-2012) och omdrev 2 (2020-2023),
//   framräknat av nnk_laser.py. Bara 10 m-pixlar helt inom ytan. Värdena är modellskattningar.
// Diken: Skogsstyrelsens AI-karterade diken (NV:s vektorversion), inom ytan och i 50 m-zon runt den.

function svar(titel, rader) {
    var infos = [];
    var attrs = {};
    for (var i in rader) {
        var namn = "rad_" + Text(i);
        Push(infos, { fieldName: namn, label: rader[i][0] });
        attrs[namn] = rader[i][1];
    }
    return { type: "fields", title: titel, fieldInfos: infos, attributes: attrs };
}

var skog = [2181, 9006, 9008, 9009, 9010, 9020, 9030, 9050, 9060, 9080, 9110, 9160, 9162,
            9180, 9190, 9740, 9750];
var myrar = [7110, 7111, 7140, 7141, 7142, 7230, 7231];
var kod = null;
if (HasKey($feature, "naturtyp_kod_text") && !IsEmpty($feature.naturtyp_kod_text)) {
    kod = Number(Left($feature.naturtyp_kod_text, 4));
}
var arSkog = !IsEmpty(kod) && Includes(skog, kod);
var arMyr = !IsEmpty(kod) && Includes(myrar, kod);
var titel = IIf(arSkog, "Skog (laserdata)", "Diken (laserdata)");

if (!arSkog && !arMyr) {
    return svar("Skog (laserdata)", [["Information", "Gäller skogstyper och myrar (R7B och R7C)."]]);
}
if (!HasKey($feature, "diken_m_inom")) {
    return svar(titel, [["Information", "Underlaget är inte inläst i lagret än."]]);
}

var rader = [];

// ---- Laser (bara skog) ----
// Alla laser_-fält publiceras tillsammans med diken_-fälten
if (arSkog) {
    if (IsEmpty($feature.laser_hojd_medel)) {
        Push(rader, ["Laserdata", "Ytan är för liten (färre än tre hela 10 m-pixlar) eller saknar laserdata."]);
    } else {
        var ar = $feature.laser_skanning_ar;
        Push(rader, ["Senaste laserskanning", IIf(IsEmpty(ar), "okänt år", Text(ar))]);
        Push(rader, ["Medelhöjd", Text($feature.laser_hojd_medel / 10, "#,##0.0") + " m"]);
        Push(rader, ["Virkesvolym", Text($feature.laser_volym_medel) + " m³sk/ha"]);
        Push(rader, ["Grundyta", Text($feature.laser_grundyta_medel) + " m²/ha"]);
        Push(rader, ["Medeldiameter", Text($feature.laser_diameter_medel) + " cm"]);

        var per = DefaultValue($feature.laser_forandring_period, "");
        if (!IsEmpty($feature.laser_hojdforandring_medel)) {
            var dh = $feature.laser_hojdforandring_medel / 10;
            var dhText = IIf(dh > 0, "+", "") + Text(dh, "#,##0.0") + " m";
            Push(rader, ["Höjdförändring" + IIf(per == "", "", " " + per), dhText]);
        }
        if (!IsEmpty($feature.laser_andel_sankt)) {
            Push(rader, ["Andel sänkt mer än 5 m" + IIf(per == "", "", " " + per),
                         Text($feature.laser_andel_sankt) + " % av ytan"]);
        }
        var fl = DefaultValue($feature.laser_flagga, "");
        if (fl != "") {
            var flText = Decode(fl,
                "Möjlig avverkning", "Möjlig avverkning: höjden har sjunkit mer än 5 m på minst 10 % av ytan eller minst 0,1 ha. Kontrollera i orto och i Skogsstyrelsens avverkningsinformation.",
                "Möjlig gallring", "Möjlig gallring: grundytan har minskat tydligt men inte höjden. Kontrollera i orto.",
                "Osäker (lövat/olövat)", "Osäker: den äldsta skanningen gjordes i lövat läge, den senaste i olövat. Minskningen kan bero på det. Kontrollera i orto.",
                fl);
            Push(rader, ["Laserflagga", flText]);
        }
        Push(rader, ["Att tänka på", "Laserdata visar inte död ved eller trädslag. Förändringar efter " + IIf(IsEmpty(ar), "senaste skanningen", Text(ar)) + " syns inte."]);
    }
}

// ---- Diken (skog och myr) ----
var di = $feature.diken_m_inom;
var du = $feature.diken_m_50m;
if (!IsEmpty(di) || !IsEmpty(du)) {
    Push(rader, ["Diken inom ytan", Text(DefaultValue(di, 0)) + " m"]);
    Push(rader, ["Diken inom 50 m utanför ytan", Text(DefaultValue(du, 0)) + " m"]);
    if (DefaultValue(di, 0) > 0 || DefaultValue(du, 0) > 0) {
        Push(rader, ["Om dikena", "AI-karterade ur laserdata (Skogsstyrelsen). Kontrollera i terrängskuggning, karteringen missar igenvuxna diken och kan ta med bäckar."]);
    }
}
return svar(titel, rader);
```


## 10. Floraväkteri (Artportalen)

Nytt uttryck, placera det efter *Skog (laserdata)*. Underlag för tillståndsbedömningen (typiska och hotade arter) och en kontroll av hävden i R7A. Visas bara för ytor med minst en floraväktarrapport, övriga ytor får en kort rad.

```js
// Floraväkteri (Artportalen)
// Floraväktarnas rapporter (projekten Floraväkteri Sverige och Arkiv Floraväktarlokaler) ur
//   SLU:s publika SOS-WFS, kopplat av nnk_floravakteri.py: punkt inom ytan, noggrannhet <= 100 m.
//   Skyddsklassade fynd finns inte i den publika tjänsten och saknas alltså här.

function svar(titel, rader) {
    var infos = [];
    var attrs = {};
    for (var i in rader) {
        var namn = "rad_" + Text(i);
        Push(infos, { fieldName: namn, label: rader[i][0] });
        attrs[namn] = rader[i][1];
    }
    return { type: "fields", title: titel, fieldInfos: infos, attributes: attrs };
}

var titel = "Floraväkteri (Artportalen)";
if (!HasKey($feature, "fv_antal_arter")) {
    return svar(titel, [["Information", "Underlaget är inte inläst i lagret än."]]);
}
if (IsEmpty($feature.fv_antal_arter)) {
    return svar(titel, [["Information", "Inga floraväktarrapporter i ytan."]]);
}

var rader = [];
var ar = $feature.fv_senaste_ar;
var alder = Year(Now()) - ar;
Push(rader, ["Arter", $feature.fv_arter]);
Push(rader, ["Antal", Text($feature.fv_antal_arter) + " arter, " + Text($feature.fv_antal_rapporter) + " rapporter"]);
Push(rader, ["Senaste rapport", Text(ar) + IIf(alder > 10, " (äldre än 10 år)", "")]);
if ($feature.fv_hotade_arter > 0) {
    Push(rader, ["Hotade arter (CR/EN/VU)", Text($feature.fv_hotade_arter)]);
}
if ($feature.fv_bilaga2_arter > 0) {
    Push(rader, ["Arter i habitatdirektivets bilaga 2", Text($feature.fv_bilaga2_arter)]);
}
if ($feature.fv_ej_aterfunna > 0) {
    Push(rader, ["Ej återfunna", Text($feature.fv_ej_aterfunna) + " arter, senaste rapporten säger ej återfunnen"]);
}
if ($feature.fv_minskande > 0) {
    Push(rader, ["Minskande", Text($feature.fv_minskande) + " arter, senaste antal under hälften av första"]);
}
if ($feature.fv_anm_havd > 0) {
    Push(rader, ["Anmärkning om hävd", Text($feature.fv_anm_havd) + " rapporter nämner igenväxning eller upphört bete. Läs kommentaren i Artportalen."]);
}
Push(rader, ["Att tänka på", "Skyddsklassade arter ingår inte. Rapporterna gäller arternas växtplatser, inte hela ytan."]);
return svar(titel, rader);
```
