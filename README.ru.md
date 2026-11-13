# Vortex 🤖 — Ваш собственный помощник для групп в Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · **Русский** · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Если вам нравится Vortex, поставьте звёзду проекту на GitHub и подпишитесь на [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — это поможет больше людям узнать о нём. Спасибо!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Что такое Vortex?

Vortex — это Telegram-бот, который живёт в ваших группах и личных чатах и отвечает людям с помощью ИИ-модели. Вы называете его по имени (по умолчанию — **Vortex**), и он отвечает — может общаться, искать в интернете, создавать картинки, проверять цены, рассказывать шутки, читать файлы, расшифровывать голосовые сообщения и многое другое.

Он работает на вашем сервере, в вашей стране и на вашем языке. Вы — главный: скрытая панель `/admin` позволяет управлять ИИ-ключами, пользователями и настройками.

## Возможности

- 💬 **ИИ-чат** в группах (по кодовому слову) и в личке (без кодового слова)
- 🔑 **Пул токенов** — используйте несколько провайдеров LLM и ключей, автоматическая ротация и переключение при сбоях
- 🖼️ **Генерация изображений** — с вашим собственным сервисом изображений (базовый URL + API-ключ + модель), добавленным в `/admin`
- 🔍 **Веб-поиск** — самодостаточный SearXNG, с запасным вариантом Wikipedia
- 💰 **Актуальные цены** — валюты, золото, нефть и крипта в вашей местной валюте
- 🕌 **Время молитв**, 🃏 **предсказания**, 😄 **шутки**, 🎲 **кубик и подбрасывание монеты**
- 📎 **Анализ файлов** и **расшифровка голосовых**
- 📥 **Скачивание** — пришлите ссылку, получите медиафайл обратно (до 45 МБ)
- 🌍 **195 стран** и **40 языков** — страна и язык — отдельные настройки
- 🔄 **Самообновление** — проверяет новые релизы каждый день и спрашивает перед обновлением
- 🛡️ **Скрытая панель /admin** — токены, пользователи, статистика, чаты, модель изображений, менеджеры, включение/выключение

## Перед установкой

Вам нужен сервер (или компьютер, который всегда включен) под **Linux** с установленными:

| Что | Как проверить | Что должно показать |
| --- | --- | --- |
| **Python 3.11 или новее** | `python3 --version` | `Python 3.11.x` или выше (3.12 и 3.13 тоже подходят) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` или `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` или похожее |
| **Docker** *(по желанию)* | `docker --version` | `Docker version 2x.x.x` — нужен только если хотите опциональный SearXNG для веб-поиска |

Если чего‑то не хватает, установите всё одной командой (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Для необязательного `docker` (нужен только если вы хотите веб‑поиск `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

После последней строки выйдите и зайдите снова (или запускайте команды `docker` с `sudo`). Установщик также предложит установить недостающие инструменты за вас с помощью `apt` в `Debian/Ubuntu`. В других системах сначала установите их через свой менеджер пакетов. `systemd` входит в состав системы — его нельзя установить отдельно.

Вам также понадобятся две вещи из Telegram (обе бесплатно):

1. **Токен бота** — напишите [@BotFather](https://t.me/BotFather) в Telegram, отправьте `/newbot` и скопируйте токен, который он выдаст.
2. **Ваш числовой Telegram ID** — напишите [@userinfobot](https://t.me/userinfobot) и скопируйте число, которое он покажет. Это ваш «босс-ID»: только этот аккаунт может пользоваться `/admin`.

## Установка

Одна команда. Скопируйте, вставьте в терминал и нажмите Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Установщик задаст шесть вопросов по порядку:

1. **Страна** — вставьте английское название вашей страны **точно так, как в [таблице стран](#countries) ниже** (например `Turkey`). Страна задаёт часовой пояс, местную валюту для цен, время молитв и локальный контент.
2. **Язык** — язык, на котором говорит бот (например `en`, `fa`, `tr`). Нажмите Enter, чтобы принять язык по умолчанию для вашей страны. Язык отделен от страны: он меняет только речь бота, и его можно сменить позже через `/admin`.
3. **Токен бота** — вставьте токен от [@BotFather](https://t.me/BotFather). Установщик проверит его вживую с Telegram.
4. **Числовой ID босса** — ваш Telegram ID от [@userinfobot](https://t.me/userinfobot).
5. **Имя бота / кодовое слово** — имя, которое люди говорят в группах, чтобы обратиться к боту. На любом языке (например `Vortex` или `Вортекс`). Enter для дефолта `Vortex`.
6. **Первый LLM-провайдер** — выберите один: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere или **Custom** (вставьте базовый URL). Потом вставьте API-ключ для этого провайдера — установщик заберёт актуальный список моделей провайдера, и вы выберете модель.

Потом установщик поставит зависимости, запишет `.env`, создаст systemd-сервис `vortex-bot`, предложит поставить SearXNG для веб-поиска (нужен Docker) и запустит бота.

> ⚠️ **Anthropic напрямую не работает.** Нативный API Anthropic не совместим с OpenAI, а этот бот говорит только на OpenAI-совместимых API. Если выберете Anthropic, установщик предупредит: ключ заработает только через OpenAI-совместимый шлюз. Используйте OpenRouter или другой провайдер из списка.

## После установки

Проверьте, что бот запущен:

```bash
systemctl status vortex-bot
```

Должно быть `active (running)`. Чтобы смотреть лог вживую:

```bash
journalctl -u vortex-bot -f
```

Теперь откройте Telegram и поговорите с ботом:

- Отправьте `/start` — бот поздоровается.
- В **личке** просто пишите ему — кодовое слово не нужно.
- В **группе** добавьте бота в группу, затем отключите **Конфиденциальность группы**: в [@BotFather](https://t.me/BotFather) отправьте `/setprivacy`, выберите своего бота и нажмите **Disable** — иначе бот не увидит сообщения группы и не услышит своё кодовое слово. Затем скажите его имя, например: `Vortex который час?`
- Как босс, отправьте `/admin` в личке, чтобы открыть скрытую админ-панель.

**Обновления автоматические.** Раз в день бот проверяет GitHub на новый релиз. Если есть — пришлёт вам в личку с кнопками ✅ / ❌. Нажмите ✅ — он сам обновится и перезапустится — сервер трогать не придётся.

## Настройка

Все настройки живут в файле `.env` в папке установки. См. [`.env.example`](.env.example) для всех опций. Самые важные:

| Настройка | Что делает |
| --- | --- |
| `BOT_TOKEN` | Ваш Telegram-токен бота (от @BotFather) |
| `BOSS_ID` | Ваш числовой Telegram ID (владелец бота) |
| `BOT_NAME` | Имя бота и кодовое слово в группах (по умолчанию `Vortex`) |
| `BOT_COUNTRY` | Страна на английском, например `United States` (задаёт часовой пояс, валюту, время молитв) |
| `BOT_LANGUAGE` | Код языка бота, например `en`, `fa`, `tr` (меняет только речь бота) |
| `LLM_PROVIDERS` | Провайдеры LLM и ключи: `base_url\|api_key\|model`, через запятую |
| `UPDATE_CHECK_ENABLED` | `1` = проверять обновления каждый день, `0` = никогда не проверять |
| `UPDATE_REPO` | Репозиторий, за релизами которого следим (по умолчанию `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Веб-поиск: `searxng` (по умолчанию), `tavily` или `serper` |
| `DAILY_LIMIT_MESSAGES` | Макс. ответов бота на пользователя в день (по умолчанию `30`, босс не ограничен) |

Страну и язык можно сменить позже из скрытой панели `/admin` (Language & Country), не редактируя файлы.

## Вариант с Docker

Если предпочитаете Docker вместо установщика:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Это запустит бота вместе с самодостаточным SearXNG для поиска. Логи: `docker compose logs -f bot`.

Примечание: автоматическое самообновление нужно systemd-сервису, поэтому в Docker обновления вручную: `git pull` и снова `docker compose up -d --build`.

## Возможности подробнее

### Панель /admin

Отправьте `/admin` в личке (только босс — никто другой не может открыть, и она никогда не появляется в `/help` или меню). Внутри:

- 🔑 **Токены и модель** — добавляйте/удаляйте LLM-ключи, смотрите, какие ключи здоровы, выбирайте активную модель, листайте живой список моделей провайдера
- 👥 **Пользователи** — счётчики, бан/разбан, белый список
- 📊 **Статистика** — цифры использования
- 💬 **Недавние чаты** — что люди писали боту (только босс, приватно)
- 🖼️ **Модель изображений** — ваш собственный сервис изображений (базовый URL + API-ключ + модель) или выкл.
- 🛡️ **Менеджеры** — дайте доверенным людям доступ к частям панели
- 🟢/🔴 **Включение/выключение** — выключите бота для всех (босс всё равно управляет)
- 🌍 **Язык и страна** — меняйте язык или страну бота в любой момент

### Пул токенов

Бот может держать ключи от нескольких LLM-провайдеров одновременно. Он ротирует между рабочими ключами и автоматически переключается, когда один падает. Из `/admin` можно закрепить одну модель, выбрать вручную или оставить боту ротировать свободно. Работает любой провайдер с OpenAI-совместимым API — включая мелкие агрегаторы, не только большие имена.

### Изображения

Генерация изображений использует ваш собственный OpenAI-совместимый сервис изображений: добавьте его базовый URL, API-ключ и модель в `/admin` (🖼️ Модель изображений). Встроенного провайдера изображений нет, и редактирование фото не поддерживается. Генерацию изображений можно отключить из `/admin`.

### Страны и языки

Vortex поддерживает **195 стран** и **40 языков**. Страна задаёт часовой пояс, валюту цен, город для времени намаза и локальный контент. Язык определяет только речь бота — группа в Belgium может использовать страну Belgium и язык English, например. Оба параметра можно изменить позже через `/admin`.

### Обновления

Бот проверяет релизы GitHub `VortexLabsHQ/vortex-telegram-bot` раз в день. Когда выходит новая версия — пишет боссу в личку с кнопками ✅ / ❌. Принятие обновляет код и перезапускает бота. Пока репозиторий приватный, проверка молча ничего не делает (API GitHub требует публичный репо) — поставьте `UPDATE_CHECK_ENABLED=0`, если проверка вообще не нужна.

## Решение проблем / FAQ

**Установщик говорит, что токен недействителен.**
Токен от [@BotFather](https://t.me/BotFather). Убедитесь, что скопировали целиком (цифры, двоеточие, потом 35+ символов), без лишних пробелов. Если бота удалили или сделали новый токен — старый перестаёт работать, вставьте новый.

**Бот не отвечает в моей группе.**
Четыре пункта для проверки: (1) Конфиденциальность группы должна быть отключена — в [@BotFather](https://t.me/BotFather) отправьте `/setprivacy`, выберите своего бота и нажмите **Disable**; с включённой конфиденциальностью бот вообще не видит сообщения группы, (2) бот должен быть добавлен в группу, (3) нужно сказать его кодовое слово — его имя, например `Vortex который час?` — бот слушает только когда его имя произносят в группах, (4) в личном чате кодовое слово не нужно вовсе.

**Бот отвечает на английском, а не на моём языке.**
Отправьте `/admin` (только босс) → Language & Country, выберите свой язык. Установщик тоже спрашивает язык — нажмите Enter там, чтобы принять дефолт вашей страны.

**Я выбрал Anthropic, и бот не общается.**
Нативный API Anthropic не OpenAI-совместимый, бот не может с ним говорить напрямую. Используйте OpenRouter (он умеет отдавать модели Claude через OpenAI-совместимый API) или выберите другой провайдер из списка.

**Веб-поиск не работает.**
Веб-поиск нужен SearXNG, который установщик предлагает поднять через Docker. Без него бот падает на Wikipedia, она слабее. Можно также поставить `SEARCH_PROVIDER=tavily` или `serper` с `SEARCH_API_KEY` в `.env`.

**Где логи?**
`journalctl -u vortex-bot -f` показывает лог вживую. `systemctl status vortex-bot` показывает, запущен ли сервис. Если бот упал, `sudo systemctl restart vortex-bot` поднимет его снова.

**Бот говорит, что я достиг дневного лимита.**
Каждому пользователю — 30 ответов бота в день (босс не ограничен). Лимит сбрасывается в полночь по часовому поясу страны бота. Поднимите через `DAILY_LIMIT_MESSAGES` в `.env`, или попросите босса.

**Нашёл баг / есть идея.**
Откройте issue на GitHub — см. [CONTRIBUTING.md](CONTRIBUTING.md) как сообщить и как прислать фикс.

## Разработка

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

Запуск тестов (простые Python-скрипты, pytest не нужен):

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

Все девять наборов должны пройти перед открытием pull request. См. [CONTRIBUTING.md](CONTRIBUTING.md) за стилем кода (ruff) и процессом PR.

## Лицензия

Vortex выпущен под [MIT License](LICENSE) — свободно использовать, копировать, менять и делиться, для любых целей.

<a id="countries"></a>

## Страны

Вставьте название страны **на английском, точно так, как написано здесь**, когда установщик спросит страну. Таблица сгенерирована из `bot/countries.py` — если имя здесь и там расходятся, побеждает `bot/countries.py`.

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



## Спасибо

> ⭐ **Пожалуйста, поставьте звёзду проекту на GitHub и подпишитесь на [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — это простейший способ поддержать Vortex и помочь другим его найти. Спасибо!
