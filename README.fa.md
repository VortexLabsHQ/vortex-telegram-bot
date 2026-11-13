# Vortex 🤖 — دستیار گروه تلگرام شما

[English](README.md) · **فارسی** · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **اگر از Vortex لذت بردید، لطفاً این پروژه را در GitHub ستاره دهید و [@VortexLabsHQ](https://github.com/VortexLabsHQ) را دنبال کنید** — این کار به دیگران کمک می‌کند تا آن را پیدا کنند. ممنون!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex چیست؟

Vortex یک ربات تلگرام است که در گروه‌ها و چت‌های خصوصی شما زندگی می‌کند و با یک مدل چت هوش مصنوعی به افراد پاسخ می‌دهد. شما نام آن را می‌گویید (نام پیش‌فرض **Vortex** است) و آن پاسخ می‌دهد — می‌تواند چت کند، وب را جستجو کند، تصویر بسازد، قیمت‌ها را بررسی کند، جوک بگوید، فایل‌ها را بخواند، پیام‌های صوتی را رونویسی کند، و کارهای دیگر.

این روی سرور شما، در کشور و زبان شما اجرا می‌شود. شما رئیس هستید: یک پنل `/admin` مخفی به شما اجازه می‌دهد کلیدهای هوش مصنوعی، کاربران و تنظیمات را مدیریت کنید.

## ویژگی‌ها

- 💬 **چت هوش مصنوعی** در گروه‌ها (کلمه بیداری) و چت‌های خصوصی (نیاز به کلمه بیداری نیست)
- 🔑 **مجموعه توکن** — از چندین ارائه‌دهنده LLM و کلید استفاده کنید، به صورت خودکار چرخش و پشتیبانی از خرابی داشته باشید
- 🖼️ **تولید تصویر** — با سرویس تصویر خودتان (آدرس پایه + کلید API + مدل)، اضافه شده در `/admin`
- 🔍 **جستجوی وب** — SearXNG میزبان‌شده، با ویکی‌پدیا به عنوان پشتیبان
- 💰 **قیمت‌های لحظه‌ای** — ارزها، طلا، نفت و کریپتو در ارز محلی شما
- 🕌 **اوقات شرعی**، 🃏 **فال**، 😄 **جوک**، 🎲 **تاس و سکه**
- 📎 **تحلیل فایل** و **رونویسی صوت**
- 📥 **دانلودها** — یک لینک بفرستید، فایل رسانه را دریافت کنید (تا ۴۵ مگابایت)
- 🌍 **۱۹۵ کشور** و **۴۰ زبان** — کشور و زبان تنظیمات جداگانه هستند
- 🔄 **خودبه‌روزرسانی** — روزانه نسخه‌های جدید را بررسی می‌کند و قبل از به‌روزرسانی از شما می‌پرسد
- 🛡️ **پنل /admin مخفی** — توکن‌ها، کاربران، آمار، چت‌ها، مدل تصویر، مدیران، قدرت

## قبل از نصب

شما به یک سرور (یا کامپیوتری که روشن بماند) با **لینوکس** نیاز دارید که موارد زیر روی آن نصب شده باشند:

| مورد | نحوه بررسی | آنچه باید ببینید |
| --- | --- | --- |
| **Python 3.11 یا جدیدتر** | `python3 --version` | `Python 3.11.x` یا بالاتر (۳.۱۲ و ۳.۱۳ هم کار می‌کنند) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` یا `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` یا مشابه |
| **Docker** *(اختیاری)* | `docker --version` | `Docker version 2x.x.x` — فقط اگر جستجوی وب SearXNG را می‌خواهید لازم است |

اگر چیزی کم است، همه را با یک دستور نصب کنید (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

برای `Docker` اختیاری (فقط در صورتی لازم است که جستجوی وب `SearXNG` را بخواهید):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

پس از خط آخر، خارج شوید و مجدداً وارد شوید (یا دستورات `docker` را با `sudo` اجرا کنید). نصب‌کننده همچنین پیشنهاد می‌دهد ابزارهای گمشده را با `apt` روی `Debian/Ubuntu` برای شما نصب کند. در سیستم‌های دیگر، ابتدا آن‌ها را با مدیریت بسته خود نصب کنید. `systemd` با سیستم ارائه می‌شود — نمی‌توان آن را به صورت جداگانه نصب کرد.

شما همچنین به دو چیز از تلگرام نیاز دارید (هر دو رایگان هستند):

1. **توکن ربات** — با [@BotFather](https://t.me/BotFather) در تلگرام صحبت کنید، `/newbot` بفرستید، و توکنی که می‌دهد را کپی کنید.
2. **شناسه عددی کاربر تلگرام شما** — با [@userinfobot](https://t.me/userinfobot) صحبت کنید و عددی که نشان می‌دهد را کپی کنید. این «شناسه رئیس» شماست: فقط این اکانت می‌تواند از `/admin` استفاده کند.

## نصب

یک دستور. آن را کپی کنید، در ترمینال خود بچسبانید، و Enter بزنید:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

نصب‌کننده از شما شش سوال می‌پرسد، به ترتیب:

1. **کشور** — نام انگلیسی کشور خود را **دقیقاً همان‌طور که در [جدول کشورها](#countries) زیر آمده** بچسبانید (مثلاً `Turkey`). کشور منطقه زمانی، ارز محلی برای قیمت‌ها، اوقات شرعی و محتوای محلی را تعیین می‌کند.
2. **زبان** — زبانی که ربات با آن صحبت می‌کند (مثلاً `en`، `fa`، `tr`). برای قبول پیش‌فرض کشور خود Enter بزنید. زبان از کشور جدا است: فقط آنچه ربات می‌گوید را تغییر می‌دهد، و بعداً می‌توانید آن را از `/admin` تغییر دهید.
3. **توکن ربات** — توکن را از [@BotFather](https://t.me/BotFather) بچسبانید. نصب‌کننده آن را به صورت زنده با تلگرام بررسی می‌کند.
4. **شناسه عددی رئیس** — شناسه کاربر تلگرام شما از [@userinfobot](https://t.me/userinfobot).
5. **نام ربات / کلمه بیداری** — نامی که افراد در گروه‌ها برای صحبت با ربات می‌گویند. هر زبانی خوب است (مثلاً `Vortex` یا `ورتکس`). برای پیش‌فرض `Vortex` کلید Enter را بزنید.
6. **اولین ارائه‌دهنده LLM** — یکی را انتخاب کنید: OpenAI، Anthropic، OpenRouter، Google AI (Gemini)، DeepSeek، Groq، Together AI، Mistral AI، xAI (Grok)، Cohere، یا **Custom** (یک base URL بچسبانید). سپس کلید API خود را برای آن ارائه‌دهنده بچسبانید — نصب‌کننده لیست مدل‌های زنده ارائه‌دهنده را دریافت می‌کند و شما یک مدل را انتخاب می‌کنید.

سپس نصب‌کننده وابستگی‌ها را نصب می‌کند، فایل `.env` را می‌نویسد، سرویس systemd `vortex-bot` را می‌سازد، پیشنهاد می‌دهد SearXNG را برای جستجوی وب نصب کند (نیاز به Docker دارد)، و ربات را راه‌اندازی می‌کند.

> ⚠️ **Anthropic به صورت مستقیم کار نمی‌کند.** API بومی Anthropic سازگار با OpenAI نیست، و این ربات فقط API‌های سازگار با OpenAI را می‌فهمد. اگر Anthropic را انتخاب کنید، نصب‌کننده شما را هشدار می‌دهد: کلید فقط از طریق یک دروازه سازگار با OpenAI کار می‌کند. از OpenRouter، یا ارائه‌دهنده دیگری از لیست استفاده کنید.

## بعد از نصب

بررسی کنید که ربات در حال اجرا است:

```bash
systemctl status vortex-bot
```

باید `active (running)` را ببینید. برای تماشای لاگ زنده:

```bash
journalctl -u vortex-bot -f
```

اکنون تلگرام را باز کنید و با ربات خود صحبت کنید:

- `/start` بفرستید — ربات سلام می‌کند.
- در **چت خصوصی**، فقط به آن بنویسید — نیازی به کلمه بیداری نیست.
- در **گروه**، ربات را به گروه اضافه کنید، سپس حریم خصوصی گروه را غیرفعال کنید: در [@BotFather](https://t.me/BotFather) دستور `/setprivacy` را بفرستید، ربات خود را انتخاب کنید و **Disable** را انتخاب کنید — در غیر این صورت ربات نمی‌تواند پیام‌های گروه را ببیند و کلمه بیداری خود را نخواهد شنید. سپس نام آن را بگویید، برای مثال: `Vortex ساعت چنده؟`
- به عنوان رئیس، در چت خصوصی `/admin` بفرستید تا پنل ادمین مخفی باز شود.

**به‌روزرسانی‌ها خودکار هستند.** روزانه یک بار ربات GitHub را برای انتشار جدید بررسی می‌کند. اگر موجود باشد، به شما به صورت خصوصی با دکمه‌های ✅ / ❌ پیام می‌دهد. ✅ را بزنید و کد را به‌روزرسانی کرده و ربات را مجدداً راه‌اندازی می‌کند — هرگز لازم نیست سرور را دست بزنید.

## تنظیمات

همه تنظیمات در فایل `.env` در پوشه نصب زندگی می‌کنند. برای هر گزینه به [`.env.example`](.env.example) نگاه کنید. مهم‌ترین‌ها:

| تنظیم | چه کاری انجام می‌دهد |
| --- | --- |
| `BOT_TOKEN` | توکن ربات تلگرام شما (از @BotFather) |
| `BOSS_ID` | شناسه عددی کاربر تلگرام شما (مالک ربات) |
| `BOT_NAME` | نام ربات و کلمه بیداری در گروه‌ها (پیش‌فرض `Vortex`) |
| `BOT_COUNTRY` | کشور به انگلیسی، مثل `United States` (منطقه زمانی، ارز، اوقات شرعی را تعیین می‌کند) |
| `BOT_LANGUAGE` | کد زبان ربات، مثل `en`، `fa`، `tr` (فقط آنچه ربات می‌گوید را تغییر می‌دهد) |
| `LLM_PROVIDERS` | ارائه‌دهندگان و کلیدهای LLM: `base_url\|api_key\|model`، جدا شده با کاما |
| `UPDATE_CHECK_ENABLED` | `1` = روزانه به‌روزرسانی چک کن، `0` = هرگز چک نکن |
| `UPDATE_REPO` | مخزنی که انتشارهای آن دیده می‌شود (پیش‌فرض `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | جستجوی وب: `searxng` (پیش‌فرض)، `tavily`، یا `serper` |
| `DAILY_LIMIT_MESSAGES` | حداکثر پاسخ ربات به هر کاربر در روز (پیش‌فرض `30`، رئیس معاف است) |

کشور و زبان همچنین بعداً از پنل `/admin` مخفی (Language & Country) قابل تغییر هستند، بدون ویرایش فایل.

## جایگزین Docker

اگر به جای نصب‌کننده، Docker را ترجیح می‌دهید:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

این ربات را به همراه موتور جستجوی SearXNG میزبان‌شده راه‌اندازی می‌کند. لاگ‌ها را با `docker compose logs -f bot` ببینید.

نکته: به‌روزرسانی‌کننده خودکار به سرویس systemd نیاز دارد، بنابراین در Docker به‌روزرسانی‌ها دستی هستند: `git pull` و سپس دوباره `docker compose up -d --build`.

## ویژگی‌ها به تفصیل

### پنل /admin

در چت خصوصی `/admin` بفرستید (فقط رئیس — هیچ‌کس دیگر نمی‌تواند آن را باز کند، و هرگز در `/help` یا منوها ظاهر نمی‌شود). این موارد را دارد:

- 🔑 **توکن‌ها و مدل** — کلید LLM اضافه یا حذف کنید، ببینید کدام کلیدها سالم هستند، مدل فعال را انتخاب کنید، لیست مدل‌های زنده یک ارائه‌دهنده را مرور کنید
- 👥 **کاربران** — تعداد کاربران، بن/آنبن، لیست مجاز
- 📊 **آمار** — اعداد استفاده
- 💬 **چت‌های اخیر** — افراد چه گفتند به ربات (فقط رئیس، خصوصی)
- 🖼️ **مدل تصویر** — سرویس تصویر خودتان (آدرس پایه + کلید API + مدل)، یا خاموش
- 🛡️ **مدیران** — به افراد قابل اعتماد دسترسی به بخش‌های پنل بدهید
- 🟢/🔴 **قدرت** — ربات را برای همه روشن یا خاموش کنید (رئیس کنترل دارد)
- 🌍 **زبان و کشور** — زبان یا کشور ربات را هر وقت خواستید تغییر دهید

### مجموعه توکن

ربات می‌تواند کلیدها از چندین ارائه‌دهنده LLM را همزمان داشته باشد. بین کلیدهای سالم چرخش می‌کند و وقتی یکی کار نکرد به صورت خودکار به سراغ دیگری می‌رود. از `/admin` می‌توانید یک مدل را قفل کنید، به صورت دستی مدل انتخاب کنید، یا ربات را به صورت آزاد چرخش دهید. هر ارائه‌دهنده‌ای با API سازگار OpenAI کار می‌کند — شامل تجمیع‌کنندگان کوچک، نه فقط نام‌های بزرگ.

### تصاویر

تولید تصویر از سرویس تصویر سازگار OpenAI خودتان استفاده می‌کند: آدرس پایه، کلید API و مدل را در `/admin` (🖼️ Image model) اضافه کنید. هیچ ارائه‌دهنده تصویر داخلی وجود ندارد و ویرایش عکس پشتیبانی نمی‌شود. تولید تصویر می‌تواند از `/admin` خاموش شود.

### کشورها و زبان‌ها

Vortex از **۱۹۵ کشور** و **۴۰ زبان** پشتیبانی می‌کند. کشور منطقه زمانی، ارزی که قیمت‌ها در آن نشان داده می‌شوند، شهر مورد استفاده برای اوقات شرعی، و محتوای محلی را تعیین می‌کند. زبان فقط آنچه ربات می‌گوید را تعیین می‌کند — مثلاً یک گروه در بلژیک می‌تواند از کشور بلژیک و زبان انگلیسی استفاده کند. هر دو بعداً از `/admin` قابل تغییر هستند.

### به‌روزرسانی‌ها

ربات روزانه یک بار انتشارهای GitHub مخزن `VortexLabsHQ/vortex-telegram-bot` را بررسی می‌کند. وقتی نسخه جدیدی منتشر شود، به رئیس به صورت خصوصی با دکمه‌های ✅ / ❌ پیام می‌دهد. قبول کردن کد را به‌روزرسانی کرده و ربات را مجدداً راه‌اندازی می‌کند. تا زمانی که مخزن خصوصی است، چک به سکوت هیچ کاری انجام نمی‌دهد (API گیت‌هاب مخزن عمومی می‌خواهد) — اگر هرگز نمی‌خواهید چک شود `UPDATE_CHECK_ENABLED=0` بگذارید.

## عیب‌یابی / سوالات متداول

**نصب‌کننده می‌گوید توکن من نامعتبر است.**
توکن از [@BotFather](https://t.me/BotFather) می‌آید. مطمئن شوید کل توکن را کپی کرده‌اید (ارقام، یک دو نقطه، سپس ۳۵+ کاراکتر)، بدون فضای اضافه. اگر ربات را حذف کرده‌اید یا توکن جدید ساخته‌اید، توکن قبلی کار نمی‌کند — توکن جدید را بچسبانید.

**ربات در گروهم پاسخ نمی‌دهد.**
چهار مورد برای بررسی: (۱) حریم خصوصی گروه باید غیرفعال باشد — در [@BotFather](https://t.me/BotFather) دستور `/setprivacy` را بفرستید، ربات خود را انتخاب کنید و **Disable** را انتخاب کنید؛ با حریم خصوصی فعال، ربات اصلا نمی‌تواند پیام‌های گروه را ببیند، (۲) ربات باید به گروه اضافه شده باشد، (۳) باید کلمه بیداری آن را بگویید — نام آن، برای مثال `Vortex ساعت چنده؟` — ربات تنها زمانی گوش می‌دهد که نامش در گروه‌ها گفته شود، (۴) در چت خصوصی هیچ کلمه بیداری لازم نیست.

**ربات به انگلیسی پاسخ می‌دهد، نه زبان من.**
`/admin` بفرستید (فقط رئیس) → Language & Country، و زبان خود را انتخاب کنید. نصب‌کننده هم از زبان می‌پرسد — آنجا Enter بزنید تا پیش‌فرض کشور شما قبول شود.

**من Anthropic را انتخاب کردم و ربات چت نمی‌کند.**
API بومی Anthropic سازگار با OpenAI نیست، بنابراین ربات نمی‌تواند مستقیماً با آن چت کند. از OpenRouter استفاده کنید (که می‌تواند مدل‌های Claude را از طریق API سازگار OpenAI سرویس دهد)، یا ارائه‌دهنده دیگری از لیست را انتخاب کنید.

**جستجوی وب کار نمی‌کند.**
جستجوی وب به SearXNG نیاز دارد، که نصب‌کننده پیشنهاد می‌دهد با Docker راه‌اندازی شود. بدون آن، ربات به ویکی‌پدیا terug می‌افتد، که ضعیف‌تر است. همچنین می‌توانید در `.env` `SEARCH_PROVIDER=tavily` یا `serper` با `SEARCH_API_KEY` بگذارید.

**لاگ‌ها کجاست؟**
`journalctl -u vortex-bot -f` لاگ زنده را نشان می‌دهد. `systemctl status vortex-bot` نشان می‌دهد که سرویس در حال اجراست یا خیر. اگر ربات متوقف شود، `sudo systemctl restart vortex-bot` آن را دوباره راه‌اندازی می‌کند.

**ربات می‌گوید به حد روزانه رسیده‌ام.**
هر کاربر روزانه ۳۰ پاسخ ربات می‌گیرد (رئیس معاف است). محدودیت در نیمه‌شب در منطقه زمانی کشور ربات ریست می‌شود. با `DAILY_LIMIT_MESSAGES` در `.env` افزایش دهید، یا از رئیس بپرسید.

**یک باگ پیدا کردم / یک ایده دارم.**
لطفاً در GitHub یک issue باز کنید — برای نحوه گزارش و ارسال رفع به [CONTRIBUTING.md](CONTRIBUTING.md) نگاه کنید.

## توسعه

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

تست‌ها را اجرا کنید (اسکریپت‌های ساده پایتون، pytest لازم نیست):

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

همه نه مجموعه باید پاس شوند قبل از باز کردن pull request. برای سبک کد (ruff) و فرآیند PR به [CONTRIBUTING.md](CONTRIBUTING.md) نگاه کنید.

## لایسنس

Vortex تحت [MIT License](LICENSE) منتشر شده — آزاد برای استفاده، کپی، تغییر و اشتراک‌گذاری، برای هر هدفی.

<a id="countries"></a>

## کشورها

نام کشور را **به انگلیسی، دقیقاً همان‌طور که اینجا نوشته شده** بچسبانید وقتی نصب‌کننده از شما کشور می‌پرسد. جدول از `bot/countries.py` تولید شده — اگر نامی اینجا و نامی آنجا با هم مخالف باشند، `bot/countries.py` برنده است.

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



## ممنون

> ⭐ **لطفاً این پروژه را در GitHub ستاره دهید و [@VortexLabsHQ](https://github.com/VortexLabsHQ) را دنبال کنید** — ساده‌ترین راه برای حمایت از Vortex و کمک به دیگران برای یافتن آن است. ممنون!
