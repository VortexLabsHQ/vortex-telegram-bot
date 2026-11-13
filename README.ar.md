# Vortex 🤖 — مساعد مجموعتك الخاص على تيليجرام

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · **العربية** · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **إذا أعجبك Vortex، يرجى وضع نجمة لهذا المشروع على GitHub ومتابعة [@VortexLabsHQ](https://github.com/VortexLabsHQ) — فهذا يساعد المزيد من الناس في العثور عليه. شكراً لك!**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ما هو Vortex؟

Vortex هو بوت تيليجرام يعيش في مجموعاتك ومحادثاتك الخاصة ويجيب الأشخاص باستخدام نموذج محادثة بالذكاء الاصطناعي. تنادي باسمه (الاسم الافتراضي هو **Vortex**) فيرد عليك — يمكنه الدردشة، البحث في الويب، إنشاء الصور، التحقق من الأسعار، سرد النكات، قراءة الملفات، تحويل الرسائل الصوتية إلى نص، والمزيد.

يعمل على خادمك الخاص، في بلدك بلغتك. أنت المسؤول: لوحة `/admin` مخفية تتيح لك إدارة مفاتيح الذكاء الاصطناعي والمستخدمين والإعدادات.

## الميزات

- 💬 **دردشة بالذكاء الاصطناعي** في المجموعات (كلمة تنبيه) والمحادثات الخاصة (لا تحتاج لكلمة تنبيه)
- 🔑 **مجموعة الرموز** — استخدم عدة مزودين ومفاتيح للذكاء الاصطناعي، مع التبديل التلقائي والتحويل عند الفشل
- 🖼️ **توليد وتحرير الصور** — مجاني (DuckAI) أو مزودين مدفوعين
- 🔍 **البحث على الويب** — SearXNG مستضاف ذاتياً، مع ويكيبيديا كبديل
- 💰 **أسعار مباشرة** — العملات، الذهب، النفط، والعملات المشفرة بعملتك المحلية
- 🕌 **أوقات الصلاة**، 🃏 **الحظ**، 😄 **النكات**، 🎲 **النرد ورمي العملة**
- 📎 **تحليل الملفات** و **نسخ الصوت**
- 📥 **التنزيلات** — أرسل رابطاً، واحصل على ملف الوسائط (حتى 45 ميجابايت)
- 🌍 **195 دولة** و **40 لغة** — الدولة واللغة إعدادان منفصلان
- 🔄 **تحديث ذاتي** — يتحقق من الإصدارات الجديدة يومياً ويسألك قبل التحديث
- 🛡️ **لوحة /admin مخفية** — الرموز، المستخدمون، الإحصائيات، المحادثات، نموذج الصورة، المديرون، الطاقة

## قبل التثبيت

تحتاج إلى خادم (أو كمبيوتر يبقى قيد التشغيل) يعمل بنظام **Linux** مع تثبيت ما يلي:

| ما هو | كيف تتحقق | ما يجب أن تراه |
| --- | --- | --- |
| **Python 3.11 أو أحدث** | `python3 --version` | `Python 3.11.x` أو أعلى (يعمل 3.12 و 3.13 أيضاً) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` أو `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` أو ما شابه |
| **Docker** *(اختياري)* | `docker --version` | `Docker version 2x.x.x` — مطلوب فقط إذا كنت تريد بحث الويب الاختياري SearXNG |

إذا كان هناك شيء مفقود، قم بتثبيته كله بأمر واحد (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

لخيار `docker` الاختياري (مطلوب فقط إذا كنت تريد بحث الويب `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

بعد السطر الأخير، قم بتسجيل الخروج والدخول مرة أخرى (أو شغّل أوامر `docker` باستخدام `sudo`). يقدّم المثبّت أيضًا تثبيت الأدوات المفقودة لك باستخدام `apt` على `Debian/Ubuntu`. في الأنظمة الأخرى، ثبّتها باستخدام مدير الحزم الخاص بك أولاً. `systemd` يأتي مع النظام — ولا يمكن تثبيته بشكل منفصل.

تحتاج أيضاً إلى شيئين من Telegram (كلاهما مجاني):

1. **رمز البوت** — تواصل مع [@BotFather](https://t.me/BotFather) على Telegram، وأرسل `/newbot`، وانسخ الرمز الذي يعطيك إياه.
2. **معرف مستخدم Telegram الرقمي الخاص بك** — تواصل مع [@userinfobot](https://t.me/userinfobot) وانسخ الرقم الذي يظهره لك. هذا هو معرف "المدير" الخاص بك: فقط هذا الحساب يمكنه استخدام `/admin`.

## التثبيت

أمر واحد. انسخه، والصقه في الطرفية، واضغط Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

يسألك المثبّت ستة أسئلة، بالترتيب:

1. **البلد** — الصق الاسم الإنجليزي لبلدك **بالضبط كما هو مدرج في [جدول البلدان](#countries) أدناه** (مثلاً `Turkey`). يحدد البلد المنطقة الزمنية، والعملة المحلية للأسعار، وأوقات الصلاة، والمحتوى المحلي.
2. **اللغة** — اللغة التي يتحدث بها البوت (مثلاً `en`، `fa`، `tr`). اضغط Enter لقبول اللغة الافتراضية لبلدك. اللغة منفصلة عن البلد: فهي تغيّر فقط ما يقوله البوت، ويمكنك تغييرها لاحقاً من `/admin`.
3. **رمز البوت** — الصق الرمز من [@BotFather](https://t.me/BotFather). يتحقق المثبّت منه مباشرة مع تيليجرام.
4. **المعرف الرقمي للمدير** — معرف مستخدم تيليجرام الخاص بك من [@userinfobot](https://t.me/userinfobot).
5. **اسم البوت / كلمة التنبيه** — الاسم الذي يقوله الناس في المجموعات للتحدث مع البوت. أي لغة مقبولة (مثلاً `Vortex` أو `ورتکس`). اضغط Enter للافتراضي `Vortex`.
6. **أول مزود LLM** — اختر واحداً: OpenAI، Anthropic، OpenRouter، Google AI (Gemini)، DeepSeek، Groq، Together AI، Mistral AI، xAI (Grok)، Cohere، أو **مخصص** (الصق رابط أساسي). ثم الصق مفتاح API الخاص بذلك المزود — يجلب المثبّت قائمة النماذج الحية للمزود وتختار نموذجاً.

ثم يثبّت المثبّت التبعيات، وينشئ ملف `.env`، وينشئ خدمة systemd باسم `vortex-bot`، ويعرض تثبيت SearXNG للبحث على الويب (يحتاج Docker)، ويبدأ البوت.

> ⚠️ **لا يعمل Anthropic مباشرة.** واجهة برمجة تطبيقات Anthropic الأصلية غير متوافقة مع OpenAI، وهذا البوت يتحدث فقط واجهات برمجة تطبيقات متوافقة مع OpenAI. إذا اخترت Anthropic، يحذرك المثبّت: المفتاح يعمل فقط عبر بوابة متوافقة مع OpenAI. استخدم OpenRouter، أو مزوداً آخر من القائمة بدلاً من ذلك.

## بعد التثبيت

تحقق من أن البوت يعمل:

```bash
systemctl status vortex-bot
```

يجب أن ترى `active (running)`. لمشاهدة السجل المباشر:

```bash
journalctl -u vortex-bot -f
```

الآن افتح تيليجرام وتحدث مع البوت:

- أرسل `/start` — سيقول البوت مرحباً.
- في **محادثة خاصة**، اكتب له مباشرة — لا حاجة لكلمة تنبيه.
- في **مجموعة**، أضف البوت إلى المجموعة، ثم أوقف خصوصية المجموعة: في [@BotFather](https://t.me/BotFather) أرسل `/setprivacy`، اختر بوتك، واختر **Disable** — وإلا لن يتمكن البوت من رؤية رسائل المجموعة ولن يسمع كلمة التنبيه. ثم قل اسمه، على سبيل المثال: `Vortex what's the time?`
- بصفتك المشرف، أرسل `/admin` في محادثة خاصة لفتح لوحة الإدارة المخفية.

**التحديثات تلقائية.** مرة في اليوم يتحقق البوت من GitHub بحثاً عن إصدار جديد. إذا وجد واحداً، يرسل لك رسالة خاصة بأزرار ✅ / ❌. اضغط ✅ فيقوم البوت بتحديث نفسه وإعادة التشغيل — لن تحتاج أبداً للمس الخادم.

## التكوين

جميع الإعدادات موجودة في ملف `.env` في مجلد التثبيت. راجع [`.env.example`](.env.example) لكل الخيارات. أهمها:

| الإعداد | ماذا يفعل |
| --- | --- |
| `BOT_TOKEN` | رمز بوت التليجرام الخاص بك (من @BotFather) |
| `BOSS_ID` | معرف مستخدم التليجرام الرقمي الخاص بك (مالك البوت) |
| `BOT_NAME` | اسم البوت وكلمة التنبيه في المجموعات (افتراضي `Vortex`) |
| `BOT_COUNTRY` | الدولة بالإنجليزية، مثل `United States` (تحدد المنطقة الزمنية، العملة، أوقات الصلاة) |
| `BOT_LANGUAGE` | كود لغة البوت، مثل `en`، `fa`، `tr` (يغير فقط ما يقوله البوت) |
| `LLM_PROVIDERS` | موفرو LLM والمفاتيح: `base_url\|api_key\|model`، مفصولة بفواصل |
| `UPDATE_CHECK_ENABLED` | `1` = التحقق من التحديثات يومياً، `0` = لا تتحقق أبداً |
| `UPDATE_REPO` | المستودع الذي تتم مراقبة إصداراته (افتراضي `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | بحث الويب: `searxng` (افتراضي)، `tavily`، أو `serper` |
| `DAILY_LIMIT_MESSAGES` | الحد الأقصى لردود البوت لكل مستخدم يومياً (افتراضي `30`، المالك مستثنى) |

يمكن تغيير الدولة واللغة لاحقاً من لوحة `/admin` المخفية (اللغة والدولة)، دون تعديل أي ملف.

## بديل Docker

إذا كنت تفضل Docker على المثبت:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

هذا يبدأ البوت مع محرك بحث SearXNG مستضاف ذاتيًا. تحقق من السجلات باستخدام `docker compose logs -f bot`.

ملاحظة: أداة التحديث التلقائي تحتاج إلى خدمة systemd، لذا في Docker التحديثات يدوية: `git pull` ثم `docker compose up -d --build` مرة أخرى.

## الميزات بالتفصيل

### لوحة /admin

أرسل `/admin` في محادثة خاصة (للمدير فقط — لا يستطيع أحد غيرك فتحها، ولا تظهر أبداً في `/help` أو القوائم). وهي تتضمن:

- 🔑 **الرموز والنموذج** — إضافة أو إزالة مفاتيح LLM، معرفة المفاتيح السليمة، اختيار النموذج النشط، تصفح قائمة النماذج الحية للمزود
- 👥 **المستخدمون** — عدد المستخدمين، حظر / إلغاء حظر، قائمة المسموحين
- 📊 **الإحصائيات** — أرقام الاستخدام
- 💬 **المحادثات الأخيرة** — ما قاله الناس للبوت (للمدير فقط، خاص)
- 🖼️ **نموذج الصور** — DuckAI (مجاني، افتراضي)، HiLinkUp، خدمة صور مخصصة، أو إيقاف
- 🛡️ **المديرون** — إعطاء أشخاص موثوقين صلاحية الوصول لأجزاء من اللوحة
- 🟢/🔴 **التشغيل** — تشغيل البوت أو إيقافه للجميع (المدير يبقى متحكمًا)
- 🌍 **اللغة والبلد** — تغيير لغة البوت أو بلده في أي وقت

### مجموعة الرموز (Token Pool)

يمكن للبوت الاحتفاظ بمفاتيح من عدة مزودي LLM في وقت واحد. يتناوب بين المفاتيح السليمة ويتحول تلقائياً عند توقف إحداها عن العمل. من `/admin` يمكنك تثبيت نموذج واحد، اختيار نموذج يدوياً، أو ترك البوت يتناوب بحرية. يعمل أي مزود بواجهة برمجة تطبيقات متوافقة مع OpenAI — بما في ذلك المجمعات الصغيرة، وليس الأسماء الكبيرة فقط.

### الصور

توليد الصور له ثلاثة أوضاع: **DuckAI** (مجاني، لا يحتاج مفتاح، افتراضي)، **HiLinkUp** (مدفوع، جودة أفضل)، أو خدمة صور **مخصصة** متوافقة مع OpenAI خاصة بك. يمكنك أيضاً إرسال صورة للبوت وقول كيف تعدلها ("اجعل هذا بأسلوب كرتوني")، وسيولد صورة جديدة. يمكن إيقاف توليد الصور من `/admin`.

### البلدان واللغات

يدعم Vortex **195 دولة** و **40 لغة**. تحدد الدولة المنطقة الزمنية، العملة التي تظهر بها الأسعار، المدينة المستخدمة لأوقات الصلاة، والمحتوى المحلي. اللغة تحدد فقط ما يقوله البوت — يمكن لمجموعة في Belgium استخدام الدولة Belgium واللغة English، على سبيل المثال. يمكن تغيير كلاهما لاحقاً من `/admin`.

### التحديثات

يتحقق البوت من إصدارات GitHub الخاصة بـ `VortexLabsHQ/vortex-telegram-bot` مرة يومياً. عند توفر إصدار جديد، يرسل للمدير رسالة خاصة بأزرار ✅ / ❌. الموافقة تحدث الكود وتعيد تشغيل البوت. بينما المستودع خاص، الفحص لا يفعل شيئاً بصمت (واجهة GitHub البرمجية تحتاج مستودع عام) — اضبط `UPDATE_CHECK_ENABLED=0` إذا كنت لا تريد الفحص أبداً.

## استكشاف الأخطاء / الأسئلة الشائعة

**يقول المثبت أن الرمز (token) الخاص بي غير صالح.**
يأتي الرمز من [@BotFather](https://t.me/BotFather). تأكد من نسخ الرمز كاملاً (أرقام، ثم نقطتان، ثم 35 حرفاً أو أكثر)، بدون مسافات إضافية. إذا حذفت البوت أو أنشأت رمزاً جديداً، يتوقف الرمز القديم عن العمل — الصق الرمز الجديد.

**البوت لا يجيب في مجموعتي.**
أربعة أشياء يجب التحقق منها: (١) يجب إيقاف خصوصية المجموعة — في [@BotFather](https://t.me/BotFather) أرسل `/setprivacy`، اختر بوتك، واختر **Disable**؛ مع تفعيل الخصوصية، لا يستطيع البوت رؤية رسائل المجموعة على الإطلاق، (٢) يجب إضافة البوت إلى المجموعة، (٣) يجب قول كلمة التنبيه — اسمه، على سبيل المثال `Vortex what's the time?` — البوت يستمع فقط عند ذكر اسمه في المجموعات، (٤) في محادثة خاصة لا حاجة لكلمة تنبيه على الإطلاق.

**البوت يجيب بالإنجليزية، وليس بلغتي.**
أرسل `/admin` (للمدير فقط) → اللغة والبلد، واختر لغتك. المثبت يسأل أيضاً عن اللغة — اضغط Enter هناك لقبول لغة بلدك الافتراضية.

**اخترت Anthropic والبوت لا يتحدث.**
واجهة برمجة التطبيقات (API) الأصلية لـ Anthropic غير متوافقة مع OpenAI، لذا لا يستطيع البوت الدردشة معها مباشرة. استخدم OpenRouter (الذي يمكنه تقديم نماذج Claude عبر API متوافق مع OpenAI)، أو اختر مزوداً آخر من القائمة.

**البحث على الويب لا يعمل.**
البحث على الويب يحتاج SearXNG، الذي يعرض المثبت إعداده باستخدام Docker. بدونه، يعود البوت لويكيبيديا، وهي أضعف. يمكنك أيضاً تعيين `SEARCH_PROVIDER=tavily` أو `serper` مع `SEARCH_API_KEY` في ملف `.env`.

**أين توجد السجلات (Logs)?**
`journalctl -u vortex-bot -f` يعرض السجل المباشر. `systemctl status vortex-bot` يوضح ما إذا كانت الخدمة تعمل. إذا توقف البوت، `sudo systemctl restart vortex-bot` يعيد تشغيله مرة أخرى.

**البوت يقول إنني وصلت للحد اليومي.**
يحصل كل مستخدم على 30 رداً من البوت يومياً (المدير مستثنى). يعاد تعيين الحد عند منتصف الليل في المنطقة الزمنية لبلد البوت. ارفعه باستخدام `DAILY_LIMIT_MESSAGES` في ملف `.env`، أو اسأل المدير.

**وجدت خطأ / لدي فكرة.**
يرجى فتح Issue على GitHub — راجع [CONTRIBUTING.md](CONTRIBUTING.md) لمعرفة كيفية الإبلاغ عنه وكيفية إرسال إصلاح.

## التطوير

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

شغّل الاختبارات (سكريبتات Python عادية، لا حاجة لـ pytest):

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

يجب أن تنجح جميع مجموعات الاختبار التسع قبل فتح طلب سحب. راجع [CONTRIBUTING.md](CONTRIBUTING.md) لمعرفة نمط الكود (ruff) وعملية طلب السحب.

## الترخيص

يُصدر Vortex بموجب [ترخيص MIT](LICENSE) — مجاني للاستخدام، والنسخ، والتعديل، والمشاركة، لأي غرض.

<a id="countries"></a>

## الدول

الصق اسم البلد **بالإنكليزية، تماماً كما هو مكتوب هنا** عندما يطلب منك المثبت بلدك. الجدول مُولَّد من `bot/countries.py` — إذا اختلف اسم هنا واسم هناك، فـ `bot/countries.py` هو المعتمد.

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

## شكراً لك

> ⭐ **يرجى وضع نجمة لهذا المشروع على GitHub ومتابعة [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — فهذه أبسط طريقة لدعم Vortex ومساعدة الآخرين في العثور عليه. شكراً لك!
