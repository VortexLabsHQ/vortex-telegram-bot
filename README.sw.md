# Vortex 🤖 — Msaidizi wako mwenyewe wa kikundi cha Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · **Kiswahili** · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Ukipenda Vortex, tafadhali toa nyota kwenye mradi huu kwenye GitHub na fuata [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — hii inasaidia watu zaidi kukupata. Asante!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Nini Vortex?

Vortex ni bot ya Telegram inayokaa kwenye vikundi vyako na mazungumzo binafsi na kujibu watu kwa modeli ya AI ya mazungumzo. Unasema jina lake (jina la chaguo-msingi ni **Vortex**) na inajibu — inaweza kuongea, kutafuta mtandaoni, kufanya picha, kuangalia bei, kusema michezo, kusoma faili, kuandika sauti, na zaidi.

Inaendeshwa kwenye seva yako mwenyewe, nchini mwako na lugha yako. Wewe ni mkuu: panel ya siri ya `/admin` inakuruhusu kudhibiti vitufe vya AI, watumiaji, na mipangilio.

## Vipengele

- 💬 **Mazungumzo ya AI** kwenye vikundi (neno la kuamka) na mazungumzo binafsi (hahitaji neno la kuamka)
- 🔑 **Kikoba cha vitufe** — tumia watoa huduma wengi wa LLM na vitufe, rudisha na fail over kiotomatiki
- 🖼️ **Uundaji na uhariri wa picha** — bure (DuckAI) au watoa huduma walio na malipo
- 🔍 **Utafutaji mtandaoni** — SearXNG ya self-hosted, na Wikipedia kama chaguo la pamoja
- 💰 **Bei za wakati halisi** — sarafu, dhahabu, mafuta, na crypto kwenye sarafu yako ya kienyeji
- 🕌 **Muda wa sala**, 🃏 **matabiri**, 😄 **michezo**, 🎲 **kubisha na kiflip cha sarafu**
- 📎 **Uchambuzi wa faili** na **uandikaji wa sauti**
- 📥 **Upakaji** — tuma kiungo, upate faili ya media nyuma (hadi 45 MB)
- 🌍 **Nchi 195** na **lugha 40** — nchi na lugha ni mipangilio tofauti
- 🔄 **Kusasisha kwa nafsi** — huangalia matoleo mapya kila siku na kukuliza kabla ya kusasisha
- 🛡️ **Panel ya siri ya /admin** — vitufe, watumiaji, takwimu, mazungumzo, modeli ya picha, wadhibiti, nguvu

## Kabla ya kupakiza

Unahitaji seva (au kompyuta inayobaki wazi) inayotekelea **Linux** na hizi zipakizwa:

| Nini | Jinsi ya kuangalia | Unachoweza kuona |
| --- | --- | --- |
| **Python 3.11 au mpya zaidi** | `python3 --version` | `Python 3.11.x` au juu (3.12 na 3.13 zinafanya kazi pia) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` au `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` au sawa |
| **Docker** *(chaguo)* | `docker --version` | `Docker version 2x.x.x` — inahitajika tu ikiwa unataka utafutaji mtandaoni wa chaguo la SearXNG |

Ikiwa kitu kingine hakipo, mpakizi atakupa majaribio ya kupakiza kwa ajili yako kwa `apt` (kwenye Debian/Ubuntu). Kwenye mifumo mingine, pakiza kwanza kwa meneja wako wa paketi.

Pia unahitaji vitu viwili kutoka Telegram (vyote ni bure):

1. **Token ya bot** — zungumza na [@BotFather](https://t.me/BotFather) kwenye Telegram, tuma `/newbot`, na nakili token inayokupwa.
2. **ID yako ya mtumiaji wa Telegram ya nambari** — zungumza na [@userinfobot](https://t.me/userinfobot) na nakili nambari inayonyesha. Hii ni ID yako ya "mkuu": akaunti hii pekee inaweza kutumia `/admin`.

## Pakiza

Amri moja. Nakili, bandika kwenye terminal yako, na bofya Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Mpakizi huliza maswali sita, kwa mpangilio:

1. **Nchi** — weka jina la Kiingereza la nchi yako **kama kilivyoorodheshwa kwenye [jedwali la nchi](#countries) hapa chini** (k.m. `Turkey`). Nchi inategemea eneo la saa, sarafu ya eneo kwa bei, muda wa salati, na maudhui ya eneo.
2. **Lugha** — lugha ambayo bot inazungumza (k.m. `en`, `fa`, `tr`). Bonyeza Enter kukubali chaguo-msingi cha nchi yako. Lugha ni tofauti na nchi: inabadilisha tu kile bot kinachosema, na unaweza kubadilisha baadaye kutoka `/admin`.
3. **Token ya Bot** — weka token kutoka [@BotFather](https://t.me/BotFather). Mweka anauhakikisha hivi karibuni na Telegram.
4. **ID ya Nambari ya Boss** — ID yako ya mtumiaji wa Telegram kutoka [@userinfobot](https://t.me/userinfobot).
5. **Jina la Bot / neno la kuamsha** — jina ambalo watu husema kwenye vikundi kuongea na bot. Lugha yoyote inapatikana (k.m. `Vortex` au `ورتکس`). Bonyeza Enter kwa chaguo-msingi `Vortex`.
6. **Mtoa LLM wa kwanza** — chagua moja: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, au **Custom** (weka URL ya msingi). Kisha weka ufunguo wako wa API kwa mtoa huyo — mweka hupakua orodha ya mwezi ya mtoa na uchague modeli.

Kisha mweka anasakabisha vihusiano, kuandika faili ya `.env`, kuunda huduma ya `vortex-bot` ya systemd, anapendekeza kusakabisha SearXNG kwa utafutaji mtandaoni (inahitaji Docker), na kuanzisha bot.

> ⚠️ **Anthropic haifanyi kazi moja kwa moja.** API ya msingi ya Anthropic haifanani na OpenAI, na bot hii inazungumza API za OpenAI-fanani tu. Ukichagua Anthropic, mweka anakupigia keho: ufunguo unafanya kazi kupitia mlango wa OpenAI-fanani tu. Tumia OpenRouter, au mtoa mwingine kutoka orodha, badala yake.

## Baada ya kusakabisha

Angalia kama bot inakimbia:

```bash
systemctl status vortex-bot
```

Unapaswa kuona `active (running)`. Kufuatilia logi ya moja kwa moja:

```bash
journalctl -u vortex-bot -f
```

Sasa fungua Telegram na ongea na bot yako:

- Tuma `/start` — bot inasalamu.
- Kwenye **mazungumzo ya binafsi**, andika kwake tu — hakuna hitaji ya neno la kuamsha.
- Kwenye **kikundi**, ongeza bot kwenye kikundi, kisha sema jina lake, k.m.: `Vortex saa ngapi?`
- Kama boss, tuma `/admin` kwenye mazungumzo ya binafsi kufungua paneli ya msimamizi iliyofichwa.

**Masasisho ni ya kiotomatiki.** Mara moja kwa siku bot inaatilia GitHub kwa toleo jipya. Ikipo, inakutumia ujumbe binafsi na viungo vya ✅ / ❌. Bonyeza ✅ na itasasisha na kuanzisha upya — hutahitaji kugusa seva.

## Mipangilio

Mipangilio yote iko kwenye faili ya `.env` kwenye direkta ya usakabishaji. Angalia [`.env.example`](.env.example) kwa kila chaguo. Muhimu zaidi ni hivi:

| Setting | Kinachofanya |
| --- | --- |
| `BOT_TOKEN` | Tokeni yako ya bot ya Telegram (kutoka @BotFather) |
| `BOSS_ID` | ID yako ya mtumiaji wa Telegram ya nambari (mwenye bot) |
| `BOT_NAME` | Jina la bot na neno la kuamsha kwenye vikundi (chaguo-msingi `Vortex`) |
| `BOT_COUNTRY` | Nchi kwa Kiingereza, mf. `United States` (inazidi eneo la saa, sarafu, na muda wa sala) |
| `BOT_LANGUAGE` | Kodi ya lugha ya bot, mf. `en`, `fa`, `tr` (inabadilisha tu kinacho sema bot) |
| `LLM_PROVIDERS` | Watoa huduma wa LLM na vitufe: `base_url\|api_key\|model`, kugawanywa na koma |
| `UPDATE_CHECK_ENABLED` | `1` = angalia masasisho kila siku, `0` = usiangalie kamwe |
| `UPDATE_REPO` | Repo ambayo matoleo yake yanachunguzwa (chaguo-msingi `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Utafutaji mtandaoni: `searxng` (chaguo-msingi), `tavily`, au `serper` |
| `DAILY_LIMIT_MESSAGES` | Makubwa ya majibu ya bot kwa mtumiaji kwa siku (chaguo-msingi `30`, boss hawezi kuzuiliwa) |

Nchi na lugha zinaweza pia kubadilishwa baadaye kutoka kwenye paneli ya `/admin` iliyofichwa (Lugha & Nchi), bila kuhariri yoyote faili.

## Chaguo la Docker

Ikiwa unapendelea Docker kuliko mpangaji:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Hii inaanza bot pamoja na injini ya utafutaji ya SearXNG iliyowekewa wenyewe. Angalia logi kwa `docker compose logs -f bot`.

Kumbuka: mwepesi wa kujisaidia wa kiotomatiki unahitaji huduma ya systemd, hivyo kwenye Docker masasisho ni ya mkono: `git pull` kisha `docker compose up -d --build` tena.

## Vipengele kwa undani

### Paneli ya /admin

Tuma `/admin` kwenye mazungumzo ya binafsi (boss pekee — mtu mwingine hawezi kifungua, na hakinaonekana kwenye `/help` au menyu). Inayo:

- 🔑 **Tokens & model** — ongeza au ondoa vitufe vya LLM, ona vitufe vinavyo stahiki, chagua modeli iliyochakama, tazama orodha ya modeli za msingi kwa wakati halisi
- 👥 **Users** — idadi ya watumiaji, kucheka / kuondoa kucheka, orodha ya ruhusa
- 📊 **Stats** — nambari za matumizi
- 💬 **Recent chats** — watu walichosema kwa bot (boss pekee, binafsi)
- 🖼️ **Image model** — DuckAI (bure, chaguo-msingi), HiLinkUp, huduma ya picha ya kipekee, au zima
- 🛡️ **Managers** — wape watu wa kuaminiwa ufikiaji kwa sehemu za paneli
- 🟢/🔴 **Power** — fungua au zima bot kwa wote (boss anaendelea kudhibiti)
- 🌍 **Language & Country** — badilisha lugha au nchi ya bot wakati wowote

### Chimbuko cha vitufe

Bot inaweza kuhifadhi vitufe kutoka kwa watoa huduma wengi wa LLM kwa wakati mmoja. Inazunguka kati ya vitufe vinavyostahiki na inabadilisha kiotomatiki wakati moja imekwama. Kutoka `/admin` unaweza kufunga modeli moja, kuchagua modeli kwa mkono, au kuacha bot izunguke bure. Yeyote mtoa huduma na API inayolingana na OpenAI inafanya kazi — ikiwa na washiriki wadogo, si tu wakuu.

### Picha

Uundaji wa picha una mwelekeo tatu: **DuckAI** (bure, hakuna kifungu, chaguo-msingi), **HiLinkUp** (kilipwa, ubora bora), au huduma ya picha ya **kuchagua** inayolingana na OpenAI yako mwenyewe. Unaweza pia kutuma bot picha na kuambia jinsi ya kuhariri ("fanya hii ya mtindo wa kartuni"), na itaundaa picha mpya. Uundaji wa picha unaweza kuzimwa kutoka `/admin`.

### Nchi na lugha

Vortex inasaidia **nchi 195** na **lugha 40**. Nchi inawakilisha msimbo wa saa, sarafu inayotumika kuonyesha bei, jiji linalotumika kwa wakati wa salati, na maudhui ya eneo. Lugha inatenga tu nini bot inasema — kundi nchini Belgium kinaweza kutumia nchi ya Belgium na lugha ya Kiingereza, kwa mfano. Zote mbili zinaweza kubadilishwa baadaye kutoka `/admin`.

### Masasisho

Bot huhakikisha matoleo ya GitHub ya `VortexLabsHQ/vortex-telegram-bot` mara moja kwa siku. Wakati toleo jipya litokea, huwasiliana na mkuu binafsi na vifaa vya ✅ / ❌. Kukubali hukusanya msimbo na kuanzisha upya bot. Wakati repo ni binafsi, uchunguzi haufanyi chochote kimya (API ya GitHub inahitaji repo ya umma) — weka `UPDATE_CHECK_ENABLED=0` usipoweza kuchunguza.

## Kutatua Matatizo / Maswali Yanayoulizwa Mara kwa Mara

**Mwanzilishi anasema token yangu si sahihi.**
Token inatoka kwa [@BotFather](https://t.me/BotFather). Hakikisha umekopi token nzima (tarakimu, nukta, kisha herufi 35+), bila nafasi zilizozidi. Ukiufuta bot au ukiunda token mpya, ya jadi haifanyi kazi tena — weka mpya.

**Bot haijibu kwenye kundi langu.**
Vitu tatu vinavyohitajika kuangalia: (1) bot lazima ongezwe kwenye kundi, (2) lazima useme neno lake la kuamka — jina lake, kwa mfano `Vortex saa ngapi?` — bot inaskia tu wakati jina lake linasemiwa kwenye vikundi, (3) kwenye mazungumzo binafsi hakuna neno la kuamka linachohitajika kabisa.

**Bot inajibu kwa Kiingereza, si lugha yangu.**
Tuma `/admin` (mkuu tu) → Lugha & Nchi, na chagua lugha yako. Mwanzilishi pia huliza lugha — bofya Enter hapo kukubali chaguo-msingi cha nchi yako.

**Nilichagua Anthropic na bot haizungumzi.**
API ya msingi ya Anthropic haifanani na OpenAI, hivyo bot hawezi kuzungumza nayo moja kwa moja. Tumia OpenRouter (ambayo inaweza kutoa modeli za Claude kupitia API inayofanana na OpenAI), au chagua mtoa huduma mwingine kutoka kwenye orodha.

**Utafutaji mtandaoni haifanyi kazi.**
Utafutaji mtandaoni unahitaji SearXNG, ambayo mwanzilishi anapendekeza kuweka kwa Docker. Bila hiyo, bot inarudi kwenye Wikipedia, ambayo ni dhaifu zaidi. Unaweza pia kuweka `SEARCH_PROVIDER=tavily` au `serper` pamoja na `SEARCH_API_KEY` kwenye `.env`.

**Rejea ziko wapi?**
`journalctl -u vortex-bot -f` inaonyesha rejea ya moja kwa moja. `systemctl status vortex-bot` inaonyesha kama huduma inafanya kazi. Ikiwa bot imasimama, `sudo systemctl restart vortex-bot` inaanza tena.

**Bot inasema nimefikia kipimo cha kila siku.**
Kila mtumiaji hupata majibu 30 ya bot kwa siku (mkuu hawezekani). Kipimo kinazidiwa usiku wa manane kwenye msimbo wa saa wa nchi ya bot. Ongeza kwa `DAILY_LIMIT_MESSAGES` kwenye `.env`, au uliza mkuu.

**Nimegundua kosa / nina wazo.**
Tafadhali fungua tatizo kwenye GitHub — angalia [CONTRIBUTING.md](CONTRIBUTING.md) jinsi ya kuripoti na jinsi ya kutuma urekebisho.

## Maendeleo

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

Endesha mitihani (skripiti za Python rahisi, hakuna pytest inayohitajika):

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

Vitao vyote kumi na tisa vinapaswa kufanikiwa kabla ya kufungua ombi la kukusanya. Angalia [CONTRIBUTING.md](CONTRIBUTING.md) kwa mtindo wa msimbo (ruff) na mchakato wa PR.

## Leseni

Vortex imetolewa chini ya [Leseni ya MIT](LICENSE) — bure kutumia, nakili, badilisha, na kushiriki, kwa lengo lolote.

<a id="countries"></a>

## Nchi

Nakili jina la nchi **kwa Kiingereza, kama ilivyoandikwa hapa** wakati mtandaji anakuuliza nchi yako. Jedwali limeundwa kutoka kwa `bot/countries.py` — kama jina hapa na jina hapo hazilingani, `bot/countries.py` ndiye inayoshinda.

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

## Asante

> ⭐ **Tafadhali toa nyota kwenye mradi huu kwenye GitHub na fuata [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — ni njia rahisi zaidi ya kusaidia Vortex na kuwasaidia wengine kupata. Asante!
