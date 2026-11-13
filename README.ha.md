# Vortex 🤖 — Mai taimakon kungiyar Telegram na kowa

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · **Hausa** · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Idan ka so Vortex, biko saka 'star' wannan ayyuka a GitHub kuma biya [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — tana taimaka wa mutane za su samu. Na gode!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Menene Vortex?

Vortex shine bot na Telegram wanda ke ciki da kungiyoyinku da rahotannin halitta ke amsa mutane da modelin AI na tafarko. Ka ce sunansa (sunan da ke tsawon **Vortex**) kuma ya amsa — zai iya tafarko, bincika wab, samar da hotuna, duba farashi, faɗa darajar, karanta faila, rubuta sautin waƙoƙi, da sauran.

Tana aiki a server na kowa, a kasar kowa da harshen kowa. Kai ne mai mulki: wani panel na `/admin` na cirewa zai ba ka damar sarrafa kayan AI, masu amfani, da saituna.

## Ƙwalli

- 💬 **AI tafarko** a kungiyoyi (kalmar fara) da rahotannin halitta (ba a buƙatar kalmar fara ba)
- 🔑 **Kudin token** — amfani da masu tallafin LLM da kayanai daban-daban, juyawa da canza a halin kuskure a takaice
- 🖼️ **Samar da hotuna da gyara** — kyauta (DuckAI) ko masu tallafin biyan kuɗi
- 🔍 **Binciken wab** — an gudana da SearXNG a cikin gida, da Wikipedia a matsayin baya
- 💰 **Farashin yanzu** — kurudda, zariya, manja, da crypto a kurdin gida
- 🕌 **Lokacin salatu**, 🃏 **fa'aloli**, 😄 **darajar**, 🎲 **kwari da gwargwado na kudi**
- 📎 **Binciken faila** da **rubutaccen sauti**
- 📥 **Saukewa** — aiko link, samu failin midiya koma (har 45 MB)
- 🌍 **Kasuwa 195** da **harsuna 40** — kasar da harshe ke saitunan bambance-bambance
- 🔄 **Sabuntawa a takaice** — duba sabon waƙoƙi kowane rana kuma yana buƙatar kai kafin sabuntawa
- 🛡️ **Panel na `/admin` na cirewa** — token, masu amfani, lambobi, tafarko, modelin hotuna, masu sarrafa, iko

## Kafin ka shigar da shi

Kuna buƙatar server (ko kuma kwantaspia tana wulakanta) tana aiki da **Linux** da wannan shigarwa:

| Me | Yadda ake duba | Me za ka ga |
| --- | --- | --- |
| **Python 3.11 ko sabuwa** | `python3 --version` | `Python 3.11.x` ko girma (3.12 da 3.13 na aiki) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` ko `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` ko matsala |
| **Docker** *(zaɓi)* | `docker --version` | `Docker version 2x.x.x` — ba a buƙatar ba sai idan ka so SearXNG na binciken wab na zaɓi |

Idan akwai abu da ke kacewa, shigar da duk da daya da amsa daya (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Don wannan `Docker` na zaɓi (sai an bukatar idan kuna so binciken `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Bayan hanyar ƙarshe, fita da sake shiga (ko yi `docker` awannan da `sudo`). Na gina ya kuma nuna shigar da kayan aiki da suka kacewa a cikin `apt` a `Debian/Ubuntu`. A sistemawa masu sauri, shigar da su da ma'amalan paketi na farko. `systemd` tana da cikin hanya — ba za a iya shigar da ita da kowa ba.

Kuna buƙatar abu biyu daga Telegram (duk biyu kyauta):

1. **Token na bot** — tafarko da [@BotFather](https://t.me/BotFather) a Telegram, aiko `/newbot`, kuma rubuta token wanda ya ba ka.
2. **ID na mutum na Telegram na lambar** — tafarko da [@userinfobot](https://t.me/userinfobot) kuma rubuta lambar wanda ya nuna maka. Wannan ne ID na "oga" na ku: wannan asusu kawai zai iya amfani da `/admin`.

## Shigarwa

Amsar daya. Rubuta, saka a terminal na ku, kuma danna Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Shigarwa yana buƙatar ku tambaya shida, a jerin:

1. **Ƙasa** — ɗauki sunan ƙasarka a Turanci **daidai kama da aka rubuta a [jedewar ƙasasuka](#countries) a ƙarƙashin** (misali `Turkey`). Ƙasa ta bada lokacin ƙasa, kuɗin ƙasa don farashin, lokacin addu'a, da abubuwan ƙasa.
2. **Harshe** — harshen da bot ke magana (misali `en`, `fa`, `tr`). Danna Enter don riƙe da default na ƙasarka. Harshe bai daidai da ƙasa ba: ita kawai tana canza abinda bot ke ce, kuma za ka iya canjata a nan daga `/admin`.
3. **Token na Bot** — ɗauki token daga [@BotFather](https://t.me/BotFather). Wannan na gwadawa ya gwada shi a cikin lokaci da Telegram.
4. **ID na Boss (Lambar)** — ID ɗin Telegram na ka daga [@userinfobot](https://t.me/userinfobot).
5. **Sunan Bot / Kalmar Fita** — suna da mutane ke kiran a ƙungiyoyi don magana da bot. Kowa harshe ya dace (misali `Vortex` ko `ورتکس`). Danna Enter don default `Vortex`.
6. **Mai Ba da LLM na Farko** — zaɓi daya: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, ko **Custom** (ɗauki base URL). Sai ka ɗauka API key ɗin ka don wannan mai ba da — wannan na gwadawa ya karɓi jerin modelin mai ba da a cikin lokaci kuma ka zaɓi model.

Sai wannan na gwadawa ya girka alama, rubuta failin `.env`, kirkira sabis na `vortex-bot` na systemd, yana ba da shawara don girka SearXNG don binciken wab (ana buƙatar Docker), kuma ya fara bot.

> ⚠️ **Anthropic ba ta aiki a kai tsaye ba.** API na asali na Anthropic ba shi da hadawa da OpenAI, kuma wannan bot kawai ya manta da API masu hadawa da OpenAI. Idan ka zaɓi Anthropic, wannan na gwadawa ya gargaɓi ka: key din kawai zai aiki ta hanyar ƙofar hadawa da OpenAI. Yi amfani da OpenRouter, ko mai ba da wani daga cikin jerin, bayanansa.

## Bayan Girkawa

Tabbatar cewa bot yana aiki:

```bash
systemctl status vortex-bot
```

Do ka ga `active (running)`. Don kallo log na yau da kullum:

```bash
journalctl -u vortex-bot -f
```

Yanzu buɗe Telegram kuma magana da bot ɗinka:

- Ayo `/start` — bot zai sallama.
- A **magana a cikin zuciya**, kawai rubuta masa — ba a buƙatar kalmar fita ba.
- A **ƙungiya**, kara bot zuwa group, sai rage Group Privacy: a [@BotFather](https://t.me/BotFather) aika `/setprivacy`, zaɓi bot ɗinka, kuma zaɓi **Disable** — in ba haka, bot ba za i ganuwa waɗannan? ba za i ji kalmar haske ba. Sai ka ce sunansa, misali: `Vortex yaushe lokaci?`
- Kamar boss, ayo `/admin` a magana a cikin zuciya don buɗe filin admin na hanyar hana.

**Sabuwawa ke aiki a hanyar mai kyau.** Kowane rana bot yana duba GitHub don sabuwar gudanarwa. Idan akwai, zai ayo wa ka sanarwa a cikin zuciya da kwanakin ✅ / ❌. Danna ✅ kuma zai sabunta shi da kai tsaye kuma ya fara sabuwa — ba ka bukatar hana hannu a server ba.

## Saitin

Duk saituna suna cikin failin `.env` a cikin folderin girkawa. Duba [`.env.example`](.env.example) don kowane opsin. Wadanda suke da muhimmanci:

| Saiti | Me ya ke yi |
| --- | --- |
| `BOT_TOKEN` | Tokin bot ɗinka na Telegram (daga @BotFather) |
| `BOSS_ID` | ID ɗin Telegram na lambar ɗinka (mai mulkin bot) |
| `BOT_NAME` | Sunnan bot da kalmar farko a cikin ƙungiyoyi (default `Vortex`) |
| `BOT_COUNTRY` | Kasa a Turanci, m: `United States` (saita lokaci, kuɗin, da lokacin salla) |
| `BOT_LANGUAGE` | Kode na harshen bot, m: `en`, `fa`, `tr` (sai yi canza abinda bot ke magana) |
| `LLM_PROVIDERS` | Masu tallafin LLM da ƙalubale: `base_url\|api_key\|model`, da koma |
| `UPDATE_CHECK_ENABLED` | `1` = duba sabuwawar kowace rana, `0` = ba a duba ba |
| `UPDATE_REPO` | Repo wanda ake kula da sabuwarsu (default `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Binciken wab: `searxng` (default), `tavily`, ko `serper` |
| `DAILY_LIMIT_MESSAGES` | Tsawon amsoshin bot ga mutum kowace rana (default `30`, mai mulki bai dawo ba) |

Kasa da harshe za a iya canza su bayan nan daga cikin panelin `/admin` mai kunkuri (Harshe & Kasa), ba tare da gyara kowanne faila ba.

## Zanen Docker

Idan kana so Docker kafin na girka:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Wannan yana fara bot tare da injinin bincike na SearXNG mai gine-kasa. Duba bayanan logs da `docker compose logs -f bot`.

Misarwari: na sabuntawa na kowa ya buƙatar sabis na systemd, saboda haka a Docker sabuwawar manual ne: `git pull` kuma sai `docker compose up -d --build` marece.

## Ƙwallaye a cikin hoto

### Panelin `/admin`

Aika `/admin` a cikin tattaunawa na shakato (mai mulki kawai — babu wani mai buƙatar buɗewa, kuma ba za ta gabata a `/help` ko a cikin menyawa ba). Tana da:

- 🔑 **Tokens & model** — kara ko cire ƙalubalen LLM, ganin wanda ke lafiya, zaɓa modelin na yau da kullum, bincika jerin modelin mai gida
- 👥 **Users** — adadin masu amfani, harjo / cire harjo, jerin masu izini
- 📊 **Stats** — lambobin amfani
- 💬 **Recent chats** — abinda mutane suka ce wa bot (mai mulki kawai, shakato)
- 🖼️ **Image model** — DuckAI (kyauta, default), HiLinkUp, sabis na hotuna na custom, ko sakeshi
- 🛡️ **Managers** — ba mutanen da aka amince wa adireshin nau'in panel
- 🟢/🔴 **Power** — saita bot on ko off ga duk wani (mai mulki ya rage mulki)
- 🌍 **Language & Country** — canza harshen bot ko kasarsa a kowace lokaci

### Kwanakin Token

Bot zai iya halar da ƙalubale daga masu tallafin LLM da yawa a lokaci daya. Yana juyawa tsakanin ƙalubale masu lafiya kuma yana canza a kowace lokacin da wani ya kasa aiki. Daga `/admin` za ka iya kuskure model ɗaya, zaɓa model da hannu, ko ka bara bot ya juya a hurumi. Kowa masu tallafi da API na OpenAI zai aiki — har ma ƙungiyoyin kananan, ba kawai sunayen girma kawai.

### Hotuna

Samar da hotuna tana da hanyen uku: **DuckAI** (kyauta, ba ƙalubale, default), **HiLinkUp** (biya, inganci mafi kyau), ko sabis na hotuna na **custom** da ya dace da OpenAI na ka. Za ka iya aika bot hoton kuma ka ce masa yadda ake gyarata ("yi wannan nau'in kartun"), kuma zai samar da hoton sabuwa. Samar da hotuna za a iya sakeshi daga `/admin`.

### Kasashe da Harsuna

Vortex yana da tallafi ga **ƙasar 195** da **harsunan 40**. Wannan ƙasa tana saita lokacin wata, kuɗin da ake nuna ciki, birnin da ake amfani da shi don lokacin salla, da abubuwan nan taken bayanai. Harshe kawai tana saita abin da bot ke magana — kungiyar a Belgium zata iya amfani da ƙasar Belgium da harshen Turanci, misali. Duk biyu za a iya sauya su bayan nan daga `/admin`.

### Sabuntawa

Bot din yana duba sabuntawar GitHub na `VortexLabsHQ/vortex-telegram-bot` kowane rana. Idan sigar sabuwa ce, zai aiko wa oga a cikin sirri da kwanakin ✅ / ❌. Yi ba da damar sabunta koodin da kuma sake fara bot din. Yanzu repo na sirri ne, duba ba shi ba wani abu (API ta GitHub tana buƙatar repo na ƙasa) — saita `UPDATE_CHECK_ENABLED=0` idan ka so ka biya duba ba.

## Hallaka Matsaloli / FAQ

**Na gina shi yana ce token na ba sai ya dace.**
Token din zo daga [@BotFather](https://t.me/BotFather). Tabbatar da cewa ka rubuta dukan token din (lambobi, colon, sai 35+ alamar), ba tare da raguwa ba. Idan ka share bot din ko ka samu token sabuwa, wannan tsohuwa tana kare aiki — rubuta wannan sabuwa.

**Ba bot ba ya amsa a kungiyar na.**
Iyalai hudu da a buƙata duba: (1) Group Privacy ya kamata a rage — a [@BotFather](https://t.me/BotFather) aika `/setprivacy`, zaɓi bot ɗinka, kuma zaɓi **Disable**; idan privacy ke cikin, bot ba za i ganuwa waɗannan? (2) a buƙata kara bot zuwa group, (3) a buƙata ka ce kalmar haske — sunansa, misali `Vortex yaushe lokaci?` — bot kawai yana sauraron idan an ce sunansa a group, (4) a private chat ba a buƙata kalmar haske ba.

**Bot din ya amsa da Turanci, ba harshen na ba.**
Aiko `/admin` (mai mulki kawai) → Harshe & Ƙasa, kuma zaɓi harshen ka. Na gina shi kuma yana buƙatar harshe — danna Enter a nan don riƙonci na ƙasar ka.

**Na zaɓi Anthropic kuma bot ba ya tattauna ba.**
API na asali ta Anthropic ba shi da hadawa da OpenAI, saboda haka bot ba zai iya tattauna da shi ba. Amfani da OpenRouter (wanda zai iya samar da modelolin Claude ta hanyar API mai hadawa da OpenAI), ko zaɓi mai samarwa wani daga jerin.

**Binciken gida ba ya aiki ba.**
Binciken gida yana buƙatar SearXNG, wanda na gina shi yana ba da damar saita shi da Docker. Ba tare da shi ba, bot zai koma Wikipedia, wanda ya fi karfi. Ka iya saita `SEARCH_PROVIDER=tavily` ko `serper` da `SEARCH_API_KEY` a cikin `.env`.

**Ina log din?**
`journalctl -u vortex-bot -f` yana nuna log na yanzu. `systemctl status vortex-bot` yana nuna ko sabis yake aiki. Idan bot ya tsaya, `sudo systemctl restart vortex-bot` zai sake fara shi.

**Bot din ya ce na isa haddin yau.**
Kowane mutum yana samun amsoshi 30 daga bot a kowane rana (mai mulki ba shi da shi ba). Haddin yana sake fara a cikin dare a lokacin wata na ƙasar bot. Kara shi da `DAILY_LIMIT_MESSAGES` a `.env`, ko tambaya mai mulki.

**Na samu wani kuskure / Na da wani tambaya.**
Don Allah ka buɗe wani mataki a GitHub — duba [CONTRIBUTING.md](CONTRIBUTING.md) don yadda ake adana shi da yadda ake aiko gyara.

## Ƙirƙirar

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

Yi gwaji (scriptodin Python na asali, ba a buƙatar pytest ba):

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

Duk suitodin tara biyu buƙata su yi nasara kafin ka buɗe pull request. Duba [CONTRIBUTING.md](CONTRIBUTING.md) don nau'in koodin (ruff) da hanyar PR.

## Leshi

An sake Vortex ƙarƙashin [MIT License](LICENSE) — kyauta don amfani, rubuta, sauya, da rage, don kowane haja.

<a id="countries"></a>

## Ƙasashe

Sake sunan kasa **a Turanci, hakan yadda aka rubuta a nan** idan na gina yana buƙatar kasa. Jadwali an haɗa shi daga `bot/countries.py` — idan sunan a nan da sunan a wurin ba su daidaita ba, `bot/countries.py` ya kasance cikin ƙarfi.

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

## Na gode

> ⭐ **Da fatan za ka juya wannan ayyuka a GitHub kuma ka biya [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — wannan hanyar na sauƙi ne don tallafa Vortex kuma taimaka wa wasu su sami shi. Na gode!
