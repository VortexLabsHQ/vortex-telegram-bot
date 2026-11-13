# Vortex 🤖 — Your own Telegram group assistant

**English** · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **If you like Vortex, please star this project on GitHub and follow [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — it helps more people find it. Thank you!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What is Vortex?

Vortex is a Telegram bot that lives in your groups and private chats and answers people with an AI chat model. You say its name (the default name is **Vortex**) and it replies — it can chat, search the web, make images, check prices, tell jokes, read files, transcribe voice messages, and more.

It runs on your own server, in your own country and language. You are the boss: a hidden `/admin` panel lets you manage AI keys, users, and settings.

## Features

- 💬 **AI chat** in groups (wake word) and private chats (no wake word needed)
- 🔑 **Token pool** — use several LLM providers and keys, rotate and fail over automatically
- 🖼️ **Image generation and editing** — free (DuckAI) or paid providers
- 🔍 **Web search** — self-hosted SearXNG, with Wikipedia fallback
- 💰 **Live prices** — currencies, gold, oil, and crypto in your local currency
- 🕌 **Prayer times**, 🃏 **fortunes**, 😄 **jokes**, 🎲 **dice and coin flips**
- 📎 **File analysis** and **voice transcription**
- 📥 **Downloads** — send a link, get the media file back (up to 45 MB)
- 🌍 **195 countries** and **40 languages** — country and language are separate settings
- 🔄 **Self-updating** — checks for new releases daily and asks you before updating
- 🛡️ **Hidden /admin panel** — tokens, users, stats, chats, image model, managers, power

## Before you install

You need a server (or a computer that stays on) running **Linux** with these installed:

| What | How to check | What you should see |
| --- | --- | --- |
| **Python 3.11 or newer** | `python3 --version` | `Python 3.11.x` or higher (3.12 and 3.13 work too) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` or `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` or similar |
| **Docker** *(optional)* | `docker --version` | `Docker version 2x.x.x` — only needed if you want the optional SearXNG web search |

If something is missing, install it all with one command (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

For the optional Docker (only needed if you want the SearXNG web search):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

After the last line, log out and back in (or run `docker` commands with `sudo`). The installer also offers to install missing tools for you with `apt` on Debian/Ubuntu. On other systems, install them with your package manager first. `systemd` comes with the system — it can't be installed separately.

You also need two things from Telegram (both are free):

1. **A bot token** — talk to [@BotFather](https://t.me/BotFather) on Telegram, send `/newbot`, and copy the token it gives you.
2. **Your numeric Telegram user ID** — talk to [@userinfobot](https://t.me/userinfobot) and copy the number it shows you. This is your "boss" ID: only this account can use `/admin`.

## Install

One command. Copy it, paste it in your terminal, and press Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

The installer asks you six questions, in order:

1. **Country** — paste the English name of your country **exactly as listed in the [country table](#countries) below** (for example `Turkey`). The country sets the time zone, the local currency for prices, prayer times, and local content.
2. **Language** — the language the bot speaks (for example `en`, `fa`, `tr`). Press Enter to accept the default for your country. Language is separate from country: it only changes what the bot says, and you can change it later from `/admin`.
3. **Bot token** — paste the token from [@BotFather](https://t.me/BotFather). The installer checks it live with Telegram.
4. **Boss numeric ID** — your Telegram user ID from [@userinfobot](https://t.me/userinfobot).
5. **Bot name / wake word** — the name people say in groups to talk to the bot. Any language is fine (for example `Vortex` or `ورتکس`). Press Enter for the default `Vortex`.
6. **First LLM provider** — pick one: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, or **Custom** (paste a base URL). Then paste your API key for that provider — the installer fetches the provider's live model list and you pick a model.

Then the installer installs the dependencies, writes the `.env` file, creates the `vortex-bot` systemd service, offers to install SearXNG for web search (needs Docker), and starts the bot.

> ⚠️ **Anthropic does not work directly.** Anthropic's native API is not OpenAI-compatible, and this bot only speaks OpenAI-compatible APIs. If you pick Anthropic, the installer warns you: the key only works through an OpenAI-compatible gateway. Use OpenRouter, or another provider from the list, instead.

## After installing

Check that the bot is running:

```bash
systemctl status vortex-bot
```

You should see `active (running)`. To watch the live log:

```bash
journalctl -u vortex-bot -f
```

Now open Telegram and talk to your bot:

- Send `/start` — the bot says hello.
- In a **private chat**, just write to it — no wake word needed.
- In a **group**, add the bot to the group, then turn off Group Privacy: in [@BotFather](https://t.me/BotFather) send `/setprivacy`, pick your bot, and choose **Disable** — otherwise the bot can't see group messages and won't hear its wake word. Then say its name, for example: `Vortex what's the time?`
- As the boss, send `/admin` in a private chat to open the hidden admin panel.

**Updates are automatic.** Once a day the bot checks GitHub for a new release. If one is available, it sends you a private message with ✅ / ❌ buttons. Tap ✅ and it updates itself and restarts — you never need to touch the server.

## Configuration

All settings live in the `.env` file in the install directory. See [`.env.example`](.env.example) for every option. The most important ones:

| Setting | What it does |
| --- | --- |
| `BOT_TOKEN` | Your Telegram bot token (from @BotFather) |
| `BOSS_ID` | Your numeric Telegram user ID (the bot owner) |
| `BOT_NAME` | The bot's name and wake word in groups (default `Vortex`) |
| `BOT_COUNTRY` | Country in English, e.g. `United States` (sets time zone, currency, prayer times) |
| `BOT_LANGUAGE` | Bot language code, e.g. `en`, `fa`, `tr` (only changes what the bot says) |
| `LLM_PROVIDERS` | LLM providers and keys: `base_url\|api_key\|model`, comma-separated |
| `UPDATE_CHECK_ENABLED` | `1` = check for updates daily, `0` = never check |
| `UPDATE_REPO` | The repo whose releases are watched (default `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Web search: `searxng` (default), `tavily`, or `serper` |
| `DAILY_LIMIT_MESSAGES` | Max bot replies per user per day (default `30`, boss is exempt) |

Country and language can also be changed later from the hidden `/admin` panel (Language & Country), without editing any file.

## Docker alternative

If you prefer Docker over the installer:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

This starts the bot together with a self-hosted SearXNG search engine. Check the logs with `docker compose logs -f bot`.

Note: the automatic self-updater needs the systemd service, so in Docker updates are manual: `git pull` and then `docker compose up -d --build` again.

## Features in detail

### The /admin panel

Send `/admin` in a private chat (boss only — nobody else can open it, and it never appears in `/help` or the menus). It has:

- 🔑 **Tokens & model** — add or remove LLM keys, see which keys are healthy, pick the active model, browse a provider's live model list
- 👥 **Users** — user counts, ban / unban, allowlist
- 📊 **Stats** — usage numbers
- 💬 **Recent chats** — what people said to the bot (boss only, private)
- 🖼️ **Image model** — DuckAI (free, default), HiLinkUp, a custom image service, or off
- 🛡️ **Managers** — give trusted people access to parts of the panel
- 🟢/🔴 **Power** — turn the bot on or off for everyone (boss stays in control)
- 🌍 **Language & Country** — change the bot's language or country any time

### The token pool

The bot can hold keys from several LLM providers at once. It rotates between healthy keys and fails over automatically when one stops working. From `/admin` you can pin one model, pick a model by hand, or let the bot rotate freely. Any provider with an OpenAI-compatible API works — including small aggregators, not just the big names.

### Images

Image generation has three modes: **DuckAI** (free, no key, default), **HiLinkUp** (paid, better quality), or a **custom** OpenAI-compatible image service of your own. You can also send the bot a photo and tell it how to edit it ("make this cartoon style"), and it will generate a new image. Image generation can be turned off from `/admin`.

### Countries and languages

Vortex supports **195 countries** and **40 languages**. The country sets the time zone, the currency prices are shown in, the city used for prayer times, and local content. The language only sets what the bot says — a group in Belgium can use the country Belgium and the language English, for example. Both can be changed later from `/admin`.

### Updates

The bot checks the GitHub releases of `VortexLabsHQ/vortex-telegram-bot` once a day. When a new version is out, it messages the boss privately with ✅ / ❌ buttons. Accepting updates the code and restarts the bot. While the repo is private, the check silently does nothing (GitHub's API needs a public repo) — set `UPDATE_CHECK_ENABLED=0` if you never want the check.

## Troubleshooting / FAQ

**The installer says my token is invalid.**
The token comes from [@BotFather](https://t.me/BotFather). Make sure you copied the whole token (digits, a colon, then 35+ characters), with no extra spaces. If you deleted the bot or made a new token, the old one stops working — paste the new one.

**The bot doesn't answer in my group.**
Four things to check: (1) Group Privacy must be off — in [@BotFather](https://t.me/BotFather) send `/setprivacy`, pick your bot, and choose **Disable**; with privacy on, the bot can't see group messages at all, (2) the bot must be added to the group, (3) you must say its wake word — its name, for example `Vortex what's the time?` — the bot only listens when its name is said in groups, (4) in a private chat no wake word is needed at all.

**The bot answers in English, not my language.**
Send `/admin` (boss only) → Language & Country, and pick your language. The installer also asks for the language — press Enter there to accept your country's default.

**I picked Anthropic and the bot doesn't chat.**
Anthropic's native API is not OpenAI-compatible, so the bot cannot chat with it directly. Use OpenRouter (which can serve Claude models through an OpenAI-compatible API), or pick another provider from the list.

**Web search doesn't work.**
Web search needs SearXNG, which the installer offers to set up with Docker. Without it, the bot falls back to Wikipedia, which is weaker. You can also set `SEARCH_PROVIDER=tavily` or `serper` with a `SEARCH_API_KEY` in `.env`.

**Where are the logs?**
`journalctl -u vortex-bot -f` shows the live log. `systemctl status vortex-bot` shows whether the service is running. If the bot stops, `sudo systemctl restart vortex-bot` starts it again.

**The bot says I've reached the daily limit.**
Each user gets 30 bot replies per day (the boss is exempt). The limit resets at midnight in the bot's country time zone. Raise it with `DAILY_LIMIT_MESSAGES` in `.env`, or ask the boss.

**I found a bug / I have an idea.**
Please open an issue on GitHub — see [CONTRIBUTING.md](CONTRIBUTING.md) for how to report it and how to send a fix.

## Development

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

Run the tests (plain Python scripts, no pytest needed):

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

All nine suites must pass before you open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for the code style (ruff) and the PR process.

## License

Vortex is released under the [MIT License](LICENSE) — free to use, copy, change, and share, for any purpose.

<a id="countries"></a>

## Countries

Paste the country name **in English, exactly as written here** when the installer asks for your country. The table is generated from `bot/countries.py` — if a name here and a name there ever disagree, `bot/countries.py` wins.

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



## Thank you

> ⭐ **Please star this project on GitHub and follow [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — it is the simplest way to support Vortex and help others find it. Thank you!
