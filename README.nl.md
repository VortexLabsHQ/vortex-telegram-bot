# Vortex 🤖 — Je eigen Telegram-groepassistent

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · **Nederlands** · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Als je Vortex leuk vindt, geef dan een ster op GitHub en volg [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — dat helpt meer mensen het te vinden. Bedankt!

[![Licentie: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Wat is Vortex?

Vortex is een Telegram-bot die in je groepen en privéchats woont en antwoorden geeft met een AI-chatmodel. Je zegt zijn naam (de standaardnaam is **Vortex**) en hij antwoordt — hij kan chatten, het web doorzoeken, afbeeldingen maken, prijzen checken, moppen vertellen, bestanden lezen, spraakberichten omzetten naar tekst, en meer.

Hij draait op je eigen server, in je eigen land en taal. Jij bent de baas: een verborgen `/admin`-paneel laat je AI-sleutels, gebruikers en instellingen beheren.

## Functies

- 💬 **AI-chat** in groepen (wakewoord) en privéchats (geen wakewoord nodig)
- 🔑 **Token-pool** — gebruik verschillende LLM-providers en sleutels, roteer en failover automatisch
- 🖼️ **Afbeeldingen genereren en bewerken** — gratis (DuckAI) of betaalde providers
- 🔍 **Webzoeken** — zelfgehoste SearXNG, met Wikipedia als fallback
- 💰 **Live prijzen** — valuta, goud, olie en crypto in je lokale valuta
- 🕌 **Gebedstijden**, 🃏 **voorspellingen**, 😄 **moppen**, 🎲 **dobbelstenen en muntjes**
- 📎 **Bestandsanalyse** en **spraaktranscriptie**
- 📥 **Downloads** — stuur een link, krijg het mediabestand terug (tot 45 MB)
- 🌍 **195 landen** en **40 talen** — land en taal zijn afzonderlijke instellingen
- 🔄 **Zelf-updaterend** — checkt dagelijks op nieuwe releases en vraagt je voordat het updatet
- 🛡️ **Verborgen /admin-paneel** — tokens, gebruikers, statistieken, chats, afbeeldingsmodel, managers, aan/uit

## Voordat je installeert

Je hebt een server (of een computer die aanblijft) met **Linux** nodig, met deze dingen geïnstalleerd:

| Wat | Hoe te checken | Wat je zou moeten zien |
| --- | --- | --- |
| **Python 3.11 of nieuwer** | `python3 --version` | `Python 3.11.x` of hoger (3.12 en 3.13 werken ook) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` of `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` of vergelijkbaar |
| **Docker** *(optioneel)* | `docker --version` | `Docker version 2x.x.x` — alleen nodig als je de optionele SearXNG-webzoekfunctie wilt |

Als er iets ontbreekt, installeer je alles met één commando (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Voor de optionele Docker (alleen nodig als je de SearXNG-webzoekfunctie wilt gebruiken):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Na de laatste regel, log uit en weer in (of voer `docker`-commando's uit met `sudo`). De installer biedt ook aan ontbrekende tools voor je te installeren met `apt` op Debian/Ubuntu. Op andere systemen installeer je ze eerst met je pakketbeheerder. `systemd` zit standaard in het systeem — het kan niet apart geïnstalleerd worden.

Je hebt ook twee dingen van Telegram nodig (beide zijn gratis):

1. **Een bot-token** — praat met [@BotFather](https://t.me/BotFather) op Telegram, stuur `/newbot`, en kopieer het token dat hij geeft.
2. **Je numerieke Telegram-gebruikers-ID** — praat met [@userinfobot](https://t.me/userinfobot) en kopieer het getal dat hij toont. Dit is je "baas"-ID: alleen dit account kan `/admin` gebruiken.

## Installeren

Eén commando. Kopieer het, plak het in je terminal, en druk op Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

De installer vraagt je zes dingen, in volgorde:

1. **Land** — plak de Engelse naam van je land **precies zoals in de [landentabel](#countries) hieronder** (bijvoorbeeld `Turkey`). Het land stelt de tijdzone in, de lokale valuta voor prijzen, gebedstijden, en lokale content.
2. **Taal** — de taal waarin de bot praat (bijvoorbeeld `en`, `fa`, `tr`). Druk op Enter om de standaard voor je land te accepteren. Taal is los van land: het verandert alleen wat de bot zegt, en je kunt het later via `/admin` wijzigen.
3. **Bot-token** — plak het token van [@BotFather](https://t.me/BotFather). De installer checkt het live met Telegram.
4. **Baas numerieke ID** — je Telegram-gebruikers-ID van [@userinfobot](https://t.me/userinfobot).
5. **Botnaam / wakewoord** — de naam die mensen in groepen zeggen om met de bot te praten. Elke taal kan (bijvoorbeeld `Vortex` of `ورتکس`). Druk op Enter voor de standaard `Vortex`.
6. **Eerste LLM-provider** — kies een: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, of **Custom** (plak een basis-URL). Plak daarna je API-sleutel voor die provider — de installer haalt de live modellijst van de provider op en je kiest een model.

Daarna installeert de installer de afhankelijkheden, schrijft het `.env`-bestand, maakt de `vortex-bot` systemd-service, biedt aan om SearXNG te installeren voor webzoeken (heeft Docker nodig), en start de bot.

> ⚠️ **Anthropic werkt niet direct.** Anthropic's native API is niet OpenAI-compatibel, en deze bot spreekt alleen OpenAI-compatibele APIs. Als je Anthropic kiest, waarschuwt de installer je: de sleutel werkt alleen via een OpenAI-compatibele gateway. Gebruik OpenRouter, of een andere provider uit de lijst.

## Na het installeren

Check of de bot draait:

```bash
systemctl status vortex-bot
```

Je zou `active (running)` moeten zien. Om de live log te bekijken:

```bash
journalctl -u vortex-bot -f
```

Open nu Telegram en praat met je bot:

- Stuur `/start` — de bot zegt hallo.
- In een **privéchat**, schrijf gewoon naar hem — geen wakewoord nodig.
- In een **groep**, voeg de bot toe aan de groep, schakel daarna Groepsprivacy uit: in [@BotFather](https://t.me/BotFather) stuur `/setprivacy`, kies je bot en selecteer **Disable** — anders kan de bot geen groepsberichten zien en hoort hij zijn wakewoord niet. Zeg daarna zijn naam, bijvoorbeeld: `Vortex hoe laat is het?`
- Als baas, stuur `/admin` in een privéchat om het verborgen admin-paneel te openen.

**Updates zijn automatisch.** Een keer per dag checkt de bot GitHub op een nieuwe release. Als er een is, stuurt hij je een privébericht met ✅ / ❌ knoppen. Tik op ✅ en hij updated zichzelf en herstart — je hoeft de server nooit meer aan te raken.

## Configuratie

Alle instellingen zitten in het `.env`-bestand in de installatiemap. Zie [`.env.example`](.env.example) voor elke optie. De belangrijkste:

| Instelling | Wat het doet |
| --- | --- |
| `BOT_TOKEN` | Je Telegram-bot-token (van @BotFather) |
| `BOSS_ID` | Je numerieke Telegram-gebruikers-ID (de bot-eigenaar) |
| `BOT_NAME` | De naam en het wakewoord van de bot in groepen (standaard `Vortex`) |
| `BOT_COUNTRY` | Land in het Engels, bv. `United States` (stelt tijdzone, valuta, gebedstijden in) |
| `BOT_LANGUAGE` | Bot-taalcode, bv. `en`, `fa`, `tr` (verandert alleen wat de bot zegt) |
| `LLM_PROVIDERS` | LLM-providers en sleutels: `base_url\|api_key\|model`, kommagescheiden |
| `UPDATE_CHECK_ENABLED` | `1` = dagelijks checken op updates, `0` = nooit checken |
| `UPDATE_REPO` | De repo waarvan releases worden gevolgd (standaard `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Webzoeken: `searxng` (standaard), `tavily`, of `serper` |
| `DAILY_LIMIT_MESSAGES` | Max bot-antwoorden per gebruiker per dag (standaard `30`, baas is vrijgesteld) |

Land en taal kun je later ook via het verborgen `/admin`-paneel wijzigen (Taal & Land), zonder bestanden te bewerken.

## Docker-alternatief

Als je Docker de installer voorkeur geeft:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Dit start de bot samen met een zelfgehoste SearXNG-zoekmachine. Check de logs met `docker compose logs -f bot`.

Let op: de automatische self-updater heeft de systemd-service nodig, dus in Docker zijn updates handmatig: `git pull` en dan weer `docker compose up -d --build`.

## Functies in detail

### Het /admin-paneel

Stuur `/admin` in een privéchat (alleen baas — niemand anders kan het openen, en het verschijnt nooit in `/help` of de menu's). Het heeft:

- 🔑 **Tokens & model** — LLM-sleutels toevoegen of verwijderen, zien welke sleutels gezond zijn, het actieve model kiezen, de live modellijst van een provider bekijken
- 👥 **Gebruikers** — gebruikerstellingen, bannen / deblokkeren, allowlist
- 📊 **Statistieken** — gebruiksgetallen
- 💬 **Recente chats** — wat mensen tegen de bot zeiden (alleen baas, privé)
- 🖼️ **Afbeeldingsmodel** — DuckAI (gratis, standaard), HiLinkUp, een eigen aangepaste afbeeldingsservice, of uit
- 🛡️ **Managers** — vertrouwde mensen toegang geven tot delen van het paneel
- 🟢/🔴 **Aan/uit** — de bot aan of uit zetten voor iedereen (baas blijft in controle)
- 🌍 **Taal & Land** — de taal of het land van de bot op elk moment wijzigen

### De token-pool

De bot kan sleutels van meerdere LLM-providers tegelijk houden. Hij roteert tussen gezonde sleutels en faalt automatisch over als er een stopt met werken. Via `/admin` kun je één model vastpinnen, handmatig een model kiezen, of de bot vrij laten roteren. Elke provider met een OpenAI-compatibele API werkt — ook kleine aggregators, niet alleen de grote namen.

### Afbeeldingen

Afbeeldingsgeneratie heeft drie modi: **DuckAI** (gratis, geen sleutel, standaard), **HiLinkUp** (betaald, betere kwaliteit), of een **eigen** OpenAI-compatibele afbeeldingsservice. Je kunt de bot ook een foto sturen en vertellen hoe hij het moet bewerken ("maak dit cartoon-achtig"), en hij genereert een nieuwe afbeelding. Afbeeldingsgeneratie is via `/admin` uitschakelbaar.

### Landen en talen

Vortex ondersteunt **195 landen** en **40 talen**. Het land stelt de tijdzone in, de valuta waarin prijzen getoond worden, de stad voor gebedstijden, en lokale content. De taal stelt alleen in wat de bot zegt — een groep in België kan het land België en de taal Engels gebruiken, bijvoorbeeld. Beiden kun je later via `/admin` wijzigen.

### Updates

De bot checkt één keer per dag de GitHub-releases van `VortexLabsHQ/vortex-telegram-bot`. Als er een nieuwe versie is, stuurt hij de baas een privébericht met ✅ / ❌ knoppen. Accepteren updated de code en herstart de bot. Terwijl de repo privé is, doet de check stil niets (GitHub's API vereist een publieke repo) — zet `UPDATE_CHECK_ENABLED=0` als je de check nooit wilt.

## Probleemoplossing / Veelgestelde vragen

**De installer zegt dat mijn token ongeldig is.**
Het token komt van [@BotFather](https://t.me/BotFather). Zorg dat je het hele token hebt gekopieerd (cijfers, een dubbele punt, dan 35+ tekens), zonder extra spaties. Als je de bot verwijderde of een nieuw token maakte, werkt het oude niet meer — plak het nieuwe.

**De bot antwoordt niet in mijn groep.**
Vier dingen om te controleren: (1) Groepsprivacy moet uitstaan — in [@BotFather](https://t.me/BotFather) stuur `/setprivacy`, kies je bot en selecteer **Disable**; met privacy aan kan de bot geen groepsberichten zien, (2) de bot moet aan de groep worden toegevoegd, (3) je moet het wakewoord zeggen — de naam, bijvoorbeeld `Vortex hoe laat is het?` — de bot luistert alleen wanneer zijn naam in groepen wordt genoemd, (4) in een privéchat is geen wakewoord nodig.

**De bot antwoordt in het Engels, niet in mijn taal.**
Stuur `/admin` (alleen baas) → Taal & Land, en kies je taal. De installer vraagt ook om de taal — druk daar op Enter om de standaard van je land te accepteren.

**Ik koos Anthropic en de bot chat niet.**
Anthropic's native API is niet OpenAI-compatibel, dus de bot kan er niet direct mee chatten. Gebruik OpenRouter (die Claude-modellen kan serveren via een OpenAI-compatibele API), of kies een andere provider uit de lijst.

**Webzoeken werkt niet.**
Webzoeken heeft SearXNG nodig, wat de installer aanbiedt met Docker in te stellen. Zonder dat valt de bot terug op Wikipedia, wat zwakker is. Je kunt ook `SEARCH_PROVIDER=tavily` of `serper` zetten met een `SEARCH_API_KEY` in `.env`.

**Waar zijn de logs?**
`journalctl -u vortex-bot -f` toont de live log. `systemctl status vortex-bot` toont of de service draait. Als de bot stopt, start `sudo systemctl restart vortex-bot` hem weer.

**De bot zegt dat ik de daglimiet heb bereikt.**
Elke gebruiker krijgt 30 bot-antwoorden per dag (de baas is vrijgesteld). De limiet reset om middernacht in de tijdzone van het land van de bot. Verhoog het met `DAILY_LIMIT_MESSAGES` in `.env`, of vraag de baas.

**Ik heb een bug gevonden / Ik heb een idee.**
Open alstublieft een issue op GitHub — zie [CONTRIBUTING.md](CONTRIBUTING.md) voor hoe je het rapporteert en hoe je een fix indient.

## Ontwikkeling

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

Draai de tests (gewone Python-scripts, geen pytest nodig):

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

Alle negen suites moeten slagen voordat je een pull request opent. Zie [CONTRIBUTING.md](CONTRIBUTING.md) voor de code-stijl (ruff) en het PR-proces.

## Licentie

Vortex wordt uitgebracht onder de [MIT-licentie](LICENSE) — gratis om te gebruiken, kopiëren, wijzigen en delen, voor elk doel.

<a id="countries"></a>

## Landen

Plak de landnaam **in het Engels, precies zoals hier geschreven** wanneer de installer om je land vraagt. De tabel is gegenereerd vanuit `bot/countries.py` — als een naam hier en een naam daar ooit verschillen, wint `bot/countries.py`.

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



## Bedankt

> ⭐ **Geef alstublieft een ster op GitHub en volg [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — het is de simpelste manier om Vortex te steunen en anderen te helpen het te vinden. Bedankt!
