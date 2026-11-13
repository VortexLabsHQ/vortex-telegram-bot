# Vortex 🤖 — Kendi Telegram grup asistanınız

[English](README.md) · [فارسی](README.fa.md) · **Türkçe** · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Vortex'i beğendiyseniz, GitHub'da bu projeyi yıldızlayın ve [@VortexLabsHQ](https://github.com/VortexLabsHQ)'yi takip edin** — bu sayede daha fazla insan bulabilir. Teşekkürler!

[![Lisans: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex nedir?

Vortex, gruplarınızda ve özel sohbetlerinizde yaşayan, bir AI sohbet modeliyle insanlara cevap veren bir Telegram botudur. Adını söylersiniz (varsayılan isim **Vortex**) ve cevap verir — sohbet edebilir, web'de arama yapabilir, resim oluşturabilir, fiyatları kontrol edebilir, şaka yapabilir, dosyaları okuyabilir, ses mesajlarını yazıya çevirebilir ve daha fazlası.

Kendi sunucunuzda, kendi ülkenizde ve dilinizde çalışır. Siz patronusunuz: gizli bir `/admin` paneli AI anahtarlarını, kullanıcıları ve ayarları yönetmenizi sağlar.

## Özellikler

- 💬 **AI sohbeti** gruplarda (uyanma kelimesiyle) ve özel sohbetlerde (uyanma kelimesi gerekmez)
- 🔑 **Token havuzu** — birkaç LLM sağlayıcısı ve anahtarı kullanın, otomatik olarak değiştirin ve hata durumunda yedek devreye girsin
- 🖼️ **Resim oluşturma ve düzenleme** — ücretsiz (DuckAI) veya ücretli sağlayıcılar
- 🔍 **Web araması** — kendi barındırdığınız SearXNG, Vikipedi yedeğiyle
- 💰 **Canlı fiyatlar** — para birimleri, altın, petrol ve kripto paralar yerel para biriminizde
- 🕌 **Ezan vakitleri**, 🃏 **fal**, 😄 **şakalar**, 🎲 **zar ve yazı-tura**
- 📎 **Dosya analizi** ve **ses yazıya çevirme**
- 📥 **İndirmeler** — link gönderin, medya dosyasını alın (45 MB'a kadar)
- 🌍 **195 ülke** ve **40 dil** — ülke ve dil ayrı ayarlar
- 🔄 **Kendi kendini güncelleme** — günde bir yeni sürüm kontrol eder, güncellemeden önce onayınızı ister
- 🛡️ **Gizli /admin paneli** — tokenlar, kullanıcılar, istatistikler, sohbetler, resim modeli, yöneticiler, güç

## Kurulumdan önce

Şunları çalıştıran bir sunucunuza (veya açık kalan bir bilgisayarınıza) ihtiyacınız var: **Linux** şunlar kurulu:

| Ne | Nasıl kontrol edilir | Ne görmelisiniz |
| --- | --- | --- |
| **Python 3.11 veya üzeri** | `python3 --version` | `Python 3.11.x` veya üzeri (3.12 ve 3.13 de çalışır) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` veya `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` veya benzeri |
| **Docker** *(isteğe bağlı)* | `docker --version` | `Docker version 2x.x.x` — sadece isteğe bağlı SearXNG web araması için gerekli |

Eksik bir şey varsa, kurulum programı `apt` ile (Debian/Ubuntu'da) sizin için kurmayı teklif eder. Diğer sistemlerde, önce paket yöneticinizle kurun.

Telegram'dan ücretsiz olarak almanız gereken iki şey daha var:

1. **Bot token'ı** — Telegram'da [@BotFather](https://t.me/BotFather) ile konuşun, `/newbot` gönderin ve size verdiği token'ı kopyalayın.
2. **Sayısal Telegram kullanıcı ID'niz** — [@userinfobot](https://t.me/userinfobot) ile konuşun ve gösterdiği numarayı kopyalayın. Bu sizin "patron" ID'niz: sadece bu hesap `/admin` kullanabilir.

## Kurulum

Tek komut. Kopyalayın, terminalinize yapıştırın ve Enter'a basın:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Kurulum programı size sırayla altı soru sorar:

1. **Ülke** — ülkenizin İngilizce adını **aşağıdaki [ülke tablosunda](#countries) listelendiği gibi tam olarak** yapıştırın (örneğin `Turkey`). Ülke, saat dilimini, fiyatlar için yerel para birimini, ezan vakitleri için şehri ve yerel içeriği belirler.
2. **Dil** — botun konuşacağı dil (örneğin `en`, `fa`, `tr`). Ülkenizin varsayılanını kabul etmek için Enter'a basın. Dil ülkenizden ayrıdır: sadece botun ne söylediğini değiştirir, daha sonra `/admin` panelinden değiştirebilirsiniz.
3. **Bot token'ı** — [@BotFather](https://t.me/BotFather)'dan aldığınız token'ı yapıştırın. Kurulum programı bunu Telegram ile canlı olarak kontrol eder.
4. **Patron sayısal ID** — [@userinfobot](https://t.me/userinfobot)'tan aldığınız Telegram kullanıcı ID'niz.
5. **Bot adı / uyanma kelimesi** — gruplarda botla konuşmak için söylenen isim. Herhangi bir dil olabilir (örneğin `Vortex` veya `ورتکس`). Varsayılan `Vortex` için Enter'a basın.
6. **İlk LLM sağlayıcısı** — birini seçin: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, veya **Özel** (bir temel URL yapıştırın). Sonra o sağlayıcı için API anahtarınızı yapıştırın — kurulum programı sağlayıcının canlı model listesini getirir ve siz bir model seçersiniz.

Sonra kurulum programı bağımlılıkları kurar, `.env` dosyasını yazar, `vortex-bot` systemd servisini oluşturur, web araması için SearXNG kurmayı teklif eder (Docker gerekir) ve botu başlatır.

> ⚠️ **Anthropic doğrudan çalışmaz.** Anthropic'in yerel API'si OpenAI-uyumlu değildir, ve bu bot sadece OpenAI-uyumlu API'leri konuşur. Anthropic'i seçerseniz, kurulum programı sizi uyarır: anahtar sadece OpenAI-uyumlu bir geçit (gateway) üzerinden çalışır. Bunun yerine listeden OpenRouter veya başka bir sağlayıcıyı kullanın.

## Kurulumdan sonra

Botun çalıştığını kontrol edin:

```bash
systemctl status vortex-bot
```

`active (running)` görmelisiniz. Canlı günlüğü izlemek için:

```bash
journalctl -u vortex-bot -f
```

Şimdi Telegram'u açın ve botunuzla konuşun:

- `/start` gönderin — bot selamlar.
- **Özel sohbetlerde**, sadece yazın — uyanma kelimesi gerekmez.
- **Gruplarda**, botu gruba ekleyin, sonra adını söyleyin, örneğin: `Vortex saat kaç?`
- Patron olarak, özel sohbette `/admin` gönderin gizli admin panelini açmak için.

**Güncellemeler otomatik.** Günde bir bot GitHub'da yeni sürüm kontrol eder. Varsa, size özel mesajla ✅ / ❌ butonlarıyla haber verir. ✅'e basarsanız kendini günceller ve yeniden başlatır — sunucuya tekrar dokunmanıza gerek kalmaz.

## Yapılandırma

Tüm ayarlar kurulum dizinindeki `.env` dosyasında. Her seçenek için [`.env.example`](.env.example) dosyasına bakın. En önemli olanlar:

| Ayar | Ne işe yarar |
| --- | --- |
| `BOT_TOKEN` | Telegram bot token'ınız (@BotFather'dan) |
| `BOSS_ID` | Sayısal Telegram kullanıcı ID'niz (bot sahibi) |
| `BOT_NAME` | Botun adı ve gruplardaki uyanma kelimesi (varsayılan `Vortex`) |
| `BOT_COUNTRY` | İngilizce ülke adı, örn. `United States` (saat dilimi, para birimi, ezan vakitlerini belirler) |
| `BOT_LANGUAGE` | Bot dil kodu, örn. `en`, `fa`, `tr` (sadece botun ne söylediğini değiştirir) |
| `LLM_PROVIDERS` | LLM sağlayıcıları ve anahtarları: `base_url\|api_key\|model`, virgülle ayrılmış |
| `UPDATE_CHECK_ENABLED` | `1` = günde bir güncelleme kontrol et, `0` = asla kontrol etme |
| `UPDATE_REPO` | İzlenen sürümlerin deposu (varsayılan `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Web araması: `searxng` (varsayılan), `tavily`, veya `serper` |
| `DAILY_LIMIT_MESSAGES` | Kullanıcı başına günde en fazla bot cevabı (varsayılan `30`, patron muaf) |

Ülke ve dil daha sonra gizli `/admin` panelinden de (Dil ve Ülke) değiştirilebilir, dosya düzenlemeden.

## Docker alternatifi

Kurulum programı yerine Docker tercih ederseniz:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Bu, botu kendi barındırılan SearXNG arama motoruyla birlikte başlatır. Günlükleri `docker compose logs -f bot` ile kontrol edin.

Not: otomatik kendi kendini güncelleyici systemd servisine ihtiyaç duyar, bu yüzden Docker'da güncellemeler manuel: `git pull` ve sonra tekrar `docker compose up -d --build`.

## Özellikler detaylı

### /admin paneli

Özel sohbette `/admin` gönderin (sadece patron — kimse açamaz, `/help` veya menülerde görünmez). Şunları içerir:

- 🔑 **Tokenlar ve model** — LLM anahtarları ekleyin/kaldırın, hangi anahtarların sağlıklı olduğunu görün, aktif modeli seçin, sağlayıcının canlı model listesine göz atın
- 👥 **Kullanıcılar** — kullanıcı sayıları, yasakla/yasak kaldır, izin listesi
- 📊 **İstatistikler** — kullanım sayıları
- 💬 **Son sohbetler** — insanlar bota ne yazdı (sadece patron, özel)
- 🖼️ **Resim modeli** — DuckAI (ücretsiz, varsayılan), HiLinkUp, özel bir resim servisi, veya kapalı
- 🛡️ **Yöneticiler** — güvenilen kişilere panelin kısımlarına erişim verin
- 🟢/🔴 **Güç** — botu herkes için açın/kapatın (patron her zaman kontrol eder)
- 🌍 **Dil ve Ülke** — botun dilini veya ülkesini istediğiniz zaman değiştirin

### Token havuzu

Bot aynı anda birkaç LLM sağlayıcısından anahtar tutabilir. Sağlıklı anahtarlar arasında döner ve biri çalışmazsa otomatik olarak yedek devreye girer. `/admin` panelinden bir modeli sabitleyebilir, elle model seçebilir, veya botun serbestçe dönmesine bırakabilirsiniz. OpenAI-uyumlu API'si olan herhangi bir sağlayıcı çalışır — büyük isimler değil, küçük toplayıcılar da dahil.

### Resimler

Resim oluşturma üç modda: **DuckAI** (ücretsiz, anahtar gerekmez, varsayılan), **HiLinkUp** (ücretli, daha iyi kalite), veya kendi **özel** OpenAI-uyumlu resim servisiniz. Bot'a fotoğraf da gönderebilir ve nasıl düzenlemesini söyleyebilirsiniz ("bunu çizgi film yap"), ve yeni bir resim oluşturur. Resim oluşturma `/admin` panelinden kapatılabilir.

### Ülkeler ve diller

Vortex **195 ülke** ve **40 dil** destekler. Ülke saat dilimini, fiyatların gösterileceği para birimini, ezan vakitleri için kullanılacak şehri ve yerel içeriği belirler. Dil sadece botun ne söylediğini belirler — örneğin Belçika grubu ülke olarak Belçika, dil olarak İngilizce kullanabilir. İkisi de daha sonra `/admin` panelinden değiştirilebilir.

### Güncellemeler

Bot `VortexLabsHQ/vortex-telegram-bot` deposunun GitHub sürümlerini günde bir kontrol eder. Yeni sürüm çıktığında, patrona özel mesajla ✅ / ❌ butonlarıyla haber verir. Kabul ederseniz kodu günceller ve botu yeniden başlatır. Depo özel (private) olduğu sürece kontrol sessizce hiçbir şey yapmaz (GitHub API'si genel repo ister) — asla kontrol istemiyorsanız `UPDATE_CHECK_ENABLED=0` yapın.

## Sorun giderme / SSS

**Kurulum programı token'ım geçersiz diyor.**
Token [@BotFather](https://t.me/BotFather)'dan gelir. Tüm token'ı kopyaladığınızdan emin olun (rakamlar, iki nokta üst üste, sonra 35+ karakter), fazladan boşluk olmadan. Botu sildiniz veya yeni token aldıysanız eski çalışmaz — yenisini yapıştırın.

**Bot grubumda cevap vermiyor.**
Üç şeyi kontrol edin: (1) bot gruba eklenmiş olmalı, (2) uyanma kelimesini — yani adını — söylemeli, örneğin `Vortex saat kaç?` — bot gruplarda sadece adı söylendiğinde dinler, (3) özel sohbetlerde hiç uyanma kelimesi gerekmez.

**Bot benim dilimde değil, İngilizce cevap veriyor.**
`/admin` gönderin (sadece patron) → Dil ve Ülke, dilinizi seçin. Kurulum programı da dil sorar — orada Enter'a basarak ülkenizin varsayılanını kabul edebilirsiniz.

**Anthropic seçtim ve bot sohbet etmiyor.**
Anthropic'in yerel API'si OpenAI-uyumlu değil, bu yüzden bot doğrudan onunla sohbet edemez. OpenRouter kullanın (Claude modellerini OpenAI-uyumlu API ile sunar), veya listeden başka bir sağlayıcı seçin.

**Web araması çalışmıyor.**
Web araması SearXNG gerektirir, kurulum programı Docker ile kurmayı teklif eder. Olmadan bot Vikipedi'ye yedeğe döner, bu daha zayıftır. `.env` dosyasında `SEARCH_PROVIDER=tavily` veya `serper` ve bir `SEARCH_API_KEY` de ayarlayabilirsiniz.

**Günlükler nerede?**
`journalctl -u vortex-bot -f` canlı günlüğü gösterir. `systemctl status vortex-bot` servisin çalışıp çalışmadığını gösterir. Bot durursa, `sudo systemctl restart vortex-bot` ile tekrar başlatırsınız.

**Bot günde limitime ulaştığımı söylüyor.**
Her kullanıcı günde 30 bot cevabı alır (patron muaf). Limit, botun ülke saat diliminde gece yarısı sıfırlanır. `.env` dosyasındaki `DAILY_LIMIT_MESSAGES` ile artırın, veya patrondan isteyin.

**Bir hata buldum / fikrim var.**
Lütfen GitHub'da bir issue açın — nasıl bildirileceği ve düzeltme nasıl gönderileceği için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

## Geliştirme

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

Testleri çalıştırın (sade Python betikleri, pytest gerekmez):

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

Tüm dokuz test paketi geçmeden pull request açmayın. Kod stili (ruff) ve PR süreci için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

## Lisans

Vortex [MIT Lisansı](LICENSE) altında yayınlanmıştır — herhangi bir amaçla kullanmak, kopyalamak, değiştirmek ve paylaşmak için ücretsizdir.

<a id="countries"></a>

## Ülkeler

Kurulum programı ülkenizi sorduğunda, ülke adını **İngilizce olarak, buradaki yazıldığı tam haliyle** yapıştırın. Tablo `bot/countries.py` dosyasından üretilmiştir — buradaki bir isimle oradaki bir isim uyuşmazsa, `bot/countries.py` geçerlidir.

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



## Teşekkürler

> ⭐ **Lütfen GitHub'da bu projeyi yıldızlayın ve [@VortexLabsHQ](https://github.com/VortexLabsHQ)'yi takip edin** — Vortex'i desteklemek ve başkalarının bulmasını sağlamak için en basit yoldur. Teşekkürler!