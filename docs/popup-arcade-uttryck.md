# Popup-uttryck (Arcade) — LstD NNK Granskning

## Länsstyrelsen i Södermanlands län · Naturskyddsenheten · NNK 2026

**Version:** 1.0 · 2026-09-22
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
