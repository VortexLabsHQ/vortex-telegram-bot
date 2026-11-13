# Vortex 🤖 — آپ کا اپنا ٹیلیگرام گروہ اسسٹنٹ

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · **اردو** · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **اگر آپ کو Vortex پسند ہے، تو براہ کرم اس پروجیکٹ کو GitHub پر اسٹار دیں اور [@VortexLabsHQ](https://github.com/VortexLabsHQ) کو فالو کریں** — اس سے زیادہ لوگ اسے تلاش کر سکیں گے۔ شکریہ!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ورٹیکس کیا ہے؟

ورٹیکس ایک ٹیلیگرام بوٹ ہے جو آپ کے گروپس اور پرائیویٹ چیٹس میں رہتا ہے اور ایک AI چیٹ ماڈل کے ذریعے لوگوں کو جواب دیتا ہے۔ آپ اس کا نام لیں (ڈیفالٹ نام **Vortex** ہے) اور یہ جواب دیتا ہے — یہ بات کر سکتا ہے، ویب تلاش کر سکتا ہے، تصاویر بنا سکتا ہے، قیمتیں چیک کر سکتا ہے، مذاق سنا سکتا ہے، فائلیں پڑھ سکتا ہے، آواز کے پیغامات کا ترجمہ کر سکتا ہے، اور بہت کچھ۔

یہ آپ کے اپنے سرور پر چلتا ہے، آپ کے اپنے ملک اور زبان میں۔ آپ ہی باس ہیں: ایک چھپا ہوا `/admin` پینل آپ کو AI کیز، صارفین، اور سیٹنگز منیج کرنے دیتا ہے۔

## خصوصیات

- 💬 **AI چیٹ** گروپس میں (ویک ورڈ کے ساتھ) اور پرائیویٹ چیٹس میں (کوئی ویک ورڈ درکار نہیں)
- 🔑 **ٹوکن پول** — کئی LLM فراہم کنندگان اور کلیدیں استعمال کریں، خودکار طور پر روٹیٹ اور فیل اوفر کریں
- 🖼️ **تصویر بنانا اور ایڈٹنگ** — مفت (DuckAI) یا ادا شدہ فراہم کنندگان
- 🔍 **ویب سرچ** — سلف-ہوسٹڈ SearXNG، ویکیپیڈیا فال بیک کے ساتھ
- 💰 **لائیو قیمتیں** — کرنسیز، سونا، تیل، اور کرپٹو آپ کی مقامی کرنسی میں
- 🕌 **نماز کے اوقات**، 🃏 **فالیں**، 😄 **جوکس**، 🎲 **پاسے اور سکہ اچھالنا**
- 📎 **فائل تجزیہ** اور **آواز کا ٹرانسکرپشن**
- 📥 **ڈاؤن لوڈز** — لنک بھیجیں، میڈیا فایل واپس پائیں (45 MB تک)
- 🌍 **195 ممالک** اور **40 زبانیں** — ملک اور زبان الگ الگ سیٹنگز ہیں
- 🔄 **خود آپ ڈیٹ ہونا** — روزانہ نئی ریلیزز چیک کرتا ہے اور آپ ڈیٹ کرنے سے پہلے پوچھتا ہے
- 🛡️ **چھپا ہوا /ایڈمن پنل** — ٹوکنز، یوزرز، اسٹٹس، چیٹس، امیج ماڈل، مینیجرز، پاور

## تنصیب سے پہلے

آپ کو ایک سرور (یا ایک کمپیوٹر جو چالو رہے) کی ضرورت ہے جس پر **Linux** چل رہا ہو اور یہ چیزیں نصب ہوں:

| کیا | کیسے چیک کریں | آپ کو کیا نظر آنا چاہیے |
| --- | --- | --- |
| **Python 3.11 یا نئی** | `python3 --version` | `Python 3.11.x` یا اعلی (3.12 اور 3.13 بھی کام کریں گے) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` یا `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` یا مماثل |
| **Docker** *(اختیاری)* | `docker --version` | `Docker version 2x.x.x` — اس کی ضرورت صرف تب ہے جب آپ اختیاری SearXNG ویب سرچ چاہتے ہوں |

اگر کچھ کمی ہو تو ایک کمانڈ سے سب کچھ انسٹال کریں (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

اختیاری Docker کے لیے (صرف اس صورت میں ضروری ہے اگر آپ SearXNG ویب سرچ چاہتے ہیں):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

آخری لائن کے بعد، لاگ آؤٹ کریں اور واپس لاگ ان کریں (یا `docker` کمانڈز `sudo` کے ساتھ چلائیں)। انسٹالر آپ کو `apt` کے ذریعے Debian/Ubuntu پر موجودہ ٹولز انسٹال کرنے کی پیشکش بھی کرتا ہے۔ دوسری سسٹمز پر، پہلے اپنے پیکیج مینیجر سے انہیں انسٹال کریں۔ `systemd` سسٹم کے ساتھ آتا ہے — اسے الگ سے انسٹال نہیں کیا جا سکتا۔

آپ کو ٹیلیگرام سے دو چیزوں کی بھی ضرورت ہے (دونوں مفت ہیں):

1. **ایک بوٹ ٹوکن** — ٹیلیگرام پر [@BotFather](https://t.me/BotFather) سے بات کریں، `/newbot` بھیجیں، اور جو ٹوکن وہ دے اسے کاپی کریں۔
2. **آپ کا نمبرین ٹیلیگرام یوزر آئی ڈی** — [@userinfobot](https://t.me/userinfobot) سے بات کریں اور جو نمبر وہ دکھائے اسے کاپی کریں۔ یہ آپ کا "باس" آئی ڈی ہے: صرف یہ اکاؤنٹ `/admin` استعمال کر سکتا ہے۔

## تنصیب

ایک کمانڈ۔ اسے کاپی کریں، اپنے ٹرمینل میں پیسٹ کریں، اور انٹر دبائیں:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

انسٹالر آپ سے چھ سوالات پوچھتا ہے، ترتیب وار:

1. **ملک** — اپنا ملک کا انگریزی نام **بالکل وہی پیسٹ کریں جو نیچے [ملک ٹیبل](#countries) میں درج ہے** (مثال کے طور پر `Turkey`)۔ ملک ٹائم زون، قیمتیں کے لیے مقامی کرنسی، نماز کے اوقات، اور مقامی مواد متعین کرتا ہے۔
2. **زبان** — وہ زبان جو بوٹ بولتا ہے (مثال کے طور پر `en`، `fa`، `tr`)。 اپنا ملک کے ڈیفالٹ کو قبول کرنے کے لیے انٹر دبائیں۔ زبان ملک سے الگ ہے: یہ صرف یہ بدلتا ہے کہ بوٹ کیا کہتا ہے، اور آپ اسے بعد میں `/admin` سے بدل سکتے ہیں۔
3. **بوٹ ٹوکن** — [@BotFather](https://t.me/BotFather) سے ٹوکن پیسٹ کریں۔ انسٹالر اسے ٹیلیگرام کے ساتھ لائیو چیک کرتا ہے۔
4. **باس نمبرک آئی ڈی** — آپ کا ٹیلیگرام یوزر آئی ڈی [@userinfobot](https://t.me/userinfobot) سے۔
5. **بوٹ کا نام / ويک ورڈ** — وہ نام جو لوگ گروپوں میں بوٹ سے بات کرنے کے لیے کہتے ہیں۔ کوئی بھی زبان چلے گی (مثال کے طور پر `Vortex` یا `ورتکس`)۔ ڈیفالٹ `Vortex` کے لیے انٹر دبائیں۔
6. **پہلا LLM فراہم کنندہ** — ایک منتخب کریں: OpenAI، Anthropic، OpenRouter، Google AI (Gemini)، DeepSeek، Groq، Together AI، Mistral AI، xAI (Grok)، Cohere، یا **کسٹم** (بейس URL پیسٹ کریں)۔ پھر اس فراہم کنندہ کے لیے اپنا API کی پیسٹ کریں — انسٹالر فراہم کنندہ کی لائیو ماڈل فہرست حاصل کرتا ہے اور آپ ایک ماڈل منتخب کرتے ہیں۔

پھر انسٹالر ڈپنڈنسیز انسٹال کرتا ہے، `.env` فائل لکھتا ہے، `vortex-bot` systemd سروس بناتا ہے، ویب سرچ کے لیے SearXNG انسٹال کرنے کی پیشکش کرتا ہے (ڈوکر درکار ہے)، اور بوٹ شروع کرتا ہے۔

> ⚠️ **Anthropic براہ راست کام نہیں کرتا۔** Anthropic کا نیٹیو API OpenAI-مطابق نہیں ہے، اور یہ بوٹ صرف OpenAI-مطابق APIs بولتا ہے۔ اگر آپ Anthropic منتخب کرتے ہیں، تو انسٹالر آپ کو خبردار کرتا ہے: کلید صرف OpenAI-مطابق گیٹ وے کے ذریعے کام کرتی ہے۔ اس کی جگہ OpenRouter، یا فہرست سے کوئی اور فراہم کنندہ استعمال کریں۔

## تنصیب کے بعد

چیک کریں کہ بوٹ چل رہا ہے:

```bash
systemctl status vortex-bot
```

آپ کو `active (running)` نظر آنا چاہیے۔ لائیو لاگ دیکھنے کے لیے:

```bash
journalctl -u vortex-bot -f
```

اب ٹیلیگرام کھولیں اور اپنے بوٹ سے بات کریں:

- `/start` بھیجیں — بوٹ ہیلو کہے گا۔
- **پرائیویٹ چیٹ** میں، بس اسے لکھیں — کوئی ويک ورڈ درکار نہیں۔
- **گروپ** میں، بوٹ کو گروپ میں شامل کریں، پھر گروپ پرائیویسی بند کریں: [@BotFather](https://t.me/BotFather) میں `/setprivacy` بھیجیں، اپنا بوٹ منتخب کریں، اور **Disable** چنیں — ورنہ بوٹ گروپ کے پیغامات نہیں دیکھ سکے گا اور اس کا ویک ورڈ نہیں سنے گا۔ پھر اس کا نام بولیں، مثلاً: `Vortex what's the time?`
- باس کے طور پر، پرائیویٹ چیٹ میں `/admin` بھیجیں تا کہ چھپا ہوا ایڈمن پینل کھل جائے۔

**اپڈیٹس خودکار ہیں۔** دن میں ایک بار بوٹ گٹ ہب پر نئی ریلیز چیک کرتا ہے۔ اگر دستیاب ہو، تو یہ آپ کو ✅ / ❌ بٹنز کے ساتھ پرائیویٹ میسج بھیجتا ہے۔ ✅ دبائیں اور یہ خود اپڈیٹ ہو کر ریستارٹ ہو جائے گا — آپ کو کبھی سرور کو چھونے کی ضرورت نہیں پڑے گی۔

## ترتیب

तमाम ترتیبات `.env` فائل میں نصب کی ڈائریکٹری میں موجود ہیں۔ ہر آپشن کے لیے [`.env.example`](.env.example) دیکھیں۔ سب سے اہم یہ ہیں:

| ترتیب | یہ کیا کرتا ہے |
| --- | --- |
| `BOT_TOKEN` | آپ کا ٹیلیگرام بوٹ ٹوکن (@BotFather سے) |
| `BOSS_ID` | آپ کی نمبرین ٹیلیگرام یوزر آئی ڈی (بوٹ کا مالک) |
| `BOT_NAME` | گروپوں میں بوٹ کا نام اور ويک ورڈ (ڈیفالٹ `Vortex`) |
| `BOT_COUNTRY` | ملک انگریزی میں، مثلاً `United States` (ٹائم زون، کرنسی، نماز کے اوقات سیٹ کرتا ہے) |
| `BOT_LANGUAGE` | بوٹ کا لینگویج کوڈ، مثلاً `en`، `fa`، `tr` (صرف یہ بدلتا ہے کہ بوٹ کیا بولتا ہے) |
| `LLM_PROVIDERS` | LLM فراہم کنندے اور کیز: `base_url\|api_key\|model`، کاما سے جدا کردہ |
| `UPDATE_CHECK_ENABLED` | `1` = روزانہ اپ ڈیٹ چیک کریں، `0` = کبھی چیک نہ کریں |
| `UPDATE_REPO` | وہ ریپو جس کے ریلیز دیکھے جاتے ہیں (ڈیفالٹ `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | ویب سرچ: `searxng` (ڈیفالٹ)، `tavily`، یا `serper` |
| `DAILY_LIMIT_MESSAGES` | فی یوزر فی دن زیادہ سے زیادہ بوٹ کے جوابات (ڈیفالٹ `30`، بوس معاف ہے) |

ملک اور زبان بعد میں چھپے ہوئے `/admin` پینل (Language & Country) سے بھی بدلی جا سکتی ہے، بغیر کسی فائل کو ادیت کیے۔

## ڈوکر کا متبادل

اگر آپ انسٹالر کے بجائے ڈوکر کو ترجیح دیتے ہیں:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

یہ بوٹ کو خود-ہوسٹڈ SearXNG سرچ انجن کے ساتھ شروع کرتا ہے۔ لاگز چیک کریں `docker compose logs -f bot` کے ساتھ۔

نوٹ: خودکار سیلف-اپڈیٹر کو systemd سروس کی ضرورت ہوتی ہے، اس لیے ڈوکر میں اپڈیٹس دستی ہیں: `git pull` اور پھر دوبارہ `docker compose up -d --build`۔

## تفصیلی خصوصیات

### /admin پینل

پرائیویٹ چیٹ میں `/admin` بھیجیں (صرف باس کے لیے — کوئی اور اسے نہیں کھول سکتا، اور یہ کبھی `/help` یا مینوز میں ظاہر نہیں ہوتا)। اس میں ہے:

- 🔑 **ٹوکنز اور ماڈل** — LLM کیز شامل کریں یا ہٹائیں، دیکھیں کون سی کیز صحت مند ہیں، فعال ماڈل منتخب کریں، فراہم کنندہ کی لائیو ماڈل فہرست براؤز کریں
- 👥 **صارفین** — صارفین کی تعداد، بن/ان بن، اجازت یافتہ فہرست
- 📊 **آंकڑے** — استعمال کی تعداد
- 💬 **حالیہ چیٹیں** — لوگوں نے بوٹ سے کیا کہا (صرف باس، پرائیویٹ)
- 🖼️ **تصویری ماڈل** — DuckAI (مفت، ڈیفالٹ)، HiLinkUp، اپنی مرضی کی تصویری سروس، یا بند
- 🛡️ **منیجرز** — قابل اعتماد لوگوں کو پینل کے حصوں تک رسائی دیں
- 🟢/🔴 **پاور** — سب کے لیے بوٹ آن یا آف کریں (باس کنٹرول میں رہتا ہے)
- 🌍 **زبان اور ملک** — بوٹ کی زبان یا ملک کبھی بھی تبدیل کریں

### ٹوکن پول

بوٹ ایک ساتھ کئی LLM فراہم کنندگان سے کیز رکھ سکتا ہے۔ یہ صحت مند کیز کے درمیان گھومتا رہتا ہے اور جب کوئی کام کرنا بند کر دے تو خود بخود دوسری پر چلا جاتا ہے۔ `/admin` سے آپ ایک ماڈل کو پن کر سکتے ہیں، دستی طور پر ماڈل منتخب کر سکتے ہیں، یا بوٹ کو آزادانہ گھومنے دے سکتے ہیں۔ OpenAI-مطابق API والا کوئی بھی فراہم کنندہ کام کرتا ہے — چھوٹے اجریگیٹرز بھی، صرف بڑے نام نہیں۔

### تصاویر

تصویری تخلیق کے تین موڈ ہیں: **DuckAI** (مفت، کوئی کلید نہیں، ڈیفالٹ)، **HiLinkUp** (ادائی، بہتر معیار)، یا اپنی **مخصوص** OpenAI-مطابق تصویری سروس۔ آپ بوٹ کو فوٹو بھیج کر بتا سکتے ہیں کہ اسے کیسے ایڈٹ کرنا ہے ("اسے کارٹون اسٹائل بنائیں")، اور یہ نئی تصویر بنائے گا۔ تصویری تخلیق کو `/admin` سے بند کیا جا سکتا ہے۔

### ممالک اور زبانیں

Vortex **195 ممالک** اور **40 زبانیں** سپورٹ کرتا ہے۔ ملک ٹائم زون، کرنسی جس میں قیمتیں دکھائی جاتی ہیں، نماز کے اوقات کے لیے شہر، اور مقامی مواد متعین کرتا ہے۔ زبان صرف یہ متعین کرتی ہے کہ بوٹ کیا بولتا ہے — مثلاً بیلجیم میں گروپ ملک بیلجیم اور زبان انگریزی استعمال کر سکتا ہے۔ دونوں کو بعد میں `/admin` سے تبدیل کیا جا سکتا ہے۔

### اپڈیٹس

بوٹ روزانہ ایک بار `VortexLabsHQ/vortex-telegram-bot` کے GitHub ریلیز چیک کرتا ہے۔ جب نئی ورژن آتی ہے، تو یہ باس کو پرائیویٹ پیغام بھیجتا ہے جس میں ✅ / ❌ بٹنز ہوتے ہیں۔ منظور کرنے پر کوڈ اپڈیٹ ہوتا ہے اور بوٹ ریستارٹ ہوتا ہے۔ جب تک ریپو پرائیویٹ ہے، چیک خاموشی سے کچھ نہیں کرتا (GitHub کے API کو پبلک ریپو درکار ہے) — اگر آپ کبھی چیک نہیں چاہتے تو `UPDATE_CHECK_ENABLED=0` سیٹ کریں۔

## ٹрабل شوٹنگ / اکثر پوچھے جانے والے سوالات

**انسٹالر کہتا ہے کہ میرا ٹوکن غلط ہے۔**
ٹوکن [@BotFather](https://t.me/BotFather) سے ملتا ہے۔ یقینی بنائیں کہ آپ نے پورا ٹوکن کاپی کیا ہے (انک، کولن، پھر 35+ حروف)، بغیر کسی اضافی خالی جگہ کے۔ اگر آپ نے بوٹ ڈیلیٹ کر دیا یا نیا ٹوکن بنا لیا، پرانا کام کرنا بند کر دیتا ہے — نئے کو پیسٹ کریں۔

**بوٹ میری گروپ میں جواب نہیں دیتا۔**
چیزیں چیک کرنے کے لیے چار باتیں: (۱) گروپ پرائیویسی ضرور بند ہونی چاہیے — [@BotFather](https://t.me/BotFather) میں `/setprivacy` بھیجیں، اپنا بوٹ منتخب کریں، اور **Disable** چنیں؛ اگر پرائیویسی آن ہو تو بوٹ گروپ کے پیغامات بالکل نہیں دیکھ سکے گا، (۲) بوٹ کو گروپ میں شامل کرنا ضروری ہے، (۳) آپ کو اس کا ویک ورڈ بولنا ہوگا — اس کا نام، مثلاً `Vortex what's the time?` — بوٹ گروپوں میں صرف تب سنتا ہے جب اس کا نام bola جائے، (۴) پرائیویٹ چیٹ میں کوئی ویک ورڈ درکار نہیں ہوتا۔

**بوٹ انگریزی میں جواب دیتا ہے، میری زبان میں نہیں۔**
`/admin` بھیجیں (صرف بوس کے لیے) → Language & Country، اور اپنی زبان منتخب کریں۔ انسٹالر بھی زبان پوچھتا ہے — وہاں انٹر دبائیں تاہا کہ آپ کے ملک کی ڈیفالٹ زبان منظور ہو جائے۔

**میں نے Anthropic منتخب کیا اور بوٹ بات نہیں کرتا۔**
Anthropic کا نیٹیو API OpenAI-کمپیٹیبل نہیں، اس لیے بوٹ اس سے براہ راست بات نہیں کر سکتا۔ OpenRouter استعمال کریں ( جو کلاؤڈ ماڈلز کو OpenAI-کمپیٹیبل API کے ذریعے فراہم کر سکتا ہے)، یا فہرست سے کوئی اور فراہم کنندہ منتخب کریں۔

**ویب سرچ کام نہیں کرتا۔**
ویب سرچ کو SearXNG کی ضرورت ہوتی ہے، جسے انسٹالر ڈوکر کے ساتھ سیٹ اپ کرنے کی پیشکش کرتا ہے۔ اس کے بغیر، بوٹ ویکیپیڈیا پر واپس آتا ہے، جو کمزور ہے۔ آپ `.env` میں `SEARCH_API_KEY` کے ساتھ `SEARCH_PROVIDER=tavily` یا `serper` بھی سیٹ کر سکتے ہیں۔

**لاگز کہاں ہیں؟**
`journalctl -u vortex-bot -f` لائیو لاگ دکھاتا ہے۔ `systemctl status vortex-bot` دکھاتا ہے کہ سروس چل رہی ہے یا نہیں۔ اگر بوٹ ruk جائے، `sudo systemctl restart vortex-bot` اسے دوبارہ چلاتا ہے۔

**بوٹ کہتا ہے کہ میں دن کی حد تک پہنچ گیا ہوں۔**
ہر صارف کو فی دن 30 بوٹ رپلائیز ملتی ہیں (بوس معاف ہے)۔ حد بوٹ کے ملک کے ٹائم زون میں رات 12 بجے ریسیٹ ہوتی ہے۔ اسے `.env` میں `DAILY_LIMIT_MESSAGES` سے بڑھائیں، یا بوس سے پوچھیں۔

**مجھے بگ ملا / میرا ایک خیال ہے۔**
براہ کرم GitHub پر ا슈و کھولیں — دیکھیں [CONTRIBUTING.md](CONTRIBUTING.md) کہ کیسے رپورٹ کرنا ہے اور کیسے فکس بھیجنا ہے۔

## ڈویلپمنٹ

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

ٹیسٹ چلائیں (سادہ پائیتھن اسکرپٹ، pytest کی ضرورت نہیں):

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

پل ریکوسٹ کھولنے سے پہلے نووں سوئٹس کا پاس ہونا ضروری ہے۔ کوڈ اسٹائل (ruff) اور PR عمل کے لیے [CONTRIBUTING.md](CONTRIBUTING.md) دیکھیں۔

## لائسنس

Vortex [MIT لائسنس](LICENSE) کے تحت جاری کیا گیا ہے — کسی بھی مقصد کے لیے مفت استعمال، کاپی، تبدیلی، اور اشتراک کی اجازت ہے۔

<a id="countries"></a>

## ممالک

جب انسٹالر آپ سے آپ کا ملک پوچھے تو ملک کا نام **انگریزی میں، بالکل یہاں لکھے ہوئے مطابق** پیسٹ کریں۔ یہ ٹیبل `bot/countries.py` سے جنریٹ ہوئی ہے — اگر یہاں اور وہاں نام میں کوئی اختلاف ہو تو `bot/countries.py` کو درست سمجھا جائے۔

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

## شکریہ

> ⭐ **براہ کرم اس پروجیکٹ کو GitHub پر اسٹار دیں اور [@VortexLabsHQ](https://github.com/VortexLabsHQ) کو فالو کریں** — یہ Vortex کو سپورٹ کرنے اور دوسروں تک پہنچانے کا سب سے آسان طریقہ ہے۔ شکریہ!
