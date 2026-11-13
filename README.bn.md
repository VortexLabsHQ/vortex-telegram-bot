# Vortex 🤖 — আপনার নিজস্ব টেলিগ্রাম গ্রুপ সহায়ক

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · **বাংলা** · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **আপনি যদি Vortex পছন্দ করেন, দয়া করে GitHub-এ এই প্রজেক্টটিকে স্টার দিন এবং [@VortexLabsHQ](https://github.com/VortexLabsHQ) ফলো করুন — এটি আরও মানুষকে খুঁজে পেতে সাহায্য করে। ধন্যবাদ!**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex কী?

Vortex হল একটি Telegram বট যা আপনার গ্রুপ এবং প্রাইভেট চ্যাটে থাকে এবং একটি AI চ্যাট মডেল ব্যবহার করে মানুষের প্রশ্নের উত্তর দেয়। আপনি এর নাম বলুন (ডিফল্ট নাম হল **Vortex**) এবং এটি উত্তর দেবে — এটি চ্যাট করতে পারে, ওয়েব সার্চ করতে পারে, ছবি তৈরি করতে পারে, দাম চেক করতে পারে, জোক বলতে পারে, ফাইল পড়তে পারে, ভয়েস মেসেজ ট্রান্সক্রাইব করতে পারে, এবং আরও অনেক কিছু।

এটি আপনার নিজের সার্ভারে, আপনার নিজের দেশে এবং ভাষায় চলে। আপনি বস: একটি লুকানো `/admin` প্যানেল আপনাকে AI কী, ব্যবহারকারী, এবং সেটিংস পরিচালনা করতে দেয়।

## বৈশিষ্ট্য

- 💬 **AI চ্যাট** গ্রুপে (ওয়েক ওয়ার্ড) এবং প্রাইভেট চ্যাটে (ওয়েক ওয়ার্ডের প্রয়োজন নেই)
- 🔑 **টোকেন পুল** — একাধিক LLM প্রোভাইডার এবং কী ব্যবহার করুন, স্বয়ংক্রিয়ভাবে রোটেট এবং ফেইলওভার করুন
- 🖼️ **ছবি তৈরি** — আপনার নিজস্ব ছবি সার্ভিস (বেস URL + API কী + মডেল) দিয়ে, `/admin`-এ যোগ করা হয়েছে
- 🔍 **ওয়েব সার্চ** — সেলফ-হোস্টেড SearXNG, উইকিপিডিয়া ফলব্যাকসহ
- 💰 **লাইভ দাম** — মুদ্রা, সোনা, তেল, এবং ক্রিপ্টো আপনার স্থানীয় মুদ্রায়
- 🕌 **নামাজের সময়**, 🃏 **ভাগ্য**, 😄 **জোকস**, 🎲 **পাসা এবং টস**
- 📎 **ফাইল বিশ্লেষণ** এবং **ভয়েস ট্রান্সক্রিপশন**
- 📥 **ডাউনলোড** — লিংক পাঠান, মিডিয়া ফাইলটি ফিরে পান (৪৫ MB পর্যন্ত)
- 🌍 **১৯৫ দেশ** এবং **৪০ ভাষা** — দেশ এবং ভাষা আলাদা সেটিংস
- 🔄 **স্বয়ংক্রিয় আপডেট** — প্রতিদিন নতুন রিলিজ চেক করে এবং আপডেট করার আগে আপনাকে জিজ্ঞাসা করে
- 🛡️ **লুকানো /admin প্যানেল** — টোকেন, ব্যবহারকারী, পরিসংখ্যান, চ্যাট, ইমেজ মডেল, ম্যানেজার, পাওয়ার

## ইনস্টল করার আগে

আপনার একটি সার্ভার (অথবা একটি কম্পিউটার যা সবসময় চালু থাকে) দরকার যেটি **Linux** চালাচ্ছে এবং নিচের জিনিসগুলো ইনস্টল করা আছে:

| কী | কীভাবে চেক করবেন | কী দেখতে পাবেন |
| --- | --- | --- |
| **Python 3.11 বা নতুন‌تر** | `python3 --version` | `Python 3.11.x` বা উচ্চতর (3.12 এবং 3.13-ও কাজ করবে) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` বা `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` বা অনুরূপ |
| **Docker** *(ঐচ্ছিক)* | `docker --version` | `Docker version 2x.x.x` — শুধু দরকার যদি আপনি ঐচ্ছিক SearXNG ওয়েব সার্চ চান |

যদি কিছু অনুপস্থিত থাকে, তবে একক কমান্ড দিয়ে সবকিছু ইনস্টল করুন (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

ঐচ্ছিক `Docker` এর জন্য (শুধু `SearXNG` ওয়েব সার্চ চাইলে প্রয়োজন):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

শেষ লাইনের পরে, লগ আউট করে আবার লগ ইন করুন (অথবা `sudo` দিয়ে `docker` কমান্ড চালান)। ইনস্টলার আপনার জন্য অনুপস্থিত টুলগুলো `apt` দিয়ে `Debian/Ubuntu`-এ ইনস্টল করার প্রস্তাব দেয়। অন্যান্য সিস্টেমে, প্রথমে আপনার প্যাকেজ ম্যানেজারের মাধ্যমে সেগুলো ইনস্টল করুন। `systemd` সিস্টেমের সাথে আসে — এটি আলাদাভাবে ইনস্টল করা যায় না।

আপনার টেলিগ্রাম থেকে দুটি জিনিসও দরকার (দুটোই ফ্রি):

1. **একটি বট টোকেন** — টেলিগ্রামে [@BotFather](https://t.me/BotFather)-এর সাথে কথা বলুন, `/newbot` পাঠান, এবং সেটি যা টোকেন দেবে সেটি কপি করুন।
2. **আপনার সংখ্যাসূচক টেলিগ্রাম ইউজার আইডি** — [@userinfobot](https://t.me/userinfobot)-এর সাথে কথা বলুন এবং সেটি যা নম্বর দেখাবে সেটি কপি করুন। এটি আপনার "বস" আইডি: শুধু এই একাউন্ট `/admin` ব্যবহার করতে পারবে।

## ইনস্টল

একটি কমান্ড। এটি কপি করুন, আপনার টার্মিনালে পেস্ট করুন, এবং এন্টার চাপুন:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

ইনস্টলার আপনাকে ক্রমে ছয়টি প্রশ্ন জিজ্ঞাসে করবে:

1. **দেশ** — আপনার দেশের ইংরেজি নাম **নিচের [দেশের তালিকায়](#countries) দেওয়া অনুযায়ী ঠিক সেইভাবে** পেস্ট করুন (উদাহরণস্বরূপ `Turkey`)। দেশটি টাইম জোন, দামের জন্য স্থানীয় মুদ্রা, নামাজের সময়, এবং স্থানীয় কন্টেন্ট নির্ধারণ করে।
2. **ভাষা** — বট যে ভাষায় কথা বলে (উদাহরণস্বরূপ `en`, `fa`, `tr`)। আপনার দেশের ডিফল্ট গ্রহণ করতে এন্টার চাপুন। ভাষা দেশ থেকে আলাদা: এটি শুধু বট যা বলে তা পরিবর্তন করে, এবং আপনি পরে `/admin` থেকে এটি পরিবর্তন করতে পারেন।
3. **বট টোকেন** — [@BotFather](https://t.me/BotFather) থেকে টোকেন পেস্ট করুন। ইনস্টলার টেলিগ্রামের সাথে লাইভভাবে এটি যাচাই করে।
4. **বসের সংখ্যাগত আইডি** — [@userinfobot](https://t.me/userinfobot) থেকে আপনার টেলিগ্রাম ইউজার আইডি।
5. **বটের নাম / ওয়েক ওয়ার্ড** — গ্রুপে লোকেরা বটের সাথে কথা বলতে যে নাম ব্যবহার করে। যেকোনো ভাষা চলবে (উদাহরণস্বরূপ `Vortex` বা `ورتکس`)। ডিফল্ট `Vortex` এর জন্য এন্টার চাপুন।
6. **প্রথম LLM প্রদানকারী** — একটি বেছে নিন: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, অথবা **কাস্টম** (একটি বেস URL পেস্ট করুন)। তারপর সেই প্রদানকারীর জন্য আপনার API কী পেস্ট করুন — ইনস্টলার প্রদানকারীর লাইভ মডেল তালিকা আনবে এবং আপনি একটি মডেল বেছে নেবেন।

তারপর ইনস্টলার নির্ভরতা ইনস্টল করে, `.env` ফাইল লিখে, `vortex-bot` systemd সার্ভিস তৈরি করে, ওয়েব সার্চের জন্য SearXNG ইনস্টল করার প্রস্তাব দেয় (ডকার প্রয়োজন), এবং বট শুরু করে।

> ⚠️ **Anthropic সরাসরি কাজ করে না।** Anthropic-এর নেটিভ API OpenAI-সামঞ্জস্যপূর্ণ নয়, এবং এই বট শুধু OpenAI-সামঞ্জস্যপূর্ণ API বোঝে। আপনি যদি Anthropic বেছে নেন, ইনস্টলার আপনাকে সতর্ক করবে: কীটি শুধু OpenAI-সামঞ্জস্যপূর্ণ গেটওয়ে 통해서 কাজ করে। বদলে OpenRouter, বা তালিকা থেকে অন্য কোনো প্রদানকারী ব্যবহার করুন।

## ইনস্টল করার পর

চেক করুন যে বটটি চলছে:

```bash
systemctl status vortex-bot
```

আপনাকে `active (running)` দেখতে পাবেন। লাইভ লগ দেখতে:

```bash
journalctl -u vortex-bot -f
```

এখন টেলিগ্রাম খুলুন এবং আপনার বটের সাথে কথা বলুন:

- `/start` পাঠান — বটটি হ্যালো বলবে।
- একটি **প্রাইভেট চ্যাটে**, শুধু এটিতে লিখুন — কোনো ওয়েক ওয়ার্ড দরকার নেই।
- একটি **গ্রুপে**-এ বটটি যোগ করুন, তারপর গ্রুপ প্রাইভেসি বন্ধ করুন: [@BotFather](https://t.me/BotFather)-এ `/setprivacy` পাঠান, আপনার বটটি বেছে নিন, এবং **Disable** বেছে নিন — অন্যথায় বটটি গ্রুপের বার্তাগুলো দেখতে পারবে না এবং এর ওয়েক ওয়ার্ড শুনতে পারবে না। তারপর এর নাম বলুন, উদাহরণস্বরূপ: `Vortex what's the time?`
- বস হিসেবে, একটি প্রাইভেট চ্যাটে `/admin` পাঠান লুকানো অ্যাডমিন প্যানেল খোলার জন্য।

**আপডেটগুলি স্বয়ংক্রিয়।** দিনে একবার বটটি GitHub-এ নতুন রিলিজের জন্য চেক করে। যদি উপলব্ধ থাকে, তবে এটি আপনাকে ✅ / ❌ বাটন সহ একটি প্রাইভেট মেসেজ পাঠায়। ✅ ট্যাপ করুন এবং এটি নিজে আপডেট হয়ে রিস্টার্ট হবে — আপনাকে কখনো সার্ভার ছুঁওতে হবে না।

## কনফিগারেশন

সभी সেটিংস ইনস্টল ডিরেক্টরির `.env` ফাইলে থাকে। প্রতিটি অপশনের জন্য [`.env.example`](.env.example) দেখুন। সবচেয়ে গুরুত্বপূর্ণ موارد:

| Setting | এটি কী করে |
| --- | --- |
| `BOT_TOKEN` | আপনার টেলিগ্রাম বট টোকেন (@BotFather থেকে) |
| `BOSS_ID` | আপনার সংখ্যাসূচক টেলিগ্রাম ইউজার আইডি (বটের মালিক) |
| `BOT_NAME` | বটের নাম এবং গ্রুপে ওয়েক ওয়ার্ড (ডিফল্ট `Vortex`) |
| `BOT_COUNTRY` | ইংরেজিতে দেশের নাম, যেমন `United States` (টাইম জোন, মুদ্রা, নামাজের সময় নির্ধারণ করে) |
| `BOT_LANGUAGE` | বটের ভাষা কোড, যেমন `en`, `fa`, `tr` (শুধু বট যা বলে তা পরিবর্তন করে) |
| `LLM_PROVIDERS` | LLM প্রোভাইডার এবং কী: `base_url\|api_key\|model`, কমা দিয়ে আলাদা |
| `UPDATE_CHECK_ENABLED` | `1` = প্রতিদিন আপডেট চেক করুন, `0` = কখনো চেক করবেন না |
| `UPDATE_REPO` | যে রিপোর রিলিজ নজর রাখা হবে (ডিফল্ট `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | ওয়েব সার্চ: `searxng` (ডিফল্ট), `tavily`, অথবা `serper` |
| `DAILY_LIMIT_MESSAGES` | প্রতি ব্যবহারকারী প্রতি দিন সর্বোচ্চ বট রিপ্লাই (ডিফল্ট `30`, বস বাদ) |

দেশ এবং ভাষা পরে হিডেন `/admin` প্যানেল থেকে (Language & Country) পরিবর্তন করা যায়, কোনো ফাইল এডিট ছাড়া।

## ডকার বিকল্প

যদি আপনি ইনস্টলারের চেয়ে ডকার পছন্দ করেন:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

এটি একটি স্ব-হোস্ট করা SearXNG সার্চ ইঞ্জিনের সাথে বট শুরু করে। লগ চেক করুন `docker compose logs -f bot` কমান্ড দিয়ে।

নোট: স্বয়ংক্রিয় সেলফ-আপডেটার সিস্টেমডি সার্ভিসের প্রয়োজন, তাই ডকারে আপডেট ম্যানুয়াল: `git pull` এবং তারপর আবার `docker compose up -d --build`।

## বিস্তারিত বৈশিষ্ট্য

### /admin প্যানেল

একটি ব্যক্তিগত চ্যাটে `/admin` পাঠান (শুধু বসের জন্য — অন্য কেউ এটি খুলতে পারবে না, এবং এটি `/help` বা মেনুতে কখনো দেখাবে না)। এতে রয়েছে:

- 🔑 **Tokens & model** — LLM কী যোগ বা সরান, কোন কীগুলো সুস্থ তা দেখুন, সক্রিয় মডেল বেছে নিন, একটি প্রদানকারীর লাইভ মডেল তালিকা ব্রাউজ করুন
- 👥 **Users** — ব্যবহারকারীর সংখ্যা, ব্যান / আনব্যান, অনুমতিপ্রাপ্ত তালিকা
- 📊 **Stats** — ব্যবহারের সংখ্যা
- 💬 **Recent chats** — লোকেরা বটকে কী বলেছে (শুধু বসের জন্য, ব্যক্তিগত)
- 🖼️ **ছবি মডেল** — আপনার নিজস্ব ছবি সার্ভিস (বেস URL + API কী + মডেল), অথবা বন্ধ
- 🛡️ **Managers** — বিশ্বস্ত লোকদের প্যানেলের অংশগুলোর অ্যাক্সেস দিন
- 🟢/🔴 **Power** — সবার জন্য বট অন বা অফ করুন (বস নিয়ন্ত্রণে থাকেন)
- 🌍 **Language & Country** — যেকোনো সময় বটের ভাষা বা দেশ পরিবর্তন করুন

### টোকেন পুল

বট একসাথে একাধিক LLM প্রদানকারীর কী ধরে রাখতে পারে। এটি সুস্থ কীগুলোর মধ্যে ঘুরে বেড়ায় এবং একটি কাজ করা বন্ধ করলে স্বয়ংক্রিয়ভাবে অন্যটিতে চলে যায়। `/admin` থেকে আপনি একটি মডেল পিন করতে পারেন, হাতের মত করে একটি মডেল বেছে নিতে পারেন, বা বটকে স্বতন্ত্রভাবে ঘুরতে দিতে পারেন। OpenAI-সামঞ্জস্যপূর্ণ API যেকোনো প্রদানকারীর কাজ করবে — ছোট এগরিগেটররা সহ, শুধু বড় নামগুলো নয়।

### ছবি

ছবি তৈরি আপনার নিজস্ব OpenAI-সামঞ্জস্যপূর্ণ ছবি সার্ভিস ব্যবহার করে: এর বেস URL, API কী এবং মডেল `/admin`-এ যোগ করুন (🖼️ Image model)। কোনো বিল্ট-ইন ছবি প্রোভাইডার নেই, এবং ফটো এডিটিং সমর্থিত নয়। ছবি তৈরি `/admin`-থেকে বন্ধ করা যাবে।

### দেশ এবং ভাষা

Vortex **১৯৫টি দেশ** এবং **৪০টি ভাষা** সমর্থন করে। দেশটি টাইম জোন, দাম দেখানোর মুদ্রা, নামাজের সময়ের জন্য ব্যবহৃত শহর, এবং স্থানীয় কন্টেন্ট নির্ধারণ করে। ভাষা শুধু বট কী বলবে তা নির্ধারণ করে — উদাহরণস্বরূপ, বেলজিয়ামের একটি গ্রুপ দেশ Belgium এবং ভাষা English ব্যবহার করতে পারে। উভয়টিই পরে `/admin` থেকে পরিবর্তন করা যাবে।

### আপডেট

বট `VortexLabsHQ/vortex-telegram-bot`-এর GitHub রিলিজগুলো দিনে একবার চেক করে। নতুন ভার্সন আসলে, এটি বসকে ব্যক্তিগতভাবে ✅ / ❌ বাটন সহ মেসেজ পাঠায়। গ্রহণ করলে কোড আপডেট হয় এবং বট রিস্টার্ট হয়। যতক্ষণ রিপো প্রাইভেট থাকে, চেকটি শান্তভাবে কিছুই করে না (GitHub-এর API পাবলিক রিপো চায়) — আপনি যদি কখনো চেক চান না তবে `UPDATE_CHECK_ENABLED=0` সেট করুন।

## সমস্যা সমাধান / FAQ

**ইনস্টলার বলে আমার টোকেন অবৈধ।**
টোকেনটি [@BotFather](https://t.me/BotFather) থেকে আসে। নিশ্চিত করুন যে আপনি পুরো টোকেনটি কপি করেছেন (সংখ্যা, একটি কোলন, তারপর ৩৫+ অক্ষর), কোনো অতিরিক্ত স্পেস ছাড়া। আপনি যদি বটটি মুছে দেন বা নতুন টোকেন তৈরি করেন, তবে পুরনোটি আর কাজ করবে না — নতুনটি পেস্ট করুন।

**বট আমার গ্রুপে উত্তর দেয় না।**
চেক করার চারটি বিষয়: (১) গ্রুপ প্রাইভেসি অবশ্যই অফ থাকতে হবে — [@BotFather](https://t.me/BotFather)-এ `/setprivacy` পাঠান, আপনার বটটি বেছে নিন, এবং **Disable** বেছে নিন; প্রাইভেসি অন থাকলে বটটি গ্রুপের কোনো বার্তা দেখতে পাবে না, (২) বটটি গ্রুপে যোগ করা থাকতে হবে, (৩) আপনাকে এর ওয়েক ওয়ার্ড বলতে হবে — এর নাম, উদাহরণস্বরূপ `Vortex what's the time?` — বটটি শুধু তখন শুনে যখন গ্রুপে এর নাম বলা হয়, (৪) প্রাইভেট চ্যাটে কোনো ওয়েক ওয়ার্ড দরকার নেই।

**বট ইংরেজিতে উত্তর দেয়, আমার ভাষায় নয়।**
`/admin` পাঠান (শুধু বস) → Language & Country, এবং আপনার ভাষা বেছে নিন। ইনস্টলারও ভাষা জিজ্ঞাসা করে — সেখানে Enter চাপিয়ে আপনার দেশের ডিফল্টটি গ্রহণ করুন।

**আমি Anthropic বেছে নিলাম কিন্তু বট চ্যাট করছে না।**
Anthropic-এর নেটিভ API OpenAI-সঙ্গে কম্প্যাটিবল নয়, তাই বটটি সরাসরি এর সাথে চ্যাট করতে পারে না। OpenRouter ব্যবহার করুন (যেটি Claude মডেলগুলো OpenAI-সঙ্গে কম্প্যাটিবল API-এর মাধ্যমে সার্ভ করতে পারে), অথবা তালিকা থেকে অন্য কোনো প্রোভাইডার বেছে নিন।

**ওয়েব সার্চ কাজ করছে না।**
ওয়েব সার্চের জন্য SearXNG দরকার, যা ইনস্টলার Docker-এ সেট আপ করার অফার দেয়। এটি ছাড়া বট Wikipedia-এ ফিরে যায়, যা দুর্বল। আপনি `.env`-এ `SEARCH_API_KEY` সহ `SEARCH_PROVIDER=tavily` বা `serper` সেট করতে পারেন।

**লগগুলো কোথায়?**
`journalctl -u vortex-bot -f` লাইভ লগ দেখায়। `systemctl status vortex-bot` সার্ভিস চলছে কিনা তা দেখায়। বট বন্ধ হলে, `sudo systemctl restart vortex-bot` দিয়ে আবার চালু করুন।

**বট বলে আমি দৈনিক লিমিট পেয়েছি।**
প্রতিটি ইউজার দিনে ৩০টি বট উত্তর পায় (বস বাদ)। লিমিটটি বটের দেশের টাইমজোন অনুযায়ী রাত ১২-টার পর রিসেট হয়। `.env`-এ `DAILY_LIMIT_MESSAGES` দিয়ে বাড়ান, অথবা বসকে বলুন।

**আমি একটি বাগ পেলাম / আমার একটি আইডিয়া আছে।**
অনুগ্রহ করে GitHub-এ একটি ইস্যু খুলুন — কীভাবে রিপোর্ট করবেন এবং ফিক্স পাঠাবেন সেটি জানতে [CONTRIBUTING.md](CONTRIBUTING.md) দেখুন।

## উন্নয়ন

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

টেস্টগুলো চালান (সাদা পাইথন স্ক্রিপ্ট, pytest দরকার নেই):

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

পুল রিকোয়েস্ট খোলার আগে নয়টি স্যুট পাস করতে হবে। কোড স্টাইল (ruff) এবং PR প্রক্রিয়ার জন্য [CONTRIBUTING.md](CONTRIBUTING.md) দেখুন।

## লাইসেন্স

Vortex [MIT লাইসেন্স](LICENSE) এর অধীনে প্রকাশিত — যেকোনো উদ্দেশ্যে ব্যবহার, কপি, পরিবর্তন এবং শেয়ার করার জন্য মুক্ত।

<a id="countries"></a>

## দেশসমূহ

ইনস্টলার আপনার দেশ জিজ্ঞাসা করলে, এখানে লেখা অনুযায়ী **ইংরেজিতে সঠিকভাবে** দেশের নাম পেস্ট করুন। টেবিলটি `bot/countries.py` থেকে তৈরি হয়েছে — যদি এখান এবং সেখানকার নাম মিলে না যায়, তবে `bot/countries.py` কেই সঠিক মানা হবে।

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

## ধন্যবাদ

> ⭐ **এই প্রজেক্টকে GitHub-এ স্টার দিন এবং [@VortexLabsHQ](https://github.com/VortexLabsHQ)-কে ফলো করুন** — এটি Vortexকে সমর্থন করার এবং অন্যদের এটি খুঁজে পেতে সাহায্য করার সবচেয়ে সহজ উপায়। ধন্যবাদ!
