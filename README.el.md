# Vortex 🤖 — Ο δικός σας βοηθός ομάδας Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · **Ελληνικά** · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Αν σας αρέσει το Vortex, παρακαλώ βάλτε αστέρι σε αυτό το έργο στο GitHub και ακολουθήστε το [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — βοηθάει περισσότερους ανθρώπους να το βρουν. Ευχαριστούμε!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Τι είναι το Vortex;

Το Vortex είναι ένας bot του Telegram που ζει στις ομάδες και τις ιδιωτικές συνομιλίες σας και απαντάει στους ανθρώπους με ένα μοντέλο AI συνομιλίας. Λέτε το όνομά του (το προεπιλεγμένο όνομα είναι **Vortex**) και απαντάει — μπορεί να συνομιλήσει, να αναζητήσει στο διαδίκτυο, να φτιάξει εικόνες, να ελέγξει τιμές, να πει χistes, να διαβάσει αρχεία, να μετατρέψει φωνητικά μηνύματα σε κείμενο, και άλλα πολλά.

Τρέχει στον δικό σας server, στη δική σας χώρα και γλώσσα. Εσείς είστε ο αρχηγός: ένα κρυφό πάνελ `/admin` σας επιτρέπει να διαχειρίζεστε κλειδιά AI, χρήστες και ρυθμίσεις.

## Χαρακτηριστικά

- 💬 **AI συνομιλία** σε ομάδες (λέξη ξύπνησης) και ιδιωτικές συνομιλίες (δεν χρειάζεται λέξη ξύπνησης)
- 🔑 **Ποολ tokens** — χρησιμοποιήστε πολλούς παρόχους LLM και κλειδιά, περιστρέφετε και ανακατευθύνετε αυτόματα
- 🖼️ **Δημιουργία εικόνας** — με τη δική σας υπηρεσία εικόνας (βάση URL + κλειδί API + μοντέλο), προστίθεται στο `/admin`
- 🔍 **Αναζήτηση στο διαδίκτυο** — self-hosted SearXNG, με fallback στην Wikipedia
- 💰 **Ζωντανές τιμές** — νομίσματα, χρυσός, πετρέλαιο και crypto στο τοπικό σας νόμισμα
- 🕌 **Ωρές προσευχής**, 🃏 **τυχερά**, 😄 **χistes**, 🎲 **ζάρια και ρίψεις νομίσματος**
- 📎 **Ανάλυση αρχείων** και **μετάφραση φωνής**
- 📥 **Λήψεις** — στείλτε έναν σύνδεσμο, πάρτε πίσω το αρχείο πολυμέσων (μέχρι 45 MB)
- 🌍 **195 χώρες** και **40 γλώσσες** — χώρα και γλώσσα είναι ξεχωριστές ρυθμίσεις
- 🔄 **Αυτοενημέρωση** — ελέγχει για νέες εκδόσεις καθημερινά και ρωτάει πριν ενημερώσει
- 🛡️ **Κρυφό πάνελ /admin** — tokens, χρήστες, στατιστικά, συνομιλίες, μοντέλο εικόνας, διαχειριστές, ισχύς

## Πριν την εγκατάσταση

Χρειάζεστε έναν server (ή έναν υπολογιστή που μένει ανοιχτό) που τρέχει **Linux** με αυτά εγκατεστημένα:

| Τι | Πώς να ελέγξετε | Τι πρέπει να δείτε |
| --- | --- | --- |
| **Python 3.11 ή νεότερο** | `python3 --version` | `Python 3.11.x` ή ανώτερο (3.12 και 3.13 δουλεύουν επίσης) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` ή `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` ή παρόμοιο |
| **Docker** *(προαιρετικό)* | `docker --version` | `Docker version 2x.x.x` — χρειάζεται μόνο αν θέλετε την προαιρετική αναζήτηση SearXNG |

Αν λείπει κάτι, εγκαταστήστε τα πάντα με μία εντολή (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Για το προαιρετικό `Docker` (απαιτείται μόνο αν θέλετε την αναζήτηση στο διαδίκτυο με το `SearXNG`):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Μετά την τελευταία γραμμή, αποσυνδεθείτε και συνδεθείτε ξανά (ή τρέξτε εντολές `docker` με `sudo`). Το πρόγραμμα εγκατάστασης προσφέρει επίσης να εγκαταστήσει τα λείποντα εργαλεία για εσάς με το `apt` στο `Debian/Ubuntu`. Σε άλλα συστήματα, εγκαταστήστε τα πρώτα με τον διαχειριστή πακέτων σας. Το `systemd` έρχεται με το σύστημα — δεν μπορεί να εγκατασταθεί ξεχωριστά.

Χρειάζεστε επίσης δύο πράγματα από το Telegram (και τα δύο είναι δωρεάν):

1. **Ένα bot token** — μιλήστε στο [@BotFather](https://t.me/BotFather) στο Telegram, στείλτε `/newbot`, και αντιγράψτε το token που σας δίνει.
2. **Ο αριθμητικός σας Telegram user ID** — μιλήστε στο [@userinfobot](https://t.me/userinfobot) και αντιγράψτε τον αριθμό που σας δείχνει. Αυτό είναι το "boss" ID σας: μόνο αυτός ο λογαριασμός μπορεί να χρησιμοποιήσει το `/admin`.

## Εγκατάσταση

Μια εντολή. Αντιγράψτε την, επικολλήστε την στο τερματικό σας, και πατήστε Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Το πρόγραμμα εγκατάστασης σας ρωτάει έξι ερωτήσεις, με τη σειρά:

1. **Χώρα** — επικολλήστε το αγγλικό όνομα της χώρας σας **ακριβώς όπως εμφανίζεται στον [πίνακα χωρών](#countries) παρακάτω** (π.χ. `Turkey`). Η χώρα ορίζει τη ζώνη ώρας, το τοπικό νόμισμα για τις τιμές, τις ώρες προσευχής και το τοπικό περιεχόμενο.
2. **Γλώσσα** — η γλώσσα που μιλάει το bot (π.χ. `en`, `fa`, `tr`). Πατήστε Enter για να αποδεχτείτε την προεπιλεγμένη για τη χώρα σας. Η γλώσσα είναι ξεχωριστή από τη χώρα: αλλάζει μόνο αυτό που λέει το bot, και μπορείτε να την αλλάξετε αργότερα από το `/admin`.
3. **Token bot** — επικολλήστε το token από τον [@BotFather](https://t.me/BotFather). Το πρόγραμμα εγκατάστασης το ελέγχει ζωντανά με το Telegram.
4. **Αριθμητικό ID Boss** — το Telegram user ID σας από τον [@userinfobot](https://t.me/userinfobot).
5. **Όνομα bot / λέξη ξύπνηματος** — το όνομα που λένε οι άνθρωποι στις ομάδες για να μιλήσουν στο bot. Οποιαδήποτε γλώσσα είναι εντάξει (π.χ. `Vortex` ή `ورتکس`). Πατήστε Enter για την προεπιλεγμένη `Vortex`.
6. **Πρώτος πάροχος LLM** — επιλέξτε έναν: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, ή **Custom** (επικολλήστε ένα base URL). Στη συνέχεια επικολλήστε το API key σας για αυτόν τον πάροχο — το πρόγραμμα εγκατάστασης ανακτά τη ζωντανή λίστα μοντέλων του πάροχου και επιλέγετε ένα μοντέλο.

Στη συνέχεια το πρόγραμμα εγκατάστασης εγκαθιστά τις εξαρτήσεις, γράφει το αρχείο `.env`, δημιουργεί την υπηρεσία systemd `vortex-bot`, προτείνει να εγκαταστήσει το SearXNG για αναζήτηση στο διαδίκτυο (απαιτεί Docker), και ξεκινά το bot.

> ⚠️ **Το Anthropic δεν λειτουργεί απευθείας.** Το native API του Anthropic δεν είναι συμβατό με OpenAI, και αυτό το bot υποστηρίζει μόνο APIs συμβατά με OpenAI. Αν επιλέξετε Anthropic, το πρόγραμμα εγκατάστασης σας προειδοποιεί: το key λειτουργεί μόνο μέσω πύλης συμβατής με OpenAI. Χρησιμοποιήστε το OpenRouter, ή άλλον πάροχο από τη λίστα, αντί για αυτό.

## Μετά την εγκατάσταση

Ελέγξτε ότι το bot τρέχει:

```bash
systemctl status vortex-bot
```

Πρέπει να δείτε `active (running)`. Για να παρακολουθείτε το ζωντανό log:

```bash
journalctl -u vortex-bot -f
```

Τώρα ανοίξτε το Telegram και μιλήστε στο bot σας:

- Στείλτε `/start` — το bot χαιρετά.
- Σε **ιδιωτική συνομιλία**, απλά γράψτε του — δεν χρειάζεται λέξη ξύπνηματος.
- Σε μια **ομάδα**, προσθέστε το ρομπότ στην ομάδα, και απενεργοποιήστε την Ιδιωτικότητα Ομάδας: στον [@BotFather](https://t.me/BotFather) στείλτε `/setprivacy`, επιλέξτε το ρομπότ σας και επιλέξτε **Disable** — αλλιώς το ρομπότ δεν μπορεί να δει τα μηνύματα της ομάδας και δεν θα ακούσει τη λέξη ξύπνημά του. Στη συνέχεια πείτε το όνομά του, για παράδειγμα: `Vortex what's the time?`
- Ως boss, στείλτε `/admin` σε ιδιωτική συνομιλία για να ανοίξετε το κρυφό admin panel.

**Οι ενημερώσεις είναι αυτόματες.** Μια φορά την ημέρα το bot ελέγχει το GitHub για νέα έκδοση. Αν υπάρχει διαθέσιμη, σας στέλνει ιδιωτικό μήνυμα με κουμπιά ✅ / ❌. Πατήστε ✅ και ενημερώνεται μόνο του και κάνει restart — δεν χρειάζεται ποτέ να αγγίξετε τον server.

## Ρύθμιση

Όλες οι ρυθμίσεις βρίσκονται στο αρχείο `.env` στον φάκελο εγκατάστασης. Δείτε το [`.env.example`](.env.example) για κάθε επιλογή. Οι σημαντικότερες:

| Setting | Τι κάνει |
| --- | --- |
| `BOT_TOKEN` | Το token του Telegram bot σας (από τον @BotFather) |
| `BOSS_ID` | Ο αριθμητικός κωδικός χρήστη Telegram σας (ο ιδιοκτήτης του bot) |
| `BOT_NAME` | Το όνομα του bot και η λέξη ξύπνησης σε ομάδες (προεπιλογή `Vortex`) |
| `BOT_COUNTRY` | Χώρα στα Αγγλικά, π.χ. `United States` (ορίζει ζώνη ώρας, νόμισμα, ώρες προσευχής) |
| `BOT_LANGUAGE` | Κωδικός γλώσσας bot, π.χ. `en`, `fa`, `tr` (αλλάζει μόνο τι λέει το bot) |
| `LLM_PROVIDERS` | Παρόχοι LLM και κλειδιά: `base_url\|api_key\|model`, διαχωρισμένα με κόμμα |
| `UPDATE_CHECK_ENABLED` | `1` = έλεγχος ενημερώσεων καθημερινά, `0` = ποτέ |
| `UPDATE_REPO` | Το repo των releases που παρακολουθείται (προεπιλογή `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Αναζήτηση στο web: `searxng` (προεπιλογή), `tavily`, ή `serper` |
| `DAILY_LIMIT_MESSAGES` | Μέγιστα απαντήσεις bot ανά χρήστη ανά ημέρα (προεπιλογή `30`, ο boss είναι εξαιρεμένος) |

Η χώρα και η γλώσσα μπορούν να αλλάξουν αργότερα και από το κρυφό πάνελ `/admin` (Γλώσσα & Χώρα), χωρίς να επεξεργαστείτε κανένα αρχείο.

## Εναλλακτική με Docker

Αν προτιμάτε το Docker από τον installer:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Αυτό ξεκινά το bot μαζί με μια self-hosted μηχανή αναζήτησης SearXNG. Ελέγξτε τα logs με `docker compose logs -f bot`.

Σημείωση: ο αυτόματος self-updater χρειάζεται το systemd service, οπότε στο Docker οι ενημερώσεις είναι χειροκίνητες: `git pull` και μετά `docker compose up -d --build` ξανά.

## Λεπτομέρειες χαρακτηριστικών

### Το πάνελ /admin

Στείλτε `/admin` σε ιδιωτική συνομιλία (μόνο boss — κανείς άλλος δεν μπορεί να το ανοίξει, και δεν εμφανίζεται ποτέ στο `/help` ή στα μενού). Περιέχει:

- 🔑 **Tokens & model** — προσθήκη ή αφαίρεση κλειδιών LLM, δείτε ποια κλειδιά είναι υγιή, επιλέξτε το ενεργό model, περιηγηθείτε στη λίστα models ενός provider σε πραγματικό χρόνο
- 👥 **Users** — μετρήσεις χρηστών, ban / unban, allowlist
- 📊 **Stats** — αριθμούς χρήσης
- 💬 **Recent chats** — τι είπαν οι άνθρωποι στο bot (μόνο boss, ιδιωτικά)
- 🖼️ **Μοντέλο εικόνας** — η δική σας υπηρεσία εικόνας (βάση URL + κλειδί API + μοντέλο), ή απενεργοποιημένο
- 🛡️ **Managers** — δώστε πρόσβαση σε μέρη του πάνελ σε αξιόπιστους ανθρώπους
- 🟢/🔴 **Power** — ανάβετε ή σβήστε το bot για όλους (ο boss παραμένει στο timόνι)
- 🌍 **Language & Country** — αλλάξτε γλώσσα ή χώρα του bot οποιαδήποτε στιγμή

### Το pool tokens

Το bot μπορεί να κρατάει κλειδιά από πολλούς παρόχους LLM ταυτόχρονα. Κυκλώνει μεταξύ υγιών κλειδιών και κάνει failover αυτόματα όταν μια σταματάει να δουλεύει. Από το `/admin` μπορείτε να κλειδώσετε ένα model, να επιλέξετε model χειροκίνητα, ή να αφήσετε το bot να κυκλώνει ελεύθερα. Οποιοσδήποτε provider με OpenAI-compatible API δουλεύει — συμπεριλαμβανομένων μικρών aggregator, όχι μόνο τα μεγάλα ονόματα.

### Εικόνες

Η δημιουργία εικόνας χρησιμοποιεί τη δική σας υπηρεσία εικόνας συμβατή με OpenAI: προσθέστε τη βάση URL, το κλειδί API και το μοντέλο στο `/admin` (🖼️ **Μοντέλο εικόνας**). Δεν υπάρχει ενσωματωμένος πάροχος εικόνων, και η επεξεργασία φωτογραφιών δεν υποστηρίζεται. Η δημιουργία εικόνων μπορεί να απενεργοποιηθεί από το `/admin`.

### Χώρες και γλώσσες

Το Vortex υποστηρίζει **195 χώρες** και **40 γλώσσες**. Η χώρα ορίζει τη ζώνη ώρας, το νόμισμα στο οποίο εμφανίζονται οι τιμές, την πόλη που χρησιμοποιείται για τις ώρες προσευχής και το τοπικό περιεχόμενο. Η γλώσσα ορίζει μόνο τι λέει το bot — για παράδειγμα, μια ομάδα στο Βέλγιο μπορεί να χρησιμοποιήσει τη χώρα Βέλγιο και τη γλώσσα Αγγλικά. Και τα δύο μπορούν να αλλάξουν αργότερα από το `/admin`.

### Ενημερώσεις

Το bot ελέγχει τις εκδόσεις του GitHub του `VortexLabsHQ/vortex-telegram-bot` μια φορά την ημέρα. Όταν βγαίνει νέα έκδοση, στέλνει ιδιωτικό μήνυμα στον boss με κουμπιά ✅ / ❌. Η αποδοχή ενημερώνει τον κώδικα και ξανεκκινεί το bot. Ενώ το repo είναι ιδιωτικό, ο έλεγχος δεν κάνει τίποτα αθόρυβα (το API του GitHub χρειάζεται δημόσιο repo) — ορίστε `UPDATE_CHECK_ENABLED=0` αν δεν θέλετε ποτέ τον έλεγχο.

## Αντιμετώπιση προβλημάτων / Συχνές ερωτήσεις

**Ο εγκαταστάτης λέει ότι το token μου είναι άκυρο.**
Το token προέρχεται από το [@BotFather](https://t.me/BotFather). Βεβαιωθείτε ότι αντιγράψατε ολόκληρο το token (ψηφία, άνω κάτω τελεία, μετά 35+ χαρακτήρες), χωρίς περιττά κενά. Αν διαγράψατε το bot ή φτιάξατε νέο token, το παλιό σταματάει να δουλεύει — επικολλήστε το νέο.

**Το bot δεν απαντάει στην ομάδα μου.**
Τέσσερα πράγματα να ελέγξετε: (1) Η Ιδιωτικότητα Ομάδας πρέπει να είναι απενεργοποιημένη — στον [@BotFather](https://t.me/BotFather) στείλτε `/setprivacy`, επιλέξτε το ρομπότ σας και επιλέξτε **Disable**; με την ιδιωτικότητα ενεργοποιημένη, το ρομπότ δεν μπορεί να δει τα μηνύματα της ομάδας καθόλου, (2) το ρομπότ πρέπει να προστεθεί στην ομάδα, (3) πρέπει να πείτε τη λέξη ξύπνημά του — το όνομά του, για παράδειγμα `Vortex what's the time?` — το ρομπότ ακούει μόνο όταν λέγεται το όνομά του σε ομάδες, (4) σε ιδιωτική συζήτηση δεν χρειάζεται λέξη ξύπνημα καθόλου.

**Το bot απαντάει στα Αγγλικά, όχι στη γλώσσα μου.**
Στείλτε `/admin` (μόνο boss) → Γλώσσα & Χώρα, και επιλέξτε τη γλώσσα σας. Ο εγκαταστάτης ρωτάει επίσης για τη γλώσσα — πατήστε Enter εκεί για να αποδεχτείτε την προεπιλογή της χώρας σας.

**Επέλεξα Anthropic και το bot δεν συνομιλάει.**
Το native API του Anthropic δεν είναι συμβατό με OpenAI, οπότε το bot δεν μπορεί να συνομιλήσει με αυτό απευθείας. Χρησιμοποιήστε το OpenRouter (το οποίο μπορεί να εξυπηρετήσει μοντέλα Claude μέσω API συμβατού με OpenAI), ή επιλέξτε άλλο provider από τη λίστα.

**Η αναζήτηση στο web δεν δουλεύει.**
Η αναζήτηση στο web χρειάζεται το SearXNG, το οποίο ο εγκαταστάτης προσφέρει να ρυθμίσει με Docker. Χωρίς αυτό, το bot αναχωρεί στην Wikipedia, η οποία είναι πιο αδύναμη. Μπορείτε επίσης να ορίσετε `SEARCH_PROVIDER=tavily` ή `serper` με `SEARCH_API_KEY` στο `.env`.

**Πού είναι τα logs;**
`journalctl -u vortex-bot -f` εμφανίζει το live log. `systemctl status vortex-bot` δείχνει αν η υπηρεσία τρέχει. Αν το bot σταματήσει, `sudo systemctl restart vortex-bot` το ξανεκκινεί.

**Το bot λέει ότι φτάσαμε το καθημερινό όριο.**
Κάθε χρήστης παίρνει 30 απαντήσεις bot την ημέρα (ο boss είναι εξαιρεμένος). Το όριο μηδενίζεται τη μεσάνυχτα στη ζώνη ώρας της χώρας του bot. Αυξήστε το με `DAILY_LIMIT_MESSAGES` στο `.env`, ή ρωτήστε τον boss.

**Βρήκα ένα bug / Έχω μια ιδέα.**
Παρακαλώ ανοίξτε ένα issue στο GitHub — δείτε το [CONTRIBUTING.md](CONTRIBUTING.md) για το πώς να το αναφέρετε και πώς να στείλετε διόρθωση.

## Ανάπτυξη

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

Τρέξτε τα tests (απλά scripts Python, δεν χρειάζεται pytest):

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

Όλες οι εννέα σουίτες πρέπει να περάσουν πριν ανοίξετε pull request. Δείτε το [CONTRIBUTING.md](CONTRIBUTING.md) για το στυλ κώδικα (ruff) και τη διαδικασία PR.

## Άδεια

Το Vortex διανέμεται υπό την [MIT License](LICENSE) — ελεύθερο να χρησιμοποιηθεί, να αντιγραφεί, να αλλάξει και να μοιραστεί, για οποιονδήποτε σκοπό.

<a id="countries"></a>

## Χώρες

Επικολλήστε το όνομα της χώρας **στα Αγγλικά, ακριβώς όπως γράφεται εδώ** όταν το πρόγραμμα εγκατάστασης ζητάει τη χώρα σας. Ο πίνακας δημιουργείται από το `bot/countries.py` — αν ένα όνομα εδώ και ένα όνομα εκεί διαφωνούν ποτέ, το `bot/countries.py` νικάει.

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

## Ευχαριστίες

> ⭐ **Παρακαλώ βάλτε αστέρι σε αυτό το έργο στο GitHub και ακολουθήστε το [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — είναι ο απλούστερος τρόπος να υποστηρίξετε το Vortex και να βοηθήσετε άλλους να το βρουν. Ευχαριστώ!
