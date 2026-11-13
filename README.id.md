# Vortex 🤖 — Asisten grup Telegram Anda sendiri

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Bahasa Indonesia** · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Jika Anda suka Vortex, silakan beri bintang proyek ini di GitHub dan ikuti [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — ini membantu lebih banyak orang menemukannya. Terima kasih!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Apa itu Vortex?

Vortex adalah bot Telegram yang berada di grup dan obrolan pribadi Anda dan menjawab orang dengan model obrolan AI. Anda sebut namanya (nama defaultnya adalah **Vortex**) dan dia akan membalas — dia bisa mengobrol, mencari web, membuat gambar, memeriksa harga, bercerita lelucon, membaca file, mentranskripsi pesan suara, dan banyak lagi.

Ini berjalan di server Anda sendiri, di negara dan bahasa Anda sendiri. Anda adalah bos: panel `/admin` tersembunyi memungkinkan Anda mengelola kunci AI, pengguna, dan pengaturan.

## Fitur

- 💬 **AI chat** di grup (kata pemicu) dan obrolan pribadi (tidak perlu kata pemicu)
- 🔑 **Token pool** — gunakan beberapa penyedia dan kunci LLM, putar dan failover otomatis
- 🖼️ **Image generation and editing** — gratis (DuckAI) atau penyedia berbayar
- 🔍 **Web search** — SearXNG self-hosted, dengan cadangan Wikipedia
- 💰 **Live prices** — mata uang, emas, minyak, dan kripto dalam mata uang lokal Anda
- 🕌 **Jadwal sholat**, 🃏 **ramalan**, 😄 **lelucon**, 🎲 **dadu dan lempar koin**
- 📎 **Analisis file** dan **transkripsi suara**
- 📥 **Unduhan** — kirim tautan, dapatkan file media kembali (maks 45 MB)
- 🌍 **195 negara** dan **40 bahasa** — negara dan bahasa adalah pengaturan terpisah
- 🔄 **Pembaruan otomatis** — memeriksa rilis baru setiap hari dan meminta konfirmasi sebelum memperbarui
- 🛡️ **Tersembunyi /admin panel** — token, pengguna, statistik, obrolan, model gambar, manajer, kekuasaan

## Sebelum menginstal

Anda memerlukan server (atau komputer yang tetap menyala) yang menjalankan **Linux** dengan hal-hal berikut terinstal:

| Apa | Cara memeriksa | Yang seharusnya Anda lihat |
| --- | --- | --- |
| **Python 3.11 atau lebih baru** | `python3 --version` | `Python 3.11.x` atau lebih tinggi (3.12 dan 3.13 juga berfungsi) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` atau `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` atau serupa |
| **Docker** *(opsional)* | `docker --version` | `Docker version 2x.x.x` — hanya diperlukan jika Anda ingin pencarian web SearXNG opsional |

Jika ada yang hilang, penginstal menawarkan untuk menginstalnya untuk Anda dengan `apt` (pada Debian/Ubuntu). Pada sistem lain, instal terlebih dahulu dengan manajer paket Anda.

Anda juga memerlukan dua hal dari Telegram (keduanya gratis):

1. **Token bot** — bicaralah dengan [@BotFather](https://t.me/BotFather) di Telegram, kirim `/newbot`, dan salin token yang diberikan.
2. **ID pengguna Telegram numerik Anda** — bicaralah dengan [@userinfobot](https://t.me/userinfobot) dan salin nomor yang ditampilkan. Ini adalah ID "bos" Anda: hanya akun ini yang dapat menggunakan `/admin`.

## Instalasi

Satu perintah. Salin, tempel di terminal Anda, dan tekan Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Penginstal akan menanyakan enam pertanyaan, secara berurutan:

1. **Negara** — tempel nama bahasa Inggris negara Anda **persis seperti yang tercantum di [tabel negara](#countries) di bawah** (misalnya `Turkey`). Negara menentukan zona waktu, mata uang lokal untuk harga, waktu sholat, dan konten lokal.
2. **Bahasa** — bahasa yang digunakan bot (misalnya `en`, `fa`, `tr`). Tekan Enter untuk menerima default negara Anda. Bahasa terpisah dari negara: hanya mengubah apa yang dikatakan bot, dan bisa diubah nanti lewat `/admin`.
3. **Token bot** — tempel token dari [@BotFather](https://t.me/BotFather). Installer memeriksanya langsung dengan Telegram.
4. **ID numerik Boss** — ID pengguna Telegram Anda dari [@userinfobot](https://t.me/userinfobot).
5. **Nama bot / kata pemicu** — nama yang diucapkan orang di grup untuk berbicara dengan bot. Bahasa apa pun boleh (misalnya `Vortex` atau `ورتکس`). Tekan Enter untuk default `Vortex`.
6. **Penyedia LLM pertama** — pilih satu: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, atau **Custom** (tempel base URL). Lalu tempel API key untuk penyedia tersebut — installer mengambil daftar model langsung dari penyedia dan Anda memilih modelnya.

Kemudian installer memasang dependensi, menulis file `.env`, membuat layanan systemd `vortex-bot`, menawarkan memasang SearXNG untuk pencarian web (butuh Docker), dan memulai bot.

> ⚠️ **Anthropic tidak bekerja langsung.** API native Anthropic tidak kompatibel dengan OpenAI, dan bot ini hanya berbicara API yang kompatibel OpenAI. Jika Anda memilih Anthropic, installer memperingatkan: key hanya berfungsi melalui gateway yang kompatibel OpenAI. Gunakan OpenRouter, atau penyedia lain dari daftar, sebagai gantinya.

## Setelah memasang

Periksa apakah bot berjalan:

```bash
systemctl status vortex-bot
```

Seharusnya tertulis `active (running)`. Untuk melihat log langsung:

```bash
journalctl -u vortex-bot -f
```

Sekarang buka Telegram dan obrol dengan bot Anda:

- Kirim `/start` — bot menyapa.
- Di **obrolan pribadi**, cukup tulis ke bot — tidak perlu kata pemicu.
- Di **grup**, tambahkan bot ke grup, lalu sebut namanya, misalnya: `Vortex jam berapa sekarang?`
- Sebagai boss, kirim `/admin` di obrolan pribadi untuk membuka panel admin tersembunyi.

**Pembaruan otomatis.** Setiap hari bot memeriksa GitHub untuk rilis baru. Jika tersedia, bot mengirim pesan pribadi ke Anda dengan tombol ✅ / ❌. Tekan ✅ dan bot memperbarui dirinya sendiri lalu restart — Anda tidak pernah perlu menyentuh server.

## Konfigurasi

Semua pengaturan berada di file `.env` di direktori pemasangan. Lihat [`.env.example`](.env.example) untuk setiap opsi. Yang paling penting:

| Setting | What it does |
| --- | --- |
| `BOT_TOKEN` | Token bot Telegram Anda (dari @BotFather) |
| `BOSS_ID` | ID pengguna Telegram numerik Anda (pemilik bot) |
| `BOT_NAME` | Nama bot dan kata pemicu di grup (default `Vortex`) |
| `BOT_COUNTRY` | Negara dalam bahasa Inggris, mis. `United States` (menetapkan zona waktu, mata uang, jadwal sholat) |
| `BOT_LANGUAGE` | Kode bahasa bot, mis. `en`, `fa`, `tr` (hanya mengubah ucapan bot) |
| `LLM_PROVIDERS` | Penyedia LLM dan kunci: `base_url\|api_key\|model`, dipisahkan koma |
| `UPDATE_CHECK_ENABLED` | `1` = cek update harian, `0` = tidak pernah cek |
| `UPDATE_REPO` | Repo yang rilisnya dipantau (default `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Pencarian web: `searxng` (default), `tavily`, atau `serper` |
| `DAILY_LIMIT_MESSAGES` | Maks balasan bot per pengguna per hari (default `30`, boss dikecualikan) |

Negara dan bahasa juga bisa diubah nanti dari panel `/admin` tersembunyi (Bahasa & Negara), tanpa mengedit file apa pun.

## Alternatif Docker

Jika Anda lebih suka Docker dibanding installer:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Ini menjalankan bot bersama mesin pencari SearXNG self-hosted. Cek log dengan `docker compose logs -f bot`.

Catatan: pembaruan otomatis butuh layanan systemd, jadi di Docker update manual: `git pull` lalu `docker compose up -d --build` lagi.

## Fitur secara detail

### Panel /admin

Kirim `/admin` di obrolan pribadi (hanya boss — orang lain tidak bisa buka, dan tidak muncul di `/help` atau menu). Isinya:

- 🔑 **Token & model** — tambah atau hapus kunci LLM, lihat kunci mana yang sehat, pilih model aktif, jelajahi daftar model langsung penyedia
- 👥 **Pengguna** — jumlah pengguna, ban / unban, daftar izin
- 📊 **Statistik** — angka penggunaan
- 💬 **Obrolan terbaru** — apa yang orang katakan ke bot (hanya boss, pribadi)
- 🖼️ **Model gambar** — DuckAI (gratis, default), HiLinkUp, layanan gambar kustom, atau mati
- 🛡️ **Manajer** — beri orang tepercaya akses ke bagian panel
- 🟢/🔴 **Daya** — nyalakan atau matikan bot untuk semua orang (boss tetap kontrol)
- 🌍 **Bahasa & Negara** — ubah bahasa atau negara bot kapan saja

### Kolam token

Bot bisa menyimpan kunci dari beberapa penyedia LLM sekaligus. Ia berputar antar kunci sehat dan failover otomatis saat satu berhenti bekerja. Dari `/admin` Anda bisa menancapkan satu model, memilih model manual, atau biarkan bot berputar bebas. Penyedia apa pun dengan API kompatibel OpenAI bekerja — termasuk agregator kecil, bukan hanya nama besar.

### Gambar

Pembuatan gambar punya tiga mode: **DuckAI** (gratis, tanpa kunci, default), **HiLinkUp** (berbayar, kualitas lebih baik), atau layanan gambar **kustom** kompatibel OpenAI milik Anda sendiri. Anda juga bisa kirim foto ke bot dan suruh diedit ("buat gaya kartun"), dan bot akan buat gambar baru. Pembuatan gambar bisa dimatikan dari `/admin`.

### Negara dan bahasa

Vortex mendukung **195 negara** dan **40 bahasa**. Negara menentukan zona waktu, mata uang yang ditampilkan, kota untuk waktu sholat, dan konten lokal. Bahasa hanya mengatur apa yang dikatakan bot — misalnya grup di Belgia bisa menggunakan negara Belgia dan bahasa Inggris. Keduanya bisa diubah nanti dari `/admin`.

### Pembaruan

Bot memeriksa rilis GitHub dari `VortexLabsHQ/vortex-telegram-bot` sekali sehari. Saat versi baru keluar, bot mengirim pesan pribadi ke boss dengan tombol ✅ / ❌. Menerima akan memperbarui kode dan me-restart bot. Selama repo bersifat pribadi, pemeriksaan diam-diam tidak melakukan apa-apa (API GitHub butuh repo publik) — atur `UPDATE_CHECK_ENABLED=0` jika Anda tidak pernah ingin pemeriksaan ini.

## Pemecahan Masalah / FAQ

**Installer mengatakan token saya tidak valid.**
Token berasal dari [@BotFather](https://t.me/BotFather). Pastikan Anda menyalin seluruh token (angka, titik dua, lalu 35+ karakter), tanpa spasi ekstra. Jika Anda menghapus bot atau membuat token baru, yang lama berhenti bekerja — tempel yang baru.

**Bot tidak menjawab di grup saya.**
Tiga hal untuk diperiksa: (1) bot harus ditambahkan ke grup, (2) Anda harus mengucapkan kata pemicunya — namanya, misalnya `Vortex jam berapa?` — bot hanya mendengar saat namanya disebut di grup, (3) di obrolan pribadi tidak perlu kata pemicu sama sekali.

**Bot menjawab dalam bahasa Inggris, bukan bahasa saya.**
Kirim `/admin` (hanya boss) → Bahasa & Negara, dan pilih bahasa Anda. Installer juga menanyakan bahasa — tekan Enter di sana untuk menerima default negara Anda.

**Saya memilih Anthropic tapi bot tidak ngobrol.**
API native Anthropic tidak kompatibel dengan OpenAI, jadi bot tidak bisa ngobrol dengannya langsung. Gunakan OpenRouter (yang bisa melayani model Claude lewat API kompatibel OpenAI), atau pilih penyedia lain dari daftar.

**Pencarian web tidak berfungsi.**
Pencarian web butuh SearXNG, yang installer tawarkan untuk di-setup dengan Docker. Tanpa itu, bot fallback ke Wikipedia, yang lebih lemah. Anda juga bisa atur `SEARCH_PROVIDER=tavily` atau `serper` dengan `SEARCH_API_KEY` di `.env`.

**Log ada di mana?**
`journalctl -u vortex-bot -f` menampilkan log langsung. `systemctl status vortex-bot` menampilkan apakah service berjalan. Jika bot berhenti, `sudo systemctl restart vortex-bot` memulainya lagi.

**Bot bilang saya mencapai batas harian.**
Setiap user dapat 30 balasan bot per hari (boss dikecualikan). Batas reset di tengah malam di zona waktu negara bot. Tingkatkan dengan `DAILY_LIMIT_MESSAGES` di `.env`, atau tanya ke boss.

**Saya nemu bug / punya ide.**
Silakan buka issue di GitHub — lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk cara melaporkan dan mengirim perbaikan.

## Pengembangan

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

Jalankan tes (skrip Python biasa, tidak perlu pytest):

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

Semua sembilan suite harus lolos sebelum Anda buka pull request. Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk gaya kode (ruff) dan proses PR.

## Lisensi

Vortex dirilis di bawah [Lisensi MIT](LICENSE) — bebas digunakan, disalin, diubah, dan dibagikan, untuk tujuan apa pun.

<a id="countries"></a>

## Negara

Tempel nama negara **dalam bahasa Inggris, persis seperti yang tertulis di sini** saat installer meminta negara Anda. Tabel dibuat dari `bot/countries.py` — jika nama di sini dan nama di sana tidak sepakat, `bot/countries.py` yang berlaku.

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

> ⭐ **Silakan beri bintang proyek ini di GitHub dan ikuti [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — itu adalah cara termudah untuk mendukung Vortex dan membantu orang lain menemukannya. Terima kasih!
