# Vortex 🤖 — Váš vlastní asistent pro Telegramové skupiny

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · **Čeština** · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Pokud se vám Vortex líbí, prosím, dejte projektu hvězdičku na GitHubu a sledujte [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — pomůže to více lidem ho najít. Děkuji!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Co je Vortex?

Vortex je Telegram bot, který žije ve vašich skupinách a soukromých chatech a odpovídá lidem pomocí AI chatového modelu. Řeknete jeho jméno (výchozí jméno je **Vortex**) a on odpoví — umí chatovat, vyhledávat na webu, generovat obrázky, kontrolovat ceny, vyprávět vtipy, číst soubory, přepisovat hlasové zprávy a další.

Běží na vašem vlastním serveru, ve vaší zemi a jazyce. Vy jste šéf: skrytý panel `/admin` vám umožňuje spravovat AI klíče, uživatele a nastavení.

## Funkce

- 💬 **AI chat** ve skupinách (slovo pro probouzení) a soukromých chatech (slovo pro probouzení nepotřebné)
- 🔑 **Token pool** — používejte několik LLM poskytovatelů a klíčů, automaticky se střídají a přepínají při selhání
- 🖼️ **Generování a úprava obrázků** — zdarma (DuckAI) nebo placení poskytovatelé
- 🔍 **Vyhledávání na webu** — self-hosted SearXNG, se záložním Wikipedia
- 💰 **Aktuální ceny** — měny, zlato, ropa a krypto ve vaší místní měně
- 🕌 **Časy modliteb**, 🃏 **předpovědi**, 😄 **vtipy**, 🎲 **hody kostkou a mince**
- 📎 **Analýza souborů** a **přepis hlasu**
- 📥 **Stahování** — pošlete odkaz, získejte mediální soubor zpět (až 45 MB)
- 🌍 **195 zemí** a **40 jazyků** — země a jazyk jsou oddělená nastavení
- 🔄 **Samostatné aktualizace** — kontroluje nové vydání denně a ptá se před aktualizací
- 🛡️ **Skrytý /admin panel** — tokeny, uživatelé, statistiky, chaty, obrazový model, manažeři, moc

## Před instalací

Potřebujete server (nebo počítač, který zůstaně zapnutý) s běžícím **Linuxem** a nainstalovanými těmito věcmi:

| Co | Jak zkontrolovat | Co byste měli vidět |
| --- | --- | --- |
| **Python 3.11 nebo novější** | `python3 --version` | `Python 3.11.x` nebo vyšší (3.12 a 3.13 fungují taky) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` nebo `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` nebo podobné |
| **Docker** *(volitelné)* | `docker --version` | `Docker version 2x.x.x` — potřebné jen pokud chcete volitelné vyhledávání SearXNG |

Pokud něco chybí, nainstalujte to vše jedním příkazem (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Pro volitelný `Docker` (potřebný pouze pokud chcete vyhledávání na webu `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Po posledním řádku se odhlaste a přihlaste se znovu (nebo spouštějte příkazy `docker` s `sudo`). Instalátor také nabídne nainstalovat chybějící nástroje za vás pomocí `apt` na `Debian/Ubuntu`. Na jiných systémech je nainstalujte nejprve pomocí svého správce balíčků. `systemd` je součástí systému — nelze ho nainstalovat samostatně.

Také potřebujete dvě věci od Telegramu (obě jsou zdarma):

1. **Token bota** — napište [@BotFather](https://t.me/BotFather) na Telegramu, pošlete `/newbot` a zkopírujte token, který vám dá.
2. **Vaše číselné Telegram ID** — napište [@userinfobot](https://t.me/userinfobot) a zkopírujte číslo, které vám ukáže. Toto je vaše "šéfové" ID: pouze tento účet může používat `/admin`.

## Instalace

Jeden příkaz. Zkopírujte ho, vložte do terminálu a stiskněte Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Instalátor vás zeptá na šest otázek, po řadě:

1. **Země** — vložte anglický název vaší země **přesně tak, jak je uveden v [tabulce zemí](#countries) níže** (např. `Turkey`). Země nastavuje časové pásmo, místní měnu pro ceny, časy modliteb a lokální obsah.
2. **Jazyk** — jazyk, kterým bot mluví (např. `en`, `fa`, `tr`). Stiskněte Enter pro přijetí výchozí hodnoty pro vaši zemi. Jazyk je oddělený od země: mění jen to, co bot říká, a můžete ho později změnit přes `/admin`.
3. **Token bota** — vložte token od [@BotFather](https://t.me/BotFather). Instalátor ho ověří přímo s Telegramem.
4. **Číselné ID šéfa** — vaše Telegram ID od [@userinfobot](https://t.me/userinfobot).
5. **Název bota / probudí slovo** — jméno, které lidé ve skupinách řeknou, aby bota adresovali. Jakýkoli jazyk je v pořádku (např. `Vortex` nebo `ورتکس`). Stiskněte Enter pro výchozí `Vortex`.
6. **První LLM poskytovatel** — vyberte jeden: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, nebo **Vlastní** (vložte základní URL). Pak vložte svůj API klíč pro daného poskytovatele — instalátor stáhne živý seznam modelů a vy si vyberete model.

Poté instalátor nainstaluje závislosti, zapíše soubor `.env`, vytvoří systemd službu `vortex-bot`, nabídne instalaci SearXNG pro webové vyhledávání (vyžaduje Docker) a spustí bota.

> ⚠️ **Anthropic nefunguje přímo.** Nativní API Anthropic není kompatibilní s OpenAI, a tento bot umí mluvit jen OpenAI-kompatibilními API. Pokud vyberete Anthropic, instalátor vás upozorní: klíč funguje jen přes OpenAI-kompatibilní bránu. Místo toho použijte OpenRouter nebo jiného poskytovatele ze seznamu.

## Po instalaci

Zkontrolujte, že bot běží:

```bash
systemctl status vortex-bot
```

Měli byste vidět `active (running)`. Pro sledování živého logu:

```bash
journalctl -u vortex-bot -f
```

Teď otevřete Telegram a povídejte si s botem:

- Pošlete `/start` — bot vás pozdraví.
- V **privátním chatu** jen pište — probudí slovo není potřeba.
- Ve **skupině** přidejte bota do skupiny, pak vypněte Skupinovou soukromí: v [@BotFather](https://t.me/BotFather) pošlete `/setprivacy`, vyberte svého bota a zvolte **Disable** — jinak bot neuvidí skupinové zprávy a neslyší své probuzovací slovo. Pak řekněte jeho jméno, například: `Vortex what's the time?`
- Jako šéf pošlete `/admin` v privátním chatu pro otevření skrytého admin panelu.

**Aktualizace jsou automatické.** Jednou denně bot zkontroluje GitHub na novou verzi. Pokud je k dispozici, pošle vám privátní zprávu s tlačítky ✅ / ❌. Stiskněte ✅ a bot se sám aktualizuje a restartuje — nikdy nemusíte sahat na server.

## Konfigurace

Všechna nastavení jsou v souboru `.env` v instalačním adresáři. Viz [`.env.example`](.env.example) pro všechny volby. Nejdůležitější z nich:

| Setting | Co dělá |
| --- | --- |
| `BOT_TOKEN` | Token vašeho Telegram bota (od @BotFather) |
| `BOSS_ID` | Vaše číselné Telegram ID (vlastník bota) |
| `BOT_NAME` | Jméno bota a slovní spoušť ve skupinách (výchozí `Vortex`) |
| `BOT_COUNTRY` | Země v angličtině, např. `United States` (nastaví časové pásmo, měnu, časy modlitby) |
| `BOT_LANGUAGE` | Kód jazyka bota, např. `en`, `fa`, `tr` (mění jen to, co bot říká) |
| `LLM_PROVIDERS` | Poskytovatelé LLM a klíče: `base_url\|api_key\|model`, oddělené čárkou |
| `UPDATE_CHECK_ENABLED` | `1` = kontrolovat aktualizace denně, `0` = nikdy nekontrolovat |
| `UPDATE_REPO` | Repozitář, jehož release se sledují (výchozí `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Vyhledávání na webu: `searxng` (výchozí), `tavily`, nebo `serper` |
| `DAILY_LIMIT_MESSAGES` | Max. odpovědí bota na uživatele denně (výchozí `30`, boss je vyloučen) |

Zemi i jazyk můžete později změnit i ze skrytého panelu `/admin` (Jazyk & Země), aniž byste editovali jakýkoli soubor.

## Docker alternativa

Pokud dáváte přednost Dockeru před instalátorem:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Toto spustí bota spolu se samohostovaným vyhledávačem SearXNG. Logy zkontrolujete přes `docker compose logs -f bot`.

Poznámka: automatický self-updater vyžaduje systemd službu, takže v Dockeru jsou aktualizace manuální: `git pull` a pak znovu `docker compose up -d --build`.

## Funkce podrobně

### Panel `/admin`

Pošlete `/admin` v privátním chatu (pouze boss — nikdo jiný ho nemůže otevřít, a nikdy se neobjeví v `/help` ani v menu). Obsahuje:

- 🔑 **Tokeny & model** — přidání nebo odebrání LLM klíčů, zobrazení zdravých klíčů, výběr aktivního modelu, prohlížení živého seznamu modelů poskytovatele
- 👥 **Uživatelé** — počty uživatelů, ban / unban, allowlist
- 📊 **Statistiky** — čísla využití
- 💬 **Nedávné chaty** — co lidé napsali botovi (pouze boss, privátně)
- 🖼️ **Obrazový model** — DuckAI (zdarma, výchozí), HiLinkUp, vlastní obrazová služba, nebo vypnuto
- 🛡️ **Manažeři** — důvěryhodným lidem povolíte přístup k částem panelu
- 🟢/🔴 **Zap/Vyp** — zapne nebo vypne bota pro všechny (boss zůstává v kontrole)
- 🌍 **Jazyk & Země** — změna jazyka nebo země bota kdykoli

### Fond tokenů

Bot může držet klíče od několika LLM poskytovatelů najednou. Rotuje mezi zdravými klíči a automaticky přepne na zálohu, když jeden přestane fungovat. Z `/admin` můžete zamknout jeden model, vybrat model ručně, nebo nechat bota volně rotovat. Funguje jakýkoli poskytovatel s OpenAI-kompatibilním API — včetně malých agregátorů, nejen velkých jmen.

### Obrázky

Generování obrázků má tři režimy: **DuckAI** (zdarma, bez klíče, výchozí), **HiLinkUp** (placený, lepší kvalita), nebo **vlastní** OpenAI-kompatibilní obrazovou službu. Můžete botovi poslat fotku a říct mu, jak ji upravit ("udělej z toho kreslený styl"), a on vygeneruje nový obrázek. Generování obrázků jde z `/admin` vypnout.

### Země a jazyky

Vortex podporuje **195 zemí** a **40 jazyků**. Země nastavuje časové pásmo, měnu, ve které se ukazují ceny, město používané pro modlitby a lokální obsah. Jazyk určuje jen to, co bot říká — skupina v Belgii může mít zemi Belgii a jazyk angličtinu, například. Obě se dají změnit později přes `/admin`.

### Aktualizace

Bot každý den zkontroluje GitHub releases repozitáře `VortexLabsHQ/vortex-telegram-bot`. Když vyjde nová verze, pošle šéfovi soukromou zprávu s tlačítky ✅ / ❌. Potvrzení aktualizuje kód a restartuje bot. Dokud je repozitář privátní, kontrola tiše nic nedělá (GitHub API vyžaduje veřejný repo) — nastavte `UPDATE_CHECK_ENABLED=0`, pokud kontrolu nikdy nechcete.

## Řešení problémů / FAQ

**Instalátor hlásí, že můj token je neplatný.**
Token získáte od [@BotFather](https://t.me/BotFather). Ujistěte se, že jste zkopírovali celý token (číslice, dvojtečka, pak 35+ znaků), bez nadbytečných mezer. Pokud jste bota smazali nebo vytvořili nový token, starý přestane fungovat — vložte ten nový.

**Bot neodpovídá ve skupině.**
Čtyři věci, které zkontrolovat: (1) Skupinová soukromí musí být vypnuté — v [@BotFather](https://t.me/BotFather) pošlete `/setprivacy`, vyberte svého bota a zvolte **Disable**; se zapnutou soukromím bot neuvidí žádné skupinové zprávy, (2) bot musí být přidán do skupiny, (3) musíte říct jeho probuzovací slovo — jeho jméno, například `Vortex what's the time?` — bot naslouchá pouze když je jeho jméno zmíněno ve skupinách, (4) v soukromém chatu není probuzovací slovo vůbec potřeba.

**Bot odpovídá v angličtině, ne v mém jazyce.**
Pošlete `/admin` (jen šéf) → Jazyk & Země, a vyberte svůj jazyk. Instalátor se také ptá na jazyk — tam stiskněte Enter pro přijetí výchozího nastavení vaší země.

**Vybral jsem Anthropic a bot nechatuje.**
Nativní API Anthropic není kompatibilní s OpenAI, takže bot s ním nemůže chatovat přímo. Použijte OpenRouter (který umí servírovat modely Claude přes OpenAI-kompatibilní API), nebo vyberte jiného poskytovatele ze seznamu.

**Vyhledávání na webu nefunguje.**
Vyhledávání na webu potřebuje SearXNG, který instalátor nabídne nastavit přes Docker. Bez něj bot upadne na Wikipedii, která je slabší. Můžete také nastavit `SEARCH_PROVIDER=tavily` nebo `serper` s `SEARCH_API_KEY` v `.env`.

**Kde jsou logy?**
`journalctl -u vortex-bot -f` ukazuje živý log. `systemctl status vortex-bot` ukazuje, jestli služba běží. Pokud bot zastaví, `sudo systemctl restart vortex-bot` ho zase spustí.

**Bot hlásí, že jsem dosáhl denního limitu.**
Každý uživatel dostane 30 odpovědí bota denně (šéf je vyjmut). Limit se resetuje v půlnoci v časovém pásmu země bota. Zvyšte ho pomocí `DAILY_LIMIT_MESSAGES` v `.env`, nebo se zeptejte šéfa.

**Našel jsem chybu / mám nápad.**
Prosím, otevřete issue na GitHubu — viz [CONTRIBUTING.md](CONTRIBUTING.md) pro to, jak to nahlásit a jak poslat opravu.

## Vývoj

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

Spusťte testy (obyčejné Python skripty, pytest není potřeba):

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

Vše devět sad musí projít, než otevřete pull request. Viz [CONTRIBUTING.md](CONTRIBUTING.md) pro styl kódu (ruff) a proces PR.

## Licence

Vortex je vydán pod [MIT licencí](LICENSE) — volné k použití, kopírování, úpravám a sdílení pro jakýkoli účel.

<a id="countries"></a>

## Země

Vložte název země **v angličtině, přesně tak, jak je zde uveden**, když vás instalátor zeptá na vaši zemi. Tabulka je generována z `bot/countries.py` — pokud se název zde a tam neshoduje, `bot/countries.py` vyhrává.

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

## Děkuji

> ⭐ **Prosím, dejte hvězdičku tomuto projektu na GitHubu a sledujte [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — je to nejjednodušší způsob, jak podpořit Vortex a pomoci ostatním ho najít. Děkuji!
