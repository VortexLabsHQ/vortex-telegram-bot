# Vortex 🤖 — A saját Telegram csoport asszisztense

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · **Magyar** · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Ha tetszik a Vortex, kérlek, csillagozd meg a projektet a GitHubon és kövesd a [@VortexLabsHQ](https://github.com/VortexLabsHQ) fiókot** — ez segít, hogy többen találják meg. Köszönjük!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Mi az a Vortex?

A Vortex egy Telegram-bot, amely a csoportjaidban és privát csevegéseidben él, és egy AI csevegési modell segítségével válaszol az embereknek. Azt hívod a nevén (az alapértelmezett név a **Vortex**) és válaszol — tud beszélgetni, keresni a weben, képeket készíteni, árakat ellenőrizni, vicceket mesélni, fájlokat olvasni, hangüzeneteket átírni, és még sok mást.

A saját szervereden fut, a saját országodban és nyelven. Te vagy a főnök: egy rejtett `/admin` panellel kezelheted az AI kulcsokat, felhasználókat és beállításokat.

## Funkciók

- 💬 **AI csevegés** csoportokban (ébresztő szó) és privát csevegésekben (ébresztő szó nem kell)
- 🔑 **Token pool** — több LLM szolgáltató és kulcs használata, automatikus rotáció és feladatátvétel
- 🖼️ **Képgenerálás és szerkesztés** — ingyenes (DuckAI) vagy fizetős szolgáltatók
- 🔍 **Webes keresés** — saját SearXNG, Wikipédia tartalékkal
- 💰 **Valós idejű árak** — devízák, arany, olaj és kripto a helyi valutádban
- 🕌 **Imaidők**, 🃏 **jósolások**, 😄 **viccek**, 🎲 **kockadobás és pénzfeldobás**
- 📎 **Fájlelemzés** és **hangátírás**
- 📥 **Letöltések** — küldj egy linket, kapd vissza a médiafájlt (legfeljebb 45 MB)
- 🌍 **195 ország** és **40 nyelv** — az ország és a nyelv külön beállítás
- 🔄 **Önfrissítés** — naponta ellenőrzi az új kiadásokat, és kérdez rögzítés előtt
- 🛡️ **Rejtett /admin panel** — tokenek, felhasználók, statisztikák, csevegések, képmodell, menedzserek, teljesítmény

## Mielőtt telepítenéd

Szükséged van egy szerverre (vagy egy folyamatosan bekapcsolt számítógépre) **Linux** rendszerrel, amin ezek telepítve vannak:

| Mit | Hogyan ellenőrizd | Mit kell látnod |
| --- | --- | --- |
| **Python 3.11 vagy újabb** | `python3 --version` | `Python 3.11.x` vagy magasabb (3.12 és 3.13 is működik) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` vagy `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` vagy hasonló |
| **Docker** *(opcionális)* | `docker --version` | `Docker version 2x.x.x` — csak akkor kell, ha az opcionális SearXNG webes keresést akarod használni |

Ha valami hiányzik, telepítsd mindent egy paranccsal (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Az opcionális `Docker`hoz (csak akkor kell, ha a `SearXNG` webkeresést szeretnéd):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Az utolsó sor után jelentkezz ki és be újra (vagy futtasd a `docker` parancsokat `sudo`val). A telepítő felajánlja, hogy `apt`-vel telepítse a hiányzó eszközöket `Debian/Ubuntu`-n. Más rendszereken előbb a csomagkezelővel telepítsd meg őket. A `systemd` a rendszerrel együtt jön — nem telepíthető külön.

Kell még két dolog a Telegramból (mindkettő ingyenes):

1. **Egy bot token** — beszélj a [@BotFather](https://t.me/BotFather) felhasználóval a Telegramon, küldd el a `/newbot` parancsot, és másold ki a kapott token.
2. **A számszerűs Telegram felhasználói ID-d** — beszélj a [@userinfobot](https://t.me/userinfobot) felhasználóval, és másold ki a megjelenő számot. Ez a "főnök" ID-d: csak ez a fiók használhatja a `/admin` parancsot.

## Telepítés

Egy parancs. Másold ki, illeszd be a terminálba, és nyomj Entert:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

A telepítő hat kérdést tesz fel, sorrendben:

1. **Ország** — illeszd be az angol nyelvű országnevet **pontosan úgy, ahogy az az [országok táblázatában](#countries) lent szerepel** (pl. `Turkey`). Az ország határozza meg az időzónát, a helyi valutát az árakhoz, az imádságidőket és a helyi tartalmakat.
2. **Nyelv** — a nyelv, amin a bot beszél (pl. `en`, `fa`, `tr`). Nyomd meg az Entert a te országodhoz tartozó alapértelmezett elfogadásához. A nyelv elkülönül az országtól: csak azt változtatja meg, amit a bot mond, és később módosítható `/admin`-ból.
3. **Bot token** — illeszd be a token-t a [@BotFather](https://t.me/BotFather) oldalról. A telepítő élőben ellenőrzi a Telegrammal.
4. **Főadmin numerikus ID** — a Telegram felhasználói ID-d a [@userinfobot](https://t.me/userinfobot) oldalról.
5. **Bot neve / ébresztő szó** — a név, amit az emberek mondanak a csoportokban, hogy a bottal beszéljenek. Bármilyen nyelv megfelel (pl. `Vortex` vagy `ورتکس`). Nyomd meg az Entert az alapértelmezett `Vortex`hez.
6. **Első LLM szolgáltató** — válassz egyet: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, vagy **Custom** (illeszd be a base URL-t). Utána add meg az API kulcsod ehhez a szolgáltatóhoz — a telepítő letölti a szolgáltató élő modelllistáját, és te kiválasztasz egy modellt.

Ezután a telepítő telepíti a függőségeket, létrehozza a `.env` fájlt, létrehozza a `vortex-bot` systemd szolgáltatást, felajánlja a SearXNG telepítését webes kereséshez (Docker kell hozzá), és elindítja a botot.

> ⚠️ **Az Anthropic nem működik közvetlenül.** Az Anthropic natív API-ja nem OpenAI-kompatibilis, és ez a bot csak OpenAI-kompatibilis API-kat beszél. Ha Anthropic-ot választasz, a telepítő figyelmeztet: a kulcs csak OpenAI-kompatibilis átjárón keresztül működik. Használd helyette az OpenRoutert, vagy a listából egy másik szolgáltatót.

## Telepítés után

Ellenőrizd, hogy a bot fut:

```bash
systemctl status vortex-bot
```

`active (running)`-ot kellene látnod. Az élő napló követéséhez:

```bash
journalctl -u vortex-bot -f
```

Most nyisd meg a Telegramot és beszélgess a botoddal:

- Küldd el a `/start` parancsot — a bot üdvözöl.
- **Privát csevegésben** csak írd be az üzeneted — ébresztő szó nem kell.
- **Csoportban**ban add hozzá a botot a csoporthoz, majd kapcsold ki a Csoportadatvédelmet: a [@BotFather](https://t.me/BotFather) küldd el a `/setprivacy` parancsot, válaszd ki a botodat, és válaszd a **Disable** opciót — különben a bot nem látja a csoport üzeneteit és nem hallja az ébresztő szót. Ezután mondd ki a nevét, például: `Vortex hány óra van?`
- Főadminként küldd el az `/admin` parancsot privát csevegésben a rejtett admin panel megnyitásához.

**A frissítések automatikusan történnek.** Naponta egyszer a bot ellenőrzi a GitHubon, hogy van-e új kiadás. Ha igen, privát üzenetben küldi el ✅ / ❌ gombokkal. Nyomd meg a ✅-ot, és az automatikusan frissül és újraindul — soha nem kell hozzányúlni a szerverhez.

## Konfiguráció

Minden beállítás a telepítési mappában lévő `.env` fájlban van. Lásd a [`.env.example`](.env.example) fájlt minden opcióhoz. A legfontosabbak:

| Setting | What it does |
| --- | --- |
| `BOT_TOKEN` | A Telegram bot tokened (a @BotFather-től) |
| `BOSS_ID` | A számodos Telegram felhasználói ID-d (a bot tulajdonosa) |
| `BOT_NAME` | A bot neve és ébresztő szava csoportokban (alapértelmezett `Vortex`) |
| `BOT_COUNTRY` | Ország angolul, pl. `United States` (időzóna, valuta, imádságidők beállítása) |
| `BOT_LANGUAGE` | Bot nyelvkód, pl. `en`, `fa`, `tr` (csak a bot válaszait változtatja) |
| `LLM_PROVIDERS` | LLM szolgáltatók és kulcsok: `base_url\|api_key\|model`, vesszővel elválasztva |
| `UPDATE_CHECK_ENABLED` | `1` = napi frissítésellenőrzés, `0` = soha nem ellenőriz |
| `UPDATE_REPO` | A figyelt release-ek repója (alapértelmezett `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Webes keresés: `searxng` (alapértelmezett), `tavily`, vagy `serper` |
| `DAILY_LIMIT_MESSAGES` | Max. bot válasz felhasználónként naponként (alapértelmezett `30`, a boss ki van zárva) |

Az országot és a nyelvet később is megváltoztathatod a rejtett `/admin` panelen (Nyelv és Ország), fájl szerkesztése nélkül.

## Docker alternatíva

Ha Docker-t preferálsz az installer helyett:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Ez elindítja a bott egy saját SearXNG keresőmotorral együtt. A logokat `docker compose logs -f bot` paranccsal követheted.

Megjegyzés: az automatikus önfrissítő a systemd szolgáltatást igényli, így Dockerben a frissítés manuális: `git pull` majd újra `docker compose up -d --build`.

## Funkciók részletesen

### Az `/admin` panel

Küldd el az `/admin` parancsot privát csevegésben (csak a boss — senki más nem nyithatja meg, és soha nem jelenik meg a `/help`-ben vagy a menükben). Tartalma:

- 🔑 **Tokenek és modell** — LLM kulcsok hozzáadása vagy eltávolítása, egészséges kulcsok megtekintése, aktív modell kiválasztása, szolgáltató élő modelllistájának böngészése
- 👥 **Felhasználók** — felhasználói statisztikák, kitiltás / feloldás, engedélyezett lista
- 📊 **Statisztikák** — használati adatok
- 💬 **Legutóbbi csevegések** — mit írtak az emberek a botnak (csak boss, privát)
- 🖼️ **Képmodell** — DuckAI (ingyenes, alapértelmezett), HiLinkUp, egyedi kép szolgáltatás, vagy kikapcsolva
- 🛡️ **Menedzserek** — megbízható embereknek részleges panelhozzáférés adása
- 🟢/🔴 **Üzem** — a bot be- vagy kikapcsolása mindenkinek (a boss továbbra is irányít)
- 🌍 **Nyelv és Ország** — a bot nyelvének vagy országának bármikor módosítása

### A token pool

A bot egyszerre tárolhat kulcsokat több LLM szolgáltatótól. Rotál az egészséges kulcsok között, és automatikusan átvesz, ha az egyik leáll. Az `/admin`-ból rögzíthetsz egy modellt, kézzel választhatsz, vagy hagyd, hogy a bot szabadon rotáljon. Bármely OpenAI-kompatibilis API-s szolgáltató működik — beleértve a kis aggregátorokat, nem csak a nagy neveket.

### Képek

A képgenerálás három módban működik: **DuckAI** (ingyenes, kulcs nélkül, alapértelmezett), **HiLinkUp** (fizetős, jobb minőség), vagy egy **egyedi** OpenAI-kompatibilis kép szolgáltatás. Elküldhetsz a botnak egy fotót is, és megmondhatod, hogyan szerkessze ("készíts belőle rajzfilm stílust"), és új képet generál. A képgenerálás kikapcsolható az `/admin`-ból.

### Országok és nyelvek

A Vortex **195 országot** és **40 nyelvet** támogat. Az ország beállítja az időzónát, a pénznemet, amiben az árak megjelennek, a várost az imádságidőkhöz, és a helyi tartalmakat. A nyelv csak azt határozza meg, mit mond a bot — például egy belgiai csoport használhatja az országot Belgiumet, a nyelvet pedig angolt. Mindkettőt később megváltoztathatod a `/admin` paranccsal.

### Frissítések

A bot naponta egyszer ellenőrzi a `VortexLabsHQ/vortex-telegram-bot` GitHub kiadásait. Ha új verzió érhető el, a gazdának privát üzenetet küld ✅ / ❌ gombokkal. Az elfogadás frissíti a kódot és újraindítja a botot. Amíg a repo privát, az ellenőrzés csendesen nem csinál semmit (a GitHub API publikus repót igényel) — állítsd be az `UPDATE_CHECK_ENABLED=0` értéket, ha soha nem akarod az ellenőrzést.

## Hibaelhárítás / GYIK

**A telepítő azt írja, hogy a tokenem érvénytelen.**
A token a [@BotFather](https://t.me/BotFather) oldalról származik. Győződj meg róla, hogy az egész token másolva van (számjegyek, egy kettőspont, majd 35+ karakter), felesleges szóközök nélkül. Ha törölted a botot vagy készítettél egy új tokent, a régi leáll — illeszd be az újat.

**A bot nem válaszol a csoportomban.**
Négy dolog, amit ellenőrizni kell: (1) A csoport adatvédelme ki kell legyen kapcsolva — a [@BotFather](https://t.me/BotFather)-ben küldd el a `/setprivacy` parancsot, válaszd ki a botodat, és válaszd a **Disable** opciót; ha az adatvédelem be van kapcsolva, a bot nem látja a csoport üzeneteit egyáltalán, (2) a botot hozzá kell adni a csoporthoz, (3) ki kell mondanod az ébresztő szót — a nevét, például `Vortex hány óra van?` — a bot csak akkor figyel, ha a nevét mondják ki a csoportokban, (4) privát csevegésben egyáltalán nem kell ébresztő szó.

**A bot angolul válaszol, nem a nyelvemen.**
Küldd el a `/admin` parancsot (csak a gazda) → Nyelv és Ország, és válaszd ki a nyelved. A telepítő is kérdezi a nyelvet — nyomj Entert ott az országod alapértelmezettének elfogadásához.

**Anthropic-ot választottam, de a bot nem cseveg.**
Az Anthropic natív API-ja nem OpenAI-kompatibilis, ezért a bot nem tud közvetlenül csevegni vele. Használd az OpenRoutert (ami OpenAI-kompatibilis API-n keresztül kiszolgálja a Claude modelleket), vagy válassz egy másik szolgáltatót a listából.

**A webes keresés nem működik.**
A webes keresés SearXNG-t igényel, amit a telepítő Dockerrel kínál fel. Nélküle a bot a Wikipédiára esik vissza, ami gyengébb. Beállíthatod a `.env` fájlban az `SEARCH_PROVIDER=tavily` vagy `serper` értéket `SEARCH_API_KEY` mellett is.

**Hol vannak a naplók?**
A `journalctl -u vortex-bot -f` mutatja az élő naplót. A `systemctl status vortex-bot` mutatja, fut-e a szolgáltatás. Ha a bot leáll, a `sudo systemctl restart vortex-bot` újraindítja.

**A bot azt írja, hogy elértem a napi limitet.**
Minden felhasználó naponta 30 bot-választ kap (a gazda mentes). A limit éjfélkor nullázódik a bot országának időzónájában. Növeld a `.env` fájlban a `DAILY_LIMIT_MESSAGES` értékkel, vagy kérdezd meg a gazdát.

**Hibát találtam / van egy ötletem.**
Kérlek, nyiss egy issue-t a GitHubon — lásd a [CONTRIBUTING.md](CONTRIBUTING.md) fájlt a jelentés módjáról és a javítás küldéséről.

## Fejlesztés

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

Futtasd a teszteket (egyszerű Python szkriptek, pytest nem kell):

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

Az összes kilenc tesztszolgáltatásnak át kell mennie, mielőtt pull requestet nyitnál. Lásd a [CONTRIBUTING.md](CONTRIBUTING.md) a kódstílusért (ruff) és a PR folyamatért.

## Licenc

A Vortex a [MIT licenc](LICENSE) alatt jelenik meg — ingyenesen használható, másolható, módosítható és megosztható bármilyen célra.

<a id="countries"></a>

## Országok

Illeszd be az ország nevét **angolul, pontosan ahogy itt szerepel**, amikor a telepítő megkérdezi az országodat. A táblázat a `bot/countries.py` fájlból generálódik — ha egy név itt és ott nem egyezik meg, a `bot/countries.py` dönt.

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

## Köszönet

> ⭐ **Kérjük, csillagozd meg ezt a projektet a GitHubon és kövesd a [@VortexLabsHQ](https://github.com/VortexLabsHQ) fiókot** — ez a legegyszerűbb módja a Vortex támogatásának és annak, hogy mások is megtalálják. Köszönjük!
