# Vortex 🤖 — Ваш власний помічник для груп у Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · **Українська** · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Якщо вам подобається Vortex, поставте зірку цьому проекту на GitHub і підпишіться на [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — це допоможе іншим знайти його. Дякуємо!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Що таке Vortex?

Vortex — це Telegram-бот, який живе у ваших групах і приватних чатах і відповідає людям за допомогою штучного інтелекту. Ви кажете його ім'я (за замовчуванням — **Vortex**), і він відповідає — може спілкуватися, шукати в інтернеті, створювати зображення, перевіряти ціни, розповідати жарти, читати файли, розпізнавати голосові повідомлення та інше.

Він працює на вашому власному сервері, у вашій країні і мові. Ви — головний: прихована панель `/admin` дозволяє керувати ключами AI, користувачами та налаштуваннями.

## Можливості

- 💬 **Чат з AI** у групах (слово-тригер) і приватних чатах (без слова-тригера)
- 🔑 **Пул токенів** — використовуйте кілька провайдерів LLM і ключів, автоматична ротація та перемикання при збоях
- 🖼️ **Генерація та редагування зображень** — безкоштовно (DuckAI) або платні провайдери
- 🔍 **Пошук у вебі** — власний SearXNG, з резервним Wikipedia
- 💰 **Актуальні ціни** — валюти, золото, нафта та крипта у вашій валюті
- 🕌 **Час молитви**, 🃏 **передбачення**, 😄 **жарти**, 🎲 **кубики та підкидання монети**
- 📎 **Аналіз файлів** та **розпізнавання голосу**
- 📥 **Завантаження** — надішліть посилання, отримайте медіафайл назад (до 45 МБ)
- 🌍 **195 країн** та **40 мов** — країна та мова є окремими налаштуваннями
- 🔄 **Самооновлення** — перевіряє нові релізи щодня і запитує перед оновленням
- 🛡️ **Прихована панель /admin** — токени, користувачі, статистика, чати, модель зображень, менеджери, увімкнення/вимкнення

## Перед встановленням

Вам потрібен сервер (або комп'ютер, що працює безперервно) на **Linux** з встановленими:

| Що | Як перевірити | Що маєте побачити |
| --- | --- | --- |
| **Python 3.11 або новіший** | `python3 --version` | `Python 3.11.x` або вищий (3.12 і 3.13 теж працюють) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` або `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` або подібне |
| **Docker** *(необов'язково)* | `docker --version` | `Docker version 2x.x.x` — потрібен лише якщо хочете SearXNG для веб-пошуку |

Якщо щось відсутнє, встановіть усе однією командою (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Для опціонального `Docker` (потрібен лише якщо ви хочете веб-пошук `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Після останнього рядка вийдіть з системи і зайдіть знову (або запускайте команди `docker` за допомогою `sudo`). Встановлювач також пропонує встановити відсутні інструменти за допомогою `apt` на `Debian/Ubuntu`. На інших системах спочатку встановіть їх за допомогою вашого менеджера пакетів. `systemd` йде з системою — його не можна встановити окремо.

Вам також потрібні дві речі від Telegram (обидві безкоштовні):

1. **Токен бота** — напишіть [@BotFather](https://t.me/BotFather) у Telegram, надішліть `/newbot` і скопіюйте токен, який він видасть.
2. **Ваш числовий ID у Telegram** — напишіть [@userinfobot](https://t.me/userinfobot) і скопіюйте число, яке він покаже. Це ваш «босовий» ID: лише цей акаунт може користуватися `/admin`.

## Встановлення

Одна команда. Скопіюйте її, вставте в термінал і натисніть Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Інсталятор задасть шість питань по черзі:

1. **Країна** — вставте англійську назву вашої країни **точно так, як у [таблиці країн](#countries) нижче** (наприклад `Turkey`). Країна задає часовий пояс, місцеву валюту для цін, час молитви та локальний контент.
2. **Мова** — мова, якою говорить бот (наприклад `en`, `fa`, `tr`). Натисніть Enter, щоб прийняти за замовчуванням для вашої країни. Мова окрема від країни: вона змінює лише те, що каже бот, і її можна змінити пізніше з `/admin`.
3. **Токен бота** — вставте токен від [@BotFather](https://t.me/BotFather). Інсталятор перевірить його у Telegram у реальному часі.
4. **Числовий ID боса** — ваш ID у Telegram від [@userinfobot](https://t.me/userinfobot).
5. **Ім'я бота / слово-тригер** — ім'я, яке люди кажуть у групах, щоб звернутися до бота. Будь-яка мова нормально (наприклад `Vortex` або `Ворткс`). Натисніть Enter для за замовчуванням `Vortex`.
6. **Перший провайдер LLM** — оберіть один: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere або **Custom** (вставте базовий URL). Потім вставте ваш API-ключ для цього провайдера — інсталятор завантажить актуальний список моделей провайдера, і ви оберете модель.

Потім інсталятор встановить залежності, створить файл `.env`, службу systemd `vortex-bot`, запропонує встановити SearXNG для веб-пошуку (потрібен Docker) і запустить бота.

> ⚠️ **Anthropic не працює безпосередньо.** Нативний API Anthropic не сумісний з OpenAI, а цей бот розуміє лише OpenAI-сумісні API. Якщо оберете Anthropic, інсталятор попередить: ключ працює лише через OpenAI-сумісний шлюз. Використовуйте OpenRouter або іншого провайдера зі списку.

## Після встановлення

Перевірте, що бот працює:

```bash
systemctl status vortex-bot
```

Маєте побачити `active (running)`. Щоб дивитися лог у реальному часі:

```bash
journalctl -u vortex-bot -f
```

Тепер відкрийте Telegram і напишіть боту:

- Надішліть `/start` — бот привітається.
- У **приватному чаті** просто пишіть йому — слово-тригер не потрібне.
- У **групі** додайте бота до групи, потім вимкніть конфіденційність групи: у [@BotFather](https://t.me/BotFather) надішліть `/setprivacy`, оберіть свого бота і виберіть **Disable** — інакше бот не побачить повідомлення групи і не почує своє слово-пробудження. Потім скажіть його ім'я, наприклад: `Vortex яка зараз година?`
- Як бос, надішліть `/admin` у приватному чаті, щоб відкрити приховану адмін-панель.

**Оновлення автоматичні.** Раз на день бот перевіряє GitHub на наявність нового релізу. Якщо є — надсилає босу приватне повідомлення з кнопками ✅ / ❌. Натисніть ✅ і він оновиться сам і перезапуститься — сервером ніколи не потрібно керувати вручну.

## Конфігурація

Усі налаштування живуть у файлі `.env` у папці встановлення. Дивіться [`.env.example`](.env.example) для всіх опцій. Найважливіші:

| Налаштування | Що робить |
| --- | --- |
| `BOT_TOKEN` | Ваш токен Telegram-бота (від @BotFather) |
| `BOSS_ID` | Ваш числовий ID у Telegram (власник бота) |
| `BOT_NAME` | Ім'я бота та слово-тригер у групах (за замовчуванням `Vortex`) |
| `BOT_COUNTRY` | Країна англійською, напр. `United States` (задає часовий пояс, валюту, час молитви) |
| `BOT_LANGUAGE` | Код мови бота, напр. `en`, `fa`, `tr` (змінює лише те, що каже бот) |
| `LLM_PROVIDERS` | Провайдери LLM та ключі: `base_url\|api_key\|model`, через кому |
| `UPDATE_CHECK_ENABLED` | `1` = перевіряти оновлення щодня, `0` = ніколи не перевіряти |
| `UPDATE_REPO` | Репозиторій, чиї релізи слідкуються (за замовчуванням `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Веб-пошук: `searxng` (за замовчуванням), `tavily` або `serper` |
| `DAILY_LIMIT_MESSAGES` | Макс. відповідей бота на користувача на день (за замовчуванням `30`, бос вільний) |

Країну та мову також можна змінити пізніше з прихованої панелі `/admin` (Мова та Країна), не редагуючи жодного файлу.

## Альтернатива через Docker

Якщо волієте Docker замість інсталятора:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Це запустить бота разом із власним SearXNG для пошуку. Перегляньте логи: `docker compose logs -f bot`.

Примітка: автоматичне самооновлення потребує systemd-служби, тому в Docker оновлення ручні: `git pull` і потім `docker compose up -d --build` знову.

## Можливості детально

### Панель /admin

Надішліть `/admin` у приватному чаті (тільки бос — ніхто інший не може її відкрити, і вона ніколи не з'являється у `/help` чи меню). Вона має:

- 🔑 **Токени та модель** — додавайте або видаляйте ключі LLM, дивіться, які ключі здорові, обирайте активну модель, переглядайте актуальний список моделей провайдера
- 👥 **Користувачі** — кількість, бан/розбан, allowlist
- 📊 **Статистика** — числа використання
- 💬 **Останні чати** — що люди писали боту (тільки бос, приватно)
- 🖼️ **Модель зображень** — DuckAI (безкоштовно, за замовчуванням), HiLinkUp, власний сервіс зображень або вимкнено
- 🛡️ **Менеджери** — дайте довіреним людям доступ до частин панелі
- 🟢/🔴 **Увімкнення** — ввімкніть або вимкніть бота для всіх (бос залишається в контролі)
- 🌍 **Мова та Країна** — змінюйте мову або країну бота будь-коли

### Пул токенів

Бот може тримати ключі від кількох провайдерів LLM одночасно. Він ротує між здоровіми ключами і автоматично перемикається, коли один перестає працювати. З `/admin` можна закріпити одну модель, обрати модель вручну або дозволити боту ротувати вільно. Працює будь-який провайдер з OpenAI-сумісним API — включаючи дрібні агрегатори, не лише великі імена.

### Зображення

Генерація зображень має три режими: **DuckAI** (безкоштовно, без ключа, за замовчуванням), **HiLinkUp** (платно, краща якість) або **власний** OpenAI-сумісний сервіс зображень. Можна також надіслати боту фото і сказати, як його редагувати («зроби це у мультяшному стилі»), і він згенерує нове зображення. Генерацію зображень можна вимкнути з `/admin`.

### Країни та мови

Vortex підтримує **195 країн** та **40 мов**. Країна задає часову зону, валюту цін, місто для часу молитви та локальний контент. Мова лише визначає, що каже бот — група в Belgium може використовувати країну Belgium та мову English, наприклад. Обидві можна змінити пізніше з `/admin`.

### Оновлення

Бот раз на день перевіряє релізи GitHub репозиторію `VortexLabsHQ/vortex-telegram-bot`. Коли виходить нова версія, він пише босу приватно з кнопками ✅ / ❌. Прийнявши — оновлює код і перезапускає бота. Поки репозиторій приватний, перевірка тихо нічого не робить (API GitHub потребує публічний репозиторій) — поставте `UPDATE_CHECK_ENABLED=0`, якщо ніколи не хочете перевірки.

## Вирішення проблем / FAQ

**Інсталятор каже, що мій токен недійсний.**
Токен від [@BotFather](https://t.me/BotFather). Переконайтеся, що скопіювали весь токен (цифри, двокрапка, потім 35+ символів), без зайвих пробілів. Якщо видалили бота або зробили новий токен, старий перестає працювати — вставте новий.

**Бот не відповідає у моїй групі.**
Чотири речі, які потрібно перевірити: (1) Конфіденційність групи має бути вимкнена — у [@BotFather](https://t.me/BotFather) надішліть `/setprivacy`, оберіть свого бота і виберіть **Disable**; якщо конфіденційність увімкнена, бот не побачить повідомлення групи взагалі, (2) бота потрібно додати до групи, (3) ви маєте сказати його слово-пробудження — його ім'я, наприклад `Vortex яка зараз година?` — бот слухає лише коли його ім'я звучить у групах, (4) у приватному чаті слово-пробудження не потрібне взагалі.

**Бот відповідає англійською, не моєю мовою.**
Надішліть `/admin` (тільки бос) → Мова та Країна, і оберіть свою мову. Інсталятор теж запитує мову — натисніть Enter там, щоб прийняти за замовчуванням вашої країни.

**Я обрав Anthropic, і бот не чатить.**
Нативний API Anthropic не сумісний з OpenAI, тому бот не може чатити з ним безпосередньо. Використовуйте OpenRouter (який може подавати моделі Claude через OpenAI-сумісний API) або оберіть іншого провайдера зі списку.

**Веб-пошук не працює.**
Веб-пошук потребує SearXNG, який інсталятор пропонує встановити з Docker. Без нього бот використовує Wikipedia як резерв, що слабше. Можна також поставити `SEARCH_PROVIDER=tavily` або `serper` з `SEARCH_API_KEY` у `.env`.

**Де логи?**
`journalctl -u vortex-bot -f` показує лог у реальному часі. `systemctl status vortex-bot` показує, чи працює служба. Якщо бот зупинився, `sudo systemctl restart vortex-bot` запустить його знову.

**Бот каже, що я досяг щоденного ліміту.**
Кожен користувач отримує 30 відповідей бота на день (бос вільний). Ліміт скидається о півночі за часовим поясом країни бота. Збільште через `DAILY_LIMIT_MESSAGES` у `.env`, або попросіть боса.

**Я знайшов баг / маю ідею.**
Будь ласка, відкрийте issue на GitHub — дивіться [CONTRIBUTING.md](CONTRIBUTING.md) як повідомити і як надіслати виправлення.

## Розробка

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

Запустіть тести (прості Python-скрипти, pytest не потрібен):

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

Усі дев'ять наборів мають пройти перед відкриттям pull request. Дивіться [CONTRIBUTING.md](CONTRIBUTING.md) для стилю коду (ruff) та процесу PR.

## Ліцензія

Vortex випущений під [MIT License](LICENSE) — вільно використовувати, копіювати, змінювати та поширювати для будь-яких цілей.

<a id="countries"></a>

## Країни

Вставте назву країни **англійською, точно як тут** коли інсталятор запитає вашу країну. Таблиця згенерована з `bot/countries.py` — якщо назва тут і там розійдуться, `bot/countries.py` виграє.

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



## Дякуємо

> ⭐ **Будь ласка, поставте зірку цьому проекту на GitHub і підпишіться на [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — це найпростіший спосіб підтримати Vortex і допомогти іншим знайти його. Дякуємо!
