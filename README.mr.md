# Vortex 🤖 — आपला स्वत:चा Telegram गट सहाय्यक

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · **मराठी** · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **जर तुम्हाला Vortex आवडल, तर कृपया GitHub वर हा प्रकल्प स्टार करा आणि [@VortexLabsHQ](https://github.com/VortexLabsHQ) ला फॉलो करा** — यामुळे अधिक लोक याला शोधू शकतात. धन्यवाद!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex काय आहे?

Vortex हा एक Telegram बॉट आहे ज्यांची राहणी तुमच्या गटांमध्ये आणि वैयक्तिक चॅटमध्ये असते आणि ते AI चॅट मॉडेलद्वारे लोकांना उत्तर देते. तुम्ही त्याचे नाव सांगता (मूळ नाव **Vortex** आहे) आणि ते उत्तर देते — ते बोलू शकते, वेब शोधू शकते, प्रतिबिंब तयार करू शकते, किंमत तपासू शकते, चुटके सांगू शकते, फाइल वाचू शकते, आवाज संदेश लिहून देऊ शकते, आणि बरेच काही.

हे तुमच्या स्वत:च्या सर्व्हरवर, तुमच्या स्वत:च्या देशात आणि भाषेत चालते. तुम्ही मालक आहात: एक गुप्त `/admin` पॅनेल तुम्हाला AI की, वापरकर्ते, आणि सेटिंग्ज व्यवस्थापित करण्यास परवानगी देते.

## वैशिष्ट्ये

- 💬 **AI चॅट** गटांमध्ये (वेक वर्ड) आणि वैयक्तिक चॅटमध्ये (वेक वर्डची गरज नाही)
- 🔑 **टोकन पूल** — अनेक LLM प्रदाते आणि की वापरा, स्वयंचलितपणे रोटेट आणि फेलओवर करा
- 🖼️ **प्रतिमा तयार करणे आणि संपादन** — विनामूल्य (DuckAI) किंवा सशुल्क प्रदाते
- 🔍 **वेब शोध** — स्वयंचलित होस्ट केलेले SearXNG, विकिपीडिया फॉलबॅकसह
- 💰 **लाइव किंमती** — चलन, सोना, तेल आणि क्रिप्टो तुमच्या स्थानिक चलनात
- 🕌 **नमाज वेळा**, 🃏 **भविष्यवाणी**, 😄 **चुटके**, 🎲 **डायस आणि सिक्का उलटणे**
- 📎 **फाइल विश्लेषण** आणि **आवाज लिप्यंतरण**
- 📥 **डाउनलोड** — लिंक पाठवा, मीडिया फाइल मिळवा (पर्यंत 45 MB)
- 🌍 **195 देशे** आणि **40 भाषा** — देश आणि भाषा वेगवेगळी सेटिंग्ज आहेत
- 🔄 **स्वयंचलित अद्ययावत** — दैनंदिन नवीन रिलीज तपासते आणि अद्ययावत करण्यापूर्वी विचारते
- 🛡️ **लपवलेले /admin पॅनेल** — टोकन, वापरकर्ते, आँकडे, चॅट्स, प्रतिमा मॉडेल, व्यवस्थापक, शक्ती

## इंस्टॉल करण्यापूर्वी

तुम्हाला **Linux** चालवणारा एक सर्व्हर (किंवा एक संगणक जे चालू आहे) हवी, ज्यामध्ये खालील गोष्टी इंस्टॉल केलेली असावीत:

| काय | कसे तपासावे | तुम्हाला काय दिसावे |
| --- | --- | --- |
| **Python 3.11 किंवा नवीन** | `python3 --version` | `Python 3.11.x` किंवा उच्च (3.12 आणि 3.13ही कार्य करतात) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` किंवा `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` किंवा समतुल्य |
| **Docker** *(पर्यायी)* | `docker --version` | `Docker version 2x.x.x` — फक्त तेव्हा गरजेचे असते जर तुम्हाला पर्यायी SearXNG वेब शोध हवा असेल |

जर काहीच कम असेल, तर इंस्टॉलर `apt` (Debian/Ubuntu वर) वापरून तो तुमच्यासाठी इंस्टॉल करण्याची ऑफर देतो. इतर प्रणालींवर, तुमच्या पॅकेज मॅनेजरचा वापर करून तो प्रथम इंस्टॉल करा.

तुम्हाला Telegram पासून दोन गोष्टीही हवी आहेत (दोनही मोफत आहेत):

1. **बॉट टोकन** — Telegram वर [@BotFather](https://t.me/BotFather)शी बोला, `/newbot` पाठवा, आणि तो तुम्हाला देणारा टोकन कॉपी करा.
2. **तुमचा संख्यात्मक Telegram यूजर ID** — [@userinfobot](https://t.me/userinfobot)शी बोला आणि तो तुम्हाला दाखवणारा नंबर कॉपी करा. हा तुमचा "बॉस" ID आहे: फक्त हाच खाते `/admin` वापरू शकते.

## इंस्टॉल

एक कमांड. तो कॉपी करा, तुमच्या टर्मिनलमध्ये पेस्ट करा, आणि एंटर दाबा:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

इंस्टॉलर तुम्हाला क्रमाने सहा प्रश्न विचारतो:

1. **देश** — तुमच्या देशाचे इंग्रजी नाव **खालील [देश तक्ते](#countries) मध्ये सूचीबद्ध प्रमाणे** पेस्ट करा (उदाहरणार्थ `Turkey`)। देश टाइम झोन, किंमतीसाठी स्थानीय चलन, नमाज वेळा, आणि स्थानीय सामग्री सेट करतो।
2. **भाषा** — बॉट ज्या भाषेत बोलतो (उदाहरणार्थ `en`, `fa`, `tr`)। तुमच्या देशाचे डिफॉल्ट स्वीकारण्यासाठी एंटर दाबा। भाषा देशापासून वेगळी आहे: ती फक्त यथार्थात बॉट काय बोलतो याचे बदल करते, आणि तुम्ही तो नंतर `/admin` पासून बदलू शकता।
3. **बॉट टोकन** — [@BotFather](https://t.me/BotFather) पासून टोकन पेस्ट करा। इंस्टॉलर तो Telegram बरोबर थेट तपासतो।
4. **बॉस न्यूमेरिक आयडी** — [@userinfobot](https://t.me/userinfobot) पासून तुमचा Telegram यूजर आयडी।
5. **बॉटचे नाव / वेक वर्ड** — लोक गटांमध्ये बॉटशी बोलण्यासाठी जे नाव म्हणतात। कोणतीही भाषा चालेल (उदाहरणार्थ `Vortex` किंवा `ورتکس`)। डिफॉल्ट `Vortex` साठी एंटर दाबा।
6. **पहिला LLM प्रदाता** — एक निवडा: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, किंवा **कस्टम** (बेस URL पेस्ट करा)। नंतर त्या प्रदाताचे API की पेस्ट करा — इंस्टॉलर प्रदात्याची थेट मॉडेल यादी आणतो आणि तुम्ही एक मॉडेल निवडता।

नंतर इंस्टॉलर अवलंबने इंस्टॉल करतो, `.env` फाईल लिहितो, `vortex-bot` systemd सेवा तयार करतो, वेब शोधासाठी SearXNG इंस्टॉल करण्याची ऑफर देतो (Docker आवश्यक आहे), आणि बॉट सुरू करतो।

> ⚠️ **Anthropic थेट काम करत नाही.** Anthropic चे मूळ API OpenAI-संगत नाही, आणि हा बॉट फक्त OpenAI-संगत API बोलतो. जर तुम्ही Anthropic निवडल्यास, इंस्टॉलर तुम्हाला चेतावतो: की फक्त OpenAI-संगत गेटवे मार्फत काम करते. तयार OpenRouter, किंवा यादीमधील इतर प्रदाता वापरा.

## इंस्टॉल केल्यानंतर

तपासा की बॉट चालू आहे:

```bash
systemctl status vortex-bot
```

तुम्हाला `active (running)` दिसावे. लाइव लॉग पाहण्यासाठी:

```bash
journalctl -u vortex-bot -f
```

आता Telegram उघडा आणि तुमच्या बॉटशी बोला:

- `/start` पाठवा — बॉट नमस्कार करेल.
- **खाजगी चॅट**मध्ये, फक्त त्यालिखा — वेक वर्डची गरज नाही.
- **गट**मध्ये, बॉटला गटमध्ये जोडा, नंतर त्याचे नाव म्हणा, उदाहरणार्थ: `Vortex what's the time?`
- मालक म्हणून, खाजगी चॅटमध्ये `/admin` पाठवा लपवलेले अॅडमिन पॅनल उघडण्यासाठी.

**अपडेट्स स्वयंचलित आहेत.** दररोज एकदा बॉट GitHub वर नवीन रिलीज तपासते. जर उपलब्ध असेल, तर ते तुम्हाला ✅ / ❌ बटन्ससह खाजगी संदेश पाठवते. ✅ दाबा आणि ते स्वयमेव अपडेट होईल आणि पुन्हा सुरू होईल — तुम्हाला सर्व्हर स्पर्शायची कधीही गरज नाही.

## कॉन्फिगरेशन

सर्व सेटिंग्ज इंस्टॉल डायरेक्टरीमधील `.env` फाइलमध्ये आहेत. प्रत्येक पर्यायासाठी [`.env.example`](.env.example) पहा. सर्वात महत्वाचे खालीलप्रमाणे:

| सेटिंग | ते काय करते |
| --- | --- |
| `BOT_TOKEN` | तुमचा टेलीग्राम बॉट टोकन (@BotFather कडून) |
| `BOSS_ID` | तुमचा संख्यात्मक टेलीग्राम यूजर आयडी (बॉट मालक) |
| `BOT_NAME` | गटांमधील बॉटचे नाव आणि वेक वर्ड (डिफॉल्ट `Vortex`) |
| `BOT_COUNTRY` | इंग्रजीमध्ये देश, उदा. `United States` (टाइम झोन, चलन, प्रार्थना वेळ सेट करते) |
| `BOT_LANGUAGE` | बॉट भाषा कोड, उदा. `en`, `fa`, `tr` (फक्त बॉट काय बोलते हे बदलते) |
| `LLM_PROVIDERS` | LLM प्रदाते आणि की: `base_url\|api_key\|model`, कॉमाद्वारे अलग केलेले |
| `UPDATE_CHECK_ENABLED` | `1` = दररोज अपडेट तपासा, `0` = कधीही तपासू नका |
| `UPDATE_REPO` | ज्याचे रिलीज पाहिले जातात असे रेपो (डिफॉल्ट `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | वेब शोध: `searxng` (डिफॉल्ट), `tavily`, किंवा `serper` |
| `DAILY_LIMIT_MESSAGES` | प्रति यूजर प्रति दिवस सर्वाधिक बॉट उत्तर (डिफॉल्ट `30`, बॉस अपवाद) |

देश आणि भाषा नंतरही लपवलेले `/admin` पॅनल (भाषा आणि देश) पासून बदलता येतात, कोणतीही फाइल संपादित केल्याशिवाय.

## Docker पर्याय

इंस्टॉलरविरूद्ध Docker पसंद असल्यास:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

हे SearXNG शोध इंजिनसह बॉट सुरू करते. `docker compose logs -f bot` सह लॉग्स तपासा.

नोट: स्वयंचलित सेल्फ-अपडेटरला systemd सेवा आवश्यक आहे, म्हणून Dockerमध्ये अपडेट्स मॅन्युअल आहेत: `git pull` आणि नंतर पुन्हा `docker compose up -d --build`.

## तपशीलवार वैशिष्ट्ये

### /admin पॅनेल

खाजगी चॅटमध्ये `/admin` पाठवा (फक्त बॉससाठी — इतर कोणीही याचे उघडू शकत नाही, आणि याचे `/help` किंवा मेनूमध्ये कधीच दर्शन होत नाही). यात खालील आहे:

- 🔑 **टोकन्स आणि मॉडेल** — LLM की जोडा/काढा, कोणती की निरोगी आहेत ते पहा, सक्रिय मॉडेल निवडा, प्रदात्याची थेट मॉडेल यादी ब्राउझ करा
- 👥 **वापरकर्ते** — वापरकर्ता संख्या, प्रतिबंध/प्रतिबंध काढा, परवानगीसूची
- 📊 **आंकडे** — वापर संख्या
- 💬 **अलीकडील चॅट्स** — लोकांनी बॉटला काय सांगितले (फक्त बॉससाठी, खाजगी)
- 🖼️ **प्रतिबिंब मॉडेल** — DuckAI (मुक्त, मूळ), HiLinkUp, कस्टम प्रतिबिंब सेवा, किंवा बंद
- 🛡️ **व्यवस्थापक** — विश्वासार्ह लोकांना पॅनेलचे भाग प्रवेश द्या
- 🟢/🔴 **शक्ती** — सर्वांसाठी बॉट चालू/बंद करा (बॉस नियंत्रणात राहतो)
- 🌍 **भाषा आणि देश** — बॉटची भाषा किंवा देश कधीही बदला

### टोकन पूल

बॉट एकाच वेळी अनेक LLM प्रदात्यांकडून की धरू शकतो. ते निरोगी कीमध्ये फिरते आणि एक बंद झाल्यावर स्वयंचलितपणे दुसऱ्यावर जातो. `/admin` पासून तुम्ही एक मॉडेल फिक्स करू शकता, हाताने मॉडेल निवडू शकता, किंवा बॉटला मुक्तपणे फिरवू शकता. OpenAI-संगत API असलेला कोणताही प्रदाता कार्य करते — लहान एग्रीगेटर्सही, फक्त मोठ्या नावांशिवाय.

### प्रतिबिंबे

प्रतिबिंब निर्माणाचे तीन मोड आहेत: **DuckAI** (मुक्त, की नाही, मूळ), **HiLinkUp** (सशुल्क, चांगली गुणवत्ता), किंवा तुमची स्वत:ची **कस्टम** OpenAI-संगत प्रतिबिंब सेवा. तुम्ही बॉटला फोटो पाठवून ते कसे संपादित करायचे ("हे कार्टून शैलीमध्ये करा") सांगू शकता, आणि ते नवीन प्रतिबिंब तयार करेल. प्रतिबिंब निर्माण `/admin` पासून बंद करता येते.

### देशे आणि भाषां

Vortex **१९५ देशे** आणि **४० भाषां** समर्थन करते. देश काळमापन, चलन ज्यामध्ये किंमत दाखवली जाते, नमाज वेळासाठी वापरलेला शहर, आणि स्थानिक सामग्री निश्चित करते. भाषा फक्त बॉट काय बोलते हे निश्चित करते — उदाहरणार्थ, बेल्जियममधील गट देश बेल्जियम आणि भाषा इंग्रजी वापरू शकते. दोन्ही `/admin` पासून नंतर बदले जाऊ शकतात.

### अद्ययावत

बॉट `VortexLabsHQ/vortex-telegram-bot` चे GitHub रिलीज दररोज एकदा तपासते. नवीन आवृत्ती आल्यावर, ते बॉसला ✅ / ❌ बटन्ससह खाजगी संदेश पाठवते. मान्य केल्यावर कोड अद्ययावत होतो आणि बॉट पुनः सुरू होते. रेपो खाजगी असताना, तपासणी मौनपणे काहीही करत नाही (GitHub चे API सार्वजनिक रेपो मागते) — `UPDATE_CHECK_ENABLED=0` सेट करा जर तुम्हाला कधीच तपासणी नसेल तर.

## समस्या निवारण / FAQ

**इंस्टॉलर आपला टोकन अवैध आहे असे सांगते.**
टोकन [@BotFather](https://t.me/BotFather) यथून येतो. खात्री करा की तुम्ही संपूर्ण टोकन कॉपी केले आहे (अंक, एक कॉलन, तर ३५+ वर्ण), कोणत्याही अतिरिक्त स्पेसशिवाय. जर तुम्ही बॉट डिलीट केले असेल किंवा नवीन टोकन तयार केले असेल, तर जुना कार्यत राहत नाही — नवीन टोकन पेस्ट करा.

**बॉट माझ्या गटात उत्तर देत नाही.**
तपासण्यासाठी तीन गोष्टी: (१) बॉट गटात जोडलेले असावे, (२) तुम्ही त्याचे वेक वर्ड — त्याचे नाव — सांगावे, उदाहरणार्थ `Vortex what's the time?` — बॉट गटात फक्त त्याचे नाव सांगल्यावरच ऐकते, (३) वैयक्तिक चॅटमध्ये वेक वर्डची गरज नाही.

**बॉट इंग्रजीत उत्तर देतो, माझ्या भाषेत नव्हे.**
`/admin` (फक्त बॉससाठी) → Language & Country पाठवा, आणि आपली भाषा निवडा. इंस्टॉलरही भाषा विचारतो — तेथे Enter दाबा तुमच्या देशाचे डिफॉल्ट स्वीकारण्यासाठी.

**मी Anthropic निवडले आणि बॉट बोलत नाही.**
Anthropic चे नॅसिव्ह API OpenAI-संगत नाही, म्हणून बॉट त्यासोबत थेट बोलू शकत नाही. OpenRouter वापरा (जे OpenAI-संगत API मार्फत Claude मॉडेल्स सेवा देऊ शकते), किंवा यादीमधून इतर प्रदाता निवडा.

**वेब शोध कार्यत नाही.**
वेब शोधाला SearXNG हवा, ज्याची इंस्टॉलर Docker सह सेट अप करण्याची ऑफर देतो. याशिवाय, बॉट विकिपीडियावर परत येते, ज्याची क्षमता कमी आहे. तुम्ही `.env` मध्ये `SEARCH_API_KEY` सह `SEARCH_PROVIDER=tavily` किंवा `serper` सेट करू शकता.

**लॉग्स कुठे आहेत?**
`journalctl -u vortex-bot -f` लाइव्ह लॉग दर्शवते. `systemctl status vortex-bot` सेवा चालू आहे की नाही हे दर्शवते. जर बॉट थांबले असेल, तर `sudo systemctl restart vortex-bot` याने तो पुन्हा सुरू होतो.

**बॉट सांगते की मी दैनंदिन मर्यादा पोहोचलो आहे.**
प्रत्येक वापरकर्ताला प्रति दिवस ३० बॉट उत्तर मिळतात (बॉस अपवाद आहे). मर्यादा बॉटच्या देशाच्या टाइमझोनमध्ये मध्यरात्री रीसेट होते. `.env` मध्ये `DAILY_LIMIT_MESSAGES` सह वाढवा, किंवा बॉसला विचारा.

**मला बग सापडला / माझा एक कल्पना आहे.**
कृपया GitHub वर एक इश्यू उघडा — [CONTRIBUTING.md](CONTRIBUTING.md) पहा यथे अहवाल कसे करावे आणि दुरुस्ती कसे पाठवावी.

## विकास

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

चाचणी चालवा (साधे Python स्क्रिप्ट्स, pytest ची गरज नाही):

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

सर्व नऊ सुइट्स पास झाल्यावरच पुल रिक्वेस्ट उघडा. कोड शैली (ruff) आणि PR प्रक्रिया साठी [CONTRIBUTING.md](CONTRIBUTING.md) पहा.

## परवाना

Vortex [MIT परवाना](LICENSE) अंतर्गत प्रसिद्ध केले आहे — वापरणे, कॉपी करणे, बदलणे आणि शेअर करणे यासाठी मुक्त, कोणत्याही उद्देश्यासाठी.

<a id="countries"></a>

## देशे

इंस्टॉलर आपल्याला आपले देश विचारा तेव्हा, देशाचे नाव **इंग्रॅजमध्ये, यथे लिहिलेलेप्रमाणे** पेस्ट करा. ही टेबल `bot/countries.py` पासून तयार केलेली आहे — इथे आणि तिथे नाव असहमत झाले तर, `bot/countries.py` मान्य असेल.

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

## धन्यवाद

> ⭐ **कृपया GitHub वर या प्रकल्पला स्टार द्या आणि [@VortexLabsHQ](https://github.com/VortexLabsHQ) ला फॉलो करा** — हे Vortex ला समर्थन देण्याचे आणि इतरांना याचे शोध घेण्यास मदत करणारे सर्वात सोपे मार्ग आहे. धन्यवाद!
