# Vortex 🤖 — Din egen Telegram-gruppeassistent

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · **Norsk**

> ⭐ **Hvis du liker Vortex, vennligst stjerne dette prosjektet på GitHub og følg [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — det hjelper flere å finne det. Takk!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Hva er Vortex?

Vortex er en Telegram-bot som bor i gruppene og private chattene dine og svarer folk med en AI-chatmodell. Du sier navnet sitt (standardnavnet er **Vortex**) og den svarer — den kan chatte, søke på nettet, lage bilder, sjekke priser, fortelle vitser, lese filer, transkribere stemmemeldinger, og mer.

Den kjører på din egen server, i ditt eget land og på ditt eget språk. Du er sjefen: et skjult `/admin`-panel lar deg administrere AI-nøkler, brukere og innstillinger.

## Funksjoner

- 💬 **AI-chat** i grupper (vekkeord) og private chater (ingen vekkeord nødvendig)
- 🔑 **Token-pool** — bruk flere LLM-leverandører og nøkler, roter og failover automatisk
- 🖼️ **Bildegenerering og redigering** — gratis (DuckAI) eller betalte leverandører
- 🔍 **Nettssøk** — selvhostet SearXNG, med Wikipedia som reserve
- 💰 **Live priser** — valutaer, gull, olje og krypto i din lokale valuta
- 🕌 **Bønnetider**, 🃏 **spådommer**, 😄 **vitser**, 🎲 **terningkast og myntkast**
- 📎 **Filanalyse** og **stemmetranskripsjon**
- 📥 **Nedlastinger** — send en lenke, få mediefilen tilbake (opp til 45 MB)
- 🌍 **195 land** og **40 språk** — land og språk er separate innstillinger
- 🔄 **Selvoppdatering** — sjekker nye utgaver daglig og spør deg før oppdatering
- 🛡️ **Skjult /admin-panel** — tokens, brukere, statistikk, chater, bilde-modell, manager, power

## Før du installerer

Du trenger en server (eller en datamaskin som står på) som kjører **Linux** med disse installert:

| Hva | Hvordan sjekke | Hva du bør se |
| --- | --- | --- |
| **Python 3.11 eller nyere** | `python3 --version` | `Python 3.11.x` eller høyere (3.12 og 3.13 fungerer også) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` eller `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` eller lignende |
| **Docker** *(valgfri)* | `docker --version` | `Docker version 2x.x.x` — kun nødvendig hvis du vil ha det valgfrie SearXNG-nettssøket |

Hvis noe mangler, installer alt med én kommando (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

For den valgfrie `Docker` (kreves bare hvis du vil ha `SearXNG` web-søk):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Etter den siste linjen, logg ut og inn igjen (eller kjør `docker`-kommandoer med `sudo`). Installatøren tilbyr også å installere manglende verktøy for deg med `apt` på `Debian/Ubuntu`. På andre systemer, installer dem med din pakkebehandler først. `systemd` følger med systemet — det kan ikke installeres separat.

Du trenger også to ting fra Telegram (begge er gratis):

1. **En bot-token** — snakk med [@BotFather](https://t.me/BotFather) på Telegram, send `/newbot`, og kopier tokenen den gir deg.
2. **Din numeriske Telegram-bruker-ID** — snakk med [@userinfobot](https://t.me/userinfobot) og kopier nummeret den viser deg. Dette er din "sjef"-ID: bare denne kontoen kan bruke `/admin`.

## Installer

Én kommando. Kopier den, lim den inn i terminalen din, og trykk Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Installasjonsprogrammet stiller deg seks spørsmål, i rekkefølge:

1. **Land** — lim inn det engelske navnet på landet ditt **nøyaktig som oppført i [land-tabellen](#countries) nedenfor** (for eksempel `Turkey`). Landet bestemmer tidssone, lokal valuta for priser, bønnetider og lokalt innhold.
2. **Språk** — språket botten snakker (for eksempel `en`, `fa`, `tr`). Trykk Enter for å godta standarden for ditt land. Språk er adskilt fra land: det endrer bare hva botten sier, og du kan endre det senere fra `/admin`.
3. **Bot-token** — lim inn tokenen fra [@BotFather](https://t.me/BotFather). Installatøren sjekker den live mot Telegram.
4. **Sjef numerisk ID** — din Telegram-bruker-ID fra [@userinfobot](https://t.me/userinfobot).
5. **Bot-navn / vekkord** — navnet folk sier i grupper for å snakke med botten. Et hvilket som helst språk er greit (for eksempel `Vortex` eller `ورتکس`). Trykk Enter for standarden `Vortex`.
6. **Første LLM-utbyder** — velg en: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, eller **Custom** (lim inn en base URL). Deretter limer du inn API-nøkkelen for den utbyderen — installatøren henter utbyderens live modelliste og du velger en modell.

Deretter installerer installatøren avhengigheter, skriver `.env`-filen, oppretter `vortex-bot` systemd-tjenesten, tilbyr å installere SearXNG for nettssøk (trenger Docker), og starter botten.

> ⚠️ **Anthropic fungerer ikke direkte.** Anthropics native API er ikke OpenAI-kompatibel, og denne botten snakker kun OpenAI-kompatible API-er. Hvis du velger Anthropic, advarer installatøren deg: nøkkelen fungerer kun gjennom en OpenAI-kompatibel gateway. Bruk OpenRouter, eller en annen utbyder fra listen, i stedet.

## Etter installasjon

Sjekk at botten kjører:

```bash
systemctl status vortex-bot
```

Du bør se `active (running)`. For å følge loggen live:

```bash
journalctl -u vortex-bot -f
```

Åpne nå Telegram og snakk med botten din:

- Send `/start` — botten sier hei.
- I en **privat chat**, skriv bare til den — ingen vekkord trengs.
- I en **gruppe**, legg til botten i gruppen, slå deretter av gruppepersonvern: i [@BotFather](https://t.me/BotFather) send `/setprivacy`, velg botten din, og velg **Disable** — ellers kan botten ikke se gruppmeldinger og vil ikke høre sitt vekkeord. Si deretter navnet sitt, for eksempel: `Vortex what's the time?`
- Som sjef, send `/admin` i en privat chat for å åpne det skjulte admin-panelet.

**Oppdateringer er automatiske.** En gang i døgnet sjekker botten GitHub etter et nytt release. Hvis ett er tilgjengelig, sender den deg en privat melding med ✅ / ❌-knapper. Trykk ✅ og den oppdaterer seg selv og starter på nytt — du trenger aldri å røre serveren.

## Konfigurasjon

Alle innstillinger ligger i `.env`-filen i installasjonsmappen. Se [`.env.example`](.env.example) for hvert alternativ. De viktigste:

| Innstilling | Hva den gjør |
| --- | --- |
| `BOT_TOKEN` | Din Telegram-bot-token (fra @BotFather) |
| `BOSS_ID` | Din numeriske Telegram-bruker-ID (bot-eieren) |
| `BOT_NAME` | Bots navn og vekkord i grupper (standard `Vortex`) |
| `BOT_COUNTRY` | Land på engelsk, f.eks. `United States` (setter tidssone, valuta, bønnetider) |
| `BOT_LANGUAGE` | Bot-språkkode, f.eks. `en`, `fa`, `tr` (endrer bare hva boten sier) |
| `LLM_PROVIDERS` | LLM-leverandører og nøkler: `base_url\|api_key\|model`, komma-separert |
| `UPDATE_CHECK_ENABLED` | `1` = sjekk oppdateringer daglig, `0` = aldri sjekk |
| `UPDATE_REPO` | Repoet hvis utgivelser overvåkes (standard `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Webbsøk: `searxng` (standard), `tavily`, eller `serper` |
| `DAILY_LIMIT_MESSAGES` | Maks bot-svar per bruker per dag (standard `30`, boss er unntatt) |

Land og språk kan også endres senere fra det skjulte `/admin`-panelet (Språk & Land), uten å redigere noen fil.

## Docker-alternativ

Hvis du foretrekker Docker fremfor installasjonsprogrammet:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Dette starter boten sammen med en selvhostet SearXNG-søkemotor. Sjekk loggene med `docker compose logs -f bot`.

Merk: den automatiske selv-oppdatereren trenger systemd-tjenesten, så i Docker er oppdateringer manuelle: `git pull` og deretter `docker compose up -d --build` igjen.

## Funksjoner i detalj

### /admin-panelet

Send `/admin` i en privat chat (kun boss — ingen andre kan åpne det, og det dukker aldri opp i `/help` eller menyene). Det har:

- 🔑 **Tokens & modell** — legg til eller fjern LLM-nøkler, se hvilke nøkler som er friske, velg aktiv modell, bla gjennom en leverandørs live modelliste
- 👥 **Brukere** — brukerantall, ban / unban, tillatelsesliste
- 📊 **Statistikk** — bruksnummer
- 💬 **Nylige chat** — hva folk sa til boten (kun boss, privat)
- 🖼️ **Bildemodell** — DuckAI (gratis, standard), HiLinkUp, en egendefinert biljetjeneste, eller av
- 🛡️ **Administratorer** — gi tillitspersoner tilgang til deler av panelet
- 🟢/🔴 **Strøm** — slå boten på eller av for alle (boss beholder kontrollen)
- 🌍 **Språk & Land** — endre botens språk eller land når som helst

### Token-pulen

Boten kan holde nøkler fra flere LLM-leverandører samtidig. Den roterer mellom friske nøkler og failoverer automatisk når en slutter å fungere. Fra `/admin` kan du feste en modell, velge en modell manuelt, eller la boten rotere fritt. Enhver leverandør med en OpenAI-kompatibel API fungerer — inkludert små aggregatorer, ikke bare de store navnene.

### Bilder

Bildegenerering har tre moduser: **DuckAI** (gratis, ingen nøkkel, standard), **HiLinkUp** (betalt, bedre kvalitet), eller en **egendefinert** OpenAI-kompatibel biljetjeneste. Du kan også sende boten et bilde og si hvordan den skal redigere det ("gjøre dette til tegneseristil"), og den vil generere et nytt bilde. Bildegenerering kan slås av fra `/admin`.

### Land og språk

Vortex støtter **195 land** og **40 språk**. Landet bestemmer tidssone, valuta priser vises i, byen som brukes for bønnetider, og lokalt innhold. Språket bestemmer bare hva boten sier — en gruppe i Belgia kan bruke landet Belgia og språket Engelsk, for eksempel. Begge kan endres senere fra `/admin`.

### Oppdateringer

Boten sjekker GitHub-utgivelser av `VortexLabsHQ/vortex-telegram-bot` en gang i dagen. Når en ny versjon er ute, sender den en privat melding til sjefen med ✅ / ❌-knapper. Godkjenning oppdaterer koden og starter boten på nytt. Mens repoet er privat, gjør sjekken ingenting stille (GitHubs API krever et offentlig repo) — sett `UPDATE_CHECK_ENABLED=0` hvis du aldri vil ha sjekken.

## Feilsøking / FAQ

**Installasjonsprogrammet sier at tokenen min er ugyldig.**
Tokenen kommer fra [@BotFather](https://t.me/BotFather). Sørg for at du kopierte hele tokenen (sifre, et kolon, så 35+ tegn), uten ekstra mellomrom. Hvis du slettet boten eller laget en ny token, slutter den gamle å fungere — lim inn den nye.

**Boten svarer ikke i gruppen min.**
Fire ting å sjekke: (1) Gruppepersonvern må være slått av — i [@BotFather](https://t.me/BotFather) send `/setprivacy`, velg botten din, og velg **Disable**; med personvern på, kan botten ikke se gruppmeldinger i det hele tatt, (2) botten må legges til i gruppen, (3) du må si vekkeordet sitt — navnet sitt, for eksempel `Vortex what's the time?` — botten lytter bare når navnet nevnes i grupper, (4) i en privat chat trengs ingen vekkeord i det hele tatt.

**Boten svarer på engelsk, ikke mitt språk.**
Send `/admin` (bare sjef) → Språk & Land, og velg ditt språk. Installasjonsprogrammet spør også om språket — trykk Enter der for å godta landets standard.

**Jeg valgte Anthropic og boten chatter ikke.**
Anthropics native API er ikke OpenAI-kompatibel, så boten kan ikke chatte med den direkte. Bruk OpenRouter (som kan tjene Claude-modeller gjennom et OpenAI-kompatibelt API), eller velg en annen leverandør fra listen.

**Webbsøk fungerer ikke.**
Webbsøk trenger SearXNG, som installasjonsprogrammet tilbyr å sette opp med Docker. Uten det, faller boten tilbake til Wikipedia, som er svakere. Du kan også sette `SEARCH_PROVIDER=tavily` eller `serper` med en `SEARCH_API_KEY` i `.env`.

**Hvor er loggene?**
`journalctl -u vortex-bot -f` viser live-logen. `systemctl status vortex-bot` viser om tjenesten kjører. Hvis boten stopper, starter `sudo systemctl restart vortex-bot` den på nytt.

**Boten sier at jeg har nådd daglig grensen.**
Hver bruker får 30 bot-svar per dag (sjefen er unntatt). Grensen nullstilles midnatt i botens lands tidssone. Øk den med `DAILY_LIMIT_MESSAGES` i `.env`, eller spør sjefen.

**Jeg fant en feil / Jeg har et forslag.**
Vennligst opprett en issue på GitHub — se [CONTRIBUTING.md](CONTRIBUTING.md) for hvordan du rapporterer det og hvordan du sender en fix.

## Utvikling

```bash
git clone https://github.com/VortexLabsHQ/vortex-telegram-bot.git
cd vortex-telegram-bot

python3.11 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install ruff

cp .env.example .env   # then fill in your own BOT_TOKEN and LLM key(s)
python -m bot.main
```

Kjør testene (vanlige Python-skript, ingen pytest nødvendig):

```bash
python tests/test_admin.py
python tests/test_admin_keys.py
python tests/test_admin_select.py
python tests/test_admin_power.py
python tests/test_admin_image.py
python tests/test_fixes.py
python tests/test_installer.py
python tests/test_locale.py
python tests/test_updater.py
```

Alle ni testserier må bestås før du åpner en pull request. Se [CONTRIBUTING.md](CONTRIBUTING.md) for kodestil (ruff) og PR-prosessen.

## Lisens

Vortex utgis under [MIT-lisensen](LICENSE) — fri å bruke, kopiere, endre og dele, for ethvert formål.

<a id="countries"></a>

## Land

Lim inn landnavnet **på engelsk, nøyaktig som skrevet her** når installasjonsprogrammet spør om ditt land. Tabellen er generert fra `bot/countries.py` — hvis et navn her og et navn der ikke stemmer overens, gjelder `bot/countries.py`.

<!-- COUNTRY_TABLE_START -->

| Country | Time zone | Currency | Capital |
| --- | --- | --- | --- |
| Iran | Asia/Tehran | IRR | Tehran |
| Turkey | Europe/Istanbul | TRY | Ankara |
| United States | America/New_York | USD | Washington |
| United Kingdom | Europe/London | GBP | London |
| Germany | Europe/Berlin | EUR | Berlin |
| France | Europe/Paris | EUR | Paris |
| Spain | Europe/Madrid | EUR | Madrid |
| Italy | Europe/Rome | EUR | Rome |
| Netherlands | Europe/Amsterdam | EUR | Amsterdam |
| Belgium | Europe/Brussels | EUR | Brussels |
| Russia | Europe/Moscow | RUB | Moscow |
| Ukraine | Europe/Kyiv | UAH | Kyiv |
| Poland | Europe/Warsaw | PLN | Warsaw |
| Sweden | Europe/Stockholm | SEK | Stockholm |
| Brazil | America/Sao_Paulo | BRL | Brasília |
| Mexico | America/Mexico_City | MXN | Mexico City |
| Argentina | America/Argentina/Buenos_Aires | ARS | Buenos Aires |
| Saudi Arabia | Asia/Riyadh | SAR | Riyadh |
| United Arab Emirates | Asia/Dubai | AED | Abu Dhabi |
| Egypt | Africa/Cairo | EGP | Cairo |
| Morocco | Africa/Casablanca | MAD | Rabat |
| India | Asia/Kolkata | INR | New Delhi |
| Pakistan | Asia/Karachi | PKR | Islamabad |
| China | Asia/Shanghai | CNY | Beijing |
| Japan | Asia/Tokyo | JPY | Tokyo |
| South Korea | Asia/Seoul | KRW | Seoul |
| Indonesia | Asia/Jakarta | IDR | Jakarta |
| Thailand | Asia/Bangkok | THB | Bangkok |
| Vietnam | Asia/Ho_Chi_Minh | VND | Hanoi |
| Australia | Australia/Sydney | AUD | Canberra |
| Nigeria | Africa/Lagos | NGN | Abuja |
| Kenya | Africa/Nairobi | KES | Nairobi |
| Afghanistan | Asia/Kabul | AFN | Kabul |
| Albania | Europe/Tirane | ALL | Tirana |
| Algeria | Africa/Algiers | DZD | Algiers |
| Andorra | Europe/Andorra | EUR | Andorra la Vella |
| Angola | Africa/Luanda | AOA | Luanda |
| Antigua & Barbuda | America/Antigua | XCD | St. John's |
| Armenia | Asia/Yerevan | AMD | Yerevan |
| Austria | Europe/Vienna | EUR | Vienna |
| Azerbaijan | Asia/Baku | AZN | Baku |
| Bahamas | America/Nassau | BSD | Nassau |
| Bahrain | Asia/Bahrain | BHD | Manama |
| Bangladesh | Asia/Dhaka | BDT | Dhaka |
| Barbados | America/Barbados | BBD | Bridgetown |
| Belarus | Europe/Minsk | BYN | Minsk |
| Belize | America/Belize | BZD | Belmopan |
| Benin | Africa/Porto-Novo | XOF | Porto-Novo |
| Bhutan | Asia/Thimphu | BTN | Thimphu |
| Bolivia | America/La_Paz | BOB | Sucre |
| Bosnia & Herzegovina | Europe/Sarajevo | BAM | Sarajevo |
| Botswana | Africa/Gaborone | BWP | Gaborone |
| Brunei | Asia/Brunei | BND | Bandar Seri Begawan |
| Bulgaria | Europe/Sofia | EUR | Sofia |
| Burkina Faso | Africa/Ouagadougou | XOF | Ouagadougou |
| Burundi | Africa/Bujumbura | BIF | Gitega |
| Cambodia | Asia/Phnom_Penh | KHR | Phnom Penh |
| Cameroon | Africa/Douala | XAF | Yaounde |
| Canada | America/Toronto | CAD | Ottawa |
| Cape Verde | Atlantic/Cape_Verde | CVE | Praia |
| Central African Republic | Africa/Bangui | XAF | Bangui |
| Chad | Africa/Ndjamena | XAF | N'Djamena |
| Chile | America/Santiago | CLP | Santiago |
| Colombia | America/Bogota | COP | Bogota |
| Comoros | Indian/Comoro | KMF | Moroni |
| Congo - Brazzaville | Africa/Brazzaville | XAF | Brazzaville |
| Congo - Kinshasa | Africa/Kinshasa | CDF | Kinshasa |
| Costa Rica | America/Costa_Rica | CRC | San Jose |
| Croatia | Europe/Zagreb | EUR | Zagreb |
| Cuba | America/Havana | CUP | Havana |
| Cyprus | Asia/Nicosia | EUR | Nicosia |
| Czechia | Europe/Prague | CZK | Prague |
| Côte d’Ivoire | Africa/Abidjan | XOF | Yamoussoukro |
| Denmark | Europe/Copenhagen | DKK | Copenhagen |
| Djibouti | Africa/Djibouti | DJF | Djibouti |
| Dominica | America/Dominica | XCD | Roseau |
| Dominican Republic | America/Santo_Domingo | DOP | Santo Domingo |
| Ecuador | America/Guayaquil | USD | Quito |
| El Salvador | America/El_Salvador | USD | San Salvador |
| Equatorial Guinea | Africa/Malabo | XAF | Ciudad de la Paz |
| Eritrea | Africa/Asmara | ERN | Asmara |
| Estonia | Europe/Tallinn | EUR | Tallinn |
| Eswatini | Africa/Mbabane | SZL | Mbabane |
| Ethiopia | Africa/Addis_Ababa | ETB | Addis Ababa |
| Fiji | Pacific/Fiji | FJD | Suva |
| Finland | Europe/Helsinki | EUR | Helsinki |
| Gabon | Africa/Libreville | XAF | Libreville |
| Gambia | Africa/Banjul | GMD | Banjul |
| Georgia | Asia/Tbilisi | GEL | Tbilisi |
| Ghana | Africa/Accra | GHS | Accra |
| Greece | Europe/Athens | EUR | Athens |
| Grenada | America/Grenada | XCD | St. George's |
| Guatemala | America/Guatemala | GTQ | Guatemala City |
| Guinea | Africa/Conakry | GNF | Conakry |
| Guinea-Bissau | Africa/Bissau | XOF | Bissau |
| Guyana | America/Guyana | GYD | Georgetown |
| Haiti | America/Port-au-Prince | HTG | Port-au-Prince |
| Honduras | America/Tegucigalpa | HNL | Tegucigalpa |
| Hungary | Europe/Budapest | HUF | Budapest |
| Iceland | Atlantic/Reykjavik | ISK | Reykjavik |
| Iraq | Asia/Baghdad | IQD | Baghdad |
| Ireland | Europe/Dublin | EUR | Dublin |
| Israel | Asia/Jerusalem | ILS | Jerusalem |
| Jamaica | America/Jamaica | JMD | Kingston |
| Jordan | Asia/Amman | JOD | Amman |
| Kazakhstan | Asia/Almaty | KZT | Astana |
| Kiribati | Pacific/Tarawa | AUD | Tarawa |
| Kuwait | Asia/Kuwait | KWD | Kuwait City |
| Kyrgyzstan | Asia/Bishkek | KGS | Bishkek |
| Laos | Asia/Vientiane | LAK | Vientiane |
| Latvia | Europe/Riga | EUR | Riga |
| Lebanon | Asia/Beirut | LBP | Beirut |
| Lesotho | Africa/Maseru | LSL | Maseru |
| Liberia | Africa/Monrovia | LRD | Monrovia |
| Libya | Africa/Tripoli | LYD | Tripoli |
| Liechtenstein | Europe/Vaduz | CHF | Vaduz |
| Lithuania | Europe/Vilnius | EUR | Vilnius |
| Luxembourg | Europe/Luxembourg | EUR | Luxembourg |
| Madagascar | Indian/Antananarivo | MGA | Antananarivo |
| Malawi | Africa/Blantyre | MWK | Lilongwe |
| Malaysia | Asia/Kuala_Lumpur | MYR | Kuala Lumpur |
| Maldives | Indian/Maldives | MVR | Male |
| Mali | Africa/Bamako | XOF | Bamako |
| Malta | Europe/Malta | EUR | Valletta |
| Marshall Islands | Pacific/Majuro | USD | Majuro |
| Mauritania | Africa/Nouakchott | MRU | Nouakchott |
| Mauritius | Indian/Mauritius | MUR | Port Louis |
| Micronesia | Pacific/Pohnpei | USD | Palikir |
| Moldova | Europe/Chisinau | MDL | Chisinau |
| Monaco | Europe/Monaco | EUR | Monaco |
| Mongolia | Asia/Ulaanbaatar | MNT | Ulaanbaatar |
| Montenegro | Europe/Podgorica | EUR | Podgorica |
| Mozambique | Africa/Maputo | MZN | Maputo |
| Myanmar | Asia/Yangon | MMK | Nay Pyi Taw |
| Namibia | Africa/Windhoek | NAD | Windhoek |
| Nauru | Pacific/Nauru | AUD | Yaren |
| Nepal | Asia/Kathmandu | NPR | Kathmandu |
| New Zealand | Pacific/Auckland | NZD | Wellington |
| Nicaragua | America/Managua | NIO | Managua |
| Niger | Africa/Niamey | XOF | Niamey |
| North Korea | Asia/Pyongyang | KPW | Pyongyang |
| North Macedonia | Europe/Skopje | MKD | Skopje |
| Norway | Europe/Oslo | NOK | Oslo |
| Oman | Asia/Muscat | OMR | Muscat |
| Palau | Pacific/Palau | USD | Melekeok |
| Palestine | Asia/Hebron | ILS | Ramallah |
| Panama | America/Panama | USD | Panama City |
| Papua New Guinea | Pacific/Port_Moresby | PGK | Port Moresby |
| Paraguay | America/Asuncion | PYG | Asuncion |
| Peru | America/Lima | PEN | Lima |
| Philippines | Asia/Manila | PHP | Manila |
| Portugal | Europe/Lisbon | EUR | Lisbon |
| Qatar | Asia/Qatar | QAR | Doha |
| Romania | Europe/Bucharest | RON | Bucharest |
| Rwanda | Africa/Kigali | RWF | Kigali |
| Samoa | Pacific/Apia | WST | Apia |
| San Marino | Europe/San_Marino | EUR | San Marino |
| Senegal | Africa/Dakar | XOF | Dakar |
| Serbia | Europe/Belgrade | RSD | Belgrade |
| Seychelles | Indian/Mahe | SCR | Victoria |
| Sierra Leone | Africa/Freetown | SLE | Freetown |
| Singapore | Asia/Singapore | SGD | Singapore |
| Slovakia | Europe/Bratislava | EUR | Bratislava |
| Slovenia | Europe/Ljubljana | EUR | Ljubljana |
| Solomon Islands | Pacific/Guadalcanal | SBD | Honiara |
| Somalia | Africa/Mogadishu | SOS | Mogadishu |
| South Africa | Africa/Johannesburg | ZAR | Pretoria |
| South Sudan | Africa/Juba | SSP | Juba |
| Sri Lanka | Asia/Colombo | LKR | Colombo |
| St. Kitts & Nevis | America/St_Kitts | XCD | Basseterre |
| St. Lucia | America/St_Lucia | XCD | Castries |
| St. Vincent & Grenadines | America/St_Vincent | XCD | Kingstown |
| Sudan | Africa/Khartoum | SDG | Khartoum |
| Suriname | America/Paramaribo | SRD | Paramaribo |
| Switzerland | Europe/Zurich | CHF | Bern |
| Syria | Asia/Damascus | SYP | Damascus |
| São Tomé & Príncipe | Africa/Sao_Tome | STN | Sao Tome |
| Tajikistan | Asia/Dushanbe | TJS | Dushanbe |
| Tanzania | Africa/Dar_es_Salaam | TZS | Dodoma |
| Timor-Leste | Asia/Dili | USD | Dili |
| Togo | Africa/Lome | XOF | Lome |
| Tonga | Pacific/Tongatapu | TOP | Nuku'alofa |
| Trinidad & Tobago | America/Port_of_Spain | TTD | Port of Spain |
| Tunisia | Africa/Tunis | TND | Tunis |
| Turkmenistan | Asia/Ashgabat | TMT | Ashgabat |
| Tuvalu | Pacific/Funafuti | AUD | Funafuti |
| Uganda | Africa/Kampala | UGX | Kampala |
| Uruguay | America/Montevideo | UYU | Montevideo |
| Uzbekistan | Asia/Tashkent | UZS | Tashkent |
| Vanuatu | Pacific/Efate | VUV | Port Vila |
| Vatican City | Europe/Vatican | EUR | Vatican City |
| Venezuela | America/Caracas | VES | Caracas |
| Yemen | Asia/Aden | YER | Sanaa |
| Zambia | Africa/Lusaka | ZMW | Lusaka |
| Zimbabwe | Africa/Harare | ZWG | Harare |

<!-- COUNTRY_TABLE_END -->

## Takk

> ⭐ **Vennligst stjern dette prosjektet på GitHub og følg [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — det er den enkleste måten å støtte Vortex på og hjelpe andre med å finne det. Takk!
