# Vortex 🤖 — Twój własny asystent grupy na Telegramie

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · **Polski** · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Jeśli podoba Ci się Vortex, polub ten projekt na GitHubie i obserwuj [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — to pomaga innym go znaleźć. Dziękuję!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Co to jest Vortex?

Vortex to bot na Telegramie, który przebywa w Twoich grupach i czatach prywatnych i odpowiada ludziom za pomocą modelu czatu AI. Wystarczy powiedzieć jego nazwę (domyślna nazwa to **Vortex**) i on odpisze — potrafi rozmawiać, szukać w sieci, tworzyć obrazy, sprawdzać ceny, opowiadać żarty, czytać pliki, transkrybować wiadomości głosowe i nie tylko.

Działa na Twoim własnym serwerze, w Twoim własnym kraju i języku. Ty jesteś szefem: ukryty panel `/admin` pozwala zarządzać kluczami AI, użytkownikami i ustawieniami.

## Funkcje

- 💬 **Czat AI** w grupach (słowo budzące) i czatach prywatnych (bez słowa budzącego)
- 🔑 **Pula tokenów** — używaj kilku dostawców LLM i kluczy, automatycznie rotuj i przełączaj w razie awarii
- 🖼️ **Generowanie i edycja obrazów** — darmowe (DuckAI) lub płatne dostawcy
- 🔍 **Wyszukiwanie w sieci** — samodzielnie hostowane SearXNG, z rezerwą Wikipedia
- 💰 **Ceny na żywo** — waluty, złoto, ropa i krypto w Twojej walucie lokalnej
- 🕌 **Czasy modlitw**, 🃏 **przepowiednie**, 😄 **kawałki**, 🎲 **rzuty kostką i monetą**
- 📎 **Analiza plików** i **transkrypcja głosu**
- 📥 **Pobieranie** — wyślij link, otrzymaj plik multimedialny z powrotem (do 45 MB)
- 🌍 **195 krajów** i **40 języki** — kraj i język to osobne ustawienia
- 🔄 **Samodzielna aktualizacja** — sprawdza nowe wydania codziennie i pyta przed aktualizacją
- 🛡️ **Ukryty panel /admin** — tokeny, użytkownicy, statystyki, czaty, model obrazu, menedżerzy, uprawnienia

## Przed instalacją

Potrzebujesz serwera (lub komputera, który pozostaje włączony) z systemem **Linux** i zainstalowanymi poniższymi elementami:

| Co | Jak sprawdzić | Co powinieneś zobaczyć |
| --- | --- | --- |
| **Python 3.11 lub nowszy** | `python3 --version` | `Python 3.11.x` lub nowszy (3.12 i 3.13 też działają) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` lub `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` lub podobny |
| **Docker** *(opcjonalnie)* | `docker --version` | `Docker version 2x.x.x` — potrzebne tylko, jeśli chcesz opcjonalną wyszukiwarkę internetową SearXNG |

Jeśli coś brakuje, instalator zaproponuje zainstalowanie tego za Ciebie za pomocą `apt` (na Debianie/Ubuntu). Na innych systemach zainstaluj to najpierw swoim menedżerem pakietów.

Potrzebujesz też dwóch rzeczy z Telegrama (obie są darmowe):

1. **Token bota** — napisz do [@BotFather](https://t.me/BotFather) na Telegramie, wyślij `/newbot` i skopiuj token, który otrzymasz.
2. **Twój numeryczny identyfikator użytkownika Telegrama** — napisz do [@userinfobot](https://t.me/userinfobot) i skopiuj wyświetloną liczbę. To Twój identyfikator "szefa": tylko to konto może używać `/admin`.

## Instalacja

Jedna komenda. Skopiuj ją, wklej w terminalu i naciśnij Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Instalator zadaje sześć pytań, w kolejności:

1. **Kraj** — wklej angielską nazwę swojego kraju **dokładnie tak, jak jest podana w [tabeli krajów](#countries) poniżej** (np. `Turkey`). Kraj ustawia strefę czasową, lokalną walutę dla cen, godziny modlitw i treści lokalne.
2. **Język** — język, którym mówi bot (np. `en`, `fa`, `tr`). Naciśnij Enter, aby zaakceptować domyślny dla Twojego kraju. Język jest oddzielny od kraju: zmienia tylko to, co mówi bot, i możesz go zmienić później z `/admin`.
3. **Token bota** — wklej token z [@BotFather](https://t.me/BotFather). Instalator sprawdza go na żywo z Telegramem.
4. **Numeryczne ID szefa** — Twoje ID użytkownika Telegram z [@userinfobot](https://t.me/userinfobot).
5. **Nazwa bota / słowo aktywujące** — nazwa, którą ludzie mówią w grupach, by porozmawiać z botem. Dowolny język jest OK (np. `Vortex` lub `ورتکس`). Naciśnij Enter dla domyślnej `Vortex`.
6. **Pierwszy dostawca LLM** — wybierz jeden: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere lub **Własny** (wklej bazowy URL). Następnie wklej swój klucz API dla tego dostawcy — instalator pobierze aktualną listę modeli dostawcy i wybierzesz model.

Następnie instalator instaluje zależności, zapisuje plik `.env`, tworzy usługę systemd `vortex-bot`, proponuje instalację SearXNG do wyszukiwania w sieci (wymaga Dockera) i uruchamia bota.

> ⚠️ **Anthropic nie działa bezpośrednio.** Natywne API Anthropic nie jest kompatybilne z OpenAI, a ten bot obsługuje tylko API kompatybilne z OpenAI. Jeśli wybierzesz Anthropic, instalator ostrzeże Cię: klucz zadziała tylko przez bramkę kompatybilną z OpenAI. Użyj zamiast tego OpenRoutera lub innego dostawcy z listy.

## Po instalacji

Sprawdź, czy bot działa:

```bash
systemctl status vortex-bot
```

Powinieneś zobaczyć `active (running)`. Aby obserwować logi na żywo:

```bash
journalctl -u vortex-bot -f
```

Teraz otwórz Telegram i porozmawiaj ze swoim botem:

- Wyślij `/start` — bot powita się.
- W **prywatnej rozmowie** po prostu napisz do niego — nie potrzebne jest słowo aktywujące.
- W **grupie** dodaj bota do grupy, a następnie powiedz jego nazwę, na przykład: `Vortex what's the time?`
- Jako szef, wyślij `/admin` w prywatnej rozmowie, aby otworzyć ukryty panel administratora.

**Aktualizacje są automatyczne.** Raz na dzień bot sprawdza na GitHubie, czy dostępna jest nowa wersja. Jeśli tak, wyśle Ci prywatną wiadomość z przyciskami ✅ / ❌. Naciśnij ✅, a bot zaktualizuje się sam i zrestartuje — nigdy nie musisz dotykać serwera.

## Konfiguracja

Wszystkie ustawienia znajdują się w pliku `.env` w katalogu instalacyjnym. Zobacz [`.env.example`](.env.example) dla pełnej listy opcji. Najważniejsze z nich:

| Ustawienie | Co robi |
| --- | --- |
| `BOT_TOKEN` | Twój token bota Telegram (od @BotFather) |
| `BOSS_ID` | Twój numeryczny ID użytkownika Telegram (właściciel bota) |
| `BOT_NAME` | Nazwa bota i słowo aktywujące w grupach (domyślnie `Vortex`) |
| `BOT_COUNTRY` | Kraj po angielsku, np. `United States` (ustawia strefę czasową, walutę, godziny modlitwy) |
| `BOT_LANGUAGE` | Kod języka bota, np. `en`, `fa`, `tr` (zmienia tylko to, co mówi bot) |
| `LLM_PROVIDERS` | Dostawcy LLM i klucze: `base_url\|api_key\|model`, rozdzielone przecinkami |
| `UPDATE_CHECK_ENABLED` | `1` = sprawdzaj aktualizacje codziennie, `0` = nigdy nie sprawdzaj |
| `UPDATE_REPO` | Repozytorium, którego wydania są obserwowane (domyślnie `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Wyszukiwanie w sieci: `searxng` (domyślnie), `tavily` lub `serper` |
| `DAILY_LIMIT_MESSAGES` | Maks. odpowiedzi bota na użytkownika dziennie (domyślnie `30`, boss jest zwolniony) |

Kraj i język można też zmienić później z ukrytego panelu `/admin` (Język i Kraj), bez edytowania żadnego pliku.

## Alternatywa Docker

Jeśli wolisz Docker zamiast instalatora:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

To uruchamia bota razem z samodzielnie hostowaną wyszukiwarką SearXNG. Sprawdź logi poleceniem `docker compose logs -f bot`.

Uwaga: automatyczny samouaktualniacz wymaga usługi systemd, więc w Dockerze aktualizacje są ręczne: `git pull` a potem ponownie `docker compose up -d --build`.

## Funkcje w szczegółach

### Panel /admin

Wyślij `/admin` na czacie prywatnym (tylko dla szefa — nikt inny nie może go otworzyć, i nigdy nie pojawia się w `/help` ani w menu). Zawiera:

- 🔑 **Tokeny i model** — dodawaj lub usuwaj klucze LLM, sprawdzaj, które klucze są sprawne, wybieraj aktywny model, przeglądaj listę modeli dostawcy na żywo
- 👥 **Użytkownicy** — liczba użytkowników, ban/odbanuj, lista dozwolonych
- 📊 **Statystyki** — dane o użyciu
- 💬 **Ostatnie czaty** — co ludzie napisali do bota (tylko szef, prywatnie)
- 🖼️ **Model obrazów** — DuckAI (darmowy, domyślny), HiLinkUp, własna usługa obrazów, lub wyłączony
- 🛡️ **Menedżerowie** — daj zaufanym osobom dostęp do części panelu
- 🟢/🔴 **Zasilanie** — włącz lub wyłącz bota dla wszystkich (szef zachowuje kontrolę)
- 🌍 **Język i kraj** — zmień język lub kraj bota w dowolnym momencie

### Pula tokenów

Bot może przechowywać klucze od kilku dostawców LLM naraz. Przełącza się między sprawnymi kluczami i automatycznie przejmuje, gdy jeden przestanie działać. Z `/admin` możesz przypiąć jeden model, wybrać model ręcznie, albo pozwolić botowi swobodnie się przełączać. Działa każdy dostawca z API kompatybilnym z OpenAI — także mniej znani agregatorzy, nie tylko duże nazwy.

### Obrazy

Generowanie obrazów ma trzy tryby: **DuckAI** (darmowy, bez klucza, domyślny), **HiLinkUp** (płatny, lepsza jakość), lub **własna** usługa obrazów kompatybilna z OpenAI. Możesz też wysłać botowi zdjęcie i powiedzieć, jak je edytować („zrób to w stylu kreskówki”), a on wygeneruje nowy obraz. Generowanie obrazów można wyłączyć z `/admin`.

### Kraje i języki

Vortex obsługuje **195 krajów** i **40 języki**. Kraj ustawia strefę czasową, walutę cen, miasto do czasów modlitwy i treści lokalne. Język określa tylko to, co mówi bot — grupa w Belgium może używać kraju Belgium i języka English, na przykład. Oba można zmienić później z `/admin`.

### Aktualizacje

Bot sprawdza wydania GitHub repozytorium `VortexLabsHQ/vortex-telegram-bot` raz dziennie. Gdy wyjdzie nowa wersja, prywatnie wysyła szefowi wiadomość z przyciskami ✅ / ❌. Zaakceptowanie aktualizuje kod i restartuje bota. Dopóki repozytorium jest prywatne, sprawdzanie cicho nic nie robi (API GitHuba wymaga publicznego repo) — ustaw `UPDATE_CHECK_ENABLED=0`, jeśli nigdy nie chcesz sprawdzania.

## Rozwiązywanie problemów / FAQ

**Instalator mówi, że mój token jest nieprawidłowy.**
Token pochodzi od [@BotFather](https://t.me/BotFather). Upewnij się, że skopiowałeś cały token (cyfry, dwukropek, potem 35+ znaków), bez dodatkowych spacji. Jeśli usunąłeś bota lub wygenerowałeś nowy token, stary przestaje działać — wklej nowy.

**Bot nie odpowiada w mojej grupie.**
Trzy rzeczy do sprawdzenia: (1) bot musi zostać dodany do grupy, (2) musisz powiedzieć jego słowo aktywujące — jego nazwę, na przykład `Vortex what's the time?` — bot nasłuchuje tylko gdy jego nazwa zostanie powiedziana w grupach, (3) w czacie prywatnym słowo aktywujące nie jest w ogóle potrzebne.

**Bot odpowiada po angielsku, a nie w moim języku.**
Wyślij `/admin` (tylko szef) → Język i kraj, i wybierz swój język. Instalator też pyta o język — tam naciśnij Enter, by zaakceptować domyślny dla twojego kraju.

**Wybrałem Anthropic, a bot nie rozmawia.**
Natywne API Anthropic nie jest kompatybilne z OpenAI, więc bot nie może z nim bezpośrednio rozmawiać. Użyj OpenRouter (który udostępnia modele Claude przez API kompatybilne z OpenAI), albo wybierz innego dostawcę z listy.

**Wyszukiwanie w sieci nie działa.**
Wyszukiwanie w sieci potrzebuje SearXNG, który instalator proponuje skonfigurować z Dockerem. Bez tego bot rezygnuje do Wikipedii, która jest słabsza. Możesz też ustawić `SEARCH_PROVIDER=tavily` albo `serper` z `SEARCH_API_KEY` w `.env`.

**Gdzie są logi?**
`journalctl -u vortex-bot -f` pokazuje logi na żywo. `systemctl status vortex-bot` pokazuje, czy usługa działa. Jeśli bot się zatrzyma, `sudo systemctl restart vortex-bot` uruchamia go ponownie.

**Bot mówi, że osiągnąłem dzienny limit.**
Każdy użytkownik dostaje 30 odpowiedzi bota dziennie (szef jest zwolniony). Limit resetuje się o północy w strefie czasowej kraju bota. Zwiększ go przez `DAILY_LIMIT_MESSAGES` w `.env`, albo zapytaj szefa.

**Znalazłem błąd / Mam pomysł.**
Proszę zgłoś problem na GitHubie — zobacz [CONTRIBUTING.md](CONTRIBUTING.md) jak to zrobić i jak wysłać poprawkę.

## Rozwój

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

Uruchom testy (zwykłe skrypty Python, pytest nie jest potrzebny):

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

Wszystkie dziewięć zestawów testów musi przejść zanim otworzysz pull request. Zobacz [CONTRIBUTING.md](CONTRIBUTING.md) dla stylu kodu (ruff) i procesu PR.

## Licencja

Vortex jest udostępniany na licencji [Licencja MIT](LICENSE) — wolny do użytku, kopiowania, modyfikowania i udostępniania w dowolnym celu.

## Kraje

Wklej nazwę kraju **po angielsku, dokładnie tak jak tutaj** gdy instalator zapyta o Twój kraj. Tabela jest generowana z pliku `bot/countries.py` — jeśli nazwa tutaj i tam się nie zgadza, wygrywa `bot/countries.py`.

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

## Dziękujemy

> ⭐ **Prosimy o polubienie tego projektu na GitHubie i śledzenie [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — to najprostszy sposób na wsparcie Vortex i pomoc innym w znalezieniu go. Dziękujemy!