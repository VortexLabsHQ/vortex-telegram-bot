# Vortex 🤖 — आपका अपना टेलीग्राम ग्रुप असिस्टेंट

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · **हिन्दी** · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **अगर आपको Vortex पसंद है, तो कृपया इस प्रोजेक्ट को GitHub पर स्टार करें और [@VortexLabsHQ](https://github.com/VortexLabsHQ) को फॉलो करें** — इससे और लोगों को इसे ढूंढने में मदद मिलती है। धन्यवाद!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex क्या है?

Vortex एक Telegram बॉट है जो आपके ग्रुप्स और प्राइवेट चैट्स में रहता है और AI चैट मॉडल के साथ लोगों को जवाब देता है। आप इसका नाम बोलते हैं (डिफ़ॉल्ट नाम **Vortex** है) और यह जवाब देता है — यह चैट कर सकता है, वेब सर्च कर सकता है, इमेज बना सकता है, कीमतें चेक कर सकता है, जोक्स सुना सकता है, फाइलें पढ़ सकता है, वॉइस मैसेज ट्रांसक्राइब कर सकता है, और भी बहुत कुछ।

यह आपके अपने सर्वर पर, आपके अपने देश और भाषा में चलता है। आप बॉस हैं: एक छिपा हुआ `/admin` पैनल आपको AI कीज़, यूज़र्स और सेटिंग्स मैनेज करने देता है।

## विशेषताएं

- 💬 **AI चैट** ग्रुप में (वेक वर्ड के साथ) और प्राइवेट चैट में (वेक वर्ड की ज़रूरत नहीं)
- 🔑 **टोकन पूल** — कई LLM प्रोवाइडर और कीज़ इस्तेमाल करें, अपने आप रोटेट और फेलओवर करें
- 🖼️ **इमेज जनरेशन** — अपनी इमेज सर्विस (बेस URL + API की + मॉडल) के साथ, `/admin` में जोड़ा गया
- 🔍 **वेब सर्च** — सेल्फ-होस्टेड SearXNG, विकिपीडिया फॉलबैक के साथ
- 💰 **लाइव कीमतें** — करेंसी, सोना, तेल, और क्रिप्टो आपकी लोकल करेंसी में
- 🕌 **नमाज़ के वक़्त**, 🃏 **किस्मत**, 😄 **चुटकुले**, 🎲 **डाइस और सिक्का उछालना**
- 📎 **फाइल एनालिसिस** और **वॉयस ट्रांसक्रिप्शन**
- 📥 **डाउनलोड** — लिंक भेजें, मीडिया फ़ाइल वापस पाएं (45 MB तक)
- 🌍 **195 देश** और **40 भाषाएं** — देश और भाषा अलग-अलग सेटिंग्स हैं
- 🔄 **सेल्फ-अपडेटिंग** — रोज़ नए रिलीज़ चेक करता है और अपडेट से पहले पूछता है
- 🛡️ **छिपा हुआ /एडमिन पैनल** — टोकन, यूज़र, स्टैट्स, चैट, इमेज मॉडल, मैनेजर, पावर

## इंस्टॉल करने से पहले

आपको एक सर्वर (या ऐसा कंप्यूटर जो चालू रहता हो) चाहिए जिस पर **Linux** चल रहा हो और जिसमें ये चीज़ें इंस्टॉल हों:

| What | How to check | What you should see |
| --- | --- | --- |
| **Python 3.11 या नया** | `python3 --version` | `Python 3.11.x` या उससे ऊपर (3.12 और 3.13 भी चलेंगे) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` या `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` या वैसा ही कुछ |
| **Docker** *(वैकल्पिक)* | `docker --version` | `Docker version 2x.x.x` — सिर्फ़ तब ज़रूरी जब आप वैकल्पिक SearXNG वेब खोज चाहते हों |

अगर कुछ गायब है, तो एक कमांड से सब इंस्टॉल करें (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

वैकल्पिक `docker` के लिए (केवल तब ज़रूरी जब आप `SearXNG` वेब खोज चाहते हैं):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

आखिरी लाइन के बाद, लॉग आउट करके फिर से लॉग इन करें (या `docker` कमांड को `sudo` के साथ चलाएं)। इंस्टॉलर `apt` के ज़रिए `Debian/Ubuntu` पर आपके लिए गायब टूल्स इंस्टॉल करने का विकल्प भी देता है। अन्य सिस्टम पर, पहले अपने पैकेज मैनेजर से उन्हें इंस्टॉल करें। `systemd` सिस्टम के साथ आता है — इसे अलग से इंस्टॉल नहीं किया जा सकता।

आपको Telegram से दो चीज़ें भी चाहिए (दोनों मुफ़्त हैं):

1. **एक बॉट टोकन** — Telegram पर [@BotFather](https://t.me/BotFather) से बात करें, `/newbot` भेजें, और जो टोकन वो दे उसे कॉपी करें।
2. **आपका संख्यात्मक Telegram यूज़र आईडी** — [@userinfobot](https://t.me/userinfobot) से बात करें और जो नंबर वो दिखाए उसे कॉपी करें। ये आपका "बॉस" आईडी है: सिर्फ़ ये अकाउंट `/admin` इस्तेमाल कर सकता है।

## इंस्टॉल करें

एक कमांड। इसे कॉपी करें, अपने टर्मिनल में पेस्ट करें, और एंटर दबाएं:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

इंस्टॉलर आपसे क्रम में छह सवाल पूछता है:

1. **देश** — अपने देश का अंग्रेजी नाम **नीचे दी गई [देश तालिका](#countries) में सूचीबद्ध ठीक उसी तरह** पेस्ट करें (उदाहरण के लिए `Turkey`)। देश टाइम ज़ोन, कीमतों के लिए स्थानीय मुद्रा, नमाज़ के समय, और स्थानीय सामग्री सेट करता है।
2. **भाषा** — वह भाषा जो बॉट बोलता है (उदाहरण के लिए `en`, `fa`, `tr`)। अपने देश के लिए डिफ़ॉल्ट स्वीकार करने के लिए एंटर दबाएं। भाषा देश से अलग है: यह केवल बदलती है कि बॉट क्या कहता है, और आप इसे बाद में `/admin` से बदल सकते हैं।
3. **बॉट टोकन** — [@BotFather](https://t.me/BotFather) से टोकन पेस्ट करें। इंस्टॉलर इसे टेलीग्राम के साथ लाइव जांचता है।
4. **बॉस न्यूमेरिक आईडी** — [@userinfobot](https://t.me/userinfobot) से आपका टेलीग्राम यूज़र आईडी।
5. **बॉट का नाम / वेक वर्ड** — वह नाम जो लोग ग्रुप में बॉट से बात करने के लिए बोलते हैं। कोई भी भाषा चलेगी (उदाहरण के लिए `Vortex` या `ورتکس`)। डिफ़ॉल्ट `Vortex` के लिए एंटर दबाएं।
6. **पहला LLM प्रोवाइडर** — एक चुनें: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, या **कस्टम** (बेस URL पेस्ट करें)। फिर उस प्रोवाइडर के लिए अपना API की पेस्ट करें — इंस्टॉलर प्रोवाइडर की लाइव मॉडल सूची लाता है और आप एक मॉडल चुनते हैं।

फिर इंस्टॉलर निर्भरताएं इंस्टॉल करता है, `.env` फाइल लिखता है, `vortex-bot` systemd सेवा बनाता है, वेब खोज के लिए SearXNG इंस्टॉल करने की पेशकश करता है (Docker चाहिए), और बॉट शुरू करता है।

> ⚠️ **Anthropic सीधे काम नहीं करता।** Anthropic का नेटिव API OpenAI-संगत नहीं है, और यह बॉट केवल OpenAI-संगत API बोलता है। अगर आप Anthropic चुनते हैं, तो इंस्टॉलर आपको चेतावनी देता है: कुंजी केवल OpenAI-संगत गेटवे के माध्यम से काम करती है। इसके बजाय OpenRouter, या सूची से कोई अन्य प्रोवाइडर उपयोग करें।

## इंस्टॉल करने के बाद

जांचें कि बॉट चल रहा है:

```bash
systemctl status vortex-bot
```

आपको `active (running)` दिखना चाहिए। लाइव लॉग देखने के लिए:

```bash
journalctl -u vortex-bot -f
```

अब टेलीग्राम खोलें और अपने बॉट से बात करें:

- `/start` भेजें — बॉट हैलो बोलेगा।
- **निजी चैट** में, बस इसे लिखें — किसी वेक वर्ड की जरूरत नहीं।
- **ग्रुप** में, बॉट को ग्रुप में जोड़ें, फिर ग्रुप प्राइवेसी बंद करें: [@BotFather](https://t.me/BotFather) में `/setprivacy` भेजें, अपना बॉट चुनें, और **Disable** चुनें — अन्यथा बॉट ग्रुप संदेश नहीं देख पाएगा और उसका वेक वर्ड नहीं सुनेगा। फिर उसका नाम बोलें, उदाहरण के लिए: `Vortex what's the time?`
- बॉस के तौर पर, निजी चैट में `/admin` भेजकर छिपा हुआ एडमिन पैनल खोलें।

**अपडेट अपने आप होते हैं।** दिन में एक बार बॉट गिटहब पर नया रिलीज चेक करता है। अगर उपलब्ध हो, तो यह आपको ✅ / ❌ बटनों के साथ एक निजी संदेश भेजता है। ✅ दबाएं और यह खुद अपडेट होकर रीस्टार्ट हो जाएगा — आपको कभी सर्वर छूने की जरूरत नहीं पड़ेगी।

## कॉन्फ़िगरेशन

सभी सेटिंग्स इंस्टॉल डायरेक्टरी में `.env` फ़ाइल में रहती हैं। हर विकल्प के लिए [`.env.example`](.env.example) देखें। सबसे ज़रूरी वाले:

| Setting | यह क्या करता है |
| --- | --- |
| `BOT_TOKEN` | आपका टेलीग्राम बॉट टोकन (@BotFather से) |
| `BOSS_ID` | आपका न्यूमेरिक टेलीग्राम यूज़र आईडी (बॉट का मालिक) |
| `BOT_NAME` | बॉट का नाम और ग्रुप में वेक वर्ड (डिफ़ॉल्ट `Vortex`) |
| `BOT_COUNTRY` | देश अंग्रेज़ी में, जैसे `United States` (टाइम ज़ोन, करेंसी, प्रेयर टाइम सेट करता है) |
| `BOT_LANGUAGE` | बॉट का लैंग्वेज कोड, जैसे `en`, `fa`, `tr` (केवल बॉट जो बोलता है उसे बदलता है) |
| `LLM_PROVIDERS` | LLM प्रोवाइडर्स और कीज़: `base_url\|api_key\|model`, कॉमा से अलग |
| `UPDATE_CHECK_ENABLED` | `1` = रोज़ अपडेट चेक करें, `0` = कभी चेक न करें |
| `UPDATE_REPO` | वह रिपो जिसके रिलीज़ देखे जाते हैं (डिफ़ॉल्ट `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | वेब सर्च: `searxng` (डिफ़ॉल्ट), `tavily`, या `serper` |
| `DAILY_LIMIT_MESSAGES` | प्रति यूज़र प्रति दिन अधिकतम बॉट रिप्लाई (डिफ़ॉल्ट `30`, बॉस को छूट) |

देश और भाषा को बाद में छिपे हुए `/admin` पैनल (Language & Country) से भी बदला जा सकता है, बिना किसी फ़ाइल को एडिट किए।

## डॉकर विकल्प

यदि आप इंस्टॉलर के बजाय डॉकर पसंद करते हैं:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

यह बॉट को एक सेल्फ-होस्टेड SearXNG सर्च इंजन के साथ शुरू करता है। लॉग्स को `docker compose logs -f bot` से जांचें।

नोट: स्वचालित सेल्फ-अपडेटर को systemd सर्विस की आवश्यकता होती है, इसलिए डॉकर में अपडेट मैन्युअल हैं: `git pull` और फिर `docker compose up -d --build` फिर से।

## विस्तार में सुविधाएँ

### /admin पैनल

प्राइवेट चैट में `/admin` भेजें (केवल बॉस के लिए — कोई और इसे नहीं खोल सकता, और यह `/help` या मेन्यू में कभी नहीं दिखता)। इसमें है:

- 🔑 **टोकन और मॉडल** — LLM कीज़ जोड़ें या हटाएँ, देखें कौन सी कीज़ ठीक हैं, एक्टिव मॉडल चुनें, प्रोवाइडर की लाइव मॉडल लिस्ट देखें
- 👥 **यूज़र्स** — यूज़र गिनती, बैन/अनबैन, अलाउलिस्ट
- 📊 **स्टैट्स** — इस्तेमाल के आँकड़े
- 💬 **हाल की चैट्स** — लोगों ने बॉट से क्या कहा (केवल बॉस, प्राइवेट)
- 🖼️ **इमेज मॉडल** — अपनी इमेज सर्विस (बेस URL + API की + मॉडल), या बंद
- 🛡️ **मैनेजर्स** — भरोसेमंद लोगों को पैनल के हिस्सों का एक्सेस दें
- 🟢/🔴 **पावर** — सबके लिए बॉट चालू या बंद करें (बॉस का कंट्रोल रहता है)
- 🌍 **भाषा और देश** — बॉट की भाषा या देश कभी भी बदलें

### टोकन पूल

बॉट एक साथ कई LLM प्रोवाइडर्स की कीज़ रख सकता है। यह ठीक कीज़ के बीच रोटेट करता है और जब कोई काम करना बंद कर दे तो अपने आप दूसरी पर चला जाता है। `/admin` से आप एक मॉडल पिन कर सकते हैं, हाथ से मॉडल चुन सकते हैं, या बॉट को आज़ादी से रोटेट करने दे सकते हैं। OpenAI-कम्पैटिबल API वाला कोई भी प्रोवाइडर काम करता है — छोटे एग्रीगेटर्स भी, सिर्फ़ बड़े नाम नहीं।

### इमेजेस

इमेज जनरेशन आपकी अपनी OpenAI-कम्पैटिबल इमेज सर्विस का उपयोग करती है: इसका बेस URL, API की और मॉडल `/admin` (🖼️ इमेज मॉडल) में जोड़ें। कोई अंतर्निहित इमेज प्रोवाइडर नहीं है, और फोटो एडिटिंग समर्थित नहीं है। इमेज जनरेशन को `/admin` से बंद किया जा सकता है।

### देश और भाषाएँ

Vortex **195 देशों** और **40 भाषाओं** को सपोर्ट करता है। देश टाइम ज़ोन सेट करता है, वह करेंसी जिसमें कीमतें दिखाई जाती हैं, प्रेयर टाइम्स के लिए इस्तेमाल होने वाला शहर, और लोकल कंटेंट। भाषा सिर्फ़ यह तय करती है कि बॉट क्या कहता है — उदाहरण के लिए, बेल्जियम में एक ग्रुप देश बेल्जियम और भाषा अंग्रेज़ी इस्तेमाल कर सकता है। दोनों को बाद में `/admin` से बदला जा सकता है।

### अपडेट्स

बॉट दिन में एक बार `VortexLabsHQ/vortex-telegram-bot` के GitHub रिलीज़ चेक करता है। जब नया वर्जन आता है, तो यह बॉस को प्राइवेट मैसेज करता है ✅ / ❌ बटन्स के साथ। स्वीकार करने पर कोड अपडेट होता है और बॉट रीस्टार्ट होता है। जब तक रेपो प्राइवेट है, चेक चुपचाप कुछ नहीं करता (GitHub के API को पब्लिक रेपो चाहिए) — अगर आप कभी चेक नहीं चाहते तो `UPDATE_CHECK_ENABLED=0` सेट करें।

## समस्या निवारण / अक्सर पूछे जाने वाले प्रश्न

**इंस्टॉलर कहता है कि मेरा टोकन अमान्य है।**
टोकन [@BotFather](https://t.me/BotFather) से आता है। सुनिश्चित करें कि आपने पूरा टोकन कॉपी किया है (अंक, एक कोलन, फिर 35+ वर्ण), बिना किसी अतिरिक्त स्पेस के। अगर आपने बॉट डिलीट कर दिया या नया टोकन बनाया, तो पुराना काम करना बंद कर देता है — नया वाला पेस्ट करें।

**बॉट मेरे ग्रुप में जवाब नहीं देता।**
जाँचने योग्य चार बातें: (१) ग्रुप प्राइवेसी बंद होनी चाहिए — [@BotFather](https://t.me/BotFather) में `/setprivacy` भेजें, अपना बॉट चुनें, और **Disable** चुनें; प्राइवेसी चालू होने पर बॉट ग्रुप संदेश बिल्कुल नहीं देख पाता, (२) बॉट को ग्रुप में जोड़ा गया हो, (३) आपको उसका वेक वर्ड बोलना होगा — उसका नाम, उदाहरण के लिए `Vortex what's the time?` — बॉट केवल तब सुनता है जब ग्रुप में उसका नाम बोला जाए, (४) निजी चैट में किसी वेक वर्ड की आवश्यकता नहीं होती।

**बॉट अंग्रेज़ी में जवाब देता है, मेरी भाषा में नहीं।**
`/admin` भेजें (केवल बॉस के लिए) → Language & Country, और अपनी भाषा चुनें। इंस्टॉलर भी भाषा पूछता है — वहाँ Enter दबाकर अपने देश की डिफ़ॉल्ट भाषा स्वीकार करें।

**मैंने Anthropic चुना और बॉट चैट नहीं करता।**
Anthropic का नेटिव API OpenAI-संगत नहीं है, इसलिए बॉट सीधे उससे चैट नहीं कर सकता। OpenRouter का उपयोग करें (जो OpenAI-संगत API के ज़रिए Claude मॉडल सर्व कर सकता है), या सूची से कोई दूसरा प्रोवाइडर चुनें।

**वेब खोज काम नहीं करती।**
वेब खोज को SearXNG की ज़रूरत होती है, जिसे इंस्टॉलर Docker के साथ सेटअप करने का विकल्प देता है। इसके बिना, बॉट Wikipedia पर चला जाता है, जो कमज़ोर है। आप `.env` में `SEARCH_API_KEY` के साथ `SEARCH_PROVIDER=tavily` या `serper` भी सेट कर सकते हैं।

**लॉग कहाँ हैं?**
`journalctl -u vortex-bot -f` लाइव लॉग दिखाता है। `systemctl status vortex-bot` दिखाता है कि सर्विस चल रही है या नहीं। अगर बॉट रुक जाए, तो `sudo systemctl restart vortex-bot` से फिर से शुरू करें।

**बॉट कहता है कि मैं दैनिक सीमा पर पहुँच गया हूँ।**
हर यूज़र को रोज़ 30 बॉट जवाब मिलते हैं (बॉस को छूट है)। सीमा बॉट के देश के टाइम ज़ोन में आधी रात को रीसेट होती है। `.env` में `DAILY_LIMIT_MESSAGES` से बढ़ाएँ, या बॉस से पूछें।

**मुझे बग मिला / मेरे पास एक आइडिया है।**
कृपया GitHub पर इश्यू खोलें — रिपोर्ट करने और फिक्स भेजने का तरीका [CONTRIBUTING.md](CONTRIBUTING.md) में देखें।

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

टेस्ट चलाएँ (साधारण Python स्क्रिप्ट, pytest की ज़रूरत नहीं):

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

पुल रिक्वेस्ट खोलने से पहले सभी नौ सुइट्स पास होने चाहिए। कोड स्टाइल (ruff) और PR प्रक्रिया के लिए [CONTRIBUTING.md](CONTRIBUTING.md) देखें।

## लाइसेंस

Vortex को [MIT License](LICENSE) के तहत जारी किया गया है — किसी भी उद्देश्य के लिए उपयोग करने, कॉपी करने, बदलने और साझा करने के लिए मुफ़्त।

<a id="countries"></a>

## देश

जब इंस्टॉलर आपका देश पूछे, तो देश का नाम **अंग्रेज़ी में, ठीक यहाँ लिखे अनुसार** पेस्ट करें। यह तालिका `bot/countries.py` से जनरेट होती है — अगर यहाँ कोई नाम और वहाँ कोई नाम कभी मेल न खाए, तो `bot/countries.py` ही मान्य होगा।

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

> ⭐ **कृपया GitHub पर इस प्रोजेक्ट को स्टार करें और [@VortexLabsHQ](https://github.com/VortexLabsHQ) को फॉलो करें** — यह Vortex को सपोर्ट करने और दूसरों को इसे खोजने में मदद करने का सबसे आसान तरीका है। धन्यवाद!
