# Vortex 🤖 — Din egen Telegram-gruppassistent

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · **Svenska** · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Om du gillar Vortex, vänligen stjärnmärk detta projekt på GitHub och följ [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — det hjälper fler att hitta det. Tack!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vad är Vortex?

Vortex är en Telegram-bot som finns i dina grupper och privata chattar och svarar med en AI-chattmodell. Du säger dess namn (standardnamnet är **Vortex**) och den svarar — den kan chatta, söka på webben, skapa bilder, kolla priser, berätta skämt, läsa filer, transkribera röstmeddelanden, och mer.

Den körs på din egen server, i ditt eget land och på ditt eget språk. Du är chefen: en dold `/admin`-panel låter dig hantera AI-nycklar, användare och inställningar.

## Funktioner

- 💬 **AI-chatt** i grupper (uppvakningsord) och privata chattar (inget uppvakningsord behövs)
- 🔑 **Tokenpool** — använd flera LLM-leverantörer och nycklar, rotera och växla automatiskt
- 🖼️ **Bildgenerering och redigering** — gratis (DuckAI) eller betalda leverantörer
- 🔍 **Webbsökning** — självhostad SearXNG, med Wikipedia som reserv
- 💰 **Live-priser** — valutor, guld, olja och krypto i din lokala valuta
- 🕌 **Bönestider**, 🃏 **förutsägelser**, 😄 **skämt**, 🎲 **tärningar och myntkast**
- 📎 **Filanalys** och **röstavskrift**
- 📥 **Nedladdningar** — skicka en länk, få tillbaka mediefilen (upp till 45 MB)
- 🌍 **195 länder** och **40 språk** — land och språk är separata inställningar
- 🔄 **Självuppdatering** — söker efter nya versioner dagligen och frågar innan uppdatering
- 🛡️ **Dold /admin-panel** — tokens, användare, statistik, chattar, bildmodell, hanterare, kraft

## Innan du installerar

Du behöver en server (eller en dator som ständigt är på) som kör **Linux** med följande installerat:

| Vad | Hur du kontrollerar | Vad du bör se |
| --- | --- | --- |
| **Python 3.11 eller nyare** | `python3 --version` | `Python 3.11.x` eller högre (3.12 och 3.13 fungerar också) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` eller `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` eller liknande |
| **Docker** *(valfritt)* | `docker --version` | `Docker version 2x.x.x` — behövs bara om du vill ha den valfria SearXNG-webbsökningen |

Om något saknas, installera allt med ett kommando (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

För den valfria `Docker` (behövs bara om du vill ha `SearXNG` webbsökning):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Efter den sista raden, logga ut och in igen (eller kör `docker`-kommandon med `sudo`). Installationsprogrammet erbjuder också att installera saknade verktyg åt dig med `apt` på `Debian/Ubuntu`. På andra system, installera dem med din pakethanterare först. `systemd` ingår i systemet — det kan inte installeras separat.

Du behöver också två saker från Telegram (båda är gratis):

1. **En bot-token** — prata med [@BotFather](https://t.me/BotFather) på Telegram, skicka `/newbot` och kopiera token den ger dig.
2. **Ditt numeriska Telegram-användar-ID** — prata med [@userinfobot](https://t.me/userinfobot) och kopiera numret den visar. Detta är ditt "chef"-ID: bara det här kontot kan använda `/admin`.

## Installera

Ett kommando. Kopiera det, klistra in det i din terminal, och tryck Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Installationsprogrammet ställer sex frågor, i ordning:

1. **Land** — klistra in det engelska namnet på ditt land **exakt som det står i [landtabellen](#countries) nedan** (t.ex. `Turkey`). Landet ställer in tidszon, lokal valuta för priser, bönestider och lokalt innehåll.
2. **Språk** — språket botten talar (t.ex. `en`, `fa`, `tr`). Tryck Enter för att acceptera standardvärdet för ditt land. Språk är separat från land: det ändrar bara vad botten säger, och du kan ändra det senare via `/admin`.
3. **Bot-token** — klistra in token från [@BotFather](https://t.me/BotFather). Installationsprogrammet verifierar det direkt mot Telegram.
4. **Chefens numeriska ID** — ditt Telegram-användar-ID från [@userinfobot](https://t.me/userinfobot).
5. **Botnamn / väckord** — namnet folk säger i grupper för att prata med botten. Vilket språk som helst fungerar (t.ex. `Vortex` eller `ورتکس`). Tryck Enter för standardvärdet `Vortex`.
6. **Första LLM-leverantör** — välj en: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, eller **Anpassad** (klistra in en bas-URL). Sedan klistrar du in din API-nyckel för den leverantören — installationsprogrammet hämtar leverantörens aktuella modellista och du väljer en modell.

Sedan installerar installationsprogrammet beroenden, skriver `.env`-filen, skapar `vortex-bot`-systemdtjänsten, erbjuder att installera SearXNG för webbsökning (kräver Docker), och startar botten.

> ⚠️ **Anthropic fungerar inte direkt.** Anthropics inbyggda API är inte OpenAI-kompatibelt, och den här botten pratar bara OpenAI-kompatibla API:er. Om du väljer Anthropic varnar installationsprogrammet dig: nyckeln fungerar bara genom en OpenAI-kompatibel gateway. Använd OpenRouter, eller en annan leverantör från listan, istället.

## Efter installationen

Kontrollera att boten körs:

```bash
systemctl status vortex-bot
```

Du bör se `active (running)`. För att följa loggen live:

```bash
journalctl -u vortex-bot -f
```

Öppna nu Telegram och prata med din bot:

- Skicka `/start` — boten säger hej.
- I en **privat chatt**, skriv bara till den — inget aktiveringsord behövs.
- I en **grupp**, lägg till boten i gruppen, stäng sedan av gruppintegritet: i [@BotFather](https://t.me/BotFather) skicka `/setprivacy`, välj din bot och välj **Disable** — annars kan boten inte se gruppmeddelanden och hör inte sitt vakningsord. Säg sedan dess namn, till exempel: `Vortex what's the time?`
- Som chef, skicka `/admin` i en privat chatt för att öppna den dolda adminpanelen.

**Uppdateringar sker automatiskt.** En gång per dag kontrollerar boten GitHub efter en ny version. Om en finns tillgänglig skickar den ett privat meddelande med ✅ / ❌-knappar. Tryck på ✅ så uppdaterar den sig själv och startar om — du behöver aldrig röra servern.

## Konfiguration

Alla inställningar finns i `.env`-filen i installationsmappen. Se [`.env.example`](.env.example) för alla alternativ. De viktigaste:

| Inställning | Vad den gör |
| --- | --- |
| `BOT_TOKEN` | Din Telegram-bot-token (från @BotFather) |
| `BOSS_ID` | Ditt numeriska Telegram-användar-ID (bot-ägaren) |
| `BOT_NAME` | Botens namn och aktiveringsord i grupper (standard `Vortex`) |
| `BOT_COUNTRY` | Land på engelska, t.ex. `United States` (sätter tidszon, valuta, bönestider) |
| `BOT_LANGUAGE` | Botens språkkod, t.ex. `en`, `fa`, `tr` (ändrar bara vad boten säger) |
| `LLM_PROVIDERS` | LLM-leverantörer och nycklar: `base_url\|api_key\|model`, komma-separerade |
| `UPDATE_CHECK_ENABLED` | `1` = kontrollera uppdateringar dagligen, `0` = kontrollera aldrig |
| `UPDATE_REPO` | Repot vars releaser övervakas (standard `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Webbsearch: `searxng` (standard), `tavily`, eller `serper` |
| `DAILY_LIMIT_MESSAGES` | Max bot-svar per användare per dag (standard `30`, boss är undantagen) |

Land och språk kan också ändras senare från den dolda `/admin`-panelen (Language & Country), utan att redigera någon fil.

## Docker-alternativ

Om du föredrar Docker framför installationsprogrammet:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Detta startar boten tillsammans med en egenvärdad SearXNG-sökmotor. Kolla loggarna med `docker compose logs -f bot`.

Obs: den automatiska självuppdateraren behöver systemd-tjänsten, så i Docker är uppdateringar manuella: `git pull` och sedan `docker compose up -d --build` igen.

## Funktioner i detalj

### /admin-panelen

Skicka `/admin` i en privat chatt (endast chef — ingen annan kan öppna den, och den visas aldrig i `/help` eller menyerna). Den har:

- 🔑 **Tokens & modell** — lägg till eller ta bort LLM-nycklar, se vilka nycklar som är felfria, välj aktiv modell, bläddra i en leverantörs live-modellista
- 👥 **Användare** — antal användare, banna / avbanna, tillåtelselista
- 📊 **Statistik** — användningssiffror
- 💬 **Senaste chattar** — vad folk säger till botten (endast chef, privat)
- 🖼️ **Bildmodell** — DuckAI (gratis, standard), HiLinkUp, en anpassad bildtjänst, eller av
- 🛡️ **Manager** — ge betrodda personer tillgång till delar av panelen
- 🟢/🔴 **Ström** — slå på eller av botten för alla (chefen behåller kontrollen)
- 🌍 **Språk & Land** — ändra botten språk eller land när som helst

### Token-poolen

Botten kan hålla nycklar från flera LLM-leverantörer samtidigt. Den växlar mellan felfria nycklar och byter automatiskt när en slutar fungera. Från `/admin` kan du fästa en modell, välja en modell manuellt, eller låta botten rotera fritt. Vilken leverantör som helst med ett OpenAI-kompatibelt API fungerar — inklusive små aggregatorer, inte bara de stora namnen.

### Bilder

Bildgenerering har tre lägen: **DuckAI** (gratis, ingen nyckel, standard), **HiLinkUp** (betald, bättre kvalitet), eller en **anpassad** OpenAI-kompatibel bildtjänst av din egen. Du kan också skicka en foto till botten och säga hur den ska redigeras ("gör den här till tecknad stil"), och den genererar en ny bild. Bildgenerering kan stängas av från `/admin`.

### Länder och språk

Vortex stöder **195 länder** och **40 språk**. Landet ställer in tidszon, valuta som priser visas i, stad som används för bönestider, och lokalt innehåll. Språket styr bara vad botten säger — en grupp i Belgium kan till exempel använda landet Belgium och språket English. Båda kan ändras senare från `/admin`.

### Uppdateringar

Botten kollar GitHub-releases för `VortexLabsHQ/vortex-telegram-bot` en gång per dag. När en ny version finns, skickar den ett privat meddelande till chefen med ✅ / ❌-knappar. Att godkänna uppdaterar koden och startar om botten. Medan repot är privat, gör kontrollen inget tyst (GitHubs API kräver ett publikt repo) — sätt `UPDATE_CHECK_ENABLED=0` om du aldrig vill ha kontrollen.

## Felsökning / Vanliga frågor

**Installationsprogrammet säger att min token är ogiltig.**
Tokenen kommer från [@BotFather](https://t.me/BotFather). Se till att du kopierade hela tokenen (siffror, ett kolon, sedan 35+ tecken), utan extra mellanslag. Om du raderade boten eller skapade en ny token slutar den gamla att fungera — klistra in den nya.

**Boten svarar inte i min grupp.**
Fyra saker att kontrollera: (1) Gruppintegritet måste vara avstängd — i [@BotFather](https://t.me/BotFather) skicka `/setprivacy`, välj din bot och välj **Disable**; med integritet på kan boten inte se gruppmeddelanden alls, (2) boten måste läggas till i gruppen, (3) du måste säga dess vakningsord — dess namn, till exempel `Vortex what's the time?` — boten lyssnar bara när dess namn sags i grupper, (4) i en privat chatt behövs inget vakningsord alls.

**Boten svarar på engelska, inte på mitt språk.**
Skicka `/admin` (endast chef) → Språk & Land, och välj ditt språk. Installationsprogrammet frågar också efter språket — tryck Enter där för att acceptera ditt lands standard.

**Jag valde Anthropic men boten chattar inte.**
Anthropics inbyggda API är inte OpenAI-kompatibelt, så boten kan inte chatta med det direkt. Använd OpenRouter (som kan servera Claude-modeller genom ett OpenAI-kompatibelt API), eller välj en annan leverantör från listan.

**Webbsökning fungerar inte.**
Webbsökning behöver SearXNG, som installationsprogrammet erbjuder att sätta upp med Docker. Utan det faller boten tillbaka på Wikipedia, som är svagare. Du kan också sätta `SEARCH_PROVIDER=tavily` eller `serper` med en `SEARCH_API_KEY` i `.env`.

**Var finns loggarna?**
`journalctl -u vortex-bot -f` visar loggen live. `systemctl status vortex-bot` visar om tjänsten körs. Om boten stannar, `sudo systemctl restart vortex-bot` startar den igen.

**Boten säger att jag nått dagens gräns.**
Varje användare får 30 bot-svar per dag (chefen är undantagen). Gränsen nollställs vid midnatt i botens lands tidszon. Öka den med `DAILY_LIMIT_MESSAGES` i `.env`, eller be chefen.

**Jag hittade en bugg / Jag har ett förslag.**
Öppna gärna ett ärende på GitHub — se [CONTRIBUTING.md](CONTRIBUTING.md) för hur du rapporterar det och hur du skickar en fix.

## Utveckling

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

Kör testen (vanliga Python-skript, pytest behövs inte):

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

Alla nio testsviter måste godkännas innan du öppnar en pull request. Se [CONTRIBUTING.md](CONTRIBUTING.md) för kodstilen (ruff) och PR-processen.

## Licens

Vortex släpps under [MIT License](LICENSE) — fri att använda, kopiera, ändra och dela, för vilket syfte som helst.

## Länder

Klistra in landets namn **på engelska, exakt som det står här** när installationsprogrammet frågar efter ditt land. Tabellen genereras från `bot/countries.py` — om ett namn här och ett namn där skulle skilja sig åt, gäller `bot/countries.py`.

<a id="countries"></a>

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

## Tack

> ⭐ **Vänligen stjärnmärk detta projekt på GitHub och följ [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — det är det enklaste sättet att stödja Vortex och hjälpa andra att hitta det. Tack!
