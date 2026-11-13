# Vortex 🤖 — Ihr eigener Telegram-Gruppenassistent

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · **Deutsch** · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Wenn Ihnen Vortex gefällt, geben Sie diesem Projekt auf GitHub einen Stern und folgen Sie [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — das hilft mehr Menschen, es zu finden. Danke!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Was ist Vortex?

Vortex ist ein Telegram-Bot, der in Ihren Gruppen und privaten Chats lebt und mit einem KI-Chattmodell antwortet. Sie sagen seinen Namen (der Standardname ist **Vortex**) und er antwortet — er kann chatten, das Web durchsuchen, Bilder erstellen, Preise prüfen, Witze erzählen, Dateien lesen, Sprachnachrichten transkribieren und mehr.

Er läuft auf Ihrem eigenen Server, in Ihrem eigenen Land und in Ihrer Sprache. Sie sind der Chef: ein verstecktes `/admin`-Panel lässt Sie KI-Schlüssel, Nutzer und Einstellungen verwalten.

## Funktionen

- 💬 **KI-Chat** in Gruppen (Weckwort) und privaten Chats (kein Weckwort nötig)
- 🔑 **Token-Pool** — mehrere LLM-Anbieter und Schlüssel nutzen, automatisch rotieren und bei Ausfall umschalten
- 🖼️ **Bilderstellung und -bearbeitung** — kostenlos (DuckAI) oder kostenpflichtige Anbieter
- 🔍 **Websuche** — selbstgehostetes SearXNG, mit Wikipedia als Fallback
- 💰 **Live-Preise** — Währungen, Gold, Öl und Krypto in Ihrer Landeswährung
- 🕌 **Gebetszeiten**, 🃏 **Wahrsagerei**, 😄 **Witze**, 🎲 **Würfel und Münzwurf**
- 📎 **Dateianalyse** und **Sprachtranskription**
- 📥 **Downloads** — Link senden, Mediendatei zurückbekommen (bis 45 MB)
- 🌍 **195 Länder** und **40 Sprachen** — Land und Sprache sind getrennte Einstellungen
- 🔄 **Selbstaktualisierung** — prüft täglich auf neue Versionen und fragt vor dem Aktualisieren
- 🛡️ **Verstecktes /admin-Panel** — Tokens, Nutzer, Statistiken, Chats, Bildmodell, Manager, Ein/Aus

## Vor der Installation

Sie brauchen einen Server (oder einen Computer, der an bleibt) mit **Linux** und diesen installierten Programmen:

| Was | Wie prüfen | Was Sie sehen sollten |
| --- | --- | --- |
| **Python 3.11 oder neuer** | `python3 --version` | `Python 3.11.x` oder höher (3.12 und 3.13 funktionieren auch) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` oder `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` oder ähnlich |
| **Docker** *(optional)* | `docker --version` | `Docker version 2x.x.x` — nur nötig, wenn Sie die optionale SearXNG-Websuche wollen |

Falls etwas fehlt, installieren Sie alles mit einem Befehl (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Für das optionale Docker (nur erforderlich, wenn Sie die SearXNG-Websuche möchten):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Nach der letzten Zeile melden Sie sich ab und wieder an (oder führen Sie `docker`-Befehle mit `sudo` aus). Das Installationsprogramm bietet auch an, fehlende Tools für Sie mit `apt` unter Debian/Ubuntu zu installieren. Auf anderen Systemen installieren Sie diese zuerst mit Ihrem Paketmanager. `systemd` gehört zum System — es kann nicht separat installiert werden.

Sie brauchen auch zwei Dinge von Telegram (beide sind kostenlos):

1. **Einen Bot-Token** — sprechen Sie mit [@BotFather](https://t.me/BotFather) auf Telegram, senden Sie `/newbot`, und kopieren Sie den Token, den er Ihnen gibt.
2. **Ihre numerische Telegram-Benutzer-ID** — sprechen Sie mit [@userinfobot](https://t.me/userinfobot) und kopieren Sie die angezeigte Zahl. Das ist Ihre "Chef-ID": nur dieses Konto kann `/admin` nutzen.

## Installation

Ein Befehl. Kopieren Sie ihn, fügen Sie ihn in Ihr Terminal ein, und drücken Sie Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Der Installer fragt Sie sechs Dinge, in dieser Reihenfolge:

1. **Land** — fügen Sie den englischen Namen Ihres Landes **genau so ein, wie er in der [Ländertabelle](#countries) unten steht** (zum Beispiel `Turkey`). Das Land legt die Zeitzone, die lokale Währung für Preise, Gebetszeiten und lokale Inhalte fest.
2. **Sprache** — die Sprache, in der der Bot spricht (zum Beispiel `en`, `fa`, `tr`). Drücken Sie Enter, um den Standard für Ihr Land zu übernehmen. Sprache ist vom Land getrennt: sie ändert nur, was der Bot sagt, und Sie können sie später über `/admin` ändern.
3. **Bot-Token** — fügen Sie den Token von [@BotFather](https://t.me/BotFather) ein. Der Installer prüft ihn live mit Telegram.
4. **Chef-numerische ID** — Ihre Telegram-Benutzer-ID von [@userinfobot](https://t.me/userinfobot).
5. **Bot-Name / Weckwort** — der Name, den Leute in Gruppen sagen, um mit dem Bot zu sprechen. Jede Sprache ist okay (zum Beispiel `Vortex` oder `ورتکس`). Drücken Sie Enter für den Standard `Vortex`.
6. **Erster LLM-Anbieter** — wählen Sie einen: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, oder **Custom** (eigene Basis-URL eingeben). Dann fügen Sie Ihren API-Schlüssel für diesen Anbieter ein — der Installer holt die aktuelle Modellliste des Anbieters und Sie wählen ein Modell.

Dann installiert der Installer die Abhängigkeiten, schreibt die `.env`-Datei, erstellt den `vortex-bot`-systemd-Dienst, bietet an, SearXNG für die Websuche zu installieren (braucht Docker), und startet den Bot.

> ⚠️ **Anthropic funktioniert nicht direkt.** Anthropics native API ist nicht OpenAI-kompatibel, und dieser Bot spricht nur OpenAI-kompatible APIs. Wenn Sie Anthropic wählen, warnt der Installer: der Schlüssel funktioniert nur über ein OpenAI-kompatibles Gateway. Nutzen Sie OpenRouter oder einen anderen Anbieter aus der Liste.

## Nach der Installation

Prüfen Sie, ob der Bot läuft:

```bash
systemctl status vortex-bot
```

Sie sollten `active (running)` sehen. Um das Live-Log zu sehen:

```bash
journalctl -u vortex-bot -f
```

Öffnen Sie jetzt Telegram und sprechen Sie mit Ihrem Bot:

- Senden Sie `/start` — der Bot begrüßt Sie.
- In einem **privaten Chat** schreiben Sie einfach — kein Weckwort nötig.
- In einer **Gruppe**, füge den Bot der Gruppe hinzu, dann deaktiviere die Gruppenprivatsphäre: in [@BotFather](https://t.me/BotFather) send `/setprivacy`, wähle deinen Bot, und wähle **Disable** — andernfalls kann der Bot keine Gruppennachrichten sehen und hört sein Weckwort nicht. Dann sage seinen Namen, zum Beispiel: `Vortex wie spät ist es?`
- Als Chef senden Sie `/admin` in einem privaten Chat, um das versteckte Admin-Panel zu öffnen.

**Updates sind automatisch.** Einmal täglich prüft der Bot GitHub auf eine neue Version. Wenn eine verfügbar ist, sendet er Ihnen eine private Nachricht mit ✅ / ❌-Buttons. Tippen Sie ✅ und er aktualisiert sich selbst und startet neu — Sie müssen den Server nie anfassen.

## Konfiguration

Alle Einstellungen stehen in der `.env`-Datei im Installationsverzeichnis. Sehen Sie [`.env.example`](.env.example) für jede Option. Die wichtigsten:

| Einstellung | Was sie bewirkt |
| --- | --- |
| `BOT_TOKEN` | Ihr Telegram-Bot-Token (von @BotFather) |
| `BOSS_ID` | Ihre numerische Telegram-Benutzer-ID (der Bot-Besitzer) |
| `BOT_NAME` | Der Name und das Weckwort des Bots in Gruppen (Standard `Vortex`) |
| `BOT_COUNTRY` | Land auf Englisch, z. B. `United States` (legt Zeitzone, Währung, Gebetszeiten fest) |
| `BOT_LANGUAGE` | Bot-Sprachcode, z. B. `en`, `fa`, `tr` (ändert nur, was der Bot sagt) |
| `LLM_PROVIDERS` | LLM-Anbieter und Schlüssel: `base_url\|api_key\|model`, kommagetrennt |
| `UPDATE_CHECK_ENABLED` | `1` = täglich auf Updates prüfen, `0` = nie prüfen |
| `UPDATE_REPO` | Das Repository, dessen Releases beobachtet werden (Standard `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Websuche: `searxng` (Standard), `tavily`, oder `serper` |
| `DAILY_LIMIT_MESSAGES` | Max. Bot-Antworten pro Nutzer pro Tag (Standard `30`, Chef ist ausgenommen) |

Land und Sprache können auch später über das versteckte `/admin`-Panel (Sprache & Land) geändert werden, ohne Dateien zu bearbeiten.

## Docker-Alternative

Wenn Sie Docker dem Installer vorziehen:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Das startet den Bot zusammen mit einer selbstgehosteten SearXNG-Suchmaschine. Logs ansehen mit `docker compose logs -f bot`.

Hinweis: der automatische Selbst-Updater braucht den systemd-Dienst, daher sind Updates in Docker manuell: `git pull` und dann `docker compose up -d --build` erneut.

## Funktionen im Detail

### Das /admin-Panel

Senden Sie `/admin` in einem privaten Chat (nur Chef — niemand sonst kann es öffnen, und es taucht nie in `/help` oder den Menüs auf). Es hat:

- 🔑 **Tokens & Modell** — LLM-Schlüssel hinzufügen oder entfernen, sehen welche Schlüssel gesund sind, aktives Modell wählen, Live-Modellliste eines Anbieters durchsuchen
- 👥 **Nutzer** — Nutzerzahlen, sperren / entsperren, Allowlist
- 📊 **Statistiken** — Nutzungszahlen
- 💬 **Letzte Chats** — was Leute dem Bot gesagt haben (nur Chef, privat)
- 🖼️ **Bildmodell** — DuckAI (kostenlos, Standard), HiLinkUp, eigener Bilddienst, oder aus
- 🛡️ **Manager** — vertrauenswürdigen Leuten Zugriff auf Teile des Panels geben
- 🟢/🔴 **Ein/Aus** — Bot für alle an- oder ausschalten (Chef behält die Kontrolle)
- 🌍 **Sprache & Land** — Bot-Sprache oder -Land jederzeit ändern

### Der Token-Pool

Der Bot kann Schlüssel von mehreren LLM-Anbietern gleichzeitig halten. Er rotiert zwischen gesunden Schlüsseln und schaltet automatisch um, wenn einer aufhört zu funktionieren. Über `/admin` können Sie ein Modell festlegen, eines manuell wählen, oder den Bot frei rotieren lassen. Jeder Anbieter mit einer OpenAI-kompatiblen API funktioniert — auch kleine Aggregatoren, nicht nur die großen Namen.

### Bilder

Bilderstellung hat drei Modi: **DuckAI** (kostenlos, kein Schlüssel, Standard), **HiLinkUp** (kostenpflichtig, bessere Qualität), oder ein **eigener** OpenAI-kompatibler Bilddienst. Sie können dem Bot auch ein Foto senden und sagen, wie er es bearbeiten soll ("mach das im Cartoon-Stil"), und er erstellt ein neues Bild. Bilderstellung ist über `/admin` abschaltbar.

### Länder und Sprachen

Vortex unterstützt **195 Länder** und **40 Sprachen**. Das Land legt die Zeitzone fest, die Währung für Preise, die Stadt für Gebetszeiten und lokale Inhalte. Die Sprache legt nur fest, was der Bot sagt — eine Gruppe in Belgien kann das Land Belgien und die Sprache Englisch nutzen, zum Beispiel. Beides lässt sich später über `/admin` ändern.

### Updates

Der Bot prüft einmal täglich die GitHub-Releases von `VortexLabsHQ/vortex-telegram-bot`. Wenn eine neue Version da ist, schreibt er dem Chef privat mit ✅ / ❌-Buttons. Bei Annahme aktualisiert er den Code und startet den Bot neu. Solange das Repository privat ist, tut die Prüfung stillschweigend nichts (GitHubs API braucht ein öffentliches Repo) — setzen Sie `UPDATE_CHECK_ENABLED=0`, wenn Sie die Prüfung nie wollen.

## Fehlerbehebung / FAQ

**Der Installer sagt, mein Token sei ungültig.**
Der Token kommt von [@BotFather](https://t.me/BotFather). Stellen Sie sicher, dass Sie den ganzen Token kopiert haben (Ziffern, ein Doppelpunkt, dann 35+ Zeichen), ohne zusätzliche Leerzeichen. Wenn Sie den Bot gelöscht oder einen neuen Token erstellt haben, funktioniert der alte nicht mehr — fügen Sie den neuen ein.

**Der Bot antwortet in meiner Gruppe nicht.**
Vier Dinge zu prüfen: (1) Gruppenprivatsphäre muss deaktiviert sein — in [@BotFather](https://t.me/BotFather) send `/setprivacy`, wähle deinen Bot, und wähle **Disable**; bei aktivierter Privatsphäre kann der Bot überhaupt keine Gruppennachrichten sehen, (2) der Bot muss der Gruppe hinzugefügt werden, (3) du musst sein Weckwort sagen — seinen Namen, zum Beispiel `Vortex wie spät ist es?` — der Bot hört nur, wenn sein Name in Gruppen genannt wird, (4) in einem privaten Chat ist kein Weckwort erforderlich.

**Der Bot antwortet auf Englisch, nicht in meiner Sprache.**
Senden Sie `/admin` (nur Chef) → Sprache & Land, und wählen Sie Ihre Sprache. Der Installer fragt auch nach der Sprache — drücken Sie dort Enter, um den Standard Ihres Landes zu übernehmen.

**Ich habe Anthropic gewählt und der Bot chattet nicht.**
Anthropics native API ist nicht OpenAI-kompatibel, daher kann der Bot nicht direkt damit chatten. Nutzen Sie OpenRouter (das Claude-Modelle über eine OpenAI-kompatible API anbieten kann), oder wählen Sie einen anderen Anbieter aus der Liste.

**Websuche funktioniert nicht.**
Websuche braucht SearXNG, das der Installer mit Docker anbietet. Ohne fällt der Bot auf Wikipedia zurück, was schwächer ist. Sie können auch `SEARCH_PROVIDER=tavily` oder `serper` mit einem `SEARCH_API_KEY` in `.env` setzen.

**Wo sind die Logs?**
`journalctl -u vortex-bot -f` zeigt das Live-Log. `systemctl status vortex-bot` zeigt, ob der Dienst läuft. Wenn der Bot stoppt, startet `sudo systemctl restart vortex-bot` ihn neu.

**Der Bot sagt, ich habe das Tageslimit erreicht.**
Jeder Nutzer bekommt 30 Bot-Antworten pro Tag (der Chef ist ausgenommen). Das Limit setzt sich um Mitternacht in der Zeitzone des Bot-Landes zurück. Erhöhen Sie es mit `DAILY_LIMIT_MESSAGES` in `.env`, oder fragen Sie den Chef.

**Ich habe einen Bug gefunden / ich habe eine Idee.**
Eröffnen Sie bitte ein Issue auf GitHub — sehen Sie [CONTRIBUTING.md](CONTRIBUTING.md) dafür, wie man es meldet und wie man einen Fix einsendet.

## Entwicklung

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

Tests ausführen (einfache Python-Skripte, kein pytest nötig):

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

Alle neun Test-Suiten müssen bestehen, bevor Sie einen Pull Request öffnen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für den Code-Stil (ruff) und den PR-Prozess.

## Lizenz

Vortex wird unter der [MIT-Lizenz](LICENSE) veröffentlicht — frei zu nutzen, kopieren, ändern und teilen, für jeden Zweck.

<a id="countries"></a>

## Länder

Fügen Sie den Ländernamen **auf Englisch, genau so wie hier geschrieben** ein, wenn der Installer nach Ihrem Land fragt. Die Tabelle wird aus `bot/countries.py` generiert — falls ein Name hier und einer dort je abweichen, gewinnt `bot/countries.py`.

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



## Danke

> ⭐ **Bitte geben Sie diesem Projekt auf GitHub einen Stern und folgen Sie [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — das ist der einfachste Weg, Vortex zu unterstützen und anderen zu helfen, es zu finden. Danke!
