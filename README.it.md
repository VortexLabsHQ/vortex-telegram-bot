# Vortex 🤖 — Il tuo assistente Telegram per gruppi

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · **Italiano** · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Se ti piace Vortex, metti una stella a questo progetto su GitHub e segui [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — aiuta più persone a trovarlo. Grazie!

[![Licenza: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Cos'è Vortex?

Vortex è un bot Telegram che vive nei tuoi gruppi e chat private e risponde alle persone con un modello di chat AI. Dici il suo nome (il nome predefinito è **Vortex**) e lui risponde — può chattare, cercare sul web, creare immagini, controllare prezzi, raccontare barzellette, leggere file, trascrivere messaggi vocali e altro ancora.

Gira sul tuo server, nel tuo paese e nella tua lingua. Sei tu il capo: un pannello `/admin` nascosto ti permette di gestire chiavi AI, utenti e impostazioni.

## Funzionalità

- 💬 **Chat AI** nei gruppi (parola di attivazione) e chat private (nessuna parola di attivazione necessaria)
- 🔑 **Pool di token** — usa diversi provider LLM e chiavi, ruota e fa failover automaticamente
- 🖼️ **Generazione e modifica immagini** — gratis (DuckAI) o provider a pagamento
- 🔍 **Ricerca web** — SearXNG self-hosted, con fallback a Wikipedia
- 💰 **Prezzi in tempo reale** — valute, oro, petrolio e crypto nella tua valuta locale
- 🕌 **Orari di preghiera**, 🃏 **fortune**, 😄 **barzellette**, 🎲 **dadi e lancio moneta**
- 📎 **Analisi file** e **trascrizione vocale**
- 📥 **Download** — invia un link, ricevi il file multimediale (fino a 45 MB)
- 🌍 **195 paesi** e **40 lingue** — paese e lingua sono impostazioni separate
- 🔄 **Auto-aggiornamento** — controlla nuove release ogni giorno e chiede prima di aggiornare
- 🛡️ **Pannello /admin nascosto** — token, utenti, statistiche, chat, modello immagine, manager, accensione

## Prima di installare

Ti serve un server (o un computer che resta acceso) con **Linux** e questi programmi installati:

| Cosa | Come verificare | Cosa dovresti vedere |
| --- | --- | --- |
| **Python 3.11 o superiore** | `python3 --version` | `Python 3.11.x` o superiore (3.12 e 3.13 vanno bene) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` o `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` o simile |
| **Docker** *(opzionale)* | `docker --version` | `Docker version 2x.x.x` — serve solo se vuoi la ricerca web SearXNG opzionale |

Se manca qualcosa, installalo tutto con un unico comando (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Per il `Docker` opzionale (necessario solo se vuoi la ricerca web di `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Dopo l'ultima riga, esci e rientra (oppure esegui i comandi `docker` con `sudo`). Il programma di installazione propone anche di installare gli strumenti mancanti per te con `apt` su `Debian/Ubuntu`. Su altri sistemi, installali prima con il tuo gestore di pacchetti. `systemd` è incluso nel sistema — non può essere installato separatamente.

Ti servono anche due cose da Telegram (entrambe gratis):

1. **Un token bot** — parla con [@BotFather](https://t.me/BotFather) su Telegram, manda `/newbot` e copia il token che ti dà.
2. **Il tuo ID utente Telegram numerico** — parla con [@userinfobot](https://t.me/userinfobot) e copia il numero che ti mostra. È il tuo ID "capo": solo questo account può usare `/admin`.

## Installa

Un comando. Copialo, incollalo nel terminale e premi Invio:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

L'installer ti fa sei domande, in ordine:

1. **Paese** — incolla il nome inglese del tuo paese **esattamente come scritto nella [tabella paesi](#countries) qui sotto** (per esempio `Turkey`). Il paese imposta il fuso orario, la valuta locale per i prezzi, gli orari di preghiera e i contenuti locali.
2. **Lingua** — la lingua che parla il bot (per esempio `en`, `fa`, `tr`). Premi Invio per accettare quella predefinita del tuo paese. La lingua è separata dal paese: cambia solo cosa dice il bot, e puoi cambiarla dopo da `/admin`.
3. **Token bot** — incolla il token da [@BotFather](https://t.me/BotFather). L'installer lo verifica in diretta con Telegram.
4. **ID numerico capo** — il tuo ID utente Telegram da [@userinfobot](https://t.me/userinfobot).
5. **Nome bot / parola di attivazione** — il nome che la gente dice nei gruppi per parlare col bot. Qualsiasi lingua va bene (per esempio `Vortex` o `ورتکس`). Premi Invio per il default `Vortex`.
6. **Primo provider LLM** — scegline uno: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, o **Custom** (incolla un URL base). Poi incolla la tua API key per quel provider — l'installer scarica la lista modelli live del provider e ne scegli uno.

Poi l'installer installa le dipendenze, scrive il file `.env`, crea il servizio systemd `vortex-bot`, si offre di installare SearXNG per la ricerca web (serve Docker), e avvia il bot.

> ⚠️ **Anthropic non funziona direttamente.** L'API nativa di Anthropic non è compatibile con OpenAI, e questo bot parla solo API compatibili OpenAI. Se scegli Anthropic, l'installer ti avverte: la chiave funziona solo tramite un gateway compatibile OpenAI. Usa OpenRouter, o un altro provider dalla lista.

## Dopo l'installazione

Controlla che il bot giri:

```bash
systemctl status vortex-bot
```

Dovresti vedere `active (running)`. Per vedere il log in diretta:

```bash
journalctl -u vortex-bot -f
```

Ora apri Telegram e parla col tuo bot:

- Manda `/start` — il bot saluta.
- In **chat privata**, scrivigli e basta — niente parola di attivazione.
- In un **gruppo**, aggiungi il bot al gruppo, poi disattiva la Privacy del gruppo: in [@BotFather](https://t.me/BotFather) invia `/setprivacy`, seleziona il tuo bot e scegli **Disable** — altrimenti il bot non può vedere i messaggi del gruppo e non sentirà la sua parola di attivazione. Poi pronuncia il suo nome, ad esempio: `Vortex che ore sono?`
- Come capo, manda `/admin` in chat privata per aprire il pannello admin nascosto.

**Gli aggiornamenti sono automatici.** Una volta al giorno il bot controlla GitHub per una nuova release. Se c'è, ti manda un messaggio privato con pulsanti ✅ / ❌. Premi ✅ e si aggiorna da solo e riparte — non devi mai toccare il server.

## Configurazione

Tutte le impostazioni stanno nel file `.env` nella cartella d'installazione. Vedi [`.env.example`](.env.example) per ogni opzione. Le più importanti:

| Impostazione | Cosa fa |
| --- | --- |
| `BOT_TOKEN` | Il tuo token bot Telegram (da @BotFather) |
| `BOSS_ID` | Il tuo ID utente Telegram numerico (il proprietario del bot) |
| `BOT_NAME` | Il nome del bot e parola di attivazione nei gruppi (default `Vortex`) |
| `BOT_COUNTRY` | Paese in inglese, es. `United States` (imposta fuso orario, valuta, orari preghiera) |
| `BOT_LANGUAGE` | Codice lingua del bot, es. `en`, `fa`, `tr` (cambia solo cosa dice il bot) |
| `LLM_PROVIDERS` | Provider e chiavi LLM: `base_url\|api_key\|model`, separati da virgola |
| `UPDATE_CHECK_ENABLED` | `1` = controlla aggiornamenti ogni giorno, `0` = non controllare mai |
| `UPDATE_REPO` | La repo di cui si guardano le release (default `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Ricerca web: `searxng` (default), `tavily`, o `serper` |
| `DAILY_LIMIT_MESSAGES` | Max risposte bot per utente al giorno (default `30`, il capo è esente) |

Paese e lingua si possono cambiare anche dopo dal pannello `/admin` nascosto (Lingua e Paese), senza modificare file.

## Alternativa Docker

Se preferisci Docker all'installer:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Questo avvia il bot insieme a un motore di ricerca SearXNG self-hosted. Controlla i log con `docker compose logs -f bot`.

Nota: l'auto-aggiornatore serve il servizio systemd, quindi in Docker gli aggiornamenti sono manuali: `git pull` e poi `docker compose up -d --build` di nuovo.

## Funzionalità in dettaglio

### Il pannello /admin

Manda `/admin` in chat privata (solo il capo — nessun altro può aprirlo, e non appare mai in `/help` o nei menu). Ha:

- 🔑 **Token e modello** — aggiungi o rimuovi chiavi LLM, vedi quali chiavi sono sane, scegli il modello attivo, sfoglia la lista modelli live di un provider
- 👥 **Utenti** — contatori utenti, ban / unban, allowlist
- 📊 **Statistiche** — numeri di utilizzo
- 💬 **Chat recenti** — cosa ha detto la gente al bot (solo il capo, privato)
- 🖼️ **Modello immagine** — DuckAI (gratis, default), HiLinkUp, un servizio immagini custom, o spento
- 🛡️ **Manager** — dai a persone fidate l'accesso a parti del pannello
- 🟢/🔴 **Accensione** — accendi o spegni il bot per tutti (il capo resta al comando)
- 🌍 **Lingua e Paese** — cambia la lingua o il paese del bot quando vuoi

### Il pool di token

Il bot può tenere chiavi di diversi provider LLM insieme. Ruota tra le chiavi sane e fa failover automatico quando una smette di funzionare. Da `/admin` puoi fissare un modello, sceglierlo a mano, o lasciare che il bot ruoti liberamente. Qualsiasi provider con API compatibile OpenAI funziona — inclusi piccoli aggregatori, non solo i grandi nomi.

### Immagini

La generazione immagini ha tre modalità: **DuckAI** (gratis, niente chiave, default), **HiLinkUp** (a pagamento, qualità migliore), o un servizio immagini **custom** compatibile OpenAI tuo. Puoi anche mandare al bot una foto e dirgli come modificarla ("fai stile cartone"), e genera una nuova immagine. La generazione immagini si può spegnere da `/admin`.

### Paesi e lingue

Vortex supporta **195 paesi** e **40 lingue**. Il paese imposta il fuso orario, la valuta in cui si vedono i prezzi, la città usata per gli orari di preghiera, e i contenuti locali. La lingua imposta solo cosa dice il bot — un gruppo in Belgio può usare il paese Belgio e la lingua Inglese, per esempio. Entrambi si cambiano dopo da `/admin`.

### Aggiornamenti

Il bot controlla le release GitHub di `VortexLabsHQ/vortex-telegram-bot` una volta al giorno. Quando esce una nuova versione, manda un messaggio privato al capo con pulsanti ✅ / ❌. Accettando, aggiorna il codice e riavvia il bot. Finché la repo è privata, il controllo non fa nulla silenziosamente (l'API GitHub serve una repo pubblica) — metti `UPDATE_CHECK_ENABLED=0` se non vuoi mai il controllo.

## Risoluzione problemi / FAQ

**L'installer dice che il mio token non è valido.**
Il token viene da [@BotFather](https://t.me/BotFather). Assicurati di aver copiato tutto il token (cifre, due punti, poi 35+ caratteri), senza spazi extra. Se hai cancellato il bot o fatto un token nuovo, il vecchio smette di funzionare — incolla il nuovo.

**Il bot non risponde nel mio gruppo.**
Quattro cose da verificare: (1) La Privacy del gruppo deve essere disattivata — in [@BotFather](https://t.me/BotFather) invia `/setprivacy`, seleziona il tuo bot e scegli **Disable**; con la privacy attiva, il bot non può vedere affatto i messaggi del gruppo, (2) il bot deve essere aggiunto al gruppo, (3) devi pronunciare la sua parola di attivazione — il suo nome, ad esempio `Vortex che ore sono?` — il bot ascolta solo quando il suo nome viene detto nei gruppi, (4) in una chat privata non è necessaria alcuna parola di attivazione.

**Il bot risponde in inglese, non nella mia lingua.**
Manda `/admin` (solo il capo) → Lingua e Paese, e scegli la tua lingua. L'installer chiede anche la lingua — premi Invio lì per accettare quella predefinita del tuo paese.

**Ho scelto Anthropic e il bot non chatta.**
L'API nativa di Anthropic non è compatibile OpenAI, quindi il bot non può chattarci direttamente. Usa OpenRouter (che serve modelli Claude tramite API compatibile OpenAI), o scegli un altro provider dalla lista.

**La ricerca web non funziona.**
La ricerca web serve SearXNG, che l'installer si offre di configurare con Docker. Senza, il bot ripiega su Wikipedia, che è più debole. Puoi anche mettere `SEARCH_PROVIDER=tavily` o `serper` con una `SEARCH_API_KEY` in `.env`.

**Dove sono i log?**
`journalctl -u vortex-bot -f` mostra il log live. `systemctl status vortex-bot` mostra se il servizio gira. Se il bot si ferma, `sudo systemctl restart vortex-bot` lo riavvia.

**Il bot dice che ho raggiunto il limite giornaliero.**
Ogni utente ha 30 risposte bot al giorno (il capo è esente). Il limite si resetta a mezzanotte nel fuso orario del paese del bot. Alza il limite con `DAILY_LIMIT_MESSAGES` in `.env`, o chiedi al capo.

**Ho trovato un bug / ho un'idea.**
Apri una issue su GitHub — vedi [CONTRIBUTING.md](CONTRIBUTING.md) per come segnalarla e come mandare una fix.

## Sviluppo

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

Esegui i test (script Python semplici, niente pytest):

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

Tutte e nove le suite devono passare prima di aprire una pull request. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) per lo stile codice (ruff) e il processo PR.

## Licenza

Vortex è rilasciato sotto [Licenza MIT](LICENSE) — libero da usare, copiare, modificare e condividere, per qualsiasi scopo.

<a id="countries"></a>

## Paesi

Incolla il nome del paese **in inglese, esattamente come scritto qui** quando l'installer chiede il tuo paese. La tabella è generata da `bot/countries.py` — se un nome qui e uno là non coincidono, vince `bot/countries.py`.

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



## Grazie

> ⭐ **Metti una stella a questo progetto su GitHub e segui [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — è il modo più semplice per supportare Vortex e aiutare altri a trovarlo. Grazie!
