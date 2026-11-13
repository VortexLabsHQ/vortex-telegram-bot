# Vortex 🤖 — העוזר האישי שלך לקבוצות טלגרם

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · **עברית** · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **אם אהבתם את Vortex, בבקשה תנו כוכב לפרויקט ב-GitHub ועקבו אחרי [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — זה עוזר לעוד אנשים למצוא אותו. תודה!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## מה זה Vortex?

Vortex הוא בוט טלגרם שחי בקבוצות ובצ'אטים הפרטיים שלכם ועונה לאנשים עם מודל צ'אט AI. אתם אומרים את שמו (שם ברירת המחדל הוא **Vortex**) והוא עונה — הוא יכול לשוחח, לחפש ברשת, ליצור תמונות, לבדוק מחירים, לספר בדיחות, לקרוא קבצים, לתמלל הודעות קוליות, ועוד.

הוא רץ על השרת שלכם, במדינה ובשפה שלכם. אתם הבוס: פאנל `/admin` נסתר מאפשר לכם לנהל מפתחות AI, משתמשים והגדרות.

## תכונות

- 💬 **צ'אט AI** בקבוצות (מילת השכמה) ובצ'אטים פרטיים (אין צורך במילת השכמה)
- 🔑 **מאגר טוקנים** — השתמשו בכמה ספקי LLM ומפתחות, סיבוב ומעבר אוטומטי במקרה כשל
- 🖼️ **יצירת תמונות** — עם שירות תמונה משלך (כתובת בסיס + מפתח API + מודל), נוסף ב-`/admin`
- 🔍 **חיפוש ברשת** — SearXNG באירוח עצמי, עם גיבוי של ויקיפדיה
- 💰 **מחירים חיים** — מטבעות, זהב, נפט וקריפטו במטבע המקומי שלכם
- 🕌 **זמני תפילה**, 🃏 **מזלות**, 😄 **בדיחות**, 🎲 **קוביות והטלת מטבע**
- 📎 **ניתוח קבצים** ו**תמלול קולי**
- 📥 **הורדות** — שלחו קישור, קבלו את קובץ המדיה בחזרה (עד 45 מגה)
- 🌍 **195 מדינות** ו**40 שפות** — מדינה ושפה הן הגדרות נפרדות
- 🔄 **עדכון עצמי** — בודק גרסאות חדשות מדי יום ושואל לפני עדכון
- 🛡️ **פאנל /admin נסתר** — טוקנים, משתמשים, סטטיסטיקות, צ'אטים, מודל תמונה, מנהלים, כוח

## לפני ההתקנה

אתם צריכים שרת (או מחשב שנשאר דולק) שרץ **Linux** עם הדברים הבאים מותקנים:

| מה | איך לבדוק | מה אתם אמורים לראות |
| --- | --- | --- |
| **Python 3.11 ומעלה** | `python3 --version` | `Python 3.11.x` ומעלה (3.12 ו-3.13 עובדים גם) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` או `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` או דומה |
| **Docker** *(אופציונלי)* | `docker --version` | `Docker version 2x.x.x` — נדרש רק אם אתם רוצים את חיפוש הרשת האופציונלי SearXNG |

אם משהו חסר, התקן הכול בפקודה אחת (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

עבור Docker האופציונלי (נדרש רק אם אתה רוצה חיפוש אינטרנט של SearXNG):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

לאחר השורה האחרונה, התנתק והיכנס שוב (או הרץ פקודות `docker` עם `sudo`). המתקין גם מציע להתקין עבורך כלים חסרים עם `apt` ב‑Debian/Ubuntu. במערכות אחרות, התקן אותם תחילה עם מנהל החבילות שלך. `systemd` מגיע עם המערכת — לא ניתן להתקין אותו בנפרד.

אתם גם צריכים שני דברים מטלגרם (שניהם בחינם):

1. **טוקן בוט** — דברו עם [@BotFather](https://t.me/BotFather) בטלגרם, שלחו `/newbot`, והעתיקו את הטוקן שהוא נותן לכם.
2. **מזהה המשתמש המספרי שלכם בטלגרם** — דברו עם [@userinfobot](https://t.me/userinfobot) והעתיקו את המספר שהוא מראה לכם. זהו המזהה "בוס" שלכם: רק החשבון הזה יכול להשתמש ב-`/admin`.

## התקנה

פקודה אחת. העתיקו אותה, הדביקו בטרמינל, ולחצו Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

המתקין ישאל אתכם שש שאלות, לפי הסדר:

1. **מדינה** — הדבק את השם האנגלי של המדינה שלך **בדיוק כפי שמופיע ב[טבלת המדינות](#countries) למטה** (למשל `Turkey`). המדינה קובעת את אזור הזמן, המטבע המקומי למחירים, זמני תפילה ותוכן מקומי.
2. **שפה** — השפה שהבוט מדבר בה (למשל `en`, `fa`, `tr`). לחץ Enter כדי לקבל את ברירת המחדל למדינה שלך. שפה נפרדת ממדינה: היא משנה רק מה הבוט אומר, ואפשר לשנות אותה אחר כך מ־`/admin`.
3. **טוקן בוט** — הדבק את הטוקן מ־[@BotFather](https://t.me/BotFather). המתקין בודק אותו בזמן אמת מול טלגרם.
4. **מזהה מספרי של הבוס** — מזהה המשתמש שלך בטלגרם מ־[@userinfobot](https://t.me/userinfobot).
5. **שם בוט / מילת השכמה** — השם שאנשים אומרים בקבוצות כדי לדבר עם הבוט. כל שפה מתקבלת (למשל `Vortex` או `ورتکس`). לחץ Enter לברירת המחדל `Vortex`.
6. **ספק LLM ראשון** — בחר אחד: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, או **Custom** (הדבק כתובת בסיס). אחר כך הדבק את מפתח ה־API של אותו ספק — המתקין שולף את רשימת המודלים החיה של הספק ואתה בוחר מודל.

אז המתקין מתקין את התלויות, כותב את קובץ `.env`, יוצר את שירות systemd `vortex-bot`, מציע להתקין SearXNG לחיפוש ברשת (דורש Docker), ומפעיל את הבוט.

> ⚠️ **Anthropic לא עובד ישירות.** ה־API המקורי של Anthropic אינו תואם OpenAI, והבוט הזה מדבר רק API־ים תואמי OpenAI. אם תבחר Anthropic, המתקין יזהיר אותך: המפתח יעבוד רק דרך שער תואם OpenAI. השתמש ב־OpenRouter, או בספק אחר מהרשימה, במקום.

## אחרי ההתקנה

בדוק שהבוט רץ:

```bash
systemctl status vortex-bot
```

אתה אמור לראות `active (running)`. כדי לצפות ביומן החי:

```bash
journalctl -u vortex-bot -f
```

עכשיו פתח טלגרם ודבר עם הבוט שלך:

- שלח `/start` — הבוט אומר שלום.
- ב**צ'אט פרטי**, פשוט כתוב לו — אין צורך במילת השכמה.
- ב**קבוצה**, הוסף את הבוט לקבוצה, ואז כבה את פרטיות הקבוצה: ב-[@BotFather](https://t.me/BotFather) שלח `/setprivacy`, בחר את הבוט שלך, ובחר **Disable** — אחרת הבוט לא יכול לראות הודעות בקבוצה ולא ישמע את מילת ההפעלה. ואז אמור את שמו, למשל: `Vortex what's the time?`
- כבוס, שלח `/admin` בצ'אט פרטי כדי לפתוח את פאנל הניהול הנסתר.

**עדכונים הם אוטומטיים.** פעם ביום הבוט בודק בגיטהאב אם יש גרסה חדשה. אם יש, הוא שולח לך הודעה פרטית עם כפתורי ✅ / ❌. לחץ ✅ והוא מעדכן את עצמו ומפעיל מחדש — לעולם לא תצטרך לגעת בשרת.

## הגדרה

כל ההגדרות נמצאות בקובץ `.env` בספריית ההתקנה. ראה [`.env.example`](.env.example) לכל האפשרויות. החשובות ביותר:

| הגדרה | מה היא עושה |
| --- | --- |
| `BOT_TOKEN` | הטוקן של הבוט בטלגרם (מ-@BotFather) |
| `BOSS_ID` | מזהה המשתמש המספרי שלך בטלגרם (בעל הבוט) |
| `BOT_NAME` | שם הבוט ומילת ההפעלה בקבוצות (ברירת מחדל `Vortex`) |
| `BOT_COUNTRY` | מדינה באנגלית, למשל `United States` (קובע אזור זמן, מטבע, זמני תפילה) |
| `BOT_LANGUAGE` | קוד שפה של הבוט, למשל `en`, `fa`, `tr` (משנה רק מה הבוט אומר) |
| `LLM_PROVIDERS` | ספקי LLM ומפתחות: `base_url\|api_key\|model`, מופרדים בפסיקים |
| `UPDATE_CHECK_ENABLED` | `1` = בדיקת עדכונים יומית, `0` = לעולם לא בודק |
| `UPDATE_REPO` | המאגר שעדכוניו נצפים (ברירת מחדל `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | חיפוש ברשת: `searxng` (ברירת מחדל), `tavily`, או `serper` |
| `DAILY_LIMIT_MESSAGES` | מקסימום תשובות בוט למשתמש ליום (ברירת מחדל `30`, הבוס פטור) |

מדינה ושפה ניתנות לשינוי גם בהמשך מהפאנל הנסתר `/admin` (שפה ומדינה), בלי לערוך אף קובץ.

## חלופת Docker

אם אתם מעדיפים Docker על פני המתקין:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

זה מפעיל את הבוט יחד עם מנוע חיפוש SearXNG שמארחים עצמאית. בודקים את הלוגים עם `docker compose logs -f bot`.

הערה: המעדכן האוטומטי זקוק לשירות systemd, לכן ב-Docker עדכונים הם ידניים: `git pull` ואז שוב `docker compose up -d --build`.

## תכונות בפירוט

### פאנל ה-/admin

שלחו `/admin` בצ'אט פרטי (רק הבוס — אף אחד אחר לא יכול לפתוח אותו, והוא לעולם לא מופיע ב-/help או בתפריטים). יש בו:

- 🔑 **טוקנים ומודל** — הוספה או הסרה של מפתחות LLM, רואים אילו מפתחות תקינים, בוחרים את המודל הפעיל, גולשים ברשימת המודלים החיה של ספק
- 👥 **משתמשים** — ספירת משתמשים, חסימה / ביטול חסימה, רשימת היתר
- 📊 **סטטיסטיקות** — מספרי שימוש
- 💬 **צ'אטים אחרונים** — מה אנשים אמרו לבוט (רק הבוס, פרטי)
- 🖼️ **מודל תמונה** — שירות תמונה משלך (כתובת בסיס + מפתח API + מודל), או כבוי
- 🛡️ **מנהלים** — נותנים לאנשים מהימנים גישה לחלקים מהפאנל
- 🟢/🔴 **כוח** — מפעילים או מכבים את הבוט לכולם (הבוס נשאר בשליטה)
- 🌍 **שפה ומדינה** — משנים את שפת הבוט או המדינה בכל עת

### מאגר הטוקנים

הבוט יכול להחזיק מפתחות מכמה ספקי LLM בו-זמנית. הוא מסתובב בין מפתחות תקינים ומבצע מעבר אוטומטי כשאחד מפסיק לעבוד. מ-/admin אפשר להצמיד מודל אחד, לבחור מודל ידנית, או לתת לבוט להסתובב בחופשיות. כל ספק עם API תואם OpenAI עובד — כולל מאגדים קטנים, לא רק השמות הגדולים.

### תמונות

יצירת תמונות משתמשת בשירות תמונה תואם OpenAI משלך: הוסף את כתובת הבסיס, מפתח ה-API והמודל ב-`/admin` (🖼️ מודל תמונה). אין ספק תמונה מובנה, ועריכת תמונות אינה נתמכת. ניתן לכבות יצירת תמונות מ-`/admin`.

### מדינות ושפות

Vortex תומך ב-**195 מדינות** ו-**40 שפות**. המדינה קובעת את אזור הזמן, את המטבע שבו מוצגים המחירים, את העיר המשמשת לזמני תפילה, ואת התוכן המקומי. השפה קובעת רק מה הבוט אומר — קבוצה בבלגיה יכולה להשתמש במדינה בלגיה ובשפה אנגלית, למשל. את שניהם אפשר לשנות אחר כך דרך `/admin`.

### עדכונים

הבוט בודק את הגרסאות ב-GitHub של `VortexLabsHQ/vortex-telegram-bot` פעם ביום. כשיוצאת גרסה חדשה, הוא שולח לבוס הודעה פרטית עם כפתורי ✅ / ❌. אישור מעדכן את הקוד ומפעיל מחדש את הבוט. כל עוד המאגר פרטי, הבדיקה לא עושה דבר בשקט (ה-API של GitHub דורש מאגר ציבורי) — הגדר `UPDATE_CHECK_ENABLED=0` אם לעולם אינך רוצה את הבדיקה.

## פתרון בעיות / שאלות נפוצות

**המתקין אומר שהטוקן שלי לא תקין.**
הטוקן מגיע מ-[@BotFather](https://t.me/BotFather). ודא שהעתקת את כל הטוקן (ספרות, נקודתיים, ואז 35+ תווים), בלי רווחים מיותרים. אם מחקת את הבוט או יצרת טוקן חדש, הישן מפסיק לעבוד — הדבק את החדש.

**הבוט לא עונה בקבוצה שלי.**
ארבעה דברים לבדוק: (1) פרטיות הקבוצה חייבת להיות כבויה — ב-[@BotFather](https://t.me/BotFather) שלח `/setprivacy`, בחר את הבוט שלך, ובחר **Disable**; כשהפרטיות מופעלת, הבוט לא יכול לראות הודעות בקבוצה בכלל, (2) הבוט חייב להיות נוסף לקבוצה, (3) עליך לומר את מילת ההפעלה שלו — שמו, למשל `Vortex what's the time?` — הבוט מקשיב רק כששמו נאמר בקבוצות, (4) בצ'אט פרטי אין צורך במילת הפעלה כלל.

**הבוט עונה באנגלית, לא בשפה שלי.**
שלח `/admin` (רק לבוס) → שפה ומדינה, ובחר את השפה שלך. המתקין גם שואל על השפה — לחץ Enter שם כדי לקבל את ברירת המחדל של המדינה שלך.

**בחרתי Anthropic והבוט לא מצ'וטט.**
ה-API המקורי של Anthropic אינו תואם OpenAI, לכן הבוט לא יכול לצ'וטט איתו ישירות. השתמש ב-OpenRouter (שיכול להגיש מודלי Claude דרך API תואם OpenAI), או בחר ספק אחר מהרשימה.

**חיפוש באינטרנט לא עובד.**
חיפוש באינטרנט צריך SearXNG, שהמתקין מציע להגדיר עם Docker. בלעדיו, הבוט נופל חזרה לוויקיפדיה, שהיא חלשה יותר. אפשר גם להגדיר `SEARCH_PROVIDER=tavily` או `serper` עם `SEARCH_API_KEY` ב-`.env`.

**איפה הלוגים?**
`journalctl -u vortex-bot -f` מראה את הלוג החי. `systemctl status vortex-bot` מראה אם השירות רץ. אם הבוט נעצר, `sudo systemctl restart vortex-bot` מפעיל אותו שוב.

**הבוט אומר שהגעתי למגבלה היומית.**
כל משתמש מקבל 30 תשובות בוט ביום (הבוס פטור). המגבלה מתאפסת בחצות לפי אזור הזמן של מדינת הבוט. אפשר להגדיל אותה עם `DAILY_LIMIT_MESSAGES` ב-`.env`, או לבקש מהבוס.

**מצאתי באג / יש לי רעיון.**
בבקשה פתח issue ב-GitHub — ראה [CONTRIBUTING.md](CONTRIBUTING.md) איך לדווח עליו ואיך לשלוח תיקון.

## פיתוח

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

הרץ את הבדיקות (סקריפטי Python פשוטים, אין צורך ב-pytest):

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

כל תשע הסוויטות חייבות לעבור לפני שאתה פותח pull request. ראה [CONTRIBUTING.md](CONTRIBUTING.md) לסגנון הקוד (ruff) ולתהליך ה-PR.

## רישיון

Vortex מופץ תחת [רישיון MIT](LICENSE) — חופשי לשימוש, העתקה, שינוי ושיתוף, לכל מטרה.

<a id="countries"></a>

## מדינות

הדבק את שם המדינה **באנגלית, בדיוק כפי שמופיע כאן** כשהמתקין מבקש את המדינה שלך. הטבלה נוצרת מ-`bot/countries.py` — אם שם כאן ושם שם אי פעם לא מסכימים, `bot/countries.py` מנצח.

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

## תודה

> ⭐ **אנא תנו כוכב לפרויקט הזה ב-GitHub ועקבו אחרי [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — זו הדרך הפשוטה ביותר לתמוך ב-Vortex ולעזור לאחרים למצוא אותו. תודה!
