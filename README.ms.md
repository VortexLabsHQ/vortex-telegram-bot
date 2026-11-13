# Vortex 🤖 — Pembantu kumpulan Telegram anda sendiri

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · **Bahasa Melayu** · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Jika anda suka Vortex, sila bintangkan projek ini di GitHub dan ikuti [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — ia membantu lebih ramai orang menemuinya. Terima kasih!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Apa itu Vortex?

Vortex adalah bot Telegram yang berada dalam kumpulan dan perbualan persendirian anda dan menjawab pengguna dengan model bercakap AI. Anda sebut namanya (nama lalai ialah **Vortex**) dan ia akan membalas — ia boleh bercakap, mencari web, menjana imej, semak harga, beritahu jenaka, baca fail, transkrip mesej suara, dan banyak lagi.

Ia berjalan pada pelayan anda sendiri, di negara dan bahasa anda sendiri. Anda adalah bos: panel `/admin` tersembunyi membolehkan anda mengurus kunci AI, pengguna, dan tetapan.

## Ciri-ciri

- 💬 **AI chat** dalam kumpulan (kata bangun) dan perbualan persendirian (tidak perlu kata bangun)
- 🔑 **Token pool** — gunakan beberapa penyedia LLM dan kunci, putar dan gagal alih secara automatik
- 🖼️ **Penjanaan dan pengeditan imej** — percuma (DuckAI) atau penyedia berbayar
- 🔍 **Carian web** — SearXNG hos sendiri, dengan Wikipedia sebagai cadangan
- 💰 **Harga langsung** — mata wang, emas, minyak, dan kripto dalam mata wang tempatan anda
- 🕌 **Waktu solat**, 🃏 **ramalan**, 😄 **jenaka**, 🎲 **dadu dan undian syiling**
- 📎 **Analisis fail** dan **transkripsi suara**
- 📥 **Muat turun** — hantar pautan, dapatkan fail media kembali (sehingga 45 MB)
- 🌍 **195 negara** dan **40 bahasa** — negara dan bahasa adalah tetapan berasingan
- 🔄 **Kemaskini sendiri** — semak terbitan baru harian dan tanya anda sebelum mengemas kini
- 🛡️ **Panel /admin tersembunyi** — token, pengguna, statistik, perbualan, model imej, pengurus, kuasa

## Sebelum anda memasang

Anda memerlukan pelayan (atau komputer yang sentiasa hidup) yang menjalankan **Linux** dengan yang berikut dipasang:

| Apa | Cara semak | Apa yang anda lihat |
| --- | --- | --- |
| **Python 3.11 atau lebih baru** | `python3 --version` | `Python 3.11.x` atau lebih tinggi (3.12 dan 3.13 juga berfungsi) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` atau `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` atau serupa |
| **Docker** *(pilihan)* | `docker --version` | `Docker version 2x.x.x` — hanya diperlukan jika anda mahu carian web SearXNG pilihan |

Jika sesuatu hilang, pemasang menawarkan untuk memasangnya untuk anda dengan `apt` (pada Debian/Ubuntu). Pada sistem lain, pasang terlebih dahulu dengan pengurus pakej anda.

Anda juga memerlukan dua perkara dari Telegram (kedua-duanya percuma):

1. **Token bot** — bercakap dengan [@BotFather](https://t.me/BotFather) di Telegram, hantar `/newbot`, dan salin token yang diberikan.
2. **ID pengguna Telegram numerik anda** — bercakap dengan [@userinfobot](https://t.me/userinfobot) dan salin nombor yang dipaparkan. Ini adalah ID "bos" anda: hanya akaun ini boleh menggunakan `/admin`.

## Pasang

Satu arahan. Salin, tampal ke terminal anda, dan tekan Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Pemasang menanya anda enam soalan, mengikut susunan:

1. **Negara** — salin nama Inggeris negara anda **persis seperti yang tersenarai dalam [jadual negara](#countries) di bawah** (contohnya `Turkey`). Negara menentukan zon masa, mata wang tempatan untuk harga, waktu solat, dan kandungan tempatan.
2. **Bahasa** — bahasa yang digunakan bot (contohnya `en`, `fa`, `tr`). Tekan Enter untuk menerima lalai bagi negara anda. Bahasa berbeza dari negara: ia hanya menukar apa yang bot katakan, dan anda boleh menukarnya kemudian dari `/admin`.
3. **Token bot** — salin token dari [@BotFather](https://t.me/BotFather). Pemasang menyemaknya secara langsung dengan Telegram.
4. **ID numerik Boss** — ID pengguna Telegram anda dari [@userinfobot](https://t.me/userinfobot).
5. **Nama bot / perkata bangun** — nama yang orang sebut dalam kumpulan untuk bercakap dengan bot. Sesapa bahasa pun boleh (contohnya `Vortex` atau `ورتکس`). Tekan Enter untuk lalai `Vortex`.
6. **Penyedia LLM pertama** — pilih satu: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, atau **Custom** (salin URL asas). Kemudian salin kunci API untuk penyedia itu — pemasang akan ambil senarai model langsung dari penyedia dan anda pilih model.

Kemudian pemasang memasang kebergantungan, menulis fail `.env`, mencipta perkhidmatan systemd `vortex-bot`, menawarkan memasang SearXNG untuk carian web (perlu Docker), dan memulakan bot.

> ⚠️ **Anthropic tidak berfungsi secara langsung.** API asli Anthropic tidak serasi dengan OpenAI, dan bot ini hanya bercakap API serasi OpenAI. Jika anda pilih Anthropic, pemasang akan amaran: kunci hanya berfungsi melalui gerbang serasi OpenAI. Gunakan OpenRouter, atau penyedia lain dari senarai, sebagai gantinya.

## Selepas memasang

Semak bahawa bot sedang berjalan:

```bash
systemctl status vortex-bot
```

Anda patut nampak `active (running)`. Untuk tonton log langsung:

```bash
journalctl -u vortex-bot -f
```

Sekarang buka Telegram dan bercakap dengan bot anda:

- Hantar `/start` — bot menyapa.
- Dalam **cakap peribadi**, tulis terus kepadanya — tiada perkata bangun diperlukan.
- Dalam **kumpulan**, tambah bot ke kumpulan, lalu sebut namanya, contohnya: `Vortex pukul berapa sekarang?`
- Sebagai boss, hantar `/admin` dalam cakap peribadi untuk buka panel admin tersembunyi.

**Kemaskini automatik.** Sekali sehari bot semak GitHub untuk rilah baru. Jika ada, ia hantar mesej peribadi kepada anda dengan butang ✅ / ❌. Tekan ✅ dan ia kemaskini sendiri dan mulakan semula — anda tidak perlu sentuh server.

## Konfigurasi

Semua tetapan berada dalam fail `.env` di direktori pemasangan. Lihat [`.env.example`](.env.example) untuk setiap pilihan. Yang paling penting:

| Setting | Apa fungsinya |
| --- | --- |
| `BOT_TOKEN` | Token bot Telegram anda (dari @BotFather) |
| `BOSS_ID` | ID pengguna Telegram numerik anda (pemilik bot) |
| `BOT_NAME` | Nama bot dan kata bangun dalam kumpulan (lalai `Vortex`) |
| `BOT_COUNTRY` | Negara dalam Bahasa Inggeris, cth. `United States` (tetapkan zon masa, mata wang, waktu solat) |
| `BOT_LANGUAGE` | Kod bahasa bot, cth. `en`, `fa`, `tr` (hanya menukar apa yang bot katakan) |
| `LLM_PROVIDERS` | Penyedia LLM dan kunci: `base_url\|api_key\|model`, dipisahkan koma |
| `UPDATE_CHECK_ENABLED` | `1` = semak kemas kini harian, `0` = tidak pernah semak |
| `UPDATE_REPO` | Repo yang release-nya dipantau (lalai `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Carian web: `searxng` (lalai), `tavily`, atau `serper` |
| `DAILY_LIMIT_MESSAGES` | Maks balasan bot per pengguna per hari (lalai `30`, boss dikecualikan) |

Negara dan bahasa boleh diubah kemudian dari panel `/admin` tersembunyi (Bahasa & Negara), tanpa mengedit sebarang fail.

## Alternatif Docker

Jika anda lebih gemar Docker berbanding pemasang:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Ini menjalankan bot bersama enjin carian SearXNG yang dihost sendiri. Semak log dengan `docker compose logs -f bot`.

Nota: pengecek kemas kini automatik memerlukan perkhidmatan systemd, jadi dalam Docker kemas kini adalah manual: `git pull` dan kemudian `docker compose up -d --build` sekali lagi.

## Fitur secara terperinci

### Panel /admin

Hantar `/admin` dalam perbualan persendirian (hanya boss — tiada sesiapa lain boleh membukanya, dan ia tidak pernah muncul dalam `/help` atau menu). Ia mempunyai:

- 🔑 **Token & model** — tambah atau buang kunci LLM, lihat kunci mana yang sihat, pilih model aktif, layari senarai model langsung penyedia
- 👥 **Pengguna** — kiraan pengguna, ban / unban, senarai benar
- 📊 **Statistik** — angka penggunaan
- 💬 **Perbualan terkini** — apa yang orang katakan kepada bot (hanya boss, persendirian)
- 🖼️ **Model imej** — DuckAI (percuma, lalai), HiLinkUp, perkhidmatan imej tersuai, atau ditutup
- 🛡️ **Pengurus** — beri orang dipercayai akses ke bahagian panel
- 🟢/🔴 **Kuasa** — hidupkan atau matikan bot untuk semua orang (boss kekal kawal)
- 🌍 **Bahasa & Negara** — tukar bahasa atau negara bot bila-bila masa

### Kolam token

Bot boleh menyimpan kunci dari beberapa penyedia LLM sekaligus. Ia berputar antara kunci sihat dan gagal ke kunci lain secara automatik apabila satu berhenti berfungsi. Daripada `/admin` anda boleh tetapkan satu model, pilih model secara manual, atau biarkan bot berputar bebas. Mana-mana penyedia dengan API yang serasi OpenAI berfungsi — termasuk pengumpul kecil, bukan hanya nama-nama besar.

### Imej

Penjanaan imej mempunyai tiga mod: **DuckAI** (percuma, tiada kunci, lalai), **HiLinkUp** (berbayar, kualiti lebih baik), atau perkhidmatan imej **tersuai** serasi OpenAI milik anda sendiri. Anda juga boleh hantar foto kepada bot dan suruh mengeditnya ("jadikan ini gaya kartun"), dan ia akan menjana imej baharu. Penjanaan imej boleh dimatikan dari `/admin`.

### Negara dan bahasa

Vortex menyokong **195 negara** dan **40 bahasa**. Negara menentukan zon masa, matawang harga dipaparkan, bandar yang digunakan untuk waktu solat, dan kandungan tempatan. Bahasa hanya menentukan apa yang bot katakan — kumpulan di Belgium boleh menggunakan negara Belgium dan bahasa English, sebagai contoh. Kedua-duanya boleh diubah kemudian dari `/admin`.

### Kemas Kini

Bot memeriksa keluar GitHub `VortexLabsHQ/vortex-telegram-bot` sekali sehari. Apabila versi baru keluar, ia menghantar mesej peribadi kepada bos dengan butang ✅ / ❌. Menerima akan mengemas kini kod dan mulakan semula bot. Semasa repo persendirian, semakan diam-diam tidak melakukan apa-apa (API GitHub memerlukan repo awam) — tetapkan `UPDATE_CHECK_ENABLED=0` jika anda tidak pernah mahu semakan itu.

## Penyelesaian Masalah / Soalan Lazim

**Pemasang menyatakan token saya tidak sah.**
Token berasal dari [@BotFather](https://t.me/BotFather). Pastikan anda menyalin keseluruhan token (digit, dua titik, kemudian 35+ aksara), tanpa ruang tambahan. Jika anda memadam bot atau membuat token baru, yang lama berhenti berfungsi — tampal yang baru.

**Bot tidak menjawab dalam kumpulan saya.**
Tiga perkara untuk diperiksa: (1) bot mesti ditambah ke kumpulan, (2) anda mesti sebut perkata bangunnya — namanya, contohnya `Vortex what's the time?` — bot hanya mendengar apabila namanya disebut dalam kumpulan, (3) dalam perbualan persendirian tiada perkata bangun diperlukan langsung.

**Bot menjawab dalam English, bukan bahasa saya.**
Hantar `/admin` (bos sahaja) → Bahasa & Negara, dan pilih bahasa anda. Pemasang juga menanyakan bahasa — tekan Enter di sana untuk menerima lalai negara anda.

**Saya memilih Anthropic dan bot tidak bercakap.**
API asli Anthropic tidak serasi dengan OpenAI, jadi bot tidak boleh bercakap dengannya secara langsung. Gunakan OpenRouter (yang boleh mengkhidmatkan model Claude melalui API serasi OpenAI), atau pilih penyedia lain dari senarai.

**Carian web tidak berfungsi.**
Carian web memerlukan SearXNG, yang pemasang tawarkan untuk disediakan dengan Docker. Tanpa itu, bot kembali ke Wikipedia, yang lebih lemah. Anda juga boleh tetapkan `SEARCH_PROVIDER=tavily` atau `serper` dengan `SEARCH_API_KEY` dalam `.env`.

**Di mana log-log?**
`journalctl -u vortex-bot -f` memaparkan log langsung. `systemctl status vortex-bot` memaparkan sama ada perkhidmatan berjalan. Jika bot berhenti, `sudo systemctl restart vortex-bot` mulakannya semula.

**Bot menyatakan saya telah mencapai had harian.**
Setiap pengguna mendapat 30 balasan bot sehari (bos dikecualikan). Had set semula pada tengah malam mengikut zon masa negara bot. Tingkatkan dengan `DAILY_LIMIT_MESSAGES` dalam `.env`, atau tanya bos.

**Saya jumpa ralat / saya ada idea.**
Sila buka isu di GitHub — lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk cara melaporkannya dan cara menghantar pembetulan.

## Pembangunan

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

Jalankan ujian (skrip Python biasa, pytest tidak diperlukan):

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

Kesembilan suite mesti lulus sebelum anda membuka permintaan tarik. Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk gaya kod (ruff) dan proses PR.

## Lesen

Vortex dikeluarkan di bawah [Lesen MIT](LICENSE) — bebas untuk digunakan, disalin, diubah, dan dikongsi, untuk mana-mana tujuan.

<a id="countries"></a>

## Negara

Tampalkan nama negara **dalam Bahasa Inggeris, persis seperti yang ditulis di sini** apabila pemasang meminta negara anda. Jadual ini dijana daripada `bot/countries.py` — sekiranya nama di sini dan nama di sana tidak sepadan, `bot/countries.py` yang menentukan.

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

## Terima kasih

> ⭐ **Sila beri bintang projek ini di GitHub dan ikuti [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — ia adalah cara paling mudah untuk menyokong Vortex dan membantu orang lain menemuinya. Terima kasih!
