# Vortex 🤖 — Votre propre assistant de groupe Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · **Français** · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Si vous aimez Vortex, merci de mettre une étoile à ce projet sur GitHub et de suivre [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — cela aide d'autres personnes à le découvrir. Merci !

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Qu'est-ce que Vortex ?

Vortex est un bot Telegram qui vit dans vos groupes et discussions privées et répond aux gens avec un modèle d'IA conversationnel. Vous dites son nom (le nom par défaut est **Vortex**) et il répond — il peut discuter, chercher sur le web, créer des images, vérifier des prix, raconter des blagues, lire des fichiers, transcrire des messages vocaux, et plus encore.

Il tourne sur votre propre serveur, dans votre propre pays et votre propre langue. Vous êtes le patron : un panneau `/admin` caché vous permet de gérer les clés d'IA, les utilisateurs et les réglages.

## Fonctionnalités

- 💬 **Discussion IA** dans les groupes (mot de réveil) et en privé (pas de mot de réveil nécessaire)
- 🔑 **Pool de tokens** — utilisez plusieurs fournisseurs et clés LLM, rotation et basculement automatiques
- 🖼️ **Génération et édition d'images** — gratuit (DuckAI) ou fournisseurs payants
- 🔍 **Recherche web** — SearXNG auto-hébergé, avec Wikipédia en secours
- 💰 **Prix en direct** — devises, or, pétrole et crypto dans votre devise locale
- 🕌 **Heures de prière**, 🃏 **fortunes**, 😄 **blagues**, 🎲 **dés et pile ou face**
- 📎 **Analyse de fichiers** et **transcription vocale**
- 📥 **Téléchargements** — envoyez un lien, récupérez le fichier média (jusqu'à 45 Mo)
- 🌍 **195 pays** et **40 langues** — le pays et la langue sont des réglages séparés
- 🔄 **Auto-mise à jour** — vérifie les nouvelles versions chaque jour et demande avant de mettre à jour
- 🛡️ **Panneau /admin caché** — tokens, utilisateurs, stats, discussions, modèle d'image, gestionnaires, marche/arrêt

## Avant d'installer

Il vous faut un serveur (ou un ordinateur qui reste allumé) sous **Linux** avec ces éléments installés :

| Quoi | Comment vérifier | Ce que vous devriez voir |
| --- | --- | --- |
| **Python 3.11 ou plus récent** | `python3 --version` | `Python 3.11.x` ou plus récent (3.12 et 3.13 fonctionnent aussi) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` ou `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` ou similaire |
| **Docker** *(optionnel)* | `docker --version` | `Docker version 2x.x.x` — seulement nécessaire si vous voulez la recherche web SearXNG optionnelle |

Si quelque chose manque, l'installeur propose de l'installer pour vous avec `apt` (sur Debian/Ubuntu). Sur d'autres systèmes, installez-le d'abord avec votre gestionnaire de paquets.

Il vous faut aussi deux choses de Telegram (les deux sont gratuites) :

1. **Un token de bot** — parlez à [@BotFather](https://t.me/BotFather) sur Telegram, envoyez `/newbot`, et copiez le token qu'il vous donne.
2. **Votre ID utilisateur Telegram numérique** — parlez à [@userinfobot](https://t.me/userinfobot) et copiez le nombre qu'il affiche. C'est votre ID « patron » : seul ce compte peut utiliser `/admin`.

## Installation

Une seule commande. Copiez-la, collez-la dans votre terminal, et appuyez sur Entrée :

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

L'installeur vous pose six questions, dans l'ordre :

1. **Pays** — collez le nom anglais de votre pays **exactement comme listé dans le [tableau des pays](#countries) ci-dessous** (par exemple `Turkey`). Le pays définit le fuseau horaire, la devise locale pour les prix, les heures de prière, et le contenu local.
2. **Langue** — la langue que parle le bot (par exemple `en`, `fa`, `tr`). Appuyez sur Entrée pour accepter la valeur par défaut de votre pays. La langue est séparée du pays : elle ne change que ce que dit le bot, et vous pouvez la changer plus tard depuis `/admin`.
3. **Token du bot** — collez le token de [@BotFather](https://t.me/BotFather). L'installeur le vérifie en direct avec Telegram.
4. **ID numérique du patron** — votre ID utilisateur Telegram de [@userinfobot](https://t.me/userinfobot).
5. **Nom du bot / mot de réveil** — le nom que les gens disent dans les groupes pour parler au bot. Toute langue convient (par exemple `Vortex` ou `ورتکس`). Appuyez sur Entrée pour la valeur par défaut `Vortex`.
6. **Premier fournisseur LLM** — choisissez-en un : OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, ou **Personnalisé** (collez une URL de base). Puis collez votre clé API pour ce fournisseur — l'installeur récupère la liste des modèles en direct du fournisseur et vous en choisissez un.

Ensuite l'installeur installe les dépendances, écrit le fichier `.env`, crée le service systemd `vortex-bot`, propose d'installer SearXNG pour la recherche web (nécessite Docker), et démarre le bot.

> ⚠️ **Anthropic ne fonctionne pas directement.** L'API native d'Anthropic n'est pas compatible OpenAI, et ce bot ne parle que des API compatibles OpenAI. Si vous choisissez Anthropic, l'installeur vous avertit : la clé ne fonctionne que via une passerelle compatible OpenAI. Utilisez OpenRouter, ou un autre fournisseur de la liste, à la place.

## Après l'installation

Vérifiez que le bot tourne :

```bash
systemctl status vortex-bot
```

Vous devriez voir `active (running)`. Pour suivre le journal en direct :

```bash
journalctl -u vortex-bot -f
```

Ouvrez maintenant Telegram et parlez à votre bot :

- Envoyez `/start` — le bot dit bonjour.
- En **discussion privée**, écrivez-lui simplement — pas de mot de réveil nécessaire.
- Dans un **groupe**, ajoutez le bot au groupe, puis dites son nom, par exemple : `Vortex quelle heure est-il ?`
- En tant que patron, envoyez `/admin` en discussion privée pour ouvrir le panneau d'administration caché.

**Les mises à jour sont automatiques.** Une fois par jour, le bot vérifie sur GitHub s'il y a une nouvelle version. Si c'est le cas, il vous envoie un message privé avec des boutons ✅ / ❌. Appuyez sur ✅ et il se met à jour et redémarre tout seul — vous n'avez jamais besoin de toucher au serveur.

## Configuration

Tous les réglages sont dans le fichier `.env` du dossier d'installation. Voir [`.env.example`](.env.example) pour toutes les options. Les plus importantes :

| Réglage | Ce qu'il fait |
| --- | --- |
| `BOT_TOKEN` | Votre token de bot Telegram (de @BotFather) |
| `BOSS_ID` | Votre ID utilisateur Telegram numérique (le propriétaire du bot) |
| `BOT_NAME` | Le nom du bot et son mot de réveil dans les groupes (défaut `Vortex`) |
| `BOT_COUNTRY` | Pays en anglais, ex. `United States` (définit fuseau horaire, devise, heures de prière) |
| `BOT_LANGUAGE` | Code de langue du bot, ex. `en`, `fa`, `tr` (ne change que ce que dit le bot) |
| `LLM_PROVIDERS` | Fournisseurs et clés LLM : `base_url\|api_key\|model`, séparés par des virgules |
| `UPDATE_CHECK_ENABLED` | `1` = vérifier les mises à jour chaque jour, `0` = ne jamais vérifier |
| `UPDATE_REPO` | Le dépôt dont les versions sont surveillées (défaut `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Recherche web : `searxng` (défaut), `tavily`, ou `serper` |
| `DAILY_LIMIT_MESSAGES` | Max réponses du bot par utilisateur par jour (défaut `30`, le patron est exempt) |

Le pays et la langue peuvent aussi être changés plus tard depuis le panneau `/admin` caché (Langue & Pays), sans éditer aucun fichier.

## Alternative Docker

Si vous préférez Docker à l'installeur :

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Cela démarre le bot avec un moteur de recherche SearXNG auto-hébergé. Consultez les logs avec `docker compose logs -f bot`.

Note : le système de mise à jour automatique a besoin du service systemd, donc en Docker les mises à jour sont manuelles : `git pull` puis `docker compose up -d --build` à nouveau.

## Fonctionnalités en détail

### Le panneau /admin

Envoyez `/admin` en discussion privée (patron seulement — personne d'autre ne peut l'ouvrir, et il n'apparaît jamais dans `/help` ni les menus). Il contient :

- 🔑 **Tokens & modèle** — ajoutez ou supprimez des clés LLM, voyez quelles clés sont saines, choisissez le modèle actif, parcourez la liste des modèles en direct d'un fournisseur
- 👥 **Utilisateurs** — compteurs, bannir / débannir, liste d'autorisation
- 📊 **Stats** — chiffres d'utilisation
- 💬 **Discussions récentes** — ce que les gens ont dit au bot (patron seulement, privé)
- 🖼️ **Modèle d'image** — DuckAI (gratuit, défaut), HiLinkUp, un service d'image personnalisé, ou désactivé
- 🛡️ **Gestionnaires** — donnez à des gens de confiance l'accès à certaines parties du panneau
- 🟢/🔴 **Marche/Arrêt** — activez ou désactivez le bot pour tout le monde (le patron garde le contrôle)
- 🌍 **Langue & Pays** — changez la langue ou le pays du bot à tout moment

### Le pool de tokens

Le bot peut garder des clés de plusieurs fournisseurs LLM à la fois. Il alterne entre les clés saines et bascule automatiquement quand l'une ne marche plus. Depuis `/admin` vous pouvez épingler un modèle, en choisir un à la main, ou laisser le bot alterner librement. Tout fournisseur avec une API compatible OpenAI fonctionne — y compris les petits agrégateurs, pas seulement les grands noms.

### Images

La génération d'images a trois modes : **DuckAI** (gratuit, pas de clé, défaut), **HiLinkUp** (payant, meilleure qualité), ou un service d'image **personnalisé** compatible OpenAI. Vous pouvez aussi envoyer une photo au bot et lui dire comment la modifier (« rends ça style dessin animé »), et il générera une nouvelle image. La génération d'images est désactivable depuis `/admin`.

### Pays et langues

Vortex gère **195 pays** et **40 langues**. Le pays définit le fuseau horaire, la devise dans laquelle les prix sont affichés, la ville utilisée pour les heures de prière, et le contenu local. La langue ne définit que ce que dit le bot — un groupe en Belgique peut utiliser le pays Belgique et la langue Anglais, par exemple. Les deux peuvent être changés plus tard depuis `/admin`.

### Mises à jour

Le bot vérifie les versions GitHub de `VortexLabsHQ/vortex-telegram-bot` une fois par jour. Quand une nouvelle version sort, il envoie un message privé au patron avec des boutons ✅ / ❌. Accepter met à jour le code et redémarre le bot. Tant que le dépôt est privé, la vérification ne fait rien silencieusement (l'API GitHub a besoin d'un dépôt public) — mettez `UPDATE_CHECK_ENABLED=0` si vous ne voulez jamais la vérification.

## Dépannage / FAQ

**L'installeur dit que mon token est invalide.**
Le token vient de [@BotFather](https://t.me/BotFather). Assurez-vous d'avoir copié tout le token (chiffres, deux-points, puis 35+ caractères), sans espaces en trop. Si vous avez supprimé le bot ou créé un nouveau token, l'ancien ne marche plus — collez le nouveau.

**Le bot ne répond pas dans mon groupe.**
Trois choses à vérifier : (1) le bot doit être ajouté au groupe, (2) vous devez dire son mot de réveil — son nom, par exemple `Vortex quelle heure est-il ?` — le bot n'écoute que quand son nom est dit dans les groupes, (3) en discussion privée aucun mot de réveil n'est nécessaire.

**Le bot répond en anglais, pas dans ma langue.**
Envoyez `/admin` (patron seulement) → Langue & Pays, et choisissez votre langue. L'installeur demande aussi la langue — appuyez sur Entrée là pour accepter la valeur par défaut de votre pays.

**J'ai choisi Anthropic et le bot ne discute pas.**
L'API native d'Anthropic n'est pas compatible OpenAI, donc le bot ne peut pas discuter avec directement. Utilisez OpenRouter (qui peut servir les modèles Claude via une API compatible OpenAI), ou choisissez un autre fournisseur de la liste.

**La recherche web ne marche pas.**
La recherche web a besoin de SearXNG, que l'installeur propose de configurer avec Docker. Sans, le bot se rabat sur Wikipédia, qui est plus faible. Vous pouvez aussi mettre `SEARCH_PROVIDER=tavily` ou `serper` avec une `SEARCH_API_KEY` dans `.env`.

**Où sont les logs ?**
`journalctl -u vortex-bot -f` montre le journal en direct. `systemctl status vortex-bot` montre si le service tourne. Si le bot s'arrête, `sudo systemctl restart vortex-bot` le redémarre.

**Le bot dit que j'ai atteint la limite quotidienne.**
Chaque utilisateur a droit à 30 réponses du bot par jour (le patron est exempt). La limite se remet à zéro à minuit dans le fuseau horaire du pays du bot. Augmentez-la avec `DAILY_LIMIT_MESSAGES` dans `.env`, ou demandez au patron.

**J'ai trouvé un bug / J'ai une idée.**
Merci d'ouvrir une issue sur GitHub — voir [CONTRIBUTING.md](CONTRIBUTING.md) pour comment la signaler et comment envoyer une correction.

## Développement

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

Lancez les tests (scripts Python simples, pas besoin de pytest) :

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

Les neuf suites doivent passer avant d'ouvrir une pull request. Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour le style de code (ruff) et le processus de PR.

## Licence

Vortex est publié sous [Licence MIT](LICENSE) — libre d'utilisation, de copie, de modification et de partage, pour tout usage.

<a id="countries"></a>

## Pays

Collez le nom du pays **en anglais, exactement comme écrit ici** quand l'installeur demande votre pays. Le tableau est généré depuis `bot/countries.py` — si un nom ici et un nom là sont en désaccord, `bot/countries.py` gagne.

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



## Merci

> ⭐ **Merci de mettre une étoile à ce projet sur GitHub et de suivre [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — c'est la façon la plus simple de soutenir Vortex et d'aider d'autres à le trouver. Merci !