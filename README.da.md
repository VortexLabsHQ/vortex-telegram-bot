# Vortex 🤖 — Din egen Telegram-gruppeassistent

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · **Dansk** · [Norsk](README.no.md)

> ⭐ **Hvis du kan lide Vortex, så giv dette projekt en stjerne på GitHub og følg [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — det hjælper flere med at finde det. Tak!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Hvad er Vortex?

Vortex er en Telegram-bot, der bor i dine grupper og private chats og svarer folk med en AI-chatmodel. Du siger dets navn (standardnavnet er **Vortex**) og den svarer — den kan chatte, søge på nettet, lave billeder, tjekke priser, fortælle jokes, læse filer, transskribere stemmebeskeder, og meget mere.

Den kører på din egen server, i dit eget land og sprog. Du er chef: et skjult `/admin`-panel lader dig styre AI-nøgler, brugere og indstillinger.

## Funktioner

- 💬 **AI-chat** i grupper (vågeord) og private chats (intet vågeord nødvendigt)
- 🔑 **Token-pool** — brug flere LLM-udbydere og nøgler, roter og failover automatisk
- 🖼️ **Billedgenerering og redigering** — gratis (DuckAI) eller betalte udbydere
- 🔍 **Websøgning** — self-hosted SearXNG, med Wikipedia som fallback
- 💰 **Live-priser** — valutaer, guld, olie og krypto i din lokale valuta
- 🕌 **Bønnetider**, 🃏 **spådomme**, 😄 **jokes**, 🎲 **terninger og myntkast**
- 📎 **Filanalyse** og **stemmetranskription**
- 📥 **Downloads** — send et link, få mediefilen retur (op til 45 MB)
- 🌍 **195 lande** og **40 sprog** — land og sprog er separate indstillinger
- 🔄 **Selv-opdatering** — tjekker efter nye udgivelser dagligt og spørger dig før opdatering
- 🛡️ **Skjult /admin-panel** — tokens, brugere, statistik, chats, billede-model, manager, power

## Før du installerer

Du har brug for en server (eller en computer, der forbliver tændt) der kører **Linux** med disse installeret:

| Hvad | Sådan tjekker du | Hvad du bør se |
| --- | --- | --- |
| **Python 3.11 eller nyere** | `python3 --version` | `Python 3.11.x` eller højere (3.12 og 3.13 virker også) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` eller `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` eller lignende |
| **Docker** *(valgfri)* | `docker --version` | `Docker version 2x.x.x` — kun nødvendig hvis du vil have den valgfrie SearXNG-websøgning |

Hvis noget mangler, tilbyder installeren at installere det for dig med `apt` (på Debian/Ubuntu). På andre systemer, installer det med din pakkehåndterer først.

Du har også brug for to ting fra Telegram (begge er gratis):

1. **En bot-token** — tal med [@BotFather](https://t.me/BotFather) på Telegram, send `/newbot`, og kopier tokenen den giver dig.
2. **Dit numeriske Telegram-bruger-ID** — tal med [@userinfobot](https://t.me/userinfobot) og kopier det nummer, den viser dig. Det er din "chef"-ID: kun denne konto kan bruge `/admin`.

## Installation

Én kommando. Kopiér den, indsæt den i din terminal, og tryk Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Installeren spørger dig om seks spørgsmål, i rækkefølge:

1. **Land** — indsæt det engelske navn på dit land **præcis som angivet i [land-tabellen](#countries) nedenfor** (f.eks. `Turkey`). Landet bestemmer tidszone, lokal valuta til priser, bønnetider og lokalt indhold.
2. **Sprog** — det sprog, botten taler (f.eks. `en`, `fa`, `tr`). Tryk Enter for at acceptere standarden for dit land. Sprog er adskilt fra land: det ændrer kun, hvad botten siger, og du kan ændre det senere fra `/admin`.
3. **Bot-token** — indsæt token fra [@BotFather](https://t.me/BotFather). Installationsprogrammet tjekker det live med Telegram.
4. **Boss numerisk ID** — dit Telegram bruger-ID fra [@userinfobot](https://t.me/userinfobot).
5. **Bot-navn / vækkeord** — navnet, folk siger i grupper for at tale med botten. Ethvert sprog er fint (f.eks. `Vortex` eller `ورتکس`). Tryk Enter for standarden `Vortex`.
6. **Første LLM-udbyder** — vælg en: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, eller **Custom** (indsæt en base URL). Indsæt derefter din API-nøgle til den udbyder — installationsprogrammet henter udbyders live modelliste, og du vælger en model.

Derefter installerer installationsprogrammet afhængighederne, skriver `.env`-filen, opretter `vortex-bot` systemd-tjenesten, tilbyder at installere SearXNG til web-søgning (kræver Docker), og starter botten.

> ⚠️ **Anthropic virker ikke direkte.** Anthropics native API er ikke OpenAI-kompatibel, og denne bot taler kun OpenAI-kompatible API'er. Hvis du vælger Anthropic, advarer installationsprogrammet dig: nøglen virker kun gennem en OpenAI-kompatibel gateway. Brug OpenRouter, eller en anden udbyder fra listen, i stedet.

## Efter installationen

Tjek, at botten kører:

```bash
systemctl status vortex-bot
```

Du bør se `active (running)`. For at følge loggen live:

```bash
journalctl -u vortex-bot -f
```

Åbn nu Telegram og tal med din bot:

- Send `/start` — botten siger hej.
- I en **privat chat**, skriv bare til den — intet vækkeord nødvendigt.
- I en **gruppe**, tilføj botten til gruppen, og sig så dets navn, f.eks.: `Vortex what's the time?`
- Som boss, send `/admin` i en privat chat for at åbne det skjulte admin-panel.

**Opdateringer er automatiske.** En gang om dagen tjekker botten GitHub efter et nyt release. Hvis der er et tilgængeligt, sender den dig en privat besked med ✅ / ❌ knapper. Tryk ✅, og den opdaterer sig selv og genstarter — du behøver aldrig at røre serveren.

## Konfiguration

Alle indstillinger ligger i `.env`-filen i installationsmappen. Se [`.env.example`](.env.example) for hver mulighed. De vigtigste:

| Indstilling | Hvad det gør |
| --- | --- |
| `BOT_TOKEN` | Din Telegram bot-token (fra @BotFather) |
| `BOSS_ID` | Dit numeriske Telegram bruger-ID (bot-ejeren) |
| `BOT_NAME` | Bottets navn og vækkeord i grupper (standard `Vortex`) |
| `BOT_COUNTRY` | Land på engelsk, f.eks. `United States` (indstiller tidszone, valuta, bønnetider) |
| `BOT_LANGUAGE` | Bot-sprogkode, f.eks. `en`, `fa`, `tr` (ændrer kun hvad botten siger) |
| `LLM_PROVIDERS` | LLM-udbydere og nøgler: `base_url\|api_key\|model`, komma-separeret |
| `UPDATE_CHECK_ENABLED` | `1` = tjek opdateringer dagligt, `0` = tjek aldrig |
| `UPDATE_REPO` | Det repo, hvis releases overvåges (standard `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Websøgning: `searxng` (standard), `tavily`, eller `serper` |
| `DAILY_LIMIT_MESSAGES` | Maks bot-svar per bruger per dag (standard `30`, boss er undtaget) |

Land og sprog kan også ændres senere fra det skjulte `/admin`-panel (Sprog & Land), uden at redigere nogen fil.

## Docker-alternativ

Hvis du foretrækker Docker frem for installationsprogrammet:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Dette starter botten sammen med en selvhostet SearXNG-søgemaskine. Tjek loggene med `docker compose logs -f bot`.

Bemærk: den automatiske selv-opdaterer har brug for systemd-tjenesten, så i Docker er opdateringer manuelle: `git pull` og derefter `docker compose up -d --build` igen.

## Funktioner i detaljer

### `/admin`-panelet

Send `/admin` i en privat chat (kun boss — ingen andre kan åbne det, og det vises aldrig i `/help` eller menuerne). Det har:

- 🔑 **Tokens & model** — tilføj eller fjern LLM-nøgler, se hvilke nøgler der er sunde, vælg den aktive model, gennemse en udbyder's live modelliste
- 👥 **Users** — brugerantal, ban / unban, allowlist
- 📊 **Stats** — brugsnumre
- 💬 **Recent chats** — hvad folk sagde til botten (kun boss, privat)
- 🖼️ **Image model** — DuckAI (gratis, standard), HiLinkUp, en brugerdefineret billedtjeneste, eller fra
- 🛡️ **Managers** — giv tillidspersoner adgang til dele af panelet
- 🟢/🔴 **Power** — slå botten til eller fra for alle (bossen forbliver i kontrol)
- 🌍 **Language & Country** — ændr botten's sprog eller land når som helst

### Token-puljen

Botten kan holde nøgler fra flere LLM-udbydere på én gang. Den roterer mellem sunde nøgler og failover automatisk, når en slutter med at virke. Fra `/admin` kan du pinde en model, vælge en model manuelt, eller lade botten rotere frit. Enhver udbydere med en OpenAI-kompatibel API virker — inklusive små aggregatorer, ikke kun de store navne.

### Billeder

Billedgenerering har tre tilstande: **DuckAI** (gratis, ingen nøgle, standard), **HiLinkUp** (betalt, bedre kvalitet), eller en **brugerdefineret** OpenAI-kompatibel billedtjeneste af din egen. Du kan også sende botten et billede og fortælle den, hvordan den skal redigere det ("gør dette til tegneseriestil"), og den vil generere et nyt billede. Billedgenerering kan slås fra fra `/admin`.

### Lande og sprog

Vortex understøtter **195 lande** og **40 sprog**. Landet indstiller tidszonen, den valuta priser vises i, den by der bruges til bønnetider, og lokalt indhold. Sproget indstiller kun, hvad botten siger — en gruppe i Belgien kan bruge landet Belgien og sproget Engelsk, for eksempel. Begge kan ændres senere fra `/admin`.

### Opdateringer

Botten tjekker GitHub-udgivelser af `VortexLabsHQ/vortex-telegram-bot` én gang om dagen. Når en ny version er ude, sender den en privat besked til chefen med ✅ / ❌-knapper. At acceptere opdaterer koden og genstarter botten. Mens repoet er privat, gør tjekket stille intet (GitHubs API kræver et offentligt repo) — sæt `UPDATE_CHECK_ENABLED=0` hvis du aldrig vil have tjekket.

## Fejlfinding / FAQ

**Installationsprogrammet siger, at min token er ugyldig.**
Token kommer fra [@BotFather](https://t.me/BotFather). Sørg for at du kopierede hele token (cifre, et kolon, så 35+ tegn), uden ekstra mellemrum. Hvis du slettede botten eller lavede en ny token, slutter den gamle med at virke — indsæt den nye.

**Botten svarer ikke i min gruppe.**
Tre ting at tjekke: (1) botten skal være tilføjet til gruppen, (2) du skal sige dets vækkeord — dets navn, for eksempel `Vortex what's the time?` — botten lytter kun, når dets navn nævnes i grupper, (3) i en privat chat er intet vækkeord nødvendigt overhovedet.

**Botten svarer på engelsk, ikke mit sprog.**
Send `/admin` (kun chef) → Sprog & Land, og vælg dit sprog. Installationsprogrammet spørger også om sproget — tryk Enter der for at acceptere dit lands standard.

**Jeg valgte Anthropic, og botten chatter ikke.**
Anthropics native API er ikke OpenAI-kompatibel, så botten kan ikke chatte med det direkte. Brug OpenRouter (som kan servere Claude-modeller gennem en OpenAI-kompatibel API), eller vælg en anden udbyder fra listen.

**Websøgning virker ikke.**
Websøgning kræver SearXNG, som installationsprogrammet tilbyder at opsætte med Docker. Uden det falder botten tilbage til Wikipedia, som er svagere. Du kan også sætte `SEARCH_PROVIDER=tavily` eller `serper` med en `SEARCH_API_KEY` i `.env`.

**Hvor er loggene?**
`journalctl -u vortex-bot -f` viser live-loggen. `systemctl status vortex-bot` viser om tjenesten kører. Hvis botten stopper, `sudo systemctl restart vortex-bot` starter den igen.

**Botten siger, at jeg har nået den daglige grænse.**
Hver bruger får 30 bot-svar om dagen (chef er undtaget). Grænsen nulstilles kl. midnat i botten lands tidszone. Øg den med `DAILY_LIMIT_MESSAGES` i `.env`, eller spørg chefen.

**Jeg fandt en fejl / Jeg har et forslag.**
Åbn venligst et issue på GitHub — se [CONTRIBUTING.md](CONTRIBUTING.md) for hvordan du rapporterer det og hvordan du sender en rettelse.

## Udvikling

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

Kør testene (rene Python-scripts, ingen pytest nødvendig):

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

Alle ni suites skal bestå, før du åbner et pull request. Se [CONTRIBUTING.md](CONTRIBUTING.md) for kodestil (ruff) og PR-processen.

## Licens

Vortex udgives under [MIT-licensen](LICENSE) — fri til at bruge, kopiere, ændre og dele, til ethvert formål.

<a id="countries"></a>

## Lande

Indsæt landets navn **på engelsk, præcis som skrevet her**, når installeren spørger efter dit land. Tabellen er genereret fra `bot/countries.py` — hvis et navn her og et navn der ikke stemmer overens, vinder `bot/countries.py`.

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

## Tak

> ⭐ **Giv dette projekt en stjerne på GitHub og følg [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — det er den simpleste måde at støtte Vortex på og hjælpe andre med at finde det. Tak!
