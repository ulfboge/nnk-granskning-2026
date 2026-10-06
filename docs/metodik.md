# Från förvaltarkunskap till NNK

*Metodik för att fånga in och registrera Naturvårdsenhetens kunskap om livsmiljötyper*

**Version 2.2 · 2026-10-06** · Gäller Natura 2000-områden och statliga naturreservat i Södermanlands län  
*Senaste ändring:* R7 anger när bevarandeplanen räknas som underlag för typ och tillstånd, och alla 197 planer har nu fastställelseår. [Versionshistorik och källor](#om-dokumentet) längst ned.

---

## 1. Varför detta är rätt spår — och att det är sanktionerat

Naturvårdsverket säger uttryckligen att lokalkännedom är en godkänd kunskapskälla. Det är värt att ha citaten redo när du tar upp det internt:

> "För att säkerställa att rätt livsmiljötyp anges behövs ofta kompletterande information, **såsom lokalkännedom och/eller nyare fältinventeringar**."
> — Handledning för NNK, avsnitt 4.1

> "Utgå ifrån **befintlig kunskap från löpande förvaltning** och titta vid behov på kartunderlag, bevarandeplaner och skötselplaner."
> — Lathund granskning WebbGIS-KartLitS, *Utgångspunkter*

> "I bevarandeplaner, beslut och skötselplaner tillsammans med annan information som samlats in vid skyddsarbete, **förvaltning** eller vid uppföljning."
> — FAQ fråga 9, om vilken befintlig kunskap som ska användas

Och avgörande: karteringsstatus **2 – Granskad vid skrivbordet** definieras som *"Denna yta har granskats av länsstyrelsen baserat på kunskap från t ex andra inventeringar"*. Det finns alltså redan en färdig kod för precis den här sortens kunskap. Du behöver inte uppfinna någon konstruktion — du behöver bara använda den.

---

## 2. Vad NNK-uttaget säger om problemets storlek

Analys av `natura-2000: docs/underlag/kartering.csv` respektive `natura-2000: docs/underlag/naturtypskarta/NNK_YTA` — **samma lager**, 14 830 polygoner, hela länet, alla skyddsformer.

> **Viktigt om källan.** Detta är den **publika** Natura naturtypskartan, inte NNK Ajourhålla. Handledningen (avsnitt 1.3) säger att den publika versionen extraheras ur Ajourhålla och att *"några av attributen som finns i NNK Ajourhålla tas bort, såsom kommentarer och användaruppgifter"*. Tre fält är följaktligen tomma i samtliga 14 830 rader: `KOMMENTAR`, `NNK_KOMMEN` och `REDIGERARE`. **Det går alltså inte att dra slutsatsen att kommentarsfältet är oanvänt i länet** — det är borttaget ur exporten. Beviset ligger i datat: `REDIGERATA` (datum för attributredigering) har värden i 12 612 rader medan `REDIGERARE` (vem som redigerade) är tomt i alla 14 830. Attributen *har* redigerats; användaruppgifterna är strippade.
>
> **Konsekvens:** allt som rör grunder, kommentarer och vem som gjort vad går inte att läsa ur den publika exporten — det krävde ett uttag ur **NNK Ajourhålla** via ArcGIS Pro. Ett sådant länsuttag hämtades **2026-08-26** (se avsnitt 8–9) och innehåller `kommentar`, `nnk_kommentar` samt redigeringshistorik (`created_user`/`last_edited_user`/`last_edited_date`). Den publika versionen duger fortfarande bäst för en snabb översikt av utbredning, naturtyp, status och datum — frågor om grund och spårbarhet besvaras nu ur länsuttaget, inte genom att vänta på ett nytt.

Följande går däremot att läsa direkt ur den publika versionen, eftersom dessa fält inte strippas:

| Observation | Antal | Innebörd |
|---|---|---|
| Polygoner med `NATURTYPSS = 5` (ej bedömd status) | 13 266 (89 %) | |
| — varav karteringsstatus **2 Granskad vid skrivbordet** | **9 824** | Ytan har granskats, men tillståndet registrerades aldrig |
| — varav karteringsstatus **3 Besökt i fält** | 122 | |
| — varav karteringsstatus **4 Inventerad i fält** | 155 | |
| — varav karteringsstatus **5 Åtgärdas** | 141 | |
| — varav karteringsstatus 1 Ej granskad | 2 592 | |
| — varav karteringsstatus saknas | 432 | |

**a) 277 ytor har faktisk fältkunskap men saknar tillståndsbedömning.** Någon har varit på plats — och tillståndet finns inte i NNK. Det är den snabbaste vinsten i hela uppdraget och kräver inget nytt fältarbete, bara att någon letar rätt på protokollet. Kontrollera `kommentar`-fältet för just dessa ytor i länsuttaget från Ajourhålla (hämtat 2026-08-26, se avsnitt 8) — där kan grunden redan stå.

**b) 141 ytor har karteringsstatus 5 "Åtgärdas".** Här skiljer sig de två källorna åt, och båda betydelserna är relevanta:

- Den **publika produktbeskrivningen** kallar koden *"äldre kod som finns kvar från basinventeringen"* som betydde *"att det behövdes kompletterande uppgifter för att bestämma naturtypen"*.
- **Handledningen 2026** (tabell 7) beskriver den som länsstyrelsens administrativa stöd för ytor man bör återkomma till, och som *ska* kompletteras med en kommentar.

Datat pekar entydigt på den första: 139 av 141 har ursprung BIDOS, samtliga redigerades 2007–2008 (tre stycken 2019), och alla har naturtypsstatus 5. Det här är alltså **basinventeringens egen markering "vi kunde inte bestämma naturtypen här" — en dokumenterad kunskapslucka som stått öppen i nitton år.** Efter koppling till områdesidentitet (avsnitt 8) visar de sig ligga koncentrerat i sju objekt:

| Objekt | Antal ytor | Areal | Dominerande livsmiljötyper |
|---|---|---|---|
| SE0220129 Skärgårdsreservaten | 91 | 48,4 ha | 9070/9071/9072 trädklädd betesmark (33), 1630 strandäng (18), 8230/8231 hällmarkstorräng (14) |
| SE0220020 Strandstuviken | 25 | 35,9 ha | 1630 strandäng (15), 6910 öppen kultiverad gräsmark (5) |
| SE0220174 Marvikarna | 7 | 55,2 ha | 3110 näringsfattiga slättsjöar (2), 4810 obestämd hed/gräsmark (2) |
| SE0220602 Vilsta | 6 | 5,3 ha | 7142 kärr och gungflyn (4), 9070 trädklädd betesmark (2) |
| SE0220231 Rågö | 5 | 1,9 ha | 1630 strandäng (4) |
| SE0220337 Storhultet | 4 | 28,0 ha | 9080 lövsumpskog (3), 9010 taiga (1) |
| SE0220176 Tovhulta stormosse | 3 | 12,6 ha | 7110 högmossar (3) |

Fördelningen är talande: nästan uteslutande hävdberoende marker — precis den kategori FAQ fråga 11 sätter högst. Och den ligger i objekt som redan är prioritet 1 i arbetsplanen. **Det gör listan till den bästa öppningsfrågan i ett förvaltarsamtal.**

**c) FAQ fråga 4 kräver spårbarhet som den publika versionen inte kan visa.** Ni ska ange *vad som ligger till grund för bedömningen av utbredning*, *vad som ligger till grund för bedömningen av tillstånd*, och *hur aktuella dessa två bedömningar är*. Detta går nu att kontrollera direkt i länsuttaget från 2026-08-26 (se avsnitt 8) — det avgör om detta är en lucka eller bara var osynlig i den publika exporten. Oavsett svar gäller regeln framåt: ingen ytredigering bör lämna kommentarsfältet tomt.

---

## 3. Flödet — två steg, inte ett

Förvaltarkunskap är i regel andrahandsinformation som du inte själv har verifierat. Den ska inte gå rakt in i den nationella databasen. Använd det tvåstegsflöde KartLitS är byggt för:

```
   FÖRVALTARE                DU                        NNK Ajourhålla
   (Naturvårdsenheten)       (Naturskyddsenheten)      (nationell databas)

   ┌─────────────┐    1     ┌──────────────────┐  3   ┌──────────────────┐
   │ Blankett /  │ ───────► │ WebbGIS-KartLitS │ ───► │ ArcGIS Pro       │
   │ samtal      │          │ granskningslager │      │ ut-/incheckning  │
   │             │          │  = FÖRSLAG       │      │  = SKARPT        │
   └─────────────┘          └──────────────────┘      └──────────────────┘
                                     │  2                      ▲
                                     ▼                         │
                             Avstämning: räcker            Endast det du
                             underlaget? Ska något         står bakom
                             fältkontrolleras först?
```

> **Granskningslagret för D-län.** `LstAB NNK granskning`, som nämns i den nationella Lathund granskning WebbGIS-KartLitS, är **Stockholms läns (AB) eget publicerade lager** — det används som illustrativt exempel i den nationella lathunden ("Se exemplet nedan för Stockholm"), inte ett gemensamt resurslager alla län delar. Enligt `Manual NNK mall för granskning.pdf` (i KartLitS-mallzippen) ska varje län själv begära ett eget uttag ur NNK Ajourhålla, kopiera in det i mallen och publicera ett eget hostat lager, namngivet med länets kod som prefix. Södermanlands eget lager — **`LstD NNK Granskning`**, plus ett tillhörande referenslager för skyddade områden — är byggt och publicerat: länsuttaget hämtades 2026-08-26 och lagren publicerades i Länsstyrelsens interna ArcGIS Enterprise-portal från och med 2026-09-01, med en tillhörande WebbGIS-app skapad via GK Konfigurator. Se `docs/webbgis-publicering.md` för hela publiceringsprocessen. Metadataposten i Geodatakatalogen (informationsklassning, åtkomst- och användningsrestriktioner) höll fortfarande på att stämmas av med GIS-avdelningen per 2026-09-11 — det påverkar inte att lagret går att använda för granskning.

**Varför två steg:**

- Granskningslagret är designat som ett *förslagslager* — dess rullistor heter "Livsmiljötyp, **behov av justering**" och "Tillstånd, **behov av justering**". Det är rätt hemvist för "förvaltaren tror att…".
- Lagret har fält som NNK saknar och som är byggda för just spårbarhet: `faltinventerare`, `egen_bet`, `kommentar_kontroll`, `Kommentar_metod`, `kommentar_livsmil_utbred`, samt `kontroll1–3` och `metod` för vad som återstår att kontrollera.
- Enligt FAQ fråga 9.1 är det granskningslagret som blir underlaget till planen för 2027. Kunskap som stannar där är alltså inte bortkastad — den är levererad.
- Om förvaltarens uppgift senare visar sig fel har du inte kontaminerat den nationella databasen.

**När hoppa direkt till steg 3?** När uppgiften är dokumenterad och du kan hänvisa till källan — ett uppföljningsprotokoll, en ängs- och betesmarksinventering, en skötselplan med daterad statusbeskrivning. Då är det inte hearsay utan ett kunskapsunderlag, och karteringsstatus 2 gäller direkt.

---

## 4. Fältmappning — vilken uppgift hamnar var

Kolumnnamnen i blanketten (`blankett_forvaltarkunskap_nnk.xlsx`) är valda så att de mappar rakt av.

| Vad förvaltaren berättar | Blankettkolumn | Granskningslager (WebbGIS) | NNK Ajourhålla |
|---|---|---|---|
| "Det är rätt livsmiljötyp" | Stämmer livsmiljötyp | `justering` = *Inget behov av justering* | `NATURTYP` oförändrad |
| "Det är egentligen 9070, inte 9010" | Föreslagen livsmiljötyp 1–3 | `justering` = *Ändring till annan livsmiljötyp*, `livsmiljötyp1–3` | `NATURTYP` |
| "Det är inte livsmiljötyp än, men kan bli" | Föreslagen livsmiljötyp 1–3 + Utvecklingsmark = Ja | `justering` = *Ändring till utvecklingsmark*, `livsmiljötyp1–3` blir målnaturtyper | `NATURTYPSS` = 3, `MALNATUR1–3` |
| "Den är i bra skick" | Tillstånd = Gott | `tillstand`, `procent_gott` | `NATURTYPSS` = 1 |
| "Den är igenvuxen / behöver restaureras" | Tillstånd = Icke gott | `tillstand`, `procent_ej_gott` | `NATURTYPSS` = 2 |
| "Halva ytan är fin, halva har vuxit igen" | Andel gott / ej gott / osäker (%) | `procent_gott`, `procent_ej_gott`, `procent_osaker` | Nya tillståndsfält, **driftsätts sept 2026** |
| "Jag vet inte" | Tillstånd = Okänt | `tillstand` = *Okänt (kan ej bedöma)* | `NATURTYPSS` = 5 |
| "Gränsen stämmer inte" | Utbredning, behov av justering | `utbredning` | Geometri — **endast om ≥ minsta karteringsenhet** |
| **På vilken grund** hen vet det | Grund för bedömning | `Kommentar_metod` + `metod` | `KOMMENTAR` |
| **När** hen senast var där | År för senaste bedömning | `habitat_period_lastdata_end` | Slutdatum senaste inventering |
| **Vem** som bedömt | Bedömare | `faltinventerare` | `KOMMENTAR` (namn + roll) |
| **Varför** uppgiften ändras — nästan alltid att kunskapen fanns men aldrig registrerats | — (sätts av dig, se R2 i blanketten) | `forandringsorsak_forslag` (Förändringsorsak, förslag) | `FÖRÄNDRINGSORSAK` |
| "Det borde någon titta närmare på" | Vad ska kontrolleras | `kontroll1–3`, `kommentar_kontroll` | `KARTERINGS` = 5 + `KOMMENTAR` |
| Fri kommentar | Kommentar | `kommentar_tillstand` / `kommentar_livsmil_utbred` | `KOMMENTAR` |

`forandringsorsak_forslag` är granskarens eget förslag och ligger i formulärgruppen *1. Avvikelse och korrigeringsförslag*. Det är skilt från det skrivskyddade källfältet `forandringsorsak`, som visar NV:s nuvarande registrerade värde. Samma tre koder: 1 Rättning, 2 Faktisk förändring, 3 Komplettering. Välj 3 Komplettering i nästan alla fall; 2 bara vid en verklig, daterad förändring på marken.

**Skrivskyddade stödfält.** Granskningslagret har också några fält som länets egen pipeline fyller i (`jobbdator_koppla_nnk_skyddskategori.py`). Du ändrar dem aldrig, men de är bra att ha framför sig i samtalet:

| Fält (alias) | Innehåll | Motsvarighet i blanketten |
|---|---|---|
| `prio` (Prioklass NNK (P1-P4)) | Objektets prioritetsklass enligt arbetsplanen 5.2. Går att filtrera på i webbGIS | Kolumn A *Prio* |
| `bevarandeplan_ar` (Bevarandeplan, fastställd (år)) | Året för bevarandeplanens gällande version (fastställd eller senast uppdaterad). Finns för alla 197 områden | Kolumn K *År* (bevarandeplanens årtal) och kolumn L *Bevarandeplan (skrivbord)* |
| `area_ha` (Areal (ha)) | Polygonens areal, 2 decimaler | Kolumn G *Areal (ha)* (summerad per objekt och livsmiljötyp) |
| `naturtyp_kod_text` (Naturtyp (kod + klartext)) | T.ex. "9010 - Taiga" | Kolumn D–E *Kod*, *Livsmiljötyp* |

Blankettens kolumn J *Bevarandestatus* (bevarandetillståndet enligt bevarandeplanen) har ingen egen motsvarighet i lagret. Den är ett skrivbordsunderlag inför bedömningen av `tillstand` och är inget facit. Sedan blankettversion 1.9 finns alla 197 Natura 2000-objekt med, även de som saknar terrester livsmiljötyp (P4 m.fl.).

**Kodvärden för `Vad ska kontrolleras`** (från lathunden, tre likadana rullistor så flera val går att göra): Typiska och karakteristiska arter · Strukturer · Hävd · Funktioner (hydrologi, störningar) · Morfologi (jordart, formationer) · Annan negativ påverkan

*Se [Typiska och karakteristiska arter](typiska-arter.html) för artlistor per naturtyp, som stöd när detta väljs.*

**Kodvärden för `Metod för kontroll`**: Fältbesök · Fältinventering (standardiserad metodik) · Skrivbord / Granska mot andra underlag · Annan metod
*Obs: detta fält är framåtsyftande — det anger vilken metod som **bör** användas, inte hur du hittills gjort.*

---

## 5. Beslutsregler — där det går fel

### R1. Igenväxning på grund av utebliven skötsel ändrar inte livsmiljötypen

Detta är den vanligaste och allvarligaste fällan i förvaltarsamtal, eftersom en förvaltare naturligt säger "den ängen är ingen äng längre".

> "Behåll dock livsmiljötypen om en faktisk förändring beror på brist på 'nödvändiga bevarandeåtgärder' – det är inte en giltig anledning att ändra, snarare har länen skyldighet att vidta nödvändiga bevarandeåtgärder. Ytan är då förmodligen i 'Icke gott tillstånd' (restaureringsmark enligt basinventeringsmanualer)."
> — Lathunden, *Vad kan vi ändra på?*

**Rätt hantering:** livsmiljötypen står kvar, `NATURTYPSS` sätts till **2 – Icke fullgod**. FAQ fråga 22 säger samma sak: om prioriterade bevarandevärden håller på att förloras ska de återställas snarare än klassas om, särskilt när orsaken är brist på skötsel, praktiska överväganden eller omfattande störningar.

Konsekvensen om man gör fel: länets areal av hävdberoende livsmiljötyper krymper på papperet, restaureringsbehovet försvinner ur statistiken, och NRF-uppföljningen visar en förbättring som inte finns.

### R2. Förändringsorsak — nästan aldrig kod 2

Handledningen 5.4: attributet finns *"för att kunna identifiera och sammanställa verkliga arealförändringar för livsmiljötyper från kvalitetsförbättrande åtgärder i databasen"*.

| Situation | `FORANDRING` |
|---|---|
| Kunskapen fanns hos förvaltaren men var aldrig registrerad | **3 – Komplettering** |
| Karteringen var fel från början (flygbildstolkningen missade) | **1 – Rättning av felaktig kartering** |
| Naturen har faktiskt förändrats sedan karteringen | **2 – Faktisk förändring av bevarandestatus/naturtypsareal** |

Nästan all förvaltarkunskap är **kod 3**. Slarvar du och sätter kod 2 rapporterar länet in arealförändringar som aldrig hänt.

### R3. Karteringsstatus speglar underlaget, inte din ansträngning

| Underlag | `KARTERINGS` |
|---|---|
| Förvaltarens minnesbild, skötselplan, bevarandeplan, äldre inventering | **2 – Granskad vid skrivbordet** |
| Förvaltaren har faktiskt varit på ytan nyligen och kan bedöma naturtypen | **3 – Besökt i fält** |
| Standardiserad inventering: uppföljning, ängs- och betesmarksinventering, basinventeringsmetodik | **4 – Inventerad i fält** |
| Du vet att något är fel men inte vad | **5 – Åtgärdas** + obligatorisk kommentar |

Handledningen är tydlig med att kod 2 förutsätter att *"underlaget som använts bedöms vara så aktuellt att uppgifterna fortfarande är giltiga"*. En förvaltares minnesbild från 2015 av en hävdberoende mark är sannolikt inte aktuell — då är svaret okänt tillstånd plus kod 5, inte en gissning.

### R4. Osäkerhet dokumenteras, den gissas inte bort

> "Är ni inte säkra, och det inte går att prioritera fältinsatser för att inhämta tillräcklig kunskap om förhållandena idag är det bättre att behålla tidigare bedömning eller till exempel ange att tillståndet är okänt eller inte gott. Dokumentera vad ni är osäkra på, så det kan kontrolleras eller följas upp när det kan prioriteras."
> — FAQ fråga 22

Ett dokumenterat "okänt" med angiven anledning är en fullgod leverans 2026. En gissning är det inte.

### R5. Utvecklingsmark har två formella krav

Lathunden: *"Används målnaturtyper så förutsätts att Naturtypsstatus är satt till 'Utvecklingsmark' och att **Naturtyp utgörs av en icke-natura-naturtyp**."*

Alltså: en yta kan inte samtidigt vara livsmiljötyp 6270 och utvecklingsmark mot 6270. Är den redan livsmiljötyp är den livsmiljötyp — i gott eller icke gott tillstånd. Upp till tre målnaturtyper får anges (`MALNATUR1–3`).

I hela länet har idag bara 87 polygoner en angiven målnaturtyp. Förvaltarna vet i regel mycket väl vilka ytor som är på väg åt rätt håll — det är en av de mest värdefulla sakerna att fråga om, och FAQ fråga 23 påpekar att ytor med påtaglig utvecklingspotential normalt är högre prioriterade för skydds- och skötselresurser.

### R6. Utpekade livsmiljötyper har ett särskilt skydd

> "Vi har ett särskilt ansvar för livsmiljötyper som legat till grund för utpekandet av ett Natura 2000-område och som tidigare har rapporterats för området. Det samma gäller prioriterade bevarandevärden som är en del av syfte och skäl för ett beslut om naturreservat. Livsmiljötyper som utgör prioriterade bevarandevärden bör karteras mer noggrant och **enbart ändras om tidigare bedömningar är uppenbart fel eller det faktisk skett en förändring**."
> — FAQ fråga 19

Kontrollera därför alltid bevarandeplanen innan du ändrar en utpekad typ. Länken finns i WebbGIS-lagret *NV Natura2000 områden*, raden `BEVPLAN` i attributtabellen.

### R7. Regelstyrd skrivbordsbedömning av naturtypsstatus — UTKAST

> **Utkast 2026-09-29.** Regeln används inte skarpt förrän piloten nedan är genomförd och fältkontrollerad. Bedömningar enligt R7 förs in som **förslag i granskningslagret**, inte direkt i NNK.

**Varför:** 6 847 av länets 7 673 delytor med Natura-naturtyp har *Ej bedömd status* (publika NNK-uttaget). De flesta kommer från BIDOS och har aldrig fått sin status satt. Handledningen säger att status ska uppdateras "om det är möjligt", och FAQ 13 godtar äldre underlag när risken för förändring är låg. Där underlaget räcker kan status alltså sättas vid skrivbordet.

**Gäller:** ytor med Natura-naturtyp och Naturtypsstatus 5. Gäller **inte** marina typer (1110–1170, FAQ 16/29) eller obestämda/osäkra koder — de behöver typbestämning först.

**Förutsättning för alla grupper — typen ska vara rimlig.** Minst ett underlag som är nyare än karteringen och oberoende av den ska stödja typen: TUVA-objekt med samma typ, bevarandeplan som anger typen i området (se *Bevarandeplanen som underlag* nedan), fältprotokoll eller fynd av typiska arter. Ortofoto får inte motsäga den. BIDOS-ytor prövas mot gällande vägledning (för 9010 och 9050 versionen från februari 2026). Stöds inte typen gäller inte R7 — ytan får Karteringsstatus 5 (*Åtgärdas*) och en kommentar.

**Registrering:** Karteringsstatus 2 (R3), Förändringsorsak 3 (R2). Kommentaren anger delregel (t.ex. "R7A") och källor med år.

**Utfall:** varje delregel ger *fullgod*, *icke fullgod* eller *till fält*. *Till fält* är ett fullgott utfall — FAQ 11 säger att man ska invänta NV:s och HaV:s metoder där tillståndet inte är tydligt (R4).

| Grupp (regel) | Typer |
|---|---|
| **Hävd** (R7A) | 1630, 4030, 5130, 5133, 6110, 6210, 6230, 6270, 6280, 6410, 6430, 6510, 8231, 9070, 9071, 9072 |
| **Skog** (R7B) | 2181, 9006, 9008, 9009, 9010, 9020, 9030, 9050, 9060, 9080, 9110, 9160, 9162, 9180, 9190, 9740, 9750 |
| **Våtmark** (R7C) — myr, våtmark, sjö | 3110, 3130, 3150, 3160, 3260, 7110, 7111, 7140, 7141, 7142, 7230, 7231 |
| **Stabila** (R7D) — strand, klippa, skär | 1220, 1230, 1232, 1620, 1621, 1640, 8210, 8220, 8230, 8232 |

> **Grupp är inte batch.** Batcherna S, A, B, C och D i arbetsplanen är arbetsordningen per Natura 2000-område. Grupperna ovan avgör vilken delregel som gäller för en enskild yta, och ett område innehåller ytor från flera grupper. Gruppen visas i popupen som *Bedömningsgrupp (R7)*.

#### R7A · Hävd

| Utfall | Villkor |
|---|---|
| Fullgod | Obruten hävd dokumenterad från att typen sattes till i dag (stödregister/miljöersättning de senaste tre åren, skötselavtal, SkötselDOS), TUVA högst 10 år gammal utan negativa noteringar, och orto/IR-orto utan igenväxning, plöjning eller gödsling. |
| Icke fullgod | Hävden har upphört eller haft avbrott i tre år eller mer, eller ortot visar igenväxning. Typen behålls (R1). |
| Till fält | Underlagen motsäger varandra; BIDOS-typ utan TUVA eller med TUVA äldre än 15 år; 6430 där hävdberoendet är osäkert (ofta inte hävdberoende längs vattendrag). |

**Underlag för hävden — jordbruksskiften.** Granskningslagret har fältet *Hävd enligt jordbruksskiften* (`havd_skiften`), framräknat ur Jordbruksverkets årslager av jordbruksskiften 2015–2025 (grödkoder för bete och slåtter). Ett år räknas som hävdat när minst 50 % av ytan ligger på bete- eller slåtterskifte.

| Värde | Betyder | Så används det i R7A |
|---|---|---|
| Ja | Hävd varje år från typens startår, eller från 2015 | Uppfyller hävdvillkoret för *fullgod*. Kontrollera ändå orto och TUVA. |
| Delvis | Hävd vissa år men inte obrutet. Fältet *År utan bete/slåtter* visar vilka år som saknas | Ett enstaka luckår 2015 är troligen en brist i skiftesdata (färre skiften det året), inte ett uppehåll. Tre år eller mer utan hävd ger *icke fullgod*. |
| Nej | Ytan träffar skiften men aldrig bete | Även en smal kantträff mot åker räcker, så värdet säger lite på skogs- och myrytor. På hävdberoende typer tyder det på upphörd hävd — pröva *icke fullgod* mot ortot. |
| Oklart | Ingen skiftesträff alls | Bete utan stöd syns inte i skiftesdata. Inget belägg åt något håll — *till fält* om inget annat underlag finns. |

*Vall senaste året* (grödkod 49, 50) är åkermark och en varningssignal, till exempel för 6270 och 6410, inte belägg för hävd. Skiftesdata ersätter inte skötselavtal och SkötselDOS, men täcker alla ytor och alla år på samma sätt.

**Underlag för hävden — TUVA.** Granskningslagret har också TUVA-fält (`tuva_objekt_id`, `tuva_inv_ar`, `tuva_havdstatus`, `tuva_havdregim`, `tuva_igenvaxning`, `tuva_naturtyp`, `tuva_paverkan`). De kommer från Jordbruksverkets ängs- och betesmarksinventering, senaste inventering per objekt (uttag 2026-08-21), och kopplas till den NNK-yta som objektet överlappar mest, med samma tröskel som för sitecode (minst 1 % av ytan eller 0,25 ha). 2 425 av länets 15 837 ytor har träff, och 1 964 av dem inventerades före 2011. TUVA beskriver marken som den var vid inventeringen, skiftena visar om den hävdats år för år 2015–2025. Använd dem tillsammans:

| Läge | Så används det i R7A |
|---|---|
| TUVA högst 10 år, välhävdad, utan negativa noteringar | Uppfyller TUVA-villkoret för *fullgod*. Hävden sedan inventeringen ska ändå synas i skiftena (*Ja*) eller i skötselavtal/SkötselDOS. |
| TUVA 11–15 år | Styrker typen och att marken hävdades då, men räcker inte för *fullgod*. Tillståndet avgörs av skiftena och ortot. Ger de inget tydligt svar: *till fält*. |
| TUVA äldre än 15 år | Räknas inte som aktuellt underlag. Finns inget annat underlag (skiften *Oklart*, inget skötselavtal eller SkötselDOS, ortot otydligt) blir utfallet ***till fält***. Gäller även när TUVA-objektet ser välhävdat ut. |
| Negativ notering i TUVA | *Ingen hävd*, *Ohävdad (restaurerbar)*, *Ej aktuell*, igenväxning *Tydlig* eller *Igenväxt*, tydlig produktionshöjande påverkan (gödsling) eller tillskottsutfodring. Pröva *icke fullgod* mot skiftena och ortot. Visar skiftena *Ja* efter inventeringsåret kan hävden ha tagits upp igen: *till fält*. |
| Skiften *Oklart* men TUVA-träff | 307 ytor. Bete utan stöd syns inte i skiftena men kan finnas i TUVA. TUVA högst 15 år kan ersätta skiftena som belägg för hävd vid inventeringen. Äldre än så: raden ovan. |
| Skiften och TUVA säger emot varandra | T.ex. skiften *Ja* och TUVA *Ingen hävd*, eller skiften *Nej* och TUVA *Välhävdad*: *till fält*. |

Fältet visar det TUVA-objekt som täcker mest av ytan. Överlappar ytan flera objekt (`tuva_antal_objekt` > 1, 169 ytor) ska de andra också kontrolleras i TUVA. Naturtyperna i `tuva_naturtyp` gäller hela TUVA-objektet, inte NNK-ytan. Samma typ där räknas som ett av beläggen för att typen är rimlig (förutsättningen ovan), men säger inget om var i objektet den ligger. TUVA har inga strukturerade uppgifter om skötselbehov, bara fritext i objektrapporten (länken *Öppna i TUVA* i popupen).

**Underlag för hävden — SkötselDOS.** Sedan 2026-10-01 har granskningslagret fält ur Metrias SkötselDOS-uttag. `skdos_havd_typ` och `skdos_havd_senaste_ar` visar utförd bete eller slåtter enligt reservatsförvaltningen (486 ytor, 159 hävdberoende). Det är det underlag som skiftena saknar för bete utan stöd. `uppf_*` sammanfattar uppföljningspunkterna för naturtyper (målindikatorer, 2015–2022) inom ytan (101 ytor).

| Läge | Så används det i R7A |
|---|---|
| SkötselDOS bete/slåtter senast 2020 eller senare | Belägg för hävd, likvärdigt med skiften *Ja* för de år som står i SkötselDOS. Tillsammans med typen rimlig och utan negativ notering: kandidat till *fullgod*. |
| Skiften *Nej*/*Oklart* men SkötselDOS bete | 53 hävdberoende ytor. SkötselDOS väger tyngre än skiftena för bete utan stöd. Kontrollera att åtgärden verkligen ligger på ytan (ortot) och inte bara på reservatet. |
| SkötselDOS utan år eller äldre än 2020 | Visar att ytan har skötts, men inte att den sköts nu. Avgörs av skiftena och ortot, annars *till fält*. |
| Uppföljning med punkter *Dålig* | 17 ytor. Pröva *icke fullgod* för de målindikatorer som brister. Punkterna är från 2015–2022, så kontrollera om skötseln ändrats sedan dess. |
| Uppföljning med enbart *Bra* | Stöd för *fullgod*, om uppföljningen är högst 10 år gammal. |

Åtgärder i SkötselDOS är ibland ritade större än den yta som faktiskt betas. Åtgärder på 200 ha eller mer är därför bortfiltrerade, men en stor fålla kan fortfarande täcka skog som inte betas.

#### R7B · Skog

| Utfall | Villkor |
|---|---|
| Fullgod | Ingen avverkning, gallring eller dikning sedan karteringen (Skogsstyrelsens avverkningsanmälningar och utförda avverkningar, laserdata, orto). Fri utveckling säkerställd (reservat, biotopskydd, naturvårdsavtal). Minst ett stöd för strukturerna, t.ex. sluten äldre skog i laserdata eller typiska arter i Artportalen. **Gäller inte 9010 och 9050**, se nedan. |
| Icke fullgod | Avverkning, gallring, dikning eller granplantering i lövtyper inom ytan efter karteringen. För 9740 och 9750 även dikning eller reglering. |
| Till fält | Ingen synlig påverkan, men strukturerna går inte att bedöma vid skrivbordet (t.ex. död ved i 9010 och 9050 enligt de nya kraven, se nedan). |

**Undantag: 9010 och 9050 kan inte bli fullgod vid skrivbordet.** Gäller 9010 med undertyperna 9006, 9008 och 9009, 9050, och den obestämda koden 9830 (9050/9010). Enligt NV:s vägledningar från 2026-02-19 ska en förekomst uppfylla *samtliga* klassningskrav för att vara livsmiljötypen. Död ved är ett av dem, alltså ett krav för typen och inte bara en del av tillståndet:

- **9010 Taiga:** en påtaglig mängd död ved som har varit död längre än ett år (bedöms efter de ekologiska förutsättningarna på platsen), och död ved av särskild betydelse för taigans arter, t.ex. grov död ved, förrötade lågor, ved i flera nedbrytningsstadier, senvuxen eller brandpåverkad ved. Kvalitetskravet gäller inte lövsuccessioner, mängdkravet gäller alltid.
- **9050 Örtrik skog med gran:** död ved som har varit död längre än ett år och som är av olika kvaliteter.

Död ved går inte att fastställa vid skrivbordet, varken i laserdata, orto eller registren. Därför:

| Läge | Utfall |
|---|---|
| Avverkning, gallring eller dikning efter karteringen | *Icke fullgod*, som för övriga skogstyper. |
| Ingen synlig påverkan | *Till fält*, även om laserdata visar sluten äldre skog och typiska arter finns. |
| Ingen synlig påverkan och indirekt stöd för död ved (vedlevande signal- eller rödlistade arter i Artportalen, fältbeskrivning, skötselplan) | *Till fält*, med kommentaren *typen trolig, död ved ej kontrollerad*. Prioritera ytan i fält. |

Frågan om befintliga NNK-ytor (karterade mot 2011 års kriterier) ska prövas om mot 2026-kriterierna ställs till NV via KartlitsN2000. Tills svar finns behandlas alla 9010- och 9050-ytor enligt tabellen ovan.

**Underlag för skogen — laserdata.** Granskningslagret har laserfält för skogsytorna (gruppen Skog, 2 918 ytor), framräknade ur Skogsstyrelsens Skogliga grunddata (10 m-raster). Länet är laserskannat två gånger: första nationella skanningen 2010–2012 och Laserdata Skog 2020 (på några ställen 2023). Nästa skanning av Södermanland görs 2026. Bara pixlar som ligger helt inom ytan räknas. 158 ytor är för små (färre än tre hela pixlar) och har tomma fält. Värdena är skattningar från en modell, inte mätningar i fält.

| Fält | Betyder | Så används det i R7B |
|---|---|---|
| `laser_hojd_medel` (dm), `laser_volym_medel` (m³sk/ha), `laser_grundyta_medel` (m²/ha), `laser_diameter_medel` (cm) | Medelvärde för ytan i den senaste skanningen (`laser_skanning_ar`) | Stöd för *sluten äldre skog*, ett av stöden för strukturerna vid *fullgod*. Volym och diameter skiljer gammal grov skog från tät medelålders skog bättre än höjden, som planar ut tidigt. Jämför mot typens median i länet: för 9010 är den 16 m, 161 m³sk/ha och 20 cm; för 9050 och 9060 kring 24 m, 360–400 m³sk/ha och 32 cm. |
| `laser_hojdforandring_medel` (dm) | Medelhöjden i senaste skanningen minus den äldsta, under `laser_forandring_period` (t.ex. 2010-2020). Negativt = sänkning | Normal tillväxt ger några dm till 1–2 m (median +0,7 m). Sänkning i medelvärdet tyder på ingrepp eller störning i en stor del av ytan. |
| `laser_andel_sankt` (%) | Andel av ytan där höjden sjunkit mer än 5 m mellan skanningarna | Fångar avverkning och kraftig gallring, även ingrepp som inte krävt anmälan, och störningar som storm och granbarkborre. |
| `laser_flagga` | *Möjlig avverkning*: minst 10 % av ytan eller minst 0,1 ha sänkt. *Möjlig gallring*: grundytan har minskat minst 3 m²/ha och 15 % medan medelhöjden inte sjunkit mer än 1 m. *Osäker (lövat/olövat)*: se begränsningar nedan | Flaggad yta prövas mot orto och Skogsstyrelsens underlag. Bekräftas ingreppet efter karteringen: *icke fullgod*. Kan orsaken vara naturlig störning (storm, brand, insekter): *till fält*, eftersom det kan vara en del av typens dynamik. Tom flagga är inget belägg för att inget har hänt, se nedan. |

*Avverkning och gallring.* Skogsstyrelsens avverkningsinformation (avverkningsanmälningar och utförda avverkningar, som tas fram ur satellitbilder varje år) är det snabbaste underlaget och täcker tiden efter 2020, som laserdata inte gör förrän nästa skanning. Laserdata kompletterar: den mäter höjd och täthet direkt och fångar ingrepp som inte kräver anmälan och gallringar som satellitdetekteringen missar. Trösklarna är förslag. Kalibrerat mot utförda avverkningar mellan skanningarna (23 ytor med avverkning på minst 0,1 ha eller 10 % av ytan) flaggas 13 av 23, och 13 av 70 flaggade ytor finns i Skogsstyrelsens register. De övriga 57 kan vara naturliga störningar, naturvårdsåtgärder eller ingrepp som är för små för satellitdetekteringen, och ska kontrolleras i orto. Gallringsflaggan går inte att kalibrera på samma sätt, eftersom gallringar inte finns i registret. Trädhöjdslagren i webbGIS (*SKS Trädhöjd 3_1*, röd och grön) är två färgskalor av samma höjd och inget förändringsskikt. De visar hur skogen ser ut men är inget belägg för ingrepp.

**Begränsningar:**
- **Död ved** syns inte tillförlitligt i laserdata. För 9010 och 9050 är död ved ett klassningskrav (vägledningarna februari 2026). Laserdata kan stödja sluten äldre skog, men utfallet blir alltid *till fält*, se undantaget ovan.
- **Trädslag.** Laserdata skiljer inte gran från löv. Granplantering eller granföryngring i lövtyper (9020, 9160, 9180, 9190 m.fl.) bedöms med Nationella marktäckedata och satellitdata, inte laser.
- **Lövat eller olövat läge.** Delar av länet skannades 2010 i lövat läge och allt 2020–2023 i olövat. I lövträd ger det skenbar sänkning och minskad grundyta. I lövdominerade typer (9020, 9080, 9110, 9160, 9162, 9180, 9190, 9750) där den äldsta skanningen var lövad ersätts därför flaggan med *Osäker (lövat/olövat)* (115 ytor). Pröva dem i orto.

#### R7C · Våtmark

| Utfall | Villkor |
|---|---|
| Fullgod | Myr och kärr: inga diken, torvtäkt eller vägar i eller i anslutning till ytan (IR-orto, laser) och ingen igenväxning. Sjöar och vattendrag: ekologisk status god eller hög i VISS och opåverkad hydromorfologi. |
| Icke fullgod | Diken som påverkar ytan, VISS-status måttlig eller sämre på grund av faktorer som är avgörande för typen, eller rikkärr där nödvändig hävd har upphört. |
| Till fält | VISS saknar klassning; rikkärr (7230) generellt. |

**Underlag för diken.** Markhöjdmodellen från laserskanningen (Lantmäteriets höjdmodell, 1 m) är det bästa underlaget för diken, eftersom diken syns i terrängskuggningen även under krontak, där de inte syns i orto. Granskningslagret har två dikesfält för skogsytorna (gruppen Skog) och myrarna i gruppen Våtmark (7110–7231), framräknade ur Skogsstyrelsens AI-karterade diken, som bygger på just höjdmodellen (Naturvårdsverkets bearbetade vektorversion, länsfil för Södermanland): `diken_m_inom` (meter dike inom ytan) och `diken_m_50m` (meter dike i en 50 m bred zon runt ytan). 749 av 3 208 ytor har dike inom ytan och ytterligare 868 har dike bara i zonen runt. Fälten räknar alla dikestyper, även vägdiken. Karteringen missar diken som är igenvuxna eller kulverterade och tar ibland med naturliga bäckar, så dikena kontrolleras i terrängskuggning (Lantmäteriets höjdmodell eller Skogsstyrelsens dikeskarta i kartan) innan de ger *icke fullgod*. Ett dike i zonen runt en myr kan dränera myrkanten och räknas som *i anslutning till ytan*.

Som kontroll av att sumpskogstyperna (9006, 9080, 9740, 9750) och myrarna ligger blött används Markfuktighetskartan (SLU och Skogsstyrelsen). Ligger en stor del av ytan i klasserna frisk eller torr, och det finns diken, är det ett tecken på att ytan dränerats.

#### R7D · Stabila

| Utfall | Villkor |
|---|---|
| Fullgod | Orto från senaste och tidigare omdrev visar ingen exploatering, täkt, bebyggelse eller igenväxning. Får bedömas gruppvis per objekt med en gemensam kommentar. |
| Icke fullgod | Exploatering, slitage eller igenväxning som påverkar typen. |
| Till fält | Sällan. |

**Hällmarkstorräng och basiska berghällar** (beslut 2026-09-29, efter NV:s vägledningar): 6110 är enligt vägledningen "i de flesta fall beroende av ett extensivt bete" och bedöms enligt R7A, liksom den hävdade undertypen 8231. 8232 (*Ej hävdberoende typ*) bedöms enligt R7D. 8230 utan undertyp bedöms på **krontäckning och igenväxning** — under 30 % krontäckning och ingen tydlig igenväxning i orto ger fullgod — eftersom vägledningen beskriver typen som störningsberoende men naturligt gles på grund av tunt jordlager och torka, särskilt vid kusten. Ligger en 8230-yta i betesmark eller ett TUVA-objekt prövas den även enligt R7A. Arbetsplanens lista över hävdberoende typer (bilaga 3) påverkas inte — den styr prioriteringen, inte bedömningen.

#### Bevarandeplanen som underlag

*Utkast 2026-10-06, del av R7.*

Popupen visar året för planens gällande version på raden *Bevarandeplan, fastställd (år)* (`bevarandeplan_ar`): fastställelsen, eller den senaste uppdateringen om planen uppdaterats. Året är utläst ur planerna själva och finns för alla 197 områden. 185 planer är från 2016 eller senare, 3 från 2014–2015 (två av dem är reservatens skötselplaner som också gäller som bevarandeplan) och 9 från 2005–2009.

**Typen.** Planen räknas som stöd för att typen är rimlig (förutsättningen ovan) bara om båda villkoren är uppfyllda:

1. Den gällande versionen är fastställd **efter karteringen** av ytan. För BIDOS-ytor är karteringen i regel från 2009–2011.
2. Planen bygger på **eget underlag** och upprepar inte bara basinventeringen eller regeringsbeslutet. Skriver planen att bedömningsunderlaget är bristfälligt, eller att inventering behövs för att avgöra om typen uppfyller kraven, räknas den inte som stöd för den typen.

Det andra villkoret går bara att pröva i själva dokumentet. Läs därför planens avsnitt om typen och om bevarandeåtgärder (steg 3 i bedömningsguiden).

**Tillståndet.** Planens bevarandetillstånd per typ (*Gynnsamt*, *Ej gynnsamt*, *Okänt*; blankettens kolumn *Bevarandestatus*) är ett myndighetsomdöme från när planen skrevs. Planen säger sällan vad det bygger på, och ett bevarandemål är inte detsamma som gott tillstånd (NV:s preliminära vägledning 2026-09-02). Därför gäller samma åldersgränser som för TUVA:

| Planens ålder (gällande version) | Så används tillståndet i R7 |
|---|---|
| Högst 10 år | Styrker utfallet men räcker aldrig ensamt för *fullgod*. *Ej gynnsamt*: pröva *icke fullgod* mot skiften, SkötselDOS och ortot, som en negativ notering i TUVA. |
| 11–15 år | Styrker typen men inte tillståndet. |
| Äldre än 15 år | Räknas inte som aktuellt underlag för tillståndet. |

Gränsen räknas från granskningsåret. 2027 passerar de 90 planerna från 2016 gränsen till 11–15 år.

#### R7-omprövning · ytor som redan har status

*Beslut 2026-10-06.*

Gäller ytor med Natura-naturtyp och Naturtypsstatus 1 *Fullgod* eller 2 *Icke fullgod*. I länets NNK-uttag (2026-08-26) är det 838 ytor, de flesta från basinventeringen (BIDOS).

*Statusen är inte daterad i sig.* Den visar bedömningen när den gjordes. Hur gammal den är får läsas ur andra fält. De tre första står i popupen under *Naturtyp (NNK-data)*; sektionen *Bedömning vid skrivbordet (R7)* sammanfattar dem på raden *Statusens ålder*:

| Fält | Vad det säger om åldern |
|---|---|
| Slutdatum senaste inventering | Rätt fält för när typen och statusen senast bedömdes. Tomt för nästan alla ytor än så länge. |
| Ursprung | *BIDOS* betyder att statusen sattes i basinventeringen. Fältdatan är då ofta 15–20 år gammal. |
| Attribut senast ändrade (`nnk_andrad_ar`, året ur NV:s `last_edited_date`, i *Statusens ålder*) | Senaste gången något attribut på ytan ändrades i NNK. Ger ett ungefärligt år när slutdatum saknas, men kan vara ett tekniskt datum från en inläsning. Använd det som "senast", inte som bevis för att någon bedömde ytan då. |
| Karteringsstatus | *Hur* bedömningen gjordes (2 skrivbord, 3 besök, 4 inventering), inte *när*. *Granskad vid skrivbordet* betyder att typ och status senast sattes utan fältbesök. |

*Regeln:*

1. **Den befintliga statusen är inget belägg för sig själv.** Att vid skrivbordet bekräfta en status från 2009 utan nytt underlag är ett antagande, inte en bedömning.
2. **Bekräfta** (behåll statusen och föreslå nytt slutdatum) bara när underlag som är *nyare än statusen* uppfyller samma villkor som delregeln för gruppen kräver för det utfallet. En hävdyta med *Fullgod* bekräftas alltså bara med obruten hävd i skiften eller SkötselDOS, ett orto utan igenväxning och TUVA högst 10 år gammal (R7A). 9010 och 9050 kan inte bekräftas som *fullgod* vid skrivbordet (R7B).
3. **Föreslå ändrad status** bara när nyare underlag tydligt visar något annat, till exempel *Fullgod* → *Icke fullgod* när skiftena visar *Nej* och ortot visar igenväxning. För utpekade typer gäller FAQ 19 (R6): ändra bara vid uppenbart fel eller faktisk förändring. *Icke fullgod* → *Fullgod* kräver samma underlag som punkt 2.
4. **Räcker inte underlaget:** låt statusen stå, föreslå inget nytt slutdatum och skriv i *Kommentar – Tillstånd*: "Status från BIDOS/[år] ej omprövad — [vad som saknas]". Fyll i *Vad ska kontrolleras* och *Metod för kontroll*. Det är ett godtagbart utfall (FAQ 22, R4).
5. **Kommentaren** anger "R7-omprövning", delregeln och källor med år, t.ex. "R7-omprövning R7A: bekräftad fullgod — skiften Ja 2015–2025, orto 2023, TUVA 2019".

Omprövningen förs in som förslag i granskningslagret, precis som övriga R7-bedömningar, och omfattas av samma pilot.

**Ytor med gammal fältdata:** 277 ytor har Karteringsstatus 3 eller 4 men ändå *Ej bedömd status*. 261 av dem kommer från BIDOS, så fältdatan är ofta 15–20 år gammal och räcker inte ensam som aktuellt underlag (R3). Den styrker att typen var rätt, men statusen prövas enligt delreglerna ovan.

#### Pilot innan regeln används skarpt

Hävdtyperna (R7A) i batch B (ängs- och hagmark i inlandet), 100 ytor med *Ej bedömd status*. 30 av dem fältkontrolleras, slumpat men med fler ur *icke fullgod* och *till fält*. Regeln godkänns om minst 27 av 30 stämmer på fullgod/icke fullgod och ingen yta visar sig ha fel typ. Annars justeras regeln innan den används på andra grupper.

#### Oklart i NV:s underlag
- Naturtypsstatus 1 definieras nu som gynnsam bevarandestatus i området. I basinventeringen betydde den att större delen av ytan uppfyller kriterierna. NV skriver själva att skillnaden "kan diskuteras".
- NNK:s nya tillståndsattribut (procent gott, inte gott och okänt) kommer hösten 2026, och FAQ 30 rekommenderar att vänta med tillståndsbedömning tills de finns. Hur naturtypsstatus 1 och 2 ska förhålla sig till procentfälten är inte beskrivet. Därför förs R7-bedömningar in som förslag i granskningslagret och registreras i NNK först när attributen finns.

---

## 6. Datering — det som glöms bort

Två nya fält i NNK, *Startdatum/Slutdatum senaste inventering av naturtypen*, motsvarar `habitat_period_lastdata_start` / `_end` i granskningslagret:

> "Slut representerar senast det gjordes en bedömning och start gången före det. Har det skett en faktisk förändring ska datumen representera den tidsperiod inom vilken förändringen skedde. Eftersom det är nya fält är dessa tomma idag, **uppdatera framför allt slutdatum när ni granskar**."
> — Handledningen, bilaga 1

Det här är den enda mekanism som gör FAQ fråga 4:s krav på *"hur aktuella dessa två bedömningar är"* besvarbart. Fråga alltid förvaltaren om årtal, även när svaret blir "någon gång runt 2018". Ett osäkert årtal är oändligt mycket bättre än inget.

---

## 7. Så lägger du upp samtalet

**Före (30 min per objekt):**

1. Ta fram objektet i WebbGIS-KartLitS, tänd `LstD NNK Granskning` och `NV Naturtypskartan NNK`
2. Läs bevarandeplanen — vilka livsmiljötyper är utpekade och vilka bevarandemål finns
3. Filtrera blanketten till objektets rader
4. Markera raderna med karteringsstatus 3, 4 eller 5 — de har en historia

**Under (45–60 min per förvaltare, flera objekt):**

1. Börja med **Åtgärdas-ytorna** — "basinventeringen kunde inte bestämma naturtypen här, vet du vad det är?" Det är den bästa öppningsfrågan som finns: den är konkret, den erkänner att kunskapen finns hos dem, och den gäller en lucka som stått öppen sedan 2008.
2. Gå igenom hävdberoende marker objekt för objekt: hävdas den, av vem, hur länge till, vad är trenden
3. Fråga efter **dokument du inte känner till**: uppföljningsprotokoll, ÄoB-blanketter, konsultrapporter, gamla skötselplansbilagor, foton. Handledningen kallar det kompletterande information — det är guld och ligger ofta på en enhets-mapp ingen letat i.
4. Fråga specifikt om **utvecklingsmark**: vilka ytor är på väg att bli livsmiljötyp, vilka har ni restaurerat
5. Fråga om **gränser** bara där det rör större arealer — under minsta karteringsenhet är det inte värt tiden
6. Avsluta med: vad borde vi kontrollera i fält, och vilka objekt kan vi lämna som de är

**Efter (30 min per objekt):**

1. För in i granskningslagret samma vecka — minnesbilder av andras minnesbilder blir snabbt oanvändbara
2. Sätt `faltinventerare` = förvaltarens namn, inte ditt
3. Sätt `habitat_period_lastdata_end` = året förvaltaren angav
4. Sätt `forandringsorsak_forslag` = 3 Komplettering, om inte naturen faktiskt har förändrats
5. Skriv `Kommentar_metod` i klartext: *"Uppgift från NN, förvaltare, samtal 2026-09-xx. Bygger på hens fältbesök hösten 2024 samt skötselplan 2019."*
6. Skicka tillbaka en avstämning på det du fört in — förvaltaren ska känna igen sin egen uppgift

---

## 8. Områdesidentitet — löst, men bara för den publika versionen

Varken `natura-2000: docs/underlag/kartering.csv` eller `natura-2000: docs/underlag/naturtypskarta/NNK_YTA` innehåller något områdes-ID. Det är inget fel i din export — den publika NNK har helt enkelt inte fältet. Kopplingen görs i stället geometriskt.

**Detta är gjort:** `natura-2000: scripts/analysis/koppla_omraden.py` hämtar det rikstäckande SCI-lagret från Naturvårdsregistret, filtrerar till Södermanland (197 områden) och kopplar varje NNK-yta till det Natura 2000-område den har störst arealöverlapp med.

| Resultat | |
|---|---|
| Ytor kopplade till Natura 2000 | 9 609 |
| Ytor utanför Natura 2000 | 5 221 (21 724 ha) — ligger i naturreservat och nationalpark utan N2000-överlapp |
| Områden med träff | 197 av 197 |
| Ytor som skär flera områden | 3 — tilldelade det med störst överlapp |
| Ytor delvis utanför beslutsgränsen | 82 — `andel_inom < 0,95`; karteringen går ibland utanför gränsen, vilket produktbeskrivningen avsnitt 2.2 varnar för |

**Validering:** summan av den klippta arealen inom Natura 2000 blir 44 798 ha, mot 44 852 ha i Naturvårdsverkets statistikuttag per 2026-01-20. Avvikelsen är 0,1 % och beror på att gränserna hämtats vid olika tillfällen. Kopplingen håller.

Utdata: `data/nnk/nnk_yta_med_sitecode.gpkg` och `.csv` med fälten `SITECODE`, `OMRADE`, `BEVPLAN` (direktlänk till bevarandeplanen), `area_ha`, `overlapp_ha`, `andel_inom` och `antal_omraden`.

**Det som återstår:**

| Behov | Hur |
|---|---|
| `NVRID` för de 5 221 ytorna utanför N2000 | Samma metod mot NVR-lagret från Naturvårdsregistret — behövs inför naturreservatsspåret 2027 (arbetspaket G) |
| Koppla `KOMMENTAR`, `NNK_KOMMEN`, `REDIGERARE` samt de nya daterings-/prioritetsfälten till sitecode-nivån | **Löst (konstaterat 2026-10-02).** Granskningslagret (`natura-2000: deliveries/nnk_granskning_sodermanland_20260901/`) bygger på länsuttaget ur NNK Ajourhålla 2026-08-26. `jobbdator_koppla_nnk_skyddskategori.py` ger varje polygon `n2000_sitecode` (minst 1 % av ytan eller 0,25 ha inom området), och `kommentar`, `nnk_kommentar`, `created_user`/`last_edited_user`/`last_edited_date` samt `habitat_priority_*` följer med per polygon. Gjordes i jobbdatorkedjan, inte genom att köra om `koppla_omraden.py` |
| `habitat_period_lastdata_start` / `_end` | Finns i länsuttaget från 2026-08-26, men tomma för nästan alla ytor — fylls i takt med förvaltarsamtalen (avsnitt 6–7) |
| `habitat_priority_all`, `habitat_priority_6210_7130` | Finns i länsuttaget från 2026-08-26 |

Länsuttaget ur Ajourhålla finns sedan 2026-08-26 och spårbarheten på polygonnivå finns nu i granskningslagret. Kvar av tabellen ovan är `NVRID` för ytorna utanför N2000 (naturreservatsspåret) och `habitat_period_lastdata_*`, som fylls i takt med förvaltarsamtalen.

---

## 9. Innan incheckning i NNK

Från handledningen avsnitt 3.3 och checklistan i 2.3:

### Teknisk uppkoppling — NNK i ArcGIS Pro

Handledningens "checka ut" och "kör toolboxen" (3.3) är i praktiken detta (källa: `NNK_i_ArcGIS_Pro_arbetsbeskrivning_v1_5.pdf`, flyttad 2026-08-26 till `natura-2000/docs/underlag/handledning/`):

1. Öppna LST:s interna geoportal-mall **"LST NNK i ArcGIS Pro – Projektmall"** (lst-geoportal.lansstyrelsen.se), hämta `.aptx`-mallen och skapa ett nytt projekt från den.
2. Koppla upp mot servern under Catalog → Servers → "services on nnk.naturvardsverket.se.ags", inloggning med Vic Natur-kontot.
   Produktionsmiljö: `https://nnk.naturvardsverket.se/arcgis/services` · Acceptanstest-/utbildningsmiljö: `https://testnnk.naturvardsverket.se/arcgis/services` (användarnamn med suffix `_utb`).
3. Sök upp området i kartvyn, spara ett bokmärke, och ta ut en **lokalkopia** ("Download Map") — då kopplas Ajourhalla-lagren bort från den centrala servern till en lokal databas på din dator.
4. Kör Toolbox-verktyg 1, **"Skapa arbetsdatabas utifrån lokalkopian"** — det är `NNK_Arbetsdatabas` (med topologiregler) du faktiskt editerar i, inte lokalkopian direkt.
5. Editera, kör topologikontroll (se checklistan nedan), kör sedan verktyg 2 **"Validera attribut"** och verktyg 3 **"Ladda in kartering inför synkronisering"**, och synkronisera tillbaka. En central administratör godkänner uppladdningen innan den syns för andra i Ajourhalla.

Kräver minst en **Standard-licens** i ArcGIS Pro (Basic räcker för att skapa feature-tjänst och ladda ner data, men Toolboxen — inklusive topologiregler — kräver Standard) samt ArcGIS Pro 3.5.

**Genomfört i praktiken:** flödet ovan har körts två gånger — 2026-08-26 för det länsuttag som ligger till grund för avsnitt 2 och 8, och 2026-09-01 för att bygga granskningslagret `LstD NNK Granskning` i avsnitt 3.

**Om ett område helt saknas i NNK** (inte bara behöver rättas) är det nykartering, inte redigering av befintlig yta: mejla underlag till `nnk-kartering@metria.se` så lägger de in området, varefter det går att justera som vanligt.

- [ ] Kör toolboxen i ArcGIS Pro på det utcheckade området — reglerna kontrolleras där
- [ ] Alla obligatoriska attribut ifyllda med godkända värden (undantag: fritextfälten)
- [ ] Inga överlapp mellan ytor; inga glapp; linjer och ytor korsar inte sig själva
- [ ] Topologifel: prioritera överlapp, åtgärda hål > 0,25 ha och remsor > 10 m, strunta i mindre
- [ ] `FORANDRING` satt på allt du ändrat — se R2
- [ ] `KARTERINGS` uppdaterad — se R3
- [ ] Slutdatum för senaste bedömning ifyllt — se avsnitt 6
- [ ] `KOMMENTAR` ifylld med grund och källa — inte tom, aldrig mer tom
- [ ] Systematiska fel i grundkarteringen rapporterade till `NNK-kartering@metria.se`

> **Tidsordning:** avvakta med att registrera *tillstånd* i NNK tills de nya attributen driftsatts (slutet av september 2026, FAQ fråga 30). Fram till dess samlar du in via blankett och granskningslager. Utbredning, livsmiljötyp, karteringsstatus, förändringsorsak och kommentarer kan du registrera direkt.

---

## 10. Vad detta ger till årets leverans

FAQ fråga 9 vill ha svar på fem frågor, och förvaltardialogen bidrar direkt till fyra av dem:

| FAQ-fråga | Vad dialogen ger |
|---|---|
| Vilka insatser krävs och vem gör det | Förvaltarna kan säga vad de själva kan bidra med inom ordinarie förvaltning |
| Er prioritering — var är det viktigast att samla in ny kunskap | De vet vilka marker som är på väg åt fel håll |
| Vilka antaganden och generaliseringar kan göras | *"Alla betesmarker med aktivt jordbruksstöd och pågående hävd antas vara i gott tillstånd"* är den sortens generalisering som bara kan formuleras med förvaltarnas underlag — och som avlastar mest om NV accepterar den |
| Vad gör ni själva, vad behöver ni hjälp med | Skiljelinjen blir konkret när man vet vad som redan är känt |

---

## Om dokumentet

**Hör ihop med:** [arbetsplanen](arbetsplan.html) (arbetspaket H), [webbGIS-publicering](webbgis-publicering.html), [bedömningsguiden](../bedomningsguide.html), `blanketter/blankett_forvaltarkunskap_nnk.xlsx` och `natura-2000: scripts/analysis/koppla_omraden.py`.

### Bygger på

- Handledning för NNK (NV, 2026-07-03, NV-26-002862)
- Lathund granskning WebbGIS-KartLitS (2026-07-10)
- FAQ om uppdraget v1.1 (2026-07-03)
- NNK publik produktbeskrivning
- Manual NNK mall för granskning (KartLitS-mallzippen)
- NNK i ArcGIS Pro, arbetsbeskrivning v1.5

### Versionshistorik

- **2.2** (2026-10-06) — avsnitt 5, R7: nytt avsnitt *Bevarandeplanen som underlag* (när planen stöder typen, åldersgränser för planens tillstånd som för TUVA). Fastställelseåret för alla 197 planer utläst ur PDF:erna (`bevarandeplan_platser.csv`, skriptet `hamta_bevarandeplan_datum.py` i natura-2000).
- **2.1** (2026-10-06) — avsnitt 5, R7: grupperna heter Hävd, Skog, Våtmark och Stabila i stället för A–D (krockade med batcherna); ny delregel *R7-omprövning* för ytor som redan har status.
- **2.0** — avsnitt 5, R7B: död ved är ett klassningskrav för 9010 och 9050 enligt NV:s vägledningar 2026-02-19, så de typerna kan inte bli *fullgod* vid skrivbordet.
- **1.9** — avsnitt 5, R7A: SkötselDOS (utförd bete/slåtter och uppföljning av målindikatorer) som fält i granskningslagret.
- **1.8** — avsnitt 5, R7B och R7C: laserdata (Skogsstyrelsens Skogliga grunddata, två omdrev) och diken som fält i granskningslagret, med tabell för hur de används.
- **1.7** — avsnitt 5, R7A: TUVA som fält i granskningslagret och hur det används tillsammans med skiftena (TUVA äldre än 15 år ger *till fält* om inget annat underlag finns).
- **1.6** — avsnitt 5, R7A: hävd enligt jordbruksskiften som underlag (fältet `havd_skiften` i granskningslagret).
- **1.5** — avsnitt 5: ny regel R7 (utkast) för regelstyrd skrivbordsbedömning av naturtypsstatus.
- **1.4** — avsnitt 4 och 7: nya fält i granskningslagret (`forandringsorsak_forslag` samt de skrivskyddade stödfälten `prio`, `bevarandeplan_ar`, `area_ha`, `naturtyp_kod_text`) och blankettens kolumner Bevarandestatus/År.
- **1.3** — avsnitt 2, 3 och 8 uppdaterade: länsuttaget ur NNK Ajourhålla hämtades 2026-08-26 och granskningslagret för D-län är byggt och publicerat — väntar inte längre på detta.
