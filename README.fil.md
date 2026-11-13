# Vortex 🤖 — Sariling Telegram group assistant mo

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · **Filipino** · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Kung gusto mo ang Vortex, paki-star ang project na ito sa GitHub at sundan ang [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — tumutulong ito para mas maraming tao ang makakita nito. Salamat!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Ano ang Vortex?

Ang Vortex ay isang Telegram bot na naninirahan sa iyong mga grupo at private chats at sumasagot sa mga tao gamit ang AI chat model. Sabihin mo ang pangalan nito (ang default na pangalan ay **Vortex**) at sasagot ito — makakachat, magsisearch sa web, gumagawa ng larawan, tse-check ng presyo, magbibiruan, magbabasa ng file, i-transcribe ang voice message, at marami pang iba.

Ito ay tumatakbo sa iyong sariling server, sa iyong sariling bansa at wika. Ikaw ang boss: isang nakatagong `/admin` panel ang nagpapamanage sa iyo ng AI keys, users, at settings.

## Mga Tampok

- 💬 **AI chat** sa mga grupo (wake word) at private chats (walang kailangang wake word)
- 🔑 **Token pool** — gamitin ang maramihang LLM providers at keys, i-rotate at fail over nang automatic
- 🖼️ **Image generation** — gamit ang iyong sariling image service (base URL + API key + model), idinagdag sa `/admin`
- 🔍 **Web search** — self-hosted na SearXNG, may Wikipedia fallback
- 💰 **Live prices** — currencies, ginto, langis, at crypto sa iyong local currency
- 🕌 **Prayer times**, 🃏 **fortunes**, 😄 **jokes**, 🎲 **dice at coin flips**
- 📎 **File analysis** at **voice transcription**
- 📥 **Downloads** — magpadala ng link, makuha ang media file (hanggang 45 MB)
- 🌍 **195 bansa** at **40 wika** — bansa at wika ay hiwalay na settings
- 🔄 **Self-updating** — tse-check ng bagong releases araw-araw at nagtatanong bago i-update
- 🛡️ **Nakatagong /admin panel** — tokens, users, stats, chats, image model, managers, power

## Bago mo i-install

Kailangan mo ng server (o computer na naka-on) na tumatakbo sa **Linux** na may mga ito na installed:

| Ano | Paano i-check | Dapat mong makita |
| --- | --- | --- |
| **Python 3.11 o mas bago** | `python3 --version` | `Python 3.11.x` o mas mataas (3.12 at 3.13 gumagana rin) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` o `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` o katulad |
| **Docker** *(optional)* | `docker --version` | `Docker version 2x.x.x` — kailangan lang kung gusto mo ang optional na SearXNG web search |

Kung may kulang, i-install mo lahat sa isang utos (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Para sa opsiyonal na `Docker` (kailangan lamang kung gusto mo ng web search ng `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Pagkatapos ng huling linya, mag-log out at mag-log in muli (o patakbuhin ang mga utos na `docker` gamit ang `sudo`). Nag-aalok din ang installer na i-install ang mga kulang na tool para sa iyo gamit ang `apt` sa `Debian/Ubuntu`. Sa ibang sistema, i-install muna sila gamit ang iyong package manager. Ang `systemd` ay kasama sa system — hindi ito maaaring i-install nang hiwalay.

Kailangan mo rin ng dalawang bagay mula sa Telegram (pareho ay libre):

1. **Isang bot token** — makipag-usap sa [@BotFather](https://t.me/BotFather) sa Telegram, ipadala ang `/newbot`, at kopyahin ang token na ibibigay niya.
2. **Iyong numeric Telegram user ID** — makipag-usap sa [@userinfobot](https://t.me/userinfobot) at kopyahin ang numerong ipapakita niya. Ito ang iyong "boss" ID: lamang ang account na ito ang makakagamit ng `/admin`.

## Pag-install

Isang command. Kopyahin ito, i-paste sa iyong terminal, at pindutin ang Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Ang installer ay magtatanong ng anim na tanong, sa pagkakasunod:

1. **Bansa** — i-paste ang Ingles na pangalan ng iyong bansa **eksakto gaya ng nakalista sa [talahanayan ng mga bansa](#countries) sa ibaba** (halimbawa `Turkey`). Ang bansa ang nagtatakda ng time zone, lokal na kurensya para sa presyo, orasyon, at lokal na nilalaman.
2. **Wika** — ang wikang ginagamit ng bot (halimbawa `en`, `fa`, `tr`). Pindutin ang Enter para tanggapin ang default para sa iyong bansa. Ang wika ay hiwalay sa bansa: ito lamang ay nagbabago ng sinasabi ng bot, at maaari mong baguhin ito mamaya mula sa `/admin`.
3. **Token ng bot** — i-paste ang token mula sa [@BotFather](https://t.me/BotFather). Sinusuri ng installer ito nang live sa Telegram.
4. **Numerikong ID ng Boss** — ang iyong Telegram user ID mula sa [@userinfobot](https://t.me/userinfobot).
5. **Pangalan ng bot / salitang pambubukas** — ang pangalan na sinasabi ng mga tao sa mga grupo para makipag-usap sa bot. Anumang wika ay okay (halimbawa `Vortex` o `ورتکس`). Pindutin ang Enter para sa default na `Vortex`.
6. **Unang LLM provider** — pumili ng isa: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, o **Custom** (i-paste ang base URL). Pagkatapos ay i-paste ang iyong API key para sa provider na iyon — kukuha ng installer ng live na listahan ng model ng provider at pumili ka ng model.

Pagkatapos ay nag-i-install ang installer ng mga dependencies, nagssulat ng `.env` file, gumagawa ng `vortex-bot` systemd service, nag-aalok na i-install ang SearXNG para sa web search (kailangan ang Docker), at nagsisimula ang bot.

> ⚠️ **Ang Anthropic ay hindi gumagana nang direktang.** Ang native API ng Anthropic ay hindi OpenAI-compatible, at ang bot na ito ay nakikipag-usap lamang sa OpenAI-compatible APIs. Kung pumili ka ng Anthropic, babalaan ka ng installer: ang key ay gumagana lamang sa pamamagitan ng OpenAI-compatible gateway. Gamitin ang OpenRouter, o ibang provider mula sa listahan, sa halip.

## Pagkatapos ng pag-install

Suriin kung tumatakbo ang bot:

```bash
systemctl status vortex-bot
```

Dapat mong makita ang `active (running)`. Upang manuod ng live na log:

```bash
journalctl -u vortex-bot -f
```

Ngayon ay buksan ang Telegram at makipag-usap sa iyong bot:

- Magpadala ng `/start` — ang bot ay magsasabi ng kumusta.
- Sa **pribadong chat**, sulatan mo lang ito — walang kailangang salitang pambubukas.
- Sa **grupo**, idagdag ang bot sa group, pagkatapos ay i-off ang Group Privacy: sa [@BotFather](https://t.me/BotFather) ipadala ang `/setprivacy`, piliin ang iyong bot, at piliin ang **Disable** — kung hindi, hindi makakakita ang bot ng mga mensahe sa group at hindi maririnig ang wake word nito. Pagkatapos ay sabihin ang pangalan nito, halimbawa: `Vortex anong oras na?`
- Bilang boss, magpadala ng `/admin` sa pribadong chat upang buksan ang nakatagong admin panel.

**Ang mga update ay awtomatik.** Minsang araw ang bot ay nagche-check sa GitHub para sa bagong release. Kung may available, ito ay nagpapadala sa iyo ng pribadong mensahe na may ✅ / ❌ na mga button. Pindutin ang ✅ at ito ay mag-update sa sarili at magrerestart — hindi mo na kailangang galawin ang server.

## Konfigurasyon

Lahat ng settings ay nasa `.env` file sa install directory. Tingnan ang [`.env.example`](.env.example) para sa bawat opsyon. Ang pinakamahalaga sa kanila:

| Setting | Ano ang ginagawa nito |
| --- | --- |
| `BOT_TOKEN` | Ang iyong Telegram bot token (mula sa @BotFather) |
| `BOSS_ID` | Ang iyong numeric Telegram user ID (ang may-ari ng bot) |
| `BOT_NAME` | Ang pangalan ng bot at wake word sa mga grupo (default `Vortex`) |
| `BOT_COUNTRY` | Bansa sa Ingles, hal. `United States` (nagse-set ng time zone, currency, orasyon times) |
| `BOT_LANGUAGE` | Language code ng bot, hal. `en`, `fa`, `tr` (nagbabago lamang ng sinasabi ng bot) |
| `LLM_PROVIDERS` | Mga LLM provider at key: `base_url\|api_key\|model`, comma-separated |
| `UPDATE_CHECK_ENABLED` | `1` = suriin ang updates araw-araw, `0` = hindi kailanman suriin |
| `UPDATE_REPO` | Ang repo na binabantayan ang mga release (default `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Web search: `searxng` (default), `tavily`, o `serper` |
| `DAILY_LIMIT_MESSAGES` | Max na bot replies bawat user bawat araw (default `30`, ang boss ay libre) |

Ang bansa at wika ay maaari ring baguhin mamaya mula sa nakatagong `/admin` panel (Language & Country), nang hindi na kailangang i-edit anumang file.

## Docker alternative

Kung mas gusto mo ang Docker kaysa sa installer:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Ito ay nagsisimula ng bot kasama ang self-hosted na SearXNG search engine. Suriin ang logs gamit ang `docker compose logs -f bot`.

Paalala: ang automatic self-updater ay nangangailangan ng systemd service, kaya sa Docker ang updates ay manual: `git pull` at saka `docker compose up -d --build` muli.

## Mga Feature sa Detalye

### Ang `/admin` panel

Ipadala ang `/admin` sa private chat (boss lang — walang iba maaaring buksan, at hindi ito lumalabas sa `/help` o sa mga menu). Mayroon itong:

- 🔑 **Tokens & model** — idagdag o alisin ang LLM keys, tingnan kung aling key ang healthy, piliin ang active model, browse ang live model list ng provider
- 👥 **Users** — bilang ng user, ban / unban, allowlist
- 📊 **Stats** — mga numero ng paggamit
- 💬 **Recent chats** — ano ang sinabi ng tao sa bot (boss lang, private)
- 🖼️ **Image model** — iyong sariling image service (base URL + API key + model), o off
- 🛡️ **Managers** — bigyan ng access ang tiwala mong tao sa mga parte ng panel
- 🟢/🔴 **Power** — i-on o i-off ang bot para sa lahat (ang boss ay nananatiling nasa kontrol)
- 🌍 **Language & Country** — baguhin ang wika o bansa ng bot anumang oras

### Ang token pool

Ang bot ay maaaring mag-imbak ng key mula sa maramihang LLM provider sabay-sabay. Ito ay nagro-rotate sa pagitan ng healthy keys at nagfa-fail over nang awtomatik kapag huminto ang isa sa pagfuncion. Mula sa `/admin` maaari mong i-pin ang isang model, pumili ng model nang manual, o hayaang malaya ang rotation ng bot. Anumang provider na may OpenAI-compatible API ay gumagana — kabilang ang maliliit na aggregator, hindi lang ang mga sikat.

### Mga Imahe

Ang image generation ay gumagamit ng iyong sariling OpenAI-compatible image service: idagdag ang base URL, API key, at model sa `/admin` (🖼️ Image model). Walang built-in image provider, at hindi suportado ang photo editing. Maaaring i-off ang image generation mula sa `/admin`.

### Mga Bansa at Wika

Suportado ng Vortex ang **195 bansa** at **40 wika**. Ang bansa ang nagtatakda ng time zone, currency na ginagamit sa presyo, lungsod para sa orasyon, at lokal na nilalaman. Ang wika lamang ang nagtatakda ng sinasabi ng bot — pwede ng grupo sa Belgium gamitin ang bansang Belgium at wikang English, halimbawa. Pareho ay pwedeng baguhin mamaya mula sa `/admin`.

### Updates

Sinusuri ng bot ang GitHub releases ng `VortexLabsHQ/vortex-telegram-bot` isang beses sa araw. Kapag may bagong bersyon, nagpadala ito sa boss nang pribado na may ✅ / ❌ na buttons. Ang pagtanggap ay nag-uupdate ng code at nagrerestart ng bot. Habang pribado ang repo, tahimik na walang ginagawa ang check (kailangan ng GitHub's API ang public repo) — i-set ang `UPDATE_CHECK_ENABLED=0` kung ayaw mo ng check.

## Troubleshooting / FAQ

**Sinasabi ng installer na invalid ang token ko.**
Ang token ay galing sa [@BotFather](https://t.me/BotFather). Siguraduhing kopyahin mo ang buong token (mga digit, colon, pagkatapos 35+ na character), walang extra spaces. Kung binura mo ang bot o gumawa ng bagong token, humihinto ang lumang — i-paste ang bago.

**Hindi sumasagot ang bot sa grupo ko.**
Apap na bagay na suriin: (1) Dapat naka-off ang Group Privacy — sa [@BotFather](https://t.me/BotFather) ipadala ang `/setprivacy`, piliin ang iyong bot, at piliin ang **Disable**; kung naka-on ang privacy, hindi makakakita ang bot ng anumang mensahe sa group, (2) kailangang idagdag ang bot sa group, (3) kailangang sabihin ang wake word nito — ang pangalan nito, halimbawa `Vortex anong oras na?` — ang bot ay nakikinig lamang kapag nabanggit ang pangalan nito sa mga group, (4) sa pribadong chat ay hindi kailangan ang wake word.

**Sumasagot ang bot sa English, hindi sa wika ko.**
Magpadala ng `/admin` (boss lang) → Language & Country, at piliin ang wika mo. Nagtatanong din ang installer para sa wika — pindutin ang Enter doon para tanggapin ang default ng bansa mo.

**Pinili ko ang Anthropic at hindi nagcha-chat ang bot.**
Ang native API ng Anthropic ay hindi OpenAI-compatible, kaya hindi makakachat ang bot nang direktang. Gamitin ang OpenRouter (na maaaring mag-serve ng Claude models sa pamamagitan ng OpenAI-compatible API), o pumili ng ibang provider sa listahan.

**Hindi gumagana ang web search.**
Kailangan ng web search ang SearXNG, na ino-offer ng installer na i-setup gamit ang Docker. Nang walang ito, ang bot ay bumalik sa Wikipedia, na mas mahina. Pwede mo ring i-set ang `SEARCH_PROVIDER=tavily` o `serper` na may `SEARCH_API_KEY` sa `.env`.

**Nasaan ang logs?**
`journalctl -u vortex-bot -f` ay nagpapakita ng live log. `systemctl status vortex-bot` ay nagpapakita kung tumatakbo ang service. Kung huminto ang bot, `sudo systemctl restart vortex-bot` ay muling nag-uumpisa nito.

**Sinasabi ng bot na naabot ko na ang daily limit.**
Bawat user ay may 30 bot replies kada araw (libre ang boss). Ang limit ay nireriset sa hatinggabi sa time zone ng bansa ng bot. Itaas ito gamit ang `DAILY_LIMIT_MESSAGES` sa `.env`, o tanungin ang boss.

**Nakita ko ang bug / may idea ako.**
Pakibuksan ang issue sa GitHub — tingnan ang [CONTRIBUTING.md](CONTRIBUTING.md) kung paano ireport at paano magpadala ng fix.

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

Patakbuhin ang mga test (plain Python scripts, walang kailangang pytest):

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

Lahat ng siyam na suite ay kailangang dumaan bago mo buksan ang pull request. Tingnan ang [CONTRIBUTING.md](CONTRIBUTING.md) para sa code style (ruff) at PR process.

## License

Ang Vortex ay inilabas sa ilalim ng [MIT License](LICENSE) — libre gamitin, kopyahin, baguhin, at ibahagi, para sa anumang layunin.

<a id="countries"></a>

## Countries

I-paste ang pangalan ng bansa **sa English, eksakto gaya ng nakasulat dito** kapag tinatanong ng installer ang iyong bansa. Ang table ay ginawa mula sa `bot/countries.py` — kung magkaiba man ang pangalan dito at doon, ang `bot/countries.py` ang susundin.

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

## Salamat

> ⭐ **Paki-star ang project na ito sa GitHub at sundan ang [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — ito ang pinakasimpleng paraan upang suportahan ang Vortex at tulungan ang iba na matagpuan ito. Salamat!
