# Vortex 🤖 — Asistentul tău propriu pentru grupuri Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · **Română** · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Dacă îți place Vortex, te rog să dai stea acestui proiect pe GitHub și să urmezi [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — ajută mai multe persoane să-l găsească. Mulțumesc!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Ce este Vortex?

Vortex este un bot Telegram care trăiește în grupurile și conversațiile tale private și răspunde oamenilor cu un model AI de chat. Spui numele lui (numele implicit este **Vortex**) și el răspunde — poate discuta, căuta pe web, crea imagini, verifica prețuri, spune glume, citi fișiere, transcrie mesaje vocale și multe altele.

Rulează pe propriul tău server, în propria ta țară și limbă. Ești șeful: un panou `/admin` ascuns îți permite să gestionezi cheile AI, utilizatorii și setările.

## Funcționalități

- 💬 **Chat AI** în grupuri (cuvânt de declanșare) și conversații private (fără cuvânt de declanșare necesar)
- 🔑 **Grup de tokenuri** — folosește mai mulți furnizori LLM și chei, rotește și comută automat la rezervă
- 🖼️ **Generare imagini** — cu propriul serviciu de imagini (URL de bază + cheie API + model), adăugat în `/admin`
- 🔍 **Căutare pe web** — SearXNG auto-gazduit, cu rezervă Wikipedia
- 💰 **Prețuri live** — valute, aur, petrol și crypto în moneda ta locală
- 🕌 **Ore de rugăciune**, 🃏 **norocuri**, 😄 **glume**, 🎲 **zaruri și aruncări de monetă**
- 📎 **Analiză fișiere** și **transcriere voce**
- 📥 **Descărcări** — trimite un link, primești fișierul media înapoi (până la 45 MB)
- 🌍 **195 țări** și **40 limbi** — țara și limba sunt setări separate
- 🔄 **Auto-actualizare** — verifică zilnic versiuni noi și te întreabă înainte de actualizare
- 🛡️ **Panou /admin ascuns** — tokenuri, utilizatori, statistici, conversații, model imagine, manageri, putere

## Înainte de a instala

Ai nevoie de un server (sau un calculator care rămâne pornit) care rulează **Linux** cu acestea instalate:

| Ce | Cum verifici | Ce ar trebui să vezi |
| --- | --- | --- |
| **Python 3.11 sau mai nou** | `python3 --version` | `Python 3.11.x` sau mai nou (3.12 și 3.13 funcționează de asemenea) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` sau `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` sau similar |
| **Docker** *(opțional)* | `docker --version` | `Docker version 2x.x.x` — necesar doar dacă vrei căutarea web opțională SearXNG |

Dacă lipsește ceva, instalați totul cu o singură comandă (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Pentru `Docker` opțional (necesar doar dacă doriți căutarea web `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

După ultima linie, deconectați-vă și reconectați-vă (sau rulați comenzi `docker` cu `sudo`). Instalatorul vă propune, de asemenea, să instalați instrumentele lipsă cu `apt` pe `Debian/Ubuntu`. Pe alte sisteme, instalați-le mai întâi cu managerul de pachete. `systemd` vine cu sistemul — nu poate fi instalat separat.

Ai nevoie și de două lucruri de la Telegram (ambele sunt gratuite):

1. **Un token de bot** — discută cu [@BotFather](https://t.me/BotFather) pe Telegram, trimite `/newbot` și copiază tokenul pe care îți-l dă.
2. **ID-ul tău numeric de utilizator Telegram** — discută cu [@userinfobot](https://t.me/userinfobot) și copiază numărul pe care îți arată. Acesta este ID-ul tău de "șef": doar acest cont poate folosi `/admin`.

## Instalare

O singură comandă. Copiaz-o, lipeste-o în terminal și apasă Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Programul de instalare te întreabă șase întrebări, în ordine:

1. **Țară** — lipiți numele în engleză al țării **exact așa cum este listat în [tabelul țărilor](#countries) mai jos** (de exemplu `Turkey`). Țara stabilește fusul orar, moneda locală pentru prețuri, timpii de rugăciune și conținutul local.
2. **Limbă** — limba pe care botul o vorbește (de exemplu `en`, `fa`, `tr`). Apăsați Enter pentru a accepta valoarea implicită pentru țara dvs. Limba este separată de țară: schimbă doar ce spune botul, și o puteți modifica ulterior din `/admin`.
3. **Token bot** — lipiți tokenul de la [@BotFather](https://t.me/BotFather). Instalatorul îl verifică live cu Telegram.
4. **ID numeric Boss** — ID-ul dvs. de utilizator Telegram de la [@userinfobot](https://t.me/userinfobot).
5. **Nume bot / cuvânt de trezire** — numele pe care oamenii îl spun în grupuri ca să vorbească cu botul. Orice limbă e bine (de exemplu `Vortex` sau `ورتکس`). Apăsați Enter pentru valoarea implicită `Vortex`.
6. **Primul furnizor LLM** — alegeți unul: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, sau **Custom** (lipiți un URL de bază). Apoi lipiți cheia API pentru acel furnizor — instalatorul preia lista live de modele a furnizorului și alegeți un model.

Apoi instalatorul instalează dependențele, scrie fișierul `.env`, creează serviciul systemd `vortex-bot`, propune să instaleze SearXNG pentru căutare web (necesită Docker), și pornește botul.

> ⚠️ **Anthropic nu funcționează direct.** API-ul nativ al Anthropic nu este compatibil cu OpenAI, iar acest bot vorbește doar API-uri compatibile OpenAI. Dacă alegeți Anthropic, instalatorul vă avertizează: cheia funcționează doar printr-o poartă compatibilă OpenAI. Folosiți OpenRouter, sau un alt furnizor din listă, în schimb.

## După instalare

Verificați că botul rulează:

```bash
systemctl status vortex-bot
```

Ar trebui să vedeți `active (running)`. Pentru a urmări logul live:

```bash
journalctl -u vortex-bot -f
```

Acum deschideți Telegram și vorbiți cu botul:

- Trimiteți `/start` — botul vă saluează.
- Într-un **chat privat**, scrieți pur și simplu — nu e nevoie de cuvânt de trezire.
- Într-un **grup**, adaugă botul în grup, apoi dezactivează Confidențialitatea grupului: în [@BotFather](https://t.me/BotFather) trimite `/setprivacy`, selectează botul tău și alege **Disable** — altfel botul nu poate vedea mesajele din grup și nu va auzi cuvântul său de activare. Apoi spune numele său, de exemplu: `Vortex what's the time?`
- Ca boss, trimiteți `/admin` într-un chat privat pentru a deschide panoul admin ascuns.

**Actualizările sunt automate.** Odată pe zi botul verifică GitHub pentru o nouă versiune. Dacă una e disponibilă, vă trimite un mesaj privat cu butoane ✅ / ❌. Apăsați ✅ și se actualizează singur și repornește — nu trebuie să atingeți serverul niciodată.

## Configurare

Toate setările se află în fișierul `.env` din directorul de instalare. Vedeți [`.env.example`](.env.example) pentru fiecare opțiune. Cele mai importante:

| Setare | Ce face |
| --- | --- |
| `BOT_TOKEN` | Tokenul tău de bot Telegram (de la @BotFather) |
| `BOSS_ID` | ID-ul tău numeric de utilizator Telegram (proprietarul botului) |
| `BOT_NAME` | Numele botului și cuvântul de declanșare în grupuri (implicit `Vortex`) |
| `BOT_COUNTRY` | Țara în engleză, ex. `United States` (stabilește fusul orar, valuta, timpii de rugăciune) |
| `BOT_LANGUAGE` | Codul limbii botului, ex. `en`, `fa`, `tr` (schimbă doar ce spune botul) |
| `LLM_PROVIDERS` | Furnizori LLM și chei: `base_url\|api_key\|model`, separate prin virgulă |
| `UPDATE_CHECK_ENABLED` | `1` = verifică actualizările zilnic, `0` = nu verifica niciodată |
| `UPDATE_REPO` | Repo-ul al cărui release-uri sunt monitorizate (implicit `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Căutare web: `searxng` (implicit), `tavily`, sau `serper` |
| `DAILY_LIMIT_MESSAGES` | Maxim răspunsuri bot per utilizator pe zi (implicit `30`, bossul este exempt) |

Țara și limba pot fi schimbate ulterior din panoul ascuns `/admin` (Limba & Țară), fără a edita niciun fișier.

## Alternativa Docker

Dacă preferați Docker în locul installer-ului:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Acest lucru pornește botul împreună cu un motor de căutare SearXNG auto-gazduit. Verificați logurile cu `docker compose logs -f bot`.

Notă: actualizatorul automat are nevoie de serviciul systemd, așadar în Docker actualizările sunt manuale: `git pull` și apoi `docker compose up -d --build` din nou.

## Funcționalități în detaliu

### Panoul /admin

Trimiteți `/admin` într-un chat privat (doar bossul — nimeni altul nu-l poate deschide, și nu apare niciodată în `/help` sau în meniuri). Are:

- 🔑 **Tokenuri & model** — adăugați sau eliminați chei LLM, vedeți ce chei sunt sănătoase, alegeți modelul activ, parcurgeți lista live de modele a unui furnizor
- 👥 **Utilizatori** — numărul utilizatorilor, ban / unban, listă de permitere
- 📊 **Statistici** — numere de utilizare
- 💬 **Chat-uri recente** — ce au spus oamenii botului (doar bossul, privat)
- 🖼️ **Model imagine** — propriul serviciu de imagini (URL de bază + cheie API + model), sau oprit
- 🛡️ **Manageri** — dați persoanelor de încredere acces la părți din panou
- 🟢/🔴 **Putere** — porniți sau opriți botul pentru toți (bossul rămâne în control)
- 🌍 **Limba & Țara** — schimbați limba sau țara botului oricând

### Pool-ul de tokenuri

Botul poate ține chei de la mai mulți furnizori LLM odată. Rotește între cheile sănătoase și face failover automat când una oprește să funcționeze. Din `/admin` puteți fixa un model, alegeți un model manual, sau lăsați botul să rotească liber. Orice furnizor cu API compatibil OpenAI funcționează — inclusiv agregatori mici, nu doar cele mari.

### Imagini

Generarea de imagini folosește propriul serviciu de imagini compatibil OpenAI: adăugați URL-ul de bază, cheia API și modelul în `/admin` (🖼️ Image model). Nu există un furnizor de imagini integrat, și editarea fotografiilor nu este acceptată. Generarea de imagini poate fi dezactivată din `/admin`.

### Țări și limbi

Vortex acceptă **195 de țări** și **40 de limbi**. Țara stabilește fusul orar, moneda în care sunt afișate prețurile, orașul folosit pentru timpii de rugăciune și conținutul local. Limba stabilește doar ce spune botul — un grup din Belgia poate folosi țara Belgia și limba engleză, de exemplu. Ambele pot fi schimbate ulterior din `/admin`.

### Actualizări

Botul verifică versiunile GitHub ale `VortexLabsHQ/vortex-telegram-bot` o dată pe zi. Când este disponibilă o versiune nouă, trimite un mesaj privat șefului cu butoanele ✅ / ❌. Acceptarea actualizează codul și repornește botul. Pe timp ce depozitul este privat, verificarea nu face nimic în mod tăcut (API-ul GitHub necesită un depozit public) — setează `UPDATE_CHECK_ENABLED=0` dacă nu dorești niciodată verificarea.

## Depanare / Întrebări frecvente

**Instalatorul spune că token-ul meu este invalid.**
Token-ul provine de la [@BotFather](https://t.me/BotFather). Asigură-te că ai copiat întregul token (cifre, două puncte, apoi 35+ caractere), fără spații extra. Dacă ai șters botul sau ai creat un token nou, cel vechi nu mai funcționează — lipește cel nou.

**Botul nu răspunde în grupul meu.**
Patru lucruri de verificat: (1) Confidențialitatea grupului trebuie să fie dezactivată — în [@BotFather](https://t.me/BotFather) trimite `/setprivacy`, selectează botul tău și alege **Disable**; cu confidențialitatea activată, botul nu poate vedea mesajele din grup deloc, (2) botul trebuie adăugat în grup, (3) trebuie să spui cuvântul său de activare — numele său, de exemplu `Vortex what's the time?` — botul ascultă doar când numele său este spus în grupuri, (4) într-un chat privat nu este necesar niciun cuvânt de activare.

**Botul răspunde în engleză, nu în limba mea.**
Trimite `/admin` (doar șeful) → Limbă & Țară, și alege limba ta. Instalatorul întreabă și el pentru limbă — apasă Enter acolo pentru a accepta implicita țării tale.

**Am ales Anthropic și botul nu conversă.**
API-ul nativ al Anthropic nu este compatibil cu OpenAI, deci botul nu poate conversa direct cu el. Folosește OpenRouter (care poate servi modele Claude printr-un API compatibil OpenAI), sau alege un alt furnizor din listă.

**Căutarea pe web nu funcționează.**
Căutarea pe web necesită SearXNG, pe care instalatorul îl propune să-l configureze cu Docker. Fără el, botul revine la Wikipedia, care este mai slabă. Poți seta și `SEARCH_PROVIDER=tavily` sau `serper` cu un `SEARCH_API_KEY` în `.env`.

**Unde sunt log-urile?**
`journalctl -u vortex-bot -f` afișează log-ul live. `systemctl status vortex-bot` arată dacă serviciul rulează. Dacă botul se oprește, `sudo systemctl restart vortex-bot` îl pornește din nou.

**Botul spune că am atins limita zilnică.**
Fiecare utilizator primește 30 de răspunsuri de la bot pe zi (șeful este exempt). Limita se resetează la miezul nopții în fusul orar al țării botului. O poți crește cu `DAILY_LIMIT_MESSAGES` în `.env`, sau întreabă șeful.

**Am găsit un bug / Am o idee.**
Te rog deschide un issue pe GitHub — vezi [CONTRIBUTING.md](CONTRIBUTING.md) pentru cum să-l raportezi și cum să trimiți o corecție.

## Dezvoltare

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

Rulează testele (scripturi Python simple, nu e nevoie de pytest):

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

Toate cele nouă suite trebuie să treacă înainte de a deschide un pull request. Vezi [CONTRIBUTING.md](CONTRIBUTING.md) pentru stilul de cod (ruff) și procesul PR.

## Licență

Vortex este lansat sub [Licența MIT](LICENSE) — liber de folosit, copiat, modificat și partajat, pentru orice scop.

<a id="countries"></a>

## Țări

Lipiți numele țării **în engleză, exact așa cum este scris aici** când programul de instalare vă solicită țara. Tabelul este generat din `bot/countries.py` — dacă un nume de aici și unul de acolo nu se potrivesc, `bot/countries.py` câștigă.

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

## Mulțumiri

> ⭐ **Vă rugăm să dați stea acestui proiect pe GitHub și să urmăriți [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — este cea mai simplă modalitate de a sprijini Vortex și de a ajuta alții să-l descopere. Mulțumim!
