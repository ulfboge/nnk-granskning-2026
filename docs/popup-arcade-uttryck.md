# Popup-uttryck (Arcade) — LstD NNK Granskning

## Länsstyrelsen i Södermanlands län · Naturskyddsenheten · NNK 2026

**Version:** 1.3 · 2026-09-30 (sektion 8 utökad med TUVA). 1.2 · 2026-09-29 (sektion 7 Typiska arter och sektion 8 Hävd enligt jordbruksskiften tillagda)
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
- **Bevarandeplan, fastställd (år)** (`bevarandeplan_ar`) tillagt i *Naturtyp (NNK-data)* 2026-09-22, på Johans önskemål — visar vilket år den senaste bevarandeplanen för N2000-siten fastställdes (tomt för siter utan bevarandeplan). Fältet är nytt och sätts av `jobbdator_koppla_nnk_skyddskategori.py` (kräver att `data/analysis/bevarandeplan_platser.csv` kopieras till jobbdatorn, se README/kvarvarande_punkter_20260922.md) — **hela pipelinen måste köras om** (koppla_nnk_skyddskategori → forbered_gdb_for_publicering → bygg_nnk_lyrx → republicera) innan fältet finns i tjänsten.

- **Typiska arter (Artportalen)** — ny sektion 7, tillagd 2026-09-29. Visar fälten `typarter_antal`, `typarter` och `typarter_senaste_ar`, som sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `typiska_arter_per_yta.csv` (framräknad av `natura-2000: scripts/analysis/artportalen_typiska_arter.py`). Uttrycket kontrollerar med `HasKey` att fälten finns, så det går att klistra in innan tjänsten är republicerad — sektionen visar då bara en rad om att underlaget saknas.
- **Hävd enligt jordbruksskiften** — ny sektion 8, tillagd 2026-09-29. Visar fälten `havd_skiften`, `havd_obrutet_sedan`, `havd_ar_utan_bete`, `havd_andel_bete_senaste`, `havd_varning_vall` och `havd_period`, som sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `havd_for_granskning.csv` (framräknad av `natura-2000: scripts/analysis/nnk_havd.py`). Sektionen visas bara för hävdberoende typer och för ytor där skiftesdata visar hävd — på övriga ytor säger värdet lite. Samma `HasKey`-skydd som sektion 7.
- **TUVA i sektion 8** — tillagt 2026-09-30. Fälten `tuva_objekt_id`, `tuva_andel_overlapp`, `tuva_antal_objekt`, `tuva_inv_ar`, `tuva_havdstatus`, `tuva_havdregim`, `tuva_igenvaxning`, `tuva_naturtyp` och `tuva_paverkan` sätts av `jobbdator_koppla_nnk_skyddskategori.py` ur `tuva_for_granskning.csv` (framräknad av `natura-2000: scripts/analysis/nnk_tuva.py`). Sektionen visas nu också för alla ytor med TUVA-träff, oavsett naturtyp och skiftesvärde. Inventeringsåret visas med ålder, och TUVA äldre än 15 år markeras. `HasKey`-skyddat för sig, så uttrycket fungerar både före och efter att TUVA-fälten publicerats.

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

Nytt uttryck, placera det efter *Typiska arter (Artportalen)*. Underlag för R7A i `metodik.md`. Titeln i popupen är fortfarande *Hävd enligt jordbruksskiften* när ytan saknar TUVA-träff. Uppdaterat 2026-09-30 med TUVA-raderna.

```js
// Hävd enligt jordbruksskiften och TUVA
// Skiften: Jordbruksverkets årslager av jordbruksskiften, framräknat av nnk_havd.py.
//   Ett år räknas som hävdat när minst 50 % av ytan ligger på bete- eller slåtterskifte.
// TUVA: Jordbruksverkets ängs- och betesmarksinventering, senaste inventering per objekt,
//   kopplat av nnk_tuva.py (störst överlapp, >= 1 % av ytan eller >= 0,25 ha).
// Visas för hävdberoende typer, för ytor där skiftena visar hävd och för alla ytor med TUVA-träff.

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
var titel = IIf(tuva, "Hävd enligt jordbruksskiften och TUVA", "Hävd enligt jordbruksskiften");

if (IsEmpty(v) && !tuva) {
    return svar(titel, [["Information", "Ytan ingick inte i hävdanalysen (bara ytlagret analyseras)."]]);
}
// På övriga typer säger Nej/Oklart lite - visa ingenting, om inte ytan har TUVA-träff
if (!havdberoende && !tuva && (v == "Nej" || v == "Oklart")) {
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
return svar(titel, rader);
```
